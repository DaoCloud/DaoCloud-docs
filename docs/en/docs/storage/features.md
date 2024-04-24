---
MTPE: windsonsea
Date: 2024-04-24
---

# Features

## Cloud Native Unified Management

- Hybrid Storage Access
   
    HwameiStor provides unified CSI standardized access to enable multiple data access types such as NFS, block storage, and local storage. This feature meets the needs of different cases.

- Dynamic Memory Management

    Supports dynamic allocation of StorageClass resources, eliminating the need for administrators to manually manage, operate, and maintain data volumes.

- Creation of Multiple Data Volumes

    Data volumes can be dynamically created through StorageClass, and snapshots can be used to create data volumes.

## Cloud Native Local Storage (HwameiStor)

- High Performance Local Volumes

    HwameiStor Cloud Native Local Storage eliminates the need for external storage devices and ensures high-performance local throughput through IO localization with no network overhead. It supports applications with high performance requirements such as databases and middleware on the cloud.

- Multiple Types of Data Volumes

    HwameiStor Cloud Native Local Storage supports LVM type and raw disk type data volumes to meet different disk demand use cases.

- CSI Standards

    HwameiStor connects to local storage through standard CSI standards, and postures are used uniformly.

- Active and Standby High Availability

    Multi-copy redundancy mechanisms of data volumes ensure high availability of data and improve the reliability of data reading and writing.

- Data Volume Expansion

    Business-insensitive expansion is supported, enabling elastic expansion of mounted data volumes during application running.

## Production Operability and Maintainability

- Non-Disruptive Upgrade

    The separation of the data plane and control plane enables zero perception of business data when the control plane upgrades/expands nodes.

- Disk Replacement

    HwameiStor supports disk replacement after disk alerts without affecting business applications, ensuring production operability and maintainability.

- One-Click Expulsion of Node Data Volumes

    Manually expel the data volume of a certain node with one click to realize production operation and maintenance.

- Automatic Expulsion of Node Data Volumes

    HwameiStor supports automatic detection and eviction of data volumes on nodes through Kubernetes eviction behavior.

- Single Disk Dimension (LD) Data Migration

    HwameiStor supports disk replacement when an early warning occurs, ensuring that all data is migrated without business application data loss.

- Data Migration of Application Load Dimension

    HwameiStor supports data migration with the application as the dimension during stateful application rescheduling, ensuring successful scheduling of business application Pods and data consistency after scheduling.

- Unified Dashboard

    The unified dashboard displays resource usage and distribution, storage resource status, and monitoring alerts.

- Rich Metrics

    HwameiStor provides all-around data service monitoring and alerting, realizing comprehensive monitoring of data disks, StorageClass, and storage drivers, and comprehensively guarantees data security.
