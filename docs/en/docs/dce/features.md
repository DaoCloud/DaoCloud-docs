# features

DaoCloud Enterprise (DCE) 5.0 combines a large number of featueres, and the typical featuers currently supported are as follows. 

=== "[multi-cluster management](../kpanda/03ProductBrief/WhatisKPanda.md)"

- Unified management of multi-cluster, supporting Kubernetes clusters in all version ranges to be included in the container management scope. 

- Rapid cluster deployment. Rapidly deploys enterprise-level Kubernetes clusters on the Web UI, quickly builds enterprise-level container cloud platform, and adapt to the underlying environment of physical machines and VMs. 

- One-click cluster upgrade. Upgrade the Kubernetes version with one click, and manage the upgrade of system components. 

- Cluster high avalability,the built-in cluster disaster recovery and backup abilities ensure that business systems can recover from host failures, equipment room interruptions, and natural disasters, improving the stability of the production environment and reducing the risk of business interruption.

- Full lifecycle management of clusters, realizing the full lifecycle management of self-build cloud native clusters. 

- Open API ability, providing native Kubernetes Open API ability. 

=== "Cloud native application management"

- Multi-form cloud native application management, realizing the deployment and lifecycle management of different types of cloud native application, supporting cloud native application, Helm, OEM, etc., and open multicloud application compatibility. 

- One-stop deployment to decouple the underlying Kubernetes platform. One-stop deployment, operation and maintenance of service application to realize the lifecycle-management of application. 

- Expansion and reduction of application load. It can manually/automatically expand and reduce the application load, and customize the policies of expansion and reduction to cope with the traffic peak. 

- The full lifecycle of application, supporting lifecycle-management of application such as application view, update, delete, rollback, time view, and upgrade. 

- Unified load management abbility of cross-cluster. 

=== "[Continuous business delivery](../amamba/01ProductBrief/WhatisAmamba.md)"

- Enterprise-level cloud native CI/CD capabilities enable standardized continuous integration and delivery ability, and agile iteration of applications. It meets new business needs quickly, and improve the efficiency of application integration and release. 

- Cloud-native ability of continuous delivery, containerized management of application construction environment, and custom build machine and other resources to ensure pipeline-level resource isolation, and supporting multiple types of application deployment, making the delivery of cloud-native application easier. 

- Improve R&D (Research and Development) efficiency. In a visual pipeline construction environment, declarative steps are pre-packaged, and complex pipelines can be created without scripts, making operation simpler. The environment can be automatically created/destroyed according to the resource size to avoid resource waste. 

- Pipelines are code. Pipelines based on declarative (grammar) are easy to learn. The grammar of different steps is standardized. Its configuration is characterized by controllable version, modularization, reusability and declarative. 

- DevOps tools popular in the community are integrated. Stepes in a single pipelines can run on multiple operating systems and multiple architecture nodes. Independent deployment on public cloud, private cloud or host is supported, and enterprise owned systems and platform can be well integrated. 
  The integration of mainstream software in the industry, such as Kubernetes, Gitlab, SonarQube, Harbor, are supported. 

=== "[Multicloud application dispatch](../kairship/01product/whatiskairship.md)"

- Unified multicloud orchestration management, unified management of multiple cloud instances, and unified request entry. 

- One-click import of multicloud clusters. 

- Rich multicloud application dispatch strategies, coverage strategies, etc. 

- Multicloud application failover function. 

=== "[Unified user authority system](../ghippo/01ProductBrief/WhatisGhippo.md)"

- Centralized management of user/user group, unified user/user group management by multi-functional modules, opening up the user system and reducing management, operation and maintenance costs. 

- The multi-model authorization model meets the needs of different enterprise scales, organizational strcture users and authorization models, realizing the shortest link authorization. 

- Enterprise-level access control, unified authentication login system, and access to the container management platform through joint authentication to achieve single sign-on. 

- Provide workspace/hierarchy management which is highly compatibel with enterprise business level, and meets the resource isolation and management requirements between departement levels.

- Flexible resource division. Resource division and binding based on resource granularity (namespace, cluster, registry, etc.), and unified allocation of container platform resources.

=== "One-stop[Microservice governance](../skoala/intro/features.md)"

- The Microservice registry centrally manages all dynamic Microservices in the cluster.

- The Microservice traffic governance modle can be quickly integrated with mainstream Microservice frameworks.

- The registration configuration center can centally manage and configure Microservice-related resources.

- The Microservice gateway plays an important role in managing the north-south traffic control of Microservices.

=== "[Observable](../insight/03ProductBrief/WhatisInsight.md)"

- The application-centric, out-of-the-box, new generation cloud-native observability operation and maintenance platform realizes fast fault location and quick troubleshooting.

- Monitor applications and resources in real time, collect data such as various indicators, logs, and events to analyze application health status, and provide alarm capabilities and comprehensive, clear, and multi-dimensional data visualization capabilities.

- The mainstream open source compoments are open and compatible, providing fast fault location and one-key monitoring and diagnosis capabilities. 

- It provides unified collection of indicators, logs, and links, supports multi-dimensional alarms on indicators and logs, and provides a concise and clear visual management interface.

=== "Featured [Middleware](../middleware/midware.md)"

- It supports a variety of mainstream middleware: Redis, MySQL, Elasticsearch, RabbitMQ, Kafka, MinIO, etc.

- It supports life-cycle management of instances, meets a variety of high-availability cluster modes, and can custom the replicas and configuration according to the needs of the scene.

- It supports online resource and storage expansion.

- It supports unified monitoring of instance resources and business dimensions.

- Permission management for multi-tenant requirements can be implemented based on workspaces.

[Apply for a free community experience](license0.md){ .md-button .md-button--primary }
[Install DCE 5.0](../install/install-dce-community.md){ .md-button .md-button--primary }