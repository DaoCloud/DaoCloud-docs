# Service mesh component resource custom configuration

This page describes how to customize mesh component resources via [Container Management](../../../kpanda/user-guide/workloads/create-deployment.md).
The control plane components of the service mesh are as follows:

| Component Name | Location | Description | Default Resource Settings |
| ---------------------------- | ------------ | ------- --------------------- | ---------------- |
| mspider-ui | Global Management Cluster | Service Mesh Interface | requests: CPU: Not set; Memory: Not set<br> limits: CPU: Not set; Memory: Not set |
| mspider-ckube | Global management cluster | Acceleration component of Kubernetes API Server, used to call global cluster-related resources | requests: CPU: not set; memory: not set<br/> limits: CPU: not set; memory: not set settings |
| mspider-ckube-remote | Global Management Cluster | Used to call Kubernetes of remote clusters, aggregate multicluster resources, and accelerate | requests: CPU: not set; memory: not set<br/> limits: CPU: not set; memory : not set |
| mspider-gsc-controller | Global management cluster | Service mesh management component, used for mesh creation, mesh configuration and other mesh control plane lifecycle management, and Mspider control plane capabilities such as permission management | requests: CPU: Not set ;memory: not set<br/>limits: CPU: not set; memory: not set |
| mspider-api-service | Global management cluster | Provide interface for Mspider background API interaction and other control behaviors | requests: CPU: not set; memory: not set <br/>limits: CPU: not set; memory: not set |
| Hosted mesh | | | |
| istiod-{meshID}-hosted | control plane cluster | policy management for hosted mesh | requests: CPU: 100m; memory: 100m <br/>limits: CPU: not set; memory: not set |
| mspider-mcpc-ckube-remote | Control plane cluster | Invoke remote mesh work clusters to accelerate and aggregate multicluster resources | requests: CPU: 100m; memory: 50m<br/>limits: CPU: 500m; memory: 500m |
| mspider-mcpc-mcpc-controller | Control plane cluster | Aggregate mesh multicluster related data plane information | requests: CPU: 100m; memory: 0<br/> limits: CPU: 300m; memory: 1.56G |
| {meshID}-hosted-apiserver | Control Plane Cluster | Hosted Control Plane Virtual Cluster API Server | requests: CPU: not set; memory: not set<br/> limits: CPU: not set; memory: not set |
| istiod | working cluster | Mainly used for sidecar lifecycle management of the cluster | requests: CPU: 100; memory: 100<br/> limits: CPU: not set; memory: not set |
| Proprietary mesh | | | |
| istiod | | used for policy creation, delivery, and sidecar lifecycle management | requests: CPU: 100; memory: 100<br/> limits: CPU: not set; memory: not set |
| mspider-mcpc-ckube-remote | working cluster | call remote mesh working cluster | requests: CPU: 100m; memory: 50m<br/> limits: CPU: 500m; memory: 500m |
| mspider-mcpc-mcpc-controller | Working cluster | Collect cluster data surface information | requests: CPU: 100m; memory: 0<br/> limits: CPU: 300m; memory: 1.56G |
| External mesh | | | |
| mspider-mcpc-ckube-remote | working cluster | call remote mesh working cluster | requests: CPU: 100m; memory: 50m<br/> limits: CPU: 500m; memory: 500m |
| mspider-mcpc-mcpc-controller | Working cluster | Collect cluster data surface information | requests: CPU: 100m; memory: 0<br/> limits: CPU: 300m; memory: 1.56G |

The preset resource settings of each control plane component of the service mesh are shown in the above table. Users can find the corresponding workload in the [Container Management] module and customize CPU and memory resources for the workload.

## Prerequisites

The cluster has been managed by the service mesh, and the mesh components have been installed normally;
The login account has the admin or editor authority of the namespace istio-system in the global management cluster and the working cluster;

## set operation

Take istiod on the working cluster under the hosted mesh as an example, the specific operations are as follows:

1. View the hosted mesh nicole-dsm-mesh access cluster under the service mesh is nicole-dsm-c2, as shown in the figure below.


2. Click the cluster name, jump to the cluster page in the __Container Management__ module, click to enter the __Workload__ -> __Stateless Load__ page to find istiod;


3. Click the workload name to enter __Container Configuration__ -> __Basic Information__ tab page;


4. Click the Edit button to modify the CPU and memory quotas, click __Next__ , __OK__ .

5. View the Pod resource information under the workload, and it can be seen that it has changed.
