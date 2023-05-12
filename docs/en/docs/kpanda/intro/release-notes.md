# Container Management Release Notes

This page lists the container-managed Release Notes to help you understand the evolution path and feature changes from release to release.

## 2023-04-28

### v0.17.0

#### Features

- **Added** Download  the patrol report
- **Added** View ETCD Backup Low
- **Added** Creating a cluster supports enabling Flannel, Kube-ovn network plug-ins
- **Added** Create a cluster Enable Cilium dual-stack networking
- **Added** Creating a cluster supports automatic recognition of the node OS type
- **Added** Services of type Headless, External
- **Added** Upgrading the kubernetes version of a working cluster in an offline environment
- **Added** Cluster-level resource backup
- **Added** Create a workload with a private key
- **Added** Configure default resource limits for Helm job
- **Added** Create a PVC using hwameistor

#### Optimize

- **Optimized** Apply Backup Cluster State
- **Optimized** Mismatch between the load state in the load detail and the state of the pod under the load
- **Optimized** Node check interface in offline mode
- **Optimized** Presentation of multi-cloud applications

#### Fix

- **Fixed** Update helm application configuration missing issue
- **Fixed** Using yaml to create multiple types of resources due to the problem of ns inconsistency leading to creation failure
- **Fixed** Failed to select Docker 19.03 runtime using the Kirin operating system
- **Fixed** Incorrect translation of English interface

## 2023-04-04

### v0.16.0

#### Features

- **Added** Use the interface to query PVC events.
- **Added** Creating a task supports the configuration of parameters such as backofflimit, completions, parallelism, and activeDeadlineSeconds.
- **Added** Integrate the self-developed open source storage component Hwameistor, and support `container storage` the view of local storage resource overview and other information in the module.
- **Added** Cluster patrol function is added, which supports second-level patrol (Alpha) of the cluster.
- **Added** Application backup function is added to support quick application backup and recovery (Alpha).
- **Added** Platform backup function is added to support backup and recovery (Alpha) of ETCD data.
- **Added** Support for Ghippo’s custom role management cluster.

#### Optimize

- **Optimized** Kpanda uninstalls the self-built cluster process to prevent the cluster from being deleted due to user misoperation.
- **Optimized** The user experience of recreating the cluster after the failure of the interface to create the cluster, which supports the user to quickly reinstall the cluster based on the configuration before the failure.
- **Optimized** Optimized processing logic when multiple Quota resources exist under one namespace. Multiple Quotas are aggregated
- **Optimized** The information display of the service access mode in the workload details supports the rapid access to the load service.
- **Optimized** Optimize the refresh mechanism of helm repo, and do not enable automatic refresh by default

#### Fix

- **Fixed** Loadblance address unreachable problem.
- **Fixed** Failed to perform an unmount cluster operation.
- **Fixed** The cluster cannot be acquired due to more than 64 characters connected to the cluster.
- **Fixed** Fixed an issue where the offline environment cluster could not display the cluster plug-in.
- **Fixed** Global cluster failed to update the configuration.
- **Fixed** When creating a cluster, the first node check fails and the node check cannot be performed again.
- **Fixed** Environment variables for creating/updating workloads do not take effect.

## 2023-02-27

### v0.15

#### Features

- **Added** Productization support for PVs (Persistent Volumes), which supports the selection of existing data volumes when creating PVCs.
- **Added** Ability to create clusters using kubernetes networkless CNI.
- **Added** Support the Chinese names of resources such as load, configuration, and service.
- **Added** Creating a workload via YAML supports the simultaneous creation of multiple types of resources.
- **Added** The ability to pause and start workloads.

#### Optimize

- **Optimized** Cluster details page, experience of cluster switching.
- **Optimized** Workload status display, add `Stopped` status.
- **Optimized** The workload increases the manual scaling window to simplify the user’s manual scaling process.
- **Optimized** The access cluster cannot access the DCE 4.X cluster.

#### Fix

- **Fixed** Fixed an issue where DNS configuration forced users to fill in upstream DNS when creating a cluster.
- **Fixed** Fixed an issue where the workload version records were sorted out of order.
- **Fixed** Kubean upgrade via Helm does not work.
- **Fixed** The problem that the last exception prompt does not disappear after the creation of the cluster execution node fails to check again.
- **Fixed** Workload creation, mirror pull failure issues.
- **Fixed** Timed backup strategy, unable to perform `Run now` operations.
- **Fixed** When modifying a workload without resource constraints, the UI automatically adds resource constraint issues.
- **Fixed** The problem of failing to `workspace` add a namespace when `workspace` no user is bound to it.
- **Fixed** Fixed an issue where binding and unbinding namespaces would cause namespace annotations to disappear.
- **Fixed** Fix the issue where the create cluster usage `kube-vip` policy does not take effect.
- **Fixed** When the create cluster is set `ntp servers` to empty, the host is cleared of existing `ntp` address issues.

## 2022-12-29

### v0.14

#### Features

- **Added** Helm chart supports the display of Chinese names and template suppliers.
- **Added** CronHPA, which supports timed scaling workloads.
- **Added** VPA (Vertical Scaling) supports manual/automatic modification of resource request values to achieve vertical workload scaling.
- **Added** Namespace has exclusive hosting capabilities.
- **Added** Storage Pools (StrogeClass) support exclusive or shared entitlement to specific namespaces.
- **Added** The Create Workload support exposes the remaining resource quota for the current namespace.
- **Added** Node connectivity check function.
- **Added** Added Mirror Selector to support the selection of mirrors within the Container registry when creating workloads.
- **Added** Apply backup and recovery features.

#### Optimize

- **Optimized** In the process of cluster uninstallation, the cluster deletion protection switch is added.
- **Optimized** Supports simultaneous creation of multiple resources when creating resources via YAML.
- **Optimized** The workload increases the manual scaling window to simplify the user’s manual scaling process.
- **Optimized** Service access mode experience, support service quick access and display node, load balancing address.
- **Optimized** File upload and download support the selection of a specific container.
- **Optimized** Support offline installation of different OS systems.
- **Optimized** Create a cluster in an offline environment-Node configuration supports the selection of node operating systems and the modification of offline Yum sources.
- **Optimized** The YAML editor does not fill in the Namespace field and supports autocomplete as Default.
- **Optimized** Cluster upgrade interface interaction experience.
- **Optimized** When Helm is used to create an application, Namespace is provided to quickly create an entry.

#### Fix

- **Fixed** Problem with not being able to add new nodes with password.
- **Fixed** Error in obtaining cluster kubeconfig accessed in Token mode.
- **Fixed** Cannot get full users and user groups when granting permissions.
- **Fixed** There is a problem unbinding the workspace original permissions when the Bindingsync component is abnormal
- **Fixed** Workspace Resync does not properly remove unwanted permissions.
- **Fixed** Delete the question in which the Namespace can also be selected.
- **Fixed** Create a key. Key data is displayed in a single line.

## 2022-11-29

### v0.13

#### Features

- **Added** Replicatsets productization:
    - Replicatsets can be managed using the WEB terminal (CloudTTY).
    - Support for viewing Replicatsets monitoring, logs, Yaml, events, and containers.
    - Support for viewing Replicatsets details.
    - Linkage ** App Workbench **, the full life cycle of Replicatsets is managed by grayscale publishing.
- **Added** Pod details page.
- **Added** Namespace details page.
- **Added** Use the WEB terminal to upload files to the container and download files from the Pod to the local.
- **Added** The workload scales elastically based on the user-defined index, which is closer to the user’s actual business elastic expansion and contraction requirements.

#### Optimize

- **Optimized** Deploy cluster support:
    - Deploy a cluster using the cilium CNI.
    - Create a cluster with nodes with different usernames, passwords, and SSH ports.
- **Optimized** The Pod list supports viewing the total number of pods and the number in operation, as well as viewing the container type.
- **Optimized** The workload increases the manual scaling window to simplify the user’s manual scaling process.
- **Optimized** The container log supports viewing init container and ephemeral container, providing a more friendly operation and maintenance experience.
- **Optimized** Node details. Note that the vaule value does not correctly display the problem.
- **Optimized** Operation prompt feedback, giving the user correct feedback on the operation.

#### Fix

- **Fixed** Failure to create a namespace due to strong coupling between the namespace creation and the binding workspace.
- **Fixed** The routing rule update failed to modify the path prefix issue for the forwarding policy.
- **Fixed** Creating a workload interface while creating Services does not work.
- **Fixed** Update service exception error reporting issue.
- **Fixed** Unable to access the AWS cluster.
- **Fixed** The user list is not synchronized after using the WS Admin user to bind the resource group.
- **Fixed** On the configuration details page, when Page Size = 50, the List ClusterConfigMaps interface reports an exception.

## 2022-10-28

### v0.10

#### Features

- **Added** NetworkPolicy policy management functions, including the creation, update, and deletion of NetworkPolicy policies, as well as the display of NetworkPolicy policy details, to help users configure network traffic policies for the Pod
- **Added** Workload supports multi-network card configuration and supports IP Pool display to meet the user’s requirement of configuring multiple network cards separately for workload configuration
- **Added** Support to view the operation log of the creation process after the failure of cluster creation, to help users quickly locate the fault
- **Added** Stateful workloads support the use of dynamic data volume templates
- **Added** Create cluster, create Secret, create Ingress, edit the information verification of namespace quota, help guide the user to input the correct configuration parameters, and reduce the user’s failure experience of creating tasks

#### Optimize

- **Optimized** The cluster drop-down list supports the display of cluster status, and optimizes the user’s experience of selecting the managed cluster when creating a cluster, selecting the target cluster when creating a namespace, and selecting the target cluster when authorizing a cluster
- **Optimized** Install the insight-agent plug-in in the helm application to support the automatic acquisition and filling of the insight-server related address of the global service cluster
- **Optimized** The default icon when the Helm chart icon is empty
- **Optimized** Select the network mode as None when creating the cluster to allow the user to install the network plug-in after the cluster is created
- **Optimized** Cluster Operations Information Architecture:
    - Adjust the cluster upgrade operation on the cluster list and cluster overview page to the cluster operation and maintenance function in the cluster details.
    - When a management cluster is removed from the cluster list, the cluster created based on this management cluster will hide the operations of upgrading the cluster, accepting managed nodes, and deleting nodes in the interface

#### Fix

- **Fixed** Problem with selected namespaces being automatically converted to all namespaces on resource switch
