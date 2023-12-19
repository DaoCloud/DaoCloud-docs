# 共享存储池

DCE 5.0 容器管理模块支持将一个存储池共享给多个命名空间使用，以便提高资源利用效率。

1. 在存储池列表中找到需要共享的存储池，在右侧操作栏下点击 __授权命名空间__ 。

    ![授权](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/sc-share01.png)

2. 点击 __自定义命名空间__ 可以逐一选择需要将此存储池共享到哪些命名空间。

    - 点击 __授权所有命名空间__ 可以一次性将此存储池共享到当前集群下的所有命名空间。
    - 在列表右侧的操作栏下方点击 __移除授权__ ，可以解除授权，停止将此存储池共享到该命名空间。

        ![授权](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/sc-share02.png)
