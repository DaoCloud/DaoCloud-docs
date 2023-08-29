# Alert Center

The Alert Center is an important feature provided by DCE 5.0 that allows users
to easily view all active and historical alerts by cluster and namespace through
a graphical interface, and search alerts based on severity level (critical, warning, info).

![alert list](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/alert01.png)

All alerts are triggered based on the threshold conditions set in the preset alert rules.
In DCE 5.0, some global alert policies are built-in, but users can also create or delete
alert policies at any time, and set thresholds for the following metrics:

- CPU usage
- Memory usage
- Disk usage
- Disk reads per second
- Disk writes per second
- Cluster disk read throughput
- Cluster disk write throughput
- Network send rate
- Network receive rate

Users can also add labels and annotations to alert rules. Alert rules can be classified as
active or expired, and certain rules can be enabled/disabled to achieve silent alerts.

When the threshold condition is met, users can configure how they want to be notified,
including email, DingTalk, WeCom, webhook, and SMS notifications. All notification
message templates can be customized and all messages are sent at specified intervals.

In addition, the Alert Center also supports sending alert messages to designated users
through short message services provided by Alibaba Cloud, Tencent Cloud, and more platforms
that will be added soon, enabling multiple ways of alert notification.

DCE 5.0 Alert Center is a powerful alert management platform that helps users
quickly detect and resolve problems in the cluster, improve business stability and availability,
and facilitate cluster inspection and troubleshooting.
