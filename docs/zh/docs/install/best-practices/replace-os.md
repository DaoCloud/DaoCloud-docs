# 不停机迁移集群操作系统

## 背景

某客户生产环境在 CentOS 7.9 操作系统上部署了 DCE 5.0 工作集群，但是由于
[CentOS 7.9 将停止维护](https://www.redhat.com/en/topics/linux/centos-linux-eol)，所以客户希望迁移到 Ubuntu 22.04。
由于是生产环境，客户希望在不停机的情况下，从 CentOS 7.9 迁移到 Ubuntu 22.04。

## 风险

- k8s 集群节点的迁移最佳实践是先增后删的操作顺序，但客户要求保证节点 IP 不发生变化，
  基于此只能调整节点迁移顺序为先删后增，此顺序的改变会导致集群容错性及稳定性下降，需要谨慎对待！

- 另外先删后增的过程中，原节点上的资源会迁移到其他节点，应保证其他节点拥有足够资源和足够的 Pod 容纳能力，否则会导致迁移失败；

    - 默认单节点最大容纳 Pod 数 `kubelet_max_pods` 为 110。若迁移可能导致超标，则最好提前更新所有节点的容纳能力
    - 删除节点的过程中，如果有服务固定在移除的节点或流量指向移除的节点上的 Pod，会有 2-3s 的业务断连

## 解决方案

- 需要从 Control Plane 、Worker 节点两个角度来处理
- 迁移操作顺序：[Worker 节点迁移](#worker) -> [非首个 Control Plane 节点迁移](#control-plane_1) -> [首个 Control Plane 节点迁移](#control-plane_2)
- 在进行节点迁移操作之前，安全起见，建议对集群的相关资源进行备份

!!! note

    本文档默认采用先删后增的操作顺序，实际场景可按需求调整操作顺序。

### 离线资源准备（在线可忽略）

1. 通过安装器命令，导入 Ubuntu 22.04 的 [iso](../commercial/start-install.md#iso)、
   [ospackage](../commercial/start-install.md#ospackage) 文件：

    ```shell
    dce5-installer import-artifact \
        --os-pkgs-path=/home/airgap/os-pkgs-ubuntu2204-v0.16.0.tar.gz \
        --iso-path=/home/iso/ubuntu-22.04.4-live-server-amd64.iso
    ```

2. 配置 Ubuntu 22.04 离线源的示例（`--limit` 用于限制源配置仅作用于指定扩容的节点）：

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

    1. 在任务运行前，先执行 enable-repo 的 playbook，为每个节点创建指定 url 的源配置

### Worker 节点迁移

1. 进入工作集群详情界面，在 **集群设置** -> **高级设置** 中，关闭 **集群删除保护**

1. 在 **节点管理** 列表中，选择一个工作节点，点击 **移除**

1. 移除成功后，在终端命令行中，连接[全局服务集群](../../kpanda/user-guide/clusters/cluster-role.md#_2)，
   获取资源类型为 `clusters.kubean.io`，名称为 <工作集群名称> 下的参数 `hosts-conf` 信息，此示例工作集群名称为：centos

    ```shell
    # 获取 hosts-conf 参数
    $ kubectl get clusters.kubean.io centos -o=jsonpath="{.spec.hostsConfRef}{'\n'}"

    {"name":"centos-hosts-conf","namespace":"kubean-system"}
    ```

1. 在 **节点管理** 列表中，点击 **接入节点** ，将之前移除的节点重新加入进来即可

1. 等待新节点扩容成功后，其他工作节点重复以上步骤直至全部迁移完成

### Control Plane 节点迁移

Control Plane 节点迁移需要分成两部分，分别为首个 Control Plane 节点迁移、非首个 Control Plane 节点迁移

#### 如何确定首个主节点

请查看集群的资源 `clusters.kubean.io` 配置 host-conf 内容，具体定位 `all.children.kube_control_plane.hosts`，
在 kube_control_plane 组中，排在首位的节点，即为首个主节点；

```yaml
      children:
        kube_control_plane:
          hosts:
            centos-master1: null # (1)!
            centos-master2: null
            centos-master3: null
```

1. 首个节点

#### 非首个 Control Plane 节点迁移

1. 在终端命令行中，连接全局服务集群，获取资源类型为 `clusters.kubean.io`，名称为 <工作集群名称> 下的参数
   `hosts-conf`、`vars-conf` 信息，此示例工作集群名称为：centos

    ```shell
    # 获取 hosts-conf 参数
    $ kubectl get clusters.kubean.io centos -o=jsonpath="{.spec.hostsConfRef}{'\n'}"

    {"name":"centos-hosts-conf","namespace":"kubean-system"}

    # 获取 vars-conf 参数
    $ kubectl get clusters.kubean.io centos -o=jsonpath="{.spec.varsConfRef}{'\n'}"

    {"name":"centos-vars-conf","namespace":"kubean-system"}
    ```

2. 创建 ConfigMap 资源用于清理 kube-apiserver 任务，资源文件如下：

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

3. 部署上述文件后，创建 ClusterOperation，用于 Control Plane 的节点缩容，资源文件如下：

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

    1. 工作集群名称
    2. 指定 Kubean 任务运行的镜像，镜像地址要与之前执行部署时的 Job 其内镜像保持一致
    3. 此处需要定义为非首个 Control Plane 的任意一个节点

4. 部署上述文件后且等待节点缩容成功后，创建 ClusterOperation 资源，用于 Control Plane 的节点扩容，资源文件如下：

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

    1. 工作集群名称
    2. 指定 Kubean 任务运行的镜像，镜像地址要与之前执行部署时的 Job 其内镜像保持一致

5. 部署上述文件后且等待第 4 步移除节点重新扩容进来后，重复执行第 3、4 步完成第三个节点的迁移

#### 首个 Control Plane 节点迁移

可参考文档[迁移工作集群的首个控制节点](../../kpanda/best-practice/replace-first-master-node.md)。

1. 在容器管理集群对工作集群的 kubeconfig 进行更新，终端登录到第二个节点

2. 更新 ConfigMap 的资源 `centos-hosts-conf`，调整工作集群首个 Control Plane 节点在
   kube_control_plane、kube_node、etcd 中的顺序（node1/node2/node3 -> node2/node3/node1）：

    === "修改前"

        ```yaml
            children:
              chakube_control_plane:
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

    === "修改后"

        ```yaml
            children:
              chakube_control_plane:
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

3. 创建 ClusterOperation，用于 Control Plane 的节点缩容，资源文件如下：

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

    1. 工作集群名称
    2. 指定 Kubean 任务运行的镜像，镜像地址要与之前执行部署时的 Job 其内镜像保持一致
    3. 此处需要定义为首个 Control Plane 的节点

4. 部署上述文件且缩容成功后，更新 ConfigMap 资源 cluster-info、kubeadm-config

    ```shell
    # 编辑 cluster-info
    kubectl -n kube-public edit cm cluster-info

    # 1. 若 ca.crt 证书更新，则需要更新 certificate-authority-data 字段的内容
    # 查看 ca 证书的 base64 编码：
    cat /etc/kubernetes/ssl/ca.crt | base64 | tr -d '\n'

    # 2. 需修改 server 字段的 IP 地址为第二个 Control Plane IP
    ```

    ```shell
    # 编辑 kubeadm-config
    kubectl -n kube-system edit cm kubeadm-config

    # 修改 controlPlaneEndpoint 为第二个 Control Plane IP
    ```

5. 创建 ClusterOperation，用于 Control Plane 的节点扩容，资源文件如下：

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

    1. 工作集群名称
    2. 指定 Kubean 任务运行的镜像，镜像地址要与之前执行部署时的 Job 其内镜像保持一致

6. 扩容任务完成后即成功完成首个 Control Plane 节点迁移
