---
hide:
  - toc
---

# Service Mesh

On the main page of the service mesh, users can browse basic mesh information, cluster instance status, and mesh running status, and perform operations such as creating, configuring, and deleting meshs.

The mesh list shows basic information such as mesh type, Istio version, cluster and pod status.
The service mesh provides users with three mesh types: managed mesh, dedicated mesh, and external mesh. Users can choose to create based on the actual cluster environment.

- Managed mesh: used for multi-cluster management, mesh resources will be stored in separate virtual clusters, a high degree of independence ensures that users can freely access and remove multiple clusters, and manage namespaces and services of multiple clusters Do aggregate governance;
- Proprietary mesh: used for mesh management of a single cluster, the mesh control plane is installed in the user's working cluster and cannot be connected to other clusters;
- External mesh: access to the native Istio installed by the user, inject the sidecar uniformly through the service mesh management platform, and issue management policies, etc.

![Mesh List](../../images/servicemesh01.png)

The meanings of each mesh list card are as follows:

| Interface text | Meaning and description of changes |
| ------------ | ------------------------------------ ------------------------ |
| mesh Name | User-created mesh name, consisting of letters, numbers, and dashes (-). |
| Running Status| The running status of the mesh. There are the following statuses:<br />- Running, indicating that the mesh has managed clusters and the configuration is complete<br />- Not Ready, indicating that the mesh has not managed any clusters <br /> - Exception, indicating that the mesh is not working properly; mesh creation, deletion, setup failed. <br />- Creating, indicating that the mesh is being created <br />- Deleting, indicating that the mesh is being deleted |
| mesh Type | Managed mesh/Proprietary mesh/External mesh |
| Istio version | Istio version number used by the current mesh |
| Control plane cluster | The management cluster used to run the control plane of the service mesh, this item cannot be modified after the mesh is created |
| Creation Time | Mesh Creation Time |
| Cluster statistics | Ratio of clusters in normal state to all clusters in the mesh |
| Number of Pod instances | Ratio of normal Pods injected with sidecars to all Pods in each cluster under the mesh |
| Cluster list | Move the cursor to the number area of ​​`Cluster Statistics`, a floating prompt will appear, displaying the names and status of all clusters managed under the current mesh |