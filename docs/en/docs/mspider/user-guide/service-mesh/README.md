---
hide:
   - toc
---

# create managed/private mesh

DCE 5.0 service mesh supports 3 meshes:

- **Hosted Mesh** is fully hosted within the DCE 5.0 service mesh. This mesh separates the core control plane components from the working cluster, and the control plane can be deployed in an independent cluster, enabling unified governance of multi-cluster services in the same mesh.
- **private mesh** adopts the traditional structure of Istio, supports only one cluster, and has a dedicated control plane in the cluster.
- **External mesh** means that the existing mesh of the enterprise can be connected to the DCE 5.0 service mesh for unified management. See [Create an external mesh](external-mesh.md).

The steps to create a managed mesh/private mesh are as follows:

1. In the upper right corner of the service mesh list page, click `Create mesh`.


1. Select `Hosted mesh` or `private mesh`, fill in the basic information and click `Next`.

     - mesh Name: Start with a lowercase letter, consist of lowercase letters, numbers, dashes (-), and cannot end with a dash (-)
     - Istio version: In case of a managed mesh, all managed clusters will use this version of Istio.
     - Control Plane Cluster: The cluster used to run the mesh management plane, with a refresh icon and `Create Cluster` button. Click `Create Cluster` to jump to the `Container Management` platform to create a new cluster. After the creation is complete, return to this page and click the refresh icon to update the cluster list.
     - Control Plane Address: Enter the IP address of the control plane.
     - mesh component warehouse: Enter the address of the mirror warehouse that contains the data surface component mirror, such as `release.daocloud.io/mspider`.
  

1. System settings. Configure whether to enable observability, set the mesh size and click `Next`.


1. Governance settings. Set outbound traffic policies, location-aware load balancing, request retries, and more.

1. Sidecar setup. After setting the global sidecar, resource limit, and log, click `OK`.


1. Automatically return to the mesh list, the newly created mesh is at the first place by default, and the status will change from `creating` to `running` after a period of time. Click `...` on the right to edit basic mesh information, add clusters, etc.


!!! info

     After the managed mesh is created, no managed cluster has been connected, and the mesh is in the state of `not ready`.
     Users can [add cluster](../cluster-management/README.md), wait for the cluster access to complete, and select the cluster access that requires service management.
