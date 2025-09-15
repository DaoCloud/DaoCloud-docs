---
MTPE: windsonsea
date: 2025-03-18
---

# Container Management Release Notes

This page provides the Release Notes for container management to help you
understand the evolution path and feature changes from release to release.

*[kpanda]: Internal development codename for DaoCloud container management

## 2025-07-31

### v0.41

- **Added** GPU management support.  
- **Improved** instructions for batch uploading nodes when creating clusters or onboarding nodes.  
- **Improved** cluster list status display when cluster creation fails.  
- **Fixed** an issue where YAML data was abnormal during Helm application updates.  
- **Fixed** an issue where the maximum GPU memory size was incorrect in GPU configuration.  
- **Fixed** an issue where the console could not access pods after enabling the `UseTokenInCloudShell` feature.  
- **Fixed** an issue where `os_package_repo` was required during retry of cluster creation or node onboarding.  
- **Fixed** an error when adding nodes to Ubuntu 22.04 clusters with kernel tuning enabled.  
- **Fixed** an issue where etcd backups could not be used.  
- **Fixed** an issue where files could not be downloaded in stateless workload pods.  
- **Fixed** errors during Helm application installation.  
- **Fixed** incorrect log messages during Helm application uninstall.  
- **Fixed** an issue where GPU quotas could not be updated in quota management.  

## 2025-05-30

### v0.40

- **Added** support for separate `limit` and `request` configuration for Helm task resources.  
- **Added** support for cluster-specific `resolv.conf`.  
- **Added** support for configuring and displaying `nodeSelector` in workloads.  
- **Improved** automatic retry time for Helm installation.  
- **Improved** Dce5.0 interface data refresh to prevent stale data.  
- **Fixed** an issue where Helm installation was blocked by Baize kueue webhook.  
- **Fixed** an issue where KPanda nodes could not switch GPU mode after GPU training tasks completed.  
- **Fixed** GPU Operator v24.6.0+1 installation failure when deploying with installer.  
- **Fixed** an issue where users with `wsadmin`/`wsedit` permissions could not configure container security policies in namespaces.  
- **Fixed** Helm application installation failure could not be updated.  
- **Fixed** Helm repository information loss during installation or failure.  
- **Fixed** delayed status display after Helm application uninstall.  
- **Fixed** CloudShell permission leakage issue.  
- **Fixed** KPanda-apiserver memory anomalies.  
- **Fixed** optional GPU type selection issue during cluster operations.  
- **Fixed** an issue where uploading Chinese files in CloudTTY resulted in missing downloads.  
- **Fixed** an issue where Cluster Admin users successfully bound workspaces to clusters.  
- **Fixed** inconsistent access permissions between container management page and main page for Namespace Admin users.  
- **Fixed** unresponsive node checks after correcting timezone differences during cluster creation.  

## 2025-03-31

### v0.38

- **Added** support for installing container management via ARM packages, downloadable directly from the download site.  
- **Fixed** an issue where namespace resource quota requests exceeded limits without warnings but could still be set successfully.  
- **Fixed** DNS resolution issue in `kpanda-shell:v0.0.13`.  
- **Fixed** an issue where audit logs did not record user modifications to node taints.  

## 2025-02-28

### v0.37

- **Fixed** image pull errors for various services after offline installation of `metax-operator`.  
- **Fixed** offline Helm installation failure for `metax-operator`.  
- **Fixed** an issue where `PatchCustomResource` API failed to update resources.  
- **Fixed** installer failure due to special characters in external MySQL passwords.  

## 2025-01-31

### v0.36

- **Added** a packaged addon for Muxi `metax-exporter`, used to collect Muxi GPU device metrics in the cluster environment, with graphical visualization available in the observability module after installation.
- **Added** a packaged addon for Muxi `metax-extensions`, providing the `gpu-device` and `gpu-label` components to enable essential resource registration and allocation capabilities for containers using Muxi GPUs.
- **Added** a packaged addon for Muxi `metax-operator`, which includes all components, further cloud-native optimized beyond `metax-extensions` to reduce cluster resource burden and simplify operations.
- **Fixed** an issue with the display of the snapshot creation button in the PVC list.

## 2024-12-31

### v0.35

- **Updated** access restrictions so that only cluster admins can access the network settings module.
- **Updated** the cloudshell readiness process to improve speed when no idle workers are available.
- **Fixed** an issue where `kpanda`-related pods in production environments did not have resource limits set.
- **Fixed** a history information leak issue in the cloudtty console.
- **Fixed** an issue where keys would be lost after creating a cluster using key-based authentication, causing the private key to be unavailable when adding nodes again.
- **Fixed** an issue where job execution failures due to timeouts did not update the `helmrelease` status.

## 2024-11-30

### v0.34.0

- **Updated** the etcd backup section in the `ListClusterSummary` cluster list page.
- **Fixed** an issue where route configurations added to `VirtualService` by cloudshell were not cleaned up after the console was shut down.
- **Fixed** an issue where the console would continually attempt to reconnect and fail to display logs after cluster creation failure.
- **Fixed** an issue where expired cloudshell resources were not cleaned up in time.
- **Fixed** a backup failure issue in the backup and restore module when using `and` filtering for resource tags without selectors.

## 2024-10-30

### v0.33.0

#### New Features

- **Added** support for managing and scheduling Cambrian GPU cards
- **Added** a protection mechanism for the deletion of kubeconfig secret resources

#### Improvements

- **Improved** the upgrade of hami and gpu-operator addon versions to v2.4.1 and v24.6.0
- **Improved** the protection mechanism for deleting kubeconfig secret resources
- **Improved** the integration of the helm push plugin into the installer offline package
- **Improved** egress port allocation, maintaining a fixed egress port for the Cluster

#### Fixes

- **Fixed** the issue where the container group page on the node details page did not filter correctly based on GPU type
- **Fixed** the issue of residuals when uninstalling the metrics-server plugin
- **Fixed** the problem where custom content for yum_repos was lost during retry installation when creating a cluster
- **Fixed** the issue where deleting a node would cause the kpanda-controller-manager to panic when a worker was lost

## 2024-09-30

### v0.32.0

#### Features

- **Added** support for [Volcano Binpack](../user-guide/gpu/volcano/volcano_binpack.md) and [Priority Preemption Strategy](../user-guide/gpu/volcano/volcano_priority.md)
- **Added** support for the use of Muxi GPU cards
- **Added** GPU utilization metrics in the GPU monitoring panel
- **Added** quota and usage display for namespaces
- **Added** support for kubeconfig issued by the platform to be permanently valid
- **Added** custom roles now support permission mapping between workspaces and namespaces
- **Added** the feature to create PVCs through snapshots, allowing users to select their own StorageClass

#### Improvements

- **Improved** the text prompt for available GPU computing power in full GPU card mode
- **Fixed** an issue where the bound workspace was not displayed after binding a namespace, requiring a manual page refresh
- **Improved** compatibility with PVs where volumeMode is set to block
- **Improved** cleaned up intermediate images after merging Addon image architectures

#### Fixes

- **Fixed** an issue where the vGPU setting showed a computing power of 100 but the dashboard's Pod utilization rate displayed 0%
- **Fixed** an issue where the GPU Operator did not enable the Driver option, resulting in the GPU mode switch function not being displayed
- **Fixed** an issue where the number of GPUs displayed on the dashboard exceeded the actual value
- **Fixed** an issue with incorrect GPU utilization display on the node details page in MIG Mixed mode
- **Fixed** an excessive memory usage issue in the Binding Syncer for large-scale scenarios in 1000+ clusters
- **Fixed** a sudden increase in Redis connection counts when binding workspaces to each cluster in 1000+ clusters, which would not close for a long time
- **Fixed** an issue of resource permission confusion in workspace sharing in large-scale scenarios in 1000+ clusters
- **Fixed** the lack of audit logs when binding workspaces to clusters
- **Fixed** an issue where virtual machine clusters appeared in compliance scanning within security management
- **Fixed** an occasional issue of two uninstall Jobs appearing when uninstalling Helm applications
- **Fixed** an installation failure issue of metrics-server when upgrading the installer from v0.19.0 to v0.20.0
- **Fixed** an issue where the detection task was not canceled when clicking 'Check' and then 'Cancel' during cluster creation, resulting in subsequent checks showing as still in progress
- **Fixed** an issue in container management -> node management where global service clusters could not add or remove nodes
- **Fixed** an issue where a cluster showed as deleting indefinitely despite having actually failed to uninstall
- **Fixed** an issue where finalizers resources under `kpanda-system` were not deleted when detaching a cluster, preventing the deletion of the `kpanda-system` namespace
- **Fixed** an issue where the downgrade compatibility package for kubean in DCE 5.0 environments did not successfully delete low-version clusters
- **Fixed** an issue of incorrect display of backup recovery trigger times
- **Fixed** an issue where the cluster inspection configuration's scheduled task hour did not match the trigger time with the configured time.

## 2024-08-30

### v0.31.0

#### New Features

- **Added** support for heterogeneous GPUs, including Metax GPUs.
- **Added** support for installing Red Hat 9.2 driver images via GPU operator for heterogeneous GPUs.
- **Added** functionality to check and remind users of the validity period of cluster access certificates.
- **Added** support for viewing Helm content and generated orchestration files directly in the UI.

#### Improvements

- **Improved** the audit logs for switching GPU modes on nodes.
- **Improved** the layout of the NPU panel.
- **Improved** the wording on the GPU resource interface.
- **Improved** the issue where GPU labels on nodes were not removed until three minutes after the gpu-operator was uninstalled.
- **Improved** documentation for GPU metric alert operations.
- **Improved** the handling of a single GPU failure in multi-GPU scenarios, resolving the "UnexpectedAdmissionError" status for Pods during workload scheduling.
- **Improved** the access method for work clusters created by Kubean to use ServiceAccount Token authentication.
- **Improved** the removal of LeaseController from cluster_controller.
- **Improved** the kpanda-controller-manager to add some business-related monitoring metrics.
- **Improved** the repo_controller to include business monitoring metrics for Repo synchronization/downloads.
- **Improved** the cluster_setting_controller to add monitoring metrics for plugin synchronization.
- **Improved** the removal of informerFactory from GPUSchedulerController.
- **Improved** the multi-controller to allow specifying whether to enable or disable Controllers.
- **Improved** the logic in cluster_status_controller by introducing successThreshold and failureThreshold.
- **Improved** the introduction of parameters to control concurrency for Controllers.
- **Improved** unified logging output levels.
- **Improved** the time for re-queuing controllers.
- **Improved** the binding-syner Controller to allow specifying whether to enable or disable it.
- **Improved** the default version of custom resource CRDs.
- **Improved** the service list to support searching by service name, access method, and access port.
- **Improved** the experience of node time consistency during Kpanda cluster installation.
- **Improved** to prohibit concurrency in Helm lifecycle operations.
- **Improved** to add K8s orchestration confirmation during Helm installation.
- **Improved** the workload rollback feature to display detailed version information.

#### Fixes

- **Fixed** the inconsistency between GPU memory usage of GPU driver Pods and the information displayed in the application.
- **Fixed** an issue where the vGPU mode switched to full card mode after shutting down and restarting the VM.
- **Fixed** the loss of labels on nodes after enabling NPU virtualization.
- **Fixed** the incorrect display of GPU utilization rates in the GPU Pod dashboard.
- **Fixed** the incorrect display of GPU memory usage/rates in the GPU Pod dashboard.
- **Fixed** an issue where monitoring metrics did not display data when creating workloads using Ascend cards.
- **Fixed** an issue where changes to deviceSplitCount in vGPU mode were not effective.
- **Fixed** an issue where the page could not reflect the memory size when 5000 was entered in vGPU mode.
- **Fixed** an issue where the GPU type dropdown for Addon plugins under the cluster settings menu did not display information related to MIG.
- **Fixed** the problem of continuous crashes when restarting nodes with GPUs or upgrading the driver pod for vgpu-device-plugin.
- **Fixed** the inconsistency between GPU memory quota units and memory quota units.
- **Fixed** the failure to update Go dependencies due to conflicts with the otel dependency.
- **Fixed** an issue where the cloudshell CRD timeout page still prompted for reconnection.
- **Fixed** an issue where users with clusteradmin permissions (without global service cluster permissions) could directly access the details page of the global service cluster from the recent operations -> cluster operations page.
- **Fixed** the 403 error when users with Namespace Admin permissions viewed basic information about container configurations on workload detail pages.
- **Fixed** an issue where the NS quota was displayed, but the edit page data was empty.
- **Fixed** the inconsistency between the image addresses displayed on the container group detail page and the workload detail page.
- **Fixed** an issue where the port information was not displayed correctly when entering the health check page of the container configuration after updating the insight-ui stateless workload.
- **Fixed** the abnormal display issue of the kubeproxy version on nodes.
- **Fixed** an issue where DCE5-0.19 had problems recognizing the system code when accessing nodes or creating clusters on Ubuntu 22.04.
- **Fixed** the unknown status issue when creating Helm applications.
- **Fixed** the initial status of applications displayed as failed when creating Helm applications in work clusters.
- **Fixed** an issue where the status of readiness waiting configuration was not recorded during the update of Helm applications.
- **Fixed** an issue where enabling readiness waiting for sub-cluster installation of Helm applications failed, and the Helm application status remained in installation.

**Known Issues**

- **Fixed** the version mismatch between kpanda front-end and back-end, which could cause the vGPU mode to switch to full card mode after shutting down and restarting the VM.

## 2024-07-31

### v0.30.0

#### Features

- **Added** support for installing Koordinator plugins via Addon, completing online and offline mixed scheduling.
- **Added** UI supports 7-day or custom date options when generating kubeconfig.
- **Added** Helm charts support viewing Helm content and generated orchestration files on the interface.
- **Added** offline gpu-operator default operating system support for CentOS 7, Ubuntu 22.04, Ubuntu 20.04.
- **Added** support for Ascend NPU virtualization in document format.
- **Added** NPU monitoring dashboard supports switching between Chinese and English.
- **Added** gpu-operator supports enabling RDMA.

#### Improvements

- **Improved** added domain name field to Ingress list.
- **Improved** support for "Cluster Vendor" name in global service clusters (Daocloud Kubean).
- **Improved** Kpanda performance.
- **Fixed** an issue where certificates generated by kpanda's `GetClusterAdminKubeConfig`
  were unusable if they expired in one year.
- **Improved** support for checking and reminding about the validity period of cluster access certificates.
- **Improved** interface calls for obtaining installation configurations when installing Helm charts.
- **Improved** in addon-pack charts, images support specifying the architecture for pulling images
  via the `--platform` flag.
- **Improved** decoupling of helm controller from cluster service and rbac service and other improvements.
- **Improved** experience when switching GPU modes by adding switching status.
- **Improved** guide users on how to switch GPU modes when installing nvidia-vgpu and gpu-operator.
- **Fixed** misunderstanding issues when mig single mode was recognized as full card and used by users.

#### Fixed

- **Fixed** an issue where HPA created by various modules was invalid due to metrics-server not being
  installed by default in global service clusters.
- **Fixed** an issue with Kpanda database connection.
- **Fixed** an issue with PV/PVC permissions for the NS Admin role.
- **Fixed** an issue where egress port refresh led to data flow interruption and controller-manager malfunction
  after modifying cluster basic configurations.
- **Fixed** an issue where restarting workloads in the access method page of workload details resulted in
  a 404 error for the service interface.
- **Fixed** an issue with the missing offline package for cro-operator in addon.
- **Fixed** an issue with unintended system reboot during automatic kernel updates on Ubuntu.
- **Fixed** an issue with occasional display of full card mode on nodes when using MIG mode.
- **Fixed** an issue where memory overcommit feature was unavailable after GPU virtualization.
- **Fixed** an issue with occasional failure in switching GPU scheduling policies when adjusting GPU scheduling policy.

## 2024-06-30

### v0.29.0

#### Features

- **Added** support for K3s as a Kubernetes distribution for connected clusters.
- **Added** GPU status monitoring, viewable on the observability platform via XDI metrics.
- **Added** support for GPU scheduling Spread (cluster level).
- **Added** support for GPU scheduling Binpack (cluster level).
- **Added** support for GPU node scheduling Spread (cluster level).
- **Added** support for GPU node scheduling Binpack (cluster level).
- **Added** support for GPU node scheduling Spread (workload level).
- **Added** support for GPU node scheduling Binpack (workload level).
- **Added** support for GPU scheduling Spread (workload level).
- **Added** support for GPU scheduling Binpack (workload level).

#### Improvements

- **Improved** download station addon package to support multiple offline packages automatically.
- **Improved** Helm installation to be more cloud-native, with the controller managing Helm operation jobs.
- **Improved** quick link to view GPU resource allocation on the node details page, optimizing the integrated GPU quota issue on the monitoring page.
- **Improved** gpu-operator to support driver installation on the same OS with different kernel versions.
- **Improved** support for binpack/spread at the cluster level for GPUs and nodes, reaching product-level support for binpack/spread.
- **Improved** configmap/secret editor to support horizontal movement.
- **Improved** version selection filtering when updating modules.
- **Improved** issue where workspace admin permissions mapped to cluster admin permissions in container management did not display.
- **Improved** container log interface to support displaying 1000 lines.

#### Fixed

- **Fixed** an issue where deleted users still appeared in the cluster permission user list.
- **Fixed** an issue where cloudtty pod could not use kubeconfig with certificates to access sub-clusters.
- **Fixed** an issue where multi-architecture integration led to missing images in addon packages, causing service disruptions.
- **Fixed** an issue where the Deployment instance list displayed Pods not belonging to the current Deployment.
- **Fixed** an inconsistency between GPU memory allocation rate in the GPU node dashboard and the actual node.
- **Fixed** an issue with incorrect display of GPU node labels.
- **Fixed** an issue with LoadBalancer type service where updating the lb IP address and viewing service details
  occasionally showed nodeport access method.
- **Fixed** an issue with configuring multiple GPU types in mig mode when creating workloads.
- **Fixed** an issue with configuration mismatches in MIG Mixed mode when Deployment specified multiple different GPU types.

[v0.29.0 and above upgrade notes](offline-upgrade.md)

## 2024-05-31

### v0.28.0

#### Features

- **Added** support for ws admin+cluster admin to bind clusters/namespaces to workspaces in Kpanda.
- **Added** support for specifying volume snapshot classes when creating storage volume snapshots.
- **Added** support for modifying storage capacity in temporary paths when creating workloads.
- **Added** NPU-related metrics to load monitoring.
- **Added** validation for the presence of extended edge unit instances when disconnecting a cluster.
- **Added** optional use of egress in Kpanda for connected clusters.
- **Added** support for multiple offline packages (standard offline package / GPU offline package) in addons.
- **Added** compute usage metrics to the GPU monitoring panel.
- **Added** NPU-related metrics support in workloads.
- **Added** Nvlink metrics support in Kpanda metrics.

#### Improvements

- **Improved** display when disconnecting management clusters and sub-clusters.
- **Improved** prompt when loadBalancerIP is unavailable during service updates.
- **Improved** binding-syncer to support lease election.
- **Improved** unified description of compute units in full-card mode for Kpanda.
- **Improved** GPU monitoring metrics to support both English and Chinese.
- **Improved** default suggestion to disable servicemonitor during vgpu installation.

#### Fixed

- **Fixed** an issue where creating a multi-cloud instance namespace caused errors in container management queries.
- **Fixed** an issue where clicking the restart button in the job list caused errors and deleted jobs.
- **Fixed** an issue where kube-system and default namespaces were not synchronized to ghippo when connecting kind clusters.
- **Fixed** an issue where workspace-bound cluster resources were not filtered for multi-cloud clusters.
- **Fixed** an issue where workspace admin permissions mapped to cluster admin permissions in Kpanda did not display.
- **Fixed** an issue where the certificate generated by the Kpanda GetClusterAdminKubeConfig interface was only valid for one year, causing expiration issues.
- **Fixed** an issue where restricted namespace resource configurations for admin users did not reflect for NS admin accounts.
- **Fixed** an issue where worker nodes failed to connect in an online environment on Ubuntu 2004.
- **Fixed** an issue where upgrading from version 14.1 to 16.1 using the installer resulted in cluster creation errors and inability to select kube version.
- **Fixed** a display issue after cluster creation failure.
- **Fixed** an issue where kocral did not support backup and restoration of cluster resource namespaces.
- **Fixed** an issue where disabling scheduled inspections was ineffective.
- **Fixed** an issue where the frontend returned incorrect information when pods still had issues after installing the insight component.
- **Fixed** an issue where the GPU list was missing when specifying GPU models during Deployment creation in vGPU mode.
- **Fixed** an issue where GPU Pod monitoring dashboards had inconsistent display information in several places.

## 2024-04-30

### v0.27.0

#### Features

- **Added** support customizing NS admin/editor/viewer permissions through CRD configuration
- **Added** support connecting to cloudtty via SSH
- **Added** support accessing running containers through the console
- **Added** Install Ascend components Device Plugin and NpuExporter through Helm app scend-mindxdl, and view relevant metrics of Ascend GPUs through Insight

#### Improvements

- **Improved** Add audit logs for binding/unbinding workspace to ns in the kpanda interface
- **Improved** Support running make commands in local containers
- **Improved** ns quota configuration prompts
- **Improved** concurrent updates of Helm apps
- **Improved** Add more monitoring metrics to GPU monitoring dashboard

#### Fixes

- **Fixed** an issue with not being able to find mounted PVC volumes from the Deployment page
- **Fixed** an issue with inability to select S3 region in etcd backup policy
- **Bug Fix** Support token authentication for kpanda openapi proxies
- **Fixed** unpaginated results in liststorageclasses interface
- **Fixed** an issue with failed execution of cd_to_prod_site job in version release pipeline, requiring CI/CD script update
- **Fixed** an issue with upload failure when uploading files to target containers multiple times
- **Fixed** instability of cluster after long-running kpanda-binding-syncer in kairship e2e online environment
- **Fixed** an issue with empty docker_rh_repo form when running with docker as the runtime for access nodes
- **Fixed** echo issue when retrying after cluster creation failure
- **Fixed** an issue with child clusters still being displayed as managed by the parent cluster after removing cluster integration
- **Fixed** failure in node authentication check when creating cluster with RedHat8-OS and key authentication
- **Fixed** an issue with fluent-bit failing to start when selecting insight-agent installation during cluster creation
- **Fixed** failure in reset.yml execution by kubespray due to symbolic links in kubelet after retrying cluster creation
- **Fixed** an issue with helm repo not found during Insight Server upgrade
- **Fixed** an issue with ready check showing as disabled when creating metallb with ready check enabled but showing as disabled when editing
- **Fixed** an issue with incorrect image addresses in synchronized chart packages when relocateContainerImages is set to false in charts-syncer
- **Fixed** an issue with inability to restore modified PVC data after successful restore of sts+pvc backup
- **Fixed** backup failure when creating backup policy without backing up data volumes, but including PVs in backup resources
- **Fixed** an issue with always returning 0 available resources in vGPU mode
- **Fixed** an issue with GPU type displayed as MIG Mixed MIG Single in node details page under mig mixed mode
- **Fixed** an issue with AI processor count always showing total value in ascend monitoring dashboard
- **Fixed** inconsistency between labels on nodes and GPU types displayed in node details page
- **Fixed** incorrect PCIE data in GPU Pod Dashboard

## 2024-03-28

### v0.26.1

#### Features

- **Added** cloudtty provides SSH proxy functionality
- **Added** support for connecting to master nodes
- **Added** application backup plans can now be created via YAML
- **Added** capability to select backup objects based on resource type for application backup
- **Added** support for deleting cluster inspection templates
- **Added** deployment of NPU monitoring panel through npu-exportor
- **Added** display of available GPU resources when creating workloads
- **Added** capability to set job priority when creating workloads
- **Added** support for oversubscription of vGPU computing power
- **Added** scenario-based video for vGPU
- **Added** the capability to set the time zone when creating a cluster

#### Improvements

- **Improved** adaptation for the productization of the ZTE Kirin v7u6 version.
- **Improved** display of resource utilization percentage.
- **Improved** external mode in offline environments, cluster creation,
  and manual selection of yum repo information.
- **Improved** productization guidance and documentation for uploading Helm charts.
- **Improved** guidance for deploying GPU operator and Nvidia vGPU when the GPU switch is enabled.
- **Improved** logic for GPU switching.
- **Improved** validation of whether the node switch card is assigned.
- **Improved** display of oversubscription resources in vGPU mode on the node details page.

#### Fixes

- **Fixed** an issue with kube-vip when creating a cluster.
- **Fixed** an issue where cluster creation failed when "Enable kernel tuning for new cluster" was selected.
- **Fixed** an issue where Helm failed to reinstall after a failed installation.
- **Fixed** an issue where values could not be retrieved during a Helm app update after machine reconnection.
- **Fixed** a default rendering error for image addresses during offline installation of Submariner.
- **Fixed** an issue with duplicate concatenation of image addresses during Kpanda upgrade.
- **Fixed** an issue where the status remained "In Progress" continuously after backup restoration.
- **Fixed** an issue where inspection did not start after reaching the inspection
  frequency when scheduled inspection was enabled.
- **Fixed** an issue where removed nodes were still displayed in dashboard filtering after being removed from a cluster.
- **Fixed** an issue where GPU memory allocation rate did not update on the node details page after stopping GPU-enabled applications (open-source issue).
- **Fixed** an ambiguity in computing power and memory monitoring metrics for Pods in vGPU mode.
- **Fixed** an issue with inaccurate allocation count in MIG single mode.
- **Fixed** an occasional inaccuracy in GPU count in MIG mode.
- **Fixed** an issue where information from multiple nodes with GPUs could not be distinguished in the cluster dashboard without node filtering.
- **Fixed** an unclear prompt for vGPU usage duration, leading to incorrect usage.
- **Fixed** a display issue with GPU mode switching status.

## 2024-01-31

### v0.25.0

#### Features

- **Added** support for batch deletion/stop of multiple workloads
- **Added** support for setting time zone during cluster installation
- **Added** one-click enablement of Velero plugin during Velero installation
- **Added** option to enable or disable kube-vip control plane LB capability during cluster creation
- **Added** support for importing heterogeneous Addon packages
- **Added** capability to create GPU workloads on specific GPU models

#### Improvements

- **Improved** availability of GPU node switching, reducing switch time to within 2 seconds
- **Improved** logic for GPU mode switching
- **Improved** documentation for GPU-operator installation failure in Ubuntu environment
- **Improved** deep review and optimization of GPU dashboard (including vGPU, MIG, and whole GPU)
- **Improved** functionality related to GPU statistics at node level using custom metrics
- **Improved** latency when accessing drop-down menus for creating PVCs, network policies, and routing in cluster details page for large-scale clusters
- **Improved** browser freeze issue when switching namespaces after adding forwarding rules
  in clusters with 1000+ services
- **Improved** image selector to prevent page freeze when there are 1000+ image repositories
- **Improved** application backup logic

#### Fixes

- **Fixed** an issue where crontab configuration with cron expression caused inability
  to modify CronJob configuration
- **Fixed** infinite loop issue in installer caused by Redis Sentinel configuration
- **Fixed** refresh loop issue in console (cloudshell) reconnection mechanism, affecting command execution
- **Fixed** incorrect display of container CIDR after integration with DCE4
- **Fixed** incorrect image address in online upgrade of installer for kcoral image
- **Fixed** failure to restore Job during backup recovery
- **Fixed** an issue where enabling both HPA and CronHPA resulted in CronHPA being overwritten
- **Fixed** ineffective selection of installing Insight plugin during cluster creation in kpanda
- **Fixed** inability to upgrade current global cluster despite the page showing upgrade availability
- **Fixed** inability to set multiple lines in calico_node_extra_envs in Advanced Settings during cluster creation
- **Fixed** abnormal display of memory usage and other related metrics in cluster inspection report for pods
- **Fixed** failure to filter deleted pod information in NVIDIA GPU Pod dashboard in Pod filtering
- **Fixed** display issue where username and password fields still appeared
  when unified password was disabled during cluster creation
- **Fixed** failure to create cluster when enabling kernel tuning for new cluster

## 2023-12-31

### v0.24.0

#### Features

- **Added** support for recording creation and deletion operations of services,
  ingress, volume claims, volumes, and storage pool resources in kpanda audit logs
- **Added** compatibility with kubean to achieve downward compatibility with k8s versions in kpanda
- **Added** support for hot restart of Pods in Cloudtty
- **Added** integration of clusterpedia with OTEL Tracing
- **Added** support for minimal installation of security, inspection, backup, and virtual machine components
- **Added** documentation for importing custom helm charts into the system's built-in addon repository
- **Added** documentation for migration scenarios from DCE 4.0 to DCE 5.0 in limited cases

#### Improvements

- **Improved** the refresh time for the Pod list in kpanda after adding a large number of clusters
- **Upgraded** gpu-operator to v23.9.0 to reduce the gap with the community version
- **Improved** backup and restore process for entire namespaces (including CR and PVC-related content)
  to display partial success and failure information

#### Fixes

- **Fixed** an issue with permission leakage during addon lifecycle management.
- **Fixed** an issue where jobs were ineffective when using the same name for scheduled scaling jobs.
- **Fixed** an issue with detection on the page after installing kubernetes-cronhpa-controller in offline environments.
- **Fixed** an issue with the default sorting order in the ListPodsByNodeOrigin API.
- **Fixed** a rare occurrence of an empty container list in the ListContainersByPod API response.
- **Fixed** an error message during the execution of the scheduled_e2e job in the pipeline, causing subsequent tests to not be executed.
- **Fixed** an issue with unresponsive search in Data Collection when using Chinese characters.
- **Fixed** an issue where namespace-resource quota was not taking effect and update exceptions.
- **Fixed** an issue where read and write data was always empty in workload-load monitoring.
- **Fixed** an offline image issue with the gpu-operator.
- **Fixed** an issue with cluster management permission leakage to regular users during Helm installation in Kpanda.
- **Fixed** an issue with incorrect display of data volume backups in backup details after enabling backup for a plan.
- **Fixed** an issue where unauthorized users could still retrieve application backup plans of other clusters through the API.
- **Fixed** an incompatibility issue between Velero version and Kubernetes version in DCE4.
- **Fixed** an issue with slow loading of user and user group lists in large-scale scenarios.
- **Fixed** a timeout error in the Clusterpedia API and the inability to retrieve cloud-edge collaboration status in large-scale scenarios, leading to usability issues.
- **Fixed** an issue with missing display of all bound namespaces in large-scale scenarios
  in the namespace section.
- **Fixed** an issue with slow loading of the ns API in the container management section of the global management cluster, causing page lagging issues.

## 2023-11-30

### v0.23.0

#### Features

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
- **Improved** status of ETCD backup policy
- **Improved** error message when MySQL fails
- **Improved** workload node affinity/workload affinity/workload anti-affinity
- **Improved** support for removing abnormal nodes

#### Fixes

- **Fixed** an issue with workspace exceeding total quota for allocated resources
- **Fixed** security vulnerability of SQL injection
- **Fixed** an issue with failure to create UOS system clusters

## 2023-11-06

### v0.22.0

#### Features

- **Added** support for upgrading system component versions and modifying system component parameters through the interface.
- **Added** compatibility with [RedHat 9.2 cluster creation](../best-practice/create-redhat9.2-on-centos-platform.md).
- **Added** support for Nvidia full card, vGPU, and MIG GPU modes.
- **Added** support for Tianjic GPUs.
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

#### Improvements

- **Improved** support for viewing associated information in Configmap/Secret details page.
- **Improved** Resources visible for different permission users when entering Container Management.
- **Improved** support for automatic refreshing of Helm Repositories and auto-refresh switch
  within a specified time interval.

#### Fixed

- **Fixed** an issue where cluster uninstallation was not possible when cluster status was unknown.
- **Fixed** an issue where CPU usage data was not available for pod in the list.
- **Fixed** an issue where Insight-agent and Metrics-server plugins couldn't be installed on ARM architecture.
- **Fixed** an issue where node check failed when creating a cluster using a key.
- **Fixed** an issue where environment variables couldn't be added when creating a workload.
- **Fixed** an issue of remaining deleted user data.
- **Fixed** pagination issue in CIS compliance scan, permission scan, and vulnerability scan report list pages.
- **Fixed** an issue where static PV pointed to incorrect StorageClass when created.

## 2023-9-06

### v0.21.0

#### Features

- **Added** connectivity check for __Helm Repo__ passwords, with support for skipping TLS certificate authentication.
- **Added** scaling of worker nodes for global service machines.

#### Improvements

- **Improved** support for uninstalling related components during cluster integration.
- **Improved** pod status handling logic, including sub-status for pods.
- **Improved** the feature to configure the number of job records to keep for cluster operations.
- **Improved** support for configuring the number of control nodes when creating worker clusters.
- **Improved** prompt for installing Insight-agent if it is not already installed.

#### Fixes

- **Fixed** an issue of missing configuration parameters when updating helm app instances.
- **Fixed** display error in associated instances for Networkpolicy.
- **Fixed** an issue of cluster creation failure due to maximum pod count in cluster configuration.
- **Fixed** an issue of failed creation of worker clusters with __Redhat__ type.
- **Fixed** an issue of "no permission" error when namespace-level users view CronJob details.
- **Fixed** an issue of users unable to bind to workspaces.

## 2023-8-01

### v0.20.0

#### Features

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

- **Fixed** an issue where helm jobs remained in "Installing" or "Uninstalling" state.
- **Fixed** kernel version detection error when checking node creation.
- **Fixed** an issue where customizing namespaces was not possible for plugin cluster creation.
- **Fixed** default addition of __ca.crt__ data in key updates.

## 2023-7-06

### v0.19.0

#### Features

- **Added** compatibility for deploying worker clusters on openAnolis / Oracle Linux operating systems.
- **Added** support for automatically adding JFrog authentication information when creating clusters in an offline environment.
- **Added** validation rules for environment variable rules when creating workloads.
- **Added** edge load balancing and services.
- **Added** dual-stack and system kernel as pre-check items for nodes.
- **Added** the feature to mount secretKey/configmapKey as ConfigMaps inside containers when creating workloads.

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
- **Fixed** an issues related to namespace-level users not being able to use StorageClasses to create PVs.
- **Fixed** an issue where specifying a namespace when creating a route did not take effect.
- **Fixed** an issue where the date returned incorrectly after upgrading the cluster.

## 2023-6-03

### v0.18.1

- **Removed** the maximum length limit when setting custom parameters for cluster installation.

## 2023-5-28

### v0.18.0

#### Features

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

#### Features

- **Added** capability to download patrol report
- **Added** view of ETCD Backup Low
- **Added** support for enabling Flannel and Kube-ovn network plug-ins while creating a cluster
- **Added** support for Cilium dual-stack networking while creating a cluster
- **Added** automatic recognition of the node OS type while creating a cluster
- **Added** services of type Headless and External
- **Added** upgrading of kubernetes version of a worker cluster in an offline environment
- **Added** cluster-level resource backup
- **Added** creation of workload with a private key
- **Added** default resource limits configuration for Helm job
- **Added** creation of PVC using hwameistor

#### Improvements

- **Improved** Applying Backup Cluster State
- **Improved** Matching the workload state in the workload detail and the state of the pod under the load
- **Improved** node check interface in offline mode
- **Improved** presentation of multicloud applications

#### Fixes

- **Fixed** helm app configuration missing issue
- **Fixed** an issues with creation failure due to ns inconsistency while creating multiple types of resources using yaml
- **Fixed** the failure to select Docker 19.03 runtime using Kirin operating system
- **Fixed** incorrect translation of English interface

## 2023-04-04

### v0.16.0

#### Features

- **Added** capability to query PVC events using the interface.
- **Added** configuration of parameters such as backofflimit, completions, parallelism,
  and activeDeadlineSeconds while creating a job
- **Added** integration of self-developed open source storage component Hwameistor and support for viewing
  local storage resource overview and other information in the __container storage__ module
- **Added** cluster patrol feature supporting second-level patrol (Alpha) of the cluster
- **Added** application backup feature supporting quick backup and recovery (Alpha)
- **Added** platform backup feature supporting backup and recovery (Alpha) of ETCD data
- **Added** support for Ghippo’s custom role management cluster

#### Improvements

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

### v0.15.0

#### Features

- **Added** Productization support for Persistent Volumes (PVs), which supports selecting existing data volumes
  while creating PVCs.
- **Added** capability to create clusters using Kubernetes networkless CNI.
- **Added** support for the Chinese names of resources such as load, configuration, and service.
- **Added** creation of multiple types of resources simultaneously while creating workload via YAML.
- **Added** capability to pause and start workloads.

#### Improvements

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

### v0.14.0

#### Features

- **Added** support for displaying Chinese names and template suppliers in the Helm chart.
- **Added** CronHPA, which enables timed scaling of workloads.
- **Added** VPA (Vertical Scaling), which supports the manual/automatic modification of resource request values
  to achieve vertical workload scaling.
- **Added** Exclusive hosting capabilities for namespaces.
- **Added** StorageClass (StorageClass) support exclusive or shared entitlement to specific namespaces.
- **Added** Creation of Workloads exposes the remaining resource quota for the current namespace.
- **Added** Node connectivity check feature.
- **Added** Mirror Selector to support the selection of mirrors within the Container registry while creating workloads.
- **Added** backup and recovery features.

#### Improvements

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

- **Fixed** an issues with not being able to add new nodes with a password.
- **Fixed** Error in obtaining the cluster kubeconfig accessed in Token mode.
- **Fixed** Cannot get full users and groups when granting permissions.
- **Fixed** an issue unbinding the workspace original permissions when the Bindingsync component is abnormal.
- **Fixed** Workspace Resync does not properly remove unwanted permissions.
- **Fixed** Delete the question in which the Namespace can also be selected.
- **Fixed** Create a key. Key data is displayed in a single line.

## 2022-11-29

### v0.13.0

#### Features

- **Added** Replicatsets productization:
    - Replicatsets can be managed using the WEB terminal (CloudTTY).
    - Support for viewing Replicatsets monitoring, logs, Yaml, events, and containers.
    - Support for viewing Replicatsets details.
    - Linkage **Workbench**, the lifecycle of Replicatsets is managed by grayscale publishing.
- **Added** Pod details page.
- **Added** Namespace details page.
- **Added** Use the WEB terminal to upload files to the container and download files from the Pod to the local.
- **Added** The workload scales elastically based on the user-defined index, which is closer to the
  user’s actual business autoscaling requirements.

#### Improvements

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

### v0.10.0

#### Features

- **Added** NetworkPolicy policy management features, including the creation, update, and deletion of NetworkPolicy
  policies, as well as the display of NetworkPolicy policy details, to help users configure network traffic policies
  for the Pod.
- **Added** Workload supports multi-network card configuration and supports IP Pool display to meet
  the user’s requirement of configuring multiple network cards separately for workload configuration.
- **Added** support to view the operation log of the creation process after the failure of cluster creation,
  to help users quickly locate the fault.
- **Added** StatefulSets support the use of dynamic data volume templates.
- **Added** Create cluster, create Secret, create Ingress, edit the information verification of namespace quota,
  help guide the user to input the correct configuration parameters, and reduce the user’s failure experience
  of creating jobs.

#### Improvements

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

- **Fixed** an issues with selected namespaces being automatically converted to all namespaces on resource switch.
