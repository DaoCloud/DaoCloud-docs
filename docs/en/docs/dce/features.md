---
MTPE: windsonsea
date: 2026-11-20
hide:
  - toc
---

# Features and Benefits

DaoCloud Enterprise (DCE) combines a large number of features into one platform to provide one-stop PaaS services. The typical features currently supported are as follows.

## Features

| Category | Feature | Description |
| :--- | :--- | :--- |
| [Multicluster Management](../kpanda/intro/index.md) | [Unified multicluster management](../kpanda/user-guide/clusters/integrate-cluster.md) | Incorporate Kubernetes clusters within a specific version range into container management, achieving unified management of multicloud and hybrid cloud container platforms across on-premises and cloud environments |
| | [Rapid cluster deployment](../kpanda/user-guide/clusters/create-cluster.md) | Rapidly deploy enterprise-level Kubernetes clusters through the web UI, adapting to physical machines and virtual machines |
| | [One-click cluster upgrade](../kpanda/user-guide/clusters/upgrade-cluster.md) | Upgrade Kubernetes versions with one click and manage system component upgrades in a unified manner |
| | Cluster high availability | Built-in disaster recovery and backup capabilities ensure business systems can recover from host failures, data center outages, and natural disasters, reducing the risk of business interruption |
| | Full lifecycle management | Realize full lifecycle management of self-built cloud native clusters |
| | [Open API](https://docs.daocloud.io/openapi/) | Provide native Kubernetes OpenAPI capabilities |
| [Cluster Operations and Security](../kpanda/user-guide/clusterops/latest-operations.md) | [Cluster inspection](../kpanda/user-guide/inspect/index.md) | Inspect the health status of clusters and nodes with one click, generate inspection reports, and quickly identify and locate risks |
| | [Application backup and restore](../kpanda/user-guide/backup/index.md) | Back up and restore applications and their persistent data based on Velero, supporting cluster migration and disaster recovery |
| | [GPU resource management](../kpanda/user-guide/gpu/index.md) | Support manual/dynamic GPU scheduling and sharing, adapting to heterogeneous computing such as NVIDIA, Ascend, Iluvatar, and MetaX |
| | [Security scanning](../kpanda/user-guide/security/index.md) | Built-in compliance scanning, permission scanning, and vulnerability scanning to secure clusters and applications |
| [Cloud Native Application Management](../amamba/intro/index.md) | Multi-form application management | Realize deployment and full lifecycle management of different types of cloud native applications, supporting cloud native applications, Helm applications, OAM, etc., with open multicloud application compatibility |
| | One-stop deployment | Decouple from the underlying Kubernetes platform, deploying and operating business applications in a one-stop manner |
| | Workload scaling | Manually/automatically scale application workloads through the UI, with custom scaling policies to cope with traffic peaks |
| | Application lifecycle | Support full lifecycle management including viewing, updating, deleting, rolling back, event viewing, and upgrading applications |
| | Cross-cluster workload management | Unified workload management capability across clusters |
| | [GitOps continuous deployment](../amamba/user-guide/gitops/create-argo-cd.md) | Declarative continuous deployment based on Argo CD, with Git as the single source of truth for application configuration |
| | [Progressive application delivery](../amamba/user-guide/release/canary.md) | Support [canary release](../amamba/user-guide/release/canary.md) and [blue-green release](../amamba/user-guide/release/blue-green.md) |
| [Continuous Business Delivery](../amamba/intro/index.md) | [Enterprise-level cloud native CI/CD](../amamba/user-guide/pipeline/create/custom.md) | Standardized continuous integration and delivery capabilities enable agile iteration of applications, quickly meeting new business needs and improving integration and release efficiency |
| | Cloud native delivery | Containerized management of application build environments, custom build machines and other resources, pipeline-level resource isolation, and support for multiple application deployment types |
| | Improved R&D efficiency | Declarative steps are pre-packaged in the visual pipeline build environment, so complex pipelines can be created without scripts; environments are automatically created/destroyed according to resource size to avoid waste |
| | Pipeline as code | Declarative pipelines are easy to learn, with version-controlled, modular, and reusable configurations |
| | DevOps tool integration | Steps in a single pipeline can run on multiple operating systems and architectures, supporting integration with mainstream software such as Kubernetes, GitLab, SonarQube, and Harbor |
| | [Code repository management](../amamba/user-guide/repo.md) | Centrally host code repositories and integrate with pipelines to achieve continuous delivery from code to application |
| [Multicloud Application Dispatch](../kairship/intro/index.md) | Unified multicloud control plane | Unified management of multiple multicloud instances with a unified request entry |
| | [One-click cluster import](../kairship/cluster.md) | Import multicloud clusters with one click |
| | [Rich dispatch and override policies](../kairship/policy/propagation.md) | Provide rich multicloud application [dispatch policies](../kairship/policy/propagation.md) and [override policies](../kairship/policy/override.md) |
| | [Failover](../kairship/failover/failover.md) | Multicloud application failover capability |
| | [Multicloud workloads](../kairship/workload/deployment.md) | Create and manage multicloud workloads, with [one-click conversion](../kairship/workload/promote.md) of regular workloads into multicloud workloads |
| | [Multicloud resource management](../kairship/resource/ns.md) | Unified management of multicloud namespaces, services, Ingresses, ConfigMaps, Secrets, and other resources |
| [Container Registry](../kangaroo/intro/index.md) | [Managed Harbor](../kangaroo/managed/harbor.md) | Create and manage Harbor instances with one click for secure hosting of images and Helm charts |
| | [Registry space](../kangaroo/space/index.md) | Workspace-based registry space management, supporting image scanning, reclamation, and manifest management |
| | [Integrated registries](../kangaroo/integrate/integrate-ws.md) | Integrate external registries (Harbor, Docker Registry, etc.) with unified credential and repository management |
| [Virtual Machine (Virtnest)](../virtnest/intro/index.md) | [VM lifecycle management](../virtnest/vm/index.md) | Create, clone, snapshot, and schedule virtual machines, with GPU passthrough support |
| | [Live migration and snapshots](../virtnest/vm/live-migration.md) | Support [live migration](../virtnest/vm/live-migration.md) and [scheduled snapshots](../virtnest/vm/scheduled-snapshot.md) of virtual machines to ensure business continuity |
| | VM templates | Provide out-of-the-box virtual machine templates for rapid batch creation of VMs |
| [Networking](../network/intro/index.md) | Multi-CNI portfolio solutions | Support multiple CNIs and their combinations (Cilium, Calico, etc., with eBPF-accelerated Overlay + Underlay), covering cross-cloud and cross-cluster connectivity |
| | [Subnet and IP pool management](../network/config/ippool/createpool.md) | Provide subnet and IP pool creation and allocation management for Underlay networks |
| | Network policy and observability | Provide network connectivity checks, network policy configuration, and link quality analysis |
| [Storage (HwameiStor)](../storage/hwameistor/intro/index.md) | Local storage | Provide local disk and LVM-based cloud native storage solutions with low latency and high throughput |
| | Storage high availability | DRBD-based data volume replication for storage-level disaster recovery |
| | Storage use cases | Provide [high-availability volumes](../storage/hwameistor/application/ha.md) and other persistence solutions for common applications such as TiDB and MinIO |
| [Cloud Edge Collaboration](../kant/intro/index.md) | [Edge unit management](../kant/user-guide/edge-unit/manage-unit.md) | Create and manage internal/external edge units and dispatch applications to units in batches |
| | [Edge applications](../kant/user-guide/edge-app/index.md) | Create edge applications individually or in batches and deploy them to specified edge units |
| | [End device management](../kant/user-guide/device/index.md) | Register and manage end devices, supporting binding devices to edge nodes and reporting device data |
| [One-stop Microservice Governance](../skoala/intro/index.md) | Centralized registry management | Centrally manage all dynamic microservices in clusters |
| | [Microservice traffic governance](../skoala/cloud-ms/traffic-control.md) | Quickly integrate with mainstream microservice frameworks |
| | Registry and configuration center | Centrally manage and configure microservice-related resources |
| | [Microservice gateway](../skoala/gateway/index.md) | Manage north-south traffic control for microservices |
| | [Traditional microservice hosting](../skoala/trad-ms/hosted/index.md) | Provide hosted and integrated registries so traditional microservices such as Spring Cloud and Dubbo can be onboarded without modification |
| | [Plugin center](../skoala/plugins/index.md) | Provide a rich gateway plugin ecosystem for authentication, rate limiting, caching, etc. |
| [Service Mesh](../mspider/intro/index.md) | [Hosted/dedicated mesh](../mspider/user-guide/service-mesh/index.md) | Create hosted and dedicated meshes with one click, unifying multicluster service governance capabilities |
| | [Multicloud mesh deployment](../mspider/user-guide/multicluster/multicluster-install.md) | Support multicloud mesh deployment and multi-cluster network interconnection for cross-cluster service communication |
| | [East-west traffic governance](../mspider/user-guide/traffic-governance/virtual-service.md) | Fine-grained east-west traffic governance and fault recovery based on VirtualService and DestinationRule |
| | [Traffic lane](../mspider/user-guide/traffic-lane/index.md) | End-to-end traffic lanes for gray-scale release scenarios |
| [Observability](../insight/intro/index.md) | Out-of-the-box | An application-centric, new-generation cloud native observability platform with unified collection of metrics, logs, and traces for rapid fault location and troubleshooting |
| | Real-time monitoring and alerting | Collect metrics, logs, and events to analyze application health status, providing alerting and multi-dimensional data visualization |
| | Open compatibility | Compatible with mainstream open-source components, providing quick fault location and one-click monitoring diagnostics |
| | [Unified alert center](../insight/user-guide/alert-center/index.md) | One-stop management of alert policies, message templates, silences, and inhibitions |
| | [Dashboards](../insight/user-guide/dashboard/index.md) | Provide out-of-the-box built-in dashboards with support for importing custom Grafana panels |
| [Unified User Authority System](../ghippo/intro/index.md) | [Centralized user/group management](../ghippo/user-guide/access-control/user.md) | Unified user/group management across functional modules, connecting user systems and reducing management and operations costs |
| | Multiple authorization models | Meet the needs of different enterprise scales, organizational structures, and authorization models with shortest-path authorization |
| | [Enterprise-level access control](../ghippo/user-guide/access-control/oidc.md) | Unified authentication login system; access the container management platform through federated authentication to achieve single sign-on |
| | [Workspace/folder management](../ghippo/user-guide/workspace/index.md) | Highly aligned with enterprise business hierarchies, meeting resource isolation and management needs across departments |
| | Flexible resource division | Resource division and binding based on resource granularity (namespaces, clusters, registries, etc.), with unified allocation of container platform resources |
| | [Audit logs](../ghippo/user-guide/audit/index.md) | Record user and API operations across the platform, with retrieval and export by operation type, time, and other dimensions |
| | [Operation management](../ghippo/user-guide/report-billing/index.md) | Integrate metering and billing systems, providing reports and billing management for departments/tenants |
| [Featured Middleware](../middleware/index.md) | Mainstream middleware | Supports [MySQL](../middleware/mysql/intro/index.md), [Redis](../middleware/redis/intro/index.md), [PostgreSQL](../middleware/postgresql/intro/index.md), [Elasticsearch](../middleware/elasticsearch/intro/index.md), [Kafka](../middleware/kafka/intro/index.md), [RocketMQ](../middleware/rocketmq/intro/index.md), [RabbitMQ](../middleware/rabbitmq/intro/index.md), [MongoDB](../middleware/mongodb/intro/index.md), [MinIO](../middleware/minio/intro/index.md), [SeaweedFS](../middleware/seaweedfs/intro/index.md), etc. |
| | Lifecycle management | Full lifecycle management of instances, supporting various high-availability cluster modes with custom replicas and configurations for different scenarios |
| | Online scaling | Online scaling of resources and storage |
| | Unified monitoring | Unified monitoring of instance resources and business dimensions |
| | Multi-tenant permissions | Permission management for multi-tenant requirements based on workspaces |

## Product Advantages

| Product Advantage | Description |
| :--- | :--- |
| Easy to use | One-click creation/joining of container clusters for unified management of large-scale clusters across clouds; graphical pipeline creation for various scenarios; one-stop application distribution compatible with multiple application formats |
| | No need to perceive differences in the underlying Kubernetes platform; simplified application deployment lowers the barrier to cloud adoption, allowing users to focus on business development without worrying about underlying infrastructure |
| | Establishes a foundation for users to **use multiple clusters like they use a single cluster** |
| Production ready | High availability of applications, supporting distributed deployment and automatic traffic switching in case of single-point failures |
| | Compatible with traditional and cloud native microservice frameworks: traditional frameworks require no modification and are transparently onboarded, with high compatibility with traditional registries such as Zookeeper and cloud native Kubernetes and Mesh registries; also supports mainstream open-source microservice frameworks such as Spring Cloud and Dubbo, and open-source gateway components such as Envoy, Sentinel, and Contour |
| | Rich monitoring metrics enable all-round application monitoring with early warning of traffic peaks and application failures |
| Continuous delivery | Containerized application build and customizable pipeline creation simplify the delivery process |
| | Based on container technology, applications can be rapidly deployed, verified, and promoted across different environments |
| | Compatible with multiple application formats, accommodating diverse deployment and management scenarios |
| Safe and reliable | Self-built clusters default to high-availability deployment mode; when a node fails or a natural disaster occurs, applications continue to run without business interruption |
| | Cross-region high availability, supporting business deployment on multiple cloud container clusters in different regions; when one cluster fails, unified traffic distribution automatically switches business traffic to other platforms |
| | Platform backup and disaster recovery solutions protect platform data and business security |
| | Three-in-one monitoring system based on centralized cluster management, implementing multi-layer, multi-dimensional monitoring of clusters, nodes, components, and applications for rapid fault location and troubleshooting |
| | Comprehensive user permission system integrating Kubernetes RBAC, supporting fine-grained permissions for different users, achieving resource isolation and business data security |
| Hybrid and heterogeneous | Multicloud heterogeneous management across on-premises and different vendors' container cloud platforms |
| | Highly automated and elastic heterogeneous multicloud support, adapting to x86 and Xinchuang (domestic innovation) cloud architectures |
| | Support mixed-cluster deployment and unified management of x86 and ARM architectures, stably running applications and ensuring network interconnectivity |
| Open compatibility | Based on native Kubernetes and Docker technology, fully compatible with Kubernetes API and kubectl commands |
| | A rich plugin system extends cloud container cluster capabilities, such as Multus, Cilium, Contour, and other [network plugins](../network/intro/index.md) |

[Download Center](https://docs.daocloud.io/en/download/){ .md-button }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button }
