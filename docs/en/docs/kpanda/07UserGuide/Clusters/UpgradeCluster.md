---
date: 2022-11-17
hide:
  - toc
---

# cluster upgrade

The Kubernetes community releases a small version every quarter, and the maintenance cycle of each version is only about 9 months.
Some major bugs or security holes will not be updated after the version stops maintenance. Manually upgrading cluster operations is cumbersome and places a huge workload on administrators.

In DCE, you can upgrade a Kubernetes cluster with one click using a graphical interface.

!!! note

    Kubernetes versions are denoted by `x.y.z`, where `x` is the major version, `y` is the minor version, and `z` is the patch version, and cluster upgrades across minor versions are not allowed.

1. Enter the cluster list, select the cluster to be updated, click the `...` icon on the right side of the cluster, and select `Cluster Upgrade` in the drop-down operation.

    ![upgrade cluster](../../images/upgradecluster01.png)

2. According to the version of your current cluster, the system will automatically display the version that the current cluster can upgrade in `upgradeable version`.

    !!! danger

        After the version is upgraded, it will not be possible to roll back to the previous version, please proceed with caution.

      ![upgradeable version](../../images/upgradecluster02.png)

3. After selecting `upgradeable version`, enter the cluster name, click `OK` to return to the cluster list, and you can see in the cluster list that the cluster status at this time is `upgrading`.

4. The cluster upgrade is expected to take 30 minutes. You can click the `Real-time Log` button to view the detailed log of the cluster upgrade.

    ![Real-time log](../../images/createcluster07.png)