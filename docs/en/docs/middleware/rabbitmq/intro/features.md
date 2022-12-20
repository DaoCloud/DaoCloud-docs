# Features

Common features of RabbitMQ include:

- Reliability
     
    RabbitMQ uses some mechanisms to ensure reliability, such as persistence, transmission confirmation, and release confirmation.

- Message clustering (Clustering)

    Multiple RabbitMQ servers can form a cluster to form a logical Broker.

- Highly Available Queues

    The queue can be mirrored on the hosts in the cluster so that the queue is still available even if some nodes fail.

- Multiple protocols (Multi-protocol)

    RabbitMQ supports multiple message queuing protocols, such as STOMP, MQTT, etc.

- Multilingual client (Many Clients)

    RabbitMQ supports almost all common languages, such as Java, .NET, Ruby, etc.

- Management UI (Management UI)

    RabbitMQ provides an easy-to-use graphical user interface that allows users to monitor and manage all aspects of the message broker.

- Tracking mechanism (Tracing)

    If the message is abnormal, RabbitMQ provides a message tracking mechanism, and users can easily find out what happened.

- Plug-in mechanism (Plugin System)

    RabbitMQ provides many plug-ins that support extensions in many ways, and you can also write your own plug-ins.

After deploying RabbitMQ in DCE 5.0, the following features will also be supported:

- Support single-node and multi-node RabbitMQ cluster deployment
- Support RabbitMQ Managerment plug-in, provide management page
- Support RabbitMQ Prometheus plug-in, expose monitoring indicators
- Use ServiceMonitor to interface with Prometheus to capture indicators
- Support the expansion and rolling upgrade of RabbitMQ cluster