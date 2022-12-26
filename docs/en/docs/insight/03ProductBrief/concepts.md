---
hide:
  - toc
---

# Basic concept

This section introduces the basic concepts related to observability (Insight).

| # | Terms | English | Definitions |
| :--- | :--------- | ----------------- | :------------- ------------------------------------------------ |
| 1 | Monitoring target | Target | The monitored object; the system will regularly initiate capture tasks to the monitoring point to obtain indicators |
| 2 | Metrics | Metric | Use the [open-metric](https://openmetrics.io/) format description to measure the degree of a certain attribute in a software or hardware system |
| 3 | Custom Indicators | Recording Rule | A named PromQL expression, which is a new indicator obtained by calculating multiple indicators to describe a more complete and complex system state |
| 4 | Dashboard | Dashboard | Dashboard is a form of visual management, that is, the performance of data, intelligence and other conditions at a glance. It displays information through various visual perceptions with intuitive images and appropriate colors. Display the real-time situation of the platform and all performance indicators in DCE through visual graphics. |
| 6 | Service Discovery | Service Discovery | A service discovery configuration for Kubernetes environment, used to batch and automatically access monitoring points on Kubernetes |
| 7 | Exporter | Exporter | A service that can provide indicators, often understood as a monitoring object |
| 8 | Alert Rules | Rule | A PromQL expression whose return value is a Boolean value, which describes whether the indicator or custom indicator is within the threshold range, and if not, an alarm event will be generated |
| 9 | Alarm message | Event | The record information when the alarm rule is triggered, which records the alarm rule, trigger time, and current system status; at the same time, it will trigger the corresponding action, such as sending an email |
| 10 | Notification | Notification | The alarm event information sent by the system to the user through e-mail or other channels |
| 11 | PromQL | PromQL | Query statements supported by the Prometheus system |