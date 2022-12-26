---
hide:
  - toc
---

# Kafka common terms

- messages and batches

    The basic data unit of Kafka is called message (message). In order to reduce network overhead and improve efficiency, multiple messages will be put into the same batch (Batch) and then written.

- Topics and partitions

    Kafka's messages are classified by Topic. A topic can be divided into several Partitions. A partition is a commit log.
    Messages are written to partitions in an append fashion and read in first-in first-out order.
    Kafka achieves data redundancy and scalability through partitions. Partitions can be distributed on different servers, which means that a topic can span multiple servers to provide more powerful performance than a single server.

    Since a Topic contains multiple partitions, the order of messages cannot be guaranteed across the entire Topic, but the order of messages within a single partition can be guaranteed.

    ![](../images/concept01.png)

- producers and consumers

    Producers are responsible for creating messages. In general, the producer distributes messages evenly to all partitions in the topic, and does not care which partition the message will be written to.
    If we want to write the message to the specified partition, we can do it by customizing the partitioner.

    A consumer is part of a consumer group, and the consumer is responsible for consuming messages. Consumers can subscribe to one or more topics and read messages in the order they were generated.
    Consumers distinguish read messages by checking their offsets.
    The offset is an incrementing number that Kafka adds to the message when it is created, and is unique to each message within a given partition.
    The consumer saves the last read offset of each partition on Zookeeper or Kafka. If the consumer is shut down or restarted, it can also retrieve the offset to ensure that the read state will not be lost.

    ![](../images/concept02.png)

    A partition can only be read by one consumer in the same group, but can be read jointly by multiple consumers in different groups.
    When consumers in multiple groups jointly read the same topic, they do not affect each other.

    ![](../images/concept03.png)

-Brokers and Clusters

    A standalone Kafka server is called a Broker. Broker receives messages from producers, sets offsets for messages, and commits messages to disk for storage.
    Broker provides services for consumers, responds to requests to read partitions, and returns messages that have been committed to disk.
    
    Broker is an integral part of the cluster (Cluster).
    Each cluster will elect a Broker as the cluster controller (Controller), and the cluster controller is responsible for management, including assigning partitions to Brokers and monitoring Brokers.
    
    In the cluster, a partition (Partition) is subordinate to a Broker, and the Broker is called the leader of the partition (Leader).
    A partition can be assigned to multiple Brokers, and partition replication will occur at this time.
    This replication mechanism provides message redundancy for partitions, and if one Broker fails, other Brokers can take over the leadership.

    ![](../images/concept04.png)