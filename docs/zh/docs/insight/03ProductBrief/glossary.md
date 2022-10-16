# 常见术语

本页面列出了一些有关可观测性 (Insight) 的常见术语。

- Alert（告警）

    告警是 Insight 主动触发告警规则后的结果。告警从 Insight 发送到 Alertmanager。

- Alert rules（告警规则）

    一个返回值是布尔值的 PromQL 表达式，它描述了指标或自定义指标是否处于阈值范围中，如果不满足将产生一条告警事件。

- Alertmanager（告警管理器）

    Alertmanager 接收告警，将其聚合分组，消除重复的告警，再应用一些策略后，通过电子邮件、企业微信、钉钉等向用户发送告警信息。

- Client Library（客户端库）

    为需要监控的服务生成相应的 metrics 并暴露给 Insight server。当 Insight server 来 pull 时，将直接返回实时状态的指标。

- Collector（收集器）

    收集器是由一组指标定义的 exporter 的组成部分。如果是直接检测（Direct instrumentation）的一部分，那么可能是一个指标；如果是从另一个系统拉取的指标，那么可能是多个指标。

- Dashboard（仪表盘）

    仪表盘是可视化管理的一种表现形式，即对数据、情报等状况一目了然的表现，它通过形象直观而又色彩适宜的各种视觉感知来展示信息。通过可视化图形展示平台的实时情况和 DCE 中所有的性能指标。

- Endpoint（端点）

    一种可被刮取指标的数据源，通常对应于单个进程。

- Event（告警消息）

    告警规则被触发时的记录信息，记录了告警规则、触发时间、当前系统状态；同时将触发相应的动作，例如发送邮件。

- Exporter

    一个能够提供指标的服务，往往被理解为监控对象。Exporter 将现有第三方服务的指标暴露给 Insight。Exporter 是随着获取指标的应用程序运行的二进制文件，将非 Insight 格式的指标暴露为 Insight 支持的格式。

- Metrics（指标）

    使用 [open-metric](https://openmetrics.io/) 格式描述，衡量软件或硬件系统中某种属性的程度的标准。对资源性能的数据描述或状态描述，指标由命名空间、维度、指标名称和单位组成。有关更多信息，参见[指标类型](../../reference/basic-knowledge/insight.md#数据模型)。

- Log（日志）

    系统运行过程中变化的一种抽象数据，其内容为指定对象的操作及其操作结果按时间的有序集合。
- Trace（链路）

    记录单次请求范围内的处理信息，其中包括服务调用和处理时长等数据。

- Instance（实例）

    实例是一个标签，唯一标识 job 中的某个目标。
  
- Job（任务）

    这是具有相同用途的目标任务集合，例如为可扩展性或可靠性而复制的一组类似进程。有关更多信息，参见[任务和实例](../../reference/basic-knowledge/insight.md#任务和实例)

- Metrics（指标）

    使用 [open-metric](https://openmetrics.io/) 格式描述，衡量软件或硬件系统中某种属性的程度的标准。对资源性能的数据描述或状态描述，指标由命名空间、维度、指标名称和单位组成。有关更多信息，参见[指标类型](../../reference/basic-knowledge/insight.md#数据模型)。

- Notification（通知）

    由系统通过邮件等渠道发送给用户的告警事件信息。通知是一个或多个告警形成的消息组，通过 Alertmanager 发送电子邮件、企业微信或钉钉消息。

- PromQL

    这是 Insight 内置的数据查询语言，提供了对时间序列数据的丰富查询功能，支持聚合和逻辑运算能力。有关更多信息，参见[数据查询语言](../../reference/basic-knowledge/insight.md#查询语言-promql)

- Pushgateway

    Pushgateway 保存来自批处理作业的最新指标推送。这使得 Insight 可以在终止后刮取指标。

- Recording Rule（自定义指标）

    一个被命名的 PromQL 表达式，这是将多个指标通过计算而得到的新指标，用来描述更加完整和复杂的系统状态。

- Sample（样本）

    样本是时间序列中某个时间点的单个值。在 Insight 中，每个样本由一个 float64 值和一个毫秒精度的时间戳组成。

- Service Discovery（服务发现）

    一个用于 Kubernetes 环境的服务发现配置，用于批量且自动地接入 Kubernetes 上的监控点。

- Target（监控目标）

    被监控的对象；系统会定时向监控点发起抓取任务，从中获取指标。
