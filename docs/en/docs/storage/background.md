# Background and challenges

## Background

**Storage requirements for middleware services on the cloud**

1. The cloud will soon become the core of new digital experiences, and the number of middleware such as databases and message queues on the cloud is increasing rapidly.
    In the process of migrating stateful applications such as middleware to the cloud, how to ensure the high performance and high reliability of business applications is a problem that enterprises need to face.
2. For the storage-computing fusion scenario of physical facilities, how to use the existing device storage space to meet the needs of stateful applications on the cloud.
3. As more and more critical applications go to the cloud, how to achieve efficient operation and maintenance of cloud storage, how to ensure the reliability of data storage, and how to implement comprehensive application/control plane/backend device monitoring will also become new issues. challenge.

**Storage solution in cloud-side collaboration scenario**

In Garner's top ten cloud trend predictions for 2021, edge computing becomes the new cloud.
In edge scenarios, the edge also has data storage requirements and edge data preprocessing requirements.
On the edge side, storage-computing integration is generally adopted, but edge resources are limited. How to perform certain data storage and data calculation based on the edge side is also a problem that needs to be solved in cloud-edge collaboration scenarios.

![Cloud-side collaboration scenario](./images/storagescenario.png)

## Challenge

**Enterprise Readiness Challenge**

Stateful key applications such as databases, message queues, and big data are gradually going to the cloud, and there are new and higher requirements for the performance (throughput, latency) of storage on the cloud. How to meet the high performance requirements at this time.

At the same time, efficient operation and maintenance ensures the reliability monitoring of data storage, and realizes comprehensive monitoring and early warning of problems, including displaying monitoring data of application-level/control plane mount points and back-end devices, and forming full-link monitoring, and can Quickly lock down storage issues.

**Agility Challenge**

Cloud-native application scenarios have very high requirements for service agility and flexibility. Many scenarios expect fast container startup and flexible scheduling, which requires both storage volumes and agile adjustments to Pod changes.

1. The efficiency of cloud disk mounting and uninstallation is improved
2. The block device can be flexibly mounted and switched quickly on different nodes
3. Provide the ability to automatically repair problems in storage services, reducing human intervention
4. Online expansion capability, in order to quickly expand the capacity of the container, how to achieve online expansion without affecting the application business?
5. As more and more stateful applications are containerized and stateful applications are deployed in the same cluster, how can applications be automatically scheduled according to the storage type in the cluster planning business sub-regional usage scenario?

**Cost Reduction and Efficiency Increase Challenge**

At present, while the computing density of the data center is increasing, how to solve the storage performance bottleneck?

1. Locating and troubleshooting performance and availability issues (unplanned equipment failures, fault location and recovery)
2. Complexity of building, configuring, maintaining and scaling applications (different deployment environments and software technology stacks)
3. Storage bottleneck: After solving the computing bottleneck, storage capacity will become a bottleneck restricting computing density
4. Business applications are planned and designed according to business peaks, and the idle rate of computing resources and storage resources is ≥ 50%. The cost is high, and how to perceive the business and perform resource balancing such as automatic expansion.