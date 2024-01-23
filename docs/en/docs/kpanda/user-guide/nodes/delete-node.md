# Cluster node shrinkage

When the peak business period is over, in order to save resource costs, you can reduce the size of the cluster and unload redundant nodes, that is, node scaling. After a node is uninstalled, applications cannot continue to run on the node.

## Prerequisites

- The current operating user has the [`Cluster Admin`](../permissions/permission-brief.md) role authorization.
- Only through the container management module [created cluster](../clusters/create-cluster.md) can node expansion and contraction be supported, and the cluster accessed from the outside does not support this operation.
- Before uninstalling a node, you need to [pause scheduling the node](schedule.md), and expel the applications on the node to other nodes.
- Eviction method: log in to the controller node, and use the kubectl drain command to evict all Pods on the node. The safe eviction method allows the containers in the pod to terminate gracefully.

## Precautions

1. When cluster nodes shrink, they can only be uninstalled one by one, not in batches.

2. If you need to uninstall cluster controller nodes, you need to ensure that the final number of controller nodes is an **odd number**.

3. The **first controller** node cannot be offline when the cluster node shrinks. If it is necessary to perform this operation, please contact the after-sales engineer.

## Steps

1. On the __Clusters__ page, click the name of the target cluster.

    If the __Cluster Role__ has the tag __Access Cluster__ , it means that the cluster does not support node expansion and contraction.

    

2. Click __Node Management__ on the left navigation bar, find the node to be uninstalled, click __ⵗ__ and select __Remove Node__ .

    

3. Enter the node name, and click __Delete__ to confirm.

    