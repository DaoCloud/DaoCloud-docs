---
hide:
  - toc
---

# 可观测性权限说明

可观测性模块使用以下角色：

- Admin / Kpanda Owner
- [Cluster Admin](../../kpanda/07UserGuide/Permissions/PermissionBrief.md#cluster-admin)
- [NS Admin](../../kpanda/07UserGuide/Permissions/PermissionBrief.md#ns-admin) / [NS Edit](../../kpanda/07UserGuide/Permissions/PermissionBrief.md#ns-edit)
- [NS View](../../kpanda/07UserGuide/Permissions/PermissionBrief.md#ns-view)

各角色所具备的权限如下：

<!--
有权限使用`&check;`，无权限使用`&cross;`
-->

| 菜单     | 操作                        | Admin / Kpanda Owner | Cluster Admin | NS Admin / NS Edit | NS View |
| -------- | --------------------------- | -------------------- | ------------- | ------------------ | ------- |
| 概览     | 查看概览                    | &check;              | &cross;       | &cross;            | &cross; |
| 仪表盘   | 查看仪表盘                  | &check;              | &cross;       | &cross;            | &cross; |
| 场景监控 | 查看集群监控                | &check;              | &check;       | &cross;            | &cross; |
|          | 查看节点监控                | &check;              | &check;       | &cross;            | &cross; |
|          | 查看容器监控                | &check;              | &check;       | &check;            | &check; |
|          | 查看服务监控                | &check;              | &check;       | &check;            | &check; |
|          | 查看拓扑                    | &check;              | &check;       | &check;            | &check; |
| 指标查询 | 查询节点指标 - 普通         | &check;              | &check;       | &cross;            | &cross; |
|          | 查询工作负载指标 - 普通     | &check;              | &check;       | &check;            | &check; |
|          | 查询指标 - 高级             | &check;              | &check;       | &check;            | &check; |
| 日志查询 | 查询集群事件日志            | &check;              | &check;       | &cross;            | &cross; |
|          | 查询节点日志                | &check;              | &check;       | &cross;            | &cross; |
|          | 查询容器日志                | &check;              | &check;       | &check;            | &check; |
| 链路查询 | 查询链路                    | &check;              | &check;       | &check;            | &check; |
| 告警列表 | 查看告警事件                | &check;              | &check;       | &check;            | &check; |
| 告警规则 | 创建指标模板规则 - 工作负载 | &check;              | &check;       | &check;            | &cross; |
|          | 创建指标模板规则 - 节点     | &check;              | &check;       | &cross;            | &cross; |
|          | 修改指标模板规则 - 工作负载 | &check;              | &check;       | &check;            | &cross; |
|          | 修改指标模板规则 - 节点     | &check;              | &check;       | &cross;            | &cross; |
|          | 查看指标模板规则 - 工作负载 | &check;              | &check;       | &check;            | &check; |
|          | 查看指标模板规则 - 节点     | &check;              | &check;       | &cross;            | &cross; |
|          | 创建 promQL 规则            | &check;              | &check;       | &check;            | &cross; |
|          | 修改 promQL 规则            | &check;              | &check;       | &check;            | &cross; |
|          | 删除自定义告警规则          | &check;              | &check;       | &check;            | &cross; |
|          | 查看内置告警规则            | &check;              | &cross;       | &cross;            | &cross; |
|          | 修改内置告警规则            | &check;              | &cross;       | &cross;            | &cross; |
| 通知对象 | 查看通知对象                | &check;              | &check;       | &check;            | &check; |
|          | 添加通知对象                | &check;              | &cross;       | &cross;            | &cross; |
|          | 修改通知对象                | &check;              | &cross;       | &cross;            | &cross; |
|          | 删除通知对象                | &check;              | &cross;       | &cross;            | &cross; |
|          | 查看消息模板                | &check;              | &check;       | &check;            | &check; |
|          | 添加消息模板                | &check;              | &cross;       | &cross;            | &cross; |
|          | 修改消息模板                | &check;              | &cross;       | &cross;            | &cross; |
|          | 删除消息模板                | &check;              | &cross;       | &cross;            | &cross; |
| 采集管理 | 查看 Agent 列表             | &check;              | &check;       | &check;            | &check; |
|          | 安装/卸载 Agent             | &check;              | &check;       | &check;            | &check; |
|          | 查看 Agent 详情             | &check;              | &check;       | &check;            | &check; |
| 系统配置 | 查看系统配置                | &check;              | &cross;       | &cross;            | &cross; |

有关权限的更多信息，请参阅[容器管理权限说明](../../kpanda/07UserGuide/Permissions/PermissionBrief.md)。

有关角色的创建、管理和删除，请参阅[角色和权限管理](../../ghippo/04UserGuide/01UserandAccess/Role.md)。
