---
hide:
  - toc
---

# Uninstall/disconnect cluster access

Clusters created through the DCE 5.0 [Container Management](../../intro/WhatisKPanda.md) platform support the `Uninstall Cluster` operation, and the clusters directly connected from other environments support the `Uninstall` operation. The difference between the two is:

- The `uninstall cluster` operation will destroy the cluster and reset the data of all nodes under the cluster. All data will be destroyed, it is recommended to make a backup. A cluster must be recreated when needed later.
- `Detaching` just removes the cluster from the container management platform, it will not destroy the cluster, nor will it destroy the data. You can reconnect later when needed.

!!! note

    The current operating user should have the [`kpanda owner`](../../../ghippo/04UserGuide/01UserandAccess/global.md) permission to perform uninstallation or removal of access operations.

1. On the `Cluster List` page, find the cluster that needs to be uninstalled/unconnected, click `...` on the right and click `Uninstall Cluster`/`Unconnect` in the drop-down list.

    

2. Enter the cluster name to confirm and click `Delete`.

    

3. Return to the `Cluster List` page, and you can see that the status of the cluster has changed to `Deleting`. It may take a while to uninstall the cluster, please wait patiently.

    