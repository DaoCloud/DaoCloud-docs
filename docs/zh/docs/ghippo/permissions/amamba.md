# 应用工作台权限说明

应用工作台支持三种用户角色：Workspace Admin, Workspace Editor, Workspace Viewer。每种角色具有不同的权限，具体说明如下。

<!--
有权限使用`&check;`，无权限使用`&cross;`
-->

!!! note

    有关角色和权限管理的完整介绍，请参考[角色和权限管理](../04UserGuide/01UserandAccess/Role.md)。

## 权限说明

| 对象     | 操作                               | Workspace Admin | Workspace Editor | Workspace Viewer |
| -------- | ---------------------------------- | --------------- | ---------------- | ---------------- |
| 应用     | 查看应用列表                       | &check;         | &check;          | &check;          |
|          | 查看详情（跳转到容器管理）         | &check;         | ✓                | ✓                |
|          | 查看应用日志（跳转到可观测）       | &check;         | ✓                | ✓                |
|          | 查看应用监控（跳转到可观测）       | &check;         | ✓                | ✓                |
|          | 查看 rabbitmq 详情 基本信息        | &check;         | ✓                | ✓                |
|          | 查看服务网格（跳转到服务网格）     | &check;         | ✓                | ✓                |
|          | 查看微服务引擎（跳转到微服务引擎） | &check;         | ✓                | ✓                |
|          | 创建应用                           | &check;         | ✓                | &cross;          |
|          | 编辑YAML                           | &check;         | ✓                | &cross;          |
|          | 更新副本数量                       | &check;         | ✓                | &cross;          |
|          | 更新容器镜像                       | &check;         | ✓                | &cross;          |
|          | 编辑流水线                         | &check;         | ✓                | &cross;          |
|          | 应用分组                           | &check;         | ✓                | &cross;          |
|          | 删除                               | &check;         | ✓                | &cross;          |
| 命名空间 | 查看                               | &check;         | &check;          | &check;          |
|          | 创建                               | &check;         | &cross;          | &cross;          |
|          | 编辑标签                           | &check;         | &cross;          | &cross;          |
|          | 编辑资源配额                       | &check;         | &cross;          | &cross;          |
|          | 删除                               | &check;         | &cross;          | &cross;          |
| 流水线   | 查看流水线                         | &check;         | &check;          | &check;          |
|          | 查看运行记录                       | &check;         | &check;          | &check;          |
|          | 创建                               | &check;         | &check;          | &cross;          |
|          | 运行                               | &check;         | &check;          | &cross;          |
|          | 删除                               | &check;         | &check;          | &cross;          |
|          | 复制                               | &check;         | &check;          | &cross;          |
|          | 编辑                               | &check;         | &check;          | &cross;          |
|          | 取消运行                           | &check;         | &check;          | &cross;          |
| 凭证     | 查看                               | &check;         | &check;          | &check;          |
|          | 创建                               | &check;         | &check;          | &cross;          |
|          | 编辑                               | &check;         | &check;          | &cross;          |
|          | 删除                               | &check;         | &check;          | &cross;          |
| 持续部署 | 查看                               | &check;         | &check;          | &check;          |
|          | 创建                               | &check;         | &check;          | &cross;          |
|          | 同步                               | &check;         | &check;          | &cross;          |
|          | 编辑                               | &check;         | &check;          | &cross;          |
|          | 删除                               | &check;         | &check;          | &check;          |
| 代码仓库 | 查看                               | &check;         | &check;          | &cross;          |
|          | 导入                               | &check;         | &check;          | &cross;          |
|          | 删除                               | &check;         | &check;          | &cross;          |
| 灰度发布 | 查看                               | &check;         | &check;          | &check;          |
|          | 创建                               | &check;         | &check;          | &cross;          |
|          | 发布                               | &check;         | &check;          | &cross;          |
|          | 继续发布                           | &check;         | &check;          | &cross;          |
|          | 终止发布                           | &check;         | &check;          | &cross;          |
|          | 更新                               | &check;         | &check;          | &cross;          |
|          | 回滚                               | &check;         | &check;          | &cross;          |
|          | 删除                               | &check;         | &check;          | &cross;          |
