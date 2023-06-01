---
hide:
  - toc
---

# Basic Concepts

## Messages and Batches

The smallest data unit in Kafka is called a message. To reduce network overhead and improve efficiency, multiple messages are batched together before being written to storage space.

## Topics and Partitions

Kafka messages are classified by topic, and a topic can be divided into multiple partitions, with each partition representing a commit log. Messages are written to the partition in append mode and read in first-in-first-out order.

Kafka uses partitioning to achieve data redundancy and scalability. Partitions can be distributed across different servers. This means that a topic can span multiple servers to provide more powerful performance than a single server.

Because a topic contains multiple partitions, message ordering cannot be guaranteed across the entire topic scope, but it can be guaranteed within a single partition.

![Topics and Partitions](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/kafka/images/concept01.png)

## Producers and Consumers

Producers are responsible for creating messages. In general, producers distribute messages evenly across all partitions in a topic without caring about which partition a message is written to. If you want to write messages to a specific partition, it can be achieved by customizing a partitioner.

Consumers are part of a consumer group and are responsible for processing messages. Consumers can subscribe to one or more topics and read them in the order they were generated.

Consumers distinguish if messages have been read or not by checking their offsets. Offset are constantly increasing values. They are added to messages when the messages are created. The offset of each message in a given partition is unique.

Consumers save the latest offsets in each partition in Zookeeper or Kafka. If a consumer is closed or restarted, it can reacquire the offset to ensure that the read status is not lost.

![Consumers](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/kafka/images/concept02.png)

A partition can only be read by one consumer in the same group, but it can be read by multiple consumers in different groups. When consumers in different groups read the same topic, they do not affect each other.

![Consumers](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/kafka/images/concept03.png)

## Broker and Cluster

An independent Kafka server is called a Broker. Brokers receive messages from producers, set offsets for messages, and commit messages to disk. Brokers respond to requests from consumers to read partitions and return messages that have been committed to disk.

Brokers are part of a cluster. Each cluster elects one broker as the cluster controller, which is responsible for managing tasks such as partition assignment and broker monitoring.

In a cluster, a partition belongs to a broker, which is called the leader of the partition. A partition can be assigned to multiple brokers, which triggers partition replication to provide message redundancy. If one broker fails, other brokers can take over leadership.

![broker and cluster](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/kafka/images/concept04.png)
