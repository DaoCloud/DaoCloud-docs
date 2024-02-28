---
hide:
  - toc
---

# remove cluster

If you want to remove a cluster from the hosting mesh, you can follow the steps below to remove the cluster.

1. Click __Cluster Management__ in the left navigation bar, and click the __Remove__ button on the right side of the cluster list. Or in the mesh list, click the __...__ button on the far right, and select __Remove__ in the pop-up menu.

    

2. In the pop-up window, after confirming that the information is correct, click __OK__ .

    

    To remove a cluster, some pre-operations need to be completed, such as:

    - Unload injected sidecars.
    - Clear cluster related mesh gateways.
    - For other pre-operations, please follow the on-screen prompts.

!!! warning

    If you remove the cluster, you will not be able to centrally manage the cluster through the mesh. In addition, related information such as cluster logs may be lost. Please operate with caution.