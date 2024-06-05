---
hide:
  - toc
---

# Container Management

Container management is a containerization management module for cloud native applications
built on Kubernetes. It is the core of DCE 5.0. Based on a native multi-cluster architecture,
it decouples the underlying infrastructure to achieve unified management across multiple clouds and clusters.
This greatly simplifies the process of migrating enterprise applications to the cloud and reduces
operational and manpower costs. With container management, you can easily create Kubernetes clusters
and quickly build an enterprise-grade container cloud management platform.

!!! tip

    Containerization is an essential trend in data center development, as it is
    a natural extension of application encapsulation, deployment, and hosting.

<div class="grid cards" markdown>

- :material-server:{ .lg .middle } __Clusters__

    ---

    DCE 5.0 container management currently supports four types of clusters:
    global service cluster, management cluster, worker cluster, and integrated cluster.

    - [Create a Cluster](../user-guide/clusters/create-cluster.md) or [Integrate a Cluster](../user-guide/clusters/integrate-cluster.md)
    - [Upgrade a Cluster](../user-guide/clusters/upgrade-cluster.md)
    - [Cluster Roles](../user-guide/clusters/cluster-role.md) and [Cluster Status](../user-guide/clusters/cluster-status.md)
    - [Choose a Runtime](../user-guide/clusters/runtime.md)

- :fontawesome-brands-node:{ .lg .middle } __Nodes__

    ---

    Nodes run components such as kubelet, container runtime, and kube-proxy.

    - [Node Scheduling](../user-guide/nodes/schedule.md)
    - [Labels and Annotations](../user-guide/nodes/labels-annotations.md), [Taints Management](../user-guide/nodes/taints.md)
    - Node [Scaling Up](../user-guide/nodes/add-node.md)/[Scaling Down](../user-guide/nodes/delete-node.md)
    - [Node Authentication](../user-guide/nodes/node-authentication.md), [Node Availability Check](../user-guide/nodes/node-check.md)

</div>

<div class="grid cards" markdown>

- :simple-myspace:{ .lg .middle } __Namespaces__

    ---

    Namespaces provide a way to build virtual space to isolate physical resources and only
    affect objects with namespaces.

    - [Create/Delete Namespaces](../user-guide/namespaces/createns.md)
    - [Namespace-exclusive Nodes](../user-guide/namespaces/exclusive.md)
    - [Configure Pod Security Policies for Namespaces](../user-guide/namespaces/podsecurity.md)

- :octicons-tasklist-16:{ .lg .middle } __Workloads__

    ---

    Workloads refer to various types of applications running on DCE 5.0.

    - Create [Deployment](../user-guide/workloads/create-deployment.md) and [StatefulSet](../user-guide/workloads/create-statefulset.md)
    - Create [DaemonSet](../user-guide/workloads/create-daemonset.md)
    - Create [Job](../user-guide/workloads/create-job.md) and [CronJob](../user-guide/workloads/create-cronjob.md)

</div>

<div class="grid cards" markdown>

- :material-expand-all:{ .lg .middle } __Autoscaling__

    ---

    Autoscaling of workloads is achieved by configuring HPA (Horizontal Pod Autoscaler) and VPA (Vertical Pod Autoscaler) policies.

    - Install [metrics-server](../user-guide/scale/install-metrics-server.md), [kubernetes-cronhpa-controller](../user-guide/scale/install-cronhpa.md), and [VPA](../user-guide/scale/install-vpa.md) plugins
    - [Create HPA Policy](../user-guide/scale/create-hpa.md)
    - [Create VPA Policy](../user-guide/scale/create-vpa.md)

- :simple-helm:{ .lg .middle } __Helm Apps__

    ---

    Helm is DCE 5.0's package management tool, providing hundreds of Helm templates for easy application deployment.

    - [Helm Charts](../user-guide/helm/README.md)
    - [Helm Apps](../user-guide/helm/helm-app.md)
    - [Helm Repo](../user-guide/helm/helm-repo.md)

</div>

<div class="grid cards" markdown>

- :material-dot-net:{ .lg .middle } __Container Networking__

    ---

    DCE 5.0 comes with a container network that facilitates external service provision,
    routing rules defined through Ingress, and traffic control based on network policies.

    - [Service](../user-guide/network/create-services.md): ClusterIP, NodePort, LoadBalancer
    - [Ingress](../user-guide/network/create-ingress.md): Path-based, Name-based
    - [Network Policies](../user-guide/network/network-policy.md)

- :material-harddisk:{ .lg .middle } __Container Storage__

    ---

    DCE 5.0 container management follows the containerized storage concept of Kubernetes, supporting native CSI for dynamic volume provisioning, volume snapshots, cloning, and more.

    - [Persistent Volume Claim (PVC)](../user-guide/storage/pvc.md)
    - [Persistent Volume (PV)](../user-guide/storage/pv.md)
    - [StorageClass](../user-guide/storage/sc.md)

</div>

<div class="grid cards" markdown>

- :material-security:{ .lg .middle } __Security Management__

    ---

    DCE 5.0 container management supports three types of scanning at the node and cluster level:

    - [Compliance Scanning](../user-guide/security/cis/config.md)
    - [Permission Scanning](../user-guide/security/audit.md)
    - [Vulnerability Scanning](../user-guide/security/hunter.md)

- :material-key:{ .lg .middle } __Configuration and Secrets__

    ---

    DCE 5.0 container management allows the management of ConfigMaps and Secrets in a key-value format:

    - [ConfigMap](../user-guide/configmaps-secrets/create-configmap.md)
    - [Secrets](../user-guide/configmaps-secrets/create-secret.md)

</div>

<div class="grid cards" markdown>

- :material-card-search:{ .lg .middle } __Cluster Inspection__

    ---

    Cluster inspection enables automatic/manual periodic or on-demand checks of the overall health status of the cluster, giving administrators proactive control over cluster security.

    - [Create Inspection Configuration](../user-guide/inspect/config.md)
    - [Perform Inspection](../user-guide/inspect/inspect.md)
    - [View Inspection Reports](../user-guide/inspect/report.md)

- :material-auto-fix:{ .lg .middle } __Cluster Operations__
    
    ---

    Cluster operations refer to tasks such as viewing cluster actions, upgrading the cluster,
    and managing cluster configurations.

    - [View Recent Operations](../user-guide/clusterops/latest-operations.md)
    - [Cluster Settings](../user-guide/clusterops/cluster-settings.md)
    - [Cluster Upgrade](../user-guide/clusters/upgrade-cluster.md)

</div>

!!! success

    With containerization, you can develop and deploy applications faster and simpler compared to
    building virtual devices. Containerized architecture brings remarkable operational and economic
    benefits, including lower or even free licensing costs, higher utilization of physical resources,
    improved scalability, and increased service reliability.

    Looking ahead, container virtualization will help enterprises make better use of hybrid and
    multi-cloud environments, enabling optimized resource management and application deployment.

[Download DCE 5.0](../../download/index.md){ .md-button .md-button--primary }
[Install DCE 5.0](../../install/index.md){ .md-button .md-button--primary }
[Free Trial Now](../../dce/license0.md){ .md-button .md-button--primary }
