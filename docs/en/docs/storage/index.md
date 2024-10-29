---
MTPE: windsonsea
Date: 2024-04-24
---

# Cloud Native Storage

Types of Cloud Native Storage in the market:

1. **Traditional Storage Cloud Native Transformation**: This type connects to the Kubernetes platform through the CSI standard. It is relatively common, allowing users to leverage existing storage while providing stable cloud native storage capabilities based on traditional storage, ensuring good reliability and strong SLA guarantees.

2. **Software-Defined Storage Cloud Native Transformation**: Software-defined storage is compatible with both traditional applications and cloud native applications. It also connects with Kubernetes based on the CSI standard. This approach utilizes the disk space of every machine within the enterprise via the network, forming a virtual storage device from these distributed resources, with data spread across various storage devices.

3. **Pure Cloud Native Storage**: This type of storage is inherently designed for cloud native environments and is built on cloud native platforms, aligning well with cloud native characteristics. It can migrate alongside application Pods and offers features such as high scalability and high availability, though it may have slightly lower reliability compared to traditional storage accessed through the CSI standard.

## DCE Cloud Native Storage

DCE 5.0 Cloud Native Storage is based on the Kubernetes CSI standard and can connect to CSI-compliant storage according to different SLA requirements and user scenarios. The cloud native local storage offered by DaoCloud naturally possesses cloud native characteristics, fulfilling the needs for high scalability and high availability in containerized environments.

![Cloud Native Storage](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/nativestorage.jpg)

## Background

**Storage Demands for Middleware Services in the Cloud**

1. The cloud is poised to become the core of new digital experiences, with a significant increase in the number of databases, message queues, and other middleware migrating to the cloud. Ensuring high performance and reliability of business applications during the transition of stateful applications like middleware to the cloud is a challenge that enterprises must address.

2. In scenarios where physical infrastructure integrates computing and storage, effectively utilizing existing device storage space to meet the cloud migration needs of stateful applications is essential.

3. As more critical applications move to the cloud, efficiently managing cloud storage operations, ensuring the reliability of data storage, and implementing comprehensive monitoring—including application, control plane, and backend device monitoring—will present new challenges.

**Storage Solutions in Cloud-Edge Collaborative Scenarios**

In Gartner's 2021 predictions for top cloud trends, edge computing emerged as a new frontier. In edge scenarios, there is a demand for both data storage and preprocessing of edge data. Typically, storage and computing are integrated at the edge, but resources are limited. Finding ways to perform data storage and computation based on edge environments is also a challenge that needs to be addressed in cloud-edge collaborative scenarios.

## Challenges

**Enterprise Readiness Challenges**

As stateful critical applications such as databases, message queues, and big data gradually move to the cloud, there are new and higher demands for storage performance (throughput and latency). Meeting these high-performance requirements is crucial.

At the same time, ensuring efficient operations and monitoring the reliability of data storage is essential. This includes achieving comprehensive monitoring and issue alerts, presenting monitoring data for application-level and control plane mount points, as well as backend devices to create a full-link monitoring system that can quickly identify storage issues.

**Agility Challenges**

Cloud native application scenarios require high agility and flexibility in service. Many scenarios expect rapid container startup and flexible scheduling, necessitating both storage volumes and the ability to quickly adjust based on changes in Pods.

1. Improved efficiency in mounting and unmounting cloud disks.
2. Flexibility to quickly switch block device mounts across different nodes.
3. Automatic issue resolution capabilities for storage services to reduce manual intervention.
4. Online expansion capabilities to enable quick scaling of applications without impacting business operations.
5. As more stateful applications are containerized and deployed within the same cluster, how can applications automatically schedule based on storage type in regionally planned business scenarios?

**Cost Reduction and Efficiency Improvement Challenges**

As data center computing density increases, addressing storage performance bottlenecks becomes critical.

1. Identifying performance and availability issues (unplanned equipment failures, fault location, and recovery).
2. Managing the complexity of building, configuring, maintaining, and scaling applications across different deployment environments and software technology stacks.
3. Addressing storage bottlenecks: Once computational bottlenecks are resolved, storage capacity can become the limiting factor for computing density.
4. Business applications are often designed based on peak demand, leading to idle rates of computing and storage resources exceeding 50%. This high cost necessitates the ability to sense business needs for automatic scaling and resource balancing.
