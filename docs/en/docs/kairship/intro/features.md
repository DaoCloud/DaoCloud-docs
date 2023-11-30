# Features

Multicloud Management module has the following features:

- Unified Management Interface: a unified interface for managing multiple multicloud instances.
- Multiple Instances: create multiple multicloud instances that work in isolation and do not affect each other.
- One-click integration of clusters: add existing clusters from Container Management module into a multicloud instance, sync the latest cluster information at real time.
- Native APIs: Supports all Kubernetes native APIs.
- Multicloud Application Deployment: flexible deployment policies and override policies for multicloud applications.
- Application Failover: Built-in capability to enable application failover across multiple clouds.
- One-Click Application Conversion: Achieve seamless conversion of applications from DCE4 to DCE5 with just one click.
- Cross-Cluster Elastic Scaling: Dynamically adjust resources across different clusters based on application workload demands.
- Observability: Rich audit rules and metrics to improve observability.
- Practical Permissions: Manage user access based on [workspaces](../../ghippo/user-guide/workspace/workspace.md).

## Multicloud Instances

- Add multicloud instances: you can create an empty multicloud instance, and add clusters later as needed.

- Check the instance list and search by instance name.

    You can view all multicloud instances visible to the current user accnout, including CPU and memory usage, cluster status, versions, creation time, etc.

- Safe Delete: multicloud instances cannot be deleted when there are still some clusters in it. This is to avoid unintentional delete and ensure data security.

## Cluster Management

- Add Cluster

    After a multicloud instance is created, you can dynamically (no need to restart) add clusters into it and manage other resources across these clsuters. Adding a clsuter is quite easy. Just select your expected clusters from the list and then click "OK".

- View Clusters

    You can view all clusters added into a multicloud instance, and further check the details of these clusters, including providers, versions, regions, CPU/Memory usage, service IP range, status, etc.

- Remove Cluster

    You can dynamically remove a cluster from the current multicloud instance.

    Removal Verification: to ensure data security, a cluster cannot be removed when there are still resources (deployments, namespaces, secrets, etc.) deploiyed in this cluster under the current multicloud instance.

- kubectl CLI

    You can use kubectl commands in the cloud shell to get the `kubeconfig` information so that users can manage the multicloud instance locally.

## Multicloud Workloads

- Create Multicloud Deployment

    - Image Creation: Create a deployment through a graphical interface and set deployment or override policies.
    - Override Settings: Support override configurations when creating workloads, allowing for cluster-specific configuration such as pod count, CPU, memory, and upgrade strategy. Enable override configurations for cluster-specific settings including image, deployment policy, container scripts, container storage, container logs, scheduling policy, labels, and annotations.
    - Create by YAML: Create a workload quickly with YAML files.
    - YAML Syntax Check: Check the syntax of these YAML files and provides prompts for incorrect syntax.

- Multi-Cloud Workload Details

    - Basic Information: Support viewing deployment details of stateless workloads, including pod count and active cluster information. Provide monitoring capabilities for individual pods, allowing users to navigate to Insight Pod logs and view logs for individual pods.
    - Deployment Information: View deployment details of stateless workloads and perform operations such as restart, pause, resume, and release for multi-cloud workloads.
    - Instance List: Display pod information of workloads across multiple Kubernetes clusters in a cluster-specific manner. Enable quick navigation to the corresponding cluster's workload details page and view monitoring and log information for the corresponding pods.
    - Service List: Segment workload service information within clusters and provide quick navigation to the corresponding cluster's workload details page. View monitoring and log information for the corresponding services.

- Update Multicloud Workload

    - Visualized Update: edit the workload through the graphical interface.
    - YAML Update: change configuration of the multicloud workload by editing its YAML file.

- Delete Multicloud Workload

    - Visualized Deletion: delete multicloud workloads as well as resources therein through the graphical interface.
    - You can also delete it in cloudshell and terminals.
    - Deletion Prompt: Remind users to perform a secondary confirmation before proceeding with the deletion.

## Resource Management

- Multi-Cloud Namespace

    - Manage Multi-Cloud Namespaces: Support viewing the resource list of multi-cloud namespaces.
    - View Multi-Cloud Namespace List: Provide a list to view namespace information across multiple clusters.
    - Create Multi-Cloud Namespace: Enable the creation of multi-cloud namespaces through a user-friendly interface.
    - Delete Multi-Cloud Namespace: Support the deletion of idle multi-cloud namespaces.

- Multi-Cloud Secrets

    - View Multi-Cloud Persistent Volume Claim (PVC) List: Support viewing the created list of multi-cloud PVC resources.
    - Create Multi-Cloud Persistent Volume Claim: Provide multiple options, including user-friendly interface and YAML, for creating storage declarations.
    - Delete Multi-Cloud Persistent Volume Claim: Support the deletion of idle storage declarations.

- Multi-Cloud Configurations

    - Manage Multi-Cloud Configurations: Support viewing the resource list of multi-cloud ConfigMaps.
    - Manage Multi-Cloud Secrets: Support viewing the resource list of multi-cloud Secrets.
    - Create Multi-Cloud Configurations or Secrets: Enable the creation of multi-cloud configurations or secrets through a user-friendly interface or YAML, with unified display in the user interface.
    - Delete Multi-Cloud Configurations or Secrets: Support the deletion of idle multi-cloud configurations or secrets. Deletion is not allowed for configurations or secrets that are currently in use.

- Multi-Cloud Services and Routes

    - Create Services and Routes: Support the creation of services through a user-friendly interface or YAML, with unified display in the user interface.
    - Delete Services and Routes: Support the deletion of services/ingresses, with corresponding prompts for those currently in use.

## Policy Management

- Deployment Policies

    - Deployment Policy List: View the list of deployment policies associated with the current instances and their associated multi-cloud resources.
    - Create Deployment Policy: Maintain and edit deployment policy information using YAML.
    - Delete Deployment Policy: Delete idle deployment policies.

- Override Policies

    - Override Policy List: View the list of Override policies associated with the current instances and their associated multi-cloud resources.
    - Create Override Policy: Maintain and edit Override policy information using YAML.
    - Delete Override Policy: View the list of Override policies associated with the current instances and their associated multi-cloud resources.

## System Settings

- Cluster Health Check Scheduling

    Configure the duration for marking the cluster health status as successful or failed.

- Failover

    Configure parameters to automatically migrate pod replicas from a failed cluster to other available clusters, ensuring service stability.

- Scheduled Rescheduling

    Regularly check the status of pods in the cluster. If a pod remains unschedulable for a specified period, it will be automatically evicted to avoid resource waste.

- Elastic Scaling

    Install karmada-metrics-adapter in the instance control plane cluster to provide metrics API. This feature is disabled by default.
