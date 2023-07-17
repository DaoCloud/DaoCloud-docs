# Alert Policies

In addition to the built-in alert policies, DCE 5.0 allows users to create custom alert policies. Each alert policy is a collection of alert rules that can be set for clusters, nodes, and workloads. When an alert object reaches the threshold set by any of the rules in the policy, an alert is automatically triggered and a notification is sent.

Taking the built-in alerts as an example, click on the first alert policy `alertmanager.rules`.

![alert policy](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy01.png)

You can see that some alert rules have been set under it. You can add more rules under this policy, or edit or delete them at any time. You can also view the historical and active alerts related to this alert policy and edit the notification configuration.

![alertmanager.rules](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy02.png)

## Creating Alert Policies

1. Select `Alert Center` -> `Alert Policies`, and click the `Create Alert Policy` button.

    ![alert policy](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy01.png)

2. Fill in the basic information, select one or more clusters, nodes, or workloads as the alert objects, and click `Next`.

    ![basic information](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy03.png)

3. The list must have at least one rule. If the list is empty, please `Add Rule`.

    ![add rule](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy04.png)

    Create an alert rule in the pop-up window, fill in the parameters, and click `OK`.

    ![create rule](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy05.png)

    - Template rules: Pre-defined basic metrics that can monitor CPU, memory, disk, network, etc.
    - PromQL rules: Input a PromQL expression, please [query Prometheus expressions](https://prometheus.io/docs/prometheus/latest/querying/basics/).
    - Duration: After the alert is triggered and the duration reaches the set value, the alert policy will become a triggered state.
    - Alert level: Including emergency, warning, and information levels.
    - Advanced settings: Custom tags and annotations.

4. After clicking `Next`, configure notifications.

    ![notification configuration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy06.png)

5. After the configuration is complete, click the `OK` button to return to the Alert Policy list.

!!! tip

    The newly created alert policy is in the `Not Triggered` state. Once the threshold conditions and duration specified in the rules are met, it will change to the `Triggered` state.

## Other Operations

Click `⋮` on the right side of the list, select `Delete` in the pop-up menu to delete the alert policy. Click the policy name to enter the policy details, where you can add, edit, or delete the alert rules under it.

![alert rule](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert-policy07.png)

!!! warning

    The deleted alert policy will disappear completely, so please use caution.
