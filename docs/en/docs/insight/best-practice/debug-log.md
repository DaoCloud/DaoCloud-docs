---
MTPE: windsonsea
date: 2024-06-11
---

# Log Collection Troubleshooting Guide

After installing the __insight-agent__ in the cluster, __Fluent Bit__ in __insight-agent__ will collect logs in the cluster by default, including Kubernetes event logs, node logs, and container logs. __Fluent Bit__ has already configured various log collection plugins, related filter plugins, and log output plugins. The working status of these plugins determines whether log collection is normal. Below is a dashboard for __Fluent Bit__ that monitors the working conditions of each __Fluent Bit__ in the cluster and the collection, processing, and export of plugin logs.

1. Use DCE 5.0 platform, enter __Insight__ , and select the __Dashboard__ in the left navigation bar.

    ![nav](./images/insight01.png)

2. Click the dashboard title __Overview__ .

    ![dashboard](./images/insight02.png)

3. Switch to the __insight-system__ -> __Fluent Bit__ dashboard.

    ![fluent](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/insight03.png)

4. There are several check boxes above the __Fluent Bit__ dashboard to select the input plugin, filter plugin, output plugin, and cluster in which it is located.

    ![fluent](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/insight/images/insight04.png)

## Plugin Description

Here are some plugins for __Fluent Bit__ .

**Log Collection Plugin**

| Input Plugin | Plugin Description | Collection Directory |
| ------------ | ------------------ | -------------------- |
| tail.kube | Collect container logs | /var/log/containers/*.log |
| tail.kubeevent | Collect Kubernetes event logs | /var/log/containers/*-kubernetes-event-exporter*.log |
| tail.syslog.dmesg | Collect host dmesg logs | /var/log/dmesg |
| tail.syslog.messages | Collect frequently used host logs | /var/log/secure, /var/log/messages, /var/log/syslog,/var/log/auth.log |
| syslog.syslog.RSyslog | Collect RSyslog logs | |
| systemd.syslog.systemd | Collect Journald daemon logs | |
| tail.audit_log.k8s | Collect Kubernetes audit logs | /var/log/*/audit/*.log |
| tail.audit_log.ghippo | Collect global management audit logs | /var/log/containers/*_ghippo-system_audit-log*.log |
| tail.skoala-gw | Collect microservice gateway logs | /var/log/containers/*_skoala-gw*.log |

**Log Filter Plugin**

| Filter Plugin | Plugin Description |
| ------------- | ------------------ |
| Lua.audit_log.k8s | Use lua to filter Kubernetes audit logs that meet certain conditions |

!!! note

    There are more filter plugins than Lua.audit_log.k8s, which only introduces filters that will discard logs.

**Log Output Plugin**

| Output Plugin | Plugin Description |
| ------------- | ------------------ |
| es.kube.kubeevent.syslog | Write Kubernetes audit logs, event logs, and syslog logs to [ElasticSearch cluster](../../middleware/elasticsearch/intro/index.md) |
| forward.audit_log | Send Kubernetes audit logs and [global management audit logs](../../ghippo/user-guide/audit/audit-log.md) to __Global Management__ |
| es.skoala | Write [request logs](../../skoala/gateway/logs/reqlog.md) and [instance logs](../../skoala/gateway/logs/inslog.md) of microservice gateway to ElasticSearch cluster  |
