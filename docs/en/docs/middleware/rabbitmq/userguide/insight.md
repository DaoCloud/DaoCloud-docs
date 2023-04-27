# instance monitoring

RabbitMQ has built-in Prometheus and Grafana monitoring modules.

1. On the Message Queue page, click a name.

    

2. In the left navigation bar, click `Instance Monitoring` to access the monitoring module.

    

The monitoring indicators are as follows.

| Panel Name | Indicator Name | Description |
| ------------ | --------- | -------------------------- ------- |
| connections | Connections | This metric is used to count the total number of connections in the RabbitMQ instance. |
| channels | Number of channels | This metric is used to count the total number of channels in the RabbitMQ instance. |
| queues | Number of queues | This metric is used to count the total number of queues in the RabbitMQ instance. |
| consumers | Number of consumers | This indicator is used to count the total number of consumers in the RabbitMQ instance. |
| publish | Production Rate | Statistics on the real-time message production rate in a RabbitMQ instance. |
| socket_used | Number of Socket connections | This indicator is used to count the number of Socket connections used by the current node RabbitMQ. |
| CPU Usage | CPU Usage | This indicator is used to count the CPU usage of the node. |
| Memory Usage | Memory Usage | This indicator is used to count the memory usage of the node. |