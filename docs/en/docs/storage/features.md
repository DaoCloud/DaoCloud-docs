# Features

## Cloud Native Unified Management

- Hybrid storage access

     Unified CSI standardized access to realize multiple data access types (NFS, block storage, local storage) access to meet the needs of different scenarios.

- Dynamic memory management

     Supports dynamic allocation of storage pool resources, eliminating the need for administrators to manually manage, operate and maintain data volumes.

- How to create multiple data volumes

     Data volumes can be dynamically created through storage pools, and snapshots can be used to create data volumes.

## Cloud Native Local Storage (Hwameistor)

- High performance local volumes

     No need for external storage devices, IO localization, no network overhead, high-performance local throughput, and support for applications with high performance requirements such as databases and middleware on the cloud.

- Multiple types of data volumes

     Supports LVM type and raw disk type data volumes to meet different disk demand scenarios.

- CSI standards

     Connect to Hwameistor local storage through standard CSI standards, and use postures uniformly.

- Active and standby high availability

     Realize the multi-copy redundancy mechanism of data volumes to ensure high availability of data and improve the reliability of data reading and writing.

- Data volume expansion

     Business-insensitive expansion, supports elastic expansion of mounted data volumes during application running.

## Production can be operated and maintained

- Non-disruptive upgrade (does not affect business data)

     The data plane and the control plane are separated, and when the control plane upgrades/expands nodes, the read and write of business application data has zero perception.

- change disc

     It supports disk replacement after disk alerts, ensuring that business applications are not affected, and production can be maintained.

- One-click expulsion of node data volumes

     Manually expel the data volume of a certain node with one click to realize production operation and maintenance.

- Automatically expel node data volumes

     Combined with Kubernetes eviction behavior to automatically detect and evict data volumes on nodes.

- Single disk dimension (LD) data migration

     It supports disk replacement when an early warning occurs and all data is migrated to ensure that business application data is not lost.

- Data migration of application load dimension

     When stateful application rescheduling is supported, data migration is implemented with the application as the dimension, ensuring successful scheduling of business application Pods and data consistency after scheduling.

- Unified Dashboard

     The unified dashboard displays resource usage and distribution, storage resource status, and monitoring alerts.

- Rich Metrics

     All-round data service monitoring and alerting realizes comprehensive monitoring of data disks, storage pools and storage drivers, and comprehensively guarantees data security.
