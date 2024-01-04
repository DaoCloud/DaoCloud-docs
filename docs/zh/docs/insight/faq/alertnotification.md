# 告警通知流程说明

在创建告警策略时，可观测性 Insight 支持为同策略下不同级别触发的告警配置不同的通知发送间隔，但由于在 Alertmanager 原生配置中存在 __group_interval__ 和 __repeat_interval__ 两个参数，会导致告警通知的实际发送间隔存在偏差。

## 参数配置

在 Alertmanager 配置如下：

```yaml
route:  
  group_by: ["rulename"]
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 1h
```

**参数说明：**

- __group_wait__ ：用于设置告警通知的等待时间。当 Alertmanager 接收到一组告警时，如果在 __group_wait__ 指定的时间内没有更多的告警，则 Alertmanager 将等待一段时间以便收集到更多相同标签和内容的告警，并将所有符合条件的告警添加到同一通知中。

- __group_interval__ ：用于设置一组告警在被合并成单一通知前等待的时间。如果在这个时间内没有收到更多的来自同一组的告警，则 Alertmanager 将发送一个包含所有已接收告警的通知。

- __repeat_interval__ ：用于设置告警通知的重复发送间隔。当 Alertmanager 发送告警通知到接收器后，如果在 __repeat_interval__ 参数指定的时间内持续收到相同标签和内容的告警，则 Alertmanager 将重复发送告警通知。

当同时设置了 __group_wait__ 、 __group_interval__ 和 __repeat_interval__ 参数时，Alertmanager 将按照以下方式处理同一 group 下的告警通知：

1. 当 Alertmanager 接收到符合条件的告警时，它将等待至少 __group_wait__ 参数中指定的时间以便收集更多相同标签和内容的告警，并将所有符合条件的告警添加到同一通知中。

2. 如果在 __group_wait__ 时间内没有接收到更多的告警，则在该时间之后，Alertmanager 会将所收到的所有此类警报发送到接收器。如果有其他符合条件的告警在此期间内到达，则 Alertmanager 将继续等待，直到收集到所有告警或超时。

3. 如果在 __group_interval__ 参数中指定的时间内接收到了更多的相同标签和内容的告警，则这些新告警也将被添加到先前的通知中并一起发送。如果在 __group_interval__ 时间结束后仍然有未发送的告警，Alertmanager 将会重新开始一个新的计时周期，并等待更多的告警，直到再次达到 __group_interval__ 时间或收到新的告警。

4. 如果在 __repeat_interval__ 参数中指定的时间内持续收到相同标签和内容的告警，则 Alertmanager 将重复发送之前已经发送过的警报通知。在重复发送警报通知时，Alertmanager 不再等待 __group_wait__ 或 __group_interval__ ，而是根据 __repeat_interval__ 指定的时间间隔进行重复通知。

5. 如果在 __repeat_interval__ 时间结束后仍有未发送的告警，则 Alertmanager 将重新开始一个新的计时周期，并继续等待相同标签和内容的新告警。这个过程将一直持续下去，直到没有新告警为止或 Alertmanager 被停止。

## 举例说明

在下述示例中，Alertmanager 将所有 CPU 使用率高于阈值的告警分配到一个名为“critical_alerts”的策略中。

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

在这种情况下：

- 当 Alertmanager 收到告警时，它将等待至少 30 秒以便收集更多相同标签和内容的告警，并将它们添加到同一通知中。
- 如果在 5 分钟内接收到了更多相同标签和内容的告警，则这些新告警也将被添加到先前的通知中并一起发送。如果在 15分钟后仍有未发送的告警，则 Alertmanager 将重新开始一个新的计时周期，并等待更多的告警，直到再次达到 5 分钟或收到新告警。
- 如果在 1 小时内持续收到相同标签和内容的告警，则 Alertmanager 将重复发送之前已经发送过的警报通知。

     ![安装](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/insight/images/alertnotifacation.png)
