---
hide:
   - toc
---

# Create Hosted or Dedicated Mesh

DCE 5.0 service mesh supports three kinds of meshes:

- **Hosted Mesh** is fully hosted within the DCE 5.0 service mesh. This mesh separates the core control plane components from the working cluster, and the control plane can be deployed in an independent cluster, enabling unified governance of multicluster services in the same mesh.
- **Dedicated mesh** adopts the traditional structure of Istio, supports only one cluster, and has a dedicated control plane in the cluster.
- **External mesh** means that the existing mesh of the enterprise can be connected to the DCE 5.0 service mesh for unified management. See [Create an external mesh](external-mesh.md).

The following explains the steps to create a Hosted Mesh/Dedicated Mesh:

1. On the right corner of the mesh list, click the `Create Mesh` button and select the type of mesh from the dropdown list.

    ![Create Mesh](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/create-mesh01.png)

2. The system will automatically detect the installation environment. After successful detection, fill in the following basic information and click `Next`.

    - Name: Can contain lowercase letters, numbers, and hyphens ('-'), and must start with a lowercase letter and end with a letter or number.
    - Istio version: For Hosted Mesh, this version will be used by all member clusters in the mesh.
    - Cluster: This is the cluster where the mesh control plane runs. The drop-down list displays the version and health status of each cluster.
    - Entry of control plane: Supports load balancer and custom.
    - Mesh component repo: Enter the address of the container registry that contains the data plane components, such as `release-ci.daocloud.io/mspider`.

        ![Basic Information](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/create-mesh02.png)

3. System settings. Configure whether to enable observability, set the scale of the mesh, select StorageClass, and click `Next`.

    ![System Settings](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/create-mesh03.png)

    !!! note

        - StorageClass is only applicable to Hosted Mesh, not Dedicated Mesh or External Mesh.
        - When the cluster where the control plane resides is OCP, you can choose to install OCP components.

4. Governance settings. Set outbound traffic policies, locality load balancing, and request retries. See [Request Retry Parameters Description](./params.md#max-retries).

    ![Governance Settings](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/create-mesh04.png)

5. Sidecar settings. Set global sidecar, sidecar resource limits, default sidecar log level, and click `OK`. See [Log Level Description](./params.md#_2).

    ![Sidecar Settings](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/create-mesh05.png)

6. You will automatically return to the Mesh List page, and the newly created mesh will be listed at the top. After some time, the status will change from `Creating` to `Running`. Click on the `...` on the right to perform operations such as editing mesh basic information, adding clusters, accessing the console, etc.

!!! info

     After the hosted mesh is created, no hosted cluster has been connected, and the mesh is in the state of `not ready`.
     Users can [add cluster](../cluster-management/README.md), wait for the cluster joined successfully, and select the cluster that requires service management.
