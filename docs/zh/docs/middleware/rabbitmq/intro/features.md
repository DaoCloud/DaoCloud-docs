# 功能特性

RabbitMQ 的通用功能特性包括：

- 可靠性（Reliability）

    RabbitMQ 使用一些机制来保证可靠性，如持久化、传输确认、发布确认。

- 消息集群（Clustering）

    多个 RabbitMQ 服务器可以组成一个集群，形成一个逻辑 Broker。

- 高可用队列（Highly Available Queues）

    队列可以在集群中的主机上进行镜像，使得在部分节点出问题的情况下队列仍然可用。

- 多种协议（Multi-protocol）

    RabbitMQ 支持多种消息队列协议，比如 STOMP、MQTT 等。

- 多语言客户端（Many Clients）

    RabbitMQ 几乎支持所有常用语言，比如 Java、.NET、Ruby 等。

- 管理界面（Management UI）

    RabbitMQ 提供了一个易用的图形用户界面，使得用户可以监控和管理消息 Broker 的方方面面。

- 跟踪机制（Tracing）

    如果消息异常，RabbitMQ 提供了消息跟踪机制，用户可以轻松找出发生了什么。

- 插件机制（Plugin System）

    RabbitMQ 提供了许多插件，支持从多方面进行扩展，也可以编写自己的插件。

在 DCE 5.0 中部署 RabbitMQ 后，还将支持以下特性：

- 支持单节点和多节点 RabbitMQ 集群部署
- 支持 RabbitMQ Managerment 插件，提供管理页面
- 支持 RabbitMQ Prometheus 插件，暴露监控指标
- 使用 ServiceMonitor 对接 Prometheus 抓取指标
- 支持 RabbitMQ 集群的扩容和滚动升级
