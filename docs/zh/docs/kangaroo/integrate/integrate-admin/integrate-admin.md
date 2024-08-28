# 仓库集成(管理员)

仓库集成(管理员)是集中管理平台镜像仓库的入口，既支持集成外部镜像仓库，如 Harbor Registry、Docker Registry；
又能够自动集成平台创建的托管 Harbor。仓库集成后，平台管理员可以通过将镜像空间与工作空间绑定的方式，
将某个私有镜像空间分配给一个或者多个工作空间（工作空间下的命名空间）。
或者将镜像空间设置为公开，供平台所有命名空间使用。

## 主要功能

- 支持集成主流的镜像仓库，如 Harbor Registry、Docker Registry，帮助您集中管理平台级别的镜像仓库。
- 支持通过概览页，快速查看仓库地址、镜像空间数、存储使用量等数据。
- 支持创建并设置镜像空间状态为公开或私有。若镜像空间状态为公开，其下的镜像能够被平台所有命名空间使用。
  若镜像空间状态为私有，则将镜像空间与一个或多个工作空间绑定后，只有被绑定的工作空间下的命名空间才能够使用该私有镜像，保证私有镜像的安全性。
- 自动集成托管 Harbor，平台创建托管 Harbor 实例后将被自动集成到集成仓库列表，进行统一的管理。

## 功能优势

- 统一管理入口，对集成镜像仓库和托管 Harbor 实例进行统一管理。
- 高安全性，私有镜像只能通过镜像空间与工作空间绑定的方式才能在部署应用时被拉到。
- 方便快捷，镜像空间一旦被设置为公开，则平台范围内的所有命名空间在部署应用时都能够拉取其下的公开镜像。
- 支持主流镜像仓库类型：Harbor Registry、Docker Registry。

## 操作步骤

可以参阅[视频教程](../../videos/kangaroo.md#_3)熟悉以下操作步骤：

1. 使用具有 Admin 角色的用户登录 DCE 5.0，从左侧导航栏点击 __镜像仓库__ -> __仓库集成(管理员)__ 。

    ![仓库集成](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kangaroo/images/integrated01.png)

1. 点击右上角的 __仓库集成__ 按钮。

    ![点击按钮](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/integrated02.png)

1. 选择仓库类型，填写集成名称、仓库地址、用户名和密码，点击 __确定__ 。

    ![填写参数](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/integrated03.png)

    !!! note

        对于 Harbor 仓库，必须提供 Admin 级别的用户名/密码。

1. 返回仓库集成列表。集成的仓库将带有 __集成__ 、 __健康__ 或 __不健康__ 等标签。光标悬浮到某个磁贴上，可以执行 __删除集成__ 、 __编辑__ 等操作。

    ![更多操作](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/integrated04.png)

下一步：[创建镜像空间](../integrate-admin/registry-space.md)
