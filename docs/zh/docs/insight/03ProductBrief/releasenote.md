# 最新动态

本文介绍了可观测性 Insight 的最新动态，欢迎使用。

## v0.11.0

### 缺陷修复

- 修复部分日志路径下无内容的问题；
- 删除错误的告警规则：KubeletPodStartUpLatencyHigh

## v0.11.0

### 功能

- 增加链路排障和对组件 `Jaeger` 监控的仪表盘；
- 告警列表、消息模版列表支持排序；
- 过滤掉未安装 `insight-agent` 的集群；
- 链路查询时默认按 span 开始时间排序。

### 缺陷修复

- 修复无数据的 `仪表盘` ，包含：opentelemetry 相关的仪表盘。

### 其他

- 将 ` victoria-metrics-k8s-stack` helm chart 升级至 v0.12.6；
- 将 ` opentelemetry-collector` helm chart 从 v0.23.0 升级至 v0.37.2；
- 将 `jaeger` helm chart 从 v0.57.0 升级至 v0.62.1；
- 将 `fluentbit ` helm chart 从 v0.20.9 升级至 v1.9.9；
- 将 `kubernetes-event-exporter` helm chart 从 v1.4.21 升级至 v2.0.0。