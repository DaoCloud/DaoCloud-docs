---
hide:
  - toc
---

# Helm 模板

Helm 是 Kubernetes 的包管理工具，方便用户快速发现、共享和使用 Kubernetes 构建的应用。第五代[容器管理模块](../../intro/index.md)提供了上百个 Helm 模板，涵盖存储、网络、监控、数据库等主要场景。借助这些模板，您可以通过 UI 界面快速部署、便捷管理 Helm 应用。此外，支持通过[添加 Helm 仓库](helm-repo.md) 添加更多的个性化模板，满足多样需求。

![模板](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/helm14.png)

**关键概念**：

使用 Helm 时需要了解以下几个关键概念：

- Chart：一个 Helm 安装包，其中包含了运行一个应用所需要的镜像、依赖和资源定义等，还可能包含 Kubernetes 集群中的服务定义，类似 Homebrew 中的 formula、APT 的 dpkg 或者 Yum 的 rpm 文件。**Chart 在 DCE 5.0 中称为 `Helm 模板`**。

- Release：在 Kubernetes 集群上运行的一个 Chart 实例。一个 Chart 可以在同一个集群内多次安装，每次安装都会创建一个新的 Release。**Release 在 DCE 5.0 中称为 `Helm 应用`**。

- Repository：用于发布和存储 Chart 的存储库。**Repository 在 DCE 5.0 中称为 `Helm 仓库`**。

更多详细信息，请前往 [Helm 官网](https://helm.sh/)查看。

**相关操作**：

- [管理 Helm 应用](helm-app.md)，包括安装、更新、卸载 Helm 应用，查看 Helm 操作记录等。
- [管理 Helm 仓库](helm-repo.md)，包括安装、更新、删除 Helm 仓库等。
