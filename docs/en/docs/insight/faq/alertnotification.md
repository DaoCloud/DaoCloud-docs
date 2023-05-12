# Alert Notification Process Description

When creating an alert policy, Observable Insight supports configuring different notification sending intervals for alerts triggered at different levels under the same policy. However, because there are two parameters, `group_interval` and `repeat_interval`, in the native configuration of Alertmanager, the actual sending interval of alert notifications may deviate.

## Parameter Configuration

In the Alertmanager configuration, set the following:

```yaml
route:  
  group_by: ["rulename"]
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 1h
```

**Parameter descriptions:**

- `group_wait`: Sets the waiting time for sending alert notifications. When Alertmanager receives a group of alerts, if no more alerts are received within the time specified by `group_wait`, Alertmanager will wait for a certain amount of time to collect more alerts with the same labels and content, and add all qualifying alerts to the same notification.

- `group_interval`: Sets the waiting time before a group of alerts are merged into a single notification. If no more alerts from the same group are received during this time, Alertmanager sends a notification containing all received alerts.

- `repeat_interval`: Sets the interval for resending alert notifications. After Alertmanager sends an alert notification to a receiver, if it continues to receive alerts with the same labels and content within the time specified by `repeat_interval`, Alertmanager will resend the alert notification.

When the `group_wait`, `group_interval`, and `repeat_interval` parameters are set simultaneously, Alertmanager handles the alert notifications under the same group as follows:

1. When Alertmanager receives qualifying alerts, it waits for at least the time specified in the `group_wait` parameter to collect more alerts with the same labels and content, and adds all qualifying alerts to the same notification.

2. If no more alerts are received during the `group_wait` time, Alertmanager sends all received alerts to the receiver after that time. If other qualifying alerts arrive during this period, Alertmanager continues to wait until all alerts are collected or until a timeout occurs.

3. If more alerts with the same labels and content are received within the `group_interval` parameter, these new alerts are also merged into the previous notification and sent together. If there are still unsent alerts after the `group_interval` time, Alertmanager starts a new timing cycle and waits for more alerts until the `group_interval` time is reached again or new alerts are received.

4. If Alertmanager keeps receiving alerts with the same labels and content within the time specified by `repeat_interval`, it will resend the alert notifications that have already been sent before. When resending alert notifications, Alertmanager does not wait for `group_wait` or `group_interval`, but sends notifications repeatedly according to the time interval specified by `repeat_interval`.

5. If there are still unsent alerts after the `repeat_interval` time, Alertmanager starts a new timing cycle and continues to wait for new alerts with the same labels and content. This process continues until there are no new alerts or Alertmanager is stopped.

## Example

In the following example, Alertmanager assigns all alerts with CPU usage above the threshold to a policy named "critical_alerts".

```yaml
groups:
- name: critical_alerts
  rules:
  - alert: HighCPUUsage
    expr: node_cpu_seconds_total{mode="idle"} < 50
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "High CPU usage detected on instance {{ $labels.instance }}"
  group_by: [rulename]
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 1h
```

In this case:

- When Alertmanager receives an alert, it waits for at least 30 seconds to collect more alerts with the same labels and content, and adds them to the same notification.

- If more alerts with the same labels and content are received within 5 minutes, these new alerts are merged into the previous notification and sent together. If there are still unsent alerts after 15 minutes, Alertmanager starts a new timing cycle and waits for more alerts until 5 minutes are reached again or new alerts are received.

- If Alertmanager keeps receiving alerts with the same labels and content within 1 hour, it will resend the alert notifications that have already been sent before.

