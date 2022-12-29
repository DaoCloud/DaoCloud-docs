---
MTPE: windsonsea
Revised: todo
Pics: NA
Date: 2022-12-20
---

# Release Notes of Service Mesh

This page lists all Release Notes of each version of Service Mesh, to provide your convenience to learn the evolution path and feature changes.

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

- The problem that some components are not updated after grid upgrade
- The problem that some resources are not cleared after the grid is removed - The sidecar resources are not synchronized correctly, instead the actual sidecar resources through the istio-proxy container in the Pod
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
