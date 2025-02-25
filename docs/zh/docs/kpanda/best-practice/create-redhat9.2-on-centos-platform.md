# 在 CentOS 管理平台上创建 RedHat 9.2 工作集群

本文介绍如何在已有的 CentOS 管理平台上创建 RedHat 9.2 工作集群。

!!! note

    本文仅针对离线模式下，使用 DCE 5.0 平台创建工作集群，管理平台和待建工作集群的架构均为 AMD。
    创建集群时不支持异构（AMD 和 ARM 混合）部署，您可以在集群创建完成后，通过接入异构节点的方式进行集群混合部署管理。

## 前提条件

你已经部署好一个 DCE 5.0 全模式，并且火种节点还存活。具体部署，请参考文档[离线安装 DCE 5.0 商业版](../../install/commercial/start-install.md)。

## 下载并导入 RedHat 相关离线包

请确保已经登录到火种节点！并且之前部署 DCE 5.0 时使用的 `clusterConfig.yaml` 文件还在。

### 下载 RedHat 相关离线包

下载所需的 RedHat OS package 包和 ISO 离线包：

| 资源名 | 说明 | 下载地址 |
| ----- | --- | ------- |
| os-pkgs-redhat9-v0.9.3.tar.gz | RedHat9.2 OS-package 包 | https://github.com/kubean-io/kubean/releases/download/v0.9.3/os-pkgs-redhat9-v0.9.3.tar.gz |
| ISO 离线包 | ISO 包导入火种节点脚本 | 前往 [RedHat 官方地址登录下载](https://access.redhat.com/zh_CN/downloads) |
| import-iso | ISO 导入火种节点脚本 | https://github.com/kubean-io/kubean/releases/download/v0.9.3/import_iso.sh |

### 导入 OS pckage 离线包至火种节点

<!-- **解压 RedHat os pckage 离线包**

执行如下命令解压下载的 os pckage 离线包。此处我们下载的 RedHat os pckage 离线包。

```bash
tar -xvf os-pkgs-redhat9-v0.9.3.tar.gz 
```

os package 解压后的文件内容如下：

```text
    os-pkgs
    ├── import_ospkgs.sh       # 该脚本用于导入 os packages 到 MinIO 文件服务
    ├── os-pkgs-amd64.tar.gz   # amd64 架构的 os packages 包
    ├── os-pkgs-arm64.tar.gz   # arm64 架构的 os packages 包
    └── os-pkgs.sha256sum.txt  # os packages 包的 sha256sum 效验文件
```

**导入 OS Package** -->

执行如下命令，导入 os pckage 包：

```bash
# 采用 build-in 内建模式部署火种集群时，我们可以不用指定 clusterConfig.yml 配置文件
dce5-installer import-artifact --os-pkgs-path=/home/os-pkgs/os-pkgs-redhat9-v0.9.3.tar.gz

# 采用 external 外接模式部署火种集群时，我们需要指定 clusterConfig.yml 配置文件
dce5-installer import-artifact -c clusterConfig.yml --os-pkgs-path=/home/os-pkgs/os-pkgs-redhat9-v0.9.3.tar.gz
```

!!! note

    上述命令中，“/home/os-pkgs”为 os pckage 包下载目录，“os-pkgs-redhat9-v0.9.3.tar.gz“为所下载的 os package 离线包名称。

### 导入 ISO 离线包至火种节点

执行如下命令，导入 ISO 包：

```bash
# 采用 build-in 内建模式部署火种集群时，我们可以不用指定 clusterConfig.yml 配置文件
dce5-installer import-artifact --iso-path=/home/iso/rhel-9.2-x86_64-dvd.iso

# 采用 external 外接模式部署火种集群时，我们需要指定 clusterConfig.yml 配置文件
dce5-installer import-artifact -c clusterConfig.yml --iso-path=/home/iso/rhel-9.2-x86_64-dvd.iso
```

!!! note

    上述命令中，“/home/iso”为 ISO 包下载目录，“rhel-9.2-x86_64-dvd.iso“ 为所下载的 ISO 离线包名称。

## 前往 UI 界面创建集群

参考文档[创建工作集群](../user-guide/clusters/create-cluster.md)，创建 RedHat 9.2 集群。
