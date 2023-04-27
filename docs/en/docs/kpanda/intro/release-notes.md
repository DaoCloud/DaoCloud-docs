# Container Management Release Notes

This page lists the Release Notes of container management, so that you can understand the evolution path and feature changes of each version.

## 2023-04-04

### v0.16.0

#### Features

- **NEW** Query PVC events using the interface.
- **NEW** Added support for configuring backofflimit, completions, parallelism, activeDeadlineSeconds and other parameters when creating a task.
- **New** Integrate the self-developed open source storage component Hwameistor, and support viewing the overview of local storage resources and other information in the `container storage` module.
- **New** Added the cluster inspection function, which supports second-level inspection of the cluster (Alpha).
- **NEW** Added application backup function, which supports interface-based quick application backup and recovery (Alpha).
- **NEW** Added platform backup function, which supports backup and recovery of ETCD data (Alpha).
- **New** Support Ghippo's custom role management cluster.

#### Optimization

- **Optimized** Kpanda uninstalls the self-built cluster process, so as to avoid the cluster being deleted due to user misoperation.
- **Optimized** The user experience of recreating a cluster after a cluster creation failure on the interface allows users to quickly reinstall the cluster based on the configuration before the failure.
- **Optimization** Optimized the processing logic when there are multiple Quota resources under one namespace. Aggregated multiple Quota
- **Optimized** The information display of the service access method in the workload details supports quick access to the load service.
- **Optimization** Optimize the Helm warehouse refresh mechanism, automatic refresh is not enabled by default

#### fix

- **FIXED** Loadblance address cannot be accessed.
- **Fix** the problem that the uninstall cluster operation failed.
- **FIXED** The problem that the cluster cannot be obtained when more than 64 characters are used to access the cluster.
- **Fix** Fix the problem that the cluster plug-in cannot be displayed in the offline environment cluster.
- **Fix** the problem that the Global cluster cannot update the configuration.
- **FIXED** When creating a cluster, the node check fails for the first time, and the node check cannot be performed again.
- **FIXED** The problem that environment variables for creating/updating workloads do not take effect.

## 2023-02-27

### v0.15

#### Features

- **Added** Product support for PV (Persistent Volumes), support for selecting existing data volumes when creating a PVC.
- **NEW** Ability to create clusters using kubernetes no-network CNI.
- **NEW** Added support for Chinese names of resources such as load, configuration, and service.
- **NEW** The creation of workloads through YAML supports the creation of multiple types of resources at the same time.
- **NEW** Pause and start functions for workloads.

#### Optimization

- **Optimized** Cluster details page, cluster switching experience.
- **Optimized** Workload status display, increase `Stopped (Stopped)` status.
- **Optimized** Added a manual scaling window for workloads, simplifying the manual scaling process for users.
- **Optimization** The access cluster cannot access the DCE4.X cluster problem.

#### fix

- **Fix** Fixed the problem that the DNS configuration forced the user to fill in the upstream DNS when creating a cluster.
- **FIXED** Fixed the confusion of sorting workload version records.
- **FIXED** Upgrade Kubean via Helm does not work.
- **Fix** The problem that the previous exception prompt did not disappear after the node check failed during cluster creation and then checked again.
- **FIXED** The problem of image pull failure when creating a workload.
- **Fixed** the problem that the scheduled backup strategy cannot execute the `Immediately` operation.
- **Fix** UI automatically adds resource limit issue when modifying workloads without resource limit.
- **FIXED** When the `workspace` is not bound to any user, adding a namespace to the `workspace` fails.
- **Fix** Fix the problem that binding and unbinding namespaces will cause namespace annotations to disappear.
- **Fix** Fix the problem that creating a cluster using `kube-vip` policy does not take effect.
- **Fix** When creating a cluster and setting `ntp servers` to be empty, the existing `ntp` address of the host will be cleared.

## 2022-12-29

### v0.14

#### Features

- **NEW** Helm templates support displaying Chinese names and template suppliers.
- **NEW** CronHPA, which supports scheduled scaling of workloads.
- **Added** VPA (Vertical Scaling), which supports manual/automatic modification of resource request values to achieve vertical scaling of workloads.
- **Added** Namespace exclusive host function.
- **New** The storage pool (StrogeClass) supports authorization to specific namespaces for exclusive use or sharing.
- **NEW** Added support for displaying the remaining resource quota of the current namespace when creating a workload.
- **Add** node connectivity check function.
- **NEW** Added an image selector, which supports selecting images in the image warehouse when creating workloads.
- **New** app backup and restore function.

#### Optimization

- **Optimize** cluster uninstall process, add cluster deletion protection switch.
- **Optimized** Support to create multiple resources at the same time when creating resources through YAML.
- **Optimized** Added a manual scaling window for workloads, simplifying the manual scaling process for users.
- **Optimized** Service (Service) access method experience, support service quick access and display node, load balancing address.
- **Optimized** Support for selecting a specific container for file upload and download.
- **Optimized** Support offline installation of different OS systems.
- **Optimized** Create a cluster in an offline environment - node configuration supports selecting node operating systems and modifying offline Yum sources.
- **Optimization** YAML editor does not fill in the Namespace field, and supports automatic completion as Default.
- **Optimized** Cluster upgrade interface interaction experience.
- **Optimization** When using Helm to create an application, provide a Namespace quick creation entry.

#### fix

- **FIXED** Can't use password to add new nodes.
- **Fixed** the cluster kubeconfig error problem for accessing through the Token method.
- **FIXED** Unable to get full user and group when granting permissions.
- **Fix** There is a problem with unbinding the original permissions of the workspace when the Bindingsync component is abnormal
- **FIXED** Workspace Resync cannot correctly delete redundant permissions.
- **Fix** the problem that the Namespace in deletion can still be selected.
- **FIXED** When creating a key, the key data is displayed in a single line.

## 2022-11-29

### v0.13

#### New features

- **New** Productization of Replicatsets:
    - Support using WEB terminal (CloudTTY) to manage Replicatsets.
    - Support viewing Replicatsets monitoring, logs, Yaml, events, containers.
    - Support viewing Replicatsets details.
    - Linked with **Application Workbench**, the whole lifecycle of Replicatsets is managed by Grayscale Release.
- **New** Pod details page.
- **NEW** Namespace details page.
- **NEW** Use the WEB terminal to upload files to the container and download files from the Pod to the local.
- **New** The workload is elastically scaled based on custom indicators, which is closer to the user's actual business elastic expansion and contraction needs.

#### Optimization

- **Optimized** Deployment cluster support:
    - Deploy the cluster using cilium CNI.
    - Create a cluster with nodes with different usernames, passwords, SSH ports.
- **Optimized** The Pod list supports viewing the total number of container groups and the running number, as well as viewing the container type.
- **Optimized** Added a manual scaling window for workloads, simplifying the manual scaling process for users.
- **Optimized** The container log supports viewing init container and ephemeral container, providing a more friendly operation and maintenance experience.
- **Optimization** node details, the value of annotation vaule is not displayed correctly.
- **Optimization** Operation prompt feedback, giving users correct feedback on operations.

#### Fix

- **FIXED** The problem that creating a namespace fails due to the strong coupling between creating a namespace and binding a workspace.
- **Fix** The problem that updating the routing rules cannot modify the path prefix of the forwarding policy.
- **FIXED** The problem that creating a service while creating a workload interface does not take effect.
- **FIXED** The update service exception error problem.
- **FIXED** Unable to connect to AWS cluster.
- **FIXED** Kpanda user list is out of sync after using WS Admin user to bind resource group.
- **Fixed** the configuration details page, when PageSize=50, the ListClusterConfigMaps interface abnormally reports an error.

## 2022-10-28

### v0.10

#### Features

- **Added** NetworkPolicy policy management functions, including creating, updating, deleting NetworkPolicy policies, and displaying NetworkPolicy policy details to help users configure inbound and outbound traffic policies for Pods
- **NEW** The workload supports multi-NIC configuration and IP Pool display, which meets the user's need to configure multiple NICs separately for workload configuration
- **New** After the cluster creation fails, it supports viewing the operation log of the creation process to help users quickly locate the fault
- **NEW** Stateful workloads support the use of dynamic data volume templates
- **Add** Create cluster, create Secret, create Ingress, edit namespace quota information verification, help guide users to enter the correct configuration parameters, and reduce user experience of failure to create tasks

#### Optimization

- **Optimized** The cluster drop-down list supports displaying cluster status, and optimizes user experience when creating a cluster to select a managed cluster, creating a namespace to select a target cluster, and cluster authorization to select a target cluster
- **Optimization** Install the insight-agent plug-in in the helm application to support automatic acquisition and filling of the Insight-server related address of the global service cluster
- **optimized** default icon for Helm template icon when it is empty
- **Optimization** Select the network mode as None when creating a cluster to allow users to install the network plug-in after the cluster is created
- **Optimized** cluster operation information architecture:
    - Adjust the cluster upgrade operation on the cluster list and cluster overview pages to the cluster operation and maintenance function in the cluster details
    - When a management cluster is removed from the cluster list, the cluster created based on this management cluster will be hidden on the interface. Cluster upgrade, manage node, delete node operations

#### Fix

- **Fix** When switching resources, the selected namespace is automatically converted to all namespaces