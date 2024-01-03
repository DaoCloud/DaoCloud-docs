---
hide:
  - toc
---

# Cluster node expansion

As business applications continue to grow and cluster resources become increasingly tight, cluster nodes can be expanded based on KubeSpray. After capacity expansion, applications can run on the newly added nodes, alleviating resource pressure.

Only through the container management module [created cluster](../clusters/create-cluster.md) can node expansion and contraction be supported, and the cluster accessed from the outside does not support this operation.

1. On the __Clusters__ page, click the name of the target cluster.

    If the __Cluster Role__ has the tag __Access Cluster__ , it means that the cluster does not support node expansion and contraction.

    

2. Click __Node Management__ in the left navigation bar, and then click __Access Node__ in the upper right corner of the page.

    

3. Enter the host name and node IP and click __OK__ .

    Click __➕ Add Work Node__ to continue to access more nodes.

    

!!! note

    It takes about 20 minutes to access the node, please be patient.