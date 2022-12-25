---
MTPE: todo
date: 2022-12-23
---
# Features

The list of capabilities for Multicloud orchestration is as follows:

- Unified management plane: Multicloud orchestration has a unified management plane, which manages multiple Multicloud instances, and unified request entry (LCM of Multicloud orchestration instances), while all other requests for Multicloud orchestration can be deployed in the global cluster.
- Multi-instance: Supports the creation of multiple Multicloud instances, and the instances work in isolation without mutual awareness or influence.
- One-click import of clusters: Supports one-click import of clusters from existing managed clusters to Multicloud instances, and real-time synchronization of the latest information of the accessed clusters (deleted at the same time).
- Native API support: Supports all Kubernetes native APIs.
- Multicloud application distribution: Rich Multicloud application distribution strategies, differentiated strategies, etc.
- Application failover: Built-in Multicloud application failover (failover) capability.
- Observability: Rich auditing, indicator measurement, and the ability to improve observability.
- Docking with global management authority: manage user access scope with workspace, and perform authentication operations on users and instances.

## Multicloud instance management

- [Multicloud instance list](../03instance/README.md): View the instance list and support retrieval by instance name

    Supports viewing the list of all Multicloud instances in the current tenant environment and the basic information of the instances, the CPU and memory usage of the instances connected to the cluster, the status of the connected clusters in the instance, etc., and supports viewing version information and instance creation time and instance status.

- Adding a Multicloud instance: Support adding an instance without joining any cluster to create an empty instance, that is, an instance that does not contain any cluster.
- One-click import: After the cluster is created, the cluster that has been connected to the container management can be imported into the Multicloud instance with one click. It supports viewing the resource information of the cluster during access, and supports searching according to the cluster name.
- Removing a Multicloud instance: Automatic verification is performed when removing a Multicloud instance; to ensure data security, the Multicloud instance can only be removed when the current instance does not contain any clusters.

## Example overview

- Basic information: display instance name, status, creation time and version information
- Working cluster information: Display information about the number of working clusters and Node nodes connected to the current instance
- Workload status: display the status information of all currently deployed workloads, and display all created, running, and abnormal quantity information
- Policy information: display all policy information, the number/total number of PropagationPolicy currently in use, and the number/total number of differentiated strategies currently in use
- Resource information: display the resource information created by the current instance, including the number of Multicloud namespaces, the number of Multicloud storage declarations, the number of Multicloud services and routes, the number of Multicloud configurations and keys
- Recent dynamics: display the change information of the latest instance, such as the change information of the lifecycle of the workload, the restart time information of the load, etc.

## Intra-instance cluster management

- list of clusters in the instance

    Cluster list: You can view the information of multiple clusters imported in the current Multicloud instance, the cluster release version and version number, the region information of the Kubernetes cluster, the platform information of the cluster, the IaaS Provider information, the CPU/Mem usage, the network type of the cluster and The record of the container network segment, the joining time of the cluster, and the current status of the cluster.

    The cluster list supports retrieval: fuzzy retrieval of cluster information that has been connected through the name of the cluster.

    Operation of the cluster list: supports quick access to the cluster console interface of container management.

- add cluster

    Supports dynamic (hot-swapping) adding new clusters to the current Multicloud instance, adds a cluster interface for selecting container management, and displays all the clusters to be connected that are currently authorized to access by default, and supports the display of basic information of the cluster, including the cluster name , status, platform, region, availability zone, Kubernetes version, etc.

- remove cluster

    Supports dynamic (hot swap) removal of clusters from the current Multicloud instance.

    Removal verification: Supports verification of cluster resources, informs users that multiple workloads, namespaces, storage declarations, configurations, and keys in the cluster need to be removed in advance, and prompts the risk of removal.

- Use Kubectl to manage instance resources

    Supports obtaining kubeconfig link information, and users can manage Multicloud instances on local terminals.

    Supports the management of Multicloud instances through the web terminal cloudshell.

## Multicloud workloads

- Stateless workload (Deployment)

    Supports displaying the list of Multicloud workloads, supports the query capability of Multicloud workloads, and can view the cluster information deployed by the corresponding Multicloud workloads.

- Create Multicloud stateless workloads

    Image creation: interface-based creation of stateless workloads, adding differentiated configurations, distribution strategies, and other differentiated configurations.

    Differential settings: Support differential configuration when creating loads, support cluster-based differential configuration cluster deployment Pod number/CPU/memory/upgrade strategy, differential configuration cluster mirroring, PropagationPolicy, container script, container storage, container Logs, scheduling policies, tags and annotations, etc.

    Create with YAML: Users create workloads through YAML.

    YAML syntax verification: Supports syntax verification of YAML entered by users, and prompts for incorrect syntax.

    Create with YAML support: The creation of Multicloud workloads, including differentiated configurations, can be done through YAML.

- Multicloud workload details

    Basic information: Supports viewing the deployment details of stateless workloads, the number of Pods, and active cluster information. Resource load provides single Pod monitoring and viewing capabilities, and can jump to Insight Pod log information to provide single Pod log viewing capabilities.

    Deployment information: View the deployment details of stateless workloads, and support operations such as restart/pause/resume/release of Multicloud workloads.

    Instance list: Supports displaying the Pod information of workloads in multiple Kubernetes clusters in a cluster manner, supports one-click quick jump to the workload details interface of the corresponding cluster, and checks the monitoring and log information of the corresponding Pod.

    Service list: Supports splitting the workload service information in the cluster according to the cluster method, supports one-click quick jump to the workload details interface of the corresponding cluster, and checks the monitoring and log information of the corresponding service.

- Edit Multicloud workloads

    Page editing: support editing clusters through pages

    YAML editing: support changing the configuration information of Multicloud workloads through YAML

- Delete Multicloud workloads

    Page deletion: supports deletion of Multicloud workloads through pages, and deletes deployments in multi-clusters at the same time

    Support cloudshell and terminal for deletion: support for terminal deletion

    Deletion prompt: Reminder that a second confirmation is required when deleting

## Resource management

- Multicloud namespace

    Multicloud namespace management: support viewing the list of Multicloud namespace resources

    View the list of Multicloud namespaces: Provide a list to view the namespace information of multi-clusters

    Create Multicloud namespaces: provide the ability to create Multicloud namespaces through interfaces

    Delete Multicloud namespace: support for deleting idle Multicloud namespaces

- Multicloud storage statement

    View the list of Multicloud storage declarations: support viewing the list of created Multicloud PVC resources

    Create Multicloud storage declarations: provide multiple ways to create storage declarations through interface and YAML

    Delete Multicloud storage claim: support for deleting free storage claims

- Multicloud configuration management

    Multicloud ConfigMap management: support viewing Multicloud ConfigMap resource list

    Multicloud secret key management: support viewing the list of Multicloud Secret resources

    Create Multicloud configuration or Multicloud key: support the creation of Multicloud configuration or Multicloud key through interface or YAML, and display them uniformly on the user interface

    Deleting Multicloud configurations or Multicloud keys: Supports deletion of idle Multicloud configurations or Multicloud keys. Deletion of in-use configurations or keys is not allowed

- Network management

    Service list: support viewing Multicloud Service list

    Create services and routes: support the creation of services through interface or YAML, and display them uniformly on the user interface

    Delete service and route: support delete operation on Service, and give corresponding delete prompts for those in use

## Strategy Center

- PropagationPolicy

    PropagationPolicy list: support viewing the PropagationPolicy list of the current instance and its associated Multicloud resources on the interface

    Create PropagationPolicy: support creating and editing PropagationPolicy information in YAML

    Delete PropagationPolicy: only provide a delete button for idle PropagationPolicy

- OverridePolicy

    List of OverridePolicy: support viewing the PropagationPolicy list of the current instance and its associated Multicloud resources on the interface

    Create OverridePolicy: support creating and editing OverridePolicy information in YAML

    Delete OverridePolicy: support viewing the OverridePolicy list of the current instance and the Multicloud resources associated with the current OverridePolicy on the interface
