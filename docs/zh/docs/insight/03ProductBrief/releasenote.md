# Insight Release Notes

本页列出 Insight 可观测性的 Release Notes，便于您了解各版本的演进路径和特性变化。

## v0.12.0

发布日期：2022.11.28

### 优化
- **新增** insight-agent Helm 模版安装时支持表单化
- **优化** PromQL 查询支持原始的指标
- **优化** 拓扑图的样式
- **升级** 内置 MySQL 镜像版本，从 v5.7.34 升级到 v8.0.29.
- **升级** Fluentbit ARM架构的 helm Chart 版本从
- **升级** kube-prometheus-stack 的 helm Chart 版本从 v39.6.0 升级至 v41.9.1
- **更新** 使用的 Bitnami 的镜像，包含：grafana-operator, grafana, kubernetes-event-exporter
- **更新** prometheus 相关的的 API 代理地址，将 /prometheus 修改为 /apis/insight.io/prometheus

### 缺陷修复

- **修复** 服务列表缓存逻辑
- **修复** 内置规则不生效的问题
- **修复** 请求延时单位问题
- **修复** Insight 内部链路的问题
- **禁用** vm-stack 中的 PSP 资源
- **修复** victoriaMetrics operator 在 Kubernetes 1.25 中不可用的问题。
- **修复** 前端镜像的浏览器兼容性问题 

## v0.11

发布日期：2022-11-21

### 优化

- **增加** 链路排障和对组件 `Jaeger` 监控的仪表盘
- **优化** 告警列表、消息模板列表支持排序
- **优化** 过滤掉未安装 `insight-agent` 的集群
- **优化** 链路查询时默认按 span 开始时间排序

### 缺陷修复

- 修复无数据的 `仪表盘`，包含 OpenTelemetry 相关的仪表盘
- 修复部分日志路径下无内容的问题
- 删除错误的告警规则：KubeletPodStartUpLatencyHigh

### 其他

- `victoria-metrics-k8s-stack` helm chart 升级至 v0.12.6
- `opentelemetry-collector` helm chart 从 v0.23.0 升级至 v0.37.2
- `jaeger` helm chart 从 v0.57.0 升级至 v0.62.1
- `fluentbit` helm chart 从 v0.20.9 升级至 v1.9.9
- `kubernetes-event-exporter` helm chart 从 v1.4.21 升级至 v2.0.0

## v0.10

发布日期：2022-10-20

### 功能特性

- 支持与 OTel 服务名称关联的容器管理 Service 名称，以辨别是否启用了服务链路
- Support kpanda service name associated with the otel service name, identify whether the service tracing enabled.
- 在全局 OTel 一栏更新了默认的跟踪样本策略
- Update default tracing sample policies in global otel col.
- 将相扑（适用于审计日志）exporter port 8080 更改为 80
- Change sumologic (work for audit log) exporter port 8080 to 80.
- 使用 go-migrate 管理数据库迁移版本
- Use go-migrate to manage db migration version.
- 修复图形 API 中多集群和多命名空间过滤器不正常的问题
- Fix multi cluster and multi namespaces filter not work well in graph API.
- 支持构建 ARM 镜像
- Support build arm image.

### 安装

- Fluentbit 支持 Dockder 和 containerd 日志的解析器
- Fluentbit support parser both docker and containerd log.
- 修复 var/log/ UTC 问题
- Fix var/log/ UTC issue.
- Fluentbit 支持 elasticsearch 输出跳过 TLS 验证
- Fluentbit support elasticsearch output skip verify TLS.
- K8s 审计日志过滤器支持从 Helm 值获取规则
- kube audit log filter support getting rule from helm values.
- 修复 centos7/ubuntu20 主机日志时间的解析问题
- Fix parse centos7/ubuntu20 host log time.
- 提升 OTel Operator 版本，移除 Operator 中随自签名证书一起部署的 cert-manager 依赖项
- Bump up otel operator version, remove cert-manager dependencies in operator deploy within self-signed cert.
- 设计了 jaeger collector 指标
- Scrape jaeger collector metrics.
- 提升 tailing-sidecar 版本
- Bump up tailing-sidecar version.
- Jaeger 支持 elasticsearch 输出跳过 TLS 验证
- Jaeger support elasticsearch output skip verify TLS.
- 在 A 模式中禁用 jaeger 组件
- Disable jaeger components in Mode A.

### 其他

- 新增 OTel collector grafana 仪表盘
- Add otel collector grafana dashboard.
- 新增 Insight 概览中文页面
- Add Insight Overview Chinese version.

## v0.9

发布日期：2022-9-25

### 功能特性

- Support kpanda service name associated with the otel service name, identify whether the service tracing enabled.
- Update default tracing sample policies in global otel col.
- Change sumologic(work for audit log) exporter port 8080 to 80.
- Use go-migrate to manage db migration version.
- Fix multi cluster and multi namespaces filter not work well in graph API.
- Support build arm image.

### 安装

- Fluentbit support parser both docker and containerd log.
- Fix /var/log/ UTC issue.
- Fluentbit support elasticsearch output skip verfify TLS.
- kube audit log filter support getting rule from helm values.
- Fix parse centos7/ubuntu20 host log time.
- Bump up otel operator version, remove cert-manager dependencies in operator deploy within self-signed cert.
- Scrape jaeger collector metrics.
- Bump up tailing-sidecar version.
- Jaeger support elasticsearch output skip verfify TLS.
- Disable jaeger components in Mode A.

### 其他

- Add otel collector grafana dashboard.
- Add Insight Overview Chinese version.

## v0.8

发布日期：2022-8-21

### 功能特性

- Migrate graph server into insight server.
- Add cluster_name param to graph query request.
- Add userinfo api.
- Add GetREDMetrics API in GraphQueryService.
- Add GetHelmInstallConfig api to get global cluster service addresses for agent to use.
- Complete auth module.
- Add init cmd/initcontainer for elasticsearch alias and ilm policy

### 架构调整

- Bump up otel operator in agent chart.
- Add kibana as builtin tools.
- Reduce traces/logs chart's default values.
- Add Helm values parameters documentation.
- Polished Helm parameters.

### 安装

- Add audit log enable/disable feature.
- Move Fluentbit config to a ConfigMap.

## v0.7

发布日期：2022-7-20

### 破坏变更

- Modify QueryOperations and GetServiceApdex's API definition in Tracing service.
- Remove resolve alert api.
- fix NFD master crash when CRDs missed.

### 功能特性

- Remove jaeger relate code in span-metric.
- Add index policy for skoala gateway logs.
- Add lua filter for Ghippo audit logs.
- Add global config api.
- Disable cache in vmselect component.
- Dock with ghippo roles.
- Expose metric `insight_cluster_info` in server.
- Add log.SearchLog API for SKoala, accept ES query DSL and return raw ES response.
- Bump up OTelcol helm chart version to 0.21.1 and update otelcol architecture.
- support mspider tracing.
- Bump up OTelcol helm chart version to 0.23.0.
- Add default tracing sample policies in global otel col.

### 架构调整

- Use GrafanaOperator Stack to replace original Grafana Stack.
- Replace insight-overview dashboard.
- Add GrafanaDashboard, GrafanaDatasource CRDs.

## v0.6

发布日期：2022-6-23

### 破坏变更

- Modify insight deployment and service name to insight-server.
- Modify trace relate metric query API response type.
- Using the unified paging mechanism

### 功能特性

- Add graph api through prometheus metrics of mesh layer.
- Add service graph api through prometheus metrics of general layer.
- Modify proto param, follow google style doc[https://developers.google.com/protocol-buffers/docs/style].
- Modify list api pagination and add sort.
- Add GProductVersion cr.
- Add insight metric config api.
- Manager insight license resource cr.
- Add traces api through access jaeger grpc endpoint with otlp/v2 protocol.
- Add service-detail api to get all metrics and scalars for a given service name.
- Add operation-detail api to get all metrics and scalars group by operation for a given service name.
- Add traces api through access jaeger grpc endpoint with jaeger v1 protocol.
- Add span metric protobuf style check

### 架构调整

- Add node-feature-discovery subchart for License module.
- Add opentelemetry-collector subcharts to insight chart.
- Delete audit log OUTPUT config in fluent-bit.
- Add groupbytrace processor to generate trace/span number metrics.
- Add built-in Elasticsearch chart and enabled by default.

### 安装

- Upgrade victoria-metrics-k8s-stack chart version from 0.6.5 to 0.9.3.
- Add servicemonitor for components in victoria-metrics-k8s-stack.
- Modify insight components resource.

## v0.5

发布日期：2022-5-18

### 功能特性

- 添加通知模板 API
- 完成规则和告警 API
- 添加服务 API
- 为 vmrules 实现增删改查
- 移除了 get 查询日志 API
- 支持用 fluentbit 收集 kube 审计日志
- 提供 Service Graph 的功能相关 API
- 增强 span_metric API：latencies, calls, errors 三个 API 支持实例维度的查询
- 增强 span_metric API：查询 Latency(with GroupByOperation) 能够返回 P99 P95 P90
- 增强 span_metric API：latencies, calls, errors 三个 API 支持 extension_filters 维度的查询
- 为查询延迟、调用和错误添加了聚合式 API
- 添加了 apdex API
- 重命名 span_metric API URL

### 安装

- 添加了内置 mysql
- 将 GO 版本升级到 1.17
- 将 insight 服务器服务端口从 8000 更改为 80
- 将 insight 服务器/指标端口从 2022 更改为 81

### 文档

- 新增文档站术语表
- 新增文档站基本概念任务和实例、数据模型、查询语言等 4 个页面
- 新增用户指南 - 场景监控、数据查询、告警中心等文档
- 文档站新增：[产品优势](../03ProductBrief/benefits.md)、[指标查询](../06UserGuide/04dataquery/metricquery.md)、[链路查询](../06UserGuide/04dataquery/tracequery.md)、仪表盘、[概述](../06UserGuide/overview.md)

## v0.4

发布日期：2022-4-22

### 功能特性

- 增加告警通知模块主要 API
- 升级并适配 kpanda 0.4.x API
- 为系统日志增加日志所属文件路径信息
- 增加查询单条日志上下文 API
- 增加查询 Kubernetes Event API
- 增强 Insight 自身可观测性能力, 提供自身的指标接口和查询链路信息
- 通过反向代理 Jaeger Query 的 API 供前端使用
- 增加 Query Tracing Operations 相关 API
- 增加 Span Metric 相关 API

### 测试

- 增加 E2E 用例覆盖率徽章
- 补充告警通知相关的测试用例文档
- 增加日志相关接口的 E2E 测试

### 文档

- 添加整体双语文档站结构及主要内容
- 增加文档所需插件, 优化渲染
- 完成 ROADMAP 内容
- 将文档 ROADMAP 内容合并如总 ROADMAP 文件
- 更新文档结构

## v0.3

发布日期：2022-3-18

### 功能特性

- gRPC 和 http 使用相同的端口
- 将 api 路径从 /api/insight/ 修改为 /api/insight.io/
- 从 kpanda 添加群集资源 api 代理
- ginkgo 从 1.x 升级到 2.x
- 整理 /api 下的 proto 文件
- 在 insight.proto 中拆分 insight 服务
- 将 kpanda api 更新为 0.3.41
- 完成群集/命名空间列表和群集摘要
- 添加批量查询即时和范围度量 api
- 添加节点和所有工作负载 api
- 添加 Otel tracing 以跟踪 insight
- 支持使用 extraLabels 进行度量查询
- 添加度量文档。
- 在 monitor 中实现基本场景案例

### Helm Charts

- 添加 Jaeger helm chart
- 添加 OpenTelemetry collector helm chart
- 添加 tailing-sidecar-operator 作为日志收集的配件/解决方案/插件
- 在 fluentbit 中添加/变量/日志/消息收集
- 将 kube exporter 添加到 collecot kube 群集事件日志
