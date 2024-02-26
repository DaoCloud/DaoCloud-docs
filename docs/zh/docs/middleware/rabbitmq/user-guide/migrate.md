# RabbitMQ 数据迁移

RabbitMQ 的数据包括元数据（RabbitMQ 用户、vhost、队列、交换和绑定）和消息数据，其中消息数据存储在单独的消息存储库中。

由于业务需要，要求把 __rabbitmq-cluster-a__  集群上的数据迁移到 __rabbitmq-cluster-b__  集群上。

## 数据迁移步骤

!!! info

    从 V3.7.0 开始，RabbitMQ 将所有消息数据存储在 __msg_stores/vhosts__  目录中，并存储在每个 vhost 的子目录中。
    每个 vhost 目录都以哈希命名，并包含一个带有 vhost 名称的 __.vhost__  文件，因此可以单独备份特定 vhost 的消息集。
    了解[更多信息](https://www.rabbitmq.com/backup.html)。

RabbitMQ 数据迁移，可以采用如下两种方案：

- 方案一：不迁移数据，先切换生产端，再切换消费端。
- 方案二：先迁移数据，然后同时切换生产端和消费端。

### 方案一

不迁移数据，先切换生产端，再切换消费端。

#### 操作流程

1. 将消息生产端切换到集群 __rabbitmq-cluster-b__ ，不再生产消息到 __rabbitmq-cluster-a__  集群中。
2. 消费端同时消费 __rabbitmq-cluster-a__  和 __rabbitmq-cluster-b__  集群中的消息。当 __rabbitmq-cluster-a__  集群中消息全部消费完后，将消息消费端切换到 __rabbitmq-cluster-b__  集群中，完成数据迁移。

#### 验证方法

- 在 RabbitMQ Management Web UI 页面查看。

    ![查看](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/rabbitmq/images/migrate01.png)

- 调用 API 查看

    ```shell
    curl -s -u username:password -XGET http://ip:port/api/overview
    ```

    参数说明：

    - username：使用 __rabbitmq-cluster-a__  集群的 RabbitMQ Management WebUI 的帐号
    - password：使用 __rabbitmq-cluster-a__  集群的 RabbitMQ Management WebUI 的密码
    - ip：使用 __rabbitmq-cluster-a__  集群的 RabbitMQ Management WebUI 的 IP 地址
    - port：使用 __rabbitmq-cluster-a__  集群的 RabbitMQ Management WebUI 的端口号

- 在 Overview 视图中，消费消息数（Ready）以及未确定的消息数（Unacked）都为 0，说明消费完成。

    ![消息数为 0](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/rabbitmq/images/migrate02.png)

### 方案二

先迁移数据，然后同时切换生产端和消费端。借助 shove 插件完成数据迁移。

> shovel 迁移数据的原理是消费 __rabbitmq-cluster-a__ 集群中的消息，将消息生产到 __rabbitmq-cluster-b__  集群中，迁移后 __rabbitmq-cluster-a__  集群中的消息被清空，建议离线迁移，业务会出现中断。

 __rabbitmq-cluster-a__  和 __rabbitmq-cluster-b__  均需要开启并配置 shovel 插件。

#### 启用 __shovel__ 

##### 开启插件

1. 进入 __中间件__  -> __RabbitMQ__  的实例列表，进入 __rabbitmq-cluster-a__  的概览页面点击 __控制台__ 按钮;

    ![控制台](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/rabbitmq/images/migrate10.png)

2. 执行以下命令，该过程可能会持续一两分钟：

    ```shell
    rabbitmq-plugins enable rabbitmq_shovel rabbitmq_shovel_management
    ```

    ![执行命令](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/rabbitmq/images/migrate11.png)

3. 进入 RabbitMQ 管理平台，在 __admin__  页签下可以看到 shovel 相关的插件信息。

    ![开启插件](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/rabbitmq/images/migrate09.png)

进入实例 __rabbitmq-cluster-b__  的概览页面，再次执行以上操作。

##### 基本配置

![插件配置](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/rabbitmq/images/migrate03.png)

参数说明：

- Name: 配置 shovel 的名称。
- Source: 指定协议类型、连接的源集群地址，源端的类型。
- Prefech count: 表示 shovel 内部缓存（从源端集群到目的实例之间的缓存部分）的消息条数。
- Auto-delete: 默认为 Never，表示不删除本集群消息，如果设置为 __After initial length transferred__ ，则在消息转移完成后删除。
- Destination: 指定协议类型，连接目标集群地址，目标端的类型。
- Add forwarding headers: 设置为 __true__ ，则会在转发的消息内添加 x-shovelled 的 header 属性。
- Reconnect delay：指定在 Shovel link 失效的情况下，重新建立连接前需要等待的时间，单位为秒。如果设置为 0，则不会进行重连动作，即 Shovel 会在首次连接失效时停止工作。默认为 5 秒。
- Acknowledgement mode：参考 Federation 的配置。

    - __no ack__  表示无须任何消息确认行为；
    - __on publish__  表示 Shovel 会把每一条消息发送到目的端之后再向源端发送消息确认；
    - __on confirm__  表示 Shovel 会使用 publisher confirm 机制，在收到目的端的消息确认之后再向源端发送消息确认。

!!! note

    服务地址（图中的 3 和 4）设置格式：amqp://用户名:密码@{rabbitmq服务地址}

下图是一个简单的配置示例

![配置示例](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/middleware/rabbitmq/images/migrate12.png)

#### 启动迁移

迁移任务将自动启动，当 shovel 状态为 __running__  时，表示迁移开始，如下图所示。

![运行状态](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/rabbitmq/images/migrate06.png)

迁移前后观察两个集群的队列状态，可明显看到数据迁移变化：

- 迁移启动前 __rabbitmq-cluster-a__  集群消息情况。

    ![迁移前消息](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/rabbitmq/images/migrate04.png)

- 迁移启动后 __rabbitmq-cluster-a__  集群消息情况，可见队列消息已迁出。

    ![集群消息](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/rabbitmq/images/migrate07.png)

- 迁移启动后 __rabbitmq-cluster-b__  集群消息情况，可见队列消息已迁入该集群。

    ![集群消息](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/rabbitmq/images/migrate08.png)


数据迁移完成后，即可将生产端、消费端切换至 __rabbitmq-cluster-b__  集群中，完成迁移过程。

