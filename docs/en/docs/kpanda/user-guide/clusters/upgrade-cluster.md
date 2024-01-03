---
date: 2022-11-17
hide:
  - toc
---

# Cluster Upgrade

The Kubernetes Community packages a small version every quarter, and the maintenance cycle of each version is only about 9 months. Some major bugs or security holes will not be updated after the version stops maintenance. Manually upgrading cluster operations is cumbersome and places a huge workload on administrators.

In DCE, you can upgrade the Kubernetes cluster with one click through the web UI interface.

!!! danger

    After the version is upgraded, it will not be possible to roll back to the previous version, please proceed with caution.

!!! note

    - Kubernetes versions are denoted as __x.y.z__ , where __x__ is the major version, __y__ is the minor version, and __z__ is the patch version.
    - Cluster upgrades across minor versions are not allowed, e.g. a direct upgrade from 1.23 to 1.25 is not possible.
    - **Access clusters do not support version upgrades. If there is no "cluster upgrade" in the left navigation bar, please check whether the cluster is an access cluster. **
    - The global service cluster can only be upgraded through the terminal.
    - When upgrading a working cluster, the [Management Cluster](cluster-role.md#_3) of the working cluster should have been connected to the container management module and be running normally.

1. Click the name of the target cluster in the cluster list.

    

2. Then click __Cluster Operation and Maintenance__ -> __Cluster Upgrade__ in the left navigation bar, and click __Version Upgrade__ in the upper right corner of the page.

    

3. Select the version that can be upgraded, and enter the cluster name to confirm.

      

4. After clicking __OK__ , you can see the upgrade progress of the cluster.

      

5. The cluster upgrade is expected to take 30 minutes. You can click the __Real-time Log__ button to view the detailed log of the cluster upgrade.

    