# Node taint management

Taint can make a node exclude a certain type of Pod and prevent Pod from being scheduled on the node. One or more taints can be applied to each node, and Pods that cannot tolerate these taints will not be scheduled on that node. For more details about taints, refer to the official Kubernetes documentation [Taints and Tolerance](https://kubernetes.io/zh-cn/docs/concepts/scheduling-eviction/taint-and-toleration/).

## Precautions

1. The current operating user should have [`NS Edit`](../Permissions/PermissionBrief.md) role authorization or other higher permissions.
2. After adding a taint to a node, only Pods that can tolerate the taint can be scheduled to the node. <!--For how to set tolerance for Pod, please refer to -->

## Steps

1. Find the target cluster on the `Cluster List` page, and click the cluster name to enter the `Cluster Overview` page.

    ![click cluster name](../../images/taint-click--cluster-name.png)

2. In the left navigation bar, click `Node Management`, find the node that needs to modify the taint, click the `ⵗ` operation icon on the right and click the `Modify taint` button.

    ![Taint Change](../../images/taint-change.png)

3. Enter the key value information of the stain in the pop-up box, select the stain effect, and click `OK`.

    Click `➕ Add` to add multiple stains to the node, and click `X` on the right side of the stain effect to delete the stain.

    Currently supports three stain effects:

    - NoSchedule: Pods that cannot tolerate a taint will not be scheduled on nodes with the taint.
    - PreferNoSchedule: **Try to avoid** Pods that cannot tolerate a taint will not be scheduled on nodes with the taint.
    - NoExecute: Keep the status quo. Pods that cannot tolerate a taint will not be evicted if they were already running on the node before the taint was set. Pods that cannot tolerate a taint will not be scheduled on the node if they were not running on the node before the taint was set on the node.

        ![Modify taint](../../images/taint-add-remove.png)