# Control Plane Components

This page lists the various components in the control plane of the service mesh along with their locations, descriptions, and default resource settings.

| Component | Location | Description | Default Resource Settings |
| ----------|----------|-------------|--------------------------|
| mspider-ui | Global Management Cluster | Service Mesh Interface | Requests: CPU - Unset; Memory - Unset<br>Limits: CPU - Unset; Memory - Unset |
| mspider-ckube | Global Management Cluster | Acceleration component of Kubernetes API Server used to call global cluster-related resources | Requests: CPU - Unset; Memory - Unset<br>Limits: CPU - Unset; Memory - Unset |
| mspider-ckube-remote | Global Management Cluster | Used to call Kubernetes of remote clusters, aggregate multicluster resources, and accelerate | Requests: CPU - Unset; Memory - Unset<br>Limits: CPU - Unset; Memory - Unset |
| mspider-gsc-controller | Global Management Cluster | Service mesh management component used for mesh creation, configuration, and other mesh control plane life cycle management, as well as Mspider control plane capabilities such as permission management | Requests: CPU - Unset; Memory - Unset<br>Limits: CPU - Unset; Memory - Unset |
| mspider-api-service | Global Management Cluster | Provides an interface for Mspider background API interaction and other control behaviors | Requests: CPU - Unset; Memory - Unset<br>Limits: CPU - Unset; Memory - Unset |
| Hosted Mesh | | | |
| istiod-{meshID}-hosted | Control Plane Cluster | Policy management for hosted mesh | Requests: CPU - 100m; Memory - 100m<br>Limits: CPU - Unset; Memory - Unset |
| mspider-mcpc-ckube-remote | Control Plane Cluster | Invokes remote mesh work clusters to accelerate and aggregate multicluster resources | Requests: CPU - 100m; Memory - 50m<br>Limits: CPU - 500m; Memory - 500m |
| mspider-mcpc-mcpc-controller | Control Plane Cluster | Aggregates mesh multicluster related data plane information | Requests: CPU - 100m; Memory - 0<br>Limits: CPU - 300m; Memory - 1.56G |
| {meshID}-hosted-apiserver | Control Plane Cluster | Hosted Control Plane Virtual Cluster API Server | Requests: CPU - Unset; Memory - Unset<br>Limits: CPU - Unset; Memory - Unset |
| istiod | Working Cluster | Mainly used for sidecar lifecycle management of the cluster | Requests: CPU - 100; Memory - 100<br>Limits: CPU - Unset; Memory - Unset |
| Proprietary Mesh | | | |
| istiod | | Used for policy creation, delivery, and sidecar lifecycle management | Requests: CPU - 100; Memory - 100<br>Limits: CPU - Unset; Memory - Unset |
| mspider-mcpc-ckube-remote | Working Cluster | Calls remote mesh working cluster | Requests: CPU - 100m; Memory - 50m<br>Limits: CPU - 500m; Memory - 500m |
| mspider-mcpc-mcpc-controller | Working Cluster | Collects cluster data surface information | Requests: CPU - 100m; Memory - 0<br>Limits: CPU - 300m; Memory - 1.56G |
| External Mesh | | | |
| mspider-mcpc-ckube-remote | Working Cluster | Calls remote mesh working cluster | Requests: CPU - 100m; Memory - 50m<br>Limits: CPU - 500m; Memory - 500m |
| mspider-mcpc-mcpc-controller | Working Cluster | Collects cluster data surface information | Requests: CPU - 100m; Memory - 0<br>Limits: CPU - 300m; Memory - 1.56G |

These are the default resource settings for each control plane component of the service mesh. Users can customize CPU and memory resources for each workload in the [Container Management](../../../kpanda/user-guide/workloads/create-deployment.md) module.
