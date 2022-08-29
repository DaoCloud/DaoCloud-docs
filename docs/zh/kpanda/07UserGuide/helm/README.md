# Helm 概述

Helm 是 Kubernetes 的包管理工具，方便用户快速发现、共享和使用 Kubernetes 构建的应用。

它包含以下几个基本概念：

- Chart：一个 Helm 包，其中包含了运行一个应用所需要的镜像、依赖和资源定义等，还可能包含 Kubernetes 集群中的服务定义，类似 Homebrew 中的 formula、APT 的 dpkg 或者 Yum 的 rpm 文件。
- Release：在 Kubernetes 集群上运行的 Chart 的一个实例。在同一个集群上，一个 Chart 可以安装很多次。每次安装都会创建一个新的 Release。
- Repository：用于发布和存储 Chart 的存储库。

更多详细信息，请前往 [Helm 官网](#https://helm.sh/)。

第五代容器管理模块支持 Helm 社区最新特性，您可以通过 UI 界面快速实现 Helm 应用的部署和管理。主要功能如下：

- [管理 Helm 应用](helm-app.md)
- [管理 Helm 仓库](helm-repo.md)
- [查看 Helm 最近操作记录](#)
