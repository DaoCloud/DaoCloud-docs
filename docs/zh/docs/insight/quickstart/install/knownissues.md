# 已知问题

本页列出一些 Insight Agent 安装和卸载有关的问题及其解决办法。

## v0.23.0

### Insight Agent

#### Insight Agent 卸载失败

当你运行以下命令卸载 Insight Agent 时。

```sh
helm uninstall insight-agent -n insight-system
```

`otel-oprator` 所使用的 `tls secret` 未被卸载掉。

`otel-operator` 定义的“重复利用 tls secret”的逻辑中，会去判断 `otel-oprator` 的 `MutationConfiguration`
是否存在并重复利用 MutationConfiguration 中绑定的 CA cert。但是由于 `helm uninstall` 已卸载 `MutationConfiguration`，导致出现空值。

综上请手动删除对应的 `secret`，以下两种方式任选一种即可：

- **通过命令行删除**：登录目标集群的控制台，执行以下命令：

    ```sh
    kubectl -n insight-system delete secret insight-agent-opentelemetry-operator-controller-manager-service-cert
    ```

- **通过 UI 删除**：登录 DCE 5.0 容器管理，选择目标集群，从左侧导航进入`密钥`，输入
   `insight-agent-opentelemetry-operator-controller-manager-service-cert`，选择`删除`。

## v0.22.0

### Insight Agent

#### 升级 Insight Agent 时更新日志收集端，未生效

更新 insight-agent 日志配置从 elasticsearch 改为 kafka 或者从 kafka 改为 elasticsearch，实际上都未生效，还是使用更新前配置。

**解决方案** ：

手动重启集群中的 fluentbit。

## v0.21.0

### Insight Agent

#### PodMonitor 采集多份 JVM 指标数据

1. 这个版本的 **PodMonitor/insight-kubernetes-pod** 存在缺陷：会错误地创建 Job 去采集标记了
   `insight.opentelemetry.io/metric-scrape=true` 的 Pod 的所有 container；而实际上只需采集
   `insight.opentelemetry.io/metric-port` 所对应 container 的端口。

2. 因为 PodMonitor 声明之后，**PromethuesOperator** 会预设置一些服务发现配置。
   再考虑到 CRD 的兼容性的问题。因此，放弃通过 PodMonitor 来配置通过 **annotation** 创建采集任务的机制。

3. 通过 Prometheus 自带的 additional scrape config 机制，将服务发现规则配置在 secret 中，在引入 Prometheus 里。

综上：

1. 删除这个 **PodMonitor** 的当前 **insight-kubernetes-pod**
2. 使用新的规则

新的规则里通过 **action: keepequal** 来比较 **source_labels** 和 **target_label** 的一致性，
来判断是否要给某个 container 的 port 创建采集任务。需要注意，这个是 Prometheus 2.41.0（2022-12-20）和更高版本才具备的功能。

```diff
+    - source_labels: [__meta_kubernetes_pod_annotation_insight_opentelemetry_io_metric_port]
+      separator: ;
+      target_label: __meta_kubernetes_pod_container_port_number
+      action: keepequal
```
