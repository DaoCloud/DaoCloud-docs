# Alert Notification Process Description

When configuring an alert policy in Insight, you have the ability to set different notification sending intervals
for alerts triggered at different levels within the same policy. However, due to the presence of two parameters,
`group_interval` and `repeat_interval`, in the native Alertmanager configuration, the actual intervals for sending
alert notifications may deviate.

## Parameter Configuration

In the Alertmanager configuration, set the following parameters:

```yaml
route:  
  group_by: ["rulename"]
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 1h
```

**Parameter descriptions:**

- `group_wait`: Specifies the waiting time before sending alert notifications. When Alertmanager receives a group of alerts,
  if no further alerts are received within the duration specified by `group_wait`, Alertmanager waits for a certain amount
  of time to collect additional alerts with the same labels and content. It then includes all qualifying alerts in the same notification.

- `group_interval`: Determines the waiting time before merging a group of alerts into a single notification.
  If no more alerts from the same group are received during this period, Alertmanager sends a notification containing all received alerts.

- `repeat_interval`: Sets the interval for resending alert notifications. After Alertmanager sends an alert notification
  to a receiver, if it continues to receive alerts with the same labels and content within the duration specified by
  `repeat_interval`, Alertmanager will resend the alert notification.

When the `group_wait`, `group_interval`, and `repeat_interval` parameters are set simultaneously, Alertmanager
handles alert notifications under the same group as follows:

1. When Alertmanager receives qualifying alerts, it waits for at least the duration specified in the
   `group_wait` parameter to collect additional alerts with the same labels and content.
   It includes all qualifying alerts in the same notification.

2. If no further alerts are received during the `group_wait` duration, Alertmanager sends all received alerts
   to the receiver after that time. If additional qualifying alerts arrive during this period, Alertmanager
   continues to wait until all alerts are collected or a timeout occurs.

3. If more alerts with the same labels and content are received within the `group_interval` parameter,
   these new alerts are merged into the previous notification and sent together. If there are still
   unsent alerts after the `group_interval` duration, Alertmanager starts a new timing cycle and waits
   for more alerts until the `group_interval` duration is reached again or new alerts are received.

4. If Alertmanager keeps receiving alerts with the same labels and content within the duration specified
   by `repeat_interval`, it will resend the previously sent alert notifications. When resending alert notifications,
   Alertmanager does not wait for `group_wait` or `group_interval`, but sends notifications repeatedly according to
   the time interval specified by `repeat_interval`.

5. If there are still unsent alerts after the `repeat_interval` duration, Alertmanager starts a new timing cycle
   and continues to wait for new alerts with the same labels and content. This process continues until there are
   no new alerts or Alertmanager is stopped.

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

- When Alertmanager receives an alert, it waits for at least 30 seconds to collect additional alerts
  with the same labels and content, and includes them in the same notification.

- If more alerts with the same labels and content are received within 5 minutes, these new alerts
  are merged into the previous notification and sent together. If there are still unsent alerts
  after 15 minutes, Alertmanager starts a new timing cycle and waits for more alerts until 5 minutes
  have passed or new alerts are received.

- If Alertmanager continues to receive alerts with the same labels and content within 1 hour,
  it will resend the previously sent alert notifications.
