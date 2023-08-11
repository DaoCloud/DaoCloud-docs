---
hide:
   - toc
---

# Create External Mesh

External mesh means that the existing mesh can be connected to the DCE 5.0 service mesh for management.

1. On the right corner of the mesh list, click the `Create Mesh` button and select `Create external mesh` from the dropdown list.

    ![Create External Mesh](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/external01.png)

2. The system will automatically detect the installation environment. After successful detection, fill in the following basic information and click `OK`.

    - Name: It can only contain lowercase letters, numbers, and hyphens ('-'), and must start with a lowercase letter and end with a letter or number.
    - Istio version: This version will be used by all member clusters in the mesh.
    - Cluster: This is the cluster where the mesh control plane runs. The drop-down list displays the version and health status of each cluster.
    - Entry of control plane: Supports load balancer and custom.
    - Mesh component repo: Enter the address of the container registry that contains the data plane components, such as `release-ci.daocloud.io/mspider`.

    ![Basic Information](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/external02.png)

3. You will automatically return to the Mesh List page, and the newly created mesh will be listed at the top. After some time, the status will change from `Creating` to `Running`. Click on the `...` on the right to perform operations such as editing basic information, adding clusters, accessing the console, and deleting.

    ![Mesh List](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/external03.png)

Next step: [Service Management](../service-list/README.md)