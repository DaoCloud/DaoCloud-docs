---
MTPE: ModetaNiu
Revised: done
Pics: NA
Date: 2025-03-18
---

# Service Mesh Release Notes

This page lists all the Release Notes for each version of Service Mesh,
providing convenience for users to learn about the evolution path and feature changes.

*[mspider]: Internal development codename for DaoCloud Service Mesh

## 2025-10-31

### v0.37.0

- **Added** support for Gateway API  
- **Fixed** deprecated `targetPort` field in PodMonitor, replaced with the recommended `portNumber` field to eliminate Prometheus Operator warning logs. Affected PodMonitor resources:  
  - mspider-system/mspider-ckube-metrics  
  - mspider-system/mspider-ckube-remote-metrics  
- **Fixed** strict validation issue with Istio gateway Helm parameters  
- **Upgraded** Ckube to v1.3.11 to fix GCC startup issue  
- **Upgraded** Ckube to v1.3.10 to fix “cluster resource not found” issue caused by watcher restarts  
- **Upgraded** hosted_apiserver to v0.0.14  
- **Upgraded** frontend version to v0.35.0  
- **Upgraded** pluma-operator to v0.1.3

## 2025-08-08

### v0.36.0

- **Added** support for Istio v1.25.3 and v1.24.6.
- **Fixed** an issue where the mesh console had no permission.
- **Fixed** an issue where mesh gateways could not be created in Istio v1.23 using the `pluma-operator`.
- **Fixed** an issue where Istio versions greater than v1.23 incorrectly reported `istio-operator`
  as missing, corrected to `pluma-operator`.
- **Fixed** an issue where the same user could not open multiple consoles.
- **Fixed** an issue where querying service versions failed when the service name length was close to 63 characters.
- **Fixed** an issue where standardized Peer Metadata Attributes in Istio v1.24 caused missing metric data.
- **Fixed** an issue where Istio v1.23+ meshes could not be installed in offline environments.
- **Upgraded** `cloudtty` to v0.8.7.

!!! note

    Starting with Istio v1.23, control plane components are managed by Pluma Operator.
    You must specify the corresponding Istio chart repository address.
    The system comes with a built-in Addon repository address, and MSpider supports this mechanism since v0.36+.

    To configure a custom repository, add the mesh installation parameter to the corresponding GlobalMesh CRD:  

    ```yaml
    global.istioRepo: https://release.daocloud.io/chartrepo/addon
    ```

    ![yaml snippet](../images/GlobalMeshCRD.png)

## 2025-05-09

### v0.35.0

- **Added** support for Istio v1.22 and v1.23, and Kubernetes v1.32.
- **Fixed** the description of the MSpider Helm Chart name.
- **Fixed** an issue where the actual access address of the mesh control plane was not displayed.
- **Fixed** an issue where workspace mesh resource bindings were cleared due to unsynchronized binding information at startup.
- **Fixed** an issue where retrieving cluster node selectors incorrectly required cluster-level permissions.
- **Fixed** an issue where a user bound to multiple roles caused permission errors.
- **Fixed** custom Istio v1.24.5-mspider deployments to retain the managed mesh architecture (since community Istio v1.24 removed `istio-remote`).
- **Fixed** a memory leak in the `traffic-lane` plugin caused by the wasm queue mechanism.
- **Optimized** Istio upgrades to v1.24.5, v1.23.6, and v1.22.8.
- **Optimized** audit log event naming standardization.

!!! note

    Istio v1.23 is set as the default recommended version.
    See [Upgrade Notes](#notes-on-upgrading-service-mesh-to-istio-123).

## 2025-01-25

### v0.34.0

- **Fixed** an issue where the mesh gateway load balancing IP could not be queried.
- **Fixed** a problem where the installation parameters for the Ingress gateway were confused when both managed cluster and workload cluster roles were present.
- **Updated** Istio v1.23 set as an experimental version, with 1.22 being the default recommended version.

## Notes on Upgrading Service Mesh to Istio 1.23+

!!! note

    Affected Range:
    If the Istio version is lower than 1.23 and a mesh gateway instance has been created, you need to upgrade to Istio 1.23.
    If Istio is lower than 1.23 but no mesh gateway instance has been created, this upgrade will not affect you.

### Background

The Istio community announced the deprecation of the In-Cluster Operator in [1.23](https://istio.io/latest/blog/2024/in-cluster-operator-deprecation-announcement/) and it will be fully deprecated in 1.24.
DCE 5.0's service mesh uses the Istio In-Cluster Operator, so to ensure that versions 1.23 and later of Istio can be installed correctly, we have developed and open-sourced the [Pluma Operator](https://github.com/pluma-tools/pluma-operator).
When the Istio version in the service mesh is 1.23 or higher, the Operator will automatically switch from the Istio In-Cluster Operator to the Pluma Operator.

### Upgrade Changes

One major change with replacing the In-Cluster Operator with the Pluma Operator is that Istio component installations will shift from being managed by the Operator to being installed using Helm standard methods. This means that certain resources will undergo changes during the upgrade.

### Component Update Details

After upgrading to version 1.23, the following components will be affected:

- The `mspider` and `istio` components under `istio-system`.
- The mesh gateway installed through Mspider.

### Mesh Gateway Upgrade Procedure

!!! note

    Failure to perform the current upgrade will result in a disruption of north-south traffic.

The most critical part of the upgrade is the data plane traffic, specifically the gateway, as the Helm standard installation brings changes to the templates. The gateway's labels change, which can prevent Pluma from properly upgrading the gateway. Thus, it is necessary to handle this in advance.

Since Kubernetes does not allow updating `Deployment` selectorLabels, it is necessary to delete and recreate the labels:

1. Create a new gateway and customize the `app` and `istio` labels:

    ```yaml
    app: $gateway_name
    Istio: $gateway_name
    ```

2. Modify the corresponding Gateway Policy CRD to bind the new gateway and migrate traffic to the new gateway.

3. Delete the old gateway that does not conform to the upgraded template.

## 2024-12-30

### v0.33.0

- **Fixed** an issue where the KubeConfig for managed mesh workload clusters was not updated and where mesh secrets were not cleaned up when a workload cluster was removed.

## 2024-11-30

### v0.32.0

- **Improved** the gateway detail interface `/apis/mspider.io/v3alpha1/meshes/{mesh_id}/mesh-gateways/{gateway}`
  by adding fields `.details.ports`, `.details.load_balancer_ip`; upgrading `.configuration.service.load_balancer_ip`
  from runtime configuration to predefined configuration. Additionally, the default in `.details` is now runtime information.
- **Fixed** an issue where, in extreme cases, the state of the managed mesh removing the cluster was incorrect.

## 2024-10-31

### v0.31.0

- **Fixed** an issue where the link collection rate could not be adjusted.
- **Fixed** an issue where binding workload waypoint did not have audit logs.
- **Fixed** an issue where the patch version of K8s could not retrieve a valid Istio version.

## 2024-09-27

### v0.30.0

- **Fixed** an issue with abnormal logs.
- **Fixed** an issue of null pointer with Istio resources.
- **Fixed** an issue where resources were not removed after shutting down the working cluster's Istio resource synchronization.
- **Fixed** an issue of the abnormal `injectedMode` status in WorkloadShadow.
- **Improved** the supported Istio version in the backend, upgraded from v1.21.5 to v1.22.4,
  with the default version set to 1.22.4.

## 2024-09-02

### v0.29.0

#### Features

- **Added** support for managed meshes to quickly synchronize traffic management policies (VS, DR, Gateway)
  of worker clusters to the control plane and provide online viewing capabilities.
- **Added** a feature to inject waypoint and ztunnel sidecar components under the Ambient Mesh mode.

#### Fixes

- **Fixed** an issue with the connectivity detection feature of the mesh network in offline environments due to missing necessary images.
- **Fixed** an issue of missing `GatewayAPI` Custom Resource Definitions (CRD) in Ambient Mesh.
- **Fixed** the calculation issue of waypoint injection status that did not account for namespace dimensions.
- **Fixed** an issue where the namespace could not be passed when deleting the waypoint interface.
- **Fixed** an issue of capturing unnecessary sidecar metric ports.
- **Fixed** the installation issue caused by conflicts with Gateway API resources in Ambient Mesh.

## 2024-08-01

### v0.28.0

#### Features

- **Added** support for connectivity test in network pools for hosted mesh.
- **Added** multi-cluster deployment capabilities for mesh gateways.
- **Upgraded** to bind with `github.com/docker/docker` v26.1.4 + incompatible.
- **Upgraded** support for Istio mesh up to v1.20.8, v1.21.4, and v1.22.2.

#### Fixes

- **Fixed** an issue preventing the Tracing option from being enabled.
- **Fixed** abnormal detection of mesh components.
- **Fixed** a potential failure when reinstalling after uninstalling the hosted mesh.
- **Fixed** incorrect error message descriptions for interconnection detection failures.
- **Fixed** issues with abnormal namespace injection operations.
- **Fixed** an injection failure in Waypoint due to a missing Gateway API CRD.
- **Fixed** an incorrect parameter format in the mspider-mcpc ConfigMap.
- **Fixed** an issue where Istio Ambient v1.22 ztunnel would not start.

#### Improvements

- **Improved** the default network detection timeout to 3 seconds.
- **Improved** the cluster health detection mechanism to be configurable.
- **Improved** the Insight dashboard by replacing the irate expression with rate to prevent data spikes.
- **Improved** the accuracy of alerts for hosted mesh certificate expiration.

## 2024-06-30

### v0.27.0

- **Added** `Istio` resource analysis to help identify resource configuration anomalies and improve user experience.
- **Fixed** an issue where components were not uninstalled when removing a dedicated mesh.
- **Fixed** an issue with abnormal mesh component detection.
- **Fixed** an issue where reinstalling after uninstalling a hosted mesh might fail.

## 2024-05-30

### v0.26.0

- **Added** a feature of Istio Analyze.
- **Added** controller for synchronizing Istio resources across worker clusters.
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
- **Fixed** an issue of incorrect display of topology nodes due to lack of permissions.

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

- **Added** monitoring dashboards for service and workload monitoring panels, including traffic distribution for upstream and downstream.
- **Added** compatibility with `Istio` versions `v1.18.7`, `v1.19.6`, `v1.20.2`.
- **Fixed** an issue where `Consumer` services could not be identified as `Dubbo` services when using `Dubbo` and `Zookeeper` simultaneously.
- **Fixed** an issue with retrieval of valid `Istio` version list not being filtered based on cluster version.
- **Fixed** an issue with inability to enable multi-cloud connectivity with `Istio` `v1.20`.

## 2023-12-31

### v0.22.0

#### Features

- **Added** quota of system component resources for custom mesh instances.
- **Added** larger scale: **S2000P8000** , **S5000P20000** mesh instances.
- **Added** gateway instance upgrade reminder, supporting one-click upgrade.

#### Improvements

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

#### Improvements

- **Improved** the algorithm mechanism for the service list state and diagnostic state to ensure consistency between diagnostic results and status fields.
- **Improved** the automatic discovery policy for hosted mesh services to display any service from any cluster with the `mspider.io/managed` label.

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
- **Added** scaling configuration **auto_scaling** for the mesh gateway.

#### Improvements

- **Improved** traffic topology **Graph** implementation with optional hiding of idle nodes.
- **Improved** detection of host **glibc** version during **docker** mode installation of **vmagent** .

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
- **Improved** upgrade interface for checking mesh availability by adding permission checks.
- **Improved** **reconcileComponentsStatus** in **gsc-controller** under mesh-cluster.
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
- **Improved** description of the **namespaces** field in the **Istio** resource interface.
- **Improved** detection process of mesh control plane, ignoring control plane clusters.
- **Improved** consistency of different permissions for different roles with the latest permission design.
- **Improved** permission design, separating multi-cloud network interconnection permission from mesh management.
- **Improved** meaning of the `global.high_available` parameter.
- **Improved** usage of `CHART.replicas` , changing default value to empty.

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
- **Improved** cache to improve the latency issue of querying **Insight Agent** status in clusters.
- **Improved** strengthened detection of conflicting meshes when creating a mesh for managed clusters.
- **Improved** ignored updates to name (Name), namespace (Namespace), and labels (Labels) when updating mesh gateways to avoid triggering exceptions.
- **Improved** updated synchronization method for Kpanda cluster kubeconfig.
- **Improved** created logic for **WorkloadShadow controller watcher** .
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
- **Added** custom parameter configuration capability for hosted mesh hosted-apiserver. (This parameter only takes effect during installation and does not support updates for the time being), (for more parameters, refer to helm parameter configuration):
- **Added** mesh control plane component status
- **Added** the **loadBalancerStatus** field to the mesh query interface to describe the actual assigned LB address.
- **Added** component progress detail interface `/apis/mspider.io/v3alpha1/meshes/{mesh_id}/components-progress`.
- **Added** HPA is added for control plane components.
- **Added** new API definition to get cluster **StorageClass** .
- **Added** new API definition to get installed components in the cluster (currently supports Insight Agent).
- **Improved** user experience for binding/unbinding workspaces.
- **Improved** the **workload_kind** field type in the workload-related interface from enumeration to **string** .
- **Improved** version detection of the control plane cluster to be included along with the working cluster when hosting a mesh .
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
- **Improved** the controller namespace and service resource handling logic to reduce frequent workloadShadow resource updates.
- **Improved** the issue of frequent fetching/updating of workloadShadow resources, now reconciling only for resources that have undergone specific changes.
- **Improved** to reduce pod changes constantly updating WorkloadShadow.
- **Improved** the Helm image rendering template. The image structure is now split into three parts: registry/repository:tag.

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

- **Upgraded** the frontend version to v0.12.2
- **Fixed** an issue of not being able to update Istio resources with **.**
- **Fixed** an issue where istio-proxy could not start properly in version 1.17.1
- **Fixed** an issue of merge failure and deployment issues caused by missing name in ingress gateway

## 2023-03-30

### v0.14.0

#### New Features

- **Added** CloudShell related API definitions
- **Added** implementation for updating service labels
- **Added** service list and details to return labels
- **Added** CloudShell related implementations
- **Added** service list now supports querying service labels
- **Added** a new API for updating service labels
- **Added** support for Istio 1.17.1
- **Added** a new etcd high availability solution
- **Added** a scenario testing framework for testing scenario-based features
- **Added** automatic adjustment of component resource configurations when selecting different mesh scales
- **Added** implementation for custom roles, supporting operations like creation, updating, deletion, binding, and unbinding of custom roles

#### Improvements

- **Improved** mcpc controller startup logic to avoid situations where the working cluster is not registered correctly
- **Improved** WorkloadShadow cleanup logic to trigger on event rather than on a timer. It will now clean up when the controller starts or detects changes in the working cluster. When WorkloadShadow changes, self-health checks will trigger cleanup if the corresponding workload does not exist.
- **Improved** mcpc controller startup logic to prevent issues with incorrect registration of the working cluster
- **Upgraded** Insight API to version v0.14.7
- **Upgraded** ckube to support complex conditional queries for labels
- **Removed** the Helm upgrade time limit

#### Fixes

- **Fixed** an issue where the interface would not display when the east-west gateway is not ready
- **Fixed** an issue where multi-cloud interconnection would automatically register the east-west gateway LB IP, potentially causing internal network anomalies (removed the label `topology.istio.io/network` from the east-west gateway instance, which would automatically register the east-west gateway)
- **Fixed** the error during cluster migration with the east-west gateway (unable to modify instance labels; if component labels need to be modified, components must be deleted and rebuilt)
- **Fixed** an issue that caused Mesh binding to workspace services to fail (the interface displayed success)
- **Fixed** an issue of orphaned namespaces in the virtual cluster due to exceptions, adding self-check and cleanup behavior when starting mcpc-controller
- **Fixed** an issue of API failing to push mesh configurations due to controller updating the mesh
- **Fixed** an issue where ServicePort's TargetPort was not set correctly when creating a managed mesh
- **Fixed** the incorrect override issue with `GlobalMesh.Status.MeshVersion`
- **Fixed** an issue where mcpc-controller could not enable debug mode
- **Fixed** an issue where mcpc-controller could not trigger cluster deletion events
- **Fixed** an issue where deleting a Mesh and then recreating a Mesh with the same name would prevent proper creation of the Mesh (hosted proxy could not be updated correctly)
- **Fixed** an issue where mcpc controller did not correctly modify the service of istiod-remote in certain cases

## 2023-02-28

### v0.13.1

#### New Features

- **Added** multi-cloud network interconnection management and related interfaces
- **Added** global configuration capabilities for the mesh (mesh system configuration, global traffic governance capabilities, global sidecar injection settings) enhancements
- **Added** support for zookeeper proxy

#### Improvements

- **Improved** Namespace controller with Cache to reduce excessive duplicate Get requests when there are too many namespaces in the cluster
- **Improved** reduced log output of ckube in normal mode

#### Fixes

- **Fixed** logical errors related to the mesh caused by the removal of clusters from the container management platform
- **Fixed** an issue where injecting Sidecar with RegProxy would cause Nacos registration failures
- **Fixed** an issue of incorrect service recognition in Spring Cloud
- **Fixed** the lack of synchronization of cluster status information from the container management platform
- **Fixed** the traffic pass-through strategy - IP segment configuration for traffic filtering not taking effect
- **Fixed** the traffic pass-through strategy - inability to delete traffic pass-through strategies
- **Fixed** an issue of returning errors when obtaining mesh configurations due to non-existent configuration paths

## 2022-12-29

### v0.12.0

#### New Features

- **Added** interface implementation for traffic pass-through functionality
- **Added** support for Istio 1.15.4, 1.16.1

#### Improvements

- **Improved** the management page of namespace sidecars by adding an "unset" sidecar policy to avoid cross-impact between namespace-level sidecar policies and workload-level policies
- **Improved** parameters for release pipelines
- **Improved** sidecar injection and resource limit logic to avoid synchronization issues

#### Fixes

- **Fixed** an issue where some components were not updated after a mesh upgrade
- **Fixed** an issue of some resources not being cleared after mesh removal - sidecar resource synchronization was incorrect, now using the actual sidecar resources from the istio-proxy container in the Pod
- **Fixed** an issue where managed clusters could not act as working clusters
- **Fixed** an issue where the injection display was incorrect when the sidecar injection instances were at 0/0
- **Fixed** an issue where sidecar-related information still displayed after canceling sidecar injection

## 2022-11-30

### v0.11.1

#### New Features

- **Added** **Key Management** related APIs
- **Added** rules and gateway lists in virtual services
- **Added** governance strategy labels and related filtering capabilities
- **Added** the ability to check the health status of clusters within the mesh
- **Added** integration with otel sdk
- **Added** multiple interface implementations for secrets
- **Added** support for Istio 1.15.3

#### Improvements

- **Improved** the workload sidecar injection interface to prevent issues
- **Improved** the monitoring dashboard for mesh services to expand by default
- **Improved** to disable sub-link redirection in the global monitoring dashboard of the mesh to avoid interface confusion
- **Improved** the processing flow of the mesh control plane to avoid conflicts caused by updating already updated objects
- **Improved** the logic for accessing and removing clusters in the mesh

#### Fixes

- **Fixed** an issue where mcpc and other components were not updated after upgrading the control plane MSpider
- **Fixed** errors in obtaining cluster resources
- **Fixed** an issue where the response code was 200 when the cluster name did not exist in the cluster namespace list interface
- **Fixed** an issue of incorrect precondition checks in the mesh upgrade process
- **Fixed** an issue of mesh upgrades not executing k8s version restrictions
- **Fixed** an issue of invalid workload sidecar resource configuration in the sidecar management interface
- **Fixed** an issue where clusters could not be removed due to monitoring detection failures within the mesh
- **Fixed** an issue where the data plane image was not packaged into the DCE 5.0 offline package
- **Fixed** an issue where Ckube could not automatically update configurations
