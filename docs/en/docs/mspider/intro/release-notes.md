---
MTPE: windsonsea
Revised: done
Pics: NA
Date: 2023-07-28
---

# Service Mesh Release Notes

This page lists all the Release Notes for each version of Service Mesh, providing convenience for users to learn about the evolution path and feature changes.

## 2023-08-31

### v0.19.0

#### Upgrades

- **Added** `userinfo` interface to retrieve permissions information for the current user.

    **Note: To obtain accurate permission information, the `mesh_id` parameter must be provided when accessing the mesh**.

- **Added** support for virtual machines (automatically creates `WorkloadShadow`) in `Mcpc Controller`.
- **Added** service interface for creating virtual machines (VM) within the mesh.
- **Added** script for building and uploading offline installation packages for virtual machines (VM).
- **Added** interface to bind services and generate configurations for virtual machines (VM).
- **Added** `Reporter` parameter to the routing panel of `Grafana`.
- **Added** `Mspider` virtual machine agent controller (`mspider-vm-agent`).
- **Added** `generator` package, implementing `ComponentAnalyzer`. Pass in `MeshCluster` or `GlobalMesh` to retrieve corresponding component statuses.
- **Improved** upgrade interface for checking mesh availability by adding permission checks.
- **Improved** `reconcileComponentsStatus` in `gsc-controller` under mesh-cluster.
- **Upgraded** frontend version to `v0.17.0`.
- **Upgraded** supported mesh versions to `1.16.6`, `1.17.5`, `1.18.2`.

#### Fixes

- **Fixed** issue with filtering `ServiceEntry` outside the mesh.
- **Fixed** compatibility problem with regular expression of `workloadId` when querying virtual machine workload instances (e.g., `{CLUSTER}-vm-{VM_APP}-{VM_IP}-{VM_NETWORK}`).
- **Fixed** issue where creating east-west gateways during cluster creation would overwrite the default north-south gateway configuration.
- **Fixed** automatic creation of governance policies for virtual machine services and inability to synchronize changes in labels to `WorkloadShadow`.
- **Fixed** issue where network groups in multi-cloud interconnection couldn't have names starting with a digit.
- **Fixed** loss of custom configuration when updating the mesh.
- **Fixed** null pointer issue in `work-api` component due to removal of `label` from `Secret`.
- **Fixed** failure to delete mesh when system namespaces were included (they are uninstalled during deletion).
- **Fixed** issue where `customMeshConfig` didn't take effect on `Operator`.
- **Fixed** mismatch between `Operator` version and actual installed version of `Istio`.
- **Fixed** inability to collect metrics in `Mspider` control plane API Server and Work API Server due to permission issues.
- **Fixed** issue where metrics weren't collected in `Mspider` control plane and `MCPC Ckube` components.
- **Fixed** issue where `k8s.pod.name` field was reported as `unknown` in `OTEL` trace data.
- **Fixed** warning alert during the initial execution of virtual machine installation script.

## 2023-07-28

### v0.18.0

#### Upgrades

- **Added** Recommended versions will be included in the `Istio` version list.
- **Added** Detection condition for joining the interconnection network pool: `CLUSTER_EXIST_NET_POOLS`.
- **Added** Interface to get the namespace list in a cluster.
- **Added** Support for filtering system namespaces in `filter_system_namespaces`.
- **Added** Interface to get the list of sidecar-injected workloads in a cluster.
- **Added** New field `graph_type` in the workload view of the monitoring topology,
  currently supporting `SERVICE_SCOPE` and `WORKLOAD_SCOPE`, defaulting to `SERVICE_SCOPE`.
- **Added** Detection condition for removing network groups: whether they exist in the network interconnection pool (`NET_EXISTS_NET_POOLS`).
- **Added** Support for searching by `PodLabels` in the sidecar workload list using `page.search`.
- **Added** Interface to query the list of multi-cluster workloads:
  `/apis/mspider.io/v3alpha1/meshes/{mesh_id}/clusters/-/sidecar-management/workloads`, also supports searching by `PodLabels`.
- **Added** Design of service diagnosis interface.
- **Added** Implementation of detection condition for removing clusters from the mesh: whether they have joined the interconnection network pool (`CLUSTER_EXIST_NET_POOLS`).
- **Added** Implementation of interface for checking the validity of gateway names in the mesh.
- **Added** Field `filter_system_namespaces` to the namespace list in a cluster.
- **Added** Field `filter_system_namespaces` to the list of sidecar-injected workloads in a cluster.
- **Added** Support for workload dimension in monitoring topology.
- **Added** Implementation of service diagnosis interface (with automatic repair for some issues).
- **Added** Detection of diagnostic items requiring manual repair.
- **Added** Implementation of service repair interface.
- **Added** New tag `k8s.pod.name` in `Trace Tags` to indicate the name of the `Pod`.
- **Added** Platform administrators and workspace administrators can manage multi-cloud network interconnections for meshes under their workspace.
- **Upgraded** `Istio api` to fix the issue where `WasmPlugin` cannot set priority.
- **Upgraded** `ckube` to `v1.3.5` to resolve the issue where the service mesh list might be empty.

#### Fixes

- **Fixed** Inconsistency between `sidecar` and `sidecarResources`.
- **Fixed** Disorder of sorting indexes in the workload list.
- **Fixed** `ListClusterNamespace` interface to support querying namespace information by cluster.
- **Fixed** Issue where globally bound mesh resources may not be displayed internally in the mesh.
- **Fixed** Inability to modify `portName` for empty port protocols.
- **Fixed** Issue where diagnostic items for `Workload` were missing `Service`.
- **Fixed** Permanent failure in synchronization of service configuration sync diagnostics.
- **Fixed** Inaccuracy in audit logs for some batch operation interfaces.
- **Fixed** Unreachable clusters are still attempted to be probed with `livez`.
- **Fixed** Incorrect status of workloads when namespace injection status changes in dedicated mesh mode.
- **Fixed** Failure in successful synchronization of `leaderelection`.
- **Fixed** Incorrect total count of `Pods` in the mesh in some cases.
- **Fixed** Typo in error messages, changing `mot` to `not`.
- **Fixed** Inability to repair sidecar injection status for certain services.
- **Fixed** Failure of interface `/apis/mspider.io/v3alpha1/clusters/{name}/components` and `/apis/mspider.io/v3alpha1/clusters/{name}` when `mesh_id` is not passed for non-admin users.
- **Fixed** Name validation of `Istio CRD`, allowing the first letter of all operation names to be a number.
- **Fixed** Incorrect comment about `label_selectors` in the `Graph` interface.
- **Fixed** Lack of message body description for service diagnosis repair interface.
- **Optimized** Description of the `namespaces` field in the `Istio` resource interface.
- **Optimized** Detection process of mesh control plane, ignoring control plane clusters.
- **Optimized** Consistency of different permissions for different roles with the latest permission design.
- **Optimized** Permission design, separating multi-cloud network interconnection permission from mesh management.
- **Optimized** Meaning of the `global.high_available` parameter.
- **Optimized** Usage of `CHART.replicas`, changing default value to empty.

## 2023-06-29

### v0.17.0

#### Features

- **Added** `mspider.io/mesh-gateway-name` label specification for defining the mesh gateway name.
- **Added** `injectionStatus` field to namespace for listing and searching purposes.
- **Added** `label_selectors` field in topology queries for conditional querying of topology results.
- **Added** `Labels` and `PodLabels` fields to sidecar workload information.
- **Added** `Labels` and `PodLabels` fields to service workload information.
- **Added** component information (components) and Istio version (meshVersion) fields to cluster information.
- **Added** `include_components` field to cluster list and mesh management cluster list for selecting whether to display cluster component information, such as Insight and other external components.
- **Added** audit information for all necessary interfaces.
- **Added** ability to clear deployment injection policies.
- **Added** Implemented index search for namespace lists.
- **Added** audit log capability.
- **Added** ability to clear deployment injection policies.
- **Added** Implemented component status in cluster list.
- **Added** `mspider.io/mesh-gateway-name` label specification for defining the gateway name.
- **Added** Implemented automatic service injection capability for `MCPC Controller`.
- **Added** Ghippo resource reporting functionality, automatically creating and updating `GProductResource` resources according to specifications.
- **Added** `global.config.enableAutoInitPolicies` configuration for enabling automatic initialization of governance policies for managed services in `MCPC Controller`.
- **Added** `global.config.enableAutoInjectedSidecar` configuration for enabling automatic injection policies for managed services in `MCPC Controller`.
- **Added** compatibility testing for various versions of K8s.
- **Optimized** cache to improve the latency issue of querying `Insight Agent` status in clusters.
- **Optimized** Strengthened detection of conflicting meshes when creating a mesh for managed clusters.
- **Optimized** Ignored updates to name (Name), namespace (Namespace), and labels (Labels) when updating mesh gateways to avoid triggering exceptions.
- **Optimized** Updated synchronization method for Kpanda cluster kubeconfig.
- **Optimized** Created logic for `WorkloadShadow controller watcher`.
- **Upgraded** Supported querying cluster and cluster component information independently without passing MeshID.
- **Upgraded** go package istio.io/istio to `v0.0.0-20230131034922-50fb2905d9f5` version.
- **Upgraded** CloudTTY to `v0.5.3` version.
- **Upgraded** front-end version to `v0.15.0`.

#### Fixes

- **Fixed** inaccurate audit log description when creating East-West gateway for clusters.
- **Fixed** ineffectiveness of replica count for East-West gateways.
- **Fixed** invalid detection of sidecar removal during mesh deletion.
- **Fixed** inability to filter namespaces in monitoring topology.
- **Fixed** inaccurate error rate data for monitoring topology services.
- **Fixed** returning 404 error when mesh does not exist.
- **Fixed** panic caused by `nil pointer` in Audit.
- **Fixed** displaying Enum type resource types as numbers in audit logs.
- **Fixed** inconsistency in behavior between GRPC requests with user authentication information and HTTP requests.
- **Fixed** failure to create `Telemetry` resources during dedicated mesh creation.
- **Fixed** failure to rebuild `RegProxy watcher`.
- **Fixed** incorrect labeling by `traffic-lane` plugin, causing traffic lane to not work.
- **Fixed** failure to properly clean up cluster configuration when deleting the mesh.
- **Fixed** abnormal behavior of `MCPC Controller` when accessing unhealthy clusters.
- **Fixed** inability to remove components during mesh deletion or cluster removal process.
- **Fixed** GlobalMesh and MeshCluster remaining in deletion state and unable to be forcefully deleted.
- **Fixed** incorrect injection status for system namespaces that are not injected by default.
- **Fixed** selection of non-ready Pods when proxying `HostedAPIServer`, causing the mesh to not become ready.
- **Fixed** failure to delete Telemetry during mesh deletion, which caused the mesh deletion process to fail. This resource is cleaned up during Istio uninstallation or removal of `HostedAPIServer`, so it does not need to be deleted during the mesh deletion process.
- **Fixed** issue with installing `HostedAPIServer` on OCP due to permission problems.
- **Fixed** description in Helm chart.

#### Removals

- **Removed** 443 port from service `istiod-[meshID]-hosted-lb` in managed mesh mode.

## 2023-05-31

### v0.16.1

#### Features

- **Added** Ckube loads resources on demand.
- **Added** IstioResource field: `labels` and `annotations`, can update Labels and Annotations.
- **Added** ClusterProvider synchronization implementation in MeshCluster.
- **Added** Definition of the `mspider.io/protected` label for mesh protection.
- **Added** Sidecar upgrade supports multiple workload capabilities, `SidecarUpgrader` simultaneously supports `workloadshadow.name` and `deployment.name`.
- **Added** Workload type is re-implemented as a string.
- **Added** The `localized_name` field is added to the workload-related interface to display workload names.
- **Added** Workload injection policy clearing capability
- **Added** Get global configuration interface `/apis/mspider.io/v3alpha1/settings/global-configs`.
- **Added** `clusterPhase` field is added to mark the cluster's status (previously marked in the phase field, now separated).
- **Added** `clusterProvider` field is added to mark the cluster provider.
- **Added** Traffic lane CRD capability implementation.
- **Added** Reg-Proxy component is enabled by default.
- **Added** Implementation of Service selector field output.
- **Added** Solving cross-cluster access problems when Sidecars are not injected by adding a Network label to Namespace.
- **Added** Custom parameter configuration capability for hosted mesh hosted-apiserver. (This parameter only takes effect during installation and does not support updates for the time being), (for more parameters, please refer to helm parameter configuration):
- **Added** Mesh control plane component status
- **Added** The mesh query interface adds the `loadBalancerStatus` field to describe the actual assigned LB address.
- **Added** Component progress detail interface `/apis/mspider.io/v3alpha1/meshes/{mesh_id}/components-progress`.
- **Added** HPA is added for control plane components.
- **Added** New API definition to get cluster `StorageClass`.
- **Added** New API definition to get installed components in the cluster (currently supports Insight Agent).
- **Optimization:** Improved user experience for binding/unbinding workspaces.
- **Optimization:** The `workload_kind` field type in the workload-related interface is optimized from enumeration to `string`.
- **Optimization:** When hosting a mesh, version detection of the control plane cluster is included along with the working cluster.

#### Fixes

- **Fixed** CloudShell permissions issue.
- **Fixed** MeshCluster Status RemotePilotAddress invalid data not cleared promptly.
- **Fixed** Problem where MeshCluster cannot be deleted.
- **Fixed** Insufficient content in FailedReason of TrafficLane.
- **Fixed** Missing action field in TrafficLaneActionsRequest.
- **Fixed** The mesh list cannot be displayed when there are unhealthy clusters.
- **Fixed** Incorrect number of effectively injected instances when an instance is abnormal.
- **Fixed** WasmPlugin cannot create multiple instances when a service is selected by multiple lanes.
- **Fixed** The service label may have residual old workloads.
- **Fixed** The service list cannot obtain the effective number of workloads, and the type parsing error of Dynamic ReadyReplicas.
- **Fixed** When the workload changes, the changed status cannot be synchronized to the corresponding Service.
- **Fixed** Checking the status of a cluster that is not connected to the mesh.
- **Fixed** Cluster status is not searchable.
- **Fixed** Mesh cannot remove the cluster when there is no sidecar.
- **Fixed** Regular expression for mesh name does not allow numbers to start.
- **Fixed** Mesh status display is incorrect, and status is sometimes displayed as normal when there is no sidecar.
- **Fixed** Fixed the problem that the automatic injection template of the mesh is not effective.
- **Fixed** the issue where non-admin users cannot obtain traffic topology due to the lack of default values in the cluster.
- **Fixed** the null pointer exception in the automatic injection service policy.

## 2023-04-27

### v0.15.0

#### Features

- Introduced `d2` as a drawing tool.
- Added a new wasm plugin that adds different headers to requests according to the trace ID.
- Hosted Istiod's LoadBalancer Annotations implementation in mesh configuration.
- Implemented mesh gateway configuration service Annotations.
- Added `load_balancer_annotations` field to mesh, supporting custom load balancing annotations.
- In `mspider-api`, manually run the pipeline and set `SYNC_OPENAPI_DOCS` as the key to trigger the upload of the document site (raise PR).
- When the MCPC Controller perceives that the `mspider.io/managed` label exists in the Service, it will trigger the automatic creation of a governance policy corresponding to the service.
- MCPC Controller multiple workload type support.
- Added health check function, which automatically rebuilds proxy when mesh APIServer fails to connect to prevent PortForward's own logic from being unreliable (may be related to Istio Sidecar).

#### Fixes

- Previously not compatible with `grpcgateway-accept-language` (equivalent to HTTP's Accept-Language) header, resulting in inability to switch between Chinese and English modes correctly. Compatible with both Accept and Accept-Language modes now.
- When synchronizing OpenAPI, upstream cannot push due to shadow clone code.
- Unable to update Istio resources with `.`.
- In version 1.17.1, istio-proxy cannot start normally.
- The ingress gateway lacks a name, causing the merge to fail and cannot be deployed.
- The service address cannot be searched.
- Unable to update Istio resources with `.`.
- Previous controller memory leak issue fixed.
- Add/delete cluster logic now triggers correctly sometimes.
- When global injection is turned on, updating the mesh may cause the istio-operator pod to be injected, causing the mesh creation to fail.
- Fixed a problem that caused the virtual cluster to be synchronized to `Mspider` and lead to access failure.
- Optimized the controller namespace and service resource processing logic to reduce frequent triggering of workloadShadow resource updates.
- Optimized the problem of frequent acquisition/update of `workloadShadow` resources and only reconcile some resources that have undergone specific changes.
- Reduce pod changes and constantly update `WorkloadShadow`.
- Wasm plugin image address wrong spelling in `relok8s`.
- TrafficLane default repository bug.
- Helm image rendering template optimized; the image structure is split into three parts: `registry/repository:tag`.

#### Removed

- Logic to sync global cluster to mesh removed.
- Deprecated Deployment Controller logic.
- `ui.version` parameter deprecated, changed to `ui.image.tag` parameter to set the frontend version.

## 2023-03-31

### v0.14.3

#### Features

- Frontend version upgraded to `v0.12.2`.

#### Fixes

- Unable to update Istio resources with `.`.
- In version 1.17.1, istio-proxy cannot start normally.
- The ingress gateway lacks a name, causing the merge to fail and cannot be deployed.

## 2023-03-30

### v0.14.0

#### Features

- CloudShell related interface definition added.
- Tag implementation for update service added.
- Service list and details will return labels.
- CloudShell related implementation added.
- Support for querying service labels added in the service list.
- New API added for updating a service's tags.
- Istio 1.17.1 support added.
- A new etcd high availability solution added.
- Scenario-based testing framework for testing scenario-based features added.
- When selecting different mesh sizes, automatically adjust component resource configuration.
- Implementation of custom roles added, supporting operations such as creation, update, deletion, binding, and unbinding of custom roles.

#### Optimization

- MCPC controller startup logic optimized to avoid the situation that the working cluster is not registered correctly.
- WorkloadShadow cleanup logic optimized: triggered by timing trigger transformation events: when the controller starts, when a change in the working cluster is detected;
   When WorkloadShadow changes, self-health detection triggers cleanup logic when the corresponding workload does not exist.
- Insight API upgraded to version `v0.14.7`.
- `Ckube` supports complex conditional query of labels.
- Helm upgrade time limit removed.

#### Fixes

- The interface does not display when the east-west gateway is not Ready.
- Multicloud interconnection will automatically register the east-west gateway LB IP, which may cause internal network abnormalities (remove the east-west gateway instance label: `topology.istio.io/network`. This label will automatically register the east-west gateway).
- Cluster migration with east-west gateway enabled may cause incorrect service resolution.
- Fixed an issue where the control plane cannot be deployed on a single-node Kubernetes cluster.
- The `istioctl` installation error caused by the `kubectl` version mismatch fixed.
- The invalidation of VirtualService cache optimized, reducing the possibility of inconsistent virtual services after deletion.
- Fixed an issue where the `meshconfig-default` ConfigMap is not properly synced when upgrading from previous versions.
- Fixed the problem that Prometheus is not running when deploying Service Mesh using `istioctl`.
- Fixed an issue where the Envoy proxy cannot start due to missing `SO_KEEPALIVE` option in the socket configuration.

#### Deprecated

- Deployment Controller logic deprecated.

## 2023-02-28

### v0.13.2

#### Features

- Automatic injection of sidecar added (requires Kubernetes 1.16 or higher).
- Istio 1.16.4 support added.
- Enhanced Mesh expansion capabilities added.
- Support for customizing the number of replicas of each component added.
- Support for customized component resource configurations like CPU and memory added.
- Integration with OAM (Open Application Model) added.
- Support for exporting metrics to OpenTelemetry added.

#### Optimization

- MCPC controller now supports updating multiple resources at once to improve synchronization efficiency.
- Improved the handling of expired certificates in mesh components.
- The performance of the `WorkloadShadow` module optimized through reducing unnecessary requests and adding local caching.
- Upgraded the `insight-api` version to improve stability.

#### Fixes

- Fixed an issue where the Istiod pod is stuck in the "Pending" state when deployed on specific Kubernetes distributions.
- Fixed an issue where VirtualServices cannot be updated due to conflicting port numbers.
- Fixed an issue where injecting a sidecar into a Pod may cause its name to exceed the maximum length allowed by Kubernetes.
- Fixed an issue where the `istioctl` command fails to connect to the Istio API server when running in a containerized environment.
- Fixed an issue where the Kiali dashboard displays inconsistent traffic data with Prometheus.

## 2023-01-31

### v0.13.0

#### Features

- Multicluster management feature added.
- Support for multicloud interconnection added.
- Service dependency analysis and visualization feature added.
- New `dial` and `readinessProbe` options added to endpoint slice.
- Service mesh security audit feature added.
- Istio 1.16.3 support added.
- Support for customizing the Istiod configuration added.

#### Optimization

- Improved the efficiency of MCPC controller synchronization.
- Optimized the performance of Istiod initialization.
- Optimized the `WorkloadShadow` module to reduce resource consumption.
- Upgraded the `Mspider` version to improve stability.

#### Deprecated

- Global cluster syncing logic removed.

## 2022-12-31

### v0.12.1

#### Features

- Service mesh visualization feature added.
- Support for exporting metrics to Grafana added.
- Virtual machine mesh support added.
- Istio 1.16.2 support added.
- The `MeshExpansion` and `SidecarInjectorWebhook` components now support custom configuration.

#### Optimization

- Improved the performance of the MCPC controller.
- Optimized the handling of expired certificates in the mesh components.
- Upgraded the `insight-api` version to improve stability.

#### Fixes

- Fixed an issue where the Istiod pod may fail to start due to a timing issue.
- Fixed an issue where the `workloadLabels` field in Istio resources is not properly handled by the controller.
- Fixed an issue where the `istioctl` command fails to connect to the Istio API server when running in a containerized environment.

## 2022-11-30

### v0.12.0

#### Features

- Support for multi-tenancy added.
- Istio 1.16.1 support added.
- New `MeshExpansion` and `SidecarInjectorWebhook` components added.
- Automatic sidecar injection feature added.
- Support for customizing the Istiod configuration added.

#### Optimization

- Improved the stability and performance of the MCPC controller.
- Upgraded the `insight-api` version to improve stability.

#### Fixes

- Fixed an issue where the Istiod pod may fail to start due to a timing issue.
- Fixed an issue where the `workloadLabels` field in Istio resources is not properly handled by the controller.
- Fixed an issue where the `istioctl` command fails to connect to the Istio API server when running in a containerized environment.
