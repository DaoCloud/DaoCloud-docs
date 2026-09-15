# Configure Alertmanager to Send Alert Notifications Individually

In certain customer scenarios, you may want Insight to send alert notifications to WeCom, DingTalk, Feishu, email, or an external webhook one by one, instead of sending them in the default aggregated (grouped) form.

This document guides you through modifying the Alertmanager configuration deployed by Insight to achieve this.

## Background: the Default Grouping Behavior of Alertmanager

By default, the Alertmanager integrated with the Insight platform __groups__ alerts that share similar labels (such as `alertname`, the alert rule name, and `group_id`, the alert policy ID) into a single notification.

This mechanism is designed to effectively reduce alert storms and avoid sending a large number of duplicate or related notifications within a short period of time.

## Solution: Disable Grouping

To send notifications individually, you need to modify the Alertmanager route (`route`) configuration so that it does not group by any specific label.

Specifically, set the `route.group_by` parameter to the special value `['...']`.

This special value `...` instructs Alertmanager to group by __all__ labels (including internal labels). Because the combination of labels for each alert is usually unique, this effectively makes every alert its own group, thus achieving the "send individually" effect.

> **Important:**
> After grouping is disabled, alert messages are sent much more frequently. This will __significantly increase__ the request volume and load on the target webhook endpoints (such as Insight Server, WeCom, and DingTalk). Before applying this configuration, be sure to evaluate the receiving and processing capacity of downstream systems.

Two methods are provided to adjust the configuration. It is strongly recommended to use the [Helm method](#method-1-adjust-through-helm-recommended) so that the configuration can be tracked and managed.

### Method 1: Adjust Through Helm (Recommended)

You can apply the configuration by modifying the `values.yaml` file or by using `helm upgrade` command parameters.

#### Option A: Modify the `values.yaml` File

Edit your `values.yaml` file and modify the `vm_alertmanager.config.route` section:

```diff
vm_alertmanager:
  config:
    global:
      resolve_timeout: 5m
      slack_api_url: "http://slack:30500/"
    templates:
      - "/etc/vm/configs/**/*.tmpl"
    route:
      group_by:
+       - "..."
-       - "alertname"
-       - "group_id"
      group_wait: 30s
      group_interval: 5m
      repeat_interval: 1h
      receiver: "insight"
    receivers:
      baseURI: "/apis/insight.io/v1alpha1/alert/hook"

```

After the modification, run `helm upgrade` for the configuration to take effect.

#### Option B: Use `helm upgrade` Command Line Parameters

If you do not want to modify the `values.yaml` file, you can specify the parameter directly with `--set` when running the `helm upgrade` command:

```bash
helm upgrade insight \
 # ... other parameters omitted ...
 --set vm_alertmanager.config.route.group_by={"..."}
```

### Method 2: Edit the Kubernetes Secret Manually (Not Recommended)

__Warning:__ This method bypasses Helm's configuration management and may cause the configuration to be overwritten during a subsequent Helm upgrade. Use it only in emergency or test scenarios.

1.  __Edit the Secret:__
    Locate the Alertmanager configuration deployed by Insight, which is usually named `insight-vmalertmanager-config` (confirm the actual name in your environment).

2.  __Modify `alertmanager.yaml`:__
    In the opened editor, locate the `alertmanager.yaml` key and modify the `route.group_by` value under its `data` field:

    ```diff
    global:
      resolve_timeout: 5m
    templates:
      - "/etc/vm/configs/**/*.tmpl"
    route:
      group_by:
    +   - "..."
    -   - "alertname"
    -   - "group_id"
      group_wait: 30s
      group_interval: 5m
      repeat_interval: 1h
      receiver: insight
    receivers:
      - name: insight
        webhook_configs:
          - url: http://insight-server.insight-system.svc.cluster.local:80/apis/insight.io/v1alpha1/alert/hook
    ```

    After you save and exit the editor, the configuration is automatically updated in the Alertmanager Pod.

## Verify the Configuration

After the configuration takes effect, you can access the Alertmanager Web UI. On the "Status" page, you will see that the original grouping rules (such as `alertname` and `group_id`) are gone, which indicates that alerts are grouped by their unique label combination.

![vmalertmanager-status](../images/vmalertmanager-status.png)
