# scenes to be used

Compared with [RabbitMQ](../../rabbitmq/intro/index.md), Kafka message queue is suitable for Cases such as building real-time data pipelines, streaming data processing, third-party decoupling, and traffic peak shaving and valley removal. It has the characteristics of large-scale, high reliability, high concurrent access, scalability, and full hosting.

## Comparison with RabbitMQ

As the saying goes, there is no best technology, only the most suitable technology. Each messaging middleware service has its own advantages and disadvantages. Here is a simple comparison between RabbitMQ and Kafka.

| | Kafka | RabbitMQ |
| ---------- | -------------------------------------- ---------------------- | --------------------------- ------------------------------------ |
| Performance | Single-node QPS reaches one million, high throughput | Single-node QPS is ten thousand, low throughput |
| Reliability | Multi-copy mechanism, high data reliability | Multi-copy mechanism, high data reliability |
| Function | Persistence<br />Transaction Message<br />Sequence at Single Partition Level| Persistence<br />Priority Queue<br />Delay Queue<br />Dead Letter Queue<br />Transaction Message |
| Consumption mode | Message filtering<br />Client actively pulls<br />Message backtracking<br />Broadcast consumption | Client actively pulls and server pushes<br />Broadcast consumption |
| Client Support| Only supports Kafka custom protocol<br />Written in Scala and Java<br />Supports SSL/SASL authentication and read and write permission control| Supports MQTT, STOMP and other protocols<br />Written in Erlang <br />Support SSL/SASL authentication and read and write permission control |
| Service Availability | Using cluster deployment, partition and multi-copy design, using a single agent downtime has no impact on services, and supports linear increase in message capacity | Supports cluster deployment, and the number of cluster agents has various specifications |
| Others| Message accumulation<br />Flow control: support client and user levels, flow control can be applied to producers or consumers through active settings| Message tracking<br />Message accumulation<br />Multi-tenancy<br /> >Flow control: Flow control is based on the Credit-based algorithm, which is an internal passively triggered protection mechanism and acts on the producer level |

In short, Kafka uses the pull method to consume messages, which has a relatively higher throughput and is suitable for massive data collection and delivery cases, such as log collection and centralized analysis.

However, RabbitMQ is developed based on the Erlang language, which is not conducive to secondary development and maintenance. It is suitable for use cases that have high requirements for routing, load balancing, data consistency, stability and reliability, but not so high requirements for performance and throughput.

## Typical scene

As a popular message queue middleware, Kafka has an efficient and reliable message asynchronous delivery mechanism, mainly used for data exchange and delivery between different systems, in enterprise solutions, financial payment, telecommunications, e-commerce, social networking, instant messaging, Video, Internet of Things, Internet of Vehicles and many other fields have a wide range of applications.

1. Asynchronous communication

    The non-core or unimportant process part of the business is sent to the target system by asynchronous message notification, so that the main business process does not need to wait for the processing results of other systems synchronously, so as to achieve the purpose of rapid system response.

    For example, in the user registration scenario of the website, after the user registers successfully, registration emails and registration SMSs need to be sent. These two processes use Kafka message service to notify the email sending system and SMS sending system, thereby improving the response speed of the registration process.

2. Peak stagger flow control and flow clipping

    In e-commerce or large-scale websites, there are differences in the processing capabilities of upstream and downstream systems. The sudden flow of upstream systems with high processing capabilities may impact some downstream systems with low processing capabilities. It is necessary to improve system availability while reducing system implementation. complexity.
    When traffic floods such as e-commerce sales promotions suddenly hit, queue services can be used to accumulate and cache orders and other information, and then process them when the downstream system is capable of processing the messages, so as to avoid the downstream subscription system from collapsing due to sudden traffic.
    The message queue provides hundreds of millions of message accumulation capabilities, with a default retention period of 3 days, and the message consumption system can process messages during off-peak hours.

    In addition, in cases where traffic surges in a short period of time, such as commodity flash sales and panic buying, in order to prevent back-end applications from being overwhelmed, Kafka message queues can be used to transmit requests between front-end and back-end systems.

3. Log synchronization

    In the design of large-scale business systems, in order to quickly locate problems, track logs across the entire link, and monitor faults in a timely manner, it is usually necessary to centrally analyze and process the logs of each system application.

    The original intention of Kafka design is to cope with a large number of log transmission cases. The application synchronizes log messages to the message service in a reliable and asynchronous manner, and then uses other components to analyze the logs in real time or offline. It can also be used to collect key log information for application monitoring.

    Log synchronization has three key parts: the log collection client, the Kafka message queue, and the backend log processing application.