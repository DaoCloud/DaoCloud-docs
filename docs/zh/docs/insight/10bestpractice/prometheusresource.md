# Prometheus 资源规划

Prometheus 的运行在实际使用过程中由于集群容器数量和开启 Istio 等影响条件下，会导致 Prometheus 的CPU、内存等资源使用量超出设定的资源。

为了保证不同规模集群下 Prometheus 的正常运行，需要根据实际集群规模对 Prometheus 进行资源调整。


## 参考资源规划

在未开启网格情况下，测试情况统计出系统 job 指标量与 pod 的关系为：**series 数量 = 800*pod 数量**

在开启服务网格时，开启功能后 pod 产生的 istio 相关指标数量级为：**series 数量 = 768*pod 数量**

以下表格为未开启&开启服务网格时根据集群规模提供的资源规划。

| 集群规模(Pod数) |     | 指标量(未开启服务网格) | CPU(core)                | 内存(GB)                   |     | 指标量(已开启服务网格) | CPU(core)               | 内存(GB)                      |
| --------------- | --- | ---------------------- | ------------------------ | -------------------------- | --- | ---------------------- | ----------------------- | ----------------------------- |
| 100             |     | 8w                     | request: 0.5<br>limit：1 | request：2GB<br>limit：4GB |     | 15w                    | request: 1<br>limit：2  | request：3GB<br>limit：6GB    |
| 200             |     | 16w                    | request：1<br>limit：1.5 |request：3GB<br>limit：6GB|     | 31w                    | request：2<br>limit：3  | request：5GB<br>limit：10GB   |
| 300             |     | 24w                    | request：1<br>limit：2|request：3GB<br>limit：6GB |     | 46w                    | request：2<br>limit：4  | request：6GB<br>limit：12GB   |
| 400             |     | 32w                    | request：1<br>limit：2|request：4GB<br>limit：8GB|     | 62w                    | request：2<br>limit：4  | request：8GB<br>limit：16GB   |
| 500             |     | 40w                    | request：1.5<br>limit：3|request：5GB<br>limit：10GB |     | 78w                    | request：3<br>limit：6  | request：10GB<br>limit：20GB  |
| 800             |     | 64w                    | request：2<br>limit：4 | request：8GB<br>limit：16GB|     | 125w                   | request：4<br>limit：8  | request：15GB<br>limit：30GB  |
| 1000            |     | 80w                    |request：2.5<br>limit：5|request：9GB<br>limit：18GB|     | 156w                   | request：5<br>limit：10 | request：18GB<br>limit：36GB  |
| 2000            |     | 160w                   |request：3.5<br>limit：7|request：20GB<br>limit：40GB |     | 312w                   | request：7<br>limit：14 | request：40GB<br>limit：80GB  |
| 3000            |     | 240w                   | request：4<br>limit：8 | request：33GB<br>limit：66GB |     | 468w                   | request：8<br>limit：16 | request：65GB<br>limit：130GB |


!!! Note

    1. 表格中 pod 数指集群中基本稳定运行的 pod 数量，如出现大量的 pod 重启，则会在短时间内造成指标量的陡增，此时资源需要进行相应上调；
    2. prometheus 内存中默认保存两小时数据，且集群中开启了 [remote write 功能](https://prometheus.io/docs/practices/remote_write/#memory-usage) 时，会占用一定内存，资源超配比建议配置为2；
    3. 表格中数据为推荐值，适用于通用情况。如环境有精确的资源要求，建议在集群运行一段时间后，查看对应 prometheus 的资源占用量进行精确配置。