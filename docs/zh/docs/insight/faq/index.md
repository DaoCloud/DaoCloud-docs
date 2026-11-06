---
hide:
  - toc
---

# 可观测常见问题

汇总可观测模块 (Insight) 使用中的常见问题与排障指南。安装前建议先阅读[部署容量规划](../quickstart/res-plan/index.md)与 [insight-agent 安装](../quickstart/install/install-agent.md)。

## 告警相关

<div class="grid cards" markdown>

- :material-bell-ring-outline:{ .lg .middle } __Prometheus 集群标签配置__

    ---

    告警信息中集群 ID 与名称的转换。

    [:arrow_forward: 查看详情](alertinfo-trans-clusterid-to-name.md)

- :material-bell-plus-outline:{ .lg .middle } __Insight 告警通知开启 v1alpha2__

    ---

    告警通知 API 版本升级说明。

    [:arrow_forward: 查看详情](alertnotify-enable-v2api.md)

</div>

## 日志相关

<div class="grid cards" markdown>

- :material-database-outline:{ .lg .middle } __ElasticSearch 数据塞满如何操作__

    ---

    ES 存储写满后的处理步骤。

    [:arrow_forward: 查看详情](expand-once-es-full.md)

- :material-filter-outline:{ .lg .middle } __容器日志黑名单__

    ---

    排除不需要采集的容器日志。

    [:arrow_forward: 查看详情](ignore-pod-log-collect.md)

- :material-tune-vertical:{ .lg .middle } __Logstash 参数优化__

    ---

    大规模日志场景下的 Logstash 调优。

    [:arrow_forward: 查看详情](logstash-optimize.md)

- :simple-apachekafka:{ .lg .middle } __Fluent Bit 按 Namespace 路由至不同 Topic__

    ---

    日志按命名空间分流到 Kafka。

    [:arrow_forward: 查看详情](fluentbit-dynamic-kafka-topic.md)

- :material-desktop-classic:{ .lg .middle } __NeoKylin Linux V10 启动 Fluent Bit 失败__

    ---

    麒麟操作系统上的兼容性问题。

    [:arrow_forward: 查看详情](kylin-fluentbit.md)

</div>

## 链路相关

<div class="grid cards" markdown>

- :material-clock-fast:{ .lg .middle } __链路数据中的时钟偏移__

    ---

    多集群间时钟不同步导致链路数据异常。

    [:arrow_forward: 查看详情](traceclockskew.md)

</div>

## 排障指南

<div class="grid cards" markdown>

- :material-bug-outline:{ .lg .middle } __日志采集排障指南__

    ---

    日志采集异常时的排查思路与步骤。

    [:arrow_forward: 查看详情](../best-practice/debug-log.md)

- :material-radar:{ .lg .middle } __链路采集排障指南__

    ---

    链路数据缺失或异常时的排查方法。

    [:arrow_forward: 查看详情](../best-practice/debug-trace.md)

- :material-target:{ .lg .middle } __使用 Insight 定位异常__

    ---

    结合指标、日志与链路快速定位应用异常。

    [:arrow_forward: 查看详情](../best-practice/find_root_cause.md)

</div>

[下载中心](https://docs.daocloud.io/download/){ .md-button .md-button--primary }
[了解 Token 工厂效能平台](https://docs.daocloud.io/tf/){ .md-button .md-button--primary }
[了解 d.run AI 操作系统](https://docs.daocloud.io/drun/){ .md-button .md-button--primary }
