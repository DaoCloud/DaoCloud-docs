---
hide:
  - toc
---

# access cluster

After creating a multicloud instance, you need to connect to the working cluster first.

1. Click `Working Cluster Management` on the left navigation bar to enter the multicloud cluster management page. The list includes all working clusters in the current multicloud instance. If you want to connect to other working clusters, click `Access Cluster` in the upper right corner ` button. If you need to connect the network between the working clusters, please create a grid instance on the service grid page and manage the following working clusters; for details, please [view document](https://docs.daocloud.io/mspider/ user-guide/multicluster/cluster-interconnect/).

    <!--screenshot-->

2. A page will pop up. The clusters in the page list are the clusters in the container management. After selecting a working cluster, click `Confirm`. If the clusters in the current list do not meet the requirements, it is also supported to access new clusters in the container management module.

    <!--screenshot-->

3. Return to the working cluster list, indicating that the creation is successful. Click the `…` button on the right side of the list to perform more operations on the cluster: suspend/resume scheduling, edit cluster labels, modify cluster stains, and remove.

    <!--screenshot-->

    - Click `Pause Scheduling` to stop the scheduling of the schedulable cluster. At this time, click to modify the cluster stain and find that it is automatically stained (as shown in the figure below). If you want to restore scheduling, you can also click Resume Scheduling, or remove the cluster stain, and the cluster becomes schedulable.

        <!--screenshot-->

    - Click `Modify cluster taint` to facilitate us to control which clusters can deploy workloads, containers, etc. Enter the key-value information of the stain in the pop-up box, the value can be empty, select the stain effect from the drop-down, click `OK`, it supports adding multiple stains. Currently supports two stain effects:

        | Effect | Description |
        | ---------- | -------------------------------------- ---------------------- |
        | NoSchedule | Indicates that only nodes with a tolerance matching this taint can be assigned to the cluster |
        | NoExecute | Defines eviction behavior in case of cluster failure. If the taint effect is defined as NoExecute, when the workload or pod is already running on the cluster, it will be evicted; if it is not running on the cluster, it will not be scheduled to the cluster again |

        <!--screenshot-->