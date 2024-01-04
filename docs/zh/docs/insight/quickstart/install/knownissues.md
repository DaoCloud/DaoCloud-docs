# 已知问题

## v0.23.0

### Insight Agent

#### Insight Agent 卸载失败

1. `helm uninstall insight agent` 的时候， `otel-oprator` 所使用的 `tls secret` 未被卸载掉。
2. 由于 `otel-operator` 中以下“重复利用 tls secret”的逻辑中，会去判断 `otel-oprator` 的 `MutationConfiguration` 是否存在而重复利用 MutationConfiguration 中绑定的 CA cert。但是由于 `helm uninstall` 已卸载 `MutationConfiguration` ，导致出现空值。

综上请手动写在对应的 `secret`，以下两种方式任选一种即可：

1. 登录目标集群的控制台，执行 `kubectl -n insight-system delete secret insight-agent-opentelemetry-operator-controller-manager-service-cert` 。
2. 登录 DCE5.0 容器管理，选择目标集群，选择左侧导航进入“密钥” ，输入`insight-agent-opentelemetry-operator-controller-manager-service-cert` ，选择删除。

## v0.21.0

### Insight Agent

#### PodMonitor 采集多份 JVM 指标数据

1. 目前的 __PodMonitor/insight-kubernetes-pod__ 存在缺陷：会错误的创建 Job 去采集标记了
   `insight.opentelemetry.io/metric-scrape=true`的 Pod 的所有 container；其实只需要采集
   `insight.opentelemetry.io/metric-port`对应的 container 的端口。

2. 因为 PodMonitor 声明之后，__PromethuesOperator__ 会预设置一些服务发现配置。
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
