---
MTPE: windsonsea
Date: 2024-04-24
---

# Storage Background and Challenges

This page outlines the historical development of the storage industry and the challenges it currently faces.

## Background

**Storage Requirements for Middleware Services in the Cloud**

1. As the cloud becomes central to new digital experiences, there is a notable increase in middleware services such as databases and message queues in cloud environments. During the transition of stateful applications to the cloud, enterprises face the challenge of maintaining high performance and reliability in their business applications.
2. In scenarios where storage and computing are integrated at physical locations, the question arises: how can existing storage resources be effectively utilized to support stateful applications in the cloud?
3. With an increasing migration of critical applications to the cloud, new challenges emerge in managing cloud storage efficiently. These include ensuring data reliability, and implementing thorough monitoring across the application, control plane, and backend devices.

**Storage Solutions in Cloud-Edge Collaboration Scenarios**

According to Gartner's top ten cloud trends for 2021, edge computing is emerging as a new frontier. Edge scenarios also demand capabilities for data storage and preprocessing. Typically, storage-computing integration is adopted at the edge, but resources are limited. Determining how to efficiently manage data storage and processing at the edge presents a challenge in cloud-edge collaboration scenarios.

## Challenges

**Enterprise Readiness Challenge**

As key stateful applications like databases, message queues, and big data platforms transition to the cloud, there are increasingly stringent requirements for cloud storage performance, including throughput and latency. The challenge lies in achieving high-performance while also ensuring efficient operations and maintenance, reliable data storage monitoring, and comprehensive monitoring that encompasses application-level, control plane, and backend device metrics. This also involves swiftly identifying and resolving storage issues.

**Agility Challenge**

Cloud native scenarios demand high service agility and flexibility. Many such scenarios require rapid container startup and adaptable scheduling, necessitating agile storage volume adjustments and pod modifications. To address this:

1. Enhance the efficiency of cloud disk mounts and dismounts.
2. Enable flexible mounting of block devices and quick transitions between different nodes.
3. Provide automatic repair capabilities for storage services, minimizing human intervention.
4. Implement capabilities for online expansion that do not disrupt ongoing business operations, facilitating rapid container capacity increases.
5. In environments where multiple stateful applications are containerized and deployed within the same cluster, automate scheduling based on storage types to optimize regional usage within the cluster.

**Cost Reduction and Efficiency Increase Challenge**

As data center computing density increases, addressing storage performance bottlenecks becomes crucial:

1. Identify and rectify unplanned equipment failures and facilitate quick recovery to address performance and availability issues.
2. Simplify the processes of building, configuring, maintaining, and scaling applications across various deployment environments and technology stacks.
3. Tackle storage constraints that emerge after computing bottlenecks have been addressed, as storage capacity can restrict computing density.
4. Recognize business demands and implement resource balancing strategies such as automatic scaling to mitigate high costs associated with idle rates of computing and storage resources exceeding 50%.
