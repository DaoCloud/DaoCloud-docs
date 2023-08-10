# 在 centos 管理平台上创建 ubuntu 工作集群

本文介绍如何在已有的 centos 管理平台上创建 ubuntu 工作集群。

!!! note

    本文仅针对离线模式下，使用 DCE 5.0 平台创建工作集群，管理平台和待建工作集群的架构均为 AMD。创建集群时不支持异构（AMD 和 ARM 混合）部署，您可以在集群创建完成后，通过接入异构节点的方式进行集群混合部署管理。

## 前提条件

- 已经部署好一个 DCE 5.0 全模式，并且火种节点还存活，部署参考文档[离线安装 DCE 5.0 商业版](../../install/commercial/start-install.md)

## 操作步骤

### 下载并导入 ubuntu 相关离线包

请确保已经登录到火种节点！并且之前部署 DCE 5.0 时使用的 clusterConfig.yaml 文件还在。

#### 下载 ubuntu 相关离线包

下载所需的 ubuntu OS package 包和 ISO 离线包

| 资源名                           | 说明                     | 下载地址                                                     |
| -------------------------------- | ------------------------ | ------------------------------------------------------------ |
| os-pkgs-ubuntu1804-v0.6.6.tar.gz | Ubuntu1804 OS-package 包 | https://github.com/kubean-io/kubean/releases/download/v0.6.6/os-pkgs-ubuntu1804-v0.6.6.tar.gz |
| ISO 离线包                   | OS 包导入火种节点脚本    | http://mirrors.melbourne.co.uk/ubuntu-releases/ |
| import-iso                   | ISO 导入火种节点脚本    | https://github.com/kubean-io/kubean/releases/download/v0.6.6/import_iso.sh |

#### 导入 os pckage 离线包至火种节点的 minio

**解压 ubuntu os pckage 离线包**

执行如下命令解压下载的 os pckage 离线包。

```bash
# 此处我们下载的 ubuntu os pckage 离线包
tar -xvf os-pkgs-ubuntu1804-v0.6.6.tar.gz 
```

os package 解压后的文件内容如下：

```text
    os-pkgs
    ├── import_ospkgs.sh       # 该脚本用于导入 os packages 到 minio 文件服务
    ├── os-pkgs-amd64.tar.gz   # amd64 架构的 os packages 包
    ├── os-pkgs-arm64.tar.gz   # arm64 架构的 os packages 包
    └── os-pkgs.sha256sum.txt  # os packages 包的 sha256sum 效验文件
```

**导入 OS Package 至火种节点的 minio**

执行如下命令, 将 os packages 包到 minio 文件服务中:

```bash
MINIO_USER=rootuser MINIO_PASS=rootpass123 ./import_ospkgs.sh  http://127.0.0.1:9000 os-pkgs-ubuntu1804-v0.6.6.tar.gz
```

!!! note

    上述命令仅仅适用于火种节点内置的 Minio 服务，如果使用外部 Minio 请将“http://127.0.0.1:9000” 替换为外部 Minio 的访问地址。 “rootuser” 和 “rootpass123”是火种节点内置的 Minio 服务的默认账户和密码。“os-pkgs-ubuntu1804-v0.6.6.tar.gz“ 为所下载的 os package 离线包的名称。

#### 导入 ISO 离线包至火种节点的 minio

执行如下命令, 将 ISO 包到 minio 文件服务中:

```bash
MINIO_USER=rootuser MINIO_PASS=rootpass123 ./import_iso.sh http://127.0.0.1:9000 ubuntu-16.04.7-server-amd64.iso
```
!!! note

    上述命令仅仅适用于火种节点内置的 Minio 服务，如果使用外部 Minio 请将“http://127.0.0.1:9000” 替换为外部 Minio 的访问地址。 “rootuser” 和 “rootpass123”是火种节点内置的 Minio 服务的默认账户和密码。“ubuntu-16.04.7-server-amd64.iso“ 为所下载的 ISO 离线包。

### 前往界面创建集群

参考文档[创建工作集群](../user-guide/clusters/create-cluster.md)，创建 ubuntu 集群。
