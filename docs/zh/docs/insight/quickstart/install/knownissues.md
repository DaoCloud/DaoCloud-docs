# 已知问题

## v0.21.0

### Insight Agent

#### PodMonitor 采集多份 JVM 指标数据

1. 目前的 __PodMonitor/insight-kubernetes-pod__ 存在缺陷：会错误的创建 Job 去采集标记了
   __insight.opentelemetry.io/metric-scrape=true__ 的 Pod 的所有 container；其实只需要采集
   __insight.opentelemetry.io/metric-port__ 对应的 container 的端口。

2. 因为 PodMonitor 声明之后， __PromethuesOperator__ 会预设置一些服务发现配置。
   再考虑到 CRD 的兼容性的问题。因此，放弃通过 PodMonitor 来配置通过 __annotation__ 创建采集任务的机制。

3. 通过 Prometheus 自带的 additional scrape config 机制，将服务发现规则配置在 secrets 中，在引入 Prometheus 里。

综上：

1. 删除这个 __PodMonitor__ 的当前 __insight-kubernetes-pod__ 
2. 使用新的规则

新的规则里通过 __action: keepequal__ 来比较 __source_labels__ 和 __target_label__ 的一致性，
来判断是否要给某个 container 的 port 创建采集任务。需要注意，这个是 Prometheus 2.41.0（2022-12-20）和更高版本才具备的功能。

```diff
+    - source_labels: [__meta_kubernetes_pod_annotation_insight_opentelemetry_io_metric_port]
+      separator: ;
+      target_label: __meta_kubernetes_pod_container_port_number
+      action: keepequal
```
