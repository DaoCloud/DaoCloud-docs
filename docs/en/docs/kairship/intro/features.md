# Function overview

The list of capabilities for multi-cloud orchestration is as follows:

- Unified management plane: Multi-cloud orchestration has a unified management plane, which manages multiple multi-cloud instances, and unified request entry (LCM of multi-cloud orchestration instances), while all other requests for multi-cloud orchestration can be deployed in the global cluster.
- Multi-instance: Supports the creation of multiple multi-cloud instances, and the instances work in isolation without mutual awareness or influence.
- One-click import of clusters: Supports one-click import of clusters from existing managed clusters to multi-cloud instances, and real-time synchronization of the latest information of the accessed clusters (deleted at the same time).
- Native API support: Supports all Kubernetes native APIs.
- Multi-cloud application distribution: Rich multi-cloud application distribution strategies, differentiated strategies, etc.
- Application failover: Built-in multi-cloud application failover (failover) capability.
- Observability: Rich auditing, indicator measurement, and the ability to improve observability.
- Docking with global management authority: manage user access scope with workspace, and perform authentication operations on users and instances.

## Multi-cloud instance management

- [Multi-cloud instance list](../instance/README.md): View the instance list and support retrieval by instance name

     Supports viewing the list of all multi-cloud instances in the current tenant environment and the basic information of the instances, the CPU and memory usage of the instances connected to the cluster, the status of the connected clusters in the instance, etc., and supports viewing version information and instance creation time and instance status.

- Adding a multi-cloud instance: Support adding an instance without joining any cluster to create an empty instance, that is, an instance that does not contain any cluster.
- One-click import: After the cluster is created, the cluster that has been connected to the container management can be imported into the multi-cloud instance with one click. It supports viewing the resource information of the cluster during access, and supports searching according to the cluster name.
- Removing a multi-cloud instance: Automatic verification is performed when removing a multi-cloud instance; to ensure data security, the multi-cloud instance can only be removed when the current instance does not contain any clusters.

## Example overview

- Basic information: display instance name, status, creation time and version information
- Working cluster information: Display information about the number of working clusters and Node nodes connected to the current instance
- Workload status: display the status information of all currently deployed workloads, and display all created, running, and abnormal quantity information
- Policy information: display all policy information, the number/total number of deployment strategies currently in use, and the number/total number of differentiated strategies currently in use
- Resource information: display the resource information created by the current instance, including the number of multi-cloud namespaces, the number of multi-cloud storage declarations, the number of multi-cloud services and routes, the number of multi-cloud configurations and keys
- Recent dynamics: display the change information of the latest instance, such as the change information of the life cycle of the workload, the restart time information of the load, etc.

## Intra-instance cluster management

- list of clusters in the instance

     Cluster list: You can view the information of multiple clusters imported in the current multi-cloud instance, the cluster release version and version number, the region information of the Kubernetes cluster, the platform information of the cluster, the IaaS Provider information, the CPU/Mem usage, the network type of the cluster and The record of the container network segment, the joining time of the cluster, and the current status of the cluster.

     The cluster list supports retrieval: fuzzy retrieval of cluster information that has been connected through the name of the cluster.

     Operation of the cluster list: supports quick access to the cluster console interface of container management.

- add cluster

     Supports dynamic (hot-swapping) adding new clusters to the current multi-cloud instance, adds a cluster interface for selecting container management, and displays all the clusters to be connected that are currently authorized to access by default, and supports the display of basic information of the cluster, including the cluster name , status, platform, region, availability zone, Kubernetes version, etc.

- remove cluster

     Supports dynamic (hot swap) removal of clusters from the current multi-cloud instance.

     Removal verification: Supports verification of cluster resources, informs users that multiple workloads, namespaces, storage declarations, configurations, and keys in the cluster need to be removed in advance, and prompts the risk of removal.

- Use Kubectl to manage instance resources

     Supports obtaining kubeconfig link information, and users can manage multi-cloud instances on local terminals.

     Supports the management of multi-cloud instances through the web terminal cloudshell.

## Multi-cloud workloads

- Stateless workload (Deployment)

     Supports displaying the list of multi-cloud workloads, supports the query capability of multi-cloud workloads, and can view the cluster information deployed by the corresponding multi-cloud workloads.

- Create multi-cloud stateless workloads

     Image creation: interface-based creation of stateless workloads, adding differentiated configurations, distribution strategies, and other differentiated configurations.

     Differential settings: Support differential configuration when creating loads, support cluster-based differential configuration cluster deployment Pod number/CPU/memory/upgrade strategy, differential configuration cluster mirroring, deployment strategy, container script, container storage, container Logs, scheduling policies, tags and annotations, etc.

     YAML Creation: Users create workloads through YAML.

     YAML syntax verification: Supports syntax verification of YAML entered by users, and prompts for incorrect syntax.

     YAML creation support: The creation of multi-cloud workloads, including differentiated configurations, can be done through YAML.

- Multi-cloud workload details

     Basic information: Supports viewing the deployment details of stateless workloads, the number of Pods, and active cluster information. Resource load provides single Pod monitoring and viewing capabilities, and can jump to Insight Pod log information to provide single Pod log viewing capabilities.

     Deployment information: View the deployment details of stateless workloads, and support operations such as restart/pause/resume/release of multi-cloud workloads.

     Instance list: Supports displaying the Pod information of workloads in multiple Kubernetes clusters in a cluster manner, supports one-click quick jump to the workload details interface of the corresponding cluster, and checks the monitoring and log information of the corresponding Pod.

     Service list: Supports splitting the workload service information in the cluster according to the cluster method, supports one-click quick jump to the workload details interface of the corresponding cluster, and checks the monitoring and log information of the corresponding service.

- Edit multi-cloud workloads

     Page editing: support editing clusters through pages

     YAML editing: support changing the configuration information of multi-cloud workloads through YAML

- Delete multi-cloud workloads

     Page deletion: supports deletion of multi-cloud workloads through pages, and deletes deployments in multi-clusters at the same time

     Support cloudshell and terminal for deletion: support for terminal deletion

     Deletion prompt: Reminder that a second confirmation is required when deleting

## Resource management

- Multi-cloud namespace

     Multi-cloud namespace management: support viewing the list of multi-cloud namespace resources

     View the list of multi-cloud namespaces: Provide a list to view the namespace information of multi-clusters

     Create multi-cloud namespaces: provide the ability to create multi-cloud namespaces through interfaces

     Delete multi-cloud namespace: support for deleting idle multi-cloud namespaces

- Multi-cloud storage statement

     View the list of multi-cloud storage declarations: support viewing the list of created multi-cloud PVC resources

     Create multi-cloud storage declarations: provide multiple ways to create storage declarations through interface and YAML

     Delete multi-cloud storage claim: support for deleting free storage claims

- Multi-cloud configuration management

     Multi-cloud configuration item management: support viewing multi-cloud ConfigMap resource list

     Multi-cloud secret key management: support viewing the list of multi-cloud Secret resources

     Create multi-cloud configuration or multi-cloud key: support the creation of multi-cloud configuration or multi-cloud key through interface or YAML, and display them uniformly on the user interface

     Deleting multi-cloud configurations or multi-cloud keys: Supports deletion of idle multi-cloud configurations or multi-cloud keys. Deletion of in-use configurations or keys is not allowed

- Network management

     Service list: support viewing multi-cloud Service list

     Create services and routes: support the creation of services through interface or YAML, and display them uniformly on the user interface

     Delete service and route: support delete operation on Service, and give corresponding delete prompts for those in use

## Strategy Center

- deployment strategy

     Deployment strategy list: support viewing the deployment strategy list of the current instance and its associated multi-cloud resources on the interface

     Create deployment strategy: support creating and editing deployment strategy information in YAML

     Delete deployment strategy: only provide a delete button for idle deployment strategies

- Differentiation strategy

     List of differentiated policies: support viewing the deployment policy list of the current instance and its associated multi-cloud resources on the interface

     Create differentiation strategy: support creating and editing differentiation strategy information in YAML

     Delete differentiation strategy: support viewing the differentiation strategy list of the current instance and the multi-cloud resources associated with the current differentiation strategy on the interface