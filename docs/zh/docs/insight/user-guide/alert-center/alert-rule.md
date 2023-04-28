# 告警规则

当资源的指标数据满足阈值条件时会产生告警事件，系统则将自动触发的告警上报至`告警列表`。

## 创建告警规则

1. 进入`可观测性`后，在左侧导航栏中，选择`告警中心` -> `告警规则`，点击`新建指标规则`按钮。

    ![新建指标规则](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/rule01.png)

2. 在`创建告警规则`页面中，分别填写基本信息，选择指标，触发条件等信息。

    ![填表](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/rule02.png)

    - 选择指标
  
        支持规则模板和 PromQL 规则两种指标：
    
        - PromQL 规则：输入一个 PromQL 表达式，具体请[查询 Prometheus 表达式](https://prometheus.io/docs/prometheus/latest/querying/basics/)。
      
        - 规则模板：预定义了基础指标，可以按节点、工作负载设定要监控的指标。

    - 触发条件：为指标设定阈值、触发时间、告警级别等。

	- 触发时间：告警被触发且持续时间达到该设定值后，告警规则将变为触发中状态。

	- 告警级别：包含紧急、警告、提示三种级别。

    - 告警通知：接收告警消息的对象，支持邮箱、钉钉、企业微信、Webhook 四种接收方式，参见[通知配置](message.md)。

3. 配置完成后，点击`确认`按钮，返回告警规则列表。

!!! tip

    新建的告警规则为`未触发`状态。一旦满足规则中的阈值条件和持续时间后，将变为`触发中`状态。

## 其他操作

在列表右侧点击`...`，在弹出菜单中选择`编辑`、`复制`或`删除`，可以修改、复制或删除告警规则。

![其他操作](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/rule03.png)

!!! warning

    删除后的告警规则将完全消失，请谨慎操作。
