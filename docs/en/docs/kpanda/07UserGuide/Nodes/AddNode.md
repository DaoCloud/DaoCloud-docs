---
hide:
  - toc
---

# Cluster node expansion

As business applications continue to grow and cluster resources become increasingly tight, cluster nodes can be expanded based on KubeSpray. After capacity expansion, applications can run on the newly added nodes, alleviating resource pressure.

Only through the container management platform [created cluster](../Clusters/CreateCluster.md) can node expansion and contraction be supported, and the cluster accessed from the outside does not support this operation.

1. On the `Cluster List` page, click the name of the target cluster.

    If the `Cluster Role` has the tag `Access Cluster`, it means that the cluster does not support node expansion and contraction.

    ![Enter the cluster list page](../../images/addnode01.png)

2. Click `Node Management` in the left navigation bar, and then click `Access Node` in the upper right corner of the page.

    ![Node Management](../../images/addnode02.png)

3. Enter the host name and node IP and click `OK`.

    Click `➕ Add Work Node` to continue to access more nodes.

    ![Node Management](../../images/addnode03.png)

!!! note

    It takes about 20 minutes to access the node, please be patient.