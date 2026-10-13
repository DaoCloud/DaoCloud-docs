# Alert Policies

An alert policy is a set of rules and conditions defined in the observability system, used to detect and trigger alerts so that the relevant personnel or systems can be notified in time when the system is abnormal or reaches a preset threshold.

Each alert policy is a collection of alert rules. It supports setting alert rules for resources such as clusters, nodes, and workloads, as well as logs and events. When an alert object reaches the threshold set by any rule under the policy, an alert is automatically triggered and a notification is sent.

## View Alert Policies

1. Click __Observability__ in the top navigation bar.
2. In the left navigation bar, select __Alert Center__ -> __Alert Policies__.

    - Cluster: Click the cluster drop-down box to switch clusters.
    - Namespace: Click the namespace drop-down box to switch namespaces.

    ![alert policy](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy01.png)

3. Click the alert policy name to view the basic information, rules, and notification configuration of the policy.

    1. In the rule list, you can view the rule type, rule expression, level, status, and other information.
    2. In the policy details, you can add, edit, or delete the alert rules under it.

    ![alertmanager.rules](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy02.png)

## Create Alert Policies

1. Fill in the basic information, select one or more clusters, nodes, or workloads as the alert objects, and click __Next__ .

    ![basic information](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy03.png)

    !!! note

        - Selecting `all clusters, nodes, or workloads`: The created alert rules take effect for all clusters with insight-agent installed.
        - Selecting a single or multiple clusters, nodes, or workloads: The created alert rules only take effect for the selected resource objects.
        - In addition, users can only set alert rules for clusters and namespaces they have permission to.

### Manually Add Rules

1. In the second step of creating an alert policy, click `Add Rule` in the upper-right corner of the list.

    ![add rule](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy04.png)

2. Create an alert rule in the pop-up window, fill in the parameters, and click __OK__ .

    ![create rule](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy05.png)

    - Template rules: Pre-defined basic metrics, and you can set metrics to monitor by CPU, memory, disk, and network.
    - PromQL rules: Input a PromQL expression. For details, please [query Prometheus expressions](https://prometheus.io/docs/prometheus/latest/querying/basics/).
    - Duration: After the alert is triggered and the duration reaches the set value, the alert policy will become a triggering state.
    - Alert level: Including emergency, warning, and information levels.
    - Advanced settings: Custom tags and annotations.

    !!! info

        The system defines built-in labels. If the `key` value of a custom label is the same as that of a built-in label, the custom label does not take effect.
        The built-in labels are: `severity`, `rule_id`, `source`, `cluster_name`, `group_id`, `target_type`, and `target`.

#### Create Log Rules

After filling in the basic information, click __Add Rule__ and select __Log Rule__ as the rule type.

!!! note

    Creating log rules is supported only when the resource object is selected as a node or workload.

![notification configuration](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/policy10.png)

**Field Explanation:**

- __Filter Condition__ : Field used to query log content, supports four filtering conditions: AND, OR, regular expression matching, and fuzzy matching.
- __Condition__ : Based on the filter condition, enter keywords or matching conditions.
- __Time Range__ : Time range for log queries.
- __Threshold Condition__ : Enter the alert threshold value in the input box. When the set threshold is reached, an alert will be triggered. Supported comparison operators are: >, ≥, =, ≤, <.
- __Alert Level__ : Select the alert level to indicate the severity of the alert.

#### Create Event Rules

After filling in the basic information, click __Add Rule__ and select __Event Rule__ as the rule type.

!!! note

    Creating event rules is supported only when the resource object is selected as a workload.

![notification configuration](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/policy04.png)

**Field Explanation:**

- __Event Rule__ : Only supports selecting the workload as the resource object.
- __Event Reason__ : Different event reasons for different types of workloads, where the event reasons are combined with "AND" relationship.
- __Time Range__ : Detect data generated within this time range. If the threshold condition is reached, an alert event will be triggered.
- __Threshold Condition__ : When the generated events reach the set threshold, an alert event will be triggered.
- __Trend Chart__ : By default, it queries the trend of event changes within the last 10 minutes. The value at each point represents the total number of occurrences within a certain period of time (time range) from the current time point to a previous time.

### Import Rule Templates

1. Click __Import Template__ to batch import alert rules from alert templates already created by the platform administrator.

    ![alert template](../../images/import-template.png){ width=1000px}

1. After clicking __Next__ , configure notifications.

    ![notification configuration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy06.png)

2. After the configuration is complete, click the __OK__ button to return to the Alert Policy list.

!!! tip

    The newly created alert policy is in the __Not Triggered__ state. Once the threshold conditions and duration specified in the rules are met, it will change to the __Triggered__ state.


!!! warning

    Deleted alert policies will be completely removed, so please proceed with caution.

## Import Alert Policies via YAML

1. Go to the alert policy list and click __Create from YAML__.

   - The selection of cluster and namespace is for the management permission of the alert policy.
   - In the YAML editor, please fill in __spec__ and its content; only one group can be imported.
   - The __alert rule name__ must comply with the specification: the name can only contain uppercase and lowercase letters, digits, underscores (_), and hyphens (-), must start with a letter, and can be up to 63 characters long.
   - The __severity__ field is required and must comply with the specification: critical, warning, info.
   - The __expr__ expression is required.

    ![create from yaml](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/create-from-yaml.png){ width=1000px}

2. After importing the YAML file, click __Preview__ to validate the format of the imported YAML and quickly confirm the imported alert rules.

    ![create from yaml](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/create-from-yaml01.png){ width=1000px}
