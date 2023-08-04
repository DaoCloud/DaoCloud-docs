# 微服务引擎权限说明

[微服务引擎](../../skoala/intro/index.md)包括微服务治理中心和微服务网关两部分。微服务引擎支持三种用户角色：

- Workspace Admin
- Workspace Editor
- Workspace Viewer

每种角色具有不同的权限，具体说明如下。

<!--
有权限使用`&check;`，无权限使用`&cross;`
-->

## 微服务治理中心权限说明

| 菜单对象              | 操作         | Workspace Admin | Workspace Editor | Workspace Viewer |
| --------------------- | ------------ | --------------- | ---------------- | ---------------- |
| 托管注册中心列表      | 查看列表     | &check;         | &check;          | &check;          |
| 托管注册中心          | 查看基础信息 | &check;         | &check;          | &check;          |
|                       | 创建         | &check;         | &check;          | &cross;          |
|                       | 重启         | &check;         | &check;          | &cross;          |
|                       | 编辑         | &check;         | &check;          | &cross;          |
|                       | 删除         | &check;         | &cross;          | &cross;          |
|                       | 上/下线      | &check;         | &check;          | &cross;          |
| 微服务命名空间        | 查看         | &check;         | &check;          | &check;          |
|                       | 创建         | &check;         | &check;          | &cross;          |
|                       | 编辑         | &check;         | &check;          | &cross;          |
|                       | 删除         | &check;         | &check;          | &cross;          |
| 微服务列表            | 查看         | &check;         | &check;          | &check;          |
|                       | 筛选命名空间 | &check;         | &check;          | &check;          |
|                       | 创建         | &check;         | &check;          | &cross;          |
|                       | 治理         | &check;         | &check;          | &cross;          |
|                       | 删除         | &check;         | &check;          | &cross;          |
| 服务治理规则-Sentinel | 查看         | &check;         | &check;          | &check;          |
|                       | 创建         | &check;         | &check;          | &cross;          |
|                       | 编辑         | &check;         | &check;          | &cross;          |
|                       | 删除         | &check;         | &check;          | &cross;          |
| 服务治理规则-Mesh     | 治理         | &check;         | &check;          | &cross;          |
| 实例列表              | 查看         | &check;         | &check;          | &check;          |
|                       | 上/下线      | &check;         | &check;          | &cross;          |
|                       | 编辑         | &check;         | &check;          | &cross;          |
| 服务治理策略-Sentinel | 查看         | &check;         | &check;          | &check;          |
|                       | 创建         | &check;         | &check;          | &cross;          |
|                       | 编辑         | &check;         | &check;          | &cross;          |
|                       | 删除         | &check;         | &check;          | &cross;          |
| 服务治理策略-Mesh     | 查看         | &check;         | &check;          | &check;          |
|                       | 创建         | &check;         | &check;          | &cross;          |
|                       | YAML 创建    | &check;         | &check;          | &cross;          |
|                       | 编辑         | &check;         | &check;          | &cross;          |
|                       | YAML 编辑    | &check;         | &check;          | &cross;          |
|                       | 删除         | &check;         | &check;          | &cross;          |
| 微服务配置列表        | 查看         | &check;         | &check;          | &check;          |
|                       | 筛选命名空间 | &check;         | &check;          | &check;          |
|                       | 批量删除     | &check;         | &check;          | &cross;          |
|                       | 导出/导入    | &check;         | &check;          | &cross;          |
|                       | 创建         | &check;         | &check;          | &cross;          |
|                       | 克隆         | &check;         | &check;          | &cross;          |
|                       | 编辑         | &check;         | &check;          | &cross;          |
|                       | 历史查询     | &check;         | &check;          | &check;          |
|                       | 回滚         | &check;         | &check;          | &cross;          |
|                       | 监听查询     | &check;         | &check;          | &check;          |
| 业务监控              | 查看         | &check;         | &check;          | &check;          |
| 资源监控              | 查看         | &check;         | &check;          | &check;          |
| 请求日志              | 查看         | &check;         | &check;          | &check;          |
| 实例日志              | 查看         | &check;         | &check;          | &check;          |
| 插件中心              | 查看         | &check;         | &check;          | &check;          |
|                       | 开启         | &check;         | &check;          | &cross;          |
|                       | 关闭         | &check;         | &check;          | &cross;          |
|                       | 编辑         | &check;         | &check;          | &cross;          |
|                       | 查看详情     | &check;         | &check;          | &check;          |
| 接入注册中心列表      | 查看         | &check;         | &check;          | &check;          |
|                       | 接入         | &check;         | &check;          | &cross;          |
|                       | 编辑         | &check;         | &check;          | &cross;          |
|                       | 移除         | &check;         | &cross;          | &cross;          |
| 微服务                | 查看列表     | &check;         | &check;          | &check;          |
|                       | 查看详情     | &check;         | &check;          | &check;          |
|                       | 治理         | &check;         | &check;          | &cross;          |
| 服务治理策略-Mesh     | 查看         | &check;         | &check;          | &check;          |
|                       | 创建         | &check;         | &check;          | &cross;          |
|                       | YAML 创建    | &check;         | &check;          | &cross;          |
|                       | 编辑         | &check;         | &check;          | &cross;          |
|                       | YAML 编辑    | &check;         | &check;          | &cross;          |
|                       | 删除         | &check;         | &check;          | &cross;          |

## 微服务网关权限说明

| 对象         | 操作 | Workspace Admin | Workspace Editor | Workspace Viewer |
| ------------ | ---- | --------------- | ---------------- | ---------------- |
| 网关列表     | 查看 | &check;         | &check;          | &check;          |
| 网关实例     | 查看 | &check;         | &check;          | &check;          |
|              | 创建 | &check;         | &check;          | &cross;          |
|              | 编辑 | &check;         | &check;          | &cross;          |
|              | 删除 | &check;         | &cross;          | &cross;          |
| 诊断模式     | 查看 | &check;         | &check;          | &check;          |
|              | 调试 | &check;         | &check;          | &cross;          |
| 服务列表     | 查看 | &check;         | &check;          | &check;          |
|              | 添加 | &check;         | &check;          | &cross;          |
|              | 编辑 | &check;         | &check;          | &cross;          |
|              | 删除 | &check;         | &check;          | &cross;          |
| 服务详情     | 查看 | &check;         | &check;          | &check;          |
| 服务来源管理 | 查看 | &check;         | &check;          | &check;          |
|              | 添加 | &check;         | &check;          | &cross;          |
|              | 编辑 | &check;         | &check;          | &cross;          |
|              | 删除 | &check;         | &check;          | &cross;          |
| API 列表     | 查看 | &check;         | &check;          | &check;          |
|              | 创建 | &check;         | &check;          | &cross;          |
|              | 编辑 | &check;         | &check;          | &cross;          |
|              | 删除 | &check;         | &check;          | &cross;          |
| 请求日志     | 查看 | &check;         | &check;          | &check;          |
| 实例日志     | 查看 | &check;         | &check;          | &check;          |
| 插件中心     | 查看 | &check;         | &check;          | &check;          |
|              | 启用 | &check;         | &check;          | &cross;          |
|              | 禁用 | &check;         | &check;          | &cross;          |
| 插件配置     | 查看 | &check;         | &check;          | &check;          |
|              | 启用 | &check;         | &check;          | &cross;          |
| 域名列表     | 查看 | &check;         | &check;          | &check;          |
|              | 添加 | &check;         | &check;          | &cross;          |
|              | 编辑 | &check;         | &check;          | &cross;          |
|              | 删除 | &check;         | &check;          | &check;          |
| 监控告警     | 查看 | &check;         | &check;          | &check;          |

!!! note

    有关角色和权限管理的完整介绍，请参考[角色和权限管理](../user-guide/access-control/role.md)。
