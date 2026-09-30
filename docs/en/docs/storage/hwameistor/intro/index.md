---
hide:
  - toc
MTPE: Fan-Lin
Date: 2024-01-23
---

# What is HwameiStor

HwameiStor is a Kubernetes-native container attached storage (CAS) solution that creates a local storage resource pool for centrally managing all disks such as HDD, SSD, and NVMe. It uses the CSI architecture to provide distributed services with local volumes and enables data persistence for stateful cloud native workloads or components.

![architecture](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/storage/hwameistor/img/architecture.png)

The specific features are as follows:

1. Automated Maintenance

    Automatically discover, identify, manage, and allocate disks. Allow smart scheduling of applications and data based on affinity, and automatically monitor disk status and reports in a timely manner.

2. High Availability

    Use cross-node replicas to synchronize data for high availability. When a problem occurs, the application will be automatically scheduled to the high-availability data node to ensure the continuity of the application.

3. Full-Range support of Storage Medium

    Aggregate HDD, SSD, and NVMe disks to provide low-latency, high-throughput data services.

4. Agile Linear Scalability

    Dynamically expand clusters according to their sizes and flexibly meet the data persistence requirements of the application.

## Product Advantages

**I/O Localization**

100% local throughput with no network overhead. When a node fails, the Pod starts on the replica node and uses the replica volume for local IO read and write.

**High Performance and High Availability**

- 100% IO localization to achieve high-performance local throughput
- 2-replica volume redundancy to ensure high data availability

**Linear Scalability**

- Independent node units, with a minimum of 1 node and unlimited expansion
- Separation of the control plane and data plane; node expansion does not affect data I/O of business applications

**Low CPU and Memory Overhead**

With IO localization, CPU remains stable without significant fluctuation for the same IO read and write, and memory resource overhead is low

**Production-Ready Operability**

- Supports migration at the node, disk, and volume group (VG) levels
- Supports operations such as disk replacement

[HwameiStor Release](https://github.com/hwameistor/hwameistor/releases){ .md-button .md-button--primary }
[Download DCE](../../../download/index.md){ .md-button .md-button--primary }
[Install DCE](../../../install/index.md){ .md-button .md-button--primary }
[Free Trial Now](../../../dce/license0.md){ .md-button .md-button--primary }
