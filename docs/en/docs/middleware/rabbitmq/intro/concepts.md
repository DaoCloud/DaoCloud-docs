---
hide:
  - toc
---

# basic concept

This section lists the proper nouns and terms involved in RabbitMQ, so that you can better understand related concepts and use RabbitMQ message queues.

- Message

    Messages are generally divided into two parts: message body and tags. Labels are also called message headers and are mainly used to describe the message. The message body is the content of the message, which is a json body or data.

    The message body is opaque, while the message header consists of a series of optional attributes, including routing-key (routing key), priority (priority relative to other messages), delivery-mode (indicating that the message may require persistent storage), etc.

    Producers publish messages, consumers consume messages, and producers and consumers have no direct relationship with each other.

- Message ID (Message ID)

    The message ID is an optional attribute of the message, and its type is a short string.

- Queue

    Queues are used to store messages, producers send messages to the queue, and consumers get messages from the queue. Multiple consumers can subscribe to the same queue at the same time, and the messages in the queue are assigned to different consumers. Each message is put into one or more queues.

- message lifetime

    The validity period of the message in the queue. When a message stays in the queue for longer than the configured message lifetime, the message expires. The value of the message lifetime must be a non-negative integer in milliseconds. For example, a time-to-live value of a message is 1000, which means that the message will survive in the queue for at most 1 second.

- Delayed messages

    The producer publishes the message to the RabbitMQ version of the message queue server, but does not expect the message to be delivered immediately, but is delayed for a certain period of time before being delivered to the consumer for consumption. The message is a delayed message.

- Producer (Publisher)

    A producer of messages is also a client application that publishes messages to an exchange. That is, the party that publishes a message to the queue. The ultimate purpose of publishing a message is to pass the content of the message to other systems/modules, so that the other party can process the message according to the agreement.

- Consumer

    The consumer of the message represents a client application program that obtains messages from the message queue. Consumers subscribe to RabbitMQ queues. When a consumer consumes a message, it only consumes the message body. During message routing, tags are discarded, and only the message body is queued.

- Broker

    The service node of the message middleware, that is, the message queue server entity.