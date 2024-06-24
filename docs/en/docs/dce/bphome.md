---
hide:
  - toc
---

# DCE 5.0 Best Practices Portal

This page summarizes the best practice documents for various modules of DCE 5.0.
These best practices refer to methods and processes that have been widely recognized as
effective and reliable through long-term experience and validation in the use and management
of the DCE 5.0 platform. The content covers aspects such as installation, cluster creation and access,
application management, multi-cloud orchestration, middleware, and more, aiming to help users run
and maintain containerized applications more efficiently and stably.

!!! tip "Someone said:"

    :man_factory_worker: <span style="color: green;">Practice Makes You Perfect.</span>

## Installation and Workbench

<div class="grid cards" markdown>

- :fontawesome-solid-jet-fighter-up:{ .lg .middle } __Installation__

    ---

    Supports both offline and online installation methods, and can be installed on various Linux and K8s distributions

    - [Deploy DCE 5.0 on All-in-One Machine](../install/best-practices/all-in-one-machine.md)
    - [High Availability Solution for Bootstrap Seed Node](../install/best-practices/thinder-ha.md)
    - [Using Host Mode for etcd and Separating Control Plane During Installation](../install/best-practices/etcd-host-deploy.md)
    - [Install on Different Linux Distributions](../install/os-install/uos-v20-install-dce5.0.md)
    - [Install on OpenShift and Alibaba Cloud](../install/k8s-install/ocp-install-dce5.0.md)

- :material-microsoft-azure-devops:{ .lg .middle } __Workbench__

    ---

    A container-based DevOps cloud-native application platform, serving as a unified entry point for creating applications

    - [Implement CI/CD with Pipeline and GitOps](../amamba/quickstart/argocd-jenkins.md)
    - [Code Scanning with Pipeline](../amamba/quickstart/scan-with-pipeline.md)
    - [Integrate Harbor for Image Security Scanning](../amamba/quickstart/scan-with-harbor.md)
    - [Gray Release Practice Based on Contour](../amamba/quickstart/contour-argorollout.md)
    - [Technical Overview of Application Workbench](../amamba/intro/tech-overview.md)

</div>

## Containers

<div class="grid cards" markdown>

- :octicons-container-16:{ .lg .middle } __Container Management Part 1__

    ---

    Building work clusters and nodes based on K8s, which is the core of DCE 5.0

    - [Create Ubuntu Work Cluster on CentOS](../kpanda/best-practice/create-ubuntu-on-centos-platform.md)
    - [Create RedHat 9.2 Work Cluster on CentOS](../kpanda/best-practice/create-redhat9.2-on-centos-platform.md)
    - [Migrate from DCE 4.0 to DCE 5.0](../kpanda/best-practice/dce4-5-migration.md)
    - [Deploy and Upgrade Kubean Backward Compatible Versions](../kpanda/best-practice/kubean-low-version.md)
    - [Use NVIDIA GPU on DCE 5.0](../kpanda/user-guide/gpu/nvidia/index.md)

- :octicons-container-16:{ .lg .middle } __Container Management Part 2__

    ---

    Adopting a native multi-cluster architecture for easy creation and access of K8s clusters

    - [Add Heterogeneous Nodes to Work Clusters](../kpanda/best-practice/multi-arch.md)
    - [Offline Upgrade of Work Clusters](../kpanda/best-practice/update-offline-cluster.md)
    - [Expand Control Nodes of Work Clusters](../kpanda/best-practice/add-master-node.md)
    - [Replace the First Control Node of Work Clusters](../kpanda/best-practice/replace-first-master-node.md)
    - [Expand Worker Nodes of Global Service Clusters](../kpanda/best-practice/add-worker-node-on-global.md)

- :material-warehouse:{ .lg .middle } __Container Registry__

    ---

    Supports multi-instance image hosting services, including Harbor and Docker registries

    - [Choosing the Access Type for Managed Harbor](../kangaroo/best-practice/managed-harbor-select-access-type.md)
    - [Login to Insecure Image Repositories](../kangaroo/best-practice/insecure_registry.md)
    - [Harbor Nginx Configuration Practice](../kangaroo/best-practice/harbor-nginx.md)
    - [Image Repository Capacity Resource Planning](../kangaroo/best-practice/capacity-planning.md)
    - [Deploy Harbor in LB Mode](../kangaroo/best-practice/lb.md)

- :material-dot-net:{ .lg .middle } __Cloud Native Network__

    ---

    Built on multiple open-source technologies, supporting single and multiple CNI network solutions

    - [NIC and Network Planning](../network/plans/ethplan.md)
    - [Performance Test Report](../network/performance/cni-performance.md)
    - [Integrate Spiderpool](../network/modules/spiderpool/index.md)
    - [Integrate Calico](../network/modules/calico/index.md)
    - [Integrate Cilium](../network/modules/cilium/index.md)

- :simple-googlecloudstorage:{ .lg .middle } __Cloud Native Storage__

    ---

    Connecting to storage that meets CSI standards according to different SLA requirements and scenarios

    - [Deploy Rook-ceph via Application Store](../storage/solutions/dce-rook-ceph.md)
    - [Deploy Longhorn via Application Store](../storage/solutions/dce-longhorn.md)
    - [Deploy and Validate OpenEBS via Helm](../storage/solutions/openebs-helm.md)
    - [Integrate and Deploy TiDB](../storage/hwameistor/application/tidb.md)
    - [Deploy Fluid via Helm Template](../storage/solutions/fluid.md)

- :material-cloud-check:{ .lg .middle } __Multicloud Management and Virtual Machine__

    ---

    **Multicloud Management** achieves centralized management of multi-cloud and hybrid cloud.
    **Virtual Machines** is a containerized virtual machine platform built on KubeVirt.

    - [Cross-Cluster Elastic Scaling](../kairship/best-practice/fhpa.md)
    - [One-Click Conversion from DCE 4.0 to DCE 5.0 Multi-Cloud Applications](../kairship/best-practice/one-click-conversion.md)
    - [Import VMware Virtual Machines to DCE 5.0](../virtnest/import/import-ubuntu.md)

</div>

## Microservices

<div class="grid cards" markdown>

- :material-monitor-dashboard:{ .lg .middle } __Insight__

    ---

    Real-time monitoring of applications and resources, collecting various metrics, logs, and event data to analyze application health

    - [Insight Deployment Resource Planning](../insight/quickstart/res-plan/index.md)
    - [What If ElasticSearch Data is Full](../insight/faq/expand-once-es-full.md)
    - [Locate Application Anomalies Using Insight](../insight/best-practice/find_root_cause.md)
    - [Enable Observability for Applications Using OTel](../insight/quickstart/otel/otel.md)
    - [Expose Metrics for Applications Using OTel SDK](../insight/quickstart/otel/meter.md)

- :material-engine:{ .lg .middle } __Microservices Engine__

    ---

    Mainly provides functionalities in two dimensions: microservices governance center and microservices gateway

    - [Experience Microservices Governance with Sample Applications](../skoala/best-practice/use-skoala-01.md)
    - [Use JWT Plugin in Cloud-Native Microservices](../skoala/best-practice/plugins/jwt.md)
    - [Microservices Gateway Accesses Authentication Server](../skoala/best-practice/auth-server.md)
    - [Gateway API Strategy](../skoala/best-practice/gateway02.md)
    - [Access Microservices via Gateway](../skoala/best-practice/gateway01.md)

- :material-table-refresh:{ .lg .middle } __Service Mesh__

    ---

    Built on Istio open-source technology, aimed at next-generation service mesh for cloud-native applications

    - [Service Mesh Vulnerability Fix Standards and Plans](../mspider/intro/sla.md)
    - [Service Mesh Application Access Specification](../mspider/intro/app-spec.md)
    - [Complete Directed Service Access Restriction Using Mesh](../mspider/best-practice/use-egress-and-authorized-policy.md)
    - [Supported Custom Workload Types for Mesh Access](../mspider/best-practice/use-custom-workloads.md)
    - [Precise Control of Multi-Cloud Internet Service Access and Traffic](../mspider/best-practice/multinet-control.md)

</div>

## Data Services and Management

<div class="grid cards" markdown>

- :material-middleware:{ .lg .middle } __Middleware__

    ---

    Use classic middleware to handle data based on actual scenarios

    - [MySQL Cross-Cluster Synchronization Solution](../middleware/mysql/best-practice/crossclusterssync.md)
    - [High Availability Deployment of Redis Single Cluster Across Data Centers](../middleware/redis/best-practice/singleclustercrosszone.md)
    - [ES Migration Practice Based on Hwameistor](../middleware/elasticsearch/user-guide/migrate-es.md)
    - [Kafka Disaster Recovery Solution with Dual Data Center Deployment](../middleware/kafka/bestpractice/kafkain2IDC.md)
    - [High Availability Deployment of RabbitMQ Single Cluster Across Data Centers](../middleware/rocketmq/best-pratice/singleclustercrosszone.md)

- :fontawesome-solid-user-group:{ .lg .middle } __Global Management__

    ---

    User and access control, workspace and hierarchy, audit logs, platform settings, and more

    - [Bind Cross-Cluster Namespace to Workspace (Tenant)](../ghippo/best-practice/ws-to-ns.md)
    - [Allocate Single Cluster to Multiple Workspaces (Tenants)](../ghippo/best-practice/cluster-for-multiws.md)
    - [Architecture Management for Large Enterprises](../ghippo/best-practice/super-group.md)
    - [GProduct Integration with Global Management](../ghippo/best-practice/gproduct/intro.md)
    - [OEM IN and OEM OUT](../ghippo/best-practice/oem/oem-in.md)

- :material-slot-machine:{ .lg .middle } __Intelligent Engine and Cloud Edge Collaboration__

    ---

    **Intelligent Engine** is an integrated platform for training and inference.
    **Cloud Edge Collaboration** extends container capabilities to the edge.

    - [Deploy NFS for Data Preheating](../baize/best-practice/deploy-nfs-in-worker.md)
    - [Update Notebook Built-in Images](../baize/best-practice/change-notebook-image.md)
    - [Checkpoint Mechanism and Usage](../baize/best-practice/checkpoint.md)
    - [Intelligent Device Control](../kant/best-practice/device-control.md)
    - [Develop Device Driver Applications Mapper](../kant/best-practice/develop-device-mapper.md)

</div>

![best practices](../images/bphome.jpeg)
