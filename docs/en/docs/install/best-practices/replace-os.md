# Migrate Cluster Operating System without Downtime

## Background

A customer has deployed a DCE 5.0 worker cluster in a production environment on CentOS 7.9.
However, since [CentOS 7.9 will no longer be maintained](https://www.redhat.com/en/topics/linux/centos-linux-eol),
the customer wants to migrate their operating system to Ubuntu 22.04. As this is a production environment,
the customer wants to migrate from CentOS 7.9 to Ubuntu 22.04 without any downtime.

## Risks

- Normally, the best practice for migrating Kubernetes nodes is add-before-remove.
  However, the customer requires that node IPs do not change. Therefore,
  the migration sequence needs to be adjusted to remove-before-add.
  This change in sequence could reduce the cluster's fault tolerance and stability,
  so it should be handled with caution.

- In the process of remove-before-add, resources from the original node will migrate to other nodes.
  Ensure that other nodes have sufficient resources and pods, or the migration will fail.
  
    - Pods per node (`kubelet_max_pods`) is up to 110 by default.
      If your migration might exceed this limit, it is recomended to update the limit on all nodes in advance.
    - In the process of the node removal, if some services are fixed on the node being removed or
      traffic directed to pods on the node being removed, your business may be interrupted about 2-3 seconds.

## Solution

- The migration needs to be handled from both Master and Worker nodes.
- The sequence to migrate: [Migrate Worker Nodes](#migrate-worker-nodes) ->
  [Migrate nodes other then master1](#migrate-nodes-other-than-master1) -> [Migrate master1](#migrate-master1).
- Before migrating any node, it is recommended to back up your cluster data for security.

!!! note

    This document assumes a remove-before-add sequence.
    You can adjust the operation sequence as needed based on your actual scenarios.

### Prepare offline resources (skip if online)

1. Use the installer command to import the
   [iso](../commercial/start-install.md#iso-operating-system-image-file-required)
   and [ospackage](../commercial/start-install.md#ospackage-offline-packages-required) files for Ubuntu 22.04:

    ```shell
    dce5-installer import-artifact \
        --os-pkgs-path=/home/airgap/os-pkgs-ubuntu2204-v0.16.0.tar.gz \
        --iso-path=/home/iso/ubuntu-22.04.4-live-server-amd64.iso
    ```

2. Configure offline source of Ubuntu 22.04
   (`--limit` is used to restrict the YAML to only be applied to specified nodes):

    ```yaml
    apiVersion: kubean.io/v1alpha1
    kind: ClusterOperation
    metadata:
      name: cluster-ops-test
    spec:
      cluster: sample
      image: ghcr.io/kubean-io/spray-job:latest
      actionType: playbook
      action: scale.yml
      preHook:
        - actionType: playbook
          action: ping.yml
        - actionType: playbook
          action: enable-repo.yml  # (1)!
          extraArgs: |
            --limit=ubuntu-worker1 -e "{repo_list: ['deb [trusted=yes] http://MINIO_ADDR:9000/kubean/ubuntu jammy main', 'deb [trusted=yes] http://MINIO_ADDR:9000/kubean/ubuntu-iso jammy main restricted']}"

        - actionType: playbook
          action: disable-firewalld.yml
    ```

    1. Before running the task, run the enable-repo playbook to create the specified URL for each node.

### Migrate worker nodes

1. Enter the details page of the worker cluster, and in **Clusters** -> **Advanced Settings** ,
   disable **Cluster Deletion Protection** .

2. In the **Nodes** list, select a worker node and click **Remove** .

3. After successful removal, connect to the
   [Global Service Cluster](../../kpanda/user-guide/clusters/cluster-role.md#global-service-cluster)
   via terminal or command line and get the `hosts-conf` argument under the `clusters.kubean.io` resource type
for the worker cluster named <worker-cluster-name>. In this example, the worker cluster name is `centos`.

    ```shell
    # Get hosts-conf argument
    $ kubectl get clusters.kubean.io centos -o=jsonpath="{.spec.hostsConfRef}{'\n'}"

    {"name":"centos-hosts-conf","namespace":"kubean-system"}
    ```

4. In the **Nodes** list, click **Add Node** to re-add the previously removed node.

5. After the new node is successfully added, repeat the above steps for the other worker nodes until all migrations are complete.

### Migrate master nodes

The process of migrating master nodes can be divided into two steps:

- Migrate master1
- Migrate nodes other than master1

#### Identify master1

Check the `clusters.kubean.io` `host-conf` content for the cluster, specifically `all.children.kube_control_plane.hosts`.
The node listed first in the `kube_control_plane` section is the master1 node.

```yaml
      children:
        kube_control_plane:
          hosts:
            centos-master1: null # (1)!
            centos-master2: null
            centos-master3: null
```

1. Primary master node

#### Migrate nodes other than master1

1. Connect to the global service cluster via terminal or command line and get the `hosts-conf` and `vars-conf` arguments
   under the `clusters.kubean.io` resource for the worker cluster named <worker cluster name>.
   In this example, the worker cluster name is `centos`.

    ```shell
    # Get hosts-conf argument
    $ kubectl get clusters.kubean.io centos -o=jsonpath="{.spec.hostsConfRef}{'\n'}"

    {"name":"centos-hosts-conf","namespace":"kubean-system"}

    # Get vars-conf argument
    $ kubectl get clusters.kubean.io centos -o=jsonpath="{.spec.varsConfRef}{'\n'}"

    {"name":"centos-vars-conf","namespace":"kubean-system"}
    ```

2. Create a ConfigMap to clean up the kube-apiserver task. The YAML file is as follows:

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: pb-clean-kube-apiserver
      namespace: kubean-system
    data:
      clean-kube-apiserver.yml: |
        - name: Clean kube-apiserver
          hosts: "{{ node | default('kube_node') }}"
          gather_facts: no
          tasks:
            - name: Kill kube-apiserver process
              shell: ps -eopid=,comm= | awk '$2=="kube-apiserver" {print $1}' | xargs -r kill -9
    ```

3. After deploying the above YAMl file, create a ClusterOperation for the master node removal. The YAML file is as follows:

    ```yaml
    apiVersion: kubean.io/v1alpha1
    kind: ClusterOperation
    metadata:
      name: cluster-remove-master2
    spec:
      cluster: centos # (1)!
      image: ghcr.io/kubean-io/spray-job:v0.12.2 # (2)!
      actionType: playbook
      action: remove-node.yml
      extraArgs: -e node=centos-master2 # (3)!
      postHook:
        - actionType: playbook
          actionSource: configmap
          actionSourceRef:
            name: pb-clean-kube-apiserver
            namespace: kubean-system
          action: clean-kube-apiserver.yml
        - actionType: playbook
          action: cluster-info.yml
    ```

    1. Worker cluster name
    2. Specify the image for running the Kubean task.
       The image address should match the one used in the previous deployment job.
    3. Define this as any non-master1 node.

4. After deploying the above YAML file and waiting for the node to be successfully removed,
   create a ClusterOperation resource for the master node addition. The YAML file is as follows:

    ```yaml
    apiVersion: kubean.io/v1alpha1
    kind: ClusterOperation
    metadata:
      name: cluster-scale-master2
    spec:
      cluster: centos # (1)!
      image: ghcr.io/kubean-io/spray-job:v0.12.2 # (2)!
      actionType: playbook
      action: cluster.yml
      extraArgs: --limit=etcd,kube_control_plane -e ignore_assert_errors=yes --skip-tags=multus
      preHook:
        - actionType: playbook
          action: disable-firewalld.yml
      postHook:
        - actionType: playbook
          action: upgrade-cluster.yml
          extraArgs: --limit=etcd,kube_control_plane -e ignore_assert_errors=yes
        - actionType: playbook
          action: cluster-info.yml
    ```

    1. Worker cluster name
    2. Specify the image for running the Kubean task.
       The image address should match the one used in the previous deployment job.

5. After deploying the above file and waiting for the node to be successfully added back,
   repeat steps 3 and 4 to complete the migration of the third node.

#### Migrate master1

Refer to [Migrating the Master Node of Worker Cluster](../../kpanda/best-practice/replace-first-master-node.md).

1. Update the kubeconfig of the worker cluster in the management cluster, and log in to the second node via terminal.

2. Update the ConfigMap `centos-hosts-conf`, adjusting the order of master nodes in `kube_control_plane`,
   `kube_node`, and `etcd` (for example: node1/node2/node3 -> node2/node3/node1):

    === "Before change"

        ```yaml
            children:
              kube_control_plane:
                hosts:
                  centos-master1: null 
                  centos-master2: null
                  centos-master3: null
              kube_node:
                hosts:
                  centos-master1: null 
                  centos-master2: null
                  centos-master3: null
              etcd:
                hosts:
                  centos-master1: null 
                  centos-master2: null
                  centos-master3: null
        ```

    === "After change"

        ```yaml
            children:
              kube_control_plane:
                hosts:
                  centos-master2: null
                  centos-master3: null 
                  centos-master1: null
              kube_node:
                hosts:
                  centos-master2: null
                  centos-master3: null 
                  centos-master1: null
              etcd:
                hosts:
                  centos-master2: null
                  centos-master3: null 
                  centos-master1: null
        ```

3. Create a ClusterOperation for the master1 node removal. The YAML file is as follows:

    ```yaml
    apiVersion: kubean.io/v1alpha1
    kind: ClusterOperation
    metadata:
      name: cluster-test-remove-master1
    spec:
      cluster: centos  # (1)!
      image: ghcr.io/kubean-io/spray-job:v0.12.2 # (2)!
      actionType: playbook
      action: remove-node.yml
      extraArgs: -e node=centos-master1 # (3)!
      postHook:
        - actionType: playbook
          actionSource: configmap
          actionSourceRef:
            name: pb-clean-kube-apiserver
            namespace: kubean-system
          action: clean-kube-apiserver.yml
        - actionType: playbook
          action: cluster-info.yml
    ```

    1. Worker cluster name
    2. Specify the image for running the Kubean task.
       The image address should match the one used in the previous deployment job.
    3. Define this as the master1 node.

4. After deploying the above YAML file and successful removal, update the ConfigMap `cluster-info` and `kubeadm-config`.

    ```shell
    # Edit cluster-info
    kubectl -n kube-public edit cm cluster-info

    # 1. If the ca.crt certificate is updated, update the certificate-authority-data field.
    # View the base64 encoding of the ca certificate:
    cat /etc/kubernetes/ssl/ca.crt | base64 | tr -d '\n'

    # 2. Modify the server field's IP address to the second Master IP.
    ```

    ```shell
    # Edit kubeadm-config
    kubectl -n kube-system edit cm kubeadm-config

    # Modify controlPlaneEndpoint to the second Master IP
    ```

5. Create a ClusterOperation for the master1 node addition. The YAML file is as follows:

    ```yaml
    apiVersion: kubean.io/v1alpha1
    kind: ClusterOperation
    metadata:
      name: cluster-test-scale-master1
    spec:
      cluster: centos # (1)!
      image: ghcr.io/kubean-io/spray-job:v0.12.2 # (2)!
      actionType: playbook
      action: cluster.yml
      extraArgs: --limit=etcd,kube_control_plane -e ignore_assert_errors=yes --skip-tags=multus
      preHook:
        - actionType: playbook
          action: disable-firewalld.yml
      postHook:
        - actionType: playbook
          action: upgrade-cluster.yml
          extraArgs: --limit=etcd,kube_control_plane -e ignore_assert_errors=yes
        - actionType: playbook
          action: cluster-info.yml
    ```

    1. Worker cluster name
    2. Specify the image for running the Kubean task.
       The image address should match the one used in the previous deployment job.

6. Once the addition task is complete, the migration of the master1 node is successfully completed.
