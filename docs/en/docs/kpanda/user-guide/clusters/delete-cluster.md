---
hide:
  - toc
---

# Uninstall/disconnect cluster access

The cluster** created through the DCE 5.0 [container management](../../intro/what.md) platform ** supports the operation of `unloading the cluster` or `disconnecting`, and directly** accessing from other environments The cluster** only supports the `unjoin` operation.

The difference between the two is:

- The `uninstall cluster` operation will destroy the cluster and reset the data of all nodes under the cluster. All data will be destroyed, it is recommended to make a backup. A cluster must be recreated when needed later.
- `Detaching` just removes the cluster from the container management module, it will not destroy the cluster, nor will it destroy the data. You can reconnect later when needed.

!!! note

    - The current operating user should have [Admin](../../../ghippo/user-guide/access-control/role.md) or [`Kpanda Owner`](../../../ghippo/user-guide/access-control/global.md) permissions to perform uninstall or remove access operations.
    - Before uninstalling the cluster, you should turn off `Cluster Deletion Protection` in `Cluster Settings`->`Advanced Configuration`, otherwise the `Uninstall Cluster` option will not be displayed.

1. On the `Cluster List` page, find the cluster that needs to be uninstalled/unconnected, click `...` on the right and click `Uninstall Cluster`/`Unconnect` in the drop-down list.

    

2. Enter the cluster name to confirm and click `Delete`.

    
    

3. Return to the `Cluster List` page, and you can see that the status of the cluster has changed to `Deleting`. It may take a while to uninstall the cluster, please wait patiently.

    