# Alert rules

When the metric data of the resource meets the threshold condition, an alert event will be generated, and the system will report the automatically triggered alert to the `alert list`.

## Create alert rules

1. After entering `Observability`, in the left navigation bar, select `Alert Center` -> `alert Rules`, and click the `New metric Rule` button.

    

2. On the `Create Alert Rule` page, fill in the basic information, select metrics, trigger conditions and other information.

    

    - select metric
  
        Two types of metrics, rule template and PromQL rule, are supported:
    
        - PromQL rule: Enter a PromQL expression, please [Query Prometheus Expression](https://prometheus.io/docs/prometheus/latest/querying/basics/) for details.
      
        - Rule template: The basic metrics are predefined, and the metrics to be monitored can be set according to nodes and workloads.

    - Trigger conditions: set the threshold, trigger time, alert level, etc. for the metric.

- Trigger time: After the alert is triggered and the duration reaches the set value, the alert rule will become in the triggering state.

- alert level: It includes three levels: emergency, warning, and prompt.

    - alert notification: The object that receives the alert message supports four receiving methods: email, DingTalk, WeChat, and Webhook, see [Notification Configuration](message.md).

3. After the configuration is complete, click the `Confirm` button to return to the list of alert rules.

!!! tip

    The newly created alert rule is in the state of `not triggered`. Once the threshold condition and duration in the rule are met, it will become `Triggering` status.

## Other operations

Click `...` on the right side of the list, and select `Edit`, `Copy` or `Delete` in the pop-up menu to modify, copy or delete the alert rule.



!!! warning

    The deleted alert rule will disappear completely, please operate with caution.