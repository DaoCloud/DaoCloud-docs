# 系统组件

在系统组件页面可快速的查看可观测性模块中系统组件的运行状态，当系用组件发生故障时，会导致可观测模块中的部分功能不可用。

1. 进入`可观测性` 产品模块，
2. 在左边导航栏选择 `系统管理 -> 系统组件`。
  
    ![系统组件](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/system00.png)

## 组件说明

|模块 | 组件名称             | 说明          |
| ----- | --------------- | ----------------------------------------------- |
|指标 | vminsert-insight-victoria-metrics-k8s-stack       | 负责将各集群中 Prometheus 采集到的指标数据写入存储组件。该组件异常会导致无法写入工作集群的指标数据。 |
|指标 | vmalert-insight-victoria-metrics-k8s-stack        | 负责生效 VM Rule 中配置的 recording 和 Alert 规则，并将触发的告警规则发送给 alertmanager。           |
|指标 | vmalertmanager-insight-victoria-metrics-k8s-stack | 负责在告警触时发送消息。该组件异常会导致无法发送告警信息。                                           |
|指标 | vmselect-insight-victoria-metrics-k8s-stack       | 负责查询指标数据。该组件异常会导致无法查询指标。                                                     |
|指标 | vmstorage-insight-victoria-metrics-k8s-stack      | 负责存储多集群的指标数据。                                                                           |
|仪表盘 | grafana-deployment                                | 提供监控面板能力。该组件异常会导致无法查看内置的仪表盘。                                             |
|链路 | insight-jaeger-collector                          | 负责接收 opentelemetry-collector 中链路数据并将其进行存储。                                          |
|链路 | insight-jaeger-query                              | 负责查询各集群中采集到的链路数据。                                                                   |
|链路 | insight-opentelemetry-collector                   | 负责接收各子集群转发的链路数据                                                                       |
|日志 | elasticsearch                                     | 负责存储各集群的日志数据。                                                                           |

!!! note

    若使用外部 Elasticsearch 可能无法获取部分数据以致于 Elasticsearch 的信息为空。
