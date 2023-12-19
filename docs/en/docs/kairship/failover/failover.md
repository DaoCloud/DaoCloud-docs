# Introduction to failover function

When a cluster fails, the pod replicas in the cluster will be automatically migrated to other available clusters to ensure service stability.

**Prerequisites**

The scheduling policy of multicloud workloads can only choose aggregation mode or dynamic weight mode, and the failover feature can only take effect at this time.

## Enable failover

1. Enter the Multicloud Management module, click __System Settings__ -> __Advanced Configuration__ , failover can realize copy scheduling between multiple clusters, it is disabled by default, please enable it if necessary.

    <!--screenshot-->

2. The following parameters are for the cluster, click to enable failover and save.

    | Parameter | Definition | Description | Field Name EN | Field Name ZH | Default |
    | ----------------------------------- | -------------- ---------------- | --------------------------------- -------------------------------------------------- ---- | --------------------------------------------- ------- | ------------------------ | ------ |
    | ClusterMonitorPeriod | Check Period Interval | Time Interval for Checking Cluster Status | Check Internal | Check Time Interval | 60s |
    | ClusterMonitorGracePeriod | The duration of an unhealthy check to mark the cluster during operation | The cluster is running, and if the health status information of the cluster is not obtained beyond this configuration time, the cluster will be marked as unhealthy | The runtime marks the duration of an unhealthy check | The runtime marks the duration of an unhealthy check | 40s |
    | ClusterStartupGracePeriod | Mark health check duration at startup | Mark health check duration at startup | Mark health check duration at startup | Mark health check duration at startup | 600s |
    | FailoverEvictionTimeout | Eviction tolerance time | After the cluster is marked as unhealthy, the cluster will be marked as unhealthy, and enter the eviction state (the cluster will increase the eviction stain) | Eviction tolerance time | Eviction tolerance time | 30s |
    | ClusterTaintEvictionRetryFrequency | Graceful eviction timeout duration | After entering the graceful eviction queue, the longest waiting time, it will be deleted immediately after timeout | Graceful ejection timeout duration | Graceful ejection timeout duration | 5s |

## Verify failover

1. Create a multicloud stateless load, choose to deploy on multiple clusters, and select the aggregation/dynamic weight mode for the scheduling strategy.

    <!--screenshot-->

2. If a cluster is unhealthy at this time and has not recovered within the specified time range, the cluster will be stained and enter the eviction state (this document will manually stain a cluster)

    <!--screenshot-->

3. At this time, the Pods with no state load will be migrated according to the resources of the remaining clusters. Eventually there will be no Pods in an unhealthy (tainted) cluster.

    <!--screenshot-->