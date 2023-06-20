# 仓库集成(工作空间)

仓库集成(工作空间)是针对工作空间提供的便捷接入仓库功能。
工作空间管理员（Workspace Admin）可根据需要为该工作空间灵活接入镜像仓库，供工作空间成员使用。
接入后，成员在工作空间下的命名空间部署应用时可通过`选择镜像`按钮一键拉取工作空间下所有公开和私有的镜像，实现快速部署应用。

- 支持关联 Harbor 和 Docker 两种仓库实例
- 对于 Harbor 实例，除了接入管理员账号外，还可以接入机器人账号达到同样的接入效果

## 优势

- 灵活便捷：工作空间的管理员均可自主接入一个或多个 Harbor / Docker 类型的镜像仓库，供工作空间成员使用。
- 全局联动：接入后，在应用工作台部署应用时，可通过`选择镜像`按钮，一键选择仓库中的镜像，实现快速部署应用。

## 操作步骤

可以参阅[视频教程](../../videos/kangaroo.md#_2)熟悉以下操作步骤：

1. 使用具有 Workspace Admin 角色的用户登录 Web 控制台，从左侧导航栏点击`镜像仓库` -> `仓库集成(工作空间)`。

    ![镜像仓库](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/related01.png)

1. 点击右上角的`仓库集成(工作空间)`按钮。

    ![仓库集成(工作空间)](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/relate02.png)

1. 填写表单信息后点击`确定`。

    ![填写表单](https://docs.daocloud.io/daocloud-docs-images/docs/kangaroo/images/relate03.png)

    !!! note

        1. Docker Registry 镜像仓库若未设置密码可不填写，Harbor 仓库必须填写用户名/密码。
        1. 有关实际操作演示，请参阅[仓库集成(工作空间)视频演示](../../videos/kangaroo.md)
