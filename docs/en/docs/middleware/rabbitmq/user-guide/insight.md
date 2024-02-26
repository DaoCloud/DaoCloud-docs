---
hide:
  - toc
---

# instance monitoring

RabbitMQ has built-in Prometheus and Grafana monitoring modules.

1. On the Message Queue page, click a name.

    <!--screenshot-->

2. In the left navigation bar, click __Instance Monitoring__ to access the monitoring module.

    <!--screenshot-->

The monitoring metrics are as follows.

| Panel Name | Metrics | Description |
| ------------ | --------- | -------------------------- ------- |
| connections | Connections | This metric is used to count the total number of connections in the RabbitMQ instance. |
| channels | Number of channels | This metric is used to count the total number of channels in the RabbitMQ instance. |
| queues | Number of queues | This metric is used to count the total number of queues in the RabbitMQ instance. |
| consumers | Number of consumers | This metric is used to count the total number of consumers in the RabbitMQ instance. |
| publish | Production Rate | Statistics on the real-time message production rate in a RabbitMQ instance. |
| socket_used | Number of Socket connections | This metric is used to count the number of Socket connections used by the current node RabbitMQ. |
| CPU Usage | CPU Usage | This metric is used to count the CPU usage of the node. |
| Memory Usage | Memory Usage | This metric is used to count the memory usage of the node. |