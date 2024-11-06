# 在 CentOS 管理平台上创建 Ubuntu 工作集群

本文介绍如何在已有的 CentOS 管理平台上创建 Ubuntu 工作集群。

!!! note

    本文仅针对离线模式下，使用 DCE 5.0 平台创建工作集群，管理平台和待建工作集群的架构均为 AMD。
    创建集群时不支持异构（AMD 和 ARM 混合）部署，您可以在集群创建完成后，通过接入异构节点的方式进行集群混合部署管理。

## 前提条件

- 已经部署好一个 DCE 5.0 全模式，并且火种节点还存活，部署参考文档[离线安装 DCE 5.0 商业版](../../install/commercial/start-install.md)

## 下载并导入 Ubuntu 相关离线包

请确保已经登录到火种节点！并且之前部署 DCE 5.0 时使用的 clusterConfig.yaml 文件还在。

### 下载 Ubuntu 相关离线包

下载所需的 Ubuntu OS package 包和 ISO 离线包：

| 资源名 | 说明 | 下载地址 |
| ----- | --- | ------- |
| os-pkgs-ubuntu2204-v0.18.2.tar.gz | Ubuntu1804 OS-package 包 | https://github.com/kubean-io/kubean/releases/download/v0.18.2/os-pkgs-ubuntu2204-v0.18.2.tar.gz |
| ISO 离线包 | ISO 包 | http://mirrors.melbourne.co.uk/ubuntu-releases/ |

### 导入 OS Package 和 ISO 离线包至火种节点的 MinIO

参考文档[离线资源导入](../../install/import.md#_5)，导入离线资源至火种节点的 MinIO。

## 前往 UI 界面创建集群

参考文档[创建工作集群](../user-guide/clusters/create-cluster.md)，创建 Ubuntu 集群。
