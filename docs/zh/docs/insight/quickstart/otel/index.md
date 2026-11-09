---
hide:
  - toc
---

# OTel 应用可观测接入

通过 OpenTelemetry（OTel）为应用赋予可观测能力：既可以通过 Operator 注解实现无侵入增强，
也可以使用 OTel SDK 手动埋点，并将链路数据发送至 Insight。

## 核心流程

<div class="grid cards" markdown>

- :material-application-brackets-outline:{ .lg .middle } __通过 Operator 实现无侵入增强__

    ---

    通过注解自动注入探针，无需修改应用代码即可采集链路数据。

    [:arrow_forward: 查看详情](operator.md)

- :material-chart-line:{ .lg .middle } __使用 OTel SDK 手动埋点__

    ---

    通过 OTel SDK 以编码方式定制化暴露指标、日志与链路数据。

    [:arrow_forward: 查看详情](otel.md)

- :material-connection:{ .lg .middle } __向 Insight 发送链路数据__

    ---

    将应用的链路数据上报至 insight-agent 内置的 OTel Collector。

    [:arrow_forward: 查看详情](send_tracing_to_insight.md)

</div>

## 语言与场景指南

<div class="grid cards" markdown>

- :material-cube-outline:{ .lg .middle } __Go 应用可观测接入__

    ---

    使用 OTel SDK 增强 Go 应用、暴露指标并将 TraceId 写入日志。

    [:arrow_forward: 查看详情](golang/)

- :material-chart-box-outline:{ .lg .middle } __Java 应用监控__

    ---

    Java Agent 自动埋点、JMX Exporter 等多种 JVM 监控指标暴露方式。

    [:arrow_forward: 查看详情](java/)

</div>

[下载中心](https://docs.daocloud.io/download/){ .md-button }
[了解 Token 工厂效能平台](https://docs.daocloud.io/tf/){ .md-button }
[了解 d.run AI 操作系统](https://docs.daocloud.io/drun/){ .md-button }
