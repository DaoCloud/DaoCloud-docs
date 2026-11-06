---
hide:
  - toc
---

# JVM 监控指标暴露

提供多种方式暴露 JVM 监控指标：可以使用 JMX Exporter 或 OpenTelemetry Java Agent 无侵入采集，
也可以将已有 JVM 指标的应用接入可观测平台。

## 接入方式

<div class="grid cards" markdown>

- :material-chart-box-outline:{ .lg .middle } __使用 JMX Exporter 暴露 JVM 指标__

    ---

    以 Java Agent 形式启动，通过 HTTP 端点暴露 JVM 监控指标。

    [:arrow_forward: 查看详情](jmx-exporter.md)

- :material-chart-line:{ .lg .middle } __使用 OTel Java Agent 暴露 JVM 指标__

    ---

    无侵入方式自动采集 JVM 与应用指标。

    [:arrow_forward: 查看详情](otel-java-agent.md)

- :material-database-outline:{ .lg .middle } __已有 JVM 指标的应用对接__

    ---

    将已通过其他方式暴露 JVM 指标的 Java 应用接入可观测平台。

    [:arrow_forward: 查看详情](legacy-jvm.md)

</div>

[下载中心](https://docs.daocloud.io/download/){ .md-button .md-button--primary }
[了解 Token 工厂效能平台](https://docs.daocloud.io/tf/){ .md-button .md-button--primary }
[了解 d.run AI 操作系统](https://docs.daocloud.io/drun/){ .md-button .md-button--primary }
