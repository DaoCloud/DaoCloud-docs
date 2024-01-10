# 删除网格网关

如果想要删除一个或多个网关，可以参照本文来操作。

## 删除一个网关

!!! caution

    删除网关之前，需要检查相应的 Gateway 和 VirtualService 资源，否则会有无效配置，导致流量异常。

以下操作步骤是推荐的操作，可以防止误删除。

1. 进入某个网格后，在左侧导航栏点击 __网格网关__ ，在列表右侧点击  __⋮__  按钮，在弹出菜单中选择 __删除__ 。

    ![删除网关](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/delete-gate01.png)

    你也可以勾选某个网关前的复选框后，点击 __删除__ 按钮。

2. 在弹出窗口中，确认信息无误后，点击 __确定__ ，该网关将被删除。

    ![删除网关](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/delete-gate02.png)

!!! warning

    删除网关后，该网关相关的信息将会丢失，请谨慎操作。

## 批量删除

如果确实需要一次性删除多个网关，可以采用此项操作。

1. 在网关列表中勾选多个网关后，点击右上角的 __删除__ 按钮。

    ![删除网关](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/delete-gate03.png)

2. 在弹出窗口中，确认信息无误后，点击 __确定__ ，选中的网关将全部被删除。

!!! warning
    
    如非必要，请勿使用批量删除功能，删除的网关无法恢复，请谨慎操作。
