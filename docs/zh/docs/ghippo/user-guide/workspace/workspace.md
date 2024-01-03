---
hide:
  - toc
---

# 创建/删除工作空间

工作空间是一种资源范畴，代表一种资源层级关系。
工作空间可以包含集群、命名空间、注册中心等资源。
通常一个工作空间对应一个项目，可以为每个工作空间分配不同的资源，指派不同的用户和用户组。

参照以下步骤创建一个工作空间。

1. 使用 admin/folder admin 角色的用户登录 DCE 5.0，点击左侧导航栏底部的 __全局管理__ -> __工作空间与层级__ 。

    ![全局管理](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/ghippo/images/ws01.png)

3. 点击右上角的 __创建工作空间__ 按钮。

    ![创建工作空间](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/ws02.png)

4. 填写工作空间名称、所属文件夹等信息后，点击 __确定__ ，完成创建工作空间。

    ![确定](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/ws03.png)

!!! tip

    创建成功后工作空间名称将显示在左侧的树状结构中，以不同的图标表示文件夹和工作空间。

    ![文件夹与工作空间](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/ws04.png)

!!! note

    选中某一个工作空间或文件夹，点击右侧的 __...__ 可以进行编辑或删除。

    - 当该工作空间下资源组、共享资源中存在资源时，该工作空间无法被删除，需要将所有资源解绑后再删除。

    - 当微服务引擎模块在该工作空间下存在接入注册中心资源时，该工作空间无法被删除，需要将所有接入注册中心移除后再删除工作空间。
