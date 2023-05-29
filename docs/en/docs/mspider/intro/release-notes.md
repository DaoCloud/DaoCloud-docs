---
MTPE: windsonsea
Revised: todo
Pics: NA
Date: 2022-12-20
---

# Service Mesh Release Notes

This page lists all the Release Notes for each version of Service Mesh, providing convenience for users to learn about the evolution path and feature changes.

## 2023-04-27

### v0.15.0

#### Added

- Introduced `d2` as a drawing tool.
- Added a new wasm plugin that adds different headers to requests according to the trace ID.
- Hosted Istiod's LoadBalancer Annotations implementation in mesh configuration.
- Implemented mesh gateway configuration service Annotations.
- Added `load_balancer_annotations` field to mesh, supporting custom load balancing annotations.
- In `mspider-api`, manually execute the pipeline and set `SYNC_OPENAPI_DOCS` as the key to trigger the upload of the document site (raise PR).
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

#### Upgraded

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
- Scenario-based testing framework for testing scenario-based functions added.
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
- Multi-cloud interconnection will automatically register the east-west gateway LB IP, which may cause internal network abnormalities (remove the east-west gateway instance label: `topology.istio.io/network`. This label will automatically register the east-west gateway).
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

- Multi-cluster management feature added.
- Support for multi-cloud interconnection added.
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
