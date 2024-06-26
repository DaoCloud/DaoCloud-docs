---
MTPE: ModetaNiu
Revised: done
Pics: NA
Date: 2024-05-31
---

# Service Mesh Release Notes

This page lists all the Release Notes for each version of Service Mesh, providing convenience for users to learn about the evolution path and feature changes.

## 2024-05-30

### v0.26.0

#### Features

- **Added** a feature of Istio Analyze.
- **Added** controller for synchronizing Istio resources across work clusters.

#### Fixes

- **Fixed** the absence of default sorting in network grouping list.
- **Fixed** stop() exception in Istio resource synchronization.
- **Fixed** an issue of `Istio analyze` not being able to resolve when all are valid.

## 2024-04-30

### v0.25.0

#### Features

- **Added** built-in mesh alert rules, and observability alert configurations can be directly used.
- **Added** compatibility with `Istio` versions `v1.19.9`,`v1.20.5`, `v1.21.1`.
- **Added** a new field `.status.replicas` to `WorkloadShadow` in `OpenAPI` to record the total number of `Pods` at runtime.

#### Fixes

- **Fixed** an security issue with the low version of `xz` and upgraded `cloudtty` image to version `v0.7.1`.
- **Fixed** an issue of changes to `Pod` not triggering workload status changes in `Ambient` mode.
- **Fixed** the issue of incorrect display of topology nodes due to lack of permissions.

## 2024-04-01

### v0.24.1

#### Features

- **Added** cluster node list API `/apis/mspider.io/v3alpha1/clusters/{cluster_name}/nodes`.
- **Added** mesh gateway affinity field `affinity`.
- **Added** traffic swim lane list API `page.search` now supports `annotations` field search.
- **Added** compatibility with `Istio` versions `v1.19.8`, `v1.20.4`.

#### Fixes

- **Fixed** an issue where the `ServicePort` section in `ServiceShadow CRD` now includes `container_port` and `protocol`.
- **Fixed** an issue of service status `STATUS_UNSPECIFIED` and `FailedReasn` not being version-compatible in the API `/apis/mcpc.mspider.io/v3alpha1/meshes/{meshId}/govern/services`.
- **Fixed** an issue with topology not displaying upstream and downstream capabilities simultaneously.
- **Fixed** `Telemetry` metrics format issues.
- **Fixed** an issue where service list cluster information was incorrect and error messages were not displayed in `serviceShadow` mode.
- **Fixed** an issue where `EnvoyFilter` was being deleted in `Istio` versions lower than `1.20`, causing no data for metrics.
- **Fixed** double metric data issues and inaccurate client metrics.
- **Fixed** an issue where `envoy filter` is needed for custom metric monitoring in proprietary meshes with `Istio` version lower than `1.20`.

### 2024-01-30

#### v0.23.0

#### Features

- **Added** monitoring dashboards for service and workload monitoring panels, including traffic distribution for upstream and downstream.
- **Added** compatibility with `Istio` versions `v1.18.7`, `v1.19.6`, `v1.20.2`.

#### Fixes

- **Fixed** an issue where `Consumer` services could not be identified as `Dubbo` services when using `Dubbo` and `Zookeeper` simultaneously.
- **Fixed** an issue with retrieval of valid `Istio` version list not being filtered based on cluster version.
- **Fixed** an issue with inability to enable multi-cloud connectivity with `Istio` `v1.20`.

## 2023-12-31

### v0.22.0

#### Features

- **Added** quota of system component resources for custom mesh instances.
- **Added** larger scale: **S2000P8000** , **S5000P20000** mesh instances.
- **Added** gateway instance upgrade reminder, supporting one-click upgrade.

#### Optimization

- **Upgraded** supported mesh versions are **1.18.6** and **1.19.5** .
- **Upgraded** the supported mesh version for **1.17** is **1.17.8-fix-20231226** , which fixes the previous memory leak issue.

#### Fixes

- **Fixed** an issue where hot upgrade for **Sidecar** under the user **istio-proxy** was not possible.
- **Fixed** an issue where the version of the dedicated mesh was not correctly updated after upgrading the mesh.

## 2023-11-30

### v0.21.0

#### Features

- **Added** support for multi-cloud connectivity in the proprietary mesh.
- **Added** the ability to select and upgrade to new versions of **Istio (1.19.3, 1.18.5, 1.17.6)** for deploying mesh instances.
- **Added** **VM Agent** support for health checks and fault recovery of **Istio** processes.
- **Added** **TrafficLane API** support for operations via **Annotations** .

#### Optimization

- **Optimized** the algorithm mechanism for the service list state and diagnostic state to ensure consistency between diagnostic results and status fields.
- **Optimized** the automatic discovery strategy for hosted mesh services to display any service from any cluster with the `mspider.io/managed` label.

#### Fixes

- **Fixed** a deadlock issue during mesh creation, preventing the premature creation of **Sidecar** resources before the initialization of mesh resources.
- **Fixed** an issue with transparent traffic flow to ensure correct ingress and egress port permissions.
- **Fixed** excessive detection of **ETCD** by the mesh, resolving the problem of abnormal mesh status display.
- **Fixed** an issue with consistent removal of mesh clusters when removing a cluster, ensuring operational consistency.
- **Fixed** an issue where the **MCPC Controller** failed to detect changes in **TrafficLane** resources after running for a long time.
- **Fixed** an issue with the simultaneous termination of **pilot-agent** process when stopping a virtual machine to ensure proper resource release.
- **Fixed** occasional rule failures caused by asynchronous clean-up and installation operations during the startup of a virtual machine.

## 2023-10-30

### v0.20.3

#### Features

- **Added** support for running **VM Agent** in containers.
- **Added** support for deleting virtual machine type workloads.
- **Added** customizable namespace scope for edge discovery in the mesh, significantly reducing resource consumption pressure on **Sidecar** .
- **Added** elastic scaling configuration **auto_scaling** for the mesh gateway.

#### Optimization

- **Optimized** traffic topology **Graph** implementation with optional hiding of idle nodes.
- **Optimized** detection of host **glibc** version during **docker** mode installation of **vmagent** .

#### Fixes

- **Fixed** an issue where querying the **Graph** with long namespaces resulted in URL length exceeding the limit while making requests to the **Prometheus** service.
- **Fixed** an issue with incorrect injection status of workloads.
- **Fixed** an issue with inaccurate display of resource bindings in workspace interfaces.
- **Fixed** a port conflict ( **15090** ) causing **istio** to become unavailable in the virtual machine monitoring service.
- **Fixed** an issue with asynchronous occurrence of rule faults during virtual machine startup, due to prior cleanup and installation operations, resulting in traffic communication issues.
- **Fixed** an issue with **ulimit** value for the **envoy** process being too small due to the use of the **su** command.

## 2023-08-31

### v0.19.0

#### Features

- **Added** **userinfo** interface to retrieve permissions information for the current user.

    **Note: To obtain accurate permission information, the **mesh_id** parameter must be provided when accessing the mesh**.

- **Added** support for virtual machines (automatically creates **WorkloadShadow** ) in **Mcpc Controller** .
- **Added** service interface for creating virtual machines (VM) within the mesh.
- **Added** script for building and uploading offline installation packages for virtual machines (VM).
- **Added** interface to bind services and generate configurations for virtual machines (VM).
- **Added** **Reporter** parameter to the routing panel of **Grafana** .
- **Added** **Mspider** virtual machine agent controller ( **mspider-vm-agent** ).
- **Added** **generator** package, implementing **ComponentAnalyzer** . Pass in **MeshCluster** or **GlobalMesh** to retrieve corresponding component statuses.
- **Optimized** upgrade interface for checking mesh availability by adding permission checks.
- **Optimized** **reconcileComponentsStatus** in **gsc-controller** under mesh-cluster.
- **Upgraded** frontend version to **v0.17.0** .
- **Upgraded** supported mesh versions to **1.16.6** , **1.17.5** , **1.18.2** .

#### Fixes

- **Fixed** an issue with filtering **ServiceEntry** outside the mesh.
- **Fixed** a compatibility issue with regular expression of **workloadId** when querying virtual machine workload instances (e.g., `{CLUSTER}-vm-{VM_APP}-{VM_IP}-{VM_NETWORK}`).
- **Fixed** an issue where creating east-west gateways during cluster creation would overwrite the default north-south gateway configuration.
- **Fixed** an issue with automatic creation of governance policies for virtual machine services and inability to synchronize changes in labels to **WorkloadShadow**.
- **Fixed** an issue where network groups in multi-cloud interconnection couldn't have names starting with a digit.
- **Fixed** loss of custom configuration when updating the mesh.
- **Fixed** a null pointer issue in `work-api` component due to removal of **label** from **Secret**.
- **Fixed** failure to delete mesh when system namespaces were included (they are uninstalled during deletion).
- **Fixed** an issue where **customMeshConfig** didn't take effect on **Operator**.
- **Fixed** a mismatch between **Operator** version and actual installed version of **Istio**.
- **Fixed** an inability to collect metrics in **Mspider** control plane API Server and Work API Server due to permission issues.
- **Fixed** an issue where metrics weren't collected in **Mspider** control plane and **MCPC Ckube** components.
- **Fixed** an issue where `k8s.pod.name` field was reported as **unknown** in **OTEL** trace data.
- **Fixed** a warning alert during the initial execution of virtual machine installation script.

## 2023-07-28

### v0.18.0

#### Features

- **Added** recommended versions will be included in the **Istio** version list.
- **Added** detection condition for joining the interconnection network pool: **CLUSTER_EXIST_NET_POOLS** .
- **Added** interface to get the namespace list in a cluster.
- **Added** support for filtering system namespaces in **filter_system_namespaces** .
- **Added** interface to get the list of sidecar-injected workloads in a cluster.
- **Added** new field **graph_type** in the workload view of the monitoring topology,
  currently supporting **SERVICE_SCOPE** and **WORKLOAD_SCOPE** , defaulting to **SERVICE_SCOPE** .
- **Added** detection condition for removing network groups: whether they exist in the network interconnection pool ( **NET_EXISTS_NET_POOLS** ).
- **Added** support for searching by **PodLabels** in the sidecar workload list using **page.search** .
- **Added** interface to query the list of multi-cluster workloads:
  `/apis/mspider.io/v3alpha1/meshes/{mesh_id}/clusters/-/sidecar-management/workloads`, also supporting searching by **PodLabels** .
- **Added** design of service diagnosis interface.
- **Added** implementation of detection condition for removing clusters from the mesh: whether they have joined the interconnection network pool ( **CLUSTER_EXIST_NET_POOLS** ).
- **Added** implementation of interface for checking the validity of gateway names in the mesh.
- **Added** field **filter_system_namespaces** to the namespace list in a cluster.
- **Added** field **filter_system_namespaces** to the list of sidecar-injected workloads in a cluster.
- **Added** support for workload dimension in monitoring topology.
- **Added** implementation of service diagnosis interface (with automatic repair for some issues).
- **Added** detection of diagnostic items requiring manual repair.
- **Added** implementation of service repair interface.
- **Added** new tag **k8s.pod.name** in **Trace Tags** to indicate the name of the **Pod** .
- **Added** platform administrators and workspace administrators can manage multi-cloud network interconnections for meshes under their workspace.
- **Upgraded** **Istio api** to fix the issue where **WasmPlugin** cannot set priority.
- **Upgraded** **ckube** to **v1.3.5** to resolve the issue where the service mesh list might be empty.

#### Fixes

- **Fixed** an issue of inconsistency between **sidecar** and **sidecarResources**.
- **Fixed** an issue with disorder of sorting indexes in the workload list.
- **Fixed** an issue with the **ListClusterNamespace** interface to support querying namespace information by cluster.
- **Fixed** an issue where globally bound mesh resources may not be displayed internally in the mesh.
- **Fixed** an issue of inability to modify **portName** for empty port protocols.
- **Fixed** an issue where diagnostic items for **Workload** were missing **Service**.
- **Fixed** an issue of permanent failure in synchronization of service configuration sync diagnostics.
- **Fixed** an issue with inaccuracy in audit logs for some batch operation interfaces.
- **Fixed** an issue where unreachable clusters are still attempted to be probed with **livez**.
- **Fixed** an issue with incorrect status of workloads when namespace injection status changes in dedicated mesh mode.
- **Fixed** an issue of failure in successful synchronization of **leaderelection**.
- **Fixed** an issue with incorrect total count of **Pods** in the mesh in some cases.
- **Fixed** a typo in error messages, changing **mot** to **not**.
- **Fixed** an issue of inability to repair sidecar injection status for certain services.
- **Fixed** an issue of failure of interface `/apis/mspider.io/v3alpha1/clusters/{name}/components` and `/apis/mspider.io/v3alpha1/clusters/{name}` when `mesh_id` is not passed for non-admin users.
- **Fixed** an issue with name validation of **Istio CRD**, allowing the first letter of all operation names to be a number.
- **Fixed** an issue with incorrect comment about **label_selectors** in the **Graph** interface.
- **Fixed** a lack of message body description for service diagnosis repair interface.
- **Optimized** description of the **namespaces** field in the **Istio** resource interface.
- **Optimized** detection process of mesh control plane, ignoring control plane clusters.
- **Optimized** consistency of different permissions for different roles with the latest permission design.
- **Optimized** permission design, separating multi-cloud network interconnection permission from mesh management.
- **Optimized** meaning of the `global.high_available` parameter.
- **Optimized** usage of `CHART.replicas` , changing default value to empty.

## 2023-06-29

### v0.17.0

#### Features

- **Added** `mspider.io/mesh-gateway-name` label specification for defining the mesh gateway name.
- **Added** **injectionStatus** field to namespace for listing and searching purposes.
- **Added** **label_selectors** field in topology queries for conditional querying of topology results.
- **Added** **Labels** and **PodLabels** fields to sidecar workload information.
- **Added** **Labels** and **PodLabels** fields to service workload information.
- **Added** component information (components) and Istio version (meshVersion) fields to cluster information.
- **Added** **include_components** field to cluster list and mesh management cluster list for selecting whether to display cluster component information, such as Insight and other external components.
- **Added** audit information for all necessary interfaces.
- **Added** ability to clear deployment injection policies.
- **Added** Implemented index search for namespace lists.
- **Added** audit log capability.
- **Added** ability to clear deployment injection policies.
- **Added** Implemented component status in cluster list.
- **Added** `mspider.io/mesh-gateway-name` label specification for defining the gateway name.
- **Added** Implemented automatic service injection capability for **MCPC Controller** .
- **Added** Ghippo resource reporting functionality, automatically creating and updating **GProductResource** resources according to specifications.
- **Added** `global.config.enableAutoInitPolicies` configuration for enabling automatic initialization of governance policies for managed services in **MCPC Controller** .
- **Added** `global.config.enableAutoInjectedSidecar` configuration for enabling automatic injection policies for managed services in **MCPC Controller** .
- **Added** compatibility testing for various versions of K8s.
- **Optimized** cache to improve the latency issue of querying **Insight Agent** status in clusters.
- **Optimized** strengthened detection of conflicting meshes when creating a mesh for managed clusters.
- **Optimized** ignored updates to name (Name), namespace (Namespace), and labels (Labels) when updating mesh gateways to avoid triggering exceptions.
- **Optimized** updated synchronization method for Kpanda cluster kubeconfig.
- **Optimized** created logic for **WorkloadShadow controller watcher** .
- **Upgraded** supported querying cluster and cluster component information independently without passing MeshID.
- **Upgraded** go package istio.io/istio to **v0.0.0-20230131034922-50fb2905d9f5** version.
- **Upgraded** **CloudTTY** to **v0.5.3** version.
- **Upgraded** front-end version to **v0.15.0** .

#### Fixes

- **Fixed** an issue with inaccurate audit log description when creating East-West gateway for clusters.
- **Fixed** an issue with ineffectiveness of replica count for East-West gateways.
- **Fixed** an issue with invalid detection of sidecar removal during mesh deletion.
- **Fixed** an issue with inability to filter namespaces in monitoring topology.
- **Fixed** an issue with inaccurate error rate data for monitoring topology services.
- **Fixed** an issue with returning 404 error when mesh does not exist.
- **Fixed** an issue with panic caused by **nil pointer** in Audit.
- **Fixed** an issue with displaying Enum type resource types as numbers in audit logs.
- **Fixed** an issue with inconsistency in behavior between GRPC requests with user authentication information and HTTP requests.
- **Fixed** an issue with failure to create **Telemetry** resources during dedicated mesh creation.
- **Fixed** an issue with failure to rebuild **RegProxy watcher**.
- **Fixed** an issue with incorrect labeling by **traffic-lane** plugin, causing traffic lane to not work.
- **Fixed** an issue with failure to properly clean up cluster configuration when deleting the mesh.
- **Fixed** abnormal behavior of **MCPC Controller** when accessing unhealthy clusters.
- **Fixed** an issue with inability to remove components during mesh deletion or cluster removal process.
- **Fixed** an issue with GlobalMesh and MeshCluster remaining in deletion state and unable to be forcefully deleted.
- **Fixed** an issue with incorrect injection status for system namespaces that are not injected by default.
- **Fixed** an issue with selection of non-ready Pods when proxying **HostedAPIServer**, causing the mesh to not become ready.
- **Fixed** an issue with failure to delete Telemetry during mesh deletion, which caused the mesh deletion process to fail. This resource is cleaned up during Istio uninstallation or removal of **HostedAPIServer**, so it does not need to be deleted during the mesh deletion process.
- **Fixed** an issue with installing **HostedAPIServer** on OCP due to permission problems.
- **Fixed** an issue with description in Helm chart.

#### Removals

- **Removed** 443 port from service **istiod-[meshID]-hosted-lb** in hosted mesh mode.

## 2023-05-31

### v0.16.1

#### Features

- **Added** Ckube loads resources on demand.
- **Added** IstioResource field: **labels** and **annotations** , able to update Labels and Annotations.
- **Added** ClusterProvider synchronization implementation in MeshCluster.
- **Added** definition of the **mspider.io/protected** label for mesh protection.
- **Added**  multiple workload capabilities to sidecars, and **SidecarUpgrader** simultaneously supporting **workloadshadow.name** and **deployment.name** .
- **Added** workload type re-implemented as a string.
- **Added** the **localized_name** field to the workload-related interface to display workload names.
- **Added** workload injection policy clearing capability.
- **Added** global configuration interface **/apis/mspider.io/v3alpha1/settings/global-configs** .
- **Added** **clusterPhase** field to mark the cluster's status (previously marked in the phase field, now separated).
- **Added** **clusterProvider** field to mark the cluster provider.
- **Added** traffic lane CRD capability implementation.
- **Added** Reg-Proxy component by default.
- **Added** a feature of Service selector field output.
- **Added** a Network label to Namespace to solve cross-cluster access problems when Sidecars are not injected.
- **Added** custom parameter configuration capability for hosted mesh hosted-apiserver. (This parameter only takes effect during installation and does not support updates for the time being), (for more parameters, please refer to helm parameter configuration):
- **Added** mesh control plane component status
- **Added** the **loadBalancerStatus** field to the mesh query interface to describe the actual assigned LB address.
- **Added** component progress detail interface `/apis/mspider.io/v3alpha1/meshes/{mesh_id}/components-progress`.
- **Added** HPA is added for control plane components.
- **Added** new API definition to get cluster **StorageClass** .
- **Added** new API definition to get installed components in the cluster (currently supports Insight Agent).
- **Optimized** user experience for binding/unbinding workspaces.
- **Optimized** the **workload_kind** field type in the workload-related interface from enumeration to **string** .
- **Optimized** version detection of the control plane cluster to be included along with the working cluster when hosting a mesh .
- **Upgrade** CloudTTY to version **0.5.3** .
- **Upgrade** the creation logic of the WorkloadShadow controller watcher .

#### Fixes

- **Fixed** an issue with the description information in the **helm chart**.
- **Fixed** an issue where the RegProxy watcher was not rebuilt.
- **Fixed** an issue where the **traffic-lane** plugin incorrectly labeled traffic, causing the traffic lane to not work.
- **Fixed** an issue where components could not be properly removed during mesh deletion or cluster removal.
- **Fixed** an issue where a 404 error should be returned when the mesh does not exist.
- **Fixed** an issue with CloudShell permissions.
- **Fixed** an issue where MeshCluster Status RemotePilotAddress invalid data was not cleared promptly.
- **Fixed** an issue where MeshCluster could not be deleted.
- **Fixed** an issue with insufficient content in FailedReason of TrafficLane.
- **Fixed** a missing action field in TrafficLaneActionsRequest.
- **Fixed** an issue where the mesh list could not be displayed when there were unhealthy clusters.
- **Fixed** an issue with incorrect number of effectively injected instances when an instance is abnormal.
- **Fixed** an issue where WasmPlugin could not create multiple instances when a service was selected by multiple lanes.
- **Fixed** an issue where the service label may have residual old workloads.
- **Fixed** an issue where the service list could not obtain the effective number of workloads, and the type parsing error of Dynamic ReadyReplicas.
- **Fixed** an issue where the changed status of a workload could not be synchronized to the corresponding Service.
- **Fixed** an issue with checking the status of a cluster that is not connected to the mesh.
- **Fixed** an issue where cluster status was not searchable.
- **Fixed** an issue where the mesh could not remove the cluster when there was no sidecar.
- **Fixed** an issue where the regular expression for mesh name did not allow numbers to start.
- **Fixed** an issue where mesh status display was incorrect, and status was sometimes displayed as normal when there was no sidecar.
- **Fixed** an issue where the automatic injection template of the mesh was not effective.
- **Fixed** an issue where non-admin users could not obtain traffic topology due to the lack of default values in the cluster.
- **Fixed** a null pointer exception in the automatic injection service policy.

## 2023-04-27

### v0.15.0

#### Features

- **Added** the introduction of d2 as a drawing tool.
- **Added** a new wasm plugin to add different headers to requests based on the trace id.
- **Added** a feature of LoadBalancer Annotations for managing Istiod in mesh configuration.
- **Added** a feature of service Annotations for mesh gateway configuration.
- **Added** a new mesh field load_balancer_annotations to support custom LoadBalancer Annotations.
- **Added** the ability to manually execute a pipeline in mspider-api by setting SYNC_OPENAPI_DOCS as the key, which triggers the upload of documentation (submit PR).
- **Added** the functionality in MCPC Controller to automatically create governance policies for services when it detects the mspider.io/managed label.
- **Added** support for multiple workload types in MCPC Controller.
- **Added** a health check feature that automatically rebuilds an APIServer proxy when it becomes unreachable, preventing PortForward's own logic from being unreliable (possibly related to Istio Sidecar).
- **Optimized** the controller namespace and service resource handling logic to reduce frequent workloadShadow resource updates.
- **Optimized** the issue of frequent fetching/updating of workloadShadow resources, now reconciling only for resources that have undergone specific changes.
- **Optimized** to reduce pod changes constantly updating WorkloadShadow.
- **Optimized** the Helm image rendering template. The image structure is now split into three parts: registry/repository:tag.

#### Fixes

- **Fixed** an issue where it was not compatible with the grpcgateway-accept-language header (equivalent to HTTP's Accept-Language), resulting in the inability to switch between Chinese and English modes correctly. It is now compatible with both Accept and Accept-Language modes.
- **Fixed** an issue where upstream could not push due to shadow clone code when synchronizing OpenAPI.
- **Fixed** an issue where Istio resources with **.** could not be updated.
- **Fixed** an issue where istio-proxy could not start normally in version 1.17.1.
- **Fixed** an issue where the ingress gateway lacked a name, causing the merge to fail and preventing deployment.
- **Fixed** an issue where the service address could not be searched.
- **Fixed** an issue where Istio resources with **.** could not be updated.
- **Fixed** a previous issue with controller memory leak.
- **Fixed** an issue where add/delete cluster logic sometimes did not trigger correctly.
- **Fixed** an issue where istio-system might be mistakenly deleted in managed mode.
- **Fixed** an issue where the ingress gateway lacked a name, causing the merge to fail and preventing deployment.
- **Fixed** an issue where, when global injection is turned on, updating the mesh may cause the istio-operator pod to be injected, leading to mesh creation failure.
- **Fixed** an issue where the service and WorkloadShadow association did not have a cleanup logic, causing services to be incorrectly bound to workloads.
- **Fixed** an issue that caused the virtual cluster to be synchronized to Mspider, leading to access failure.
- **Fixed** a typo in the wasm plugin image address in relok8s.
- **Fixed** the default repository error in TrafficLane.

#### Removals

- **Removed** the logic for synchronizing global clusters to the mesh.
- **Deprecated** the logic of the Deployment Controller.
- **Deprecated** ui.version parameter, replaced by the ui.image.tag parameter to set the front-end version.

## 2023-03-31

### v0.14.3

#### Features

- Frontend version upgraded to **v0.12.2** .

#### Fixes

- **Fixed** an issue where Istio resources with **.** could not be updated.
- **Fixed** an issue where istio-proxy could not start normally in version 1.17.1.
- **Fixed** an issue where the ingress gateway lacked a name, causing the merge to fail and preventing deployment.

## 2023-03-30

### v0.14.0

#### Features

- **Added** CloudShell related API definitions.
- **Added** implementation for updating service labels.
- **Added** services list and details now return labels.
- **Added** CloudShell related implementations.
- **Added** support for querying service labels in the service list.
- **Added** a new API for updating service labels.
- **Added** support for istio 1.17.1.
- **Added** a new high-availability solution for etcd.
- **Added** a scenario-based testing framework for testing scenario-based functions.
- **Added** automatic adjustment of component resource configurations when selecting different mesh scales.
- **Added** custom role implementation, supporting the creation, updating, deletion, binding, and unbinding of custom roles.

#### Optimization

- **Optimized** the mcpc controller startup logic to avoid situations where work clusters are not correctly registered.
- **Optimized** the WorkloadShadow cleanup logic to be triggered by events instead of on a schedule; it triggers on controller startup, detection of changes in work clusters, or changes in WorkloadShadow.
- **Optimized** the mcpc controller startup logic to avoid situations where work clusters are not correctly registered.
- **Upgraded** the Insight API to version v0.14.7.
- **Upgraded** ckube to support complex condition queries for labels.
- **Removed** the time limit for Helm upgrades.

#### Fixes

- **Fixed** an issue where the interface did not display anything when the East-West gateway was not ready.
- **Fixed** an issue where multi-cloud interconnection would automatically register the East-West gateway LB IP, potentially causing internal network issues (removed the `topology.istio.io/network` label from the East-West gateway instance, which would otherwise automatically register the East-West gateway).
- **Fixed** an issue with migrating clusters that have East-West gateways, where the instance's label could not be modified (if needed, the component has to be deleted and recreated).
- **Fixed** an issue where binding a Mesh to a workspace service would fail (displaying success in the UI).
- **Fixed** an issue where detached namespaces existed in the virtual cluster due to anomalies, adding self-check and cleanup behavior on mcpc-controller startup.
- **Fixed** an issue where updating the mesh via the controller caused the API to fail to deliver mesh configurations.
- **Fixed** an issue where the TargetPort of ServicePort was not set correctly when creating a hosted mesh.
- **Fixed** an issue with `GlobalMesh.Status.MeshVersion` being incorrectly overwritten.
- **Fixed** an issue where mcpc-controller could not enable debug mode.
- **Fixed** an issue where mcpc-controller could not trigger cluster deletion events.
- **Fixed** an issue where deleting a Mesh and recreating a Mesh with the same name would cause the Mesh to fail to create properly (hosted proxy could not update correctly).
- **Fixed** an issue where mcpc controller did not correctly modify the service of istiod-remote in some cases.

## 2023-02-28

### v0.13.2

#### Features

- **Added** multi-cloud network interconnection management and related interfaces.
- **Added** enhanced global configuration capabilities for meshes (mesh system configuration, global traffic governance capabilities, global sidecar injection settings).
- **Added** support for zookeeper proxy.

#### Optimization

- **Optimized** the Namespace controller by adding a cache to reduce redundant Get requests when there are too many namespaces in the cluster.
- **Optimized** to reduce the log output of ckube in normal mode.

#### Fixes

- **Fixed** mesh-related logic errors caused by removing clusters from the container management platform.
- **Fixed** an issue where RegProxy injected Sidecar would cause Nacos to fail to register.
- **Fixed** an issue with incorrect recognition of Spring Cloud services.
- **Fixed** an issue where the Cluster status was not synchronized with the container management platform.
- **Fixed** an issue where the traffic passthrough policy - IP segment configuration did not take effect.
- **Fixed** an issue where the traffic passthrough policy - traffic passthrough policy could not be deleted.
- **Fixed** an issue where errors were returned when fetching mesh configurations due to non-existent configuration paths. 

## 2023-01-31

### v0.13.0

#### Features

- **Added** multicluster management feature.
- **Added** Support for multicloud interconnection.
- **Added** service dependency analysis and visualization feature.
- **Added** new **dial** and **readinessProbe** options to endpoint slice.
- **Added** service mesh security audit feature.
- **Added** Istio 1.16.3 support.
- **Added** support for customizing the Istiod configuration .

#### Optimization

- **Optimized** the efficiency of MCPC controller synchronization.
- **Optimized** the performance of Istiod initialization.
- **Optimized** the **WorkloadShadow** module to reduce resource consumption.
- **Optimized** the **Mspider** version to improve stability.

#### Removals

- **Removed** Global cluster syncing logic.

## 2022-12-31

### v0.12.1

#### Features

- **Added** service mesh visualization feature.
- **Added** support for exporting metrics to Grafana.
- **Added** virtual machine mesh support.
- **Added** Istio 1.16.2 support.
- **Added** the **MeshExpansion** and **SidecarInjectorWebhook** components now support custom configuration.

#### Optimization

- **Optimized** the performance of the MCPC controller.
- **Optimized** the handling of expired certificates in the mesh components.
- **Optimized** the **insight-api** version to improve stability.

#### Fixes

- **Fixed** an issue where the Istiod pod may fail to start due to a timing issue.
- **Fixed** an issue where the **workloadLabels** field in Istio resources is not properly handled by the controller.
- **Fixed** an issue where the **istioctl** command fails to connect to the Istio API server when running in a containerized environment.

## 2022-11-30

### v0.12.0

#### Features

- **Added** support for multi-tenancy.
- **Added** Istio 1.16.1 support.
- **Added** new **MeshExpansion** and **SidecarInjectorWebhook** components.
- **Added** automatic sidecar injection feature.
- **Added** support for customizing the Istiod configuration.

#### Optimization

- **Optimized** the stability and performance of the MCPC controller.
- **Optimized** the **insight-api** version to improve stability.

#### Fixes

- **Fixed** an issue where the Istiod pod may fail to start due to a timing issue.
- **Fixed** an issue where the **workloadLabels** field in Istio resources is not properly handled by the controller.
- **Fixed** an issue where the **istioctl** command fails to connect to the Istio API server when running in a containerized environment.
