# Container Management Release Notes

This page lists the container-managed Release Notes to help you understand the evolution path and feature changes from release to release.

## 2023-04-28

### v0.17.0

#### New features

- **Add** Download  the patrol report
- **Add** View ETCD Backup Low
- **Add** Creating a cluster supports enabling Flannel, Kube-ovn network plug-ins
- **Add** Create a cluster Enable Cilium dual-stack networking
- **Add** Creating a cluster supports automatic recognition of the node OS type
- **Add** Services of type Headless, External
- **Add** Upgrading the kubernetes version of a working cluster in an offline environment
- **Add** Cluster-level resource backup
- **Add** Create a workload with a private key
- **Add** Configure default resource limits for Helm job
- **Add** Create a PVC using hwameistor

#### Optimize

- **Optimize** Apply Backup Cluster State
- **Optimize** Mismatch between the load state in the load detail and the state of the pod under the load
- **Optimize** Node check interface in offline mode
- **Optimize** Presentation of multi-cloud applications

#### Fix

- **Fix** Update helm application configuration missing issue
- **Fix** Using yaml to create multiple types of resources due to the problem of ns inconsistency leading to creation failure
- **Fix** Failed to select Docker 19.03 runtime using the Kirin operating system
- **Fix** Incorrect translation of English interface

## 2023-04-04

### v0.16.0

#### New features

- **Add** Use the interface to query PVC events.
- **Add** Creating a task supports the configuration of parameters such as backofflimit, completions, parallelism, and activeDeadlineSeconds.
- **Add** Integrate the self-developed open source storage component Hwameistor, and support `container storage` the view of local storage resource overview and other information in the module.
- **Add** Cluster patrol function is added, which supports second-level patrol (Alpha) of the cluster.
- **Add** Application backup function is added to support quick application backup and recovery (Alpha).
- **Add** Platform backup function is added to support backup and recovery (Alpha) of ETCD data.
- **Add** Support for Ghippo’s custom role management cluster.

#### Optimize

- **Optimize** Kpanda uninstalls the self-built cluster process to prevent the cluster from being deleted due to user misoperation.
- **Optimize** The user experience of recreating the cluster after the failure of the interface to create the cluster, which supports the user to quickly reinstall the cluster based on the configuration before the failure.
- **Optimize** Optimized processing logic when multiple Quota resources exist under one namespace. Multiple Quotas are aggregated
- **Optimize** The information display of the service access mode in the workload details supports the rapid access to the load service.
- **Optimize** Optimize the refresh mechanism of helm repo, and do not enable automatic refresh by default

#### Fix

- **Fix** Loadblance address unreachable problem.
- **Fix** Failed to perform an unmount cluster operation.
- **Fix** The cluster cannot be acquired due to more than 64 characters connected to the cluster.
- **Fix** Fixed an issue where the offline environment cluster could not display the cluster plug-in.
- **Fix** Global cluster failed to update the configuration.
- **Fix** When creating a cluster, the first node check fails and the node check cannot be performed again.
- **Fix** Environment variables for creating/updating workloads do not take effect.

## 2023-02-27

### v0.15

#### New features

- **Add** Productization support for PVs (Persistent Volumes), which supports the selection of existing data volumes when creating PVCs.
- **Add** Ability to create clusters using kubernetes networkless CNI.
- **Add** Support the Chinese names of resources such as load, configuration, and service.
- Creating a workload **Add** via YAML supports the simultaneous creation of multiple types of resources.
- The ability to pause and start **Add** workloads.

#### Optimize

- **Optimize** Cluster details page, experience of cluster switching.
- **Optimize** Workload status display, add `Stopped` status.
- **Optimize** The workload increases the manual scaling window to simplify the user’s manual scaling process.
- **Optimize** The access cluster cannot access the DCE 4.X cluster.

#### Fix

- **Fix** Fixed an issue where DNS configuration forced users to fill in upstream DNS when creating a cluster.
- **Fix** Fixed an issue where the workload version records were sorted out of order.
- **Fix** Kubean upgrade via Helm does not work.
- **Fix** The problem that the last exception prompt does not disappear after the creation of the cluster execution node fails to check again.
- **Fix** Workload creation, mirror pull failure issues.
- **Fix** Timed backup strategy, unable to perform `Run now` operations.
- **Fix** When modifying a workload without resource constraints, the UI automatically adds resource constraint issues.
- **Fix** The problem of failing to `workspace` add a namespace when `workspace` no user is bound to it.
- **Fix** Fixed an issue where binding and unbinding namespaces would cause namespace annotations to disappear.
- **Fix** Fix the issue where the create cluster usage `kube-vip` policy does not take effect.
- **Fix** When the create cluster is set `ntp servers` to empty, the host is cleared of existing `ntp` address issues.

## 2022-12-29

### v0.14

#### New features

- **Add** Helm template supports the display of Chinese names and template suppliers.
- **Add** CronHPA, which supports timed scaling workloads.
- **Add** VPA (Vertical Scaling) supports manual/automatic modification of resource request values to achieve vertical workload scaling.
- **Add** Namespace has exclusive hosting capabilities.
- **Add** Storage Pools (StrogeClass) support exclusive or shared entitlement to specific namespaces.
- **Add** The Create Workload support exposes the remaining resource quota for the current namespace.
- **Add** Node connectivity check function.
- **Add** Added Mirror Selector to support the selection of mirrors within the mirror repository when creating workloads.
- **Add** Apply backup and recovery features.

#### Optimize

- **Optimize** In the process of cluster uninstallation, the cluster deletion protection switch is added.
- **Optimize** Supports simultaneous creation of multiple resources when creating resources via YAML.
- **Optimize** The workload increases the manual scaling window to simplify the user’s manual scaling process.
- **Optimize** Service access mode experience, support service quick access and display node, load balancing address.
- **Optimize** File upload and download support the selection of a specific container.
- **Optimize** Support offline installation of different OS systems.
- **Optimize** Create a cluster in an offline environment-Node configuration supports the selection of node operating systems and the modification of offline Yum sources.
- **Optimize** The YAML editor does not fill in the Namespace field and supports autocomplete as Default.
- **Optimize** Cluster upgrade interface interaction experience.
- **Optimize** When Helm is used to create an application, Namespace is provided to quickly create an entry.

#### Fix

- **Fix** Problem with not being able to add new nodes with password.
- **Fix** Error in obtaining cluster kubeconfig accessed in Token mode.
- **Fix** Cannot get full users and user groups when granting permissions.
- **Fix** There is a problem unbinding the workspace original permissions when the Bindingsync component is abnormal
- **Fix** Workspace Resync does not properly remove unwanted permissions.
- **Fix** Delete the question in which the Namespace can also be selected.
- **Fix** Create a key. Key data is displayed in a single line.

## 2022-11-29

### v0.13

#### New features

- **Add** Replicatsets productization:
    - Replicatsets can be managed using the WEB terminal (CloudTTY).
    - Support for viewing Replicatsets monitoring, logs, Yaml, events, and containers.
    - Support for viewing Replicatsets details.
    - Linkage ** Application Workbench **, the full life cycle of Replicatsets is managed by grayscale publishing.
- **Add** Pod details page.
- **Add** Namespace details page.
- **Add** Use the WEB terminal to upload files to the container and download files from the Pod to the local.
- **Add** The workload scales elastically based on the user-defined index, which is closer to the user’s actual business elastic expansion and contraction requirements.

#### Optimize

- **Optimize** Deploy cluster support:
    - Deploy a cluster using the cilium CNI.
    - Create a cluster with nodes with different usernames, passwords, and SSH ports.
- **Optimize** The Pod list supports viewing the total number of pods and the number in operation, as well as viewing the container type.
- **Optimize** The workload increases the manual scaling window to simplify the user’s manual scaling process.
- **Optimize** The container log supports viewing init container and ephemeral container, providing a more friendly operation and maintenance experience.
- **Optimize** Node details. Note that the vaule value does not correctly display the problem.
- **Optimize** Operation prompt feedback, giving the user correct feedback on the operation.

#### Fix

- **Fix** Failure to create a namespace due to strong coupling between the namespace creation and the binding workspace.
- **Fix** The routing rule update failed to modify the path prefix issue for the forwarding policy.
- **Fix** Creating a workload interface while creating Services does not work.
- **Fix** Update service exception error reporting issue.
- **Fix** Unable to access the AWS cluster.
- **Fix** The user list is not synchronized after using the WS Admin user to bind the resource group.
- **Fix** On the configuration details page, when Page Size = 50, the List ClusterConfigMaps interface reports an exception.

## 2022-10-28

### v0.10

#### New features

- **Add** NetworkPolicy policy management functions, including the creation, update, and deletion of NetworkPolicy policies, as well as the display of NetworkPolicy policy details, to help users configure network traffic policies for the Pod
- **Add** Workload supports multi-network card configuration and supports IP Pool display to meet the user’s requirement of configuring multiple network cards separately for workload configuration
- **Add** Support to view the operation log of the creation process after the failure of cluster creation, to help users quickly locate the fault
- **Add** Stateful workloads support the use of dynamic data volume templates
- **Add** Create cluster, create Secret, create Ingress, edit the information verification of namespace quota, help guide the user to input the correct configuration parameters, and reduce the user’s failure experience of creating tasks

#### Optimize

- **Optimize** The cluster drop-down list supports the display of cluster status, and optimizes the user’s experience of selecting the managed cluster when creating a cluster, selecting the target cluster when creating a namespace, and selecting the target cluster when authorizing a cluster
- **Optimize** Install the insight-agent plug-in in the helm application to support the automatic acquisition and filling of the insight-server related address of the global service cluster
- **Optimize** The default icon when the Helm template icon is empty
- **Optimize** Select the network mode as None when creating the cluster to allow the user to install the network plug-in after the cluster is created
- **Optimize** Cluster Operations Information Architecture:
    - Adjust the cluster upgrade operation on the cluster list and cluster overview page to the cluster operation and maintenance function in the cluster details.
    - When a management cluster is removed from the cluster list, the cluster created based on this management cluster will hide the operations of upgrading the cluster, accepting managed nodes, and deleting nodes in the interface

#### Fix

- **Fix** Problem with selected namespaces being automatically converted to all namespaces on resource switch
