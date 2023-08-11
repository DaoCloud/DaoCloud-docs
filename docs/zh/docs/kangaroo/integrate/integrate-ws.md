# 仓库集成(工作空间)

仓库集成(工作空间)是针对工作空间提供的便捷接入仓库功能。
工作空间管理员（Workspace Admin）可根据需要为该工作空间灵活接入镜像仓库，供工作空间成员使用。
接入后，成员在工作空间下的命名空间部署应用时可通过`选择镜像`按钮一键拉取工作空间下所有公开和私有的镜像，实现快速部署应用。

支持集成 3 种仓库：

- Harbor Registry：这是一个开源的企业级 Docker 镜像仓库，提供镜像存储、版本控制、访问控制和安全扫描等功能。
  它专注于为企业环境提供高度可定制和安全的容器镜像管理解决方案。
  Harbor Registry 支持跨多个容器编排平台进行集成，并具有丰富的权限管理和审计功能。

- Docker Registry：这是 Docker 官方提供的镜像仓库服务。它作为 Docker 生态系统的一部分，
  用于存储、分发和管理 Docker 镜像。Docker Registry 提供了基本的镜像存储和版本控制功能，
  可以通过简单的 API 进行操作。

- JFrog Artifactory：这是一个通用的软件包管理和分发平台，支持各种不同的包类型，包括 Docker 镜像。
  除了作为 Docker 镜像仓库外，Artifactory 还支持其他软件包格式（如 Maven、npm 等）的存储、分发和管理。
  Artifactory 提供强大的权限控制、缓存和快速复制等功能，同时具备高度可扩展性和可定制性。
  与上述两个镜像仓库相比，Artifactory 是一个较为全面的软件包管理平台，适用于跨多种包类型的工作负载。

## 优势

- 灵活便捷：工作空间的管理员均可自主接入一个或多个 Harbor / Docker 类型的镜像仓库，供工作空间成员使用。
- 全局联动：接入后，在应用工作台部署应用时，可通过`选择镜像`按钮，一键选择仓库中的镜像，实现快速部署应用。

## 操作步骤

可以参阅[视频教程](../../videos/kangaroo.md#_2)熟悉以下操作步骤：

1. 使用具有 Workspace Admin 角色的用户登录 DCE 5.0，从左侧导航栏点击`镜像仓库` -> `仓库集成(工作空间)`。

    ![镜像仓库](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/related01.png)

1. 点击右上角的`仓库集成`按钮。

    ![仓库集成](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/relate02.png)

1. 填写表单信息后点击`确定`。

    ![填写表单](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/relate03.png)

    !!! note

        1. Docker Registry 镜像仓库若未设置密码可不填写，Harbor 仓库必须填写用户名/密码。
        1. 有关实际操作演示，请参阅[仓库集成(工作空间)视频演示](../../videos/kangaroo.md)
