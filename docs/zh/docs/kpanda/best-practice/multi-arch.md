# 为工作集群添加异构节点

本文介绍如何为 AMD 架构，操作系统为 CentOS 7.9 的工作集群添加 ARM 架构，操作系统为 Kylin v10 sp2 的工作节点

!!! note

    本文仅针对离线模式下，使用 DCE 5.0 平台所创建的工作集群进行异构节点的添加，不包括接入的集群。

## 前提条件

- 已经部署好一个 DCE 5.0 全模式，并且火种节点还存活，部署参考文档[离线安装 DCE 5.0 商业版](../../install/commercial/start-install.md)
- 已经通过 DCE 5.0 平台创建好一个 AMD 架构，操作系统为 CentOS 7.9 的工作集群，创建参考文档[创建工作集群](../user-guide/clusters/create-cluster.md)

## 操作步骤

### 下载并导入离线包（以 ARM 架构、操作系统Kylin v10 sp2 为例）

请确保已经登录到火种节点！并且之前部署 DCE 5.0 时使用的 clusterConfig.yaml 文件还在。

#### 离线镜像包

!!! note

    可以在[下载中心](https://docs.daocloud.io/download/dce5/)下载最新版本。

| CPU 架构 | 版本   | 下载地址                                                     |
| :------- | :----- | :----------------------------------------------------------- |
| AMD64    | v0.10.0 | <https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.10.0-amd64.tar> |
| ARM64    | v0.10.0 | <https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/offline-v0.10.0-arm64.tar> |

下载完毕后解压离线包。此处我们下载 arm64 架构的离线包：

```bash
tar -xvf offline-v0.10.0-arm64.tar
```

#### ISO 离线包（Kylin v10 sp2）

| CPU 架构 | 操作系统版本                                        | 下载地址                                                     |
| :------- | :-------------------------------------------------- | :----------------------------------------------------------- |
| ARM64    | Kylin Linux Advanced Server release V10 (Sword) SP2 | 申请地址：<https://www.kylinos.cn/scheme/server/1.html> <br />注意：麒麟操作系统需要提供个人信息才能下载使用，下载时请选择 V10 (Sword) SP2 |

#### osPackage 离线包 （Kylin v10 sp2）

其中 [Kubean](https://github.com/kubean-io/kubean) 提供了不同操作系统的osPackage 离线包，可以前往 <https://github.com/kubean-io/kubean/releases> 查看。

| 操作系统版本                                        | 下载地址                                                     |
| :-------------------------------------------------- | :----------------------------------------------------------- |
| Kylin Linux Advanced Server release V10 (Sword) SP2 | <https://files.m.daocloud.io/github.com/kubean-io/kubean/releases/download/v0.7.4/os-pkgs-kylinv10-v0.7.4.tar.gz> |

!!! note

    osPackage 离线包的具体对应版本请查看离线镜像包中 `offline/sample/clusterConfig.yaml` 中对应的 kubean 版本

#### 导入离线包至火种节点

执行 import-artifact 命令：

```bash
./offline/dce5-installer import-artifact -c clusterConfig.yaml \
    --offline-path=/root/offline \
    --iso-path=/root/Kylin-Server-10-SP2-aarch64-Release-Build09-20210524.iso \
    --os-pkgs-path=/root/os-pkgs-kylinv10-v0.7.4.tar.gz
```

!!! note

    参数说明：

    - `-c clusterConfig.yaml` 指定之前部署 DCE5.0 时使用的 clusterConfig.yaml 文件
    - `--offline-path` 指定下载的离线镜像包文件地址
    - `--iso-path` 指定下载的 ISO 操作系统镜像文件地址
    - `--os-pkgs-path` 指定下载的 osPackage 离线包文件地址

导入命令执行成功后，会将离线包上传到火种节点的 Minio 中。

### 添加异构工作节点

请确保已经登录到 DCE5.0 的 Global 集群的管理节点上。

#### 修改主机清单文件

主机清单文件示例：

=== "新增节点前"

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
            children:
                kube_control_plane:
                hosts:
                    centos-master: 
                kube_node:
                hosts:
                    centos-master: 
                etcd:
                hosts:
                    centos-master: 
                k8s_cluster:
                children:
                    kube_control_plane: 
                    kube_node: 
    ```

=== "新增节点后"

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
                # 添加异构节点信息
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
                    centos-master: 
                kube_node:
                hosts:
                    centos-master: 
                    kylin-worker: # 添加新增的异构节点名称
                etcd:
                hosts:
                    centos-master: 
                k8s_cluster:
                children:
                    kube_control_plane: 
                    kube_node: 
    ```

按照上述的配置注释，添加新增的工作节点信息。

```shell
kubectl edit cm ${cluster-name}-hosts-conf -n kubean-system
```

`cluster-name` 为工作集群的名称，通过容器管理创建集群时会默认生成。

#### 通过 ClusterOperation.yml 新增扩容任务

示例：

```yaml title="ClusterOperation.yml"
apiVersion: kubean.io/v1alpha1
kind: ClusterOperation
metadata:
  name: add-worker-node
spec:
  cluster: ${cluster-name} # 指定 cluster name
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

    - spec.image 镜像地址要与之前执行部署时的 job 其内镜像保持一致
    - spec.action 设置为 scale.yml
    - spec.extraArgs 设置为 --limit=g-worker
    - pec.preHook 中的 enable-repo.yml 剧本参数，要填写相关OS的正确的 repo_list 

按照上述的配置，创建并部署 join-node-ops.yaml：

```shell
vi join-node-ops.yaml
kubectl kubectl apply -f join-node-ops.yaml -n kubean-system
```

#### 检查任务执行状态

```shell
kubectl -n kubean-system get pod | grep add-worker-node
```

了解缩容任务执行进度，可查看该 Pod 日志。

### 前往界面验证

1. 前往`容器管理`->`集群`->`节点管理`

    ![节点管理](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/arm02.png)

2. 点击新增的节点，查看详情

    ![节点详情](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/arm01.png)
