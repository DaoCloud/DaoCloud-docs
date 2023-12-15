# Features

MultiCloud Management module has the following features:

- **Unified Management Interface**: A unified interface for managing multiple multicloud instances.
- **Multiple Instances**: Create multiple multicloud instances that work in isolation and do not affect each other.
- **One-click Integration of Clusters**: Add existing clusters from Container Management module into a multicloud instance, sync the latest cluster information at real time.
- **Native APIs**: Supports all Kubernetes native APIs.
- **MultiCloud Application Deployment**: Flexible deployment policies and override policies for multicloud applications.
- **Application Failover**: Built-in capability to enable application failover across multiple clouds.
- **One-Click Application Conversion**: Achieve seamless conversion of applications from DCE4 to DCE5 with just one click.
- **Cross-Cluster Elastic Scaling**: Dynamically adjust resources across different clusters based on application workload demands.
- **Observability**: Rich audit rules and metrics to improve observability.
- **Practical Permissions**: Manage user access based on [workspaces](../../ghippo/user-guide/workspace/workspace.md).

## MultiCloud Instances

- **Add MultiCloud Instances**: You can create an empty multicloud instance, and add clusters later as needed.

- **Check the instance list and search by instance name**.

    You can view all multicloud instances visible to the current user account, including CPU and memory usage, cluster status, versions, creation time, etc.

- **Safe Delete**: MultiCloud instances cannot be deleted when there are still some clusters in it. This is to avoid unintentional delete and ensure data security.

## Cluster Management

- **Add Cluster**

    After a multicloud instance is created, you can dynamically (no need to restart) add clusters into it and manage other resources across these clusters. Adding a cluster is quite easy. Just select your expected clusters from the list and then click "OK".

- **View Cluster**

    You can view all clusters added into a multicloud instance, and further check the details of these clusters, including providers, versions, regions, CPU/Memory usage, service IP range, status, etc.

- **Remove Cluster**

    You can dynamically remove a cluster from the current multicloud instance.

    Removal Verification: To ensure data security, a cluster cannot be removed when there are still resources (deployments, namespaces, secrets, etc.) deployed in this cluster under the current multicloud instance.

- **kubectl CLI**

    You can use kubectl commands in the cloud shell to get the `kubeconfig` information so that users can manage the multicloud instance locally.

## MultiCloud Workloads

- **Create MultiCloud Deployment**

    - Image Creation: Create a deployment through a graphical interface and set deployment or override policies.
    - Override Settings: Support override configurations when creating workloads, allowing for cluster-specific configuration such as pod count, CPU, memory, and upgrade strategy. Enable override configurations for cluster-specific settings including image, deployment policy, container scripts, container storage, container logs, scheduling policy, labels, and annotations.
    - Create by YAML: Create a workload quickly with YAML files.
    - YAML Syntax Check: Check the syntax of these YAML files and provides prompts for incorrect syntax.

- **MultiCloud Workload Details**

    - Basic Information: Support viewing deployment details of stateless workloads, including pod count and active cluster information. Provide monitoring capabilities for individual pods, allowing users to navigate to Insight Pod logs and view logs for individual pods.
    - Deployment Information: View deployment details of stateless workloads and perform operations such as restart, pause, resume, and release for multicloud workloads.
    - Instance List: Display pod information of workloads across multiple Kubernetes clusters in a cluster-specific manner. Enable quick navigation to the corresponding cluster's workload details page and view monitoring and log information for the corresponding pods.
    - Service List: Segment workload service information within clusters and provide quick navigation to the corresponding cluster's workload details page. View monitoring and log information for the corresponding services.

- **Update MultiCloud Workload**

    - Visualized Update: Edit the workload through the graphical interface.
    - YAML Update: Change configuration of the multicloud workload by editing its YAML file.

- **Delete MultiCloud Workload**

    - Visualized Deletion: Delete multicloud workloads as well as resources therein through the graphical interface.
    - You can also delete it in cloudshell and terminals.
    - Deletion Confirmation: Remind users to perform a secondary confirmation before proceeding with the deletion.

## Resource Management

- **MultiCloud Namespace**

    - Manage MultiCloud Namespaces: Support viewing the resource list of multicloud namespaces.
    - View MultiCloud Namespace List: Provide a list to view namespace information across multiple clusters.
    - Create MultiCloud Namespace: Enable the creation of multicloud namespaces through a user-friendly interface.
    - Delete MultiCloud Namespace: Support the deletion of idle multicloud namespaces.

- **MultiCloud Secrets**

    - View MultiCloud PVC List: Support viewing the created list of multicloud PVC resources.
    - Create MultiCloud PVC: Provide multiple options, including user-friendly interface and YAML, for creating storage declarations.
    - Delete MultiCloud PVC: Support the deletion of idle storage declarations.

- **MultiCloud ConfigMaps**

    - Manage MultiCloud ConfigMaps: Support viewing the resource list of multicloud configmaps.
    - Manage MultiCloud Secrets: Support viewing the resource list of multicloud Secrets.
    - Create MultiCloud ConfigMaps or Secrets: Enable the creation of multicloud configmaps or secrets through a user-friendly interface or YAML, with unified display in the user interface.
    - Delete MultiCloud ConfigMaps or Secrets: Support the deletion of idle multicloud configmaps or secrets. Deletion is not allowed for configmaps or secrets that are currently in use.

- **MultiCloud Services and Ingress**

    - Create Services and Ingress: Support the creation of services through a user-friendly interface or YAML, with unified display in the user interface.
    - Delete Services and Ingress: Support the deletion of services/ingress, with corresponding prompts for those currently in use.

## Policy Management

- **Propagation Policies**

    - Propagation Policy List: View the list of propagation policies associated with the current instances and their associated multicloud resources.
    - Create Propagation Policy: Maintain and edit propagation policy information using YAML.
    - Delete Propagation Policy: Delete idle propagation policies.

- **Override Policies**

    - Override Policy List: View the list of override policies associated with the current instances and their associated multicloud resources.
    - Create Override Policy: Maintain and edit override policy information using YAML.
    - Delete Override Policy: View the list of override policies associated with the current instances and their associated multicloud resources.

## System Settings

- **Cluster Health Check**

    Configure the duration for marking the cluster health status as successful or failed.

- **Failover**

    Configure parameters to automatically migrate pod replicas from a failed cluster to other available clusters, ensuring service stability.

- **CronReschedule**

    Regularly check the status of pods in the cluster. If a pod remains unschedulable for a specified period, it will be automatically evicted to avoid resource waste.

- **Federated HPA**

    Install karmada-metrics-adapter in the instance control plane cluster to provide metrics API. This feature is disabled by default.
