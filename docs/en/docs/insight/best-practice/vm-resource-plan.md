# VictoriaMetrics 资源规划

`VictoriaMetrics` 相关组件在 `Prometheus RemoteWrite` 实际使用过程中，会受到集群容器数量以及指标量的影响，而导致 `vminsert` 和 `vmstorage` 的 CPU、内存 等资源使用量超出设定的资源。为了保证不同规模集群下 `VictoriaMetrics` 组件的正常运行，需要根据集群的实际规模对 `VictoriaMetrics` 进行资源调整。

## 测试结果

经过对 `Prometheus RemoteWrite` 到 `VictoriaMetrics` 的指标持续观测，我们发现 `VictoriaMetrics` 相关组件资源大部分情况和 `ingestion rate`（指标摄取率）呈正相关，而指标摄取率和 Pod 数量同样呈正相关。

- **Ingestion_rate**：sum(rate(vm_rows_inserted_total{job="vminsert-insight-victoria-metrics-k8s-stack"}[1m]))
- **Pod 数量**：sum(kube_pod_info)

其中，以上的 **ingestion_rate** 显示每秒有多少数据点插入到 `vminsert` 中，即此指标不考虑由于复制而导致的数据增加。如果想知道包括复制因子在内的指标摄取率，可以使用查询 sum(rate(vm_vminsert_metrics_read_total{job="vmstorage-insight-victoria-metrics-k8s-stack"}[1m]))，该查询显示 `vmstorage` 从 `vminsert` 读取了多少个数据点。

通过对多集群长时间的测试，两个指标摄取率差别不大。因此，该文的指标摄取率主要以每秒插入到 vminsert 的数据点为准。

## 计算方法

### 资源使用

| **组件**        | **资源**     | **计算公式**                                 | **备注**                                    |
|---------------|------------|------------------------------------------|-------------------------------------------|
| **vminsert**  | CPU        | ( ingestion_rate / 100k + 0.07 ) * 2     |                                           |
|           | 接收带宽 (KB/s) | 60 * ingestion_rate / 1k + 120           |                                           |
|           | 传输带宽 (KB/s) | 20 * ingestion_rate / 1k + 40            | 大约是接收带宽的 1/3                               |
| **vmstorage** | CPU        | ( 2 * ingestion_rate / 100k - 0.02 ) * 2 |                                           |
|           | 内存 (MB)     | 100 * ingestion_rate / 1k * 2            |                                           |
|           | 接收带宽 (KB/s) | 30 * ingestion_rate / 1k                 |                                           |

**参数说明：**

1. CPU 计算公式： * 2 是为了预留 50% 的空闲 CPU，以降低在工作负载高峰期间出现性能瓶颈的风险。
2. 内存计算公式：* 2 是为了预留 50% 的空闲内存，以减少在工作负载激增时因 OOM（内存溢出）导致崩溃的可能性。

### 集群规模

按照现存环境，集群规模和指标摄取率关系大概如下：**ingestion_rate = Pod 数量 * 1000 /  120 

## 参考资源规划

以下为 Prometheus RemoteWrite 场景下，不同规模集群中 VictoriaMetrics 组件大概所需资源：

| **集群规模（Pod 数量）** | **ingestion_rate** | **vminsert CPU(core)** | **vminsert 内存** | **vminsert 接收带宽** | **vminsert 传输带宽** | **vmstorage CPU(core)** | **vmstorage 内存** | **vmstorage 接收带宽** |
|-----------------|--------------------|------------------------|-----------------|------------------|------------------|-------------------------|------------------|-------------------|
| 100             | 8k                 | 0.3                    | 160 MB          | 600 KB/s         | 200 KB/s         | 0.28                    | 1.6 GB           | 240 KB/s          |
| 200             | 17k                | 0.48                   | 340 MB          | 1.1 MB/s         | 380 KB/s         | 0.64                    | 3.3 GB           | 510 KB/s          |
| 300             | 25k                | 0.64                   | 500 MB          | 1.6 MB/s         | 540 KB/s         | 0.96                    | 4.9 GB           | 750 KB/s          |
| 400             | 34k                | 0.84                   | 500 MB          | 2.1 MB/s         | 720 KB/s         | 1.32                    | 6.7 GB           | 1020 KB/s         |
| 500             | 42k                | 0.98                   | 500 MB          | 2.6 MB/s         | 880 KB/s         | 1.64                    | 8.2 GB           | 1.3 MB/s          |
| 800             | 67k                | 1.48                   | 500 MB          | 4.1 MB/s         | 1.4 MB/s         | 2.64                    | 13.1 GB          | 2 MB/s            |
| 1000            | 84k                | 1.82                   | 500 MB          | 5.1 MB/s         | 1.7 MB/s         | 3.32                    | 16.4 GB          | 2.5 MB/s          |
| 2000            | 167k               | 3.48                   | 500 MB          | 10 MB/s          | 3.3 MB/s         | 6.64                    | 32.6 GB          | 4.9 MB/s          |

**说明：**

1. 表格中的 Pod 数量 指已正常安装 insight-agent 的集群中基本稳定运行的 Pod 数量，如出现大量的 Pod 重启，则会造成短时间内指标量的陡增，此时资源需要进行相应上调。
2. 表格中数据为对应规模下组件可正常运行的资源使用值。如环境有精确的资源要求，建议在已有业务类型的集群运行一段时间后，查看对应 VictoriaMetrics 的资源占用量再进行精确配置。
3. 在 Prometheus RemoteWrite 过程中，主要是 vminsert 和 vmselect 参与工作。暂无 vmselect 的资源规划，需要根据 读取量 进行评估。

## 组件资源扩展建议

1. 扩展 `vminsert` 的副本数可以提升数据摄取能力，因为摄取的数据可以在更多的 `vminsert` 节点之间进行拆分。

2. 扩展 `vmstorage` 副本数或者增加 CPU 和内存都能提升可处理的活跃时间序列数量。相比之下，更推荐扩展副本数，这样可以在高流失率（churn rate）情况下提高时间序列的查询性能，并增强集群的稳定性。
  
3. 增加 `vmselect` 的 CPU 和内存可以提升复杂查询的性能，尤其是处理大量时间序列和原始样本时。扩展 `vmselect` 的副本数可以提高查询的并发处理能力，因为传入的请求可以在更多的 vmselect 节点之间分配，从而提升查询的最大速度。

4. 正常安装模式下 `VictoriaMetrics` 使用官方默认配置。指标 `vm_concurrent_insert_capacity` 默认为指标 `vm_available_cpu_coresvm_available_cpu_cores{job="vminsert-insight-victoria-metrics-k8s-stack"}` 的 2 倍；`vm_concurrent_select_capacity` 默认为 `vm_available_cpu_cores{job="vmselect-insight-victoria-metrics-k8s-stack"}`的 2 倍。当给定组件的 CPU 不足时，可能出现 `vm_concurrent_insert_current 或vm_concurrent_select_current` 达到上限，这种情况下需根据实际情况在 CR 中增加以下配置：

```shell
# vmcluster的cr中，在spec.vminsert.extraArgs下增加如下，则可以将最大并发提高到32 
maxConcurrentInserts: "32"
  
# vmcluster的cr中，在spec.vmselect.extraArgs下增加如下，则可以将最大并发提高到16 
search.maxConcurrentRequests: "16"
```

## 参考文档

1. https://docs.victoriametrics.com/cluster-victoriametrics/#cluster-resizing-and-scalability
2. https://docs.victoriametrics.com/cluster-victoriametrics/#capacity-planning
3. https://docs.victoriametrics.com/cluster-victoriametrics/#resource-usage-limits
