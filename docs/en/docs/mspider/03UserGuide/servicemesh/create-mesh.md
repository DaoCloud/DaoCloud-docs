# Create managed/private mesh

The DCE 5.0 service mesh supports the creation of managed meshs, dedicated meshs, and external meshs. The steps to create a managed mesh/proprietary mesh are as follows:

!!! info
    - Managed mesh refers to the separation of mesh core control plane components from the concept of working clusters, which can be deployed in an independent control plane cluster, reducing the user's O&M burden and resource consumption, and users can control the components located in the same mesh Unified management of multi-cluster services in .
    - The biggest difference between dedicated and managed meshs is: dedicated meshs are single-cluster models.
    - For information on how to integrate an integrated mesh, see [Create an integrated mesh](integrate-mesh.md).

1. In the upper right corner of the service mesh list page, click `Create mesh`.

    

2. Select `Hosted mesh` or `Proprietary mesh` and fill in the mesh configuration information.

    - mesh name: start with a lowercase letter, consist of lowercase letters, numbers, dashes (-), and cannot end with a dash (-)
    - Alias: used to improve ease of use and mesh recognition, you can enter letters, numbers, Chinese and other symbols, within 60 characters
    - Istio version: The Istio version number that the current system can support. Select one as the Istio version of the currently created mesh. If it is a managed mesh, then all managed clusters will use this version of Istio.
    - Control plane cluster: the cluster used to run the mesh management plane, the list includes the clusters that the current mesh platform can access and are in normal state. The item comes with a refresh icon and a `Create Cluster` button. Click `Create Cluster` to jump to `Container Management Platform` to create a new cluster. After the creation is complete, return to this page and click the refresh icon to update the list.
    - container registry: Enter the address of the container registry that contains the data plane component image. If the cluster can access the public network, you can fill in the official image address: `release.daocloud.io/mspider`. For private environments, please upload the image yourself and fill in the actual address.
  
    

3. Click the `OK` button to complete the mesh creation. The system automatically returns to the mesh list, and you can view and manage the newly added meshs.

!!! info

    After the managed mesh is created, no managed cluster has been connected, and the mesh is in the state of `not ready`. Users can [Add Cluster](../08ClusterManagement/README.md), wait for the cluster access to complete, and select the cluster access that requires service management.

## Optional settings

After filling out the basic configuration correctly, you can successfully create a basic hosted mesh. If you want to use advanced features, you can click `Optional Settings` to fill in the optional configuration.

- mesh Scale: Contains four size options and provides resource suggestion information related to the selected size
- Sidecar injection strategy: You can enable/disable the sidecar automatic injection strategy at the mesh level. After enabling, all access clusters will automatically inject sidecars
- Sidecar resource setting: implement resource restrictions on injected sidecars of all clusters under the mesh, which can be used as the default sidecar resource value under the mesh. The execution priority of sidecar resource limit rules at each level is: workload-level resource limit -> cluster-level resource limit -> mesh resource limit

