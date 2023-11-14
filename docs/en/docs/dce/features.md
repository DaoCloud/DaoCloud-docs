---
hide:
  - toc
---

# Features and Benefits

DaoCloud Enterprise (DCE) 5.0 combines a large number of features, and the typical features currently supported are as follows.

=== "[Multicluster management](../kpanda/intro/index.md)"

- Unified management of multicluster, supporting Kubernetes clusters in all version ranges to be included
  in the container management scope.
- Rapid cluster deployment. Rapidly deploys enterprise-level Kubernetes clusters on the Web UI, quickly builds
  enterprise-level container cloud platform, and adapt to the underlying environment of physical machines and VMs.
- One-click cluster upgrade. Upgrade the Kubernetes version with one click, and manage the upgrade of system components.
- Cluster high avalability, the built-in cluster disaster recovery and backup abilities ensure that business systems
  can recover from host failures, equipment room interruptions, and natural disasters, improving the stability of the
  production environment and reducing the risk of business interruption.
- Full lifecycle management of clusters, realizing the full lifecycle management of self-build cloud native clusters.
- OpenAPI capability, providing native Kubernetes openAPI ability.

=== "Cloud native application management"

- Multi-form cloud native application management, realizing the deployment and lifecycle management of different types
  of cloud native application, supporting cloud native application, Helm, OEM, etc., and open multicloud application compatibility.
- One-stop deployment to decouple the underlying Kubernetes platform. One-stop deployment, operation and maintenance of
  service application to realize the lifecycle-management of application.
- Expansion and reduction of application load. It can manually/automatically expand and reduce the application load, and
  customize the policies of expansion and reduction to cope with the traffic peak.
- The full lifecycle of application, supporting lifecycle-management of application such as application view, update,
  delete, rollback, time view, and upgrade.
- Unified load management abbility of cross-cluster.

=== "[Continuous business delivery](../amamba/intro/index.md)"

- Enterprise-level cloud native CI/CD capabilities enable standardized continuous integration and delivery ability, and
  agile iteration of applications. It meets new business needs quickly, and improve the efficiency of application
  integration and release.
- Cloud native ability of continuous delivery, containerized management of application construction environment, and
  custom build machine and other resources to ensure pipeline-level resource isolation, and supporting multiple types
  of application deployment, making the delivery of cloud native application easier.
- Improve R&D (Research and Development) efficiency. In a visual pipeline construction environment, declarative steps
  are pre-packaged, and complex pipelines can be created without scripts, making operation simpler. The environment
  can be automatically created/destroyed according to the resource size to avoid resource waste.
- Pipelines are code. Pipelines based on declarative (grammar) are easy to learn. The grammar of different steps is
  standardized. Its configuration is characterized by controllable version, modularization, reusability and declarative.
- DevOps tools popular in the community are integrated. Stepes in a single pipelines can run on multiple operating systems
  and multiple architecture nodes. Independent deployment on public cloud, private cloud or host is supported, and enterprise
  owned systems and platform can be well integrated. The integration of mainstream software in the industry, such as
  Kubernetes, Gitlab, SonarQube, Harbor, are supported.

=== "[Multicloud application dispatch](../kairship/intro/index.md)"

- Unified multicloud orchestration management, unified management of multiple cloud instances, and unified request entry.
- One-click import of multicloud clusters.
- Rich multicloud application dispatch strategies, coverage strategies, etc.
- Multicloud application failover function.

=== "[Unified user authority system](../ghippo/intro/index.md)"

- Centralized management of user/group, unified user/group management by multi-functional modules, opening up the
  user system and reducing management, operation and maintenance costs.
- The multi-model authorization model meets the needs of different enterprise scales, organizational strcture users
  and authorization models, realizing the shortest link authorization.
- Enterprise-level access control, unified authentication login system, and access to the container management platform
  through joint authentication to achieve single sign-on.
- Provide workspace/hierarchy management which is highly compatibel with enterprise business level, and meets the
  resource isolation and management requirements between departement levels.
- Flexible resource division. Resource division and binding based on resource granularity (namespace, cluster, registry, etc.),
  and unified allocation of container platform resources.

=== "One-stop [Microservice governance](../skoala/intro/index.md)"

- The Microservice registry centrally manages all dynamic Microservices in the cluster.
- The Microservice traffic governance modle can be quickly integrated with mainstream Microservice frameworks.
- The registration configuration center can centally manage and configure Microservice-related resources.
- The Microservice gateway plays an important role in managing the north-south traffic control of Microservices.

=== "[Insight](../insight/intro/index.md)"

- The application-centric, out-of-the-box, new generation cloud native observability operation and maintenance platform
  realizes fast fault location and quick troubleshooting.
- Monitor applications and resources in real time, collect data such as various metrics, logs, and events to analyze
  application health status, and provide alert capabilities and comprehensive, clear, and multi-dimensional data visualization capabilities.
- The mainstream open source compoments are open and compatible, providing fast fault location and one-key monitoring
  and diagnosis capabilities.
- It provides unified collection of metrics, logs, and traces, supports multi-dimensional alerts on metrics and logs,
  and provides a concise and clear visual management interface.

=== "Featured [Middleware](../middleware/index.md)"

- It supports a variety of mainstream middleware: Redis, MySQL, Elasticsearch, RabbitMQ, Kafka, MinIO, etc.
- It supports life-cycle management of instances, meets a variety of high-availability cluster modes, and can
  custom the replicas and configuration according to the needs of the scene.
- It supports online resource and storage expansion.
- It supports unified monitoring of instance resources and business dimensions.
- Permission management for multi-tenant requirements can be implemented based on workspaces.

## Product Advantages

=== "Easy to Use"

- One-click creation/joining of container clusters for unified management of large-scale clusters across
  clouds/clusters. Graphical creation of pipelines to meet various needs. One-stop application distribution,
  compatible with multiple application formats. Comprehensive one-stop cloud native management platform.
- No need to perceive differences in the underlying Kubernetes platform, simplifying the application
  deployment process and lowering the difficulty of deploying applications to the cloud, allowing users
  to focus on application development without worrying about underlying infrastructure settings. At the
  same time, it establishes a foundation for users to **use multiple clusters like they use a single cluster** .

=== "Production Ready"

- High availability of applications, supporting distributed deployment of applications and automatic
  switching of traffic in case of single-point failures.
- Simplifying the application deployment process and lowering the difficulty of deploying applications
  to the cloud, allowing users to focus on application development without worrying about underlying
  infrastructure settings. At the same time, it establishes a foundation for users to
  **use multiple clusters like they use a single cluster** .
- Compatible with traditional microservice frameworks and cloud native frameworks.
  Traditional microservice frameworks do not require modification and can be easily integrated,
  highly compatible with traditional registration centers such as Zookeeper, as well as cloud native
  Kubernetes and Mesh registration centers. It also supports mainstream open-source microservice
  frameworks, such as Spring Cloud and Dubbo, and open-source gateway components, such as Envoy, Sentinel, and Contour.
- Rich monitoring metrics to achieve all-round monitoring of applications and early warning of
  high traffic peaks and application failures.

=== "Continuous Delivery"

- Containerized application construction and customizable pipeline creation simplify the delivery process.
- Based on container technology, applications can be quickly deployed, verified, and circulated in different environments.
- Compatible with multiple application formats, accommodating diverse deployment and management use cases.

=== "Safe and Reliable"

- The self-built cluster defaults to a high-availability deployment mode to ensure the high availability
  of your business. When a node fails or a natural disaster occurs, the application can continue to run,
  ensuring high availability in production environments and ensuring uninterrupted operation of business application systems.
- High availability of cross-region applications, supporting cross-region deployment of different container
  clusters and deploying business on multiple cloud container clusters in different regions to help applications
  achieve traffic distribution across multiple regions.
  When a cloud container cluster fails, the data center is down, or a natural disaster occurs, the mechanism of
  unified traffic distribution automatically switches the business traffic to other cloud container platforms,
  ensuring high availability of the application.
- Providing platform backup and disaster recovery solutions to ensure platform data and business security.
- Comprehensive monitoring system with a three-in-one monitoring system based on centralized cluster management
  that implements multi-layer and multi-dimensional monitoring mechanisms for clusters, nodes, components,
  and applications, facilitating rapid fault location and troubleshooting.
- Perfect user permission system that integrates Kubernetes RBAC permission system, supporting fine-grained
  permissions for different users, achieving resource isolation, and ensuring the security of business data.

=== "Hybrid Heterogeneous"

- Multicloud heterogeneous, realizing the heterogeneous management capability of clouds and different
  vendor container cloud platforms.
- Providing highly automated and elastic heterogeneous multicloud support capabilities, adapting to x86
  and ARM cloud system architectures.
- Supporting mixed-cluster deployment and unified management of x86 and ARM architectures, stably
  supporting application operations, and ensuring network interconnectivity between applications.

=== "Open Compatibility"

- Based on native Kubernetes and Docker technology, fully compatible with Kubernetes API and Kubectl commands.
- Provides a rich plug-in system to extend the functionality of cloud container clusters, such as Multus,
  Cillum, Contour, and other [network plug-ins](../network/intro/index.md).

[Download DCE 5.0](../download/index.md){ .md-button .md-button--primary }
[Install DCE 5.0](../install/index.md){ .md-button .md-button--primary }
[Free Trial](license0.md){ .md-button .md-button--primary }
