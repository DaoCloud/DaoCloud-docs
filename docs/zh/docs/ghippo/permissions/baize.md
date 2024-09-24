---
hide:
  - toc
---

# AI Lab 权限说明

[AI Lab](../../baize/intro/index.md)支持四种用户角色：

- Admin / Baize Owner：拥有 `开发控制台` 和 `运维管理` 全部功能的增删改查的权限。
- Workspace Admin：拥有授权工作空间的 `开发控制台` 全部功能的增删改查的权限。
- Workspace Editor：拥有授权工作空间的 `开发控制台` 全部功能的更新、查询的权限。
- Workspace Viewer：拥有授权工作空间的 `开发控制台` 全部功能的查询的权限。

每种角色具有不同的权限，具体说明如下。

<!--
有权限使用 `&check;`，无权限使用 `&cross;`
-->

| 菜单对象 |操作 |Admin / Baize Owner |Workspace Admin |Workspace Editor |Workspace Viewer |
|-----------|-----------|---------------|---------|-----|----|
| **开发控制台** | | | | | |
| 概览 | 查看概览 | &check; | &check; | &check; | &check; |
| Notebooks | 查看 Notebooks 列表 | &check; | &check; | &check; | &check; |
| | 查看 Notebooks 详情 | &check; | &check; | &check; | &cross; |
| | 创建 Notebooks | &check; | &check; | &cross; | &cross; |
| | 更新 Notebooks | &check; | &check; | &check; | &cross; |
| | 克隆 Notebooks | &check; | &check; | &cross; | &cross; |
| | 停止 Notebooks | &check; | &check; | &check; | &cross; |
| | 启动 Notebooks | &check; | &check; | &check; | &cross; |
| | 删除 Notebooks | &check; | &check; |  &cross; | &cross; |
| 任务列表 | 查看任务列表 | &check; | &check; | &check; | &check; |
| | 查看任务详情 | &check; | &check; | &check; | &check; |
| | 创建任务 | &check; | &check; | &cross; | &cross; |
| | 克隆任务 | &check; | &check; | &cross; | &cross; |
| | 查看任务负载详情 | &check; | &check; | &check; | &cross; |
| | 删除任务 | &check; | &check; | &cross; | &cross; |
| 任务分析 | 查看任务分析 | &check; | &check; | &check; | &check; |
| | 查看任务分析详情 | &check; | &check; | &check; | &check; |
| | 删除任务分析 | &check; | &check; | &cross; | &cross; |
| 数据集列表 | 查看数据集列表 | &check; | &check; | &check; | &cross; |
| | 创建数据集 | &check; | &check; | &cross; | &cross; |
| | 重新同步数据集 | &check; | &check; | &check; | &cross; |
| | 更新凭证 | &check; | &check; | &check; | &cross; |
| | 删除数据集 | &check; | &check; | &cross; | &cross; |
| 环境管理 | 查看环境管理列表 | &check; | &check; | &check; | &check; |
| | 创建环境 | &check; | &check; | &cross; | &cross; |
| | 更新环境 | &check; | &check; | &check; | &cross; |
| | 删除环境 | &check; | &check; | &cross; | &cross; |
| 推理服务 | 查看推理服务列表 | &check; | &check; | &check; | &check; |
| | 查看推理服务详情 | &check; | &check; | &check; | &check; |
| | 创建推理服务 | &check; | &check; | &cross; | &cross; |
| | 更新推理服务 | &check; | &check; | &check; | &cross; |
| | 停止推理服务 | &check; | &check; | &check; | &cross; |
| | 启动推理服务 | &check; | &check; | &check; | &cross; |
| | 删除推理服务 | &check; | &check; | &cross; | &cross; |
| **运维管理** | | | | | |
| 概览 | 查看概览 | &check; | &cross; | &cross; | &cross; |
| GPU 管理 | 查看 GPU 管理列表 | &check; | &cross; | &cross; | &cross; |
| 队列管理 | 查看队列管理列表 | &check; | &cross; | &cross; | &cross; |
| | 查看队列详情 | &check; | &cross; | &cross; | &cross; |
| | 创建队列 | &check; | &cross; | &cross; | &cross; |
| | 更新队列 | &check; | &cross; | &cross; | &cross; |
| | 删除队列 | &check; | &cross; | &cross; | &cross; |
