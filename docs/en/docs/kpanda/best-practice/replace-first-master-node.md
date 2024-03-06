# Replace the first master node of the worker cluster

This page will take a highly available three-master-node worker cluster as an example.
When the first master node of the worker cluster fails or malfunctions,
how to replace or reintroduce the first master node.

This page features a highly available cluster with three master nodes.

- node1 (172.30.41.161)
- node2 (172.30.41.162)
- node3 (172.30.41.163)

Assuming node1 is down, the following steps will explain how to reintroduce the
recovered node1 back into the worker cluster.

## Preparations

Before performing the replacement operation, first obtain basic information about the cluster resources,
which will be used when modifying related configurations.

!!! note

    The following commands to obtain cluster resource information are executed in the management cluster.

1. Get the cluster name

    Execute the following command to find the clusters.kubean.io resource corresponding to the cluster:

    ```shell
    # For example, if the resource name of clusters.kubean.io is cluster-mini-1
    # Get the name of the cluster
    CLUSTER_NAME=$(kubectl get clusters.kubean.io cluster-mini-1 -o=jsonpath="{.metadata.name}{'\n'}")
    ```

1. Get the host list configmap of the cluster

    ```shell
    kubectl get clusters.kubean.io cluster-mini-1 -o=jsonpath="{.spec.hostsConfRef}{'\n'}"
    {"name":"mini-1-hosts-conf","namespace":"kubean-system"}
    ```

1. Get the configuration parameters configmap of the cluster

    ```shell
    kubectl get clusters.kubean.io cluster-mini-1 -o=jsonpath="{.spec.varsConfRef}{'\n'}"
    {"name":"mini-1-vars-conf","namespace":"kubean-system"}
    ```

## Steps

1. Adjust the order of control plane nodes

    Reset the node1 node to restore it to the state before installing the cluster (or use a new node),
    maintaining the network connectivity of the node1 node.

    Adjust the order of the node1 node in the kube_control_plane, kube_node, and etcd sections in the host list
    (node1/node2/node3 -> node2/node3/node1):

    ```yaml
    function change_control_plane_order() {
      cat << EOF | kubectl apply -f -
    ---
    apiVersion: v1
    kind: ConfigMap
    metadata:
    name: mini-1-hosts-conf
    namespace: kubean-system
    data:
    hosts.yml: |
        all:
        hosts:
            node1:
            ip: "172.30.41.161"
            access_ip: "172.30.41.161"
            ansible_host: "172.30.41.161"
            ansible_connection: ssh
            ansible_user: root
            ansible_password: dangerous
            node2:
            ip: "172.30.41.162"
            access_ip: "172.30.41.162"
            ansible_host: "172.30.41.162"
            ansible_connection: ssh
            ansible_user: root
            ansible_password: dangerous
            node3:
            ip: "172.30.41.163"
            access_ip: "172.30.41.163"
            ansible_host: "172.30.41.163"
            ansible_connection: ssh
            ansible_user: root
            ansible_password: dangerous
        children:
            kube_control_plane:
            hosts:
                node2:
                node3:
                node1:
            kube_node:
            hosts:
                node2:
                node3:
                node1:
            etcd:
            hosts:
                node2:
                node3:
                node1:
            k8s_cluster:
            children:
                kube_control_plane:
                kube_node:
            calico_rr:
            hosts: {}
    EOF
    }
    
    change_control_plane_order
    ```

1. Remove the first master node in an abnormal state

    After adjusting the order of nodes in the host list, remove the node1 in an abnormal state of the K8s control plane.

    !!! note

        If node1 is offline or malfunctioning, the following configuration items must be added to extraArgs,
        you need not to add them when node1 is online.

        ```toml
        reset_nodes=false # Skip resetting node operation
        allow_ungraceful_removal=true # Allow ungraceful removal operation
        ```

    ```bash
    # Image spray-job can use an accelerator address here
 
    SPRAY_IMG_ADDR="ghcr.m.daocloud.io/kubean-io/spray-job"
    SPRAY_RLS_2_22_TAG="2.22-336b323"
    KUBE_VERSION="v1.24.14"
    CLUSTER_NAME="cluster-mini-1"
    REMOVE_NODE_NAME="node1"
    
    cat << EOF | kubectl apply -f -
    ---
    apiVersion: kubean.io/v1alpha1
    kind: ClusterOperation
    metadata:
      name: cluster-mini-1-remove-node-ops
    spec:
      cluster: ${CLUSTER_NAME}
      image: ${SPRAY_IMG_ADDR}:${SPRAY_RLS_2_22_TAG}
      actionType: playbook
      action: remove-node.yml
      extraArgs: -e node=${REMOVE_NODE_NAME} -e reset_nodes=false -e allow_ungraceful_removal=true -e kube_version=${KUBE_VERSION}
      postHook:
        - actionType: playbook
          action: cluster-info.yml
    EOF
    ```

1. Manually modify the cluster configuration, edit and update cluster-info

    ```bash
    # Edit cluster-info
    kubectl -n kube-public edit cm cluster-info
    
    # 1. If the ca.crt certificate is updated, the content of the certificate-authority-data field needs to be updated
    # View the base64 encoding of the ca certificate:
    cat /etc/kubernetes/ssl/ca.crt | base64 | tr -d '\n'
    
    # 2. Change the IP address in the server field to the new first master IP, this document will use the IP address of node2, 172.30.41.162
    ```

1. Manually modify the cluster configuration, edit and update kubeadm-config

    ```bash
    # Edit kubeadm-config
    kubectl -n kube-system edit cm kubeadm-config
    
    # Change controlPlaneEndpoint to the new first master IP,
    # this document will use the IP address of node2, 172.30.41.162
    ```

1. Scale up the master node and update the cluster

    !!! note

        - Use `--limit` to limit the update operation to only affect the etcd and kube_control_plane node groups.
        - If it is an offline environment, spec.preHook needs to add enable-repo.yml,
          and the extraArgs parameter should fill in the correct repo_list for the related OS.

    ```bash
    cat << EOF | kubectl apply -f -
    ---
    apiVersion: kubean.io/v1alpha1
    kind: ClusterOperation
    metadata:
      name: cluster-mini-1-update-cluster-ops
    spec:
      cluster: ${CLUSTER_NAME}
      image: ${SPRAY_IMG_ADDR}:${SPRAY_RLS_2_22_TAG}
      actionType: playbook
      action: cluster.yml
      extraArgs: --limit=etcd,kube_control_plane -e kube_version=${KUBE_VERSION}
      preHook:
        - actionType: playbook
          action: enable-repo.yml  # This yaml needs to be added in an offline environment,
                                   # and set the correct repo-list (install operating system packages),
                                   # the following parameter values are for reference only
          extraArgs: |
            -e "{repo_list: ['http://172.30.41.0:9000/kubean/centos/\$releasever/os/\$basearch','http://172.30.41.0:9000/kubean/centos-iso/\$releasever/os/\$basearch']}"
      postHook:
        - actionType: playbook
          action: cluster-info.yml
    EOF
    ```

This completes the replacement of the first Master node.
