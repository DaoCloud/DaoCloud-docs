# 部署容量规划

默认情况下，可观测性模块为了避免消耗过多资源，已经设置了资源上线（resource limit），可观测系统需要处理大量的数据，如果容量规划不合理，可能会导致系统负载过高，影响稳定性和可靠性。

## 观测组件的资源规划

可观测性模块包含  Insight 和 Insight Agent。其中，Insight 主要负责观测数据的存储，分析与展示。而 Insight Agent 包含了数据采集、数据处理、数据上传等功能。

### 存储组件的容量规划

Insight 的存储组件主要包括 ElasticSearch 和 VictoriaMetrics. 其中，ElasticSearch 主要负责存储和查询日志与链路数据，VictoriaMetrics 主要负责存储和查询指标数据。

* **VictoriaMetircs**:  其磁盘用量与存储的指标有关，根据 [vmstorage 的磁盘规划](./vms-res-plan.md) 预估容量后 [调整 vmstorage 磁盘](./modify-vms-disk.md)。

### 采集器的资源规划

Insight Agent 的采集器中包含 Proemtheus，虽然 Prometheus 本身是一个独立的组件，但是在 Insight Agent 中，Prometheus 会被用于采集数据，因此需要对 Prometheus 的资源进行规划。

* **Prometheus**：其资源用量与采集的指标量有关，可以参考 [Prometheus 资源规划](./prometheus-res.md) 进行调整。
