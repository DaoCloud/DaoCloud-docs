# Cross-Cluster Data Synchronization

Redis, as an open-source in-memory data storage system, offers excellent performance, high availability, and real-time capabilities to meet the needs of applications and services for large-scale access requests and data storage. However, due to the lack of built-in data security features, certain disaster recovery techniques need to be employed in practical applications to ensure the reliability of Redis data.

Disaster recovery techniques are primarily implemented through means such as data replication and data backup to provide both cold and hot backup methods. In the event of network, server, or database failures resulting in data loss, these techniques ensure the security of enterprise data and the continuity of business operations through processes like failover and data recovery.

Redis-Shake is a tool used for merging, synchronizing, and migrating Redis data. It provides corresponding data synchronization solutions based on different Redis modes. This article will introduce the methods for data synchronization and data recovery between different modes.

- [Cluster mode to Cluster mode](./cluster2cluster.md)
- [Sentinel mode to Sentinel mode](./sentinel2sentinel.md)
- [Cluster mode to Sentinel mode](./cluster2sentinel.md)

Please refer to the video tutorial: [Redis Cross-Cluster Data Synchronization](../../../videos/use-cases.md#redis).
