---
hide:
  - toc
---

# Basic Concepts

This page lists terms and concepts related to Elasticsearch.

- Node

    Data node: A node that stores index data and is primarily responsible for operations such as adding, deleting, modifying, querying, and aggregating documents.

    Master-eligible node: A node that operates on the cluster, such as creating or deleting indexes, tracking which nodes are part of the cluster, and determining which shards are allocated to which nodes. A stable master node is critical to the health of the cluster, and by default, any node in the cluster can be selected as the master-eligible node.

    Coordinating node: A node that shares the CPU workload of data nodes to improve processing performance and service stability.

- Index

    Used to store Elasticsearch data. An index is a logical space where one or more shards are grouped together.

- Shard

    An index can store data that requires more than one node's storage resources. Elasticsearch provides the ability to split an index into multiple shards. When you create an index, you can specify the number of shards as needed. Each shard is hosted on a node in the cluster and the shard itself is an independent, full-featured "index". The number of shards can only be specified before the index is created and cannot be changed after the index is created.

- Replica

    Replicas are backups of an index, and Elasticsearch can set multiple replicas. The write operation is performed on the primary shard and then distributed to the replica shards. Because both the primary and replica shards of an index can provide query services externally, replicas can ensure high availability and performance under search concurrency. However, if there are too many replicas, it will also increase the burden of data synchronization during write operations.
