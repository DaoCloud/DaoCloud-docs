# cluster monitoring

Cluster monitoring can view the basic information of the cluster, the resource consumption in the cluster and the change trend of resource consumption over a period of time.

## Prerequisites

The cluster has [insight-agent installed](../../06UserGuide/01quickstart/installagent.md) and the application is in `running` state.

## View cluster details

1. Select `Scene Monitoring -> Cluster Monitoring` in the left navigation bar, and the information of the first selected cluster will be displayed by default.

    ![Container Monitoring](../../images/cluster01.png)

2. Select the target cluster in the cluster list to view the detailed information of the cluster

    - CPU usage: This metric refers to the ratio of the actual CPU usage of all Pod resources in the cluster to the total CPU usage of all nodes.
    - CPU Allocation Ratio: This metric refers to the ratio of the sum of the CPU requests of all Pods in the cluster to the total CPU of all nodes.
    - Memory usage: This metric refers to the ratio of the actual memory usage of all Pod resources in the cluster to the total memory of all nodes.
    - Memory allocation ratio: This metric refers to the ratio of the sum of the memory requests of all Pods in the cluster to the total memory of all nodes.

    ![Container Monitoring](../../images/cluster02.png)