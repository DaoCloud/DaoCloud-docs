---
MTPE: windsonsea
Revised: todo
Pics: NA
Date: 2022-12-20
---

# Release Notes of Service Mesh

This page lists all Release Notes of each version of Service Mesh, to provide your convenience to learn the evolution path and feature changes.

## 2023-03-31

### v0.14.3

#### upgrade

- **Upgrade** front-end version to v0.12.2

#### fix

- **FIX** Unable to update Istio resources with .
- **FIXED** In version 1.17.1, istio-proxy cannot start normally
- **Fix** the problem that the ingress gateway lacks a name, which causes the merge to fail and cannot be deployed.

## 2023-03-30

### v0.14.0

#### Features

- **Add** CloudShell related interface definition
- **NEW** Tag implementation for update service
- **Add** service list and details will return labels
- **Add** CloudShell related implementation
- **NEW** The service list supports querying service labels
- **NEW** Added a new API for updating a service's tags
- **Added** istio 1.17.1 support
- **NEW** Added a new etcd high availability solution
- **Add** scenario-based testing framework for testing scenario-based functions
- **NEW** When selecting different mesh sizes, automatically adjust component resource configuration
- **New** Added the implementation of custom roles, supporting operations such as creation, update, deletion, binding, and unbinding of custom roles

#### Optimization

- **Optimize** mcpc controller startup logic to avoid the situation that the working cluster is not registered correctly
- **Optimized** WorkloadShadow cleanup logic: triggered by timing trigger transformation events: when the controller starts, when a change in the working cluster is detected;
   When WorkloadShadow changes, self-health detection triggers cleanup logic when the corresponding workload does not exist
- **Optimize** mcpc controller startup logic to avoid the situation that the working cluster is not registered correctly
- **Upgrade** Insight api upgraded to version v0.14.7
- **Upgrade** ckube supports complex conditional query of labels
- **REMOVED** Remove Helm upgrade time limit

#### fix

- **Fix** the problem that the interface does not display when the east-west gateway is not Ready
- **Fixed** The multi-cloud interconnection will automatically register the east-west gateway LB IP, which may cause internal network abnormalities (remove the east-west gateway instance label: topology.istio.io/network, this label will automatically register the east-west gateway)
- **Fix** The cluster migration with east-west gateways will cause errors (the label of the instance cannot be modified, if you need to modify the component label, you can only delete the component and rebuild it)
- **FIXED** Fixed a problem that caused Mesh to bind the workspace service to fail (the interface shows success)
- **Fix** Due to abnormality, there is a free namespace in the virtual cluster, add self-check and clear behavior when starting mcpc-controller
- **Fix** Due to the update of the mesh by the controller, the api fails to deliver the mesh configuration
- **FIXED** ServicePort's TargetPort was not set correctly when creating hosted mesh
- **FIX** GlobalMesh.Status.MeshVersion wrong coverage issue
- **Fix** mcpc-controller cannot open debug mode
- **Fix** mcpc-controller can't trigger cluster delete event
- **FIXED** When deleting a Mesh and rebuilding a Mesh with the same name, the Mesh cannot be created normally (hosted proxy cannot be updated normally)
- **Fix** mcpc controller does not modify the istiod-remote service correctly in some cases

## 2023-02-28

### v0.13.1

#### Features

- **Add** multi-cloud network interconnection management and related interfaces
- **NEW** Enhanced mesh global configuration capabilities (mesh system configuration, global traffic management capabilities, global sidecar injection settings)
- **NEW** Added support for zookeeper proxy

#### Optimization

- **Optimize** Namespace controller plus Cache, when there are too many Namespaces in the cluster, it will cause too many repeated Get requests
- **Optimize** reduce the log output of ckube in normal mode

#### fix

- **FIXED** mesh related logic error caused by container management platform removing cluster
- **Fix** RegProxy injecting Sidecar will cause Nacos to fail to register
- **Fix** Spring Cloud service identification error
- **Fix** The cluster status information of the container management platform is not synchronized
- **Fix** traffic transparent transmission policy - traffic filtering IP segment configuration does not take effect
- **Fix** traffic transparent transmission policy - traffic transparent transmission policy cannot be deleted
- **FIXED** When getting the mesh configuration, an error is returned because the configuration path does not exist

## 2022-12-29

### v0.12.0

#### New features

- Interface implementation of traffic transparent transmission function
- Support for istio 1.15.4, 1.16.1

#### Optimized

- Added "unset" sidecar policy to the namespace sidecar management page to avoid sidecar policies at the namespace level from having a collateral impact on the workload level;
- Publish pipeline parameter optimization
- Optimize the logic of sidecar injection and sidecar resource limitation to avoid out-of-sync phenomenon

#### Fixed

- The problem that some components are not updated after mesh upgrade
- The problem that some resources are not cleared after the mesh is removed - The sidecar resources are not synchronized correctly, instead the actual sidecar resources through the istio-proxy container in the Pod
- Managed clusters cannot be used as working clusters
- Injection is displayed incorrectly when sidecar injection instance is 0/0
- After canceling sidecar injection, sidecar related information is still displayed

## 2022-11-30

### v0.11.1

#### New features

- Added `Key Management` related APIs
- Added governance policy tags and related filtering capabilities in the lists of `Virtual Service`, `Target Rules`, and `Gateway Rules`
- Added capability of checking the health status of clusters in the mesh
- Added support of accessing OTel sdk
- Added implementation of multiple interfaces for secrets
- Added support for Istio 1.15.3

#### Optimized

- Optimized those interfaces with heavy workload for sidecar injection to prevent from potential problems
- The mesh service monitoring panel is expanded by default
- Disable the sub-link jump of the global monitoring panel of the mesh to avoid interface confusion
- Optimize the mesh control plane processing process to avoid conflicts caused by updating objects that have been updated
- Optimize mesh cluster access and removal logic

#### Fixed

- When the control plane is upgraded, components such as MCPC are not updated
- Get cluster resource error
- The response code is 200 when the interface cluster name does not exist to get the cluster namespace list
- The problem of incorrect judgment of preconditions in the mesh upgrade process
- The problem that the mesh upgrade does not implement k8s version restrictions
- The sidecar resource configuration failure of the sidecar management interface workload
- The problem that the cluster cannot be removed due to the failure of the monitoring and detection of the cluster in the mesh
- The image of the data plane is not packaged into the offline package of DCE 5.0
- The problem that Ckube cannot automatically update the configuration
