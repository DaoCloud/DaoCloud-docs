# 日志采集排障指南

在集群中[安装 insight-agent](../user-guide/quickstart/install-agent.md) 后，`insight-agent` 中的 `Fluent Bit` 会默认采集集群中的日志，包括 Kubernetes 事件日志、节点日志、容器日志等。
`Fluent Bit` 已配置好各种日志采集插件、相关的过滤器插件及日志输出插件。
这些插件的工作状态决定了日志采集是否正常。
下面是一个针对 `Fluent Bit` 的仪表盘，它用来监控各个集群中 `Fluent Bit` 的工作情况和插件的采集、处理、导出日志的情况。

1. 使用 DCE 5.0 平台，进入`可观测性`，选择左侧导航栏的 `仪表盘`。

    ![insight 入口](../images/insight01.png)

2. 点击仪表盘标题`概览`。

    ![概览](../images/insight02.png)

3. 切换到 `insight-system` -> `Fluent Bit` 仪表盘。

    ![fluentbit](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/insight03.png)

4. `Fluent Bit` 仪表盘上方有几个选项框，可以选择日志采集插件、日志过滤插件、日志输出插件及所在集群名。

    ![fluentbit](https://docs.daocloud.io/daocloud-docs-images/docs/insight/images/insight04.png)

## 插件说明

此处说明 `Fluent Bit` 的几个插件。

**日志采集插件**

| input plugin           | 插件介绍               | 采集目录                                                                |
| ---------------------- | ------------------ | ------------------------------------------------------------------- |
| tail.kube              | 采集容器日志             | /var/log/containers/*.log                                          |
| tail.kubeevent         | 采集 Kubernetes 事件日志   | /var/log/containers/*-kubernetes-event-exporter*.log              |
| tail.syslog.dmesg      | 采集主机 dmesg 日志     | /var/log/dmesg                                                      |
| tail.syslog.messages   | 采集主机常用日志           | /var/log/secure, /var/log/messages, /var/log/syslog,/var/log/auth.log |
| syslog.syslog.RSyslog  | 采集 RSyslog 日志      |                                                                     |
| systemd.syslog.systemd | 采集 Journald daemon 日志   |                                                                     |
| tail.audit_log.k8s    | 采集 Kubernetes 审计日志   | /var/log/*/audit/*.log                                            |
| tail.audit_log.ghippo | 采集全局管理审计日志 | /var/log/containers/*_ghippo-system_audit-log*.log              |
| tail.skoala-gw         | 采集微服务网关日志     | /var/log/containers/*_skoala-gw*.log                             |

**日志过滤插件**

| filter plugin      | 插件介绍 |
| ------------------------ | ---------------------------------- |
| Lua.audit_log.k8s | 使用 lua 过滤符合条件的 Kubernetes 审计日志 |

!!! note

    过滤器插件不止 Lua.audit_log.k8s，这里只介绍会丢弃日志的过滤器。

**日志输出插件**

| output plugin            | 插件介绍                               |
| ------------------------ | ---------------------------------- |
| es.kube.kubeevent.syslog | 把 Kubernetes 审计日志、事件日志，syslog 日志写入 [ElasticSearch 集群](../../middleware/elasticsearch/intro/what.md) |
| forward.audit_log | 把 Kubernetes 审计日志和[全局管理的审计日志](../../ghippo/user-guide/audit-log.md)发送到`全局管理`   |
| es.skoala | 把微服务网关的[请求日志](../../skoala/ms-gateway/logs/reqlog.md)和[实例日志](../../skoala/ms-gateway/logs/inslog.md)写入到 ElasticSearch 集群            |
