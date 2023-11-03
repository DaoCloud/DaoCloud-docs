# Features Provided by Container Management

This page lists the main features of container management.

## Cluster Lifecycle Management

- Unified Management of Clusters: Support for any Kubernetes cluster within a specific version range to be included in the scope of container management, and to realize unified management of on-cloud, off-cloud, multicloud, and hybrid cloud container cloud platforms.
- Quick Creation of Clusters:
    - Based on DaoCloud's independent open-source project [Kubean](https://github.com/kubean-io/kubean), it supports the rapid deployment of enterprise-level Kubernetes clusters through the Web UI interface, quickly builds enterprise-level container platforms, and adapts to physical machines and the underlying environment of the virtual machine.
    - Supports access/creation of clusters to help users build a one-stop infrastructure management platform.
    - Supports specifying the runtime type when creating a cluster, and supports multiple runtimes such as contained and Docker.
- One-Click Cluster Upgrade: One-click upgrade of the Kubernetes version of the self-built container cloud platform, and unified management of system component upgrades.
- High Availability of Clusters: Built-in cluster disaster recovery and backup capabilities to ensure that the business system can be restored in the event of host failure, computer room interruption, natural disasters, etc., to improve the stability of the production environment, and reduce the risk of business interruption.
- Certificate Hot Update: Supports one-click hot update of Kubernetes certificates on the web interface.
- Node Management: Support for self-built clusters to add and delete nodes to ensure that the cluster can meet business needs.

## Cloud-Native Application Load

- Full Application Lifecycle Management: Support for Kubernetes-native workload type deployment and management capabilities, including full lifecycle management such as creation, configuration, monitoring, capacity expansion, upgrade, rollback, and deletion.
- One-Stop Application Load Creation: Decouple the underlying Kubernetes platform, and create, operate, and maintain business workloads in one stop.
- Cross-Cluster Application Load Management: Unified management of cross-cluster loads and efficient retrieval capabilities.
- Scaling and Shrinking of Application Load: Through the interface, manual/automatic scaling of application load can be realized, and the expansion and shrinking strategy can be customized to cope with traffic peaks.
- Container Lifecycle Settings: Support for setting callback features, parameters after startup, and parameters before stopping when creating workloads to meet the needs of specific cases.
- Container Readiness Check and Survival Check Settings: Support for setting workload readiness check and survival check when deploying applications:
    - Workload readiness check: Used to detect whether the user's business is ready. If it is not ready, the traffic will not be forwarded to the current instance.
    - Workload survival check: The user checks whether the container is normal. If it is abnormal, the cluster will run the container restart operation.
- Container Environment Variable Settings: Specify environment variables for business container runtime environment settings.
- Automatic Scheduling of Containers: Support for application service scheduling management, automatically schedule containers according to host resource usage, specify specific deployment hosts, and schedule containers through label policies.
- Affinity and Anti-Affinity: Supports the definition of affinity and anti-affinity for scheduling between pods; and affinity and anti-affinity between pods and nodes to meet business custom scheduling requirements.
- Container Security User Setting: Support for setting the container running user. If running with Root privileges, fill in the Root user ID 0.
- Custom Resource (CRD) Support: Supports full lifecycle management such as creation, configuration, and deletion of custom resources.

## Service and Routing

Service (Service) is a Kubernetes-native resource that provides cloud native load balancing capabilities and is accessed through a fixed IP address and port. Currently supported Service types include:

- Intra-Cluster Access (ClusterIP): Access services only within the cluster.
- Node Access (NodePort): Use node IP + service port to access.

## Namespace Management

- Namespace Management: Supports namespace creation, quota setting, resource limit setting, etc.
- Cross-Cluster Namespace Management: Supports unified management of cross-cluster namespaces and efficient retrieval capabilities, and realizes namespace management capabilities in multicloud cases and disaster recovery use cases.

## Container Storage

- Data Volume Management: Supports local storage, file storage, and block storage, accessed through CSI capabilities, and provided for application workloads.
- Dynamic Creation of Data Volumes: Supports StorageClass to dynamically create data volumes.

## Policy Management

- Unified Management and Distribution of Policies: Support for the formulation of network policies, quota policies, resource limit policies, disaster recovery policies, security policies, and other policies at the granularity of namespaces or clusters, and support for policy delivery at the granularity of clusters/namespaces.
- Network Policy: Supports the formulation of network policies at the granularity of namespace or cluster and limits the communication rules between pods and network "entities" on the network plane.
- Quota Policy: Supports setting quota policies at namespace or cluster granularity tolimit the resource usage of namespaces in the cluster.
- Resource Limit Policy: Supports setting resource limit policies at namespace or cluster granularity and constrains resource usage limits for applications in corresponding namespaces.
- Disaster Recovery Strategy: Supports disaster recovery strategy setting at the granularity of namespace or cluster, realizes disaster recovery backup with namespace as the dimension, and ensures the security of the cluster.
- Security Policy: Supports setting security policies at namespace or cluster granularity and defines different isolation levels for Pods.

## Extensions

Provides a wealth of system plugins to expand the features of cloud container clusters. Extension plugins include DNS, HPA, etc.

## Authority Management

Supports [Namespace Authorization](../user-guide/permissions/cluster-ns-auth.md). Through permission settings, different users or groups can have permission to operate different Kubernetes resources under the specified namespace.

## Cluster Operation and Maintenance

- All-Round Cluster Monitoring: Comprehensive coverage of cluster and node metric monitoring and alerts, real-time understanding and viewing of cluster and node status, and timely implementation of operation and maintenance measures to ensure business continuity.
- openAPI: Provides native Kubernetes OpenAPI capabilities.
- [CloudShell](../../community/cloudtty.md) Access to the Cluster: Supports connecting to the cluster through CloudShell and accessing the cluster through Kubectl.

See [Container Management Feature Release Updates](./news.md).
