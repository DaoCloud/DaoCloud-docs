---
hide:
  - toc
---

# DaoCloud Enterprise 5.0

DaoCloud Enterprise 5.0 is a high-performance, scalable cloud-native operating system. It can provide a consistent and stable experience in any infrastructure and environment, supporting heterogeneous clouds, edge clouds, and Multicloud Management. DCE 5.0 integrates the latest service mesh and microservice technologies, which can track the entire lifecycle of each traffic, help you understand the detailed metrics of clusters, nodes, applications, and services, and visualize the health status of applications through dynamic dashboards and topology maps.

DCE 5.0 natively supports the DevOps development and operation mode, which can realize the standardization and automation of the entire app delivery process, and integrates various selected databases and middleware to make operation and maintenance governance more efficient. Each product module is independently decoupled, supports flexible upgrades, has no impact on business, and can be docked with many cloud-native ecological products to provide a complete solution system. It has been tested in production cases by nearly a thousand industry customers, building a solid and reliable digital foundation, helping enterprises define digital boundaries, and unleashing cloud-native productivity.

<div class="grid cards" markdown>

- :fontawesome-solid-jet-fighter-up: **Install** [Install Community Package and Enterprise Package](../install/intro.md)
- :octicons-container-16: **Container management** [Cluster/node/workload infrastructure](../kpanda/intro/what.md)
- :fontawesome-solid-user-group: **Global Management** [Set login/permissions/appearance](../ghippo/intro/what.md)
- :material-monitor-dashboard: **Observability** [One-stop graphical dashboard](../insight/intro/what.md)
- :material-microsoft-azure-devops: **Workbench** [CI/CD pipeline](../amamba/intro/what.md)
- :material-cloud-check: **Multicloud Management** [Multicloud instance/load/policy](../kairship/intro/what.md)
- :material-engine: **Microservice Engine** [Microservice Governance and Gateway](../skoala/intro/what.md)
- :material-table-refresh: **Service Mesh** [Non-intrusive service governance](../mspider/intro/what.md)
- :material-middleware: **Middleware** [ES, Kafka, MinIO, MySQL, etc.](../middleware/what.md)
- :material-warehouse: **Container Registry** [Registry integration and hosting service](../kangaroo/what.md)
- :material-dot-net: **Network** [Multi-CNI fusion solution](../network/intro/what-is-net.md)
- :floppy_disk: **Storage** [Containerized storage](../storage/what.md)

</div>

![modules](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/images/dce-modules04.jpg)

In the past eight years, DaoCloud has invested huge to explore and develop a cloud-native operating system with custom and scalable modules to facilitate your business digitalization. You can use each module like a LEGO brick, with zero downtime while upgrading any module. DCE 5.0 is also easy to integrate with hundreds of cloud-native ecological plugins, so you can simply customize solutions for different cases. Things go better with such a kind of modular style to grow day by day.

=== "Multicloud Management"

     Supports unified and centralized management of multicloud and hybrid clouds, provides cross-cloud resource retrieval and cross-cloud application deployment, release, and operation and maintenance capabilities, realizes efficient management and control of multicloud applications, provides elastic scaling of applications based on cluster resources, and achieves global load balancing. The fault recovery capability can effectively solve the problem of multicloud application disaster recovery, and help enterprises build multicloud and hybrid cloud digital infrastructure.

     **Modules involved**: [Global Management](../ghippo/intro/what.md), [Container Management](../kpanda/intro/what.md), [Multicloud Management](../kairship/intro/what.md), [cloud native network](../network/intro/what-is-net.md), [cloud native storage](../storage/what.md), Heterogeneous architecture

    ![multicloud](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/images/01multicloud.jpg)

=== "Data Middleware Service"

     The cloud-native local storage capability specially designed for stateful applications meets the high I/O storage requirements of middleware and improves the efficiency of operation and maintenance management. Select middleware such as various databases, distributed messages, and log retrieval,
     It provides middleware management capabilities for the whole life cycle of multi-tenancy, deployment, observation, backup, operation and maintenance operations, etc., and realizes self-service application, elastic expansion, high concurrent processing, and high stability and high availability of data services.

     **Related modules**: [Global Management](../ghippo/intro/what.md), [Container Management](../kpanda/intro/what.md), [Cloud Native Network](../network/intro/what-is-net.md), [cloud native storage](../storage/what.md), [selected middleware](../middleware/what.md)

    ![data](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/images/02data.jpg)

=== "Microservice Governance"

     Provides non-intrusive traffic management functions, supports non-sensing access to traditional microservices, cloud-native microservices, and open source microservice frameworks, and realizes the integrated management of existing microservice systems and old and new microservice systems of enterprises.
     Support the full life cycle management of microservices from development, deployment, access, observation, operation and maintenance, provide high-performance cloud-native microservice gateways, and ensure the continuous availability of microservice applications; introduce the independent open source eBPF mesh acceleration technology to comprehensively improve Traffic forwarding efficiency.

     **Related modules**: [Global Management](../ghippo/intro/what.md), [Container Management](../kpanda/intro/what.md), [Microservice Engine](../skoala/intro/what.md), [Service Mesh](../mspider/intro/what.md), [Observability](../insight/intro/what.md), [Workbench](../amamba/intro/what.md), [Cloud Native Network](../network/intro/what-is-net.md), [Cloud Native Storage](../storage/what.md)

    ![microservie engine](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/images/03msgov.jpg)

=== "Observability"

     Based on logs, traces, metrics, eBPF and other technical means, comprehensive collection of service data, in-depth acquisition of request link information, dynamic observation, multi-dimensional control of real-time changes in clusters, nodes, applications and services,
     Realize the query of all clusters and load observation data through a unified control plane, introduce topology analysis technology to visualize the application health status, and realize second-level fault location.

     *[eBPF]: Extended Berkeley Packet Filter, which is a component of the Linux kernel that can run sandboxed programs in the kernel

     **Modules involved**: [Global Management](../ghippo/intro/what.md), [Container Management](../kpanda/intro/what.md), [Observability](../insight/intro/what.md), [cloud-native network](../network/intro/what-is-net.md), [cloud-native storage](../storage/what.md)

    ![Observability](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/images/04insight.jpg)

=== "App Store"

     Include software products from ecological partners in ten major fields such as big data, AI, middleware, realize the integration of ecological technology, products, operation services and other capabilities, provide out-of-the-box ecological application software, and create a complete solution system.

     **Related modules**: [Global Management](../ghippo/intro/what.md), [Container Management](../kpanda/intro/what.md), [Cloud Native Network](../network/intro/what-is-net.md), [cloud native storage](../storage/what.md), app store, product ecology

=== "App Delivery"

     Realize self-service migration to the cloud through a consistent and scalable app delivery process, support flexible tenant systems, dynamically adapt to user organizational structure planning and real-time resource allocation, based on cloud-native CI/CD pipelines, integrate rich tool chains and support pipelines Efficient concurrent execution flow,
     Automate the construction and deployment of applications, innovatively introduce Gitops and progressive delivery capability systems, and achieve more refined management and operation of applications.

     **Modules involved**: [Global Management](../ghippo/intro/what.md), [Container Management](../kpanda/intro/what.md), [Workbench](../amamba/intro/what.md), [container registry](../kangaroo/what.md), [cloud native network](../network/intro/what-is-net.md), [cloud native storage](../storage/what.md)

    ![app delivery](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/images/06appdeliv.jpg)

=== "Heterogeneous architecture"

     Adopt heterogeneous cloud-native technology architecture, compatible with domestic chips and servers, support heterogeneous operating system and heterogeneous application ecosystem, shield the complexity of underlying heterogeneous infrastructure, and adapt traditional operating systems from software ecological compatibility that requires long-term accumulation liberated from
     Realize the flexible scheduling of mixed heterogeneous clusters, ensure the stability and reliability of heterogeneous application operating environment, and help heterogeneous process to further speed up.

     **Related modules**: [Global Management](../ghippo/intro/what.md), [Container Management](../kpanda/intro/what.md), [Cluster Lifecycle Management](../community/kubean.md), [heterogeneous Middleware](../middleware/what.md), [Cloud Native Network](../network/intro/what-is-net.md), [Cloud Native Storage](../storage/what.md)

    ![Heterogeneous](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/images/08xinchuan.jpg)

=== "Cloud to Edge Continuum"

     Extend the cloud-native capabilities to the edge, adopt the edge cluster and edge node mode, move the computing power of the data center down, and move up the computing power of the end device, and unify the control and scheduling of discrete and heterogeneous computing resources to solve the problem of massive edge and end devices. Unify the requirements of large-scale app delivery, operation and maintenance, and management and control on the Internet, and realize the true integration of cloud and edge.

     **Related modules**: [Global Management](../ghippo/intro/what.md), [Container Management](../kpanda/intro/what.md), [Cluster Lifecycle Management](../community/kubean.md), [cloud native network](../network/intro/what-is-net.md), [cloud native storage](../storage/what.md), weak network cluster

    ![Cloud to edge continuum](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/images/09cloud-edge.jpg)

=== "Cloud Native Base"

     Provide cloud native computing, [network](../network/intro/what-is-net.md), storage and other capabilities, compatible with various cluster access, support the whole life of the cluster from deployment, version upgrade, certificate change, configuration change, recycling, etc. Cycle management breaks through K8s API performance bottlenecks and enables large-scale enterprise users to use multiple clusters concurrently.
     For the enterprise environment, provide scenario-based network solutions to maximize the reuse of the current enterprise network infrastructure and lower the threshold for enterprises to use cloud-native applications.

     **Related modules**: [Global Management](../ghippo/intro/what.md), [Container Management](../kpanda/intro/what.md), [Cluster Lifecycle Management](../community/kubean.md), [cloud-native full-scenario network](../network/intro/what-is-net.md), [cloud-native storage](../storage/what.md)

[Download DCE 5.0](../download/dce5.md){ .md-button .md-button--primary }
[Install DCE 5.0](../install/intro.md){ .md-button .md-button--primary }
[Free Trial](./license0.md){ .md-button .md-button--primary }
