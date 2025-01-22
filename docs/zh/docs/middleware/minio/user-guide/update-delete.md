# 更新、删除 MinIO 实例

## 更新 MinIO 实例

如果想要更新或修改 MinIO 的资源配置，可以执行如下操作：

1. 在实例列表中，点击右侧的 __...__  按钮，在弹出菜单中选择 __更新实例__ 。

    ![选择 __更新实例__ ](../images/update01.png)

2. 修改基本信息，然后点击 __下一步__ 。

    - 仅支持修改描述信息
    - 实例名称、部署位置不可修改

        ![基本信息](../images/update02.png)

3. 修改规格配置，然后点击 __下一步__ 。

    - 仅支持修改：CPU 配额、内存配额和储存容量
    - 不可修改：版本、部署模式、副本数、存储池、每副本磁盘数

    ![规格配置](../images/update03.png)

4. 修改服务设置，然后点击 __确定__ 。

    ![服务设置](../images/update04.png)

5. 返回实例列表，屏幕右上角将显示消息： __更新实例成功__ 。

    ![成功](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/minio/images/update05.png)

## 删除 MinIo 实例

如果想要删除一个实例，可以执行如下操作：

1. 在实例列表中，点击右侧的 __...__  按钮，在弹出菜单中选择 __删除实例__ 。

    ![选择删除实例](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/minio/images/delete01.png)

2. 在弹窗中输入该实例列表的名称，确认无误后，点击 __删除__ 按钮。

    !!! warning

        删除实例后，该实例相关的所有消息也会被全部删除，请谨慎操作。

    ![点击删除](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/minio/images/delete02.png)
