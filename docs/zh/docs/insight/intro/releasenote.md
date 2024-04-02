# Insight Release Notes

本页列出 Insight 可观测性的 Release Notes，便于您了解各版本的演进路径和特性变化。

## 2024.03.31

### Insight Server: v0.25.0

#### 优化

- **优化** 链路关联日志支持根据 TraceID 和容器组过滤
- **优化** 支持对通知对象的敏感信息进行加密隐藏
- **优化** 将 `insight-server` 拆分成 `insight-server` 和 `insight-manager` 两个组件
- **优化** `opentelemetry-collector` 组件支持高可用
- **优化** Grafana 和 Jaeger 未登陆不可访问
- **优化** 支持自定义在安装时是否初始化日志索引的能力

#### 修复

- **修复** 修复告警相关的权限问题
- **修复** 概览查询指标无数据的问题
- **修复** YAML 导入告警策略时的校验问题
- **修复**  Grafana 访问速度受限的缺陷

## 2024.01.31

### Insight Server: v0.24.0

#### 新增

- **新增** 支持告警抑制
- **新增** 支持告警模板并从模板创建告警策略

#### 优化

- **优化** Grafana 支持增加 JSON API 类型的数据源
- **优化** Grafana 禁止使用 ECS 键退出全屏模式

#### 修复

- **修复** 创建日志告警预览查询不准确的问题
- **修复** insight-system 部署过程中的监听 IPv6 问题报错
- **修复** Grafana 仪表盘没有通过认证允许查看的问题
- **修复** 强制所有 SMTP 邮件启用 InsecureSkipVerify

### Insight Agent: v0.23.0

#### 优化

- **优化** 升级 OpenTelemetry Collector 相关组件的镜像版本

## 2023.12.31

### Insight Server: v0.23.0

#### 新增

- **新增** 集成网络观测 Deepflow 社区版
- **新增** 告警模板

#### 优化

- **优化** 使用 DSL 作为日志告警的查询语句

#### 修复

- **修复** 拓扑图没有请求延时数据
- **修复** 当集群状态异常时，Insight Agent 状态未更新
- **修复** 拨测的配置文件中缺少 `metadata`
- **修复** 日志告警的预览趋势图查询不准确且告警对象不准确
- **修复** Insight Server Chart 中 `app.kubernetes.io/name` 字段重复出现

### Insight Agent: v0.23.0

#### 优化

- **优化** 链路追踪的探针注入需要自动注入 `k8s_namespce_name`
- **优化** 为每个已部署 Insight Agent 的集群自动生成并配置日志索引

## 2023.11.30

### Insight Server: v0.22.0

#### 新增

- **新增** 支持网络连通性拨测功能
- **新增** 通过 YAML 导入告警策略
- **新增** 支持操作审计记录

### 优化

- **优化** 安装时自动下发 OTel instrumentation CR

#### 修复

- **修复** Elasticsearch 索引初始化失败的问题

### Insight Agent: v0.22.0

- **修复** Fluentbit 采集目录不兼容 DCE 4.0 的问题

## 2023.10.31

!!! note

    Insight Agent v0.21.0 修复了 PodMonitor 配置后会重复集多份 JVM 指标数据的问题，建议升级至该版本进行修复。
    详情可查看[已知问题](../../insight/quickstart/install/knownissues.md)。

### Insight Server: v0.21.0

#### 新增

- **新增** 命名空间维度监控

#### 优化

- **优化** 更新 Insight 导航栏结构
- **优化** 点击链路分布图可快速查看对应链路详情

#### 修复

- **修复** 无法查看到容器日志的上下文
- **修复** 初始化事件索引出错

### Insight Agent: v0.21.0

#### 修复

- **修复** 链路查询中的操作中出现异常 Span 名称
- **修复** 银行麒麟 Kylin-V10(SP3) 操作系统中，tailing-sidecar 启动的容器无法正常启动

## 2023.08.31

### Insight Server: v0.20.0

#### 新增

- **新增** 容器事件告警
- **新增** 链路查询相关日志
- **新增** 事件详情增加元数据
- **新增** 日志支持 Lucene 语法查询

#### 优化

- **优化** 集群状态异常时增加提示
- **优化** 日志过滤的条件增强
- **优化** 告警静默条件创建时允许添加相同的标签
- **优化** 节点日志支持通过文件路径过滤
- **优化** 增加针对 CoreDNS 的内置告警策略

#### 修复

- **修复** 系统组件中 Elasticsearch 的创建时间不正确
- **修复** 日志上下文查询出来的日志条数和实际的日志条数不符
- **修复** 告警修复建议中跳转链接重定向
- **修复** 事件查询中部分数据的兼容性问题
- **修复** 拓扑图图例颜色错误问题
- **修复** 拓扑图取消集群、命名空间边界时所有的节点变成外部节点问题
- **修复** 消息模板中要是任一通知类型的模板内容出错，就会导致告警无法通知

### Insight Agent: v0.20.0

#### 优化

- **优化** 日志和链路数据支持通过 Kafka 消费数据。

#### 修复

- **修复** 与 Openshift 集群的兼容性问题
- **修复** 与 Kubernetes v0.18.20 的兼容性问题
- **修复** 与 DCE 4.0 的兼容性问题
- **修复** 指标计算异常的问题

## 2023.07.30

### v0.19.0

#### 新增

- **新增** Kubenetes 事件分析及查询功能
- **新增** 内置告警策略提供告警修复建议
- **新增** 支持自定义日志导出字段及格式

#### 优化

- **优化** 系统组件中获取 Elasticsearch 组件状态的逻辑
- **优化** 支持在安装参数中配置是否导入默认消息模板

#### 修复

- **修复** 部分角色查看告警规则详情的指标时无权限
- **修复** 部分角色在创建、编辑、预览告警静默时无权限
- **修复** 部分角色查看告警消息的详情无权限
- **修复** 链路查询气泡图中显示的时间错误
- **修复** 查询容器日志时未传递命名空间的问题
- **修复** 消息模板中默认变量的自定义标签参数有误
- **修复** 在切换过滤条件时等未发送新请求
- **修复** 告警静默的创建、编辑、预览无权限
- **修复** 概览中日志统计值为 0 的问题
- **修复** 部分内置告警策略不生效的问题

## 2023.07.01

### v0.18.0

#### 新增

- **新增** 日志告警
- **新增** 采集管理增加集群状态
- **新增** 静默规则列表增加静默条件
- **新增** 邮箱配置检测
- **新增** 支持 PostgreSQL 和 Kingbase 作为系统数据库
- **新增** Nvidia GPU 监控仪表盘

#### 优化

- **优化** 更新服务拓扑的图例
- **优化** 服务详情操作指标增加指标平均值并支持排序
- **优化** 链路查询支持 Span、延时、发生时间等排序
- **优化** 告警策略配置通知时下拉框增加搜索
- **优化** 告警模板支持格式化时区
- **优化** 升级 **opentelemetry collector** Chart 版本从 **0.50.1** 到 **0.59.3**
- **优化** 升级 **opentelemetry Operator** Chart 版本从 **0.26.1** 到 **0.30.1**

#### 修复

- **修复** 告警静默预览匹配告警时预览和实际生效静默的告警不相同的问题
- **修复** 系统组件中组件版本错误的问题
- **修复** 仪表盘中列表标题错误
- **修复** 通过告警列表创建静默，预览匹配告警数据无返回
- **修复** 部分环境中 Fluentbit 第一次无法启动的问题

## 2023.06.01

### v0.17.0

!!! warning

    在 v0.17.x 版本中将 kube-prometheus-stack chart 版本从 41.9.1 升级至 45.28.1,
    其中使用的 CRD 也存在一些字段的升级，如 servicemonitor 的 __attachMetadata__ 字段，
    升级 insight agent 前，请参考：
    [从 v0.16.x（或更低版本）升级到 v0.17.x](../quickstart/install/upgrade-note.md#v016x-v017x)。

#### 新增

- **新增** 支持查看活动告警和历史告警详情
- **新增** 支持通过告警快速创建静默规则
- **新增** 告警支持短信通知
- **新增** 邮箱通知支持发送测试信息
- **新增** 邮箱通知的消息模板支持自定义邮箱主题
- **新增** 消息模板增加变量说明
- **新增** Insight Server 组件支持默认高可用

#### 优化

- **优化** 链路查询展示完整 TraceID
- **优化** 链路查询增加服务为空时的提示
- **优化** JVM 监控增加无数据提示
- **优化** 告警策略详情不通知时不显示其他参数
- **优化** 增加 OpenTelemetry Operator 的资源限制
- **优化** 升级 Grafana 版本到 v9.3.14
- **优化** 升级 tailing sidecar 版本从 v0.5.6 到 v0.7.0
- **优化** 升级 kube-prometheus-stack 版本到 v45.28.1
- **优化** 升级 prometheus 版本到 v2.44.0

#### 缺陷

- **修复** 服务拓扑命名空间为空时前端生效的问题
- **修复** 服务拓扑状态说明的文档链接无效的问题
- **修复** 创建告警策略时显示的命名空间和无状态负载重复的问题
- **修复** 告警列表和告警策略中的告警列表缺少触发值数据
- **修复** 告警静默添加静默条件时类型、关键字和值的必填校验错误的问题
- **修复** 告警静默时间范围时区不生效的问题
- **修复** 为工作负载类型创建 PromQL 规则时没有告警告警对象的问题
- **修复** 修改内置告警规则时无法保存的问题
- **修复** 组件中时区写死的问题

## 2023.04.28

### v0.16.0

!!! warning

    可观测性 Insight v0.16.0 使用了 vmalertmanagers CRD 的新特性参数 __disableRouteContinueEnforce__ ,
    升级 insight server 前，请参考[从 v0.15.x（或更低版本）升级到 v0.16.x](../quickstart/install/upgrade-note.md)

#### 新增

- **新增** Java 应用的 JVM 监控。
- **新增** 设置告警静默通知。
- **新增** 告警策略功能，支持在一个告警策略中增加多条告警规则进行管理。
- **新增** Nginx Ingress、Contour 等组件监控仪表盘。
- **新增** 服务拓扑支持开启或关闭虚拟节点。
- **新增** 当前活动告警的数量统计。
- **新增** 内置 HwameiStor 组件的 ServiceMonitor。
- **新增** 域名支持访问 sub path。
- **新增** 【仪表盘】根据全局管理的配置增加备案信息
- **新增** 【仪表盘】域名支持访问 sub path。

#### 优化

- **优化** 内置消息模板的内容。
- **优化** 调整内置告警规则到对应的策略中。
- **优化** 服务命名空间为空的筛选显示问题。
- **优化** 服务列表增加缓存。

#### 修复

- **修复** 搜索中文无效的问题。
- **修复** 服务拓扑命名空间权限无法查看拓扑图的问题。
- **修复** 【仪表盘】麒麟图标的样式问题
- **修复** 【仪表盘】tooltip 过长的问题

## 2023.04.04

### v0.15.4

#### 优化

- **优化** 更新 ES 索引的默认主分片数，使其与中间件默认的 ES 节点数匹配。
- **优化** 修改 JVM 信息 API 响应体结构。

#### 修复

- **修复** 修复多次触发警报记录
- **修复** Fluentbit CVE-2021-46848，从 2.0.5 升级到 2.0.8
- **修复** 检查许可证资源的任务
- **修复** 清除警报历史记录的 SQL 语句
- **修复** 英文仪表盘存在的中文问题

## 2023.03.30

### v0.15.1

#### 新增

- **新增** JVM 指标采集并集成监控面板
- **新增** 链路接入的引导
- **新增** 服务拓扑支持错误率、请求延时过滤
- **新增** 链路支持 Trace ID 搜索
- **新增** Prometheus 组件开启自动垂直扩容

#### 优化

- **优化** 拓扑图虚拟节点的样式
- **优化** 服务拓扑虚拟节点增加开关

#### 修复

- **修复** 容器组运行状态的显示样式
- **修复** 未开启链路功能时，隐藏相关配置参数
- **修复** 部分前端样式不生效问题
- **修复** 采集容器组指标无数据问题
- **修复** 在 OpenShift 集群无法安装 insight-agent 问题

## 2023.02.27

### v0.14.6

#### 新增

- **新增** 图表增加刷新按钮
- **新增** 服务拓扑支持选择多集群并支持通过服务名搜索
- **新增** 服务拓扑详情及流量出口、入口的指标
- **新增** 服务拓扑详情中点击服务名称可跳转到服务的详情
- **新增** 服务监控的列表及流量出口、入口的指标
- **新增** 系统组件监控列表
- **新增** CoreDNS 监控面板
- **新增** 安装时 Insight Agent 添加是否开启 kubeAudit 采集设置

#### 优化

- **优化** 链路查询中的过滤条件并可查看存在 Error 的链路
- **优化** 链路查询的散点图更新为气泡图
- **优化** 将 Prometheus 的指标保留时间缩短至 2 小时
- **优化** VMStorage 的 retentionPeriod 默认参数调整为 1 个月
- **升级** fluentbit 的 helm chart 版本至 0.24.0
- **更新** **tailing-sidecar/operator** 的镜像
- **更新** 全局采集规则间隔为 60 秒

#### 修复

- **修复** 内置 vmcluster 仪表盘
- **修复** 未开启链路时，导航栏无法加载
- **修复** 系统组件跳转查看详情的链接错误
- **修复** 采集管理列表快捷安装/卸载的链接不对
- **修复** 指标高级查询查询后，下拉框的指标联想与图表重合部分无法选中
- **修复** 修改历史告警存储时长时允许输入小数
- **修复** 当告警规则生成多个告警时发送多个通知
- **修复** **vmalert** and **vmalertmanager** 的 **configmap-reload** 镜像错误
- **修复** ARM 架构中 Insight Agent 的 fluentbit

## 2023.01.10

### v0.13.2

#### 修复

- **修复** insight-agent 中 **kubernetes-event-exporter** 镜像地址错误的问题
- **修复** 通过资源名称过滤告警 API

## 2023.12.30

### v0.13.1

#### 修复

- **修复** 构建离线包增加 **.relok8s-images** 文件
- **修复** 调整 insight-agent 中组件 **otel-collector** 端口对应的端口名

## 2022.12.29

### v0.13.0

#### 新功能

- **新增** 支持修改历史告警存储时间
- **新增** 采集管理组件状态详情
- **新增** 内置消息模板
- **新增** 图表指标计算说明

### 优化

- **优化** 日志列表字段显示
- **优化** insight-agent 的判断逻辑
- **升级** Jaeger 的 Chart 版本从 v0.62.1 升级到 0.65.1

### 修复

- **修复** 部分内置告警规则不生效
- **修复** 创建规则时修复名称可重名的错误
- **修复** 钉钉机器人以 '-' 结尾的问题
- **修复** 告警规则中不区分大小写的模糊搜索
- **修复** 服务指标错误延迟计算不准确
- **修复** Jaeger 查询出现 **too many open files** 的问题
- **修复** es 索引翻转别名和清理策略未起作用的问题

## 2022.11.28

### v0.12

#### 新功能

- **新增** insight-agent Helm 模板安装时支持表单化

#### 优化

- **优化** PromQL 查询支持原始的指标
- **优化** 拓扑图的样式
- **升级** 内置 MySQL 镜像版本，从 v5.7.34 升级到 v8.0.29.
- **升级** Fluentbit ARM 架构的 helm Chart 版本从
- **升级** kube-prometheus-stack 的 helm Chart 版本从 v39.6.0 升级至 v41.9.1
- **更新** 使用的 Bitnami 的镜像，包含 grafana-operator, grafana, kubernetes-event-exporter
- **更新** prometheus 相关的的 API 代理地址，将 **/prometheus** 修改为 **/apis/insight.io/prometheus**

#### 修复

- **修复** 服务列表缓存逻辑
- **修复** 内置规则不生效的问题
- **修复** 请求延时单位问题
- **修复** Insight 内部链路的问题
- **禁用** vm-stack 中的 PSP 资源
- **修复** victoriaMetrics operator 在 Kubernetes 1.25 中不可用的问题。
- **修复** 前端镜像的浏览器兼容性问题

## 2022-11-21

### v0.11

#### 优化

- **增加** 链路排障和对组件 **Jaeger** 监控的仪表盘
- **优化** 告警列表、消息模板列表支持排序
- **优化** 过滤掉未安装 **insight-agent** 的集群
- **优化** 链路查询时默认按 span 开始时间排序

#### 缺陷修复

- **修复** 无数据的 **仪表盘** ，包含 OpenTelemetry 相关的仪表盘
- **修复** 部分日志路径下无内容的问题
- **修复** 删除错误的告警规则：KubeletPodStartUpLatencyHigh

#### 其他

- **victoria-metrics-k8s-stack** helm chart 升级至 v0.12.6
- **opentelemetry-collector** helm chart 从 v0.23.0 升级至 v0.37.2
- **jaeger** helm chart 从 v0.57.0 升级至 v0.62.1
- **fluentbit** helm chart 从 v0.20.9 升级至 v1.9.9
- **kubernetes-event-exporter** helm chart 从 v1.4.21 升级至 v2.0.0

## 2022-10-20

### v0.10

#### 功能特性

- 支持与 OTel 服务名称关联的容器管理 Service 名称，以辨别是否启用了服务链路
- 在全局 OTel 一栏更新了默认的跟踪样本策略
- 将相扑（适用于审计日志）exporter port 8080 更改为 80
- 使用 go-migrate 管理数据库迁移版本
- 修复图形 API 中多集群和多命名空间过滤器不正常的问题
- 支持构建 ARM 镜像

#### 安装

- Fluentbit 支持 Dockder 和 containerd 日志的解析器
- 修复 var/log/ UTC 问题
- Fluentbit 支持 elasticsearch 输出跳过 TLS 验证
- K8s 审计日志过滤器支持从 Helm 值获取规则
- 修复 centos7/ubuntu20 主机日志时间的解析问题
- 提升 OTel Operator 版本，移除 Operator 中随自签名证书一起部署的 cert-manager 依赖项
- 设计了 jaeger collector 指标
- 提升 tailing-sidecar 版本
- Jaeger 支持 elasticsearch 输出跳过 TLS 验证
- 在 A 模式中禁用 jaeger 组件

#### 其他

- 新增 OTel collector grafana 仪表盘
- 新增 Insight 概览中文页面

## 2022-9-25

### v0.9

#### 功能特性

- Support kpanda service name associated with the otel service name, identify whether the service tracing enabled.
- Update default tracing sample policies in global otel col.
- Change sumologic(work for audit log) exporter port 8080 to 80.
- Use go-migrate to manage db migration version.
- Fix multi cluster and multi namespaces filter not work well in graph API.
- Support build arm image.

#### 安装

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

#### 其他

- Add otel collector grafana dashboard.
- Add Insight Overview Chinese version.

## 2022-8-21

### v0.8

#### 功能特性

- Migrate graph server into insight server.
- Add cluster_name param to graph query request.
- Add userinfo api.
- Add GetREDMetrics API in GraphQueryService.
- Add GetHelmInstallConfig api to get global cluster service addresses for agent to use.
- Complete auth module.
- Add init cmd/initcontainer for elasticsearch alias and ilm policy

#### 架构调整

- Bump up otel operator in agent chart.
- Add kibana as builtin tools.
- Reduce traces/logs chart's default values.
- Add Helm values parameters documentation.
- Polished Helm parameters.

#### 安装

- Add audit log enable/disable feature.
- Move Fluentbit config to a ConfigMap.

## 2022-7-20

### v0.7

#### 破坏变更

- Modify QueryOperations and GetServiceApdex's API definition in Tracing service.
- Remove resolve alert api.
- fix NFD master crash when CRDs missed.

#### 功能特性

- Remove jaeger relate code in span-metric.
- Add index policy for skoala gateway logs.
- Add lua filter for Ghippo audit logs.
- Add global config api.
- Disable cache in vmselect component.
- Dock with ghippo roles.
- Expose metric **insight_cluster_info** in server.
- Add log.SearchLog API for SKoala, accept ES query DSL and return raw ES response.
- Bump up OTelcol helm chart version to 0.21.1 and update otelcol architecture.
- support mspider tracing.
- Bump up OTelcol helm chart version to 0.23.0.
- Add default tracing sample policies in global otel col.

#### 架构调整

- Use GrafanaOperator Stack to replace original Grafana Stack.
- Replace insight-overview dashboard.
- Add GrafanaDashboard, GrafanaDatasource CRDs.

## 2022-6-23

### v0.6

#### 破坏变更

- Modify insight deployment and service name to insight-server.
- Modify trace relate metric query API response type.
- Using the unified paging mechanism

#### 功能特性

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

#### 架构调整

- Add node-feature-discovery subchart for License module.
- Add opentelemetry-collector subcharts to insight chart.
- Delete audit log OUTPUT config in fluent-bit.
- Add groupbytrace processor to generate trace/span number metrics.
- Add built-in Elasticsearch chart and enabled by default.

#### 安装

- Upgrade victoria-metrics-k8s-stack chart version from 0.6.5 to 0.9.3.
- Add servicemonitor for components in victoria-metrics-k8s-stack.
- Modify insight components resource.

## 2022-5-18

### v0.5

#### 功能特性

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

#### 安装

- 添加了内置 mysql
- 将 GO 版本升级到 1.17
- 将 insight 服务器服务端口从 8000 更改为 80
- 将 insight 服务器/指标端口从 2022 更改为 81

#### 文档

- 新增文档站术语表
- 新增文档站基本概念任务和实例、数据模型、查询语言等 4 个页面
- 新增用户指南 - 场景监控、数据查询、告警中心等文档
- 文档站新增：[产品优势](../intro/benefits.md)、[指标查询](../user-guide/data-query/metric.md)、[链路查询](../user-guide/trace/trace.md)、仪表盘、[概述](../user-guide/dashboard/overview.md)

## 2022-4-22

### v0.4

#### 功能特性

- 增加告警通知模块主要 API
- 升级并适配 kpanda 0.4.x API
- 为系统日志增加日志所属文件路径信息
- 增加查询单条日志上下文 API
- 增加查询 Kubernetes Event API
- 增强 Insight 自身可观测性能力，提供自身的指标接口和查询链路信息
- 通过反向代理 Jaeger Query 的 API 供前端使用
- 增加 Query Tracing Operations 相关 API
- 增加 Span Metric 相关 API

#### 测试

- 增加 E2E 用例覆盖率徽章
- 补充告警通知相关的测试用例文档
- 增加日志相关接口的 E2E 测试

#### 文档

- 添加整体双语文档站结构及主要内容
- 增加文档所需插件，优化渲染
- 完成 ROADMAP 内容
- 将文档 ROADMAP 内容合并如总 ROADMAP 文件
- 更新文档结构

## 2022-3-18

### v0.3

#### 功能特性

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

#### Helm Charts

- 添加 Jaeger helm chart
- 添加 OpenTelemetry collector helm chart
- 添加 tailing-sidecar-operator 作为日志收集的配件/解决方案/插件
- 在 fluentbit 中添加/变量/日志/消息收集
- 将 kube exporter 添加到 collecot kube 群集事件日志
