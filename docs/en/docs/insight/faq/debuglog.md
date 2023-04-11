# Log Collection Troubleshooting Guide

After [installing insight-agent](../user-guide/01quickstart/installagent.md) in the cluster, `Fluent Bit` in `insight-agent` will collect the logs in the cluster by default, including Kubernetes event logs, node logs, container logs etc.
`Fluent Bit` has been configured with various log collection plug-ins, related filter plug-ins and log output plug-ins.
The working status of these plug-ins determines whether the log collection is normal.
The following is a dashboard for `Fluent Bit`, which is used to monitor the working status of `Fluent Bit` in each cluster and the collection, processing, and export of logs by plug-ins.

1. Use the DCE 5.0 platform, enter `Observability`, and select `Dashboard` in the left navigation bar.

    

2. Click on the dashboard title `Overview`.

    

3. Switch to `insight-system` -> `Fluent Bit` dashboard.

    

4. There are several option boxes above the `Fluent Bit` dashboard, where you can choose the log collection plug-in, log filtering plug-in, log output plug-in and the name of the cluster.

    

## Plugin description

Several plugins for `Fluent Bit` are described here.

**Log collection plugin**

| input plugin | Plugin introduction | Collection directory |
| ---------------------- | ------------------ | ------- -------------------------------------------------- ---------- |
| tail.kube | Collect container logs | /var/log/containers/*.log |
| tail.kubeevent | Collect Kubernetes event logs | /var/log/containers/*-kubernetes-event-exporter*.log |
| tail.syslog.dmesg | Collect host dmesg logs | /var/log/dmesg |
| tail.syslog.messages | Collection of common logs of the host | /var/log/secure, /var/log/messages, /var/log/syslog, /var/log/auth.log |
| syslog.syslog.RSyslog | Collect RSyslog logs | |
| systemd.syslog.systemd | Collect Journald daemon logs | |
| tail.audit_log.k8s | Collect Kubernetes audit logs | /var/log/*/audit/*.log |
| tail.audit_log.ghippo | Collect global management audit logs | /var/log/containers/*_ghippo-system_audit-log*.log |
| tail.skoala-gw | Collect microservice gateway logs | /var/log/containers/*_skoala-gw*.log |

**Log filter plugin**

| filter plugin | Plugin introduction |
| ------------------------ | ------------------------ ---------- |
| Lua.audit_log.k8s | Use lua to filter qualified Kubernetes audit logs |

!!! note

    The filter plug-in is not limited to Lua.audit_log.k8s, only filters that discard logs are introduced here.

**log output plugin**

| output plugin | Plugin introduction |
| ------------------------ | ------------------------ ---------- |
| es.kube.kubeevent.syslog | Write Kubernetes audit log, event log, syslog log to [ElasticSearch cluster](../../middleware/elasticsearch/intro/what.md) |
| forward.audit_log | Forward the Kubernetes audit log and [Audit Log for Global Admin](../../ghippo/04UserGuide/03AuditLog.md) to `Global Admin` |
| es.skoala | [Request log](../../skoala/ms-gateway/logs/reqlog.md) and [Instance log](../../skoala/ms-gateway /logs/inslog.md) is written to the ElasticSearch cluster |