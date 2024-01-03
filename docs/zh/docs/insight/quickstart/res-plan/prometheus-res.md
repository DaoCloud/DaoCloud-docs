# Prometheus 资源规划

Prometheus 在实际使用过程中，受到集群容器数量以及开启 Istio 的影响，会导致 Prometheus 的 CPU、内存等资源使用量超出设定的资源。

为了保证不同规模集群下 Prometheus 的正常运行，需要根据集群的实际规模对 Prometheus 进行资源调整。

## 参考资源规划

在未开启网格情况下，测试情况统计出系统 Job 指标量与 Pod 的关系为：**Series 数量 = 800\*Pod 数量**

在开启服务网格时，开启功能后 Pod 产生的 Istio 相关指标数量级为：**Series 数量 = 768\*Pod 数量**

### 当未开启服务网格时

以下资源规划为 **未开启服务网格** 场景下，Prometheus 的资源规划推荐：

| 集群规模(Pod 数) | 指标量(未开启服务网格) | CPU(core)                | 内存(GB)                     |
| ---------------- | ---------------------- | ------------------------ | ---------------------------- |
| 100              | 8w                     | Request: 0.5<br>Limit：1 | Request：2GB<br>Limit：4GB   |
| 200              | 16w                    | Request：1<br>Limit：1.5 | Request：3GB<br>Limit：6GB   |
| 300              | 24w                    | Request：1<br>Limit：2   | Request：3GB<br>Limit：6GB   |
| 400              | 32w                    | Request：1<br>Limit：2   | Request：4GB<br>Limit：8GB   |
| 500              | 40w                    | Request：1.5<br>Limit：3 | Request：5GB<br>Limit：10GB  |
| 800              | 64w                    | Request：2<br>Limit：4   | Request：8GB<br>Limit：16GB  |
| 1000             | 80w                    | Request：2.5<br>Limit：5 | Request：9GB<br>Limit：18GB  |
| 2000             | 160w                   | Request：3.5<br>Limit：7 | Request：20GB<br>Limit：40GB |
| 3000             | 240w                   | Request：4<br>Limit：8   | Request：33GB<br>Limit：66GB |

### 当开启服务网格功能时

以下资源规划为 **开启服务网格** 场景下，Prometheus 的资源规划推荐：

| 集群规模(Pod 数) | 指标量(已开启服务网格) | CPU(core)               | 内存(GB)                      |
| ---------------- | ---------------------- | ----------------------- | ----------------------------- |
| 100              | 15w                    | Request: 1<br>Limit：2  | Request：3GB<br>Limit：6GB    |
| 200              | 31w                    | Request：2<br>Limit：3  | Request：5GB<br>Limit：10GB   |
| 300              | 46w                    | Request：2<br>Limit：4  | Request：6GB<br>Limit：12GB   |
| 400              | 62w                    | Request：2<br>Limit：4  | Request：8GB<br>Limit：16GB   |
| 500              | 78w                    | Request：3<br>Limit：6  | Request：10GB<br>Limit：20GB  |
| 800              | 125w                   | Request：4<br>Limit：8  | Request：15GB<br>Limit：30GB  |
| 1000             | 156w                   | Request：5<br>Limit：10 | Request：18GB<br>Limit：36GB  |
| 2000             | 312w                   | Request：7<br>Limit：14 | Request：40GB<br>Limit：80GB  |
| 3000             | 468w                   | Request：8<br>Limit：16 | Request：65GB<br>Limit：130GB |

!!! note

    1. 表格中的 __Pod 数量__ 指集群中基本稳定运行的 Pod 数量，如出现大量的 Pod 重启，则会造成短时间内指标量的陡增，此时资源需要进行相应上调。
    2. Prometheus 内存中默认保存两小时数据，且集群中开启了 [Remote Write 功能](https://prometheus.io/docs/practices/remote_write/#memory-usage)时，会占用一定内存，资源超配比建议配置为 2。
    3. 表格中数据为推荐值，适用于通用情况。如环境有精确的资源要求，建议在集群运行一段时间后，查看对应 Prometheus 的资源占用量进行精确配置。
