---
hide:
  - toc
---

# add cluster

After the user creates a managed grid, but has not yet connected to any managed cluster, the grid is in the `not ready` state, and the user needs to add one or more clusters.

The specific operation steps are as follows:

1. Click `Cluster Management` on the left navigation bar, and click the `Add Cluster` button. Or in the grid list, click the `...` button on the far right, and select `Add Cluster` from the pop-up menu.

    ![Add cluster button](../../images/addcluster01.png)

2. In the cluster list that pops up, check the cluster to be added, and click the `OK` button to complete the cluster addition operation.

    ![Add cluster page](../../images/addcluster02.png)

!!! note

    1. Only **hosted grids** can add clusters, and dedicated grids cannot add clusters.

    2. Only clusters whose status is `Running` can be added to the grid, and clusters in other states cannot be selected or added.

    3. The process of adding clusters will last for a few seconds. Please pay attention to the "cluster statistics" information in the grid list to understand the changes in the number of normal clusters.