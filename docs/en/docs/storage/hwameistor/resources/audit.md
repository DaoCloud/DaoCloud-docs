为了记录 HwameiStor 集群系统的使用和操作历史信息，HwameiStor 提供了系统审计日志。该审计日志具有 HwameiStor 系统语义，易于用户查阅、解析。审计日志记录了 HwameiStor 系统中各类资源的使用操作信息，包括 Cluster、Node、StoragePool、Volume 等。

您可以通过以下步骤查看审计日志：

1. 在 HwameiStor 界面底部的菜单栏中，点击 "审计" 按钮。

2. 在审计页面中，您可以看到操作类型、资源名称、资源类型、状态、操作时间和操作内容等字段。

   ![audit01](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/storage/images/auit01.png)

   其中资源类型支持：

   - Cluster
   - StorageNode
   - Disk
   - DiskNode
   - Pool
   - Volume
   - DiskVolume

   操作内容：您可以查看更多的操作细节信息。下图展示了 `StorageNode` 资源的一条审计操作内容。

   ![audit02](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/storage/images/audit02.png)
