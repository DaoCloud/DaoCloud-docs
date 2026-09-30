---
hide:
  - toc
---

# Delete/Remove Clusters

Clusters **created** through the DCE [Container Management](../../intro/index.md) platform support the __Delete Cluster__ or __Remove__ operation, while clusters directly **integrated** from other environments only support the __Remove__ operation.

!!! Info

    If you want to completely delete an integrated cluster, you need to go to the original platform where the cluster was created. DCE does not support deleting integrated clusters.

In the DCE platform, the difference between __Delete Cluster__ and __Remove__ is:

- The __Delete Cluster__ operation destroys the cluster and resets the data of all nodes under the cluster. All data will be destroyed, so it is recommended to make a backup. If you need it later, you must create a new cluster.
- The __Remove__ operation removes the current cluster from the platform without destroying the cluster or the data.

## Delete a Cluster

!!! note

    - The current operating user should have [Admin](../../../ghippo/user-guide/access-control/role.md) or [Kpanda Owner](../../../ghippo/user-guide/access-control/global.md) permissions to perform the delete cluster operation.
    - Before deleting a cluster, you should first click a cluster name in the cluster list and turn off __Cluster Deletion Protection__ in __Operations and Maintenance__ -> __Cluster Settings__ -> __Advanced Settings__ ;
      otherwise, the __Delete Cluster__ option will not be displayed.
    - The __global service cluster__ does not support deletion or removal.

1. On the __Cluster List__ page, find the cluster to be deleted, click __┇__ on the right, and select __Delete Cluster__ in the drop-down list.

    ![Click the delete button](../../images/delete001.png)

2. Enter the cluster name to confirm, and then click __Delete__ .

    ![Confirm deletion](../../images/delete002.png)

    If you are prompted that some residual resources still exist in the cluster, you need to delete the related resources as prompted before you can perform the deletion.

3. Return to the __Cluster List__ page, and you can see that the status of the cluster has changed to __Deleting__ . Deleting a cluster may take a while, so please be patient.

    ![Deleting status](https://docs.daocloud.io/daocloud-docs-images/docs/kpanda/images/delete004.png)

## Remove an Integrated Cluster

!!! note

    - The current operating user should have [Admin](../../../ghippo/user-guide/access-control/role.md) or
      [Kpanda Owner](../../../ghippo/user-guide/access-control/global.md) permissions to perform the remove operation.
    - The __global service cluster__ does not support removal.

1. On the __Cluster List__ page, find the cluster to be removed, click __┇__ on the right, and select __Remove__ in the drop-down list.

    ![Click the remove button](../../images/remove001.png)

2. Enter the cluster name to confirm, and then click __Remove__ .

    ![Confirm removal](../../images/delete003.png)

    If you are prompted that some residual resources still exist in the cluster, you need to delete the related resources as prompted before you can remove it.

## Clean Up the Configuration Data of a Removed Cluster

After a cluster is removed, the original management platform data in the cluster is not automatically cleared. If you need to integrate the cluster into a new management platform, you need to manually perform the following operations:

1. Delete the kpanda-system and insight-system namespaces.

    ```shell
    kubectl delete ns kpanda-system insight-system
    ```

2. If the service mesh capability is enabled for the current cluster, refer to the [Delete Mesh](../../../mspider/user-guide/service-mesh/delete.md) documentation to delete the mesh instance in the current cluster.
