# Manage Worker Clusters

After creating multicloud instances, you need to connect them to worker clusters.

## Add a Cluster

1. Click __Worker Cluster Management__ in the left navigation bar, then click __Connect Cluster__ in the top-right corner.

    If you want to establish network connectivity between worker clusters, you need to create a mesh instance and manage worker clusters on the Service Mesh page. For detailed steps, refer to [MultiCloud Network Interconnect](../mspider/user-guide/multicluster/cluster-interconnect.md).

    ![Connect Cluster](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/cluster01.png)

2. Select the worker cluster you want to add and click __OK__ .

    If the target cluster you want to add is not listed, you can either integrate or create a cluster in the Container Management module. For more details, refer to [Cluster Integration](../kpanda/user-guide/clusters/integrate-cluster.md) or [Create Cluster](../kpanda/user-guide/clusters/create-cluster.md).

    ![Confirm](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/cluster02.png)

## Remove a Cluster

1. Click the __┇__ button on the right side of the cluster, and select __Remove__ from the pop-up menu.

    ![Removal](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/cluster03.png)

2. In the dialog box, enter the name of the cluster, and click __Confirm Removal__ after confirming that it is correct.

    ![Removal](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/cluster04.png)

!!! note
    - After removing a worker cluster, the workloads of the cluster will no longer be managed by this multicloud instance.
    - All multicloud workloads that have been distributed to this cluster will be automatically migrated to other worker clusters managed by this multicloud instance.

## More Operations

The system will automatically return to the worker cluster list. Click the __┇__ button on the right side of the cluster to perform operations such as __Pause/Resume Schedule__ , __Edit Cluster Labels__ , and __Modify Cluster Taints__ .

![More Operations](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/cluster05.png)

## Pause/Resume Scheduling

1. Click __Pause Schedule__ to pause the scheduling of the cluster. This means that new multicloud resources will not be distributed to this cluster, but the previously distributed resources to this cluster will not be affected.

2. At this point, click __Modify Cluster Taint__ and you will find that the cluster has been automatically tainted.

    > If you want to resume scheduling, you can also click __Resume Schedule__ or manually remove the corresponding cluster taint.

## Modify Cluster Taints

1. Click __Modify Cluster Taints__ to control the deployment of workloads, containers, and other resources in the cluster.

2. Enter the key-value information of the taint in the pop-up box. The value can be left empty.

3. Select the taint effect from the drop-down menu and click __OK__ .

    > Multiple taints can be added. Currently, two taint effects are supported:

    | Effect      | Description                                                  |
    | ----------- | ------------------------------------------------------------ |
    | NoSchedule  | Only nodes with tolerations matching this taint can be assigned to this cluster. |
    | NoExecute   | Define eviction behavior to deal with cluster failures. If the taint effect is defined as NoExecute, when the workload or pod is already running on this cluster, it will be evicted. If it is not running on this cluster, it will not be scheduled to this cluster either. |

   ![Modify Cluster Taint](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/cluster06.png)
