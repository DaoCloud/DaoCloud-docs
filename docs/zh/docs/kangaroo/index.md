---
hide:
  - toc
---

# 什么是镜像仓库

镜像仓库是一个支持多实例生命周期管理的云原生镜像托管服务，支持将镜像仓库实例部署至任意云原生基础环境，同时支持集成外部镜像仓库（Harbor Registry 和 Docker Registry）。
通过镜像仓库服务，您可以将私有镜像空间分配给一个或多个工作空间（租户）使用，确保私有镜像的安全性，也可以将镜像空间公开给所有 Kubernetes 命名空间使用，镜像仓库配合[容器管理](../kpanda/intro/index.md)服务帮助用户快速部署应用。

**功能特性**

- 镜像仓库全生命周期管理

    通过托管 Harbor 提供镜像仓库的全生命周期管理，包括镜像仓库的创建、编辑、删除等。

- 租户化应用部署

    支持将镜像空间分配给一个或多个工作空间（租户）使用；支持工作空间（租户）独立关联外部镜像仓库。

- 镜像扫描

    支持镜像扫描功能，识别镜像安全风险

- 镜像选择

    与容器管理模块联动，通过“选择镜像”功能快速选择镜像，完成应用部署。

**产品逻辑架构**

![逻辑架构图](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/architect.png)

[下载 DCE 5.0](../download/index.md){ .md-button .md-button--primary }
[安装 DCE 5.0](../install/index.md){ .md-button .md-button--primary }
[申请社区免费体验](../dce/license0.md){ .md-button .md-button--primary }