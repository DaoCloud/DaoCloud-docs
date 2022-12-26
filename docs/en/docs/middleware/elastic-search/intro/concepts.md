---
hide:
  - toc
---

# Basic concept

This section lists proper nouns and terms related to Elasticsearch.

- node

    Data node: a node that stores index data, and mainly performs operations such as adding, deleting, modifying, checking, and aggregating documents.

    Dedicated Master Node: Operates on the cluster, such as creating or deleting indexes, keeps track of which nodes are part of the cluster, and decides which shards are assigned to the relevant nodes. A stable master node is very important to the health of the cluster. By default, any node in the cluster may be elected as the master node.

    Coordinator node: share the CPU overhead of data nodes, thereby improving processing performance and service stability.

- Index

    The data used to store Elasticsearch is a logical space grouped together by one or more shards.

- Shard

    Indexes can store data whose amount of data exceeds the hardware limit of 1 node. To meet such needs, Elasticsearch provides the ability to split an index into multiple ones, called Shards.
    When you create an index, you can specify the number of shards according to the actual situation. Each shard is hosted on any node in the cluster, and each shard is itself an independent, fully functional "index".
    The number of shards can only be specified before creating the index, and cannot be modified after the index is created successfully.

- replicas

    Replicas are backups of the index, and Elasticsearch can set up multiple copies. Write operations are first completed on the primary shard and then distributed to replica shards.
    Because both the primary and replica shards of the index can provide query services to the outside world, replicas can improve the high availability of the system and the concurrency performance of searches. But if there are too many copies, it will also increase the burden of data synchronization during write operations.