# RabbitMQ 数据迁移

RabbitMQ 的数据包括元数据（RabbitMQ 用户、vhost、队列、交换和绑定）和消息数据，其中消息数据存储在单独的消息存储库中。

由于业务需要，要求把 `rabbitmq-cluster-a` 集群上的数据迁移到 `rabbitmq-cluster-b` 集群上。

## 数据迁移步骤

!!! info

    从 V3.7.0 开始，RabbitMQ 将所有消息数据存储在 `msg_stores/vhosts` 目录中，并存储在每个 vhost 的子目录中。
    每个 vhost 目录都以哈希命名，并包含一个带有 vhost 名称的 `.vhost` 文件，因此可以单独备份特定 vhost 的消息集。
    了解[更多信息](https://www.rabbitmq.com/backup.html)。

RabbitMQ 数据迁移，可以采用如下两种方案：

- 方案一：不迁移数据，先切换生产端，再切换消费端。
- 方案二：先迁移数据，然后同时切换生产端和消费端。

### 方案一

不迁移数据，先切换生产端，再切换消费端。

#### 操作流程

1. 将消息生产端切换到集群 `rabbitmq-cluster-b`，不再生产消息到 `rabbitmq-cluster-a` 集群中。
2. 消费端同时消费 `rabbitmq-cluster-a` 和 `rabbitmq-cluster-b` 集群中的消息，当 `rabbitmq-cluster-a` 集群中消息全部消费完后，将消息消费端切换到 `rabbitmq-cluster-b` 集群中，完成数据迁移。

#### 验证方法

- 在 RabbitMQ Management Web UI 页面查看。

    ![查看](../images/migrate01.png)

- 调用 API 查看

    ```shell
    curl -s -u username:password -XGET http://ip:port/api/overview
    ```

    参数说明：

    - username：使用`rabbitmq-cluster-a`集群的RabbitMQ Management WebUI的帐号
    - password：使用`rabbitmq-cluster-a`集群的RabbitMQ Management WebUI的密码
    - ip：使用`rabbitmq-cluster-a`集群的RabbitMQ Management WebUI的IP地址
    - port：使用`rabbitmq-cluster-a`集群的RabbitMQ Management WebUI的端口号

- 在 Overview 视图中，消费消息数（Ready）以及未确定的消息数（Unacked）都为 0，说明消费完成。

    ![消息数为0](../images/migrate02.png)

### 方案二

先迁移数据，然后同时切换生产端和消费端。借助 shove 插件完成数据迁移。

> shovel 迁移数据的原理是消费`rabbitmq-cluster-a`集群中的消息，将消息生产到`rabbitmq-cluster-b`集群中，迁移后`rabbitmq-cluster-a`集群中的消息被清空，建议离线迁移，业务会出现中断。

`rabbitmq-cluster-a` 和 `rabbitmq-cluster-b` 均需要开启 shovel 插件。

![开启插件](../images/migrate03.png)

参数说明:

- Name: 配置 shovel 的名称。
- Source: 指定协议类型、连接的源集群地址，源端的类型。
- Prefech count: 表示 shovel 内部缓存（从源端集群到目的集群之间的缓存部分）的消息条数。
- Auto-delete: 默认为 Never，表示不删除本集群消息，如果设置为 `After initial length transferred`，则在消息转移完成后删除。
- Destination: 指定协议类型，连接目标集群地址，目标端的类型。
- Add forwarding headers: 设置为 `true`，则会在转发的消息内添加 x-shovelled 的 header 属性。
- Reconnect delay：指定在 Shovel link 失效的情况下，重新建立连接前需要等待的时间，单位为秒。如果设置为 0，则不会进行重连动作，即 Shovel 会在首次连接失效时停止工作。默认为 5 秒。
- Acknowledgement mode：参考 Federation 的配置。

    - `no ack` 表示无须任何消息确认行为；
    - `on publish` 表示 Shovel 会把每一条消息发送到目的端之后再向源端发送消息确认；
    - `on confirm` 表示 Shovel 会使用 publisher confirm 机制，在收到目的端的消息确认之后再向源端发送消息确认。

#### 迁移前消息数量

![迁移前消息](../images/migrate04.png)

#### 配置 shovel 信息

![配置 shovel](../images/migrate05.png)

#### shovel 运行状态

![运行状态](../images/migrate06.png)

当 shovel 状态为 “running” 时，表示迁移开始。等数据迁移完成后，将生产端、消费端切换至 `rabbitmq-cluster-b` 集群中，完成迁移过程。

#### 迁移后消息数量

- rabbitmq-cluster-a 集群消息情况

    ![集群消息](../images/migrate07.png)

- rabbitmq-cluster-b 集群消息情况

    ![集群消息](../images/migrate08.png)
