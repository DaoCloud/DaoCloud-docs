# 消息模板

可观测性提供自定义消息模板内容的能力，支持邮件、企业微信、钉钉、Webhook 等不同的通知对象定义不同的消息通知内容。

## 创建消息模板

1. 在左侧导航栏中，选择 __告警中心__ -> __消息模板__。

   - Insight 默认内置中英文两个模板，以便用户使用。

    ![点击按钮](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/template00.png)

2. 点击 __新建消息模板__ 按钮，填写模板内容。

    ![点击按钮](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/template01.png)

!!! info

    可观测性预置了消息模板。若需要定义模板的内容，请参考：[配置通知模板](../../reference/notify-helper.md)

### 参数说明

| 参数 | 变量  | 描述 |
| -- | -- | -- |
| 规则名称 | {{ .Labels.alertname }} | 触发告警的规则名称 |
| 策略名称 | {{ .Labels.alertgroup }}  | 触发告警规则所属的告警策略名称 |
| 告警级别 | {{ .Labels.severity }} | 触发告警的级别 |
| 集群 | {{ .Labels.cluster }} | 触发告警的资源所在的集群 |
| 命名空间 | {{ .Labels.namespace }} | 触发告警的资源所在的命名空间 |
| 节点 | {{ .Labels.node }} | 触发告警的资源所在的节点 |
| 资源类型 | {{ .Labels.target_type }} | 告警对象的资源类型 |
| 资源名称 | {{ .Labels.target }} | 触发告警的对象名称 |
| 触发值 | {{ .Annotations.value }} | 触发告警通知时的指标值 |
| 发生时间 |  {{ .StartsAt }} | 告警开始发生的时间 |
| 结束时间 |  {{ .EndsAT }} | 告警结束的时间 |
| 描述 |  {{ .Annotations.description  }} | 告警的详细描述 |
| 标签 |  {{ for .labels}} {{end}} | 告警的所有标签，使用 for 函数遍历 labels 列表，获取告警的所有标签内容。 |

## 编辑或删除消息模板

在列表右侧点击 __︙__，在弹出菜单中选择 __编辑__ 或 __删除__，可以修改或删除消息模板。

!!! warning

    请注意，删除模板后无法恢复，请谨慎操作。
