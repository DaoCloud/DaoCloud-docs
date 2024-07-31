---
MTPE: windsonsea
Date: 2024-07-30
---

# How to Add Heterogeneous Nodes to a Worker Cluster

This page explains how to add ARM architecture nodes with Kylin v10 sp2 operating system
to an AMD architecture worker cluster with CentOS 7.9 operating system.

!!! note

    This page is only applicable to adding heterogeneous nodes to a worker cluster created
    using the DCE 5.0 platform in offline mode, excluding connected clusters.

## Prerequisites

- A DCE 5.0 Full Mode deployment has been successfully completed, and the bootstrap node is still alive.
  Refer to the documentation [Offline Installation of DCE 5.0 Enterprise](../../install/commercial/start-install.md) for the deployment process.
- A worker cluster with AMD architecture and CentOS 7.9 operating system has been created through the
  DCE 5.0 platform. Refer to the documentation
  [Creating a Worker Cluster](../user-guide/clusters/create-cluster.md) for the creation process.

## Procedure

### Download and Import Offline Packages

Take ARM architecture and Kylin v10 sp2 operating system as examples.

Make sure you are logged into the bootstrap node! Also, make sure the
__clusterConfig.yaml__ file used during the DCE 5.0 deployment is available.

#### Offline Image Package

!!! note

    The latest version can be downloaded from the [Download Center](https://docs.daocloud.io/download/dce5/).

| CPU Architecture | Version | Download Link |
| :--------------- | :------ | :------------ |
| AMD64 | v0.18.0 | <https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.18.0-amd64.tar> |
| ARM64 | v0.18.0 | <https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.18.0-arm64.tar> |

After downloading, extract the offline package:

```bash
tar -xvf offline-v0.18.0-arm64.tar
```

#### ISO Offline Package (Kylin v10 sp2)

| CPU Architecture | Operating System Version | Download Link |
| :--------------- | :----------------------- | :------------ |
| ARM64 | Kylin Linux Advanced Server release V10 (Sword) SP2 | <https://www.kylinos.cn/support/trial.html> |

!!! note

    Kylin operating system requires personal information to be provided for downloading and usage. Select V10 (Sword) SP2 when downloading.

#### osPackage Offline Package (Kylin v10 sp2)

The [Kubean](https://github.com/kubean-io/kubean) project provides osPackage offline packages
for different operating systems. Visit <https://github.com/kubean-io/kubean/releases> to view the available packages.

| Operating System Version | Download Link |
| :----------------------- | :------------ |
| Kylin Linux Advanced Server release V10 (Sword) SP2 | <https://github.com/kubean-io/kubean/releases/download/v0.16.3/os-pkgs-kylinv10-v0.16.3.tar.gz> |

!!! note

    Check the specific version of the osPackage offline package in the
    __offline/sample/clusterConfig.yaml__ file of the offline image package.

#### Import Offline Packages to the Bootstrap Node

Run the import-artifact command:

```bash
./offline/dce5-installer import-artifact -c clusterConfig.yaml \
    --offline-path=/root/offline \
    --iso-path=/root/Kylin-Server-10-SP2-aarch64-Release-Build09-20210524.iso \
    --os-pkgs-path=/root/os-pkgs-kylinv10-v0.7.4.tar.gz
```

!!! note

    Parameter Explanation:

    - __-c clusterConfig.yaml__ specifies the clusterConfig.yaml file used during the previous DCE 5.0 deployment.
    - __--offline-path__ specifies the file path of the downloaded offline image package.
    - __--iso-path__ specifies the file path of the downloaded ISO operating system image.
    - __--os-pkgs-path__ specifies the file path of the downloaded osPackage offline package.

After a successful import command execution, the offline package will be uploaded to Minio on the bootstrap node.

### Add Heterogeneous Worker Nodes

!!! note

    If the version of DCE 5.0 you have installed is higher than (inclusive of)
    [DCE5.0-20230731](../../dce/dce-rn/20230731.md), after completing the above steps,
    you can directly integrate nodes via UI; if not, you will need to continue with
    the following steps to integrate heterogeneous nodes.

Make sure you are logged into the management node of the DCE 5.0
[Global Service Cluster](../user-guide/clusters/cluster-role.md#global-service-cluster).

#### Modify the Host Manifest

Here is an example of host manifest:

=== "Before adding a node"

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: ${cluster-name}-hosts-conf
      namespace: kubean-system
    data:
      hosts.yml: |
        all:
          children:
            etcd:
              hosts:
                centos-master:
            k8s_cluster:
              children:
                kube_control_plane:
                kube_node:
            kube_control_plane:
              hosts:
                centos-master:
            kube_node:
              hosts:
                centos-master:
        hosts:
          centos-master:
            ip: 10.5.14.122
            access_ip: 10.5.14.122
            ansible_host: 10.5.14.122
            ansible_connection: ssh
            ansible_user: root
            ansible_ssh_pass: ******
    ```

=== "After adding a node"

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: ${cluster-name}-hosts-conf
      namespace: kubean-system
    data:
      hosts.yml: |
        all:
          hosts:
            centos-master:
              ip: 10.5.14.122
              access_ip: 10.5.14.122
              ansible_host: 10.5.14.122
              ansible_connection: ssh
              ansible_user: root
              ansible_ssh_pass: ******
              # Add heterogeneous nodes
            kylin-worker:
              ip: 10.5.10.220
              access_ip: 10.5.10.220
              ansible_host: 10.5.10.220
              ansible_connection: ssh
              ansible_user: root
              ansible_ssh_pass: dangerous@2022
            children:
              kube_control_plane:
                hosts:
                  - centos-master
              kube_node:
                hosts:
                  - centos-master
                  - kylin-worker  # Add the name of heterogeneous node
              etcd:
                hosts:
                  - centos-master
              k8s_cluster:
                children:
                  - kube_control_plane
                  - kube_node
    ```

To add information about the newly added worker nodes according to the above comments:

```shell
kubectl edit cm ${cluster-name}-hosts-conf -n kubean-system
```

#### Add Expansion Tasks through ClusterOperation.yml

Example:

```yaml title="ClusterOperation.yml"
apiVersion: kubean.io/v1alpha1
kind: ClusterOperation
metadata:
  name: add-worker-node
spec:
  cluster: ${cluster-name} # Specify cluster name
  image: ghcr.m.daocloud.io/kubean-io/spray-job:v0.5.0
  backoffLimit: 0
  actionType: playbook
  action: scale.yml
  extraArgs: --limit=kylin-worker
  preHook:
    - actionType: playbook
      action: ping.yml
    - actionType: playbook
      action: disable-firewalld.yml
    - actionType: playbook
      action: enable-repo.yml
      extraArgs: |
        -e "{repo_list: ["http://10.5.14.30:9000/kubean/kylin-iso/\$releasever/os/\$basearch","http://10.5.14.30:9000/kubean/kylin/\$releasever/os/\$basearch"]}"
  postHook:
    - actionType: playbook
      action: cluster-info.yml
```

!!! note

    - Ensure the __spec.image__ image address matches the image used in the previous deployment job.
    - Set __spec.action__ to __scale.yml__ .
    - Set __spec.extraArgs__ to __--limit=g-worker__ .
    - Fill in the correct __repo_list__ parameter for the relevant OS in __spec.preHook__ 's __enable-repo.yml__ script.

To create and deploy __join-node-ops.yaml__ according to the above configuration:

```shell
vi join-node-ops.yaml
kubectl apply -f join-node-ops.yaml -n kubean-system
```

#### Check the status of the task execution

```shell
kubectl -n kubean-system get pod | grep add-worker-node
```

To check the progress of the scaling task, you can view the logs of the corresponding pod.

### Verify in UI

1. Go to __Container Management__ -> __Clusters__ -> __Nodes__ .

    <!-- Add image later -->

2. Click the newly added node to view details.

    <!-- Add image later -->
