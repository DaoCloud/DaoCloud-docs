---
MTPE: windsonsea
Revised: done
Pics: NA
Date: 2023-10-30
---

# Service Mesh Release Notes

This page lists all the Release Notes for each version of Service Mesh, providing convenience for users to learn about the evolution path and feature changes.

## 2024-04-01

### v0.24.0

#### Features

- **Added** API endpoint for cluster node list: `/apis/mspider.io/v3alpha1/clusters/{cluster_name}/nodes`
- **Added** affinity field for mesh gateway
- **Added** support for searching annotations field in traffic lane list API `page.search`
- **Added** support for Istio `1.19.8` and `1.20.4`

#### Fixes

- **Fixed** `container_port` and `protocol` in `ServicePort` section of `ServiceShadow CRD`
- **Fixed** service status in service list API `/apis/mcpc.mspider.io/v3alpha1/meshes/{meshId}/govern/services`.
  After adding the `STATUS_UNSPECIFIED` state for services that are not injected,
  there was an issue with compatibility of the `FailedReason` field.
- **Fixed** inability to display both upstream and downstream capabilities in topology
- **Fixed** format issue with `metrics` in `Telemetry`
- **Fixed** incorrect cluster information in service list and no error message displayed in `serviceShadow` mode
- **Fixed** deletion of `EnvoyFilter` when Istio version is less than `1.20`, causing metric data to be missing
- **Fixed** duplicate metric data and inaccurate client-side metrics
- **Fixed** the need to enable `envoy filter` for custom metric monitoring in proprietary mesh when Istio version is less than `1.20`

## 2024-01-30

### v0.23.0

#### Features

- **Added** Service and workload's grafana dashboard, adding upstream and downstream traffic distribution.
- **Added** Adapt __Istio__ version to __1.18.7__ , __1.19.6__ , and __1.20.2__ .

#### Fixes

- **Fixed** The __Consumer__ service of __Dubbo__ + __Zookeeper__ cannot be recognized as a __Dubbo__ service problem.
- **Fixed** Get a list of valid __Istio__ versions, and filter them based on the cluster version.
- **Fixed** __Istio__ __1.20__ Unable to enable multi-cloud interconnection issue.

## 2023-12-31

### v0.22.0

#### Features

- **Added** Quota of system component resources for custom mesh instances.
- **Added** Larger scale: __S2000P8000__ , __S5000P20000__ mesh instances.
- **Added** Gateway instance upgrade reminder, support one-click upgrade.

#### Improvements

- **Upgraded** Supported mesh versions are __1.18.6__ and __1.19.5__ .
- **Upgraded** The supported mesh version for __1.17__ is __1.17.8-fix-20231226__ , which fixes the previous memory leak issue.

#### Fixes

- **Fixed** The problem of unable to perform hot upgrade for __Sidecar__ under the user __istio-proxy__ .
- **Fixed** Under the dedicated mesh, the version of the mesh is not correctly updated after upgrading the mesh.

## 2023-11-30

### v0.21.0

#### Features

- **Added** support for multi-cloud connectivity in the proprietary mesh.
- **Added** the ability to select and upgrade to new versions of __Istio (1.19.3, 1.18.5, 1.17.6)__ for deploying mesh instances.
- **Added** __VM Agent__ support for health checks and fault recovery of __Istio__ processes.
- **Added** __TrafficLane API__ support for operations via __Annotations__ .

#### Improvements

- **Optimized** the algorithm mechanism for the service list state and diagnostic state to ensure consistency between diagnostic results and status fields.
- **Improved** the automatic discovery strategy for managed mesh services to display any service from any cluster with the `mspider.io/managed` label.

#### Fixes

- **Fixed** a deadlock issue during mesh creation, preventing the premature creation of __Sidecar__ resources before the initialization of mesh resources.
- **Fixed** the issue with transparent traffic flow to ensure correct ingress and egress port permissions.
- **Fixed** excessive detection of __ETCD__ by the mesh, resolving the problem of abnormal mesh status display.
- **Fixed** consistent removal of mesh clusters when removing a cluster, ensuring operational consistency.
- **Fixed** the issue where the __MCPC Controller__ failed to detect changes in __TrafficLane__ resources after running for a long time.
- **Fixed** the simultaneous termination of __pilot-agent__ process when stopping a virtual machine to ensure proper resource release.
- **Fixed** occasional rule failures caused by asynchronous clean-up and installation operations during the startup of a virtual machine.

## 2023-10-30

### v0.20.3

#### Feature

- **Added** support for running __VM Agent__ in containers.
- **Added** support for deleting virtual machine type workloads.
- **Added** customizable namespace scope for edge discovery in the mesh, significantly reducing resource consumption pressure on __Sidecar__ .
- **Added** elastic scaling configuration __auto_scaling__ for the mesh gateway.

#### Improved

- **Improved** traffic topology __Graph__ implementation with optional hiding of idle nodes.
- **Improved** detection of host __glibc__ version during __docker__ mode installation of __vmagent__ .

#### Fixes

- **Fixed** issue where querying the __Graph__ with long namespaces resulted in URL length exceeding the limit while making requests to the __Prometheus__ service.
- **Fixed** incorrect injection status of workloads.
- **Fixed** inaccurate display of resource bindings in workspace interfaces.
- **Fixed** port conflict ( __15090__ ) causing __istio__ to become unavailable in the virtual machine monitoring service.
- **Fixed** asynchronous occurrence of rule faults during virtual machine startup, due to prior cleanup and installation operations, resulting in traffic communication issues.
- **Fixed** __ulimit__ value for the __envoy__ process being too small due to the use of the __su__ command.

## 2023-08-31

### v0.19.0

#### Upgrades

- **Added** __userinfo__ interface to retrieve permissions information for the current user.

    **Note: To obtain accurate permission information, the __mesh_id__ parameter must be provided when accessing the mesh**.

- **Added** support for virtual machines (automatically creates __WorkloadShadow__ ) in __Mcpc Controller__ .
- **Added** service interface for creating virtual machines (VM) within the mesh.
- **Added** script for building and uploading offline installation packages for virtual machines (VM).
- **Added** interface to bind services and generate configurations for virtual machines (VM).
- **Added** __Reporter__ parameter to the routing panel of __Grafana__ .
- **Added** __Mspider__ virtual machine agent controller ( __mspider-vm-agent__ ).
- **Added** __generator__ package, implementing __ComponentAnalyzer__ . Pass in __MeshCluster__ or __GlobalMesh__ to retrieve corresponding component statuses.
- **Improved** upgrade interface for checking mesh availability by adding permission checks.
- **Improved** __reconcileComponentsStatus__ in __gsc-controller__ under mesh-cluster.
- **Upgraded** frontend version to __v0.17.0__ .
- **Upgraded** supported mesh versions to __1.16.6__ , __1.17.5__ , __1.18.2__ .

#### Fixes

- **Fixed** issue with filtering __ServiceEntry__ outside the mesh.
- **Fixed** compatibility problem with regular expression of __workloadId__ when querying virtual machine workload instances (e.g., `{CLUSTER}-vm-{VM_APP}-{VM_IP}-{VM_NETWORK}` ).
- **Fixed** issue where creating east-west gateways during cluster creation would overwrite the default north-south gateway configuration.
- **Fixed** automatic creation of governance policies for virtual machine services and inability to synchronize changes in labels to __WorkloadShadow__ .
- **Fixed** issue where network groups in multi-cloud interconnection couldn't have names starting with a digit.
- **Fixed** loss of custom configuration when updating the mesh.
- **Fixed** null pointer issue in __work-api__ component due to removal of __label__ from __Secret__ .
- **Fixed** failure to delete mesh when system namespaces were included (they are uninstalled during deletion).
- **Fixed** issue where __customMeshConfig__ didn't take effect on __Operator__ .
- **Fixed** mismatch between __Operator__ version and actual installed version of __Istio__ .
- **Fixed** inability to collect metrics in __Mspider__ control plane API Server and Work API Server due to permission issues.
- **Fixed** issue where metrics weren't collected in __Mspider__ control plane and __MCPC Ckube__ components.
- **Fixed** issue where __k8s.pod.name__ field was reported as __unknown__ in __OTEL__ trace data.
- **Fixed** warning alert during the initial execution of virtual machine installation script.

## 2023-07-28

### v0.18.0

#### Upgrades

- **Added** Recommended versions will be included in the __Istio__ version list.
- **Added** Detection condition for joining the interconnection network pool: __CLUSTER_EXIST_NET_POOLS__ .
- **Added** Interface to get the namespace list in a cluster.
- **Added** Support for filtering system namespaces in __filter_system_namespaces__ .
- **Added** Interface to get the list of sidecar-injected workloads in a cluster.
- **Added** New field __graph_type__ in the workload view of the monitoring topology,
  currently supporting __SERVICE_SCOPE__ and __WORKLOAD_SCOPE__ , defaulting to __SERVICE_SCOPE__ .
- **Added** Detection condition for removing network groups: whether they exist in the network interconnection pool ( __NET_EXISTS_NET_POOLS__ ).
- **Added** Support for searching by __PodLabels__ in the sidecar workload list using __page.search__ .
- **Added** Interface to query the list of multi-cluster workloads:
  `/apis/mspider.io/v3alpha1/meshes/{mesh_id}/clusters/-/sidecar-management/workloads`, also supports searching by __PodLabels__ .
- **Added** Design of service diagnosis interface.
- **Added** Implementation of detection condition for removing clusters from the mesh: whether they have joined the interconnection network pool ( __CLUSTER_EXIST_NET_POOLS__ ).
- **Added** Implementation of interface for checking the validity of gateway names in the mesh.
- **Added** Field __filter_system_namespaces__ to the namespace list in a cluster.
- **Added** Field __filter_system_namespaces__ to the list of sidecar-injected workloads in a cluster.
- **Added** Support for workload dimension in monitoring topology.
- **Added** Implementation of service diagnosis interface (with automatic repair for some issues).
- **Added** Detection of diagnostic items requiring manual repair.
- **Added** Implementation of service repair interface.
- **Added** New tag __k8s.pod.name__ in __Trace Tags__ to indicate the name of the __Pod__ .
- **Added** Platform administrators and workspace administrators can manage multi-cloud network interconnections for meshes under their workspace.
- **Upgraded** __Istio api__ to fix the issue where __WasmPlugin__ cannot set priority.
- **Upgraded** __ckube__ to __v1.3.5__ to resolve the issue where the service mesh list might be empty.

#### Fixes

- **Fixed** Inconsistency between __sidecar__ and __sidecarResources__ .
- **Fixed** Disorder of sorting indexes in the workload list.
- **Fixed** __ListClusterNamespace__ interface to support querying namespace information by cluster.
- **Fixed** Issue where globally bound mesh resources may not be displayed internally in the mesh.
- **Fixed** Inability to modify __portName__ for empty port protocols.
- **Fixed** Issue where diagnostic items for __Workload__ were missing __Service__ .
- **Fixed** Permanent failure in synchronization of service configuration sync diagnostics.
- **Fixed** Inaccuracy in audit logs for some batch operation interfaces.
- **Fixed** Unreachable clusters are still attempted to be probed with __livez__ .
- **Fixed** Incorrect status of workloads when namespace injection status changes in dedicated mesh mode.
- **Fixed** Failure in successful synchronization of __leaderelection__ .
- **Fixed** Incorrect total count of __Pods__ in the mesh in some cases.
- **Fixed** Typo in error messages, changing __mot__ to __not__ .
- **Fixed** Inability to repair sidecar injection status for certain services.
- **Fixed** Failure of interface `/apis/mspider.io/v3alpha1/clusters/{name}/components` and
  `/apis/mspider.io/v3alpha1/clusters/{name}` when __mesh_id__ is not passed for non-admin users.
- **Fixed** Name validation of __Istio CRD__ , allowing the first letter of all operation names to be a number.
- **Fixed** Incorrect comment about __label_selectors__ in the __Graph__ interface.
- **Fixed** Lack of message body description for service diagnosis repair interface.
- **Optimized** Description of the __namespaces__ field in the __Istio__ resource interface.
- **Optimized** Detection process of mesh control plane, ignoring control plane clusters.
- **Optimized** Consistency of different permissions for different roles with the latest permission design.
- **Optimized** Permission design, separating multi-cloud network interconnection permission from mesh management.
- **Optimized** Meaning of the `global.high_available` parameter.
- **Optimized** Usage of `CHART.replicas` , changing default value to empty.

## 2023-06-29

### v0.17.0

#### Features

- **Added** `mspider.io/mesh-gateway-name` label specification for defining the mesh gateway name.
- **Added** __injectionStatus__ field to namespace for listing and searching purposes.
- **Added** __label_selectors__ field in topology queries for conditional querying of topology results.
- **Added** __Labels__ and __PodLabels__ fields to sidecar workload information.
- **Added** __Labels__ and __PodLabels__ fields to service workload information.
- **Added** component information (components) and Istio version (meshVersion) fields to cluster information.
- **Added** __include_components__ field to cluster list and mesh management cluster list for selecting whether to display cluster component information, such as Insight and other external components.
- **Added** audit information for all necessary interfaces.
- **Added** ability to clear deployment injection policies.
- **Added** Implemented index search for namespace lists.
- **Added** audit log capability.
- **Added** ability to clear deployment injection policies.
- **Added** Implemented component status in cluster list.
- **Added** `mspider.io/mesh-gateway-name` label specification for defining the gateway name.
- **Added** Implemented automatic service injection capability for __MCPC Controller__ .
- **Added** Ghippo resource reporting functionality, automatically creating and updating __GProductResource__ resources according to specifications.
- **Added** `global.config.enableAutoInitPolicies` configuration for enabling automatic initialization of governance policies for managed services in __MCPC Controller__ .
- **Added** `global.config.enableAutoInjectedSidecar` configuration for enabling automatic injection policies for managed services in __MCPC Controller__ .
- **Added** compatibility testing for various versions of K8s.
- **Optimized** cache to improve the latency issue of querying __Insight Agent__ status in clusters.
- **Optimized** Strengthened detection of conflicting meshes when creating a mesh for managed clusters.
- **Optimized** Ignored updates to name (Name), namespace (Namespace), and labels (Labels) when updating mesh gateways to avoid triggering exceptions.
- **Optimized** Updated synchronization method for Kpanda cluster kubeconfig.
- **Optimized** Created logic for __WorkloadShadow controller watcher__ .
- **Upgraded** Supported querying cluster and cluster component information independently without passing MeshID.
- **Upgraded** go package istio.io/istio to __v0.0.0-20230131034922-50fb2905d9f5__ version.
- **Upgraded** CloudTTY to __v0.5.3__ version.
- **Upgraded** front-end version to __v0.15.0__ .

#### Fixes

- **Fixed** inaccurate audit log description when creating East-West gateway for clusters.
- **Fixed** ineffectiveness of replica count for East-West gateways.
- **Fixed** invalid detection of sidecar removal during mesh deletion.
- **Fixed** inability to filter namespaces in monitoring topology.
- **Fixed** inaccurate error rate data for monitoring topology services.
- **Fixed** returning 404 error when mesh does not exist.
- **Fixed** panic caused by __nil pointer__ in Audit.
- **Fixed** displaying Enum type resource types as numbers in audit logs.
- **Fixed** inconsistency in behavior between GRPC requests with user authentication information and HTTP requests.
- **Fixed** failure to create __Telemetry__ resources during dedicated mesh creation.
- **Fixed** failure to rebuild __RegProxy watcher__ .
- **Fixed** incorrect labeling by __traffic-lane__ plugin, causing traffic lane to not work.
- **Fixed** failure to properly clean up cluster configuration when deleting the mesh.
- **Fixed** abnormal behavior of __MCPC Controller__ when accessing unhealthy clusters.
- **Fixed** inability to remove components during mesh deletion or cluster removal process.
- **Fixed** GlobalMesh and MeshCluster remaining in deletion state and unable to be forcefully deleted.
- **Fixed** incorrect injection status for system namespaces that are not injected by default.
- **Fixed** selection of non-ready Pods when proxying __HostedAPIServer__ , causing the mesh to not become ready.
- **Fixed** failure to delete Telemetry during mesh deletion, which caused the mesh deletion process to fail. This resource is cleaned up during Istio uninstallation or removal of __HostedAPIServer__ , so it does not need to be deleted during the mesh deletion process.
- **Fixed** issue with installing __HostedAPIServer__ on OCP due to permission problems.
- **Fixed** description in Helm chart.

#### Removals

- **Removed** 443 port from service __istiod-[meshID]-hosted-lb__ in managed mesh mode.

## 2023-05-31

### v0.16.1

#### Features

- **Added** Ckube loads resources on demand.
- **Added** IstioResource field: __labels__ and __annotations__ , can update Labels and Annotations.
- **Added** ClusterProvider synchronization implementation in MeshCluster.
- **Added** Definition of the __mspider.io/protected__ label for mesh protection.
- **Added** Sidecar upgrade supports multiple workload capabilities, __SidecarUpgrader__ simultaneously supports __workloadshadow.name__ and __deployment.name__ .
- **Added** Workload type is re-implemented as a string.
- **Added** The __localized_name__ field is added to the workload-related interface to display workload names.
- **Added** Workload injection policy clearing capability
- **Added** Get global configuration interface __/apis/mspider.io/v3alpha1/settings/global-configs__ .
- **Added** __clusterPhase__ field is added to mark the cluster's status (previously marked in the phase field, now separated).
- **Added** __clusterProvider__ field is added to mark the cluster provider.
- **Added** Traffic lane CRD capability implementation.
- **Added** Reg-Proxy component is enabled by default.
- **Added** Implementation of Service selector field output.
- **Added** Solving cross-cluster access problems when Sidecars are not injected by adding a Network label to Namespace.
- **Added** Custom parameter configuration capability for hosted mesh hosted-apiserver. (This parameter only takes effect during installation and does not support updates for the time being), (for more parameters, please refer to helm parameter configuration):
- **Added** Mesh control plane component status
- **Added** The mesh query interface adds the __loadBalancerStatus__ field to describe the actual assigned LB address.
- **Added** Component progress detail interface `/apis/mspider.io/v3alpha1/meshes/{mesh_id}/components-progress`.
- **Added** HPA is added for control plane components.
- **Added** New API definition to get cluster __StorageClass__ .
- **Added** New API definition to get installed components in the cluster (currently supports Insight Agent).
- **Optimization:** Improved user experience for binding/unbinding workspaces.
- **Optimization:** The __workload_kind__ field type in the workload-related interface is optimized from enumeration to __string__ .
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

- Introduced __d2__ as a drawing tool.
- Added a new wasm plugin that adds different headers to requests according to the trace ID.
- Hosted Istiod's LoadBalancer Annotations implementation in mesh configuration.
- Implemented mesh gateway configuration service Annotations.
- Added __load_balancer_annotations__ field to mesh, supporting custom load balancing annotations.
- In __mspider-api__ , manually run the pipeline and set __SYNC_OPENAPI_DOCS__ as the key to trigger the upload of the document site (raise PR).
- When the MCPC Controller perceives that the `mspider.io/managed` label exists in the Service, it will trigger the automatic creation of a governance policy corresponding to the service.
- MCPC Controller multiple workload type support.
- Added health check function, which automatically rebuilds proxy when mesh APIServer fails to connect to prevent PortForward's own logic from being unreliable (may be related to Istio Sidecar).

#### Fixes

- Previously not compatible with __grpcgateway-accept-language__ (equivalent to HTTP's Accept-Language) header, resulting in inability to switch between Chinese and English modes correctly. Compatible with both Accept and Accept-Language modes now.
- When synchronizing OpenAPI, upstream cannot push due to shadow clone code.
- Unable to update Istio resources with __.__ .
- In version 1.17.1, istio-proxy cannot start normally.
- The ingress gateway lacks a name, causing the merge to fail and cannot be deployed.
- The service address cannot be searched.
- Unable to update Istio resources with __.__ .
- Previous controller memory leak issue fixed.
- Add/delete cluster logic now triggers correctly sometimes.
- When global injection is turned on, updating the mesh may cause the istio-operator pod to be injected, causing the mesh creation to fail.
- Fixed a problem that caused the virtual cluster to be synchronized to __Mspider__ and lead to access failure.
- Optimized the controller namespace and service resource processing logic to reduce frequent triggering of workloadShadow resource updates.
- Optimized the problem of frequent acquisition/update of __workloadShadow__ resources and only reconcile some resources that have undergone specific changes.
- Reduce pod changes and constantly update __WorkloadShadow__ .
- Wasm plugin image address wrong spelling in __relok8s__ .
- TrafficLane default repository bug.
- Helm image rendering template optimized; the image structure is split into three parts: `registry/repository:tag` .

#### Removed

- Logic to sync global cluster to mesh removed.
- Deprecated Deployment Controller logic.
- __ui.version__ parameter deprecated, changed to `ui.image.tag` parameter to set the frontend version.

## 2023-03-31

### v0.14.3

#### Features

- Frontend version upgraded to __v0.12.2__ .

#### Fixes

- Unable to update Istio resources with __.__ .
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
- Insight API upgraded to version __v0.14.7__ .
- __Ckube__ supports complex conditional query of labels.
- Helm upgrade time limit removed.

#### Fixes

- The interface does not display when the east-west gateway is not Ready.
- Multicloud interconnection will automatically register the east-west gateway LB IP, which may cause internal network abnormalities (remove the east-west gateway instance label: `topology.istio.io/network` . This label will automatically register the east-west gateway).
- Cluster migration with east-west gateway enabled may cause incorrect service resolution.
- Fixed an issue where the control plane cannot be deployed on a single-node Kubernetes cluster.
- The __istioctl__ installation error caused by the __kubectl__ version mismatch fixed.
- The invalidation of VirtualService cache optimized, reducing the possibility of inconsistent virtual services after deletion.
- Fixed an issue where the __meshconfig-default__ ConfigMap is not properly synced when upgrading from previous versions.
- Fixed the problem that Prometheus is not running when deploying Service Mesh using __istioctl__ .
- Fixed an issue where the Envoy proxy cannot start due to missing __SO_KEEPALIVE__ option in the socket configuration.

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
- The performance of the __WorkloadShadow__ module optimized through reducing unnecessary requests and adding local caching.
- Upgraded the __insight-api__ version to improve stability.

#### Fixes

- Fixed an issue where the Istiod pod is stuck in the "Pending" state when deployed on specific Kubernetes distributions.
- Fixed an issue where VirtualServices cannot be updated due to conflicting port numbers.
- Fixed an issue where injecting a sidecar into a Pod may cause its name to exceed the maximum length allowed by Kubernetes.
- Fixed an issue where the __istioctl__ command fails to connect to the Istio API server when running in a containerized environment.
- Fixed an issue where the Kiali dashboard displays inconsistent traffic data with Prometheus.

## 2023-01-31

### v0.13.0

#### Features

- Multicluster management feature added.
- Support for multicloud interconnection added.
- Service dependency analysis and visualization feature added.
- New __dial__ and __readinessProbe__ options added to endpoint slice.
- Service mesh security audit feature added.
- Istio 1.16.3 support added.
- Support for customizing the Istiod configuration added.

#### Optimization

- Improved the efficiency of MCPC controller synchronization.
- Optimized the performance of Istiod initialization.
- Optimized the __WorkloadShadow__ module to reduce resource consumption.
- Upgraded the __Mspider__ version to improve stability.

#### Deprecated

- Global cluster syncing logic removed.

## 2022-12-31

### v0.12.1

#### Features

- Service mesh visualization feature added.
- Support for exporting metrics to Grafana added.
- Virtual machine mesh support added.
- Istio 1.16.2 support added.
- The __MeshExpansion__ and __SidecarInjectorWebhook__ components now support custom configuration.

#### Optimization

- Improved the performance of the MCPC controller.
- Optimized the handling of expired certificates in the mesh components.
- Upgraded the __insight-api__ version to improve stability.

#### Fixes

- Fixed an issue where the Istiod pod may fail to start due to a timing issue.
- Fixed an issue where the __workloadLabels__ field in Istio resources is not properly handled by the controller.
- Fixed an issue where the __istioctl__ command fails to connect to the Istio API server when running in a containerized environment.

## 2022-11-30

### v0.12.0

#### Features

- Support for multi-tenancy added.
- Istio 1.16.1 support added.
- New __MeshExpansion__ and __SidecarInjectorWebhook__ components added.
- Automatic sidecar injection feature added.
- Support for customizing the Istiod configuration added.

#### Optimization

- Improved the stability and performance of the MCPC controller.
- Upgraded the __insight-api__ version to improve stability.

#### Fixes

- Fixed an issue where the Istiod pod may fail to start due to a timing issue.
- Fixed an issue where the __workloadLabels__ field in Istio resources is not properly handled by the controller.
- Fixed an issue where the __istioctl__ command fails to connect to the Istio API server when running in a containerized environment.
