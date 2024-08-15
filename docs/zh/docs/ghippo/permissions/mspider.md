---
hide:
  - toc
---

# 服务网格权限说明

[服务网格](../../mspider/intro/index.md)支持以下几种用户角色：

- Admin
- Workspace Admin
- Workspace Editor
- Workspace Viewer

!!! info

    自 DCE 5.0 的 [v0.6.0](../../download/index.md) 起，全局管理模块支持为服务网格配置自定义角色，
    即除了使用系统默认角色外，还可以在服务网格中自定义角色并授予不同权限。

<!--
有权限使用 `&check;`，无权限使用 `&cross;`
-->

这些角色的具体权限如下表所示。

| 菜单对象 | 操作 | Admin | Workspace Admin | Workspace Editor | Workspace Viewer |
| ------- | --- | ----- | --------------- | ---------------- | ---------------- |
| 服务网格列表 | [创建网格](../../mspider/user-guide/service-mesh/README.md) | &check; | &cross; | &cross; | &cross; |
| | 更新网格 | &check; | &check; | &cross; | &cross; |
| | [删除网格](../../mspider/user-guide/service-mesh/delete.md) | &check; | &cross; | &cross; | &cross; |
| | [查看网格列表](../../mspider/user-guide/service-mesh/README.md) | &check; | &check; | &check; | &check; |
| 网格概览 | 查看 | &check; | &check; | &check; | &check; |
| 服务列表 | 查看 | &check; | &check; | &check; | &check; |
| 服务列表 | 创建 VM 服务 | &check; | &check; | &check; | &cross; |
| 服务列表 | 删除 VM 服务 | &check; | &check; | &check; | &cross; |
| 服务条目 | 创建 | &check; | &check; | &check; | &cross; |
| | 编辑 | &check; | &check; | &check; | &cross; |
| | 删除 | &check; | &check; | &check; | &cross; |
| | 查看 | &check; | &check; | &check; | &check; |
| 虚拟服务 | 创建 | &check; | &check; | &check; | &cross; |
| | 编辑 | &check; | &check; | &check; | &cross; |
| | 删除 | &check; | &check; | &check; | &cross; |
| | 查看 | &check; | &check; | &check; | &check; |
| 目标规则 | 创建 | &check; | &check; | &check; | &cross; |
| | 编辑 | &check; | &check; | &check; | &cross; |
| | 删除 | &check; | &check; | &check; | &cross; |
| | 查看 | &check; | &check; | &check; | &check; |
| 网关规则 | 创建 | &check; | &check; | &check; | &cross; |
| | 编辑 | &check; | &check; | &check; | &cross; |
| | 删除 | &check; | &check; | &check; | &cross; |
| | 查看 | &check; | &check; | &check; | &check; |
| 对等身份认证 | 创建 | &check; | &check; | &check; | &cross; |
| | 编辑 | &check; | &check; | &check; | &cross; |
| | 删除 | &check; | &check; | &check; | &cross; |
| | 查看 | &check; | &check; | &check; | &check; |
| 请求身份认证 | 创建 | &check; | &check; | &check; | &cross; |
| | 编辑 | &check; | &check; | &check; | &cross; |
| | 删除 | &check; | &check; | &check; | &cross; |
| | 查看 | &check; | &check; | &check; | &check; |
| 授权策略 | 创建 | &check; | &check; | &check; | &cross; |
| | 编辑 | &check; | &check; | &check; | &cross; |
| | 删除 | &check; | &check; | &check; | &cross; |
| | 查看 | &check; | &check; | &check; | &check; |
| 命名空间边车管理 | 启用注入 | &check; | &check; | &check; | &cross; |
| | 禁用注入 | &check; | &check; | &check; | &cross; |
| | 查看 | &check; | &check; | &check; | &check; |
| | 边车服务发现范围 | &check; | &check; | &check; | &cross; |
| 工作负载边车管理 | 启用注入 | &check; | &check; | &check; | &cross; |
| | 禁用注入 | &check; | &check; | &check; | &cross; |
| | 边车资源设置 | &check; | &check; | &check; | &cross; |
| | 查看 | &check; | &check; | &check; | &check; |
| 全局边车注入 | 启用注入 | &check; | &check; | &cross; | &cross; |
| | 禁用注入 | &check; | &check; | &cross; | &cross; |
| | 边车资源设置 | &check; | &check; | &cross; | &cross; |
| | 查看 | &check; | &check; | &check; | &check; |
| 集群纳管 (仅托管网格) | 集群接入 | &check; | &check; | &cross; | &cross; |
| | 集群移除 | &check; | &check; | &cross; | &cross; |
| | 查看 | &check; | &check; | &check; | &check; |
| 网格网关 | 创建 | &check; | &check; | &cross; | &cross; |
| | 编辑 | &check; | &check; | &check; | &cross; |
| | 删除 | &check; | &check; | &cross; | &cross; |
| | 查看 | &check; | &check; | &check; | &check; |
| Istio 资源管理 | 创建 | &check; | &check; | &cross; | &cross; |
| | 编辑 | &check; | &check; | &check; | &cross; |
| | 删除 | &check; | &check; | &cross; | &cross; |
| | 查看 | &check; | &check; | &check; | &check; |
| TLS 证书管理 | 创建 | &check; | &check; | &check; | &cross; |
| | 编辑 | &check; | &check; | &check; | &cross; |
| | 删除 | &check; | &check; | &check; | &cross; |
| | 查看 | &check; | &check; | &check; | &check; |
| 多云网络互联 (托管、专用网格) | 启用 | &check; | &check; | &cross; | &cross; |
| | 查看 | &check; | &check; | &cross; | &cross; |
| | 编辑 | &check; | &check; | &cross; | &cross; |
| | 删除 | &check; | &check; | &cross; | &cross; |
| | 关闭 | &check; | &check; | &cross; | &cross; |
| 系统升级 | Istio 升级 | &check; | &check; | &cross; | &cross; |
| | 边车升级 | &check; | &check; | &cross; | &cross; |
| | 查看 | &check; | &check; | &check; | &check; |
| 工作空间管理 | 绑定 | &check; | &cross; | &cross; | &cross; |
| | 解绑 | &check; | &cross; | &cross; | &cross; |
| | 查看 | &check; | &cross; | &cross; | &cross; |
