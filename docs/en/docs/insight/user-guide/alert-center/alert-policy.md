# Alert Policies

In addition to the built-in alert policies, DCE 5.0 allows users to create custom alert policies. Each alert policy is a collection of alert rules that can be set for clusters, nodes, and workloads. When an alert object reaches the threshold set by any of the rules in the policy, an alert is automatically triggered and a notification is sent.

Taking the built-in alerts as an example, click the first alert policy __alertmanager.rules__ .

![alert policy](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy01.png)

You can see that some alert rules have been set under it. You can add more rules under this policy, or edit or delete them at any time. You can also view the historical and active alerts related to this alert policy and edit the notification configuration.

![alertmanager.rules](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy02.png)

## Creating Alert Policies

1. Select __Alert Center__ -> __Alert Policies__ , and click the __Create Alert Policy__ button.

    ![alert policy](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy01.png)

2. Fill in the basic information, select one or more clusters, nodes, or workloads as the alert objects, and click __Next__ .

    ![basic information](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy03.png)

3. The list must have at least one rule. If the list is empty, please __Add Rule__ .

    ![add rule](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy04.png)

    Create an alert rule in the pop-up window, fill in the parameters, and click __OK__ .

    ![create rule](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy05.png)

    - Template rules: Pre-defined basic metrics that can monitor CPU, memory, disk, network, etc.
    - PromQL rules: Input a PromQL expression, please [query Prometheus expressions](https://prometheus.io/docs/prometheus/latest/querying/basics/).
    - Duration: After the alert is triggered and the duration reaches the set value, the alert policy will become a triggered state.
    - Alert level: Including emergency, warning, and information levels.
    - Advanced settings: Custom tags and annotations.

4. After clicking __Next__ , configure notifications.

    ![notification configuration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy06.png)

5. After the configuration is complete, click the __OK__ button to return to the Alert Policy list.

!!! tip

    The newly created alert policy is in the __Not Triggered__ state. Once the threshold conditions and duration specified in the rules are met, it will change to the __Triggered__ state.

### Creating Log Rules

After filling in the basic information, click __Add Rule__ and select __Log Rule__ as the rule type.

Creating log rules is supported only when the resource object is selected as a node or workload.


**Field Explanation:**

- __Filter Condition__ : Field used to query log content, supports four filtering conditions: AND, OR, regular expression matching, and fuzzy matching.
- __Condition__ : Based on the filter condition, enter keywords or matching conditions.
- __Time Range__ : Time range for log queries.
- __Threshold Condition__ : Enter the alert threshold value in the input box. When the set threshold is reached, an alert will be triggered. Supported comparison operators are: >, ≥, =, ≤, <.
- __Alert Level__ : Select the alert level to indicate the severity of the alert.

### Creating Event Rules

After filling in the basic information, click __Add Rule__ and select __Event Rule__ as the rule type.

Creating event rules is supported only when the resource object is selected as a workload.

**Field Explanation:**

- __Event Rule__ : Only supports selecting the workload as the resource object.
- __Event Reason__ : Different event reasons for different types of workloads, where the event reasons are combined with "AND" relationship.
- __Time Range__ : Detect data generated within this time range. If the threshold condition is reached, an alert event will be triggered.
- __Threshold Condition__ : When the generated events reach the set threshold, an alert event will be triggered.
- __Trend Chart__ : By default, it queries the trend of event changes within the last 10 minutes. The value at each point represents the total number of occurrences within a certain period of time (time range) from the current time point to a previous time.

## Other Operations

Click __⋮__ at the right side of the list, then choose __Delete__ from the pop-up menu to delete an alert strategy. By clicking on the strategy name, you can enter the strategy details where you can add, edit, or delete the alert rules under it.

![alert rule](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy07.png)

!!! warning

    Deleted alert strategies will be permanently removed, so please proceed with caution.
