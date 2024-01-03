# 中间件数据服务权限说明

[中间件数据服务](../../middleware/index.md)包括了许多精选的中间件：MySQL、Redis、MongoDB、PostgreSQL、Elasticsearch、Kafka、RabbitMQ、RocketMQ、MinIO。
中间件数据服务支持三种用户角色：

- Workspace Admin
- Workspace Editor
- Workspace Viewer

每种角色具有不同的权限，具体说明如下。

<!--
有权限使用 `&check;`，无权限使用 `&cross;`
-->

## 中间件数据服务权限说明

| 中间件模块    | 菜单对象               | 操作                 | Workspace Admin | Workspace Editor | Workspace Viewer |
| ------------- | ---------------------- | -------------------- | --------------- | ---------------- | ---------------- |
| MySQL         | MySQL 实例列表         | 查看列表             | &check;         | &check;          | &check;          |
|               |                        | 实例名称搜索         | &check;         | &check;          | &check;          |
|               |                        | 创建实例             | &check;         | &check;          | &cross;          |
|               |                        | 更新实例配置         | &check;         | &check;          | &cross;          |
|               |                        | 删除实例             | &check;         | &cross;          | &cross;          |
|               | MySQL 实例详情         | 实例概览             | &check;         | &check;          | &check;          |
|               |                        | 实例监控             | &check;         | &check;          | &check;          |
|               |                        | 查看实例配置参数     | &check;         | &check;          | &check;          |
|               |                        | 修改实例配置参数     | &check;         | &check;          | &cross;          |
|               |                        | 查看实例访问密码     | &check;         | &check;          | &cross;          |
|               |                        | 查看实例备份列表     | &check;         | &check;          | &check;          |
|               |                        | 实例创建备份         | &check;         | &check;          | &cross;          |
|               |                        | 实例修改自动备份任务 | &check;         | &check;          | &cross;          |
|               |                        | 使用备份创建新实例   | &check;         | &check;          | &cross;          |
|               | 备份配置管理           | 备份配置列表         | &check;         | &cross;          | &cross;          |
|               |                        | 创建备份配置         | &check;         | &cross;          | &cross;          |
|               |                        | 修改备份配置         | &check;         | &cross;          | &cross;          |
|               |                        | 删除备份配置         | &check;         | &cross;          | &cross;          |
| RabbitMQ      | RabbitMQ 实例列表      | 查看列表             | &check;         | &check;          | &check;          |
|               |                        | 实例名称搜索         | &check;         | &check;          | &check;          |
|               |                        | 创建实例             | &check;         | &check;          | &cross;          |
|               |                        | 更新实例配置         | &check;         | &check;          | &cross;          |
|               |                        | 删除实例             | &check;         | &cross;          | &cross;          |
|               | RabbitMQ 实例详情       | 实例概览             | &check;         | &check;          | &check;          |
|               |                        | 实例监控             | &check;         | &check;          | &check;          |
|               |                        | 查看实例配置参数     | &check;         | &check;          | &check;          |
|               |                        | 修改实例配置参数     | &check;         | &check;          | &cross;          |
|               |                        | 查看实例访问密码     | &check;         | &check;          | &cross;          |
| Elasticsearch | Elasticsearch 实例列表 | 查看列表             | &check;         | &check;          | &check;          |
|               |                        | 实例名称搜索         | &check;         | &check;          | &check;          |
|               |                        | 创建实例             | &check;         | &check;          | &cross;          |
|               |                        | 更新实例配置         | &check;         | &check;          | &cross;          |
|               |                        | 删除实例             | &check;         | &cross;          | &cross;          |
|               | Elasticsearch 实例详情  | 实例概览             | &check;         | &check;          | &check;          |
|               |                        | 实例监控             | &check;         | &check;          | &check;          |
|               |                        | 查看实例配置参数     | &check;         | &check;          | &check;          |
|               |                        | 修改实例配置参数     | &check;         | &check;          | &cross;          |
|               |                        | 查看实例访问密码     | &check;         | &check;          | &cross;          |
| Redis         | Redis 实例列表         | 查看列表             | &check;         | &check;          | &check;          |
|               |                        | 实例名称搜索         | &check;         | &check;          | &check;          |
|               |                        | 创建实例             | &check;         | &check;          | &cross;          |
|               |                        | 更新实例配置         | &check;         | &check;          | &cross;          |
|               |                        | 删除实例             | &check;         | &cross;          | &cross;          |
|               | Redis 实例详情          | 实例概览             | &check;         | &check;          | &check;          |
|               |                        | 实例监控             | &check;         | &check;          | &check;          |
|               |                        | 查看实例配置参数     | &check;         | &check;          | &check;          |
|               |                        | 修改实例配置参数     | &check;         | &check;          | &cross;          |
|               |                        | 查看实例访问密码     | &check;         | &check;          | &cross;          |
| Kafka         | Kafka 实例列表         | 查看列表             | &check;         | &check;          | &check;          |
|               |                        | 实例名称搜索         | &check;         | &check;          | &check;          |
|               |                        | 创建实例             | &check;         | &check;          | &cross;          |
|               |                        | 更新实例配置         | &check;         | &check;          | &cross;          |
|               |                        | 删除实例             | &check;         | &cross;          | &cross;          |
|               | Kafka 实例详情          | 实例概览             | &check;         | &check;          | &check;          |
|               |                        | 实例监控             | &check;         | &check;          | &check;          |
|               |                        | 查看实例配置参数     | &check;         | &check;          | &check;          |
|               |                        | 修改实例配置参数     | &check;         | &check;          | &cross;          |
|               |                        | 查看实例访问密码     | &check;         | &check;          | &cross;          |
| MinIO         | MinIO 实例列表         | 查看列表             | &check;         | &check;          | &check;          |
|               |                        | 实例名称搜索         | &check;         | &check;          | &check;          |
|               |                        | 创建实例             | &check;         | &check;          | &cross;          |
|               |                        | 更新实例配置         | &check;         | &check;          | &cross;          |
|               |                        | 删除实例             | &check;         | &cross;          | &cross;          |
|               | MinIO 实例详情          | 实例概览             | &check;         | &check;          | &check;          |
|               |                        | 实例监控             | &check;         | &check;          | &check;          |
|               |                        | 查看实例配置参数     | &check;         | &check;          | &check;          |
|               |                        | 修改实例配置参数     | &check;         | &check;          | &cross;          |
|               |                        | 查看实例访问密码     | &check;         | &check;          | &cross;          |
