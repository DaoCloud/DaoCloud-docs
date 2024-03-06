# 镜像同步

镜像同步是指将两个或多个镜像仓库之间的镜像进行同步更新的过程。
在软件开发或系统管理中，这种同步更新方式常用于确保在多个服务器之间共享相同的软件或操作系统镜像，
以便在进行部署时能够确保一致性和减少工作量。通常情况下，通过镜像同步可以实时地将镜像内容同步到其他服务器上，
从而保证多个服务器上的镜像都是最新版本。

DCE 5.0 镜像仓库可以让用户创建同步规则，添加目标仓库等。

!!! note

    创建同步规则和添加目标仓库需要管理员权限。

## 创建同步规则

1. 从仓库集成或托管 Harbor 页面中，点击某个仓库。

    ![选择一个仓库](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kangaroo/images/sync00.png)

1. 在左侧导航栏，依次点击 __镜像同步__ -> __同步规则__ ，点击 __创建同步规则__ 按钮。

    ![点击按钮](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kangaroo/images/sync01.png)

1. 填写各项参数后点击 __确定__ 。

    ![配置参数](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kangaroo/images/sync02.png)

    同步模式：
    - 推送：将镜像同步到目标仓库
    - 拉取：把目标仓库的镜像同步到当前仓库
    - 覆盖：指定如果存在相同资源的名称，是否要覆盖
    镜像过滤器：
    - 名称：按名称过滤当前镜像空间下的资源，不填或 `**` 将匹配所有资源。
    - Tag：按 tag/version 过滤当前镜像空间下的资源，不填或 `**` 将匹配所有资源。
    目标镜像空间：如果不填写，镜像将被放到与源仓库相同的镜像空间中。

1. 返回同步规则列表，新建的规则默认处于启用状态。点击右侧的 __⋮__ ，可以执行同步、编辑、禁用、删除等操作。

    ![更多操作](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kangaroo/images/sync03.png)

## 添加目标仓库

1. 从仓库集成或托管 Harbor 页面中，点击某个仓库。

    ![选择一个仓库](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kangaroo/images/sync00.png)

1. 在左侧导航栏，依次点击 __镜像同步__ -> __目标仓库__ ，点击 __添加目标仓库__ 按钮。

    ![点击按钮](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kangaroo/images/target01.png)

1. 可以点选已集成的仓库，或自定义仓库。

    ![选择](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kangaroo/images/target02.png)

    ![自定义](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kangaroo/images/target03.png)

1. 返回目标仓库列表，点击右侧的 __⋮__ ，可以执行编辑、删除等操作。
