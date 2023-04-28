# 自定义角色

DCE 5.0 支持创建三种范围的自定义角色：

- **平台角色** 的权限对平台所有相关资源生效
- **工作空间角色** 的权限对该用户所在的工作空间下的资源生效
- **文件夹角色** 的权限对该用户所在的文件夹及其下的子文件夹和工作空间资源生效

## 创建平台角色

平台角色指的是能够操控 DCE 5.0 某个模块（例如容器管理、微服务引擎、多云编排、服务网格、镜像仓库、应用工作台和全局管理等）相关特性的角色。

1. 从左侧导航栏点击`全局管理` -> `用户与访问控制` -> `角色`，点击`创建自定义角色`。

    ![创建自定义角色](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/ghippo/user-guide/access-control/images/custom01.png)

1. 输入名称、描述，选择`平台角色`，勾选角色权限后点击`确定`。

    ![平台角色](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/ghippo/user-guide/access-control/images/custom02.png)

1. 返回角色列表，搜索刚创建的自定义角色，点击右侧的 `⋮`，可以执行复制、编辑和删除等操作。

    ![更多操作](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/ghippo/user-guide/access-control/images/custom03.png)

1. 平台角色创建成功后，可以去[用户](./user.md)/[用户组](./group.md)授权，为这个角色添加用户和用户组。

## 创建工作空间角色

工作空间角色指的是能够按照工作空间操控某个模块（例如容器管理、微服务引擎、多云编排、服务网格、镜像仓库、应用工作台和全局管理等）相关特性的角色。

1. 从左侧导航栏点击`全局管理` -> `用户与访问控制` -> `角色`，点击`创建自定义角色`。

    ![创建自定义角色](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/ghippo/user-guide/access-control/images/custom01.png)

1. 输入名称、描述，选择`工作空间角色`，勾选角色权限后点击`确定`。

    ![工作空间角色](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/ghippo/user-guide/access-control/images/custom04.png)

1. 返回角色列表，搜索刚创建的自定义角色，点击右侧的 `⋮`，可以执行复制、编辑和删除等操作。

    ![更多操作](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/ghippo/user-guide/access-control/images/custom05.png)

1. 工作空间角色创建成功后，可以去[工作空间](../workspace/workspace.md)授权，设定这个角色可以管理哪些工作空间。

## 创建文件夹角色

文件夹角色指的是能够按照文件夹、子文件夹操控 DCE 5.0 某个模块（例如容器管理、微服务引擎、多云编排、服务网格、镜像仓库、应用工作台和全局管理等）相关特性的角色。

1. 从左侧导航栏点击`全局管理` -> `用户与访问控制` -> `角色`，点击`创建自定义角色`。

    ![创建自定义角色](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/ghippo/user-guide/access-control/images/custom01.png)

1. 输入名称、描述，选择`文件夹角色`，勾选角色权限后点击`确定`。

    ![文件夹角色](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/ghippo/user-guide/access-control/images/custom06.png)

1. 返回角色列表，搜索刚创建的自定义角色，点击右侧的 `⋮`，可以执行复制、编辑和删除等操作。

    ![更多操作](https://community-github.cn-sh2.ufileos.com/daocloud-docs-images/docs/ghippo/user-guide/access-control/images/custom07.png)

1. 文件夹角色创建成功后，可以去[文件夹](../workspace/folders.md)授权，设定这个角色可以管理哪些文件夹。
