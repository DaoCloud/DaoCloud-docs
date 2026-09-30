# Basic Concepts of RocketMQ

This page lists some basic concepts of RocketMQ to help you better understand and use RocketMQ.

## Topic

A topic is a top-level container that is used in RocketMQ to transfer and store
messages that belong to the same business logic.

## MessageType

Categories defined by message transfer characteristics for type management and security
verification. RocketMQ support NORMAL, FIFO, TRANSACTION and DELAY message type.

!!! info

    Starting from version 5.0, RocketMQ supports enforcing the validation of message types,
    that is, each topic only allows messages of a single type to be sent. This can better
    facilitate operation and management of production systems and avoid confusion. However,
    to ensure backward compatibility with version 4.x, the validation feature is disabled
    by default. It is recommended to enable it manually through the server parameter
    "enableTopicMessageTypeCheck".

## MessageQueue

MessageQueue is a container that is used to store and transmit messages in RocketMQ.
MessageQueue is the smallest unit of storage for RocketMQ messages.

## Message

A message is the smallest unit of data transmission in RocketMQ. A producer encapsulates
the load and extended attributes of business data into messages and sends the messages
to an RocketMQ broker. Then, the broker delivers the messages to the consumer based on
the relevant semantics.

## MessageView

MessageView is read-only interface to message from a development perspective.
The message view allows you to read multiple properties and payload information
inside a message, but you cannot make any changes to the message itself.

## MessageTag

MessageTag is a fine-grained message classification property that allows message
to be subdivided below the topic level. Consumers implement message filtering by
subscribing to specific tags.

## MessageOffset

Messages are stored in the queue in order of precedence, each message has a
unique coordinate of type Long in the queue, which is defined as the message site.

## ConsumerOffset

A message is not removed from the queue immediately after it has been consumed
by a consumer, RocketMQ will record the last consumed message based on each consumer group.

## MessageKey

MessageKey is The message-oriented index property. By setting the message index,
you can quickly find the corresponding message content.

## Producer

A producer in RocketMQ is a functional messaging entity that creates messages and
sends them to the server. A producer is typically integrated on the business system
and serves to encapsulate data as messages in RocketMQ and send the messages to the server.

## TransactionChecker

RocketMQ uses a transaction messaging mechanism that requires a producer to
implement a transaction checker to ensure eventual consistency of transactions.

## TransactionResolution

A status identifier of a transaction during the sending of a transactional message in
RocketMQ. The broker controls whether a transactional message should be committed and
delivered based on the transaction status. Transaction states include transaction commit,
transaction rollback, and transaction pending.

## ConsumerGroup

A consumer group is a load balancing group that contains consumers that use
the same consumption behaviors in RocketMQ.

## Consumer

A consumer is an entity that receives and processes messages in RocketMQ. Consumers
are usually integrated in business systems. They obtain messages from RocketMQ brokers
and convert the messages into information that can be perceived and processed by business logic.

## ConsumeResult

The result returned by a PushConsumer message listener in RocketMQ after it finishes
processing a message, used to indicate whether the message was processed correctly.
The consumption result includes consumption success and consumption failure.

## Subscription

A subscription is the rule and status settings for consumers to obtain and process messages
in RocketMQ. Subscriptions are dynamically registered by consumer groups with brokers.
Messages are then matched and consumed based on the filter rules defined by subscriptions.

## Message Filtering

Consumers can filter messages by subscribing to specified message tags (Tag), ensuring
that only the filtered message set is ultimately received. The calculation and matching
of filter rules are completed on the RocketMQ broker.

## Reset Consumer Offset

Using the timeline as the coordinate, reset the consumption progress of a consumer group
on a subscribed topic within the time range of message persistence. After the setting is
complete, the consumer will receive the messages that the producer sends to the RocketMQ
broker after the specified point in time.

## Message Trace

The complete link information aggregated from data such as the time and place of each
related node during the process from a message being sent by the producer to being
received and processed by the consumer. With message traces, you can clearly locate the
complete path of a message from the producer, through the RocketMQ broker, to the
consumer, which facilitates troubleshooting.

## Message Accumulation

The producer has already sent messages to the RocketMQ broker, but because the consuming
capacity of the consumer is limited, it cannot correctly consume all messages within a
short period of time. At this point, unconsumed messages are stored on the broker. This
state is called message accumulation.

## Transactional Messages

Transactional messages are an advanced message type provided by RocketMQ, supporting
eventual consistency between message production and local transactions in distributed
scenarios.

## Scheduled/Delayed Messages

Scheduled/delayed messages are an advanced message type provided by RocketMQ. After a
message is sent to the broker, it can only be consumed by the consumer after a specified
time. By setting a certain scheduled time, a delayed scheduling trigger effect in
distributed scenarios can be achieved.

## Ordered Messages

Ordered messages are an advanced message type provided by RocketMQ, supporting consumers
to obtain messages in the order in which they were sent, thereby achieving sequential
processing in business scenarios.

For more information, see the [Apache RocketMQ official documentation](https://rocketmq.apache.org/zh/).
