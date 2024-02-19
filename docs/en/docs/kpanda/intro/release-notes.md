---
MTPE: windsonsea
date: 2024-01-05
---

# Container Management Release Notes

This page provides the Release Notes for container management to help you
understand the evolution path and feature changes from release to release.

*[kpanda]: Internal development codename for DaoCloud container management

## 2024-01-31

### v0.25.0

#### New Features

- **Added** Support for batch deletion/stop of multiple workloads
- **Added** Support for setting time zone during cluster installation
- **Added** One-click enablement of Velero plugin during Velero installation
- **Added** Option to enable or disable kube-vip control plane LB capability during cluster creation
- **Added** Support for importing heterogeneous Addon packages
- **Added** Ability to create GPU workloads on specific GPU card models

#### Improvements

- **Improved** Enhanced availability of GPU node switching, reducing switch time to within 2 seconds
- **Improved** Improved logic for GPU mode switching
- **Improved** Enhanced documentation for GPU-operator installation failure in Ubuntu environment
- **Improved** Deep review and optimization of GPU dashboard (including VGPU, MIG, and whole GPU card)
- **Improved** Optimized functionality related to GPU statistics at node level using custom metrics
- **Improved** Reduced latency when accessing drop-down menus for creating PVCs, network policies, and routing in cluster details page for large-scale clusters
- **Improved** Resolved browser freeze issue when switching namespaces after adding forwarding rules in clusters with 1000+ services
- **Improved** Optimized image selector to prevent page freeze when there are 1000+ image repositories
- **Improved** Optimized application backup logic

#### Fixes

- **Fixed** Issue where crontab configuration with cron expression caused inability to modify scheduled task configuration
- **Fixed** Infinite loop issue in installer caused by Redis Sentinel configuration
- **Fixed** Refresh loop issue in console (cloudshell) reconnection mechanism, affecting command execution
- **Fixed** Incorrect display of container CIDR after integration with DCE4
- **Fixed** Incorrect image address in online upgrade of installer for kcoral image
- **Fixed** Failure to restore Job during backup recovery
- **Fixed** Issue where enabling both HPA and CronHPA resulted in CronHPA being overwritten
- **Fixed** Ineffective selection of installing Insight plugin during cluster creation in kpanda
- **Fixed** Inability to upgrade current global cluster despite the page showing upgrade availability
- **Fixed** Inability to set multiple lines in calico_node_extra_envs in Advanced Settings during cluster creation
- **Fixed** Abnormal display of memory usage and other related metrics in cluster inspection report for container groups
- **Fixed** Failure to filter deleted pod information in NVIDIA GPU Pod dashboard in Pod filtering
- **Fixed** Display issue where username and password fields still appeared when unified password was disabled during cluster creation
- **Fixed** Failure to create cluster when enabling kernel tuning for new cluster

## 2023-12-31

### v0.24.0

#### New Features

- **Added** support for recording creation and deletion operations of services, routes, volume claims, volumes, and storage pool resources in kpanda audit logs
- **Added** compatibility with kubean to achieve downward compatibility with k8s versions in kpanda
- **Added** support for hot restart of Pods in Cloudtty
- **Added** integration of clusterpedia with OTEL Tracing
- **Added** support for minimal installation of security, inspection, backup, and virtual machine components
- **Added** documentation for importing custom helm charts into the system's built-in addon repository
- **Added** documentation for migration scenarios from DCE 4.0 to DCE 5.0 in limited cases

#### Improvements

- **Improved** the refresh time for the Pod list in kpanda after adding a large number of clusters
- **Upgraded** gpu-operator to v23.9.0 to reduce the gap with the community version
- **Improved** backup and restore process for entire namespaces (including CR and PVC-related content) to display partial success and failure information

#### Bug Fixes

- **Fixed** permission leakage issue during addon lifecycle management
- **Fixed** task ineffectiveness when using the same name for scheduled scaling tasks
- **Fixed** detection issue on the page after installing kubernetes-cronhpa-controller in offline environments
- **Fixed** default sorting order issue in ListPodsByNodeOrigin API
- **Fixed** rare occurrence of empty container list in ListContainersByPod API response
- **Fixed** error message during execution of scheduled_e2e task in pipeline, causing subsequent tests to not be executed
- **Fixed** unresponsive search in Data Collection using Chinese characters
- **Fixed** namespace-resource quota not taking effect and update exceptions
- **Fixed** read and write data always being empty in workload-load monitoring
- **Fixed** offline image issue with gpu-operator
- **Fixed** cluster management permission leakage to regular users during helm installation in kpanda
- **Fixed** incorrect display of data volume backups in backup details after enabling backup for a plan
- **Fixed** an issue where unauthorized users could still retrieve application backup plans of other clusters through the API
- **Fixed** incompatibility between velero version and k8s version in DCE4
- **Fixed** slow loading of user and user group lists in large-scale scenarios
- **Fixed** timeout error in clusterpedia API and inability to retrieve cloud-edge collaboration status in large-scale scenarios, leading to usability issues
- **Fixed** missing display of all bound namespaces in large-scale scenarios in the namespace section
- **Fixed** slow loading of ns API in the container management section of the global management cluster, causing page lagging issues.

## 2023-11-30

### v0.23.0

#### New Features

- **Added** audit logs for key functionalities such as cluster creation, deletion, access,
  unbinding, and upgrade; node access and unbinding; creation/deletion of deployment, statefulset,
  daemonset, job, and cron job; deployment/deletion of Helm apps
- **Added** support for integrating with ghippo LDAP user systems with usernames that
  exceed the legal range of K8s
- **Added** lifecycle management for large charts such as insight-agent
- **Added** support for hot reloading of ConfigMaps/Secrets
- **Added** support for subPathExpr in data storage

#### Improvements

- **Improved** display of the namespace to which an event belongs
- **Improved** status of ETCD backup strategy
- **Improved** error message when MySQL fails
- **Improved** workload node affinity/workload affinity/workload anti-affinity
- **Improved** support for removing abnormal nodes

#### Fixes

- **Fixed** an issue with workspace exceeding total quota for allocated resources
- **Fixed** security vulnerability of SQL injection
- **Fixed** an issue with failure to create UOS system clusters

## 2023-11-06

### v0.22.0

#### New Features

- **Added** support for upgrading system component versions and modifying system component parameters through the interface.
- **Added** Compatibility with [RedHat 9.2 cluster creation](../best-practice/create-redhat9.2-on-centos-platform.md).
- **Added** support for Nvidia full card, vGPU, and MIG GPU modes.
- **Added** support for Tianjic GPU cards.
- **Added** support for namespace-level GPU resource quota management.
- **Added** support for application-level GPU resource quota.
- **Added** Offline deployment and usage support for
  [CentOS 7.9](../user-guide/gpu/nvidia/install_nvidia_driver_of_operator.md)
  and [Redhat8.4 GPU Operator](../user-guide/gpu/nvidia/upgrade_yum_source_redhat8_4.md).
- **Added** support for monitoring cluster, node, and application-level GPU resources.
- **Added** Offline upgrade support for Container Management, Application Backup and Restore,
  Cluster Inspection, and Security Scanning product modules.
- **Added** support for multi-architecture deployment of Helm Charts.
- **Added** support for same version upgrade of clusters.
- **Added** support for [Configmap/Secret hot reloading](../user-guide/configmaps-secrets/configmap-hot-loading.md).
- **Added** Custom parameter configuration support for cluster-node checks to meet enterprise
  node encryption authentication and other scenarios.

#### Improved

- **Improved** support for viewing associated information in Configmap/Secret details page.
- **Improved** Resources visible for different permission users when entering Container Management.
- **Improved** support for automatic refreshing of Helm Repositories and auto-refresh switch
  within a specified time interval.

#### Fixed

- **Fixed** an issue where cluster uninstallation was not possible when cluster status was unknown.
- **Fixed** an issue where CPU usage data was not available for container group in the list.
- **Fixed** an issue where Insight-agent and Metrics-server plugins couldn't be installed on ARM architecture.
- **Fixed** an issue where node check failed when creating a cluster using a key.
- **Fixed** an issue where environment variables couldn't be added when creating a workload.
- **Fixed** an issue of remaining deleted user data.
- **Fixed** pagination issue in CIS compliance scan, permission scan, and vulnerability scan report list pages.
- **Fixed** an issue where static PV pointed to incorrect StorageClass when created.

## 2023-9-06

### v0.21.0

#### New Features

- **Added** connectivity check for __Helm Repo__ passwords, with support for skipping TLS certificate authentication.
- **Added** scaling of worker nodes for global service machines.

#### Improvements

- **Improved** support for uninstalling related components during cluster integration.
- **Improved** pod status handling logic, including sub-status for pods.
- **Improved** ability to configure the number of task records to keep for cluster operations.
- **Improved** support for configuring the number of control nodes when creating working clusters.
- **Improved** prompt for installing Insight-agent if it is not already installed.

#### Bug Fixes

- **Fixed** an issue of missing configuration parameters when updating helm app instances.
- **Fixed** display error in associated instances for Networkpolicy.
- **Fixed** an issue of cluster creation failure due to maximum pod count in cluster configuration.
- **Fixed** an issue of failed creation of working clusters with __Redhat__ type.
- **Fixed** an issue of "no permission" error when namespace-level users view scheduled task details.
- **Fixed** an issue of users unable to bind to workspaces.

## 2023-8-01

### v0.20.0

#### New Features

- **Added** helm app interface supports viewing Helm operation logs.
- **Added** workload clusters support heterogeneous node integration.
- **Added** batch import of nodes supported for cluster creation.
- **Added** container storage supports creating NFS-type data volumes.
- **Added** support for vGPU, with automatic detection of node CPUs and support
  for adding negative CPU quota in workload configuration.

#### Improvements

- **Improved** cluster integration logic. When integrating a cluster with a new management platform
  after the initial integration, it is necessary to clean up the data redundancy from the old management platform
  before it can be integrated. For more details about cluster integration, refer to
  [Uninstall/Deintegrate Cluster](../user-guide/clusters/delete-cluster.md).
- **Upgraded** clusterpedia to v0.7.0.
- **Improved** permission-based page interactions, where users without permissions will not
  be able to access pages with no resource permissions.
- **Improved** advanced parameter configuration, such as kernel tuning, for integrated nodes.
- **Improved** installation detection mechanism for Insight component.

#### Fixes

- **Fixed** an issue where helm tasks remained in "Installing" or "Uninstalling" state.
- **Fixed** kernel version detection error when checking node creation.
- **Fixed** an issue where customizing namespaces was not possible for plugin cluster creation.
- **Fixed** default addition of __ca.crt__ data in key updates.

## 2023-7-06

### v0.19.0

#### New Features

- **Added** compatibility for deploying working clusters on openAnolis / Oracle Linux operating systems.
- **Added** support for automatically adding JFrog authentication information when creating clusters in an offline environment.
- **Added** validation rules for environment variable rules when creating workloads.
- **Added** edge load balancing and services.
- **Added** dual-stack and system kernel as pre-check items for nodes.
- **Added** the ability to mount secretKey/configmapKey as ConfigMaps inside containers when creating workloads.

#### Improvements

- **Improved** helm repository refresh mechanism.
- **Improved** some I8N English translation interfaces.

#### Fixes

- **Fixed** an issue where custom parameters entered when creating a cluster would incorrectly
  convert values of 0 or 1 to true or false.
- **Fixed** an issue where containerd account password configuration could not be written when
  creating a cluster in an offline environment.
- **Fixed** an issue where upgrading a cluster with version 1.26 or above failed due to changes
  in the Kubernetes container registry.
- **Fixed** issues related to namespace-level users not being able to use StorageClasses to create PVs.
- **Fixed** an issue where specifying a namespace when creating a route did not take effect.
- **Fixed** an issue where the date returned incorrectly after upgrading the cluster.

## 2023-6-03

### v0.18.1

- **Removed** the maximum length limit when setting custom parameters for cluster installation.

## 2023-5-28

### v0.18.0

#### New Features

- **Added** inspection report download.
- **Added** global audit logs for high-priority operations.
- **Added** timeout handling for connecting to Minio.

#### Improvements

- **Improved** the mounting of KubeConfig in CloudShell from using ConfigMap to using Secret.
- **Added** a switch to filter clusters that have backup strategies when selecting a cluster
  for creating a backup policy.

#### Fixes

- **Fixed** the offlineization of etcdbrctl images.
- **Fixed** an issue where the image selector could not select an image.
- **Fixed** the rendering of Repo address when creating a cluster.

## 2023-04-28

### v0.17.0

#### New Features

- **Added** ability to download patrol report
- **Added** view of ETCD Backup Low
- **Added** support for enabling Flannel and Kube-ovn network plug-ins while creating a cluster
- **Added** support for Cilium dual-stack networking while creating a cluster
- **Added** automatic recognition of the node OS type while creating a cluster
- **Added** services of type Headless and External
- **Added** upgrading of kubernetes version of a working cluster in an offline environment
- **Added** cluster-level resource backup
- **Added** creation of workload with a private key
- **Added** default resource limits configuration for Helm job
- **Added** creation of PVC using hwameistor

#### Optimizations

- **Improved** Applying Backup Cluster State
- **Improved** Matching the load state in the load detail and the state of the pod under the load
- **Improved** node check interface in offline mode
- **Improved** presentation of multicloud applications

#### Fixes

- **Fixed** helm app configuration missing issue
- **Fixed** issues with creation failure due to ns inconsistency while creating multiple types of resources using yaml
- **Fixed** the failure to select Docker 19.03 runtime using Kirin operating system
- **Fixed** incorrect translation of English interface

## 2023-04-04

### v0.16.0

#### New Features

- **Added** ability to query PVC events using the interface.
- **Added** configuration of parameters such as backofflimit, completions, parallelism,
  and activeDeadlineSeconds while creating a task
- **Added** integration of self-developed open source storage component Hwameistor and support for viewing
  local storage resource overview and other information in the __container storage__ module
- **Added** cluster patrol feature supporting second-level patrol (Alpha) of the cluster
- **Added** application backup feature supporting quick backup and recovery (Alpha)
- **Added** platform backup feature supporting backup and recovery (Alpha) of ETCD data
- **Added** support for Ghippo’s custom role management cluster

#### Optimizations

- **Improved** kpanda uninstalls self-built cluster process to prevent cluster deletion due to user misoperation.
- **Improved** User experience of recreating the cluster after the failure of the interface to create the cluster.
  Supports quickly reinstalling the cluster based on the configuration before the failure.
- **Improved** Aggregated multiple Quotas when multiple Quota resources exist under one namespace.
- **Improved** Information display of service access mode in workload details supporting rapid
  access to load service.
- **Improved** Refresh mechanism of helm repo without enabling automatic refresh by default.

#### Fixes

- **Fixed** Loadblance address unreachable issue.
- **Fixed** Failed to perform an unmount cluster operation.
- **Fixed** Cluster acquisition issue due to more than 64 characters connected to the cluster.
- **Fixed** Cluster plugin display issue in offline environment cluster.
- **Fixed** Global cluster failed to update configuration
- **Fixed** First node check failure while creating a cluster resulting in no further node checks.
- **Fixed** Environment variables for creating/updating workloads not taking effect.

## 2023-02-27

### v0.15

#### New Features

- **Added** Productization support for Persistent Volumes (PVs), which supports selecting existing data volumes
  while creating PVCs.
- **Added** Ability to create clusters using Kubernetes networkless CNI.
- **Added** support for the Chinese names of resources such as load, configuration, and service.
- **Added** creation of multiple types of resources simultaneously while creating workload via YAML.
- **Added** ability to pause and start workloads.

#### Optimizations

- **Improved** Cluster details page, experience of cluster switching.
- **Improved** Workload status display, add __Stopped__ status.
- **Improved** Manual scaling window of workload increased to simplify user's manual scaling process.
- **Improved** Accessing DCE 4.X cluster from cluster.
- **Improved** Resync Workspace removes unwanted permissions properly.
- **Improved** Cluster upgrade interface interaction experience.
- **Improved** Namespace provided to quickly create an entry when Helm is used to create an application.

#### Fixes

- **Fixed** DNS configuration issue forcing users to fill in upstream DNS while creating a cluster.
- **Fixed** Workload version records sorted out of order.
- **Fixed** Kubean upgrade via Helm not working.
- **Fixed** Last exception promptmissing while creating a cluster.
- **Fixed** an issue that the workload status is displayed incorrectly or cannot be refreshed in some cases.
- **Fixed** an issue of missing prompt for Workspace deletion.
- **Fixed** an issue of incorrect display of resource utilization information in some cases.
- **Fixed** an issue of failed access to DCE 4.X clusters using domain names.

## 2022-12-29

### v0.14

#### New Features

- **Added** support for displaying Chinese names and template suppliers in the Helm chart.
- **Added** CronHPA, which enables timed scaling of workloads.
- **Added** VPA (Vertical Scaling), which supports the manual/automatic modification of resource request values
  to achieve vertical workload scaling.
- **Added** Exclusive hosting capabilities for namespaces.
- **Added** StorageClass (StorageClass) support exclusive or shared entitlement to specific namespaces.
- **Added** Creation of Workloads exposes the remaining resource quota for the current namespace.
- **Added** Node connectivity check function.
- **Added** Mirror Selector to support the selection of mirrors within the Container registry while creating workloads.
- **Added** backup and recovery features.

#### Optimizations

- **Improved** The process of cluster uninstallation by adding the cluster deletion protection switch.
- **Improved** supports simultaneous creation of multiple resources when creating resources via YAML.
- **Improved** The workload increases the manual scaling window to simplify the user’s manual scaling process.
- **Improved** Service access mode experience, supports service quick access and display node, load balancing address.
- **Improved** File upload and download functionality to support the selection of a specific container.
- **Improved** support offline installation of different OS systems.
- **Improved** Node configuration while creating a cluster in an offline environment supports the selection of
  node operating systems and the modification of offline Yum sources.
- **Improved** The YAML editor does not fill in the Namespace field and supports autocomplete as default.
- **Improved** Cluster upgrade interface interaction experience.
- **Improved** When Helm is used to create an application, Namespace is provided to quickly create an entry.

#### Fixes

- **Fixed** Issues with not being able to add new nodes with a password.
- **Fixed** Error in obtaining the cluster kubeconfig accessed in Token mode.
- **Fixed** Cannot get full users and groups when granting permissions.
- **Fixed** an issue unbinding the workspace original permissions when the Bindingsync component is abnormal.
- **Fixed** Workspace Resync does not properly remove unwanted permissions.
- **Fixed** Delete the question in which the Namespace can also be selected.
- **Fixed** Create a key. Key data is displayed in a single line.

## 2022-11-29

### v0.13

#### New Features

- **Added** Replicatsets productization:
    - Replicatsets can be managed using the WEB terminal (CloudTTY).
    - Support for viewing Replicatsets monitoring, logs, Yaml, events, and containers.
    - Support for viewing Replicatsets details.
    - Linkage **Workbench**, the full life cycle of Replicatsets is managed by grayscale publishing.
- **Added** Pod details page.
- **Added** Namespace details page.
- **Added** Use the WEB terminal to upload files to the container and download files from the Pod to the local.
- **Added** The workload scales elastically based on the user-defined index, which is closer to the
  user’s actual business elastic expansion and contraction requirements.

#### Optimizations

- **Improved** Deploy cluster support:
    - Deploy a cluster using the cilium CNI.
    - Create a cluster with nodes with different usernames, passwords, and SSH ports.
- **Improved** The Pod list supports viewing the total number of pods and the number in operation,
  as well as viewing the container type.
- **Improved** The workload increases the manual scaling window to simplify the user’s manual scaling process.
- **Improved** The container log supports viewing init container and ephemeral container, providing
  a more friendly operation and maintenance experience.
- **Improved** Node details. Note that the value does not correctly display the issue.
- **Improved** Operation prompt feedback, giving the user correct feedback on the operation.

#### Fixes

- **Fixed** Failure to create a namespace due to strong coupling between the namespace creation
  and the binding workspace.
- **Fixed** The routing rule update failed to modify the path prefix issue for the forwarding policy.
- **Fixed** Creating a workload interface while creating Services does not work.
- **Fixed** Update service exception error reporting issue.
- **Fixed** Unable to access the AWS cluster.
- **Fixed** The user list is not synchronized after using the WS Admin user to bind the resource group.
- **Fixed** On the configuration details page, when Page Size = 50, the List ClusterConfigMaps
  interface reports an exception.

## 2022-10-28

### v0.10

#### New Features

- **Added** NetworkPolicy policy management features, including the creation, update, and deletion of NetworkPolicy
  policies, as well as the display of NetworkPolicy policy details, to help users configure network traffic policies
  for the Pod.
- **Added** Workload supports multi-network card configuration and supports IP Pool display to meet
  the user’s requirement of configuring multiple network cards separately for workload configuration.
- **Added** support to view the operation log of the creation process after the failure of cluster creation,
  to help users quickly locate the fault.
- **Added** Stateful workloads support the use of dynamic data volume templates.
- **Added** Create cluster, create Secret, create Ingress, edit the information verification of namespace quota,
  help guide the user to input the correct configuration parameters, and reduce the user’s failure experience
  of creating tasks.

#### Optimizations

- **Improved** The cluster drop-down list supports the display of cluster status, and optimizes the
  user’s experience of selecting the managed cluster when creating a cluster, selecting the target cluster
  when creating a namespace, and selecting the target cluster when authorizing a cluster.
- **Improved** Install the insight-agent plug-in in the helm app to support the automatic acquisition
  and filling of the insight-server related address of the global service cluster.
- **Improved** The default icon when the Helm chart icon is empty.
- **Improved** Select the network mode as None when creating the cluster to allow the user to install
  the network plug-in after the cluster is created.
- **Improved** Cluster Operations Information Architecture:
    - Adjust the cluster upgrade operation on the cluster list and cluster overview page to the cluster operation and maintenance feature in the cluster details.
    - When a management cluster is removed from the cluster list, the cluster created based on this
      management cluster will hide the operations of upgrading the cluster, accepting managed nodes,
      and deleting nodes in the interface.

#### Fixes

- **Fixed** Issues with selected namespaces being automatically converted to all namespaces on resource switch.
