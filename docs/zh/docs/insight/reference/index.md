---
hide:
  - toc
---

# 可观测参考

本页汇总可观测模块 (Insight) 的参考文档，涵盖告警通知、数据采集、查询语法与安全集成等内容。

## 告警与通知

<div class="grid cards" markdown>

- :material-bell-outline:{ .lg .middle } __告警通知流程说明__

    ---

    告警从触发到送达的完整链路。

    [:arrow_forward: 查看详情](alertnotification.md)

- :material-email-edit-outline:{ .lg .middle } __通知模板使用说明__

    ---

    自定义邮件、企业微信、钉钉等消息模板。

    [:arrow_forward: 查看详情](notify-helper.md)

- :material-send-outline:{ .lg .middle } __Alertmanager 逐条发送告警通知__

    ---

    告警消息逐条推送配置。

    [:arrow_forward: 查看详情](send-alert-notifications-individually.md)

</div>

## 链路与日志采集

<div class="grid cards" markdown>

- :material-server-network:{ .lg .middle } __创建 Remote Sampling Server__

    ---

    链路数据远程采样服务部署。

    [:arrow_forward: 查看详情](remote-sampling.md)

- :material-chart-areaspline:{ .lg .middle } __开启链路指标告警与自定义链路告警规则__

    ---

    基于 Span 指标配置告警。

    [:arrow_forward: 查看详情](span-metrics-alert.md)

- :material-package-variant:{ .lg .middle } __通过 Sidecar 采集容器日志__

    ---

    无共享存储卷容器的日志采集方案。

    [:arrow_forward: 查看详情](tailing-sidecar.md)

</div>

## 查询语法与指标

<div class="grid cards" markdown>

- :material-text-search:{ .lg .middle } __Lucene 语法使用方法__

    ---

    日志高级查询语法说明。

    [:arrow_forward: 查看详情](lucene.md)

- :material-numeric:{ .lg .middle } __Insight 参考指标说明__

    ---

    平台内置指标的含义与用法。

    [:arrow_forward: 查看详情](used-metric-in-insight.md)

</div>

## 安全与集成

<div class="grid cards" markdown>

- :material-lock-outline:{ .lg .middle } __Insight 和 insight-agent 安全连接到 Kafka__

    ---

    采集数据接入 Kafka 的认证配置。

    [:arrow_forward: 查看详情](security-connect-kafka.md)

</div>

[下载中心](https://docs.daocloud.io/download/){ .md-button .md-button--primary }
[了解 Token 工厂效能平台](https://docs.daocloud.io/tf/){ .md-button .md-button--primary }
[了解 d.run AI 操作系统](https://docs.daocloud.io/drun/){ .md-button .md-button--primary }
