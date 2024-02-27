---
hide:
  - toc
---

# 移除集群

如果想要从托管网格中移除一个集群，可以按照以下步骤移除集群。

1. 在左侧导航栏点击 __集群纳管__ ，在集群列表右侧，点击 __移除__ 按钮。或者在网格列表中，点击最右侧的 __...__ 按钮，在弹出菜单中选择 __移除__ 。

    ![移除集群](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/remo-cluster01.png)

2. 在弹出窗口中，确认信息无误后，点击 __确定__ 。

    ![移除集群](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/remo-cluster02.png)

    移除集群，需要完成一些前置操作，例如：

    - 卸载已注入的边车。
    - 清除集群相关的网格网关。
    - 其他前置操作，请按屏幕提示操作。

!!! warning

    移除集群，将无法通过网格集中管理集群，另外集群日志等相关信息可能会丢失，请谨慎操作。
