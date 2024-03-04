# 替换工作集群的首个控制节点

本文将以一个高可用三控制节点的工作集群为例，当工作集群的首个控制节点故障或异常时，如何替换或重新接入首个控制节点。

高可用 3 Master 节点集群

- node1 (172.30.41.161)
- node2 (172.30.41.162)
- node3 (172.30.41.163)

假设 node1 宕机，接下来介绍如何将宕机后恢复的 node1 重新接入工作集群。

## 准备工作

在执行替换操作之前，先获取集群资源基本信息，修改相关配置时会用到。

!!! note

    以下获取集群资源信息的命令均在管理集群中执行。

a.获取集群名称

    执行如下命令，找到集群对应的 clusters.kubean.io 资源：

    ```shell
    # 比如 clusters.kubean.io 的资源名称为 cluster-mini-1
    # 则获取集群的名称
    $ CLUSTER_NAME=$(kubectl get clusters.kubean.io cluster-mini-1 -o=jsonpath="{.metadata.name}{'\n'}")
    ```

b.获取集群的主机清单 configmap

    ```shell
    $ kubectl get clusters.kubean.io cluster-mini-1 -o=jsonpath="{.spec.hostsConfRef}{'\n'}"
    {"name":"mini-1-hosts-conf","namespace":"kubean-system"}
    ```

c.获取集群的配置参数 configmap

    ```shell
    $ kubectl get clusters.kubean.io cluster-mini-1 -o=jsonpath="{.spec.varsConfRef}{'\n'}"
    {"name":"mini-1-vars-conf","namespace":"kubean-system"}
    ```

## 操作步骤

1. 调整控制平面节点顺序

    重置 node1 节点使其恢复到安装集群之前的状态（或使用新的节点），保持 node1 节点的网络连通性。

    调整主机清单中 node1 节点在 kube_control_plane 、kube_node、etcd 中的顺序（node1/node2/node3 → node2/node3/node1）：

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

1. 移除异常状态的首个 master 节点

    主机清单节点顺序调整完成后，移除 k8s 控制平面异常状态的 node1。

    !!! note

        如果 node1 离线或故障，则 extraArgs 须添加以下配置项，node1 在线时不需要添加。

        ```yaml
        reset_nodes=false #跳过重置节点操作
        allow_ungraceful_removal=true #允许非优雅的移除操作
        ```

    ```yaml
    # 镜像 spray-job 这里可以采用加速器地址
 
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

1. 手动修改集群配置，编辑更新 cluster-info

    ```yaml
    # 编辑 cluster-info
    $ kubectl -n kube-public edit cm cluster-info
    
    # 1. 若 ca.crt 证书更新，则需要更新 certificate-authority-data 字段的内容
    # 查看 ca 证书的 base64 编码：
    $ cat /etc/kubernetes/ssl/ca.crt | base64 | tr -d '\n'
    
    # 2. 需改 server 字段的 IP 地址为新 first master IP, 本文档场景将使用 node2 的 IP 地址 172.30.41.162
    ```

1. 手动修改集群配置，编辑更新 kubeadm-config

    ```yaml
    # 编辑 kubeadm-config
    $ kubectl -n kube-system edit cm kubeadm-config
    
    # 1. 修改 controlPlaneEndpoint 为新 first master IP, 本文档场景将使用 node2 的 IP 地址 172.30.41.162
    ```

1. 重新扩容 master 节点并更新集群

    !!! note

        - 使用 --limit 限制更新操作仅作用于 etcd 和 kube_control_plane 节点组。
        - 如果是离线环境，spec.preHook 需要添加 enable-repo.yml，并且 extraArgs 参数填写相关 OS 的正确 repo_list。

    ```yaml
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
          action: enable-repo.yml  # 离线环境下需要添加此 yaml，并且设置正确的 repo-list(安装操作系统软件包)，以下参数值仅供参考
          extraArgs: |
            -e "{repo_list: ['http://172.30.41.0:9000/kubean/centos/\$releasever/os/\$basearch','http://172.30.41.0:9000/kubean/centos-iso/\$releasever/os/\$basearch']}"
      postHook:
        - actionType: playbook
          action: cluster-info.yml
    EOF
    ```

以上，完成首个 master 节点的替换。