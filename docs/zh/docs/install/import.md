# 离线资源导入

安装器 dce5-installer（仅支持 v0.9.0 版本及以上）支持 `import-artifact` 命令来导入离线资源。目前可被导入的离线资源包括：

- `*.iso` 操作系统 ISO 镜像文件
- `os-pkgs-${disto}-${kubean_version}.tar.gz` Kubean 提供的 osPackage 离线包
- `offline-${install_version}-${arch}.tar` 安装器全模式离线镜像包：
    - K8s 二进制和镜像
    - DCE 5.0 各个模块的镜像文件和 Chart 包

## 使用场景

### 场景一

当全局服务集群的操作系统与创建的工作集群操作系统不一致时，需要导入对应工作集群的操作系统的 ISO 镜像文件 和 osPackage 离线包。

例如[在 CentOS 的全局服务集群上创建 Ubuntu 操作系统的工作集群](../kpanda/best-practice/create-ubuntu-on-centos-platform.md)。

### 场景二

在混合架构的离线部署场景中，需要在原有的 amd64 离线资源（K8s 二进制）和（K8s 镜像 + 各个模块的镜像文件和 Chart 包）基础上，导入并整合 arm64 的对应资源。

例如[如何为工作集群添加异构节点](../kpanda/best-practice/multi-arch.md)。

## 导入命令介绍

需要提前下载好 dce5-installer 二进制文件。

### 导入操作系统 ISO 镜像文件

以导入 TencentOS-Server-3.1-TK4-x86_64-minimal-2209.3.iso 为例：

``` bash
# 采用 build-in 内建模式部署火种集群时，可以不用指定 clusterConfig.yml 配置文件
dce5-installer import-artifact --iso-path=/home/iso/TencentOS-Server-3.1-TK4-x86_64-minimal-2209.3.iso

# 采用 external 外接模式部署火种集群时，需要指定 clusterConfig.yml 配置文件
dce5-installer import-artifact -c clusterConfig.yml --iso-path=/home/iso/TencentOS-Server-3.1-TK4-x86_64-minimal-2209.3.iso
```

### 导入 Kubean 提供的 osPackage 离线包

以导入 os-pkgs-tencent31-v0.6.2.tar.gz 为例：

``` bash
# 采用 build-in 内建模式部署火种集群时，可以不用指定 clusterConfig.yml 配置文件
dce5-installer import-artifact --os-pkgs-path=/home/os-pkgs/os-pkgs-tencent31-v0.6.2.tar.gz

# 采用 external 外接模式部署火种集群时，需要指定 clusterConfig.yml 配置文件
dce5-installer import-artifact -c clusterConfig.yml --os-pkgs-path=/home/os-pkgs/os-pkgs-tencent31-v0.6.2.tar.gz
```

### 导入安装器离线镜像包 Offline 目录内容

``` bash
# 采用 build-in 内建模式部署火种集群时，可以不用指定 clusterConfig.yml 配置文件
dce5-installer import-artifact --offline-path=/home/offline/

# 采用 external 外接模式部署火种集群时，需要指定 clusterConfig.yml 配置文件
dce5-installer import-artifact -c clusterConfig.yml --offline-path=/home/offline/
```

### 同时指定导入多种离线资源

``` bash
# 采用 build-in 内建模式部署火种集群时，可以不用指定 clusterConfig.yml 配置文件
dce5-installer import-artifact \
      --offline-path=/home/offline/ \
      --os-pkgs-path=/home/os-pkgs/os-pkgs-tencent31-v0.6.2.tar.gz \
      --iso-path=/home/iso/TencentOS-Server-3.1-TK4-x86_64-minimal-2209.3.iso

# 采用 external 外接模式部署火种集群时，需要指定 clusterConfig.yml 配置文件
dce5-installer import-artifact -c clusterConfig.yml \
      --offline-path=/home/offline/ \
      --os-pkgs-path=/home/os-pkgs/os-pkgs-tencent31-v0.6.2.tar.gz \
      --iso-path=/home/iso/TencentOS-Server-3.1-TK4-x86_64-minimal-2209.3.iso
```
