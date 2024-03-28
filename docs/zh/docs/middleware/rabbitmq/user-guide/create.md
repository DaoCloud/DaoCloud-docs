---
hide:
  - toc
---

# 创建 RabbitMQ

在 RabbitMQ 消息队列中，执行以下操作：

1. 在右上角点击 __新建实例__ 。

    ![点击新建实例](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/rabbitmq/images/mq03.png)

2. 在 __创建 RabbitMQ 实例__ 页面中，设置基本信息后，点击 __下一步__ 。

    ![基本信息](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/rabbitmq/images/mq04.png)

3. 配置规格后，点击 __下一步__ 。

    - 版本：RabbitMQ 的版本号，当前仅支持 RabbitMQ 3.7.20。
    - 副本数：支持 1、3、5、7 副本数。
    - 资源配额：根据实际情况选择规则。
    - 存储卷：选择 RabbitMQ 实例的存储卷和储存空间总量。

    ![配置规格](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/rabbitmq/images/mq05.png)

4. 服务设置后，点击 __下一步__ 。

    - 访问方式：可以选择集群内访问还是 Nodeport 访问。
    - 服务设置：设置连接 RabbitMQ 实例的用户名、密码。

    ![服务设置](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/rabbitmq/images/mq06.png)

5. 确认实例信息无误，点击 __确定__ 完成创建。

    ![确认](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/rabbitmq/images/mq07.png)

6. 在实例列表页查看实例是否创建成功。刚创建的实例状态为 __未就绪__ ，等几分钟后该状态变为 __运行中__ 。

    ![状态](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/rabbitmq/images/mq09.png)
