# Insight 参考指标说明

本文中的指标是基于社区的 kube-prometheus 的基础之上整理而成。
目前涵盖了 Cluster、Node、Namespace、Workload 等多个层面的指标。
本文枚举了一些常用的指标名、中文描述和单位，以便索引。

## 集群（Cluster）

| 指标名                             | 中文描述                      | 单位   |
| ---------------------------------- | ----------------------------- | ------ |
| cluster_cpu_utilization            | 集群 CPU 使用率               |        |
| cluster_cpu_total                  | 集群 CPU 总量                 | Core   |
| cluster_cpu_usage                  | 集群 CPU 用量                 | Core   |
| cluster_cpu_requests_commitment    | 集群 CPU 分配率               |        |
| cluster_memory_utilization         | 集群内存使用率                |        |
| cluster_memory_usage               | 集群内存使用量                | Byte   |
| cluster_memory_available           | 集群可用内存                  | Byte   |
| cluster_memory_requests_commitment | 集群内存分配率                |        |
| cluster_memory_total               | 集群内存可用量                | Byte   |
| cluster_net_utilization            | 集群网络数据传输速率          | Byte/s |
| cluster_net_bytes_transmitted      | 集群网络数据发送 (上行) 速率    | Byte/s |
| cluster_net_bytes_received         | 集群网络数据接受 (下行) 速率    | Byte/s |
| cluster_disk_read_iops             | 集群磁盘每秒读次数            | 次/s   |
| cluster_disk_write_iops            | 集群磁盘每秒写次数            | 次/s   |
| cluster_disk_read_throughput       | 集群磁盘每秒读取数据量        | Byte/s |
| cluster_disk_write_throughput      | 集群磁盘每秒写入数据量        | Byte/s |
| cluster_disk_size_capacity         | 集群磁盘总容量                | Byte   |
| cluster_disk_size_available        | 集群磁盘可用大小              | Byte   |
| cluster_disk_size_usage            | 集群磁盘使用量                | Byte   |
| cluster_disk_size_utilization      | 集群磁盘使用率                |        |
| cluster_node_total                 | 集群节点总数                  | 个     |
| cluster_node_online                | 集群节点总数                  | 个     |
| cluster_node_offline_count         | 集群失联的节点个数            | 个     |
| cluster_pod_count                  | 集群 Pod 总数                 | 个     |
| cluster_pod_running_count          | 集群正常运行 Pod 个数         | 个     |
| cluster_pod_abnormal_count         | 集群异常运行 Pod 个数         | 个     |
| cluster_deployment_count           | 集群 Deployment 总数          | 个     |
| cluster_deployment_normal_count    | 集群正常的 Deployment 总数    | 个     |
| cluster_deployment_abnormal_count  | 集群异常的 Deployment 总数    | 个     |
| cluster_statefulset_count          | 集群 StatefulSet 个数         | 个     |
| cluster_statefulset_normal_count   | 集群正常运行 StatefulSet 个数 | 个     |
| cluster_statefulset_abnormal_count | 集群异常运行 StatefulSet 个数 | 个     |
| cluster_daemonset_count            | 集群 DaemonSet 个数           | 个     |
| cluster_daemonset_normal_count     | 集群正常运行 DaemonSet 个数   | 个     |
| cluster_daemonset_abnormal_count   | 集群异常运行 DaemonSet 个数   | 个     |
| cluster_job_count                  | 集群 Job 总数                 | 个     |
| cluster_job_normal_count           | 集群正常运行 Job 个数         | 个     |
| cluster_job_abnormal_count         | 集群异常运行 Job 个数         | 个     |

!!! tip

    使用率一般是（0,1] 区间的数字（例如：0.21，而不是 21%）

## 节点（Node）

| 指标名                          | 中文描述                   | 单位   |
| ------------------------------- | -------------------------- | ------ |
| node_cpu_utilization            | 节点 CPU 使用率            |        |
| node_cpu_total                  | 节点 CPU 总量              | Core   |
| node_cpu_usage                  | 节点 CPU 用量              | Core   |
| node_cpu_requests_commitment    | 节点 CPU 分配率            |        |
| node_memory_utilization         | 节点内存使用率             |        |
| node_memory_usage               | 节点内存使用量             | Byte   |
| node_memory_requests_commitment | 节点内存分配率             |        |
| node_memory_available           | 节点可用内存               | Byte   |
| node_memory_total               | 节点内存可用量             | Byte   |
| node_net_utilization            | 节点网络数据传输速率       | Byte/s |
| node_net_bytes_transmitted      | 节点网络数据发送 (上行) 速率 | Byte/s |
| node_net_bytes_received         | 节点网络数据接受 (下行) 速率 | Byte/s |
| node_disk_read_iops             | 节点磁盘每秒读次数         | 次/s   |
| node_disk_write_iops            | 节点磁盘每秒写次数         | 次/s   |
| node_disk_read_throughput       | 节点磁盘每秒读取数据量     | Byte/s |
| node_disk_write_throughput      | 节点磁盘每秒写入数据量     | Byte/s |
| node_disk_size_capacity         | 节点磁盘总容量             | Byte   |
| node_disk_size_available        | 节点磁盘可用大小           | Byte   |
| node_disk_size_usage            | 节点磁盘使用量             | Byte   |
| node_disk_size_utilization      | 节点磁盘使用率             |        |

## 工作负载（Workload）

目前支持的工作负载类型包括：Deployment、StatefulSet、DaemonSet、Job 和 CronJob。

| 指标名                         | 中文描述                       | 单位   |
| ------------------------------ | ------------------------------ | ------ |
| workload_cpu_usage             | 工作负载 CPU 用量              | Core   |
| workload_cpu_limits            | 工作负载 CPU 限制量            | Core   |
| workload_cpu_requests          | 工作负载 CPU 请求量            | Core   |
| workload_cpu_utilization       | 工作负载 CPU 使用率            |        |
| workload_memory_usage          | 工作负载内存使用量             | Byte   |
| workload_memory_limits         | 工作负载 内存 限制量           | Byte   |
| workload_memory_requests       | 工作负载 内存 请求量           | Byte   |
| workload_memory_utilization    | 工作负载内存使用率             |        |
| workload_memory_usage_cached   | 工作负载内存使用量（包含缓存） | Byte   |
| workload_net_bytes_transmitted | 工作负载网络数据发送速率       | Byte/s |
| workload_net_bytes_received    | 工作负载网络数据接受速率       | Byte/s |
| workload_disk_read_throughput  | 工作负载磁盘每秒读取数据量     | Byte/s |
| workload_disk_write_throughput | 工作负载磁盘每秒写入数据量     | Byte/s |

1. 此处计算 workload 总量
2. 通过 `workload_cpu_usage{workload_type="deployment", workload="prometheus"}` 的方式获取指标
3. `workload_pod_utilization` 计算规则： `workload_pod_usage / workload_pod_request`

## 容器组（Pod）

| 指标名                    | 中文描述                     | 单位   |
| ------------------------- | ---------------------------- | ------ |
| pod_cpu_usage             | 容器组 CPU 用量              | Core   |
| pod_cpu_limits            | 容器组 CPU 限制量            | Core   |
| pod_cpu_requests          | 容器组 CPU 请求量            | Core   |
| pod_cpu_utilization       | 容器组 CPU 使用率            |        |
| pod_memory_usage          | 容器组内存使用量             | Byte   |
| pod_memory_limits         | 容器组内存限制量             | Byte   |
| pod_memory_requests       | 容器组内存请求量             | Byte   |
| pod_memory_utilization    | 容器组内存使用率             |        |
| pod_memory_usage_cached   | 容器组内存使用量（包含缓存） | Byte   |
| pod_net_bytes_transmitted | 容器组网络数据发送速率       | Byte/s |
| pod_net_bytes_received    | 容器组网络数据接受速率       | Byte/s |
| pod_disk_read_throughput  | 容器组磁盘每秒读取数据量     | Byte/s |
| pod_disk_write_throughput | 容器组磁盘每秒写入数据量     | Byte/s |

通过 `pod_cpu_usage{workload_type="deployment", workload="prometheus"}` 获取名为 prometheus 的 Deployment 所拥有的所有 Pod 的 CPU 使用率。

## Span 指标

| 指标名                                                | 中文描述            | 单位 |
|----------------------------------------------------|-----------------| ---- |
| calls_total                                        | 服务请求总数          |      |
| duration_milliseconds_bucket                       | 服务延时直方图         |      |
| duration_milliseconds_sum                          | 服务总延时           | ms   |
| duration_milliseconds_count                        | 服务延时记录条数        |      |
| otelcol_processor_groupbytrace_spans_released      | 采集到的 span 数     |      |
| otelcol_processor_groupbytrace_traces_released     | 采集到的 trace 数    |      |
| traces_service_graph_request_total                 | 服务请求总数 (拓扑功能使用)  |      |
| traces_service_graph_request_server_seconds_sum    | 服务总延时 (拓扑功能使用)   | ms   |
| traces_service_graph_request_server_seconds_bucket | 服务延时直方图 (拓扑功能使用) |      |
| traces_service_graph_request_server_seconds_count | 服务请求总数 (拓扑功能使用)  |      |
