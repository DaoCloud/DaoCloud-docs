# Features Provided by Container Management

The main features of container management are as follows:

| Category | Feature Description |
|----- |-------- |
| Cluster Lifecycle Management | Unified Management of Clusters:<br>&nbsp;&nbsp;- Supports including any Kubernetes cluster within a specific version range in the scope of container management<br>&nbsp;&nbsp;- Achieves unified management of on-cloud, off-cloud, multicloud, and hybrid cloud container platforms |
| | Quick Creation of Clusters:<br>&nbsp;&nbsp;- Based on DaoCloud's independent open-source project [Kubean](https://github.com/kubean-io/kubean)<br>&nbsp;&nbsp;- Supports integrating and creating clusters<br>&nbsp;&nbsp;- Supports specifying the runtime type when creating a cluster |
| | One-Click Cluster Upgrade: One-click upgrade of the Kubernetes version of a self-built container platform, with unified management of system component upgrades. |
| | High Availability of Clusters: Built-in cluster disaster recovery and backup capabilities ensure that business systems can be restored in the event of host failure, computer room interruption, or natural disasters, improving the stability of the production environment and reducing the risk of business interruption. |
| | Node Management: Supports adding and deleting nodes for self-built clusters to ensure that the cluster can meet business needs. |
| Application Load | Full Application Lifecycle Management: Supports Kubernetes-native workload type deployment and management capabilities, including lifecycle management such as creation, configuration, monitoring, scaling, upgrade, rollback, and deletion. |
| | One-Stop Application Load Creation: Decouples the underlying Kubernetes platform, creating and maintaining business workloads in one stop. |
| | Cross-Cluster Application Load Management: Unified management of cross-cluster loads and efficient retrieval capabilities. |
| | Application Load Scaling: Through the interface, manual/automatic scaling of application loads can be achieved, and scaling policies can be customized to handle traffic peaks. |
| | Container Lifecycle Settings: Supports setting callback functions, post-start parameters, and pre-stop parameters when creating workloads to meet the needs of specific scenarios. |
| | Container Readiness Check and Liveness Check Settings:<br>&nbsp;&nbsp;- Workload readiness check: Used to detect whether the user's business is ready. If it is not ready, traffic is not forwarded to the current instance.<br>&nbsp;&nbsp;- Workload liveness check: Used to detect whether the container is normal. If it is abnormal, the cluster performs a container restart operation. |
| | Container Environment Variable Settings: Specifies environment variables for the business container runtime environment. |
| | Automatic Scheduling of Containers: Supports application service scheduling management, automatically schedules containers based on host resource usage, allows specifying a specific deployment host, and supports container scheduling through label policies. |
| | Affinity and Anti-Affinity: Supports defining affinity and anti-affinity for scheduling between Pods, as well as affinity and anti-affinity between Pods and nodes, meeting custom business scheduling requirements. |
| | Container Security User Setting: Supports setting the container running user. If running with Root privileges, enter Root user ID 0. |
| | Custom Resource (CRD) Support: Supports lifecycle management such as creation, configuration, and deletion of custom resources. |
| Service and Routing | Service is a Kubernetes-native resource that provides cloud native load balancing capabilities and is accessed through a fixed IP address and port. The currently supported Service types include: |
| | &nbsp;&nbsp;Intra-Cluster Access (ClusterIP): Access services only within the cluster. |
| | &nbsp;&nbsp;Node Access (NodePort): Access using the node IP + service port. |
| Namespace Management | Namespace Management: Supports namespace creation, quota setting, resource limit setting, and more. |
| | Cross-Cluster Namespace Management: Supports unified management and efficient retrieval of cross-cluster namespaces, enabling namespace management in multicloud and disaster recovery scenarios. |
| Container Storage | Data Volume Management: Supports local storage, file storage, and block storage, which are accessed through CSI capabilities and provided for use by application workloads. |
| | Dynamic Creation of Data Volumes: Supports storage pools to dynamically create data volumes. |
| Policy Management | Unified Policy Management and Distribution: Supports formulating network policies, quota policies, resource limit policies, disaster recovery policies, security policies, and other policies at the granularity of namespaces or clusters, and supports policy distribution at the granularity of clusters/namespaces. |
| | Network Policy: Supports formulating network policies at the granularity of namespaces or clusters, restricting the communication rules between Pods and network "entities" on the network plane. |
| | Quota Policy: Supports setting quota policies at the granularity of namespaces or clusters to limit the resource usage of namespaces in the cluster. |
| | Resource Limit Policy: Supports setting resource limit policies at the granularity of namespaces or clusters to constrain the resource usage limits of applications in the corresponding namespace. |
| | Disaster Recovery Policy: Supports setting disaster recovery policies at the granularity of namespaces or clusters, implementing disaster recovery backup with namespaces as the dimension and ensuring cluster security. |
| | Security Policy: Supports setting security policies at the granularity of namespaces or clusters, defining different isolation levels for Pods. |
| Extensions | Provides a wealth of system plugins to expand the features of cloud container clusters. Extension plugins include DNS, HPA, and more. |
| Authority Management | Supports [Namespace Authorization](../user-guide/permissions/cluster-ns-auth.md). Through permission settings, different users or user groups can have permission to operate different Kubernetes resources under the specified namespace. |
| Cluster Operation and Maintenance | All-Round Cluster Monitoring: Comprehensive coverage of cluster and node metric monitoring and alerts, real-time understanding and viewing of cluster and node status, and timely implementation of operation and maintenance measures to ensure business continuity. |
| | Open API: Provides native Kubernetes OpenAPI capabilities. |
| | [CloudShell](../../community/cloudtty.md) Access to Clusters: Supports connecting to the cluster through CloudShell and accessing the cluster through kubectl. |
| Heterogeneous Acceleration | Supports heterogeneous GPU hardware acceleration for NVIDIA, Iluvatar, Ascend, and more. |
| | Supports computing power, memory, and slicing for a single physical GPU card. Multiple service containers can share a single GPU card, and the GPU computing power and memory quotas occupied by each service container can be limited and isolated. |
| | Supports GPU resource quota management by project. |
