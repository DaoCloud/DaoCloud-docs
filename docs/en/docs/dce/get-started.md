---
MTPE: windsonsea
date: 2024-01-09
hide:
  - toc
---

# Get Started

In the current era, cloud native containerization technology is rapidly evolving and making waves worldwide.
To seize this market trend and capitalize on significant business opportunities, it is crucial to stay in
sync with the pulse of the times. Transforming data centers into Kubernetes (K8s) infrastructure undoubtedly
represents the best pathway to achieving the cloud native landscape.

DCE 5.0, built on K8s as its development foundation, offers highly scalable and powerful features for
production-grade functionality, enabling enterprises to effortlessly build and manage distributed applications.
Leveraging the inherent cloud native capabilities of DCE 5.0, businesses can fully leverage the advantages of
both on-premises and cloud environments, optimizing resource utilization, improving the reliability and
elasticity of IT systems, and significantly accelerating application delivery.

!!! tip

    Embrace the wave of containerization and embark on an exploratory journey with DaoCloud Enterprise 5.0!

## Installation and Tutorials

<div class="grid cards" markdown>

- :fontawesome-solid-jet-fighter-up:{ .lg .middle } __Installation__

    ---

    DCE 5.0 supports both offline and online installation methods, and can be installed on various Linux distributions.

    - [Install Dependencies](../install/install-tools.md)
    - [Install Community Package](../install/community/resources.md)
    - [Install Enterprise Package](../install/commercial/deploy-requirements.md)
    - [Install on Different Linux Distributions](../install/os-install/uos-v20-install-dce5.0.md)
    - [Install on Different K8s Versions](../install/k8s-install/ocp-install-dce5.0.md)

- :material-microsoft-azure-devops:{ .lg .middle } __Video Tutorials__

    ---

    We have created many video tutorials for different modules and scenarios of DCE 5.0.

    - [Scenario-based Videos](../videos/use-cases.md)
    - [Workbench Videos](../videos/amamba.md)
    - [Container Management Videos](../videos/kpanda.md)
    - [Microservices Videos](../videos/skoala.md)
    - [Middleware Videos](../videos/mcamel.md)
    - [Global Management Videos](../videos/ghippo.md)

</div>

## Product Modules

<div class="grid cards" markdown>

- :material-microsoft-azure-devops:{ .lg .middle } __Workbench__

    ---

    This is a container-based DevOps cloud native application platform, serving as the unified entry point for creating applications in DCE 5.0.

    - [Creating Applications with Wizard](../amamba/user-guide/wizard/create-app-git.md)
    - [Pipelines](../amamba/user-guide/pipeline/create/custom.md)
    - [GitOps](../amamba/user-guide/gitops/create-argo-cd.md)
    - [Canary Release](../amamba/user-guide/release/canary.md)
    - [Integrated Toolchain](../amamba/user-guide/tools/integrated-toolchain.md)

- :octicons-container-16:{ .lg .middle } __Container Management__

    ---

    This containerization management module is built on Kubernetes (K8s) and designed for cloud native applications, serving as the core of DCE 5.0.

    - [Cluster Management](../kpanda/user-guide/clusters/create-cluster.md)
    - [Node Management](../kpanda/user-guide/nodes/add-node.md)
    - [Namespace Management](../kpanda/user-guide/namespaces/createns.md)
    - [Workloads: Deployment, StatefulSet, DaemonSet, Job, CronJob](../kpanda/user-guide/workloads/create-deployment.md)
    - [Helm Applications](../kpanda/user-guide/helm/helm-app.md)

</div>

<div class="grid cards" markdown>

- :material-cloud-check:{ .lg .middle } __MultiCloud Orchestration__

    ---

    This is a user-centric, out-of-the-box multicloud application orchestration platform that provides centralized management for multicloud and hybrid cloud environments.

    - [MultiCloud Working Clusters](../kairship/cluster.md)
    - [MultiCloud Workloads](../kairship/workload/deployment.md)
    - [MultiCloud Custom Resources](../kairship/crds/crd.md)
    - [Resource Management: Service, Routing, Namespace, etc.](../kairship/resource/service.md)
    - [Policy Management](../kairship/policy/propagation.md)

- :material-warehouse:{ .lg .middle } __Container Registry__

    ---

    This is a cloud native image hosting service that supports the management of multiple instances and integrates with container registries like Harbor and Docker.

    - [Registry Spaces](../kangaroo/space/index.md)
    - [Registry Integration (Workspace)](../kangaroo/integrate/integrate-ws.md)
    - [Registry Integration (Admin)](../kangaroo/integrate/integrate-admin.md)
    - [Managed Harbor](../kangaroo/managed/intro.md)

</div>

<div class="grid cards" markdown>

- :material-engine:{ .lg .middle } __Microservice Engine__

    ---

    This is a comprehensive microservice management platform tailored for mainstream microservice ecosystems.

    - [Cloud Native Gateway](../skoala/gateway/index.md)
    - [Cloud Native Microservices](../skoala/cloud-ms/index.md)
    - [Traditional Microservices](../skoala/trad-ms/hosted/index.md)
    - [Plugin Center](../skoala/plugins/intro.md)

- :material-table-refresh:{ .lg .middle } __Service Mesh__

    ---

    This next-generation service mesh is built on Istio and designed for cloud native applications.

    - [Traffic Governance](../mspider/user-guide/traffic-governance/README.md)
    - [Security Governance](../mspider/user-guide/security/README.md)
    - [Sidecar Management](../mspider/user-guide/sidecar-management/workload-sidecar.md)
    - [Traffic Monitoring](../mspider/user-guide/traffic-monitor/README.md)

</div>

<div class="grid cards" markdown>

- :material-middleware:{ .lg .middle } __Middleware 1__

    ---

    DCE 5.0 selects classic middleware to process data for practical application scenarios.

    - [Elasticsearch Search Service](../middleware/elasticsearch/intro/index.md)
    - [MinIO Object Storage](../middleware/minio/intro/index.md)
    - [MySQL Database](../middleware/mysql/intro/index.md)
    - [PostgreSQL Database](../middleware/postgresql/intro/index.md)

- :material-middleware:{ .lg .middle } __Middleware 2__

    ---

    DCE 5.0 selects classic middleware to process data for practical application scenarios.

    - [MongoDB Database](../middleware/mongodb/intro/index.md)
    - [Redis Cache Service](../middleware/redis/intro/index.md)
    - [RabbitMQ Message Queue](../middleware/rabbitmq/intro/index.md)
    - [Kafka Message Queue](../middleware/kafka/intro/index.md)

</div>

<div class="grid cards" markdown>

- :fontawesome-solid-user-group:{ .lg .middle } __Global Management__

    ---

    It focuses on user-centric services, including access control, workspaces, audit logs, platform settings.

    - [Access Control](../ghippo/user-guide/access-control/user.md)
    - [Workspaces and Folders](../ghippo/user-guide/workspace/workspace.md)
    - [Audit Logs](../ghippo/user-guide/audit/open-audit.md)
    - [Operations Management and System Settings](../ghippo/user-guide/platform-setting/appearance.md)

- :material-monitor-dashboard:{ .lg .middle } __Insight__

    ---

    This provides real-time monitoring of applications and resources, collects metrics, logs, and events to analyze the health status.

    - [Infrastructure Monitoring](../insight/user-guide/scenario-insight/cluster.md)
    - [Log Query](../insight/user-guide/data-query/log.md)
    - [Tracing](../insight/user-guide/data-query/trace.md)
    - [Alerts](../insight/user-guide/alert-center/index.md)

</div>

<div class="grid cards" markdown>

- :material-dot-net:{ .lg .middle } __Cloud Native Networking__
    
    ---

    It provides support for both single CNI networks and combinations of multiple CNI networks.

    - [Network Interface and Planning](../network/plans/ethplan.md)
    - [Performance Testing Report](../network/performance/cni-performance.md)
    - [Integrating Different CNIs](../network/modules/calico/install.md)

- :floppy_disk:{ .lg .middle } __Cloud Native Storage__
    
    ---

    It is based on the K8s CSI standard and can integrate with different storage solutions based on different SLA requirements and user cases.

    - [Introduction to DCE 5.0 Cloud Native Storage](../storage/index.md)
    - [HwameiStor Local Storage](../storage/hwameistor/intro/index.md)
    - [Integrating Open-Source Storage Solutions](../storage/solutions/rook-ceph.md)

</div>

## Download and Ecosystem

<div class="grid cards" markdown>

- :material-download:{ .lg .middle } __Download Center__

    ---

    It contains offline installation packages for the DCE 5.0 Community Package, Enterprise Package, and sub-modules.

    - [Download Community Package](../download/free/dce5-installer-history.md)
    - [Download Enterprise Package](../download/business/dce5-installer-history.md)
    - [Download Sub-Modules](../download/index.md#download-modules)

- :simple-opensourceinitiative:{ .lg .middle } __DaoCloud Open Source Ecosystem__

    ---

    DaoCloud adheres to an open source enterprise culture, with multiple open source technologies included in the CNCF Sandbox.

    - [Clusterpedia: Multi-Cluster Encyclopedia](../community/clusterpedia.md)
    - [HwameiStor: Local Storage](../community/hwameistor.md)
    - [Merbridge: Service Mesh Acceleration](../community/merbridge.md)

</div>

*[DCE]: An abbreviation for DaoCloud Enterprise, a next-generation AI computing platform

!!! success

    ```yaml
    What leads to a company's success?
      It's the shared dream, a unified vision,
        The joy of open source, collaborative decision.
          Thriving on the thrill, working day and night,
            Building magical things that shine so bright.

    Together, let us now unite,
      Honoring efforts past, present, future with delight.
    ```

[Download DCE 5.0](../download/index.md){ .md-button .md-button--primary }
[Install DCE 5.0](../install/index.md){ .md-button .md-button--primary }
[Free Trial](./license0.md){ .md-button .md-button--primary }

![Sail Image](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/dce/images/sail.jpg)
