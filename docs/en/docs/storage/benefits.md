---
MTPE: windsonsea
Date: 2024-04-24
hide:
  - toc
---

# Hwameistor Benefits

**I/O Localization**

Hwameistor cloud native local storage guarantees 100% local throughput, eliminating network overhead. In the event of a node failure, the Pod automatically restarts on a replica node, utilizing the replica data volume for localized read and write operations.

**High Performance, High Availability**

- Delivers top-tier local throughput by achieving 100% I/O localization.
- Enhances data availability by maintaining redundant backups across two data volumes.

**Linear Expansion**

- Features a scalable architecture starting from a single node with the capacity for limitless expansion.
- Maintains a separation between the control plane and data plane, ensuring that node scaling does not impact the I/O performance of business applications.

**Minimal CPU and Memory Overhead**

Hwameistor's cloud native local storage is designed to keep CPU usage stable without significant fluctuations during I/O operations, and it minimizes memory overhead through efficient I/O localization.

**Operational Manageability**

- Facilitates management tasks including node, disk, and data volume group (VG) migrations.
- Supports essential maintenance activities such as disk replacement, enhancing operational efficiency.
