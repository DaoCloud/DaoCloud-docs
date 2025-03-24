# VictoriaMetrics Resource Planning

The resource consumption of `VictoriaMetrics` components in actual `Prometheus RemoteWrite` usage is impacted by the number of containers in the cluster and the volume of metrics. This can lead to `vminsert` and `vmstorage` exceeding their allocated CPU and memory limits. To ensure stable operation of `VictoriaMetrics` components across clusters of different sizes, resources need to be adjusted according to the actual scale of the cluster.

## Test Results

After continuous monitoring of metrics from `Prometheus RemoteWrite` to `VictoriaMetrics`, we observed that the resource usage of `VictoriaMetrics` components is generally positively correlated with the **ingestion rate**, which is also positively correlated with the number of Pods.

- **Ingestion_rate**：sum(rate(vm_rows_inserted_total{job="vminsert-insight-victoria-metrics-k8s-stack"}[1m]))
- **Pod 数量**：sum(kube_pod_info)

This shows how many data points per second are inserted into `vminsert` (replication is not accounted for in this metric).
If you need to know the ingestion rate including the replication factor, use:  
`sum(rate(vm_vminsert_metrics_read_total{job="vmstorage-insight-victoria-metrics-k8s-stack"}[1m]))`  
This query shows how many data points `vmstorage` reads from `vminsert`.

Through long-term testing across multiple clusters, the difference between these two ingestion rates is minor. Therefore, for simplicity, we use the data points per second inserted into `vminsert` as the primary ingestion rate in this document.

## Calculation Methods

### Resource Usage Formulas

| **Component** | **Resource** | **Formula** | **Notes** |
|---------------|--------------|-------------|-----------|
| **vminsert** | CPU | (ingestion_rate / 100k + 0.07) * 2 | |
| | Ingress bandwidth (KB/s) | 60 * ingestion_rate / 1k + 120 | |
| | Outgoing bandwidth (KB/s) | 20 * ingestion_rate / 1k + 40 | Approximately 1/3 of ingress bandwidth |
| **vmstorage** | CPU | (2 * ingestion_rate / 100k - 0.02) * 2 | |
| | Memory (MB) | 100 * ingestion_rate / 1k * 2 | |
| | Ingress bandwidth (KB/s) | 30 * ingestion_rate / 1k | |

**Parameter explanations:**

1. The `* 2` multiplier in the CPU formula reserves 50% idle CPU to reduce performance bottlenecks during peak load.
2. The `* 2` multiplier in the memory formula reserves 50% idle memory to lower the risk of OOM (Out of Memory) crashes during usage spikes.

### Cluster Sizing

Based on current observations, the approximate relationship between cluster size and ingestion rate is:  
**ingestion_rate = (Pod count * 1000) / 120**

## Resource Planning Reference

The following table shows the approximate resource requirements for `VictoriaMetrics` components at different cluster sizes under Prometheus RemoteWrite scenarios:

| **Cluster Size (Pod Count)** | **ingestion_rate** | **vminsert CPU (core)** | **vminsert Memory** | **vminsert Ingress Bandwidth** | **vminsert Outgoing Bandwidth** | **vmstorage CPU (core)** | **vmstorage Memory** | **vmstorage Ingress Bandwidth** |
|-------|--------|-----------|----------|-----------|----------|----------|---------|-----------|
| 100 | 8k | 0.3 | 160 MB | 600 KB/s | 200 KB/s | 0.28 | 1.6 GB | 240 KB/s |
| 200 | 17k | 0.48 | 340 MB | 1.1 MB/s | 380 KB/s | 0.64 | 3.3 GB | 510 KB/s |
| 300 | 25k | 0.64 | 500 MB | 1.6 MB/s | 540 KB/s | 0.96 | 4.9 GB | 750 KB/s |
| 400 | 34k | 0.84 | 500 MB | 2.1 MB/s | 720 KB/s | 1.32 | 6.7 GB | 1,020 KB/s |
| 500 | 42k | 0.98 | 500 MB | 2.6 MB/s | 880 KB/s | 1.64 | 8.2 GB | 1.3 MB/s |
| 800 | 67k | 1.48 | 500 MB | 4.1 MB/s | 1.4 MB/s | 2.64 | 13.1 GB | 2 MB/s |
| 1000 | 84k | 1.82 | 500 MB | 5.1 MB/s | 1.7 MB/s | 3.32 | 16.4 GB | 2.5 MB/s |
| 2000 | 167k | 3.48 | 500 MB | 10 MB/s | 3.3 MB/s | 6.64 | 32.6 GB | 4.9 MB/s |

**Notes:**

1. The Pod count refers to the number of stable-running Pods in clusters where `insight-agent` is installed. If there are frequent Pod restarts, it can cause short-term metric spikes, requiring temporary resource adjustments.
2. The table shows resource usage values where components run stably at the given scale. For more precise requirements, it is recommended to monitor actual usage in a production environment before fine-tuning resource settings.
3. During Prometheus RemoteWrite operations, `vminsert` and `vmselect` are primarily involved. Currently, there’s no resource planning guideline for `vmselect`; it should be evaluated based on query load.

## Recommendations for Scaling Components

1. Scaling out `vminsert` replicas increases ingestion capacity, as incoming data can be distributed across more `vminsert` nodes.
2. Scaling out `vmstorage` replicas or adding more CPU and memory can increase the number of active time series it can handle. Replica scaling is preferred, as it improves query performance and cluster stability, especially under high churn rates.
3. Increasing `vmselect` CPU and memory improves performance for complex queries, particularly those processing large numbers of time series or raw samples. Adding `vmselect` replicas improves query concurrency by distributing requests across more nodes.
4. Under standard installation modes, `VictoriaMetrics` uses default configurations:
   - The `vm_concurrent_insert_capacity` defaults to twice the value of `vm_available_cpu_cores{job="vminsert-insight-victoria-metrics-k8s-stack"}`.
   - The `vm_concurrent_select_capacity` defaults to twice the value of `vm_available_cpu_cores{job="vmselect-insight-victoria-metrics-k8s-stack"}`.
   - If CPU resources are insufficient, `vm_concurrent_insert_current` or `vm_concurrent_select_current` may hit their limits. In that case, you can increase the limits in the `CR` by adding the following:

```shell
# In the vmcluster CR, under spec.vminsert.extraArgs:
maxConcurrentInserts: "32"

# In the vmcluster CR, under spec.vmselect.extraArgs:
search.maxConcurrentRequests: "16"
```

## Reference Documentation

- [Cluster resizing and scalability](https://docs.victoriametrics.com/cluster-victoriametrics/#cluster-resizing-and-scalability)
- [Capacity planning](https://docs.victoriametrics.com/cluster-victoriametrics/#capacity-planning)
- [Resource usage limits](https://docs.victoriametrics.com/cluster-victoriametrics/#resource-usage-limits)
