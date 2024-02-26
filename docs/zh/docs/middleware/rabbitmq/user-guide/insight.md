---
hide:
  - toc
---

# 实例监控

RabbitMQ 内置了 Prometheus 和 Grafana 监控模块。

1. 在消息队列页面中，点击某个名称。

    ![点击某个名称](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/rabbitmq/images/view01.png)

2. 在左侧导航栏，点击 __实例监控__ ，可以接入监控模块。

    ![实例监控](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/rabbitmq/images/insight.png)

各项监控指标如下。

| Panel 名      | 指标名称      | 说明                                |
| ------------ | --------- | --------------------------------- |
| connections  | 连接数       | 该指标用于统计 RabbitMQ 实例中的总连接数。          |
| channels     | 通道数       | 该指标用于统计 RabbitMQ 实例中的总通道数。          |
| queues       | 队列数       | 该指标用于统计 RabbitMQ 实例中的总队列数。          |
| consumers    | 消费者数      | 该指标用于统计 RabbitMQ 实例中的总消费者数。         |
| publish      | 生产速率      | 统计 RabbitMQ 实例中实时消息生产速率。            |
| socket_used | Socket 连接数 | 该指标用于统计当前节点 RabbitMQ 所使用的 Socket 连接数。 |
| CPU Usage    | CPU 使用量    | 该指标用于统计节点 CPU 使用量。                  |
| Memory Usage | 内存使用量     | 该指标用于统计节点内存使用量。                   |
