---
hide:
  - toc
---

# Service Mesh

On the main page of the service grid, users can browse basic grid information, cluster instance status, and grid running status, and perform operations such as creating, configuring, and deleting grids.

The grid list shows basic information such as grid type, Istio version, cluster and pod status.
The service grid provides users with three grid types: managed grid, dedicated grid, and external grid. Users can choose to create based on the actual cluster environment.

- Managed grid: used for multi-cluster management, grid resources will be stored in separate virtual clusters, a high degree of independence ensures that users can freely access and remove multiple clusters, and manage namespaces and services of multiple clusters Do aggregate governance;
- Proprietary grid: used for grid management of a single cluster, the grid control plane is installed in the user's working cluster and cannot be connected to other clusters;
- External grid: access to the native Istio installed by the user, inject the sidecar uniformly through the service grid management platform, and issue management policies, etc.

![Mesh List](../../images/servicemesh01.png)

The meanings of each grid list card are as follows:

| Interface text | Meaning and description of changes |
| ------------ | ------------------------------------ ------------------------ |
| Grid Name | User-created grid name, consisting of letters, numbers, and dashes (-). |
| Running Status| The running status of the grid. There are the following statuses:<br />- Running, indicating that the grid has managed clusters and the configuration is complete<br />- Not Ready, indicating that the grid has not managed any clusters <br /> - Exception, indicating that the grid is not working properly; grid creation, deletion, setup failed. <br />- Creating, indicating that the grid is being created <br />- Deleting, indicating that the grid is being deleted |
| Grid Type | Managed Grid/Proprietary Grid/External Grid |
| Istio version | Istio version number used by the current mesh |
| Control plane cluster | The management cluster used to run the control plane of the service mesh, this item cannot be modified after the mesh is created |
| Creation Time | Mesh Creation Time |
| Cluster statistics | Ratio of clusters in normal state to all clusters in the grid |
| Number of Pod instances | Ratio of normal Pods injected with sidecars to all Pods in each cluster under the grid |
| Cluster list | Move the cursor to the number area of ​​`Cluster Statistics`, a floating prompt will appear, displaying the names and status of all clusters managed under the current grid |