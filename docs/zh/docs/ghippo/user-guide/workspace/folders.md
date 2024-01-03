---
hide:
  - toc
---

# 创建/删除文件夹

文件夹具有权限映射能力，能够将用户/用户组在本文件夹的权限映射到其下的子文件夹、工作空间以及资源上。

参照以下步骤创建一个文件夹。

1. 使用 admin/folder admin 角色的用户登录 DCE 5.0，点击左侧导航栏底部的 __全局管理__ -> __工作空间与层级__ 。

    ![全局管理](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/ws01.png)

1. 点击右上角的 __创建文件夹__ 按钮。

    ![创建文件夹](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/fd02.png)

1. 填写文件夹名称、上一级文件夹等信息后，点击 __确定__ ，完成创建文件夹。

    ![确定](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/fd03.png)

!!! tip

    创建成功后文件夹名称将显示在左侧的树状结构中，以不同的图标表示工作空间和文件夹。

    ![工作空间和文件夹](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/ws04.png)

!!! note

    选中某一个文件夹或文件夹，点击右侧的 __...__ 可以进行编辑或删除。

    - 当该文件夹下资源组、共享资源中存在资源时，该文件夹无法被删除，需要将所有资源解绑后再删除。

    - 当微服务引擎模块在该文件夹下存在接入注册中心资源时，该文件夹无法被删除，需要将所有接入注册中心移除后再删除文件夹。
