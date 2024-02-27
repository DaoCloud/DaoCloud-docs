---
hide:
  - toc
---

# 删除网格

当用户不再使用网格治理服务时可以使用删除操作，删除网格需用户完成一系列前置操作，才可以激活对话框的 __确定__ 按钮。

!!! danger

    执行删除操作后，网格不可恢复，如需再次纳管，需重新创建网格。

1. 在网格列表的右侧，点击 __...__ 按钮，在弹出菜单中选择 __删除__ 。

    ![删除网格](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/deletemesh01.png)

1. 按照网格类型，系统将自动检测是否满足删除条件。

    - 删除外接网格。只需输入网格名称确认，就能完成删除操作。

        ![外接网格](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/deletemesh02.png)

    - 删除专有网格。需要按提示关闭网格删除保护、移除边车、清除网关后，输入网格名称确认删除操作。

        ![专有网格](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/deletemesh03.png)

    - 删除托管网格。需要按提示关闭网格删除保护、移除已注入的边车、清除网关、移除网格下的集群后，输入网格名称确认删除操作。

        ![托管网格](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/deletemesh04.png)
