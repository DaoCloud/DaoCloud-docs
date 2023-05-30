# Optimize failover latency sensitivity

Multi-cloud supports automatic failover of applications across clusters, thereby ensuring the stability of applications deployed in multiple clusters. The delay time of failover is mainly affected by the following two dimensions of metrics, and a combination of configurations is required to finally achieve the effect of delay sensitivity.

1. Cluster dimension: mark the cluster as unhealthy inspection time, cluster eviction tolerance time
2. Workload dimension: cluster taint tolerance duration

## Failover feature introduction

After enabling failover in DCE 5.0 multi-cloud orchestration, the following parameter configuration options are available:

| parameter | definition | description | field name EN | field name ZH | default value |
| ----------------------------------- | -------------- ---------------- | --------------------------------- --------------------------- | ---------------------- ------------------------------ | ------------------- ----- | ------ |
| ClusterMonitorPeriod | Check Period Interval | Time Interval for Checking Cluster Status | Check Internal | Check Time Interval | 60s |
| ClusterMonitorGracePeriod | The duration of an unhealthy check to mark the cluster during operation | The cluster is running, and if the health status information of the cluster is not obtained beyond this configuration time, the cluster will be marked as unhealthy | The runtime marks the duration of an unhealthy check | The runtime marks the duration of an unhealthy check | 40s |
| ClusterStartupGracePeriod | Mark health check duration at startup | Mark health check duration at startup | Mark health check duration at startup | Mark health check duration at startup | 600s |
| FailoverEvictionTimeout | Eviction tolerance time | After the cluster is marked as unhealthy, the cluster will be marked as unhealthy, and enter the eviction state (the cluster will increase the eviction stain) | Eviction tolerance time | Eviction tolerance time | 30s |
| ClusterTaintEvictionRetryFrequency | Graceful eviction timeout duration | After entering the graceful eviction queue, the longest waiting time, it will be deleted immediately after timeout | Graceful ejection timeout duration | Graceful ejection timeout duration | 5s |

## Timeline of workload evictions

Briefly explain the following figure: We stipulate that the API of the cluster is called once every 10s to record the health status of the cluster. When the four results are all healthy, we consider the cluster to be in a healthy state.
At this time, we disconnect the TCP between DCE and the cluster APIserver within 10s-20s. If the health status of the cluster is not obtained, the cluster will be considered abnormal.
If the cluster does not return to health within the specified time, it will be marked as unhealthy and stained with NoSchedule. After the specified eviction tolerance time is exceeded, it will be stained with NoExecute and finally evicted.

<!--screenshot-->

## Optimized configuration for multi-cloud instances

For multi-cloud instances, you need to enter the Advanced Settings -> Failover section. For the following configurations, you can refer to the above figure to fill in the parameter information.

<!--screenshot-->

## Configuration optimization for multi-cloud workloads

The multi-cloud workload is mainly related to its deployment policy (PP), and the corresponding cluster taint tolerance period needs to be modified in the deployment policy.

<!--screenshot-->