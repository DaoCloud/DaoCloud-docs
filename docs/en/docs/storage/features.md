---
MTPE: windsonsea
Date: 2024-04-24
---

# Features

DCE 5.0 Cloud Native Storage offers the following features:

| Features | Description |
| ------- | --- |
| **Cloud Native Unified Management** | |
| Hybrid Storage Access | Provides unified CSI standardized access, enabling multiple data access types (NFS, block storage, local storage) to meet diverse scenario requirements. |
| Dynamic Storage Management | Supports dynamic allocation of storage pool resources, eliminating the need for manual management or maintenance of volumes by administrators. |
| Multiple Volume Creation Methods | Allows for dynamic creation of volumes through storage pools, as well as snapshot-based creation of volumes. |
| **Cloud Native Local Storage (HwameiStor)** | |
| High-Performance Local Volumes | Achieves IO localization without the need for external storage devices, minimizing network overhead and ensuring high local throughput, making it suitable for high-performance applications in the cloud. |
| Multiple Types of Volumes | Supports LVM-type and raw disk-type volumes to accommodate various disk requirements. |
| CSI Standard | Accesses HwameiStor local storage through standardized CSI, ensuring a consistent usage approach. |
| Master-Slave High Availability | Implements a multi-replica redundancy mechanism for volumes, ensuring high data availability and enhancing the reliability of data read and write operations. |
| Volume Expansion | Allows for seamless expansion of volumes during business operations, supporting elastic scaling of mounted volumes while applications are running. |
| **Production Operability** | |
| Non-Disruptive Upgrades (No Impact on Business Data) | Separates the data plane and control plane, allowing for upgrades or expansion of control plane nodes without affecting the read/write operations of business application data. |
| Disk Replacement | Supports disk replacement after alerts, ensuring that business applications remain unaffected and maintaining operational continuity. |
| One-Click Eviction of Node Volumes | Enables manual one-click eviction of volumes from specific nodes, facilitating operational management. |
| Automatic Eviction of Node Volumes | Automatically detects and evicts volumes from nodes based on Kubernetes eviction behavior. |
| Single Disk Dimension (LD) Data Migration | Supports the migration of all data when a disk alert occurs and replacement is necessary, ensuring that business application data is not lost. |
| Application Load Dimension Data Migration | Facilitates data migration based on application dimensions during the rescheduling of stateful applications, ensuring successful scheduling of business application Pods and maintaining data consistency post-scheduling. |
| Unified Dashboard | Features a centralized dashboard that displays resource usage rates and distributions, as well as the status of storage resources and monitoring alerts. |
| Rich Metrics Indicators | Provides comprehensive monitoring and alerts for data services, ensuring thorough oversight of data disks, storage pools, and storage drivers to safeguard data security. |
