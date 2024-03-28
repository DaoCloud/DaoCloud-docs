---
hide:
  - toc
---

# 创建 Kafka

在 Kafka 消息队列中，执行以下操作创建 Kafka 实例。

1. 在右上角点击 __新建实例__ 。

    ![新建实例](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/kafka/images/create01.png)

2. 在 __创建 Kafka 实例__ 页面中，设置基本信息后，点击 __下一步__ 。

    ![设置基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/kafka/images/create02.png)

3. 配置规格后，点击 __下一步__ 。

    - 版本：Kafka 的版本号，当前仅支持 Kafka 3.1.0。
    - 副本数：支持 1、3、5、7 副本数。
    - 资源配额：根据实际情况选择规则。
    - 存储卷：选择 Kafka 实例的存储卷和储存空间总量。

    ![配置规格](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/kafka/images/create03.png)

4. 服务设置后，点击 __下一步__ 。

    - 访问方式：可以选择集群内访问还是 Nodeport 访问。
    - 服务设置：设置连接 Kafka 实例的用户名、密码。

    ![服务设置](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/kafka/images/create04.png)

5. 确认实例配置信息无误，点击 __确定__ 完成创建。

    ![点击 __确定__ ](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/kafka/images/create05.png)

6. 在实例列表页查看实例是否创建成功。刚创建的实例状态为 __未就绪__ ，等几分钟后该状态变为 __运行中__ 。

    ![查看状态](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/kafka/images/create06.png)
