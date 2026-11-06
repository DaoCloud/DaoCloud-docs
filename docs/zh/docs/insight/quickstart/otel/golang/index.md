---
hide:
  - toc
---

# Go 应用可观测接入

使用 OpenTelemetry（OTel）SDK 为 Go 应用接入可观测能力，支持链路采集、自定义指标暴露以及日志与链路的关联查询。

## 接入指南

<div class="grid cards" markdown>

- :material-application-brackets-outline:{ .lg .middle } __使用 OTel SDK 增强 Go 应用__

    ---

    通过 OTel SDK 为 Go 应用接入链路与指标采集。

    [:arrow_forward: 查看详情](golang.md)

- :material-gauge:{ .lg .middle } __为应用程序暴露指标__

    ---

    使用 OTel SDK 的 Metrics API 暴露自定义指标。

    [:arrow_forward: 查看详情](meter.md)

- :material-text-search:{ .lg .middle } __将 TraceId 和 SpanId 写入日志__

    ---

    在应用日志中注入链路上下文，便于日志与链路的关联查询。

    [:arrow_forward: 查看详情](traceid_logs.md)

</div>

[下载中心](https://docs.daocloud.io/download/){ .md-button .md-button--primary }
[了解 Token 工厂效能平台](https://docs.daocloud.io/tf/){ .md-button .md-button--primary }
[了解 d.run AI 操作系统](https://docs.daocloud.io/drun/){ .md-button .md-button--primary }
