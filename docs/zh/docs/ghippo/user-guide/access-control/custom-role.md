# 自定义角色

DCE 5.0 支持创建三种范围的自定义角色：

- **平台角色** 的权限对平台所有相关资源生效
- **工作空间角色** 的权限对该用户所在的工作空间下的资源生效
- **文件夹角色** 的权限对该用户所在的文件夹及其下的子文件夹和工作空间资源生效

## 创建平台角色

平台角色是粗粒度角色，能够对所选权限内的所有资源生效。如授权后用户可以拥有所有工作空间的查看权限、所有集群的编辑权限等，而不能针对某个工作空间或某个集群生效。平台角色创建完成后可以在用户/用户组列表中进行授权。

1. 从左侧导航栏点击 __全局管理__ -> __用户与访问控制__ -> __角色__ ，点击 __创建自定义角色__ 。

    ![创建自定义角色](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/user-guide/access-control/images/custom01.png)

1. 输入名称、描述，选择 __平台角色__ ，勾选角色权限后点击 __确定__ 。

    ![平台角色](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/user-guide/access-control/images/custom02.png)

1. 返回角色列表，搜索刚创建的自定义角色，点击右侧的 __⋮__ ，可以执行复制、编辑和删除等操作。

    ![更多操作](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/user-guide/access-control/images/custom03.png)

1. 平台角色创建成功后，可以去[用户](./user.md)/[用户组](./group.md)授权，为这个角色添加用户和用户组。

## 创建工作空间角色

工作空间角色是细粒度角色，针对某个工作空间生效。如在该角色中选择应用工作台的全部权限，给用户在某个工作空间下授予该角色后，该用户将仅能在该工作空间下使用应用工作台相关的功能，而无法使用如微服务引擎、中间件等其他模块的能力。工作空间角色创建完成后，可以在工作空间与层级中选择工作空间后进行授权。

1. 从左侧导航栏点击 __全局管理__ -> __用户与访问控制__ -> __角色__ ，点击 __创建自定义角色__ 。

    ![创建自定义角色](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/user-guide/access-control/images/custom01.png)

1. 输入名称、描述，选择 __工作空间角色__ ，勾选角色权限后点击 __确定__ 。

    ![工作空间角色](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/user-guide/access-control/images/custom04.png)

1. 返回角色列表，搜索刚创建的自定义角色，点击右侧的 __⋮__ ，可以执行复制、编辑和删除等操作。

    ![更多操作](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/user-guide/access-control/images/custom05.png)

1. 工作空间角色创建成功后，可以去[工作空间](../workspace/workspace.md)授权，设定这个角色可以管理哪些工作空间。

## 创建文件夹角色

文件夹角色针对某个文件夹和该文件夹下的所有子文件夹及工作空间生效。如在该角色中选择全局管理-工作空间和应用工作台，给用户在某个文件夹下授予该角色后，该用户将能够在其下的所有工作空间中使用应用工作台的相关功能，而无法使用如微服务引擎、中间件等其他模块的能力。文件夹角色创建完成后，可以在工作空间与层级中选择文件夹后进行授权。
请注意：应用工作台、多云编排、镜像仓库、微服务引擎、服务网格和中间件均依赖于工作空间，因此在创建文件夹角色时大部分场景下需要用到工作空间，请注意在全局管理-工作空间下勾选。

1. 从左侧导航栏点击 __全局管理__ -> __用户与访问控制__ -> __角色__ ，点击 __创建自定义角色__ 。

    ![创建自定义角色](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/user-guide/access-control/images/custom01.png)

1. 输入名称、描述，选择 __文件夹角色__ ，勾选角色权限后点击 __确定__ 。

    ![文件夹角色](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/user-guide/access-control/images/custom06.png)

1. 返回角色列表，搜索刚创建的自定义角色，点击右侧的 __⋮__ ，可以执行复制、编辑和删除等操作。

    ![更多操作](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/user-guide/access-control/images/custom07.png)

1. 文件夹角色创建成功后，可以去[文件夹](../workspace/folders.md)授权，设定这个角色可以管理哪些文件夹。
