---
hide:
  - toc
---

# 最佳实践

Insight 底层采用标准 OTel 技术以及标准 OTLP 协议，可以兼容任意符合 OTLP 协议的观测数据。本页汇总可观测模块的最佳实践，涵盖观测技术集成、数据存储与性能优化、排障指南三个方向。

## 观测技术集成

<div class="grid cards" markdown>

- :material-exchange:{ .lg .middle } __OTel 零代码接收 SkyWalking 链路数据__

    ---

    SkyWalking Agent 链路数据无缝接入。

    [:arrow_forward: 查看详情](sw-to-otel.md)

- :material-gate:{ .lg .middle } __接入 Nginx Ingress 的链路追踪__

    ---

    让网关流量具备全链路观测能力。

    [:arrow_forward: 查看详情](ingress-otel.md)

- :material-water:{ .lg .middle } __集成 DeepFlow__

    ---

    借助 eBPF 技术补齐应用零侵扰观测。

    [:arrow_forward: 查看详情](integration_deepflow.md)

</div>

## 数据存储与性能

<div class="grid cards" markdown>

- :material-chart-box-outline:{ .lg .middle } __Insight Grafana 持久化到数据库__

    ---

    自定义仪表盘的持久化方案。

    [:arrow_forward: 查看详情](grafana-use-db.md)

- :simple-apachekafka:{ .lg .middle } __Kafka 与 Elasticsearch 流式架构应对超大规模日志__

    ---

    大规模日志部署架构调整。

    [:arrow_forward: 查看详情](insight-kafka.md)

- :material-gauge:{ .lg .middle } __VictoriaMetrics 资源规划__

    ---

    VM 存储组件的容量与资源配置。

    [:arrow_forward: 查看详情](vm-resource-plan.md)

- :material-filter-variant:{ .lg .middle } __链路数据采样介绍与配置__

    ---

    尾部采样策略，兼顾成本与排障价值。

    [:arrow_forward: 查看详情](tail-based-sampling.md)

</div>

## 排障指南

<div class="grid cards" markdown>

- :material-bug-outline:{ .lg .middle } __日志采集排障指南__

    ---

    日志采集异常时的排查思路与步骤。

    [:arrow_forward: 查看详情](debug-log.md)

- :material-radar:{ .lg .middle } __链路采集排障指南__

    ---

    链路数据缺失或异常时的排查方法。

    [:arrow_forward: 查看详情](debug-trace.md)

- :material-target:{ .lg .middle } __使用 Insight 定位应用异常__

    ---

    结合指标、日志与链路快速定位应用异常。

    [:arrow_forward: 查看详情](find_root_cause.md)

</div>

[下载中心](https://docs.daocloud.io/download/){ .md-button .md-button--primary }
[了解 Token 工厂效能平台](https://docs.daocloud.io/tf/){ .md-button .md-button--primary }
[了解 d.run AI 操作系统](https://docs.daocloud.io/drun/){ .md-button .md-button--primary }
