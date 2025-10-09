---
MTPE: windsonsea
date: 2025-10-09
---

# Features

The feature list of **MultiCloud Management** is as follows:

* **Unified Management Plane:** MultiCloud Management provides a unified management plane responsible for managing multiple multicloud instances, serving as the unified request entry point (LCM of MultiCloud Management instances). All other multicloud-related requests can be deployed in the global service cluster.
* **Multiple Instances:** Supports creating multiple multicloud instances, with isolated workloads that do not affect or perceive each other.
* **One-Click Cluster Access:** Supports one-click access for clusters from existing managed clusters into a multicloud instance, and synchronizes the latest cluster information in real-time (clusters are deleted along with the instance).
* **Native API Support:** Supports all native Kubernetes APIs.
* **MultiCloud Application Distribution:** Provides a wide range of distribution and differentiation strategies for multicloud applications.
* **Application Failover:** Built-in failover capability for multicloud applications.
* **One-Click Application Migration:** Enables one-click migration of applications from DCE4 to DCE5.
* **Cross-Cluster Autoscaling:** Dynamically adjusts resources across clusters based on application load requirements.
* **Observability:** Provides rich auditing and metrics capabilities to enhance observability.
* **Integration with Global Access Control:** Manages user access scope via workspaces and performs authentication and authorization for users and instances.

## Detailed Breakdown

| Feature | Description |
| ------- | ----------- |
| **MultiCloud Instance Management** | **Add MultiCloud Instance:** Supports adding instances without any clusters to create empty instances. |
| | **View MultiCloud Instance:** Supports search by instance name and viewing instance list, basic information, CPU and memory usage, status, version, creation time, etc. |
| | **Remove MultiCloud Instance:** Performs validation before removal; only allows removal when the instance contains no clusters. |
| **Cluster Management Within Instances** | **Add Cluster:** Supports dynamically adding new clusters to the current multicloud instance and displaying available clusters that the user has access to. |
| | **View Cluster:** Supports viewing detailed information about the connected clusters, such as name, status, platform, region, availability zone, and Kubernetes version. |
| | **Remove Cluster:** Supports dynamic cluster removal with resource validation and risk warnings. |
| | **Manage Instance Resources via kubectl:** Supports obtaining kubeconfig links and managing multicloud instances through a web terminal. |
| **MultiCloud Workloads** | **Create MultiCloud Stateless Workloads:** Supports graphical creation, differentiated configuration, YAML creation, and syntax validation. |
| | **MultiCloud Workload Details:** View deployment details, resource usage, instance lists, service lists, and supports operations such as restart, pause, and resume. |
| | **Update MultiCloud Workload:** Supports configuration updates through the web UI or YAML editor. |
| | **Delete MultiCloud Workload:** Supports deletion through the UI or CLI with secondary confirmation. |
| **Resource Management** | **MultiCloud Namespace:** Supports viewing, creating, and deleting multicloud namespace resources. |
| | **MultiCloud Configuration Items:** Supports viewing, creating, and deleting multicloud ConfigMap and Secret resources. |
| | **MultiCloud Services and Routing:** Supports creating and deleting Service/Ingress resources. |
| **Policy Management** | **Deployment Policy:** Supports viewing, creating, and deleting deployment policies. |
| | **Differentiation Policy:** Supports viewing, creating, and deleting differentiation policies. |
| **System Settings** | **Cluster Health Check Configuration:** Configure the duration for marking a cluster's health status as successful or failed. |
| | **Failover:** Automatically migrates Pod replicas from failed clusters to other available clusters. |
| | **Scheduled Rescheduling:** Periodically checks Pod status and automatically evicts unschedulable Pods. |
| | **Autoscaling:** Installs `karmada-metrics-adapter` to provide metrics APIs (disabled by default). |
