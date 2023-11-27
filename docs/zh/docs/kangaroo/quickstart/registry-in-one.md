---
hide:
  - toc
---

# 管理外部镜像仓库

如果您有一个或多个 Harbor 、 Docker 、Jfrog Artifacty 镜像仓库，完全可以用 DCE 5.0 镜像仓库进行统一管理。视操作员的角色权限，可以使用两种方式：

- 仓库集成（工作空间）：支持 Harbor 、 Docker 、Jfrog Artifacty 三种镜像仓库类型
- 仓库集成（管理员）：支持 Harbor 、 Docker 两种镜像仓库类型


## 仓库集成(工作空间)

如果是 Workspace Admin，可以通过仓库集成(工作空间)功能，将现有镜像仓库关联到 DCE 平台，供工作空间的成员使用。简单的操作步骤如下：

1. 以 Workspace Admin 角色登录，从左侧导航栏点击`仓库集成(工作空间)`，点击右上角的`仓库集成`按钮。

    ![仓库集成(工作空间)](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/relate02.png)

2. 填写表单信息后点击`确定`。

    ![填写表单](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/relate03.png)

    !!! note

        1. Docker Registry 镜像仓库若未设置密码可不填写，Harbor 镜像仓库必须填写用户名/密码。
        2. 有关实际操作演示，请参阅[仓库集成视频演示](../../videos/kangaroo.md)。

## 仓库集成(管理员)

如果是 Admin（平台管理员），还可以通过仓库集成功能，将现有镜像仓库集成到 DCE 平台。
仓库集成是集中管理平台镜像仓库的入口，对于 Harbor 镜像仓库平台管理员可以通过将镜像空间与工作空间绑定的方式，
将某个私有镜像空间分配给一个或者多个工作空间（工作空间下的命名空间）使用。或者将镜像空间设置为公开，供平台所有命名空间使用。

1. 以 Admin 角色登录，在左侧导航栏点击`仓库集成(管理员)`。

    ![仓库集成](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/interg01.png)

1. 点击右上角的`仓库集成`按钮。

    ![仓库集成](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/interg02.png)

1. 选择仓库类型，填写集成名称、仓库地址、用户名和密码后点击`确定`。

    ![填写表单](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/interg03.jpg)

1. 在集成的仓库列表中，光标悬浮于某个仓库上，点击眼睛图标可查看概览。

    ![查看概览](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/interg04.jpg)

1. 概览页面显示了当前仓库的基本信息、统计信息，还在顶部提供了快速入门，方便管理镜像空间、工作空间、创建应用。

    ![查看概览](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/interg05.jpg)

    !!! note

        1. Docker Registry 镜像仓库不支持镜像空间与工作空间绑定的能力，若 Docker Registry 未设置密码，则相当于该 Docker Registry 是公开的，平台所有命名空间创建应用时均能拉取其中的全部镜像。