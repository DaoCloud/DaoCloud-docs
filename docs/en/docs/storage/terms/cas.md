# CAS storage

Container Attached Storage (CAS) is a microservice storage controller-based software storage system orchestrated by Kubernetes. Its storage controllers are managed and run in containers as part of a Kubernetes cluster. This makes CAS portable and can run on any Kubernetes platform, including any cloud platform, bare metal server, or traditional shared storage system. Crucially, the data itself is also accessible through the container rather than being stored in a non-platform shared scale-out storage system. I/O access times are reduced as CAS leverages a microservices architecture that keeps the storage solution closely tied to the application bound to the physical storage device.

The CAS pattern fits well with the trend towards distributed data and is also suitable for small autonomous teams with micro loosely coupled workloads. For example, one team might need Postgres to provide microservices, while another team might rely on Redis and MongoDB for their R&D data. some cases may be performance demanding, some may die in 20 minutes, some are write/read intensive, etc. In a large enterprise, as the enterprise grows in size, the enterprise trusts each team more and more to choose the tools they use, and the technology that each team relies on will become more and more different.

CAS means that developers can work without worrying about the underlying requirements of the enterprise storage architecture. For CAS, cloud disk is no different from SAN, bare metal or virtual machine. Developers and platform SRE engineers don't have to meet to decide on the next storage vendor, or go back and forth on how to set it up to support a use case. Developers remain autonomous and can spin up their own CAS containers using whatever storage is available to the Kubernetes cluster.

CAS reflects a broader trend of solutions, many of which are CNCF projects, built on top of Kubernetes and microservices, resulting in a thriving cloud-native ecosystem. Today, CNCF's cloud-native ecosystem includes security, DNS, networking, network policy management, messaging, tracking, logging, and many other projects.

## Benefits of CAS

### Agility

Each storage volume in CAS has a containerized storage controller and corresponding containerized replica. So resource maintenance and tuning around these components is truly agile. Kubernetes' rolling upgrade feature enables seamless upgrades of storage controllers and storage replicas. Resources such as CPU and memory can be optimized using container cgroups.

### Granularity of Storage Policy

Containerizing storage software and dedicating storage controllers to each volume enables maximum granularity in storage policies. With the CAS architecture, you can configure all storage policies on a per-volume basis. Additionally, you can monitor storage parameters for each volume and dynamically update storage policies to achieve the desired results for each workload. As the granularity in volume storage policies increases, so does the control over storage throughput, IOPS, and latency.

### Avoid Binding

Avoiding lock-in to cloud providers is a common goal for many Kubernetes users. However, the data of stateful applications usually still depends on the cloud service provider and its technology, or on the underlying traditional shared storage system NAS or SAN. With the CAS method, the storage controller can perform data migration in the background of each workload, making live migration easier. In other words, the granularity of control of CAS simplifies the migration of stateful workloads from one Kubernetes cluster to another in a non-disruptive manner.

### Native Cloud

CAS containerizes storage software and uses Kubernetes CRDs to represent underlying storage resources such as disks and StorageClass. This model enables storage to be seamlessly integrated into other cloud hosting tools. You can use Prometheus, Grafana, Fluentd, Weavescope, Jaeger and other cloud host tools to provision, monitor and manage storage resources.

In addition, the storage and performance of volumes in CAS are scalable. Since each volume has its own storage controller, it can be elastically scaled within the allowed range of the node's storage capacity. As the number of container applications in a given Kubernetes cluster increases, more nodes are added, increasing the overall availability of storage capacity and performance, making storage available for new application containers.

### Smaller area of ​​influence

Because the CAS architecture is partitioned by workload and the components are loosely coupled, the reach of CAS is much smaller than that of typical distributed storage architectures.

CAS can provide high availability through synchronous replication from storage controllers to storage replicas. The metadata required to maintain a replica is reduced to information about the replica nodes and information about the status of the replica. If a node fails, the storage controller will rotate through a second or third replica on a node that is running and has data available. Therefore, when using CAS, the scope of the impact is much smaller, and the impact is limited to volumes that have replicas on that node.