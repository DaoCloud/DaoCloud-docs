---
MTPE: Fan-Lin
Date: 2024-01-23
---

# What is HwameiStor

HwameiStor is a Kubernetes-native container attached storage (CAS) solution that creates a local storage resource pool for centrally managing all disks such as HDD, SSD, and NVMe. It uses the CSI architecture to provide distributed services with local volumes and enables data persistence for stateful cloud native workloads or components.

![architecture](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/storage/hwameistor/img/architecture.png)

## Features

1. Automated Maintenance

    Automatically discover, identify, manage, and allocate disks. Allow smart scheduling of applications and data based on affinity, and automatically monitor disk status and reports in a timely manner.

2. High Availability

    Use cross-node replicas to synchronize data for high availability. When a problem occurs, the application will be automatically scheduled to the high-availability data node to ensure the continuity of the application.

3. Full-Range support of Storage Medium

    Aggregate HDD, SSD, and NVMe disks to provide low-latency, high-throughput data services.

4. Agile Linear Scalability

    Dynamically expand clusters according to their sizes and flexibly meet the data persistence requirements of the application.

[HwameiStor Release](https://github.com/hwameistor/hwameistor/releases){ .md-button .md-button--primary }
[Download DCE 5.0](../../../download/index.md){ .md-button .md-button--primary }
[Install DCE 5.0](../../../install/index.md){ .md-button .md-button--primary }
[Free Trial Now](../../../dce/license0.md){ .md-button .md-button--primary }
