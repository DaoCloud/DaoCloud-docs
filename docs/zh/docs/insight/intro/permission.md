---
hide:
  - toc
---

# 可观测性权限说明

可观测性模块使用以下角色：

- Admin / Kpanda Owner
- [Cluster Admin](../../kpanda/user-guide/permissions/permission-brief.md#cluster-admin)
- [NS Admin](../../kpanda/user-guide/permissions/permission-brief.md#ns-admin) / [NS Edit](../../kpanda/user-guide/permissions/permission-brief.md#ns-edit)
- [NS View](../../kpanda/user-guide/permissions/permission-brief.md#ns-view)

各角色所具备的权限如下：

<!--
有权限使用 __&check;__ ，无权限使用 __&cross;__ 
-->

| 菜单     | 操作                        | Admin / Kpanda Owner | Cluster Admin | NS Admin / NS Edit | NS View |
| -------- | --------------------------- | -------------------- | ------------- | ------------------ | ------- |
| 概览     | 查看概览                    | &check;              | &cross;       | &cross;            | &cross; |
| 仪表盘   | 查看仪表盘                  | &check;              | &cross;       | &cross;            | &cross; |
| 基础设施 | 查看集群监控                | &check;              | &check;       | &cross;            | &cross; |
|          | 查看节点监控                | &check;              | &check;       | &cross;            | &cross; |
|          | 查看命名空间监控          | &check;              | &check;       | &check;           | &check;  |
|          | 查看工作负载监控           | &check;              | &check;       | &check;            | &check; |
|          | 查看事件              | &check;              | &check;       | &check;            | &check; |
|          | 查看拨测任务            | &check;              | &check;       | &check;            | &check; |
|          | 创建拨测任务            | &check;              | &check;       | &check;            | &cross;  |
|          | 编辑拨测任务            | &check;              | &check;       | &check;            | &cross;  |
|          | 删除拨测任务            | &check;              | &check;       | &check;            | &cross; |
| 指标     | 查询节点指标         | &check;              | &check;       | &cross;            | &cross; |
|          | 查询工作负载指标     | &check;              | &check;       | &check;            | &check; |
|          | 高级查询            | &check;              | &check;       | &check;            | &check; |
| 日志     | 查询节点日志                | &check;              | &check;       | &cross;            | &cross; |
|          | 查询容器日志                | &check;              | &check;       | &check;            | &check; |
|          | Lucene 语法查询节点日志     | &check;              | &check;       | &cross;            | &cross; |
|          | Lucene 语法查询容器日志     | &check;              | &check;       | &check;            | &check; |
| 链路追踪 | 查看服务拓扑                   | &check;              | &check;       | &check;            | &check; |
|        | 查看服务列表                   | &check;              | &check;       | &check;            | &check; |
|        | 查询调用链                | &check;              | &check;       | &check;            | &check; |
|        | TraceID 查询链路          | &check;              | &check;       | &check;            | &check; |
| 告警列表 | 查看告警事件                | &check;              | &check;       | &check;            | &check; |
| 告警规则 | 创建指标模板规则 - 工作负载 | &check;              | &check;       | &check;            | &cross; |
|          | 创建指标模板规则 - 节点     | &check;              | &check;       | &cross;            | &cross; |
|          | 修改指标模板规则 - 工作负载 | &check;              | &check;       | &check;            | &cross; |
|          | 修改指标模板规则 - 节点     | &check;              | &check;       | &cross;            | &cross; |
|          | 查看指标模板规则 - 工作负载 | &check;              | &check;       | &check;            | &check; |
|          | 查看指标模板规则 - 节点     | &check;              | &check;       | &cross;            | &cross; |
|          | 创建 promQL 规则            | &check;              | &check;       | &check;            | &cross; |
|          | 修改 promQL 规则            | &check;              | &check;       | &check;            | &cross; |
|          | 创建日志规则            | &check;              | &check;       | &check;            | &cross; |
|          | 创建时间规则            | &check;              | &check;       | &check;            | &cross; |
|          | 删除自定义告警规则          | &check;              | &check;       | &check;            | &cross; |
|          | 查看内置告警规则            | &check;              | &cross;       | &cross;            | &cross; |
|          | 修改内置告警规则            | &check;              | &cross;       | &cross;            | &cross; |
|          | YAML 导入告警规则            | &check;              | &check;       | &check;            | &cross; |
| 通知对象 | 查看通知对象                | &check;              | &check;       | &check;            | &check; |
|          | 添加通知对象                | &check;              | &cross;       | &cross;            | &cross; |
|          | 修改通知对象                | &check;              | &cross;       | &cross;            | &cross; |
|          | 删除通知对象                | &check;              | &cross;       | &cross;            | &cross; |
|          | 查看消息模板                | &check;              | &check;       | &check;            | &check; |
|          | 添加消息模板                | &check;              | &cross;       | &cross;            | &cross; |
|          | 修改消息模板                | &check;              | &cross;       | &cross;            | &cross; |
|          | 删除消息模板                | &check;              | &cross;       | &cross;            | &cross; |
| 告警静默  | 查看静默规则列表              | &check;              | &check;      | &check;          | &check; |
|          | 创建静默规则              | &check;              | &check;      | &check;           | &cross; |
|          | 编辑静默规则              | &check;              | &check;      | &check;           | &cross; |
|          | 删除静默规则              | &check;              | &check;      | &check;           | &cross; |
| 采集管理 | 查看 Agent 列表             | &check;              | &check;       | &check;            | &check; |
|          | 安装/卸载 Agent             | &check;              | &check;       | &check;            | &check; |
|          | 查看 Agent 详情             | &check;              | &check;       | &check;            | &check; |
| 系统配置 | 查看系统配置                | &check;              | &cross;       | &cross;            | &cross; |
|         | 修改系统配置                | &check;              | &cross;       | &cross;            | &cross; |

有关权限的更多信息，请参阅[容器管理权限说明](../../kpanda/user-guide/permissions/permission-brief.md)。

有关角色的创建、管理和删除，请参阅[角色和权限管理](../../ghippo/user-guide/access-control/role.md)。
