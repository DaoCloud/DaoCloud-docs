# 镜像空间

DCE 5.0 镜像仓库提供了基于镜像空间的镜像隔离功能。镜像空间分为公开和私有两种类型：

- 公开镜像仓库：所有用户都可以访问，通常存放公开的镜像，默认有一个公开镜像空间。
- 私有镜像仓库：只有授权用户才可以访问，通常存放镜像空间本身的镜像。

您可以选择不同的实例，查看其下的所有镜像空间。

![切换实例](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kangaroo/images/space01.png)

点击某一个镜像空间的名称，可以查看当前空间内的镜像列表以及镜像回收规则。
您可以为当前镜像空间创建镜像回收规则。所有镜像回收规则独立计算并且适用于所有符合条件的镜像，最多支持 15 条回收规则。

![镜像空间包含什么](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kangaroo/images/space02.png)

通过左侧导航栏的 __仓库集成(工作空间)__ 进入镜像空间后，点击右侧的 __推送命令__ 按钮。

![按钮](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kangaroo/images/push-cmd01.png)

可以查看将镜像推送到当前镜像空间的推送命令。

![推送命令](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kangaroo/images/push-cmd02.png)

点击 __上传镜像__ 按钮，可以上传格式为 tar 或 tar.gz 的镜像文件。
注意不要超过 2GB，一个文件对应一个镜像，目前仅支持上传 1.11.2 及以上容器引擎客户端版本制作的镜像压缩包。

![上传镜像](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kangaroo/images/push-cmd03.png)
