---
hide:
  - toc
---

# 服务网格权限说明

[服务网格](../../mspider/01Intro/WhatismSpider.md)支持几种用户角色：

- Super Admin
- Workspace Admin
- Workspace Editor
- Workspace Viewer

<!--
有权限使用`&check;`，无权限使用`&cross;`
-->

这些角色的具体权限如下表所示。

| 菜单对象         | 操作           | Super Admin | Workspace Admin | Workspace Editor | Workspace Viewer |
| ---------------- | -------------- | ----------- | --------------- | ---------------- | ---------------- |
| 服务网格列表     | 创建网格       | &check;           | &cross;               | &cross;                | &cross;                |
|                  | 编辑网格       | &check;           | &check;               | &check;                | &cross;                |
|                  | 删除网格       | &check;           | &check;               | &check;                | &cross;                |
|                  | 查看           | &check;           | &check;               | &check;                | &check;                |
| 网格概览         | 查看           | &check;           | &check;               | &check;                | &check;                |
| 服务列表         | 跳转至治理页面 | &check;           | &check;               | &check;                | &cross;                |
|                  | 查看           | &check;           | &check;               | &check;                | &check;                |
| 服务条目         | 创建           | &check;           | &check;               | &check;                | &cross;                |
|                  | 编辑           | &check;           | &check;               | &check;                | &cross;                |
|                  | 删除           | &check;           | &check;               | &check;                | &cross;                |
|                  | 查看           | &check;           | &check;               | &check;                | &check;                |
| 虚拟服务         | 创建           | &check;           | &check;               | &check;                | &cross;                |
|                  | 编辑           | &check;           | &check;               | &check;                | &cross;                |
|                  | 删除           | &check;           | &check;               | &check;                | &cross;                |
|                  | 查看           | &check;           | &check;               | &check;                | &check;                |
| 目标规则         | 创建           | &check;           | &check;               | &check;                | &cross;                |
|                  | 编辑           | &check;           | &check;               | &check;                | &cross;                |
|                  | 删除           | &check;           | &check;               | &check;                | &cross;                |
|                  | 查看           | &check;           | &check;               | &check;                | &check;                |
| 网关规则         | 创建           | &check;           | &check;               | &check;                | &cross;                |
|                  | 编辑           | &check;           | &check;               | &check;                | &cross;                |
|                  | 删除           | &check;           | &check;               | &check;                | &cross;                |
|                  | 查看           | &check;           | &check;               | &check;                | &check;                |
| 对等身份认证     | 创建           | &check;           | &check;               | &check;                | &cross;                |
|                  | 编辑           | &check;           | &check;               | &check;                | &cross;                |
|                  | 删除           | &check;           | &check;               | &check;                | &cross;                |
|                  | 查看           | &check;           | &check;               | &check;                | &check;                |
| 请求身份认证     | 创建           | &check;           | &check;               | &check;                | &cross;                |
|                  | 编辑           | &check;           | &check;               | &check;                | &cross;                |
|                  | 删除           | &check;           | &check;               | &check;                | &cross;                |
|                  | 查看           | &check;           | &check;               | &check;                | &check;                |
| 授权策略         | 创建           | &check;           | &check;               | &check;                | &cross;                |
|                  | 编辑           | &check;           | &check;               | &check;                | &cross;                |
|                  | 删除           | &check;           | &check;               | &check;                | &cross;                |
|                  | 查看           | &check;           | &check;               | &check;                | &check;                |
| 命名空间边车管理 | 启用注入       | &check;           | &check;               | &check;                | &cross;                |
|                  | 禁用注入       | &check;           | &check;               | &check;                | &cross;                |
|                  | 查看           | &check;           | &check;               | &check;                | &check;                |
| 工作负载边车管理 | 启用注入       | &check;           | &check;               | &check;                | &cross;                |
|                  | 禁用注入       | &check;           | &check;               | &check;                | &cross;                |
|                  | 边车资源设置   | &check;           | &check;               | &check;                | &cross;                |
|                  | 查看           | &check;           | &check;               | &check;                | &check;                |
| 全局边车注入     | 启用注入       | &check;           | &check;               | &check;                | &cross;                |
|                  | 禁用注入       | &check;           | &check;               | &check;                | &cross;                |
|                  | 边车资源设置   | &check;           | &check;               | &check;                | &cross;                |
|                  | 查看           | &check;           | &check;               | &check;                | &check;                |
| 集群纳管         | 集群接入       | &check;           | &check;               | &cross;                | &cross;                |
|                  | 集群移除       | &check;           | &check;               | &cross;                | &cross;                |
|                  | 查看           | &check;           | &check;               | &check;                | &check;                |
| 网格网关         | 创建           | &check;           | &check;               | &check;                | &cross;                |
|                  | 编辑           | &check;           | &check;               | &check;                | &cross;                |
|                  | 删除           | &check;           | &check;               | &check;                | &cross;                |
|                  | 查看           | &check;           | &check;               | &check;                | &check;                |
| Istio 资源管理   | 创建           | &check;           | &check;               | &check;                | &cross;                |
|                  | 编辑           | &check;           | &check;               | &check;                | &cross;                |
|                  | 删除           | &check;           | &check;               | &check;                | &cross;                |
|                  | 查看           | &check;           | &check;               | &check;                | &check;                |
| TLS 证书管理     | 创建           | &check;           | &check;               | &check;                | &cross;                |
|                  | 编辑           | &check;           | &check;               | &check;                | &cross;                |
|                  | 删除           | &check;           | &check;               | &check;                | &cross;                |
|                  | 查看           | &check;           | &check;               | &check;                | &check;                |
| 系统升级         | Istio 升级     | &check;           | &check;               | &cross;                | &cross;                |
|                  | 边车升级       | &check;           | &check;               | &check;                | &cross;                |
|                  | 查看           | &check;           | &check;               | &check;                | &check;                |
| 工作空间管理     | 绑定           | &check;           | &cross;               | &cross;                | &cross;                |
|                  | 解绑           | &check;           | &cross;               | &cross;                | &cross;                |
|                  | 查看           | &check;           | &cross;               | &cross;                | &cross;                |

!!! note

    有关角色和权限管理的完整介绍，请参考[角色和权限管理](../04UserGuide/01UserandAccess/Role.md)。
