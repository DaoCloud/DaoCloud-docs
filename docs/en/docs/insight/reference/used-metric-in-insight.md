---
MTPE: ModetaNiu
DATE: 2024-09-18
---

# Insight Reference Metric

The metrics in this article are organized based on the community's kube-prometheus framework. 
Currently, it covers metrics from multiple levels, including Cluster, Node, Namespace, and Workload. 
This article lists some commonly used metrics, their descriptions, and units for easy reference.

## Cluster

| Metric Name | Description | Unit |
| ---------------------------------- | ----------------------------- | ------ |
| cluster_cpu_utilization | Cluster CPU Utilization |        |
| cluster_cpu_total | Total CPU in Cluster | Core |
| cluster_cpu_usage | CPU Used in Cluster | Core |
| cluster_cpu_requests_commitment | CPU Allocation Rate in Cluster |        |
| cluster_memory_utilization | Cluster Memory Utilization |        |
| cluster_memory_usage | Memory Usage in Cluster | Byte   |
| cluster_memory_available | Available Memory in Cluster | Byte   |
| cluster_memory_requests_commitment | Memory Allocation Rate in Cluster |        |
| cluster_memory_total | Total Memory in Cluster | Byte   |
| cluster_net_utilization | Network Data Transfer Rate in Cluster | Byte/s |
| cluster_net_bytes_transmitted | Network Data Transmitted in Cluster (Upstream) | Byte/s |
| cluster_net_bytes_received | Network Data Received in Cluster (Downstream) | Byte/s |
| cluster_disk_read_iops | Disk Read IOPS in Cluster | times/s |
| cluster_disk_write_iops | Disk Write IOPS in Cluster | times/s |
| cluster_disk_read_throughput | Disk Read Throughput in Cluster | Byte/s |
| cluster_disk_write_throughput | Disk Write Throughput in Cluster | Byte/s |
| cluster_disk_size_capacity | Total Disk Capacity in Cluster | Byte   |
| cluster_disk_size_available | Available Disk Size in Cluster | Byte   |
| cluster_disk_size_usage | Disk Usage in Cluster | Byte   |
| cluster_disk_size_utilization | Disk Utilization in Cluster |        |
| cluster_node_total | Total Nodes in Cluster | units  |
| cluster_node_online | Online Nodes in Cluster | units  |
| cluster_node_offline_count | Count of Offline Nodes in Cluster | units  |
| cluster_pod_count | Total Pods in Cluster | units  |
| cluster_pod_running_count | Count of Running Pods in Cluster | units  |
| cluster_pod_abnormal_count | Count of Abnormal Pods in Cluster | units  |
| cluster_deployment_count | Total Deployments in Cluster | units  |
| cluster_deployment_normal_count | Count of Normal Deployments in Cluster | units  |
| cluster_deployment_abnormal_count | Count of Abnormal Deployments in Cluster | units  |
| cluster_statefulset_count | Count of StatefulSets in Cluster | units  |
| cluster_statefulset_normal_count | Count of Normal StatefulSets in Cluster | units  |
| cluster_statefulset_abnormal_count | Count of Abnormal StatefulSets in Cluster | units  |
| cluster_daemonset_count | Count of DaemonSets in Cluster  | units  |
| cluster_daemonset_normal_count | Count of Normal DaemonSets in Cluster | units  |
| cluster_daemonset_abnormal_count | Count of Abnormal DaemonSets in Cluster | units  |
| cluster_job_count | Total Jobs in Cluster | units  |
| cluster_job_normal_count | Count of Normal Jobs in Cluster  | units  |
| cluster_job_abnormal_count | Count of Abnormal Jobs in Cluster | units  |

!!! tip

    Utilization is generally a number in the range (0,1] (e.g., 0.21, not 21%)

## Node

| Metric Name                        | Description           | Unit   |
| ---------------------------------- | ----------------------------- | ------ |
| node_cpu_utilization | Node CPU Utilization |        |
| node_cpu_total | Total CPU in Node | Core   |
| node_cpu_usage | CPU Usage in Node | Core   |
| node_cpu_requests_commitment | CPU Allocation Rate in Node |        |
| node_memory_utilization | Node Memory Utilization |        |
| node_memory_usage | Memory Usage in Node | Byte   |
| node_memory_requests_commitment | Memory Allocation Rate in Node |        |
| node_memory_available | Available Memory in Node | Byte   |
| node_memory_total | Total Memory in Node | Byte   |
| node_net_utilization | Network Data Transfer Rate in Node | Byte/s |
| node_net_bytes_transmitted | Network Data Transmitted in Node (Upstream) | Byte/s |
| node_net_bytes_received | Network Data Received in Node (Downstream) | Byte/s |
| node_disk_read_iops | Disk Read IOPS in Node | times/s |
| node_disk_write_iops | Disk Write IOPS in Node | times/s |
| node_disk_read_throughput | Disk Read Throughput in Node | Byte/s |
| node_disk_write_throughput | Disk Write Throughput in Node | Byte/s |
| node_disk_size_capacity | Total Disk Capacity in Node | Byte   |
| node_disk_size_available | Available Disk Size in Node | Byte   |
| node_disk_size_usage | Disk Usage in Node | Byte   |
| node_disk_size_utilization | Disk Utilization in Node |        |

## Workload

The currently supported workload types include: Deployment, StatefulSet, DaemonSet, Job, and CronJob.

| Metric Name | Description | Unit   |
| ---------------------------------- | ----------------------------- | ------ |
| workload_cpu_usage | Workload CPU Usage | Core   |
| workload_cpu_limits | Workload CPU Limit | Core   |
| workload_cpu_requests | Workload CPU Requests | Core   |
| workload_cpu_utilization | Workload CPU Utilization |        |
| workload_memory_usage | Workload Memory Usage | Byte   |
| workload_memory_limits | Workload Memory Limit | Byte   |
| workload_memory_requests | Workload Memory Requests | Byte   |
| workload_memory_utilization | Workload Memory Utilization |        |
| workload_memory_usage_cached | Workload Memory Usage (including cache) | Byte   |
| workload_net_bytes_transmitted | Workload Network Data Transmitted Rate | Byte/s |
| workload_net_bytes_received | Workload Network Data Received Rate | Byte/s |
| workload_disk_read_throughput | Workload Disk Read Throughput  | Byte/s |
| workload_disk_write_throughput | Workload Disk Write Throughput | Byte/s |

1. Total workload is calculated here.
2. Metrics can be obtained using `workload_cpu_usage{workload_type="deployment", workload="prometheus"}`.
3. Calculation rule for `workload_pod_utilization`: `workload_pod_usage / workload_pod_request`.

## Pod

| Metric Name                        | Description           | Unit   |
| ---------------------------------- | ----------------------------- | ------ |
| pod_cpu_usage | Pod CPU Usage | Core   |
| pod_cpu_limits | Pod CPU Limit | Core   |
| pod_cpu_requests | Pod CPU Requests | Core   |
| pod_cpu_utilization | Pod CPU Utilization |        |
| pod_memory_usage | Pod Memory Usage | Byte   |
| pod_memory_limits | Pod Memory Limit | Byte   |
| pod_memory_requests | Pod Memory Requests | Byte   |
| pod_memory_utilization | Pod Memory Utilization |        |
| pod_memory_usage_cached | Pod Memory Usage (including cache) | Byte   |
| pod_net_bytes_transmitted | Pod Network Data Transmitted Rate | Byte/s |
| pod_net_bytes_received | Pod Network Data Received Rate | Byte/s |
| pod_disk_read_throughput | Pod Disk Read Throughput | Byte/s |
| pod_disk_write_throughput | Pod Disk Write Throughput | Byte/s |

You can obtain the CPU usage of all Pods belonging to the Deployment named prometheus by using `pod_cpu_usage{workload_type="deployment", workload="prometheus"}`.

## Span Metrics

| Metric Name                                                | Description         | Unit |
|----------------------------------------------------------|-----------------------------|------|
| calls_total | Total Service Requests |      |
| duration_milliseconds_bucket | Service Latency Histogram |      |
| duration_milliseconds_sum | Total Service Latency       | ms   |
| duration_milliseconds_count | Number of Latency Records |      |
| otelcol_processor_groupbytrace_spans_released | Number of Collected Spans |      |
| otelcol_processor_groupbytrace_traces_released | Number of Collected Traces |      |
| traces_service_graph_request_total | Total Service Requests (Topology Feature) |      |
| traces_service_graph_request_server_seconds_sum | Total Latency (Topology Feature) | ms   |
| traces_service_graph_request_server_seconds_bucket | Service Latency Histogram (Topology Feature) |      |
| traces_service_graph_request_server_seconds_count | Total Service Requests (Topology Feature) |      |