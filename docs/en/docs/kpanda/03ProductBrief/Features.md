# Function overview

This page lists the main functional features of container management.

## Cluster life cycle management

- Unified management of clusters: Support any Kubernetes cluster within a specific version range to be included in the scope of container management, and realize unified management of on-cloud, off-cloud, multicloud, and hybrid cloud container cloud platforms.

- Quick creation of clusters:

    - Quickly deploy enterprise-level Kubernetes clusters through the web interface, quickly build enterprise-level container platforms, and adapt to the underlying environment of physical machines and virtual machines.

    - Supports access/creation of clusters to help users build a one-stop infrastructure management platform.
    
    - Supports specifying the runtime type when creating a cluster, and supports multiple runtimes such as Contained and Docker.

- One-click cluster upgrade: One-click upgrade of the Kubernetes version of the self-built container cloud platform, and unified management of system component upgrades.

- High availability of clusters: built-in cluster disaster recovery and backup capabilities to ensure that the business system can be restored in the event of host failure, computer room interruption, natural disasters, etc., improve the stability of the production environment, and reduce the risk of business interruption.

- Certificate hot update: Supports one-click hot update of Kubernetes certificates on the web interface.

- Node management: Support self-built clusters to add and delete nodes to ensure that the cluster can meet business needs.

## Cloud Native Application Load

- Full application life cycle management: Support Kubernetes-native workload type deployment and management capabilities, including: creation, configuration, monitoring, expansion, upgrade, rollback, deletion, etc. full life cycle management.

- One-stop application load creation: decouple the underlying Kubernetes platform, and create, operate and maintain business workloads in one stop.

- Cross-cluster application load management: Unified management of cross-cluster loads and efficient retrieval capabilities.

- Scaling and shrinking of application load: Through the interface, the manual/automatic scaling of application load can be realized, and the expansion and shrinking strategy can be customized to cope with traffic peaks.

- Container life cycle settings: support setting callback functions, parameters after startup, and parameters before stopping when creating workloads to meet the needs of specific scenarios.

- Container readiness check and survival check settings: support setting workload readiness check and survival check when deploying applications:

    - Workload readiness check: It is used to detect whether the user business is ready. If it is not ready, the traffic will not be forwarded to the current instance.

    - Workload survival check: The user checks whether the container is normal. If it is abnormal, the cluster will execute the container restart operation.

- Container environment variable settings: specify environment variables for business container runtime environment settings.

- Automatic scheduling of containers: Support application service scheduling management, automatically schedule containers according to host resource usage, specify specific deployment hosts, and schedule containers through label policies.

- Affinity and anti-affinity: Supports the definition of affinity and anti-affinity for scheduling between container groups; and affinity and anti-affinity between container groups and nodes to meet business custom scheduling requirements.

- Container security user setting: support setting the container running user, if running with Root privileges, fill in the Root user ID 0.

- Custom resource (CRD) support: Supports full life cycle management such as creation, configuration, and deletion of custom resources.

## Service and Routing

Service (Service) is a Kuberetes-native resource that provides cloud-native load balancing capabilities and is accessed through a fixed IP address and port. Currently supported Service types include:

- Intra-cluster access (ClusterIP): Access services only within the cluster.

- Node access (NodePort): Use node IP for access.

## Namespace management

- Namespace management: supports namespace creation, quota setting, resource limit setting, etc.

- Cross-cluster namespace management: supports unified management of cross-cluster namespaces and efficient retrieval capabilities, and realizes namespace management capabilities in multicloud scenarios and disaster recovery scenarios.

## Container storage

- Data volume management: supports local storage, file storage, and block storage access through CSI capabilities, and provides them for application workloads.

- Dynamic creation of data volumes: Supports storage pools to dynamically create data volumes.

## Policy management

- Unified management and distribution of policies: support the formulation of network policies, quota policies, resource limit policies, disaster recovery policies, security policies and other policies at the granularity of namespaces or clusters, and support policy delivery at the granularity of clusters/namespaces.

- Network policy: Supports the formulation of network policies at the granularity of namespace or cluster, and limits the communication rules between container groups and network "entities" on the network plane.

- Quota policy: Supports setting quota policies at namespace or cluster granularity to limit the resource usage of namespaces in the cluster.

- Resource limit policy: Supports setting resource limit policies at namespace or cluster granularity, and constrains resource usage limits for applications in corresponding namespaces.

- Disaster recovery strategy: Support disaster recovery strategy setting at the granularity of namespace or cluster, realize disaster recovery backup with namespace as the dimension, and ensure the security of the cluster.

- Security policy: Supports setting security policies at namespace or cluster granularity, and defines different isolation levels for Pods.

## Extensions

Provides a wealth of system plug-ins to expand the functions of cloud container clusters. Extension plug-ins include: DNS, HPA, etc.

## Authority management

Support [Namespace Authorization](../07UserGuide/Permissions/Cluster-NSAuth.md), through permission settings, different users or user groups can have permission to operate different Kubernetes resources under the specified namespace.

## Cluster operation and maintenance

- All-round cluster monitoring: comprehensive coverage of cluster and node indicator monitoring and alarms, real-time understanding and viewing of cluster and node status, and timely implementation of operation and maintenance measures to ensure business continuity.

- Open API: Provides native Kubernetes OpenAPI capabilities.

- [CloudShell](../../community/cloudtty.md) access to the cluster: supports connecting to the cluster through CloudShell and accessing the cluster through Kubectl.