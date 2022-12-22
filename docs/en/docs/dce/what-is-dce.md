---
hide:
  - toc
---

# DaoCloud Enterprise 5.0

DaoCloud Enterprise 5.0 is a high-performance, scalable cloud-native operating system that provides a consistent and stable experience on any infrastructure and in any environment. It supports hybrid, edge, and multicloud orchestration. DCE 5.0 integrates the latest service mesh and microservice technologies to track every flow and help you gain insight into the detailed metrics of clusters, nodes, applications, and services, and visualize the health status of applications through dynamic dashboards and topology maps.

DCE 5.0 natively supports the DevOps development and operation and maintenance mode, which can realize the full process standardization and automation of application delivery, and integrate various selected databases and middleware to make operation and maintenance governance more efficient. The various product modules of DCE 5.0 are independently decoupled and support flexible upgrades without affecting the business, and can be docked with many cloud-native ecological products to provide a complete solution system. It has been tested by nearly a thousand industry customers' production scenarios, and has built a solid and reliable digital foundation to help enterprises define digital boundaries and release cloud-native productivity.

<div class="grid cards" markdown>

- :fontawesome-solid-jet-fighter-up: **Installation** [Install Community and Commercial releases](../install/intro.md)
- :octicons-container-16: **Container Management** [Manage multi-cluster containers and pods](../kpanda/03ProductBrief/WhatisKPanda.md)
- :fontawesome-solid-user-group: **Global Management** [Login, user and access, appearance](../ghippo/01ProductBrief/WhatisGhippo.md)
- :material-monitor-dashboard: **Observability** [One-stop graphical dashboard](../insight/03ProductBrief/WhatisInsight.md)
- :material-microsoft-azure-devops: **Workbench** [CI/CD pipeline](../amamba/01ProductBrief/WhatisAmamba.md)
- :material-cloud-check: **Multicloud Orchestration** [Manage multi-cloud instances, workloads, policies](kairship/01product/whatiskairship.md)
- :material-engine: **Microservice Engine** [Microservice registry and gateway](../skoala/select-workspace.md)
- :material-table-refresh: **Service Mesh** [Non-intrusive service governance](../mspider/01Intro/WhatismSpider.md)
- :material-middleware: **Middleware** [ES, Kafka, MinIO, MySQL, etc.](../middleware/midware.md)
- :material-warehouse: **Container Registry** [Integrate and manage registries](../kangaroo/intro.md)
- :material-dot-net: **Network** [Multi-CNI fusion solution](../network/intro/what-is-net.md)
- :floppy_disk: **Storage** [Comprehensive solution for containerized storage](../hwameistor/intro/what.md)

</div>

![modules](../images/dce-modules04.png)

In the past eight years, DaoCloud has invested huge to explore and develop a cloud-native operating system with custom and scalable modules to facilitate your business digitalization. You can use each module like a LEGO brick, with zero downtime while upgrading any module. DCE 5.0 is also easy to integrate with hundreds of cloud-native ecological plugins, so you can simply customize solutions for different scenarios. Things go better with such a kind of modular style to grow day by day.

=== "Multicloud Orchestration"

    **Applicable scenarios**: The deployment of multicloud and multi-cluster in an enterprise has become the norm, and it is hoped to have the capabilities of multicloud app release and cross-cloud disaster recovery.

    **Benefits**: Using innovative technologies to orchestrate disaster recovery (DR) across clouds, this solution has high concurrent performance of cross-cloud resource retrieval, and can help your IT departments quickly plan and implement DR capabilities in combination with the capabilities of the Container Management to adapt to various scenarios such as edge and Xinchuang.

    **Modules**: [Container Management](../kpanda/03ProductBrief/WhatisKPanda.md), [Multicloud Orchestration](../kairship/01product/whatiskairship.md), cloud to edge continuum, Xinchuang Heterogeneous

    ![multi-cloud](../images/01multi-cloud.png)

=== "Data Service"

    **Applicable scenarios**: An enterprise has an app architecture that relies on mainstream middleware capabilities. It is hoped to run and maintain middleware in a unified manner and get more professional support capabilities for middleware planning, operation, and maintenance (O&M).

    **Benefits**: This solution has selected middlewares with a consistent UI to manage, with the help of HwameiStor capabilities designed for stateful applications, providing features of multi-tenant, deployment, observation, backup, operation and maintenance of the whole lifecycle of middleware management capabilities.

    **Modules**: [Container Management](../kpanda/03ProductBrief/WhatisKPanda.md), [HwameiStor](../hwameistor/intro/what.md), [Middleware](../middleware/midware.md)

    ![data](../images/02data.png)

=== "Microservice Governance"

    **Applicable scenarios**

    An enterprise decides to adopt a microservice architecture or has already adopted microservices, hopes to obtain a full range of technical support and O&M capabilities such as a microservice framework, or hopes to use service mesh technologies, and tries to achieve smoothness in the process of digital transformation.

    - The enterprise doesn't want to change anything, but just wants to view various service states via a panoramic view, and hopes to easily troubleshoot faults with traces and logs.
    - The enterprise has the idea of tranforming from the traditional microservice framework to service mesh, but it is more conservative. It is hoped that there will be a transition period for the gradual transformation. At this time, it is more suitable to use a service mesh solution.
    - The enterprise hopes to directly tranform to service mesh. In this case, it is a good idea to remove Eureka-related components and directly use the microservice engine and service mesh.
    - The enterprise does not want to tranform from traditional microservices to mesh, but wants to do east-west traffic management.

    **Benefits**

    Seamless integrate with legacy and popular microservice technologies, such as the first-generation microservices represented by SpringCloud and Dubbo and the new generation of microservices represented by Istio service mesh, with the lifecycle management capabilities of development, deployment, joining, exposing to external, observation, and O&M. Seamlessly add the existing microservice system of the enterprise, provide the complete capabilities of managed microservice governance, and offer the high-performance cloud-native microservice gateway.

    **Modules**: [Container Management](../kpanda/03ProductBrief/WhatisKPanda.md), [Microservice Engine](../skoala/intro/features.md), [Service Mesh](../mspider/01Intro/WhatismSpider.md), [Insight](../insight/03ProductBrief/WhatisInsight.md), [App Workbench](../amamba/01ProductBrief/WhatisAmamba.md)

    ![Microservie](../images/03msgov.png)

=== "Insight"

    **Applicable scenarios**: An enterprise has a weak capability to watch running applications, and hopes to complete the Insight through a lightweight or unmodified method, to get a panaramic view for current apps with logs, metrics, traces.

    **Benefits**: This solution provides in-depth and subtle observation of the current app status. With a comprehensive dashboard, you can query all cluster and workload data. It supports for microservice architecture, service mesh, eBPF-based network, and other observation capabilities.

    **Modules**: [Container Management](../kpanda/03ProductBrief/WhatisKPanda.md), [Insight](../insight/03ProductBrief/WhatisInsight.md)

    ![Insight](../images/04insight.png)

=== "App Store"

    **Applicable scenarios**: An enterprise wants to obtain out-of-the-box cloud native apps capabilities for some exclusive scenarios

    **Benefits**: This solution provides the ecological capabilities including software products from partners,  with a complete software stack to meet the actual business needs. Where, you can easily find, test, and deploy middlewares running on DaoCloud Enterprise 5.0 with a development process of low-code or no-code.

    **Modules**: [Container Management](../kpanda/03ProductBrief/WhatisKPanda.md), App Store, Product Ecosystem

=== "App Delivery"

    **Applicable scenarios**: An enterprise adopts cloud-native technology on a large scale, and expects to promote cloud-native technology to a wider range by combining with DevOps concepts.

    **Benefits**: With a consistent workflow to deliver apps, this solution supports a hierarchical multi-tenant system, seamlessly adapts to the user's organizational structure to plan resource allocation, automates app build and deployment with the CI/CD pipelines, and innovatively introduces the GitOps progressive delivery capability.

    **Modules**: [Container Management](../kpanda/03ProductBrief/WhatisKPanda.md), [App Workbench](../amamba/01ProductBrief/WhatisAmamba.md), Registry

    ![App Delivery](../images/06appdeliv.png)

=== "Cloud Native Base"

    **Applicable scenarios**: The O&M team of an enterprise needs to undertake tasks to maintain thousands of clusters, and the cluster network needs to meet the traditional network supervision requirements.

    **Benefits**: 

    Breaking through the performance bottleneck of Kubernetes API, this solution supports for ultra-large scale clusters concurrently, and provides full life-cycle management capabilities from deployment, rolling update, certificate management, configuration settings, and garbage collection.

    - MacVLAN solution
    - SR-IOV smart network acceleration solution
    - SpiderPool IPAM solution
    - Clilum eBPF-based network solution
    - Underlay and Overlay network continuum

    All clusters and workloads are managed through Clusterpedia. This solution is compatible with joining standard Kubernetes clusters, breaking through the performance bottleneck of Kubernetes API and supporting thousands of users using it at the same time.

    **Modules**: [Container Management](../kpanda/03ProductBrief/WhatisKPanda.md), [Cluster lifecycle manager](../community/kubean.md), [Network](../network/), [HwameiStor](../hwameistor/)

    ![Cloud Native Base](../images/07base.png)

=== "Xinchuang Heterogeneous"

    **Applicable scenarios**: An enterprise needs to set up Xinchuang infrastructure. For example, the CPU processor must be from one of Loongson, Hygon, Phytium, Kunpeng, Intel; and the operating system must be KirinOS, UOS, OpenEuler, etc.

    **Benefits**: This solution can consolidate Xinchuang cloud-native capabilities for government sectors and state-owned factories, supports domestic chips and servers in the north, and supports Xinchuang operating system and app ecosystem in containers in the south.

    **Modules**: [Container Management](../kpanda/03ProductBrief/WhatisKPanda.md), [Cluster lifecycle manager](../community/kubean.md), [信创中间件](../middleware/midware.md)

    ![Xinchuang](../images/08xinchuan.png)

=== "cloud to edge continuum"

    **Applicable scenarios**: An enterprise designs an edge collaboration solution on the basis of cloud, edge, and terminal. The edge is a general computing platform and has strict computing requirements. The edge supports several deployment modes: edge node, edge cluster, data center computing downwards, edge device computing upwards.

    **Benefits**: This solution extends the general cloud-native framework, empowers the edge computing capability, uniformly manages and controls all edge clusters and nodes. Based on the traditional three-tier model of cloud, edge, and terminal. To meet the strict edge computing requirements, this solution provides a four-tier model from cloud to edge continuum by adding the edge clusters and nodes.

    **Modules**: [Container Management](../kpanda/03ProductBrief/WhatisKPanda.md), [Cluster lifecycle manager](../community/kubean.md), Edge nodes, clusters in the weak network

    ![cloud-edge](../images/09cloud-edge.png)

Just like Lego bricks, it combines dozens of the best open source technologies into a platform. After many dialectical selection, adaptation and running-in, coding debugging, and massive testing, a sword is sharpened in ten years. The new generation of containerized platforms can meet the needs of various scenarios for enterprises migrating to the cloud.
