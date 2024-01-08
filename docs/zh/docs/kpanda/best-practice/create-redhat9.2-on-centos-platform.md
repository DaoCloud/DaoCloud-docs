# 在 CentOS 管理平台上创建 RedHat 9.2 工作集群

本文介绍如何在已有的 CentOS 管理平台上创建 RedHat 9.2 工作集群。

!!! note

    本文仅针对离线模式下，使用 DCE 5.0 平台创建工作集群，管理平台和待建工作集群的架构均为 AMD。
    创建集群时不支持异构（AMD 和 ARM 混合）部署，您可以在集群创建完成后，通过接入异构节点的方式进行集群混合部署管理。

## 前提条件

已经部署好一个 DCE 5.0 全模式，并且火种节点还存活，部署参考文档[离线安装 DCE 5.0 商业版](../../install/commercial/start-install.md)

## 下载并导入 RedHat 相关离线包

请确保已经登录到火种节点！并且之前部署 DCE 5.0 时使用的 `clusterConfig.yaml` 文件还在。

### 下载 RedHat 相关离线包

下载所需的 RedHat OS package 包和 ISO 离线包：

| 资源名 | 说明 | 下载地址 |
| ----- | --- | ------- |
| os-pkgs-redhat9-v0.9.3.tar.gz | RedHat9.2 OS-package 包 | https://github.com/kubean-io/kubean/releases/download/v0.9.3/os-pkgs-redhat9-v0.9.3.tar.gz |
| ISO 离线包 | ISO 包导入火种节点脚本 | 前往 [RedHat 官方下载地址](https://access.cdn.redhat.com/content/origin/files/sha256/a1/a18bf014e2cb5b6b9cee3ea09ccfd7bc2a84e68e09487bb119a98aa0e3563ac2/rhel-9.2-x86_64-dvd.iso?user=cb58db6b16a8cf7e24021ebac6be33e8&_auth_=1698145622_cdb9984fa8440b24f4e126ec2e368c82) |
| import-iso | ISO 导入火种节点脚本 | https://github.com/kubean-io/kubean/releases/download/v0.9.3/import_iso.sh |

### 导入 os pckage 离线包至火种节点的 minio

**解压 RedHat os pckage 离线包**

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

**导入 OS Package 至火种节点的 MinIO**

执行如下命令, 将 os packages 包到 MinIO 文件服务中:

```bash
MINIO_USER=rootuser MINIO_PASS=rootpass123 ./import_ospkgs.sh  http://127.0.0.1:9000 os-pkgs-redhat9-v0.9.3.tar.gz
```

!!! note

    上述命令仅仅适用于火种节点内置的 MinIO 服务，如果使用外部 MinIO 请将 `http://127.0.0.1:9000` 替换为外部 MinIO 的访问地址。
    “rootuser” 和 “rootpass123” 是火种节点内置的 MinIO 服务的默认账户和密码。“os-pkgs-redhat9-v0.9.3.tar.gz“
    为所下载的 os package 离线包的名称。

### 导入 ISO 离线包至火种节点的 MinIO

执行如下命令, 将 ISO 包到 MinIO 文件服务中:

```bash
MINIO_USER=rootuser MINIO_PASS=rootpass123 ./import_iso.sh http://127.0.0.1:9000 rhel-9.2-x86_64-dvd.iso
```

!!! note

    上述命令仅仅适用于火种节点内置的 MinIO 服务，如果使用外部 MinIO 请将 `http://127.0.0.1:9000` 替换为外部 MinIO 的访问地址。
    “rootuser” 和 “rootpass123” 是火种节点内置的 MinIO 服务的默认账户和密码。
    “rhel-9.2-x86_64-dvd.iso“ 为所下载的 ISO 离线包。

## 前往 UI 界面创建集群

参考文档[创建工作集群](../user-guide/clusters/create-cluster.md)，创建 RedHat 9.2 集群。
