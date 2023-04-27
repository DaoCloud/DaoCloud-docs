# Redis 缓存服务 Release Notes

本页列出 Redis 缓存服务的 Release Notes，便于您了解各版本的演进路径和特性变化。

## v0.7.1

发布日期：2023-04-27

### 新功能

- **新增** `mcamel-redis` 支持自动化备份恢复
- **新增** `Mcamel-Redis` 获取用户列表接口
- **新增** `Mcamel-Redis` 支持 arm 架构
- **新增** `Mcamel-Redis` 支持在 ARM 环境安装主备模式的 Redis 集群
- **新增** `Mcamel-Redis` sc 扩容提示
- **新增** `Mcamel-Redis` 返回列表或者详情时的公共字段
- **新增** `Mcamel-Redis` 增加返回告警列表
- **新增** `Mcamel-Redis` 校验 Service 注释
- **新增** `Mcamel-Redis` 当部署单例和集群模式的时候，会自动添加probe
- **新增** `Mcamel-Redis` 获取集群已经分配的 NodePort 列表接口
- **新增** `Mcamel-Redis` NodePort 端口冲突提前检测
- **新增** `Mcamel-Redis` 节点亲和性配置
- **新增** `Mcamel-Redis` helm-docs 模版文件
- **新增** `Mcamel-Redis` 应用商店中的 Operator 只能安装在 mcamel-system
- **新增** `Mcamel-Redis` 支持 cloud shell
- **新增** `Mcamel-Redis` 支持导航栏单独注册
- **新增** `Mcamel-Redis` 支持查看日志
- **新增** `Mcamel-Redis` 更新单例/集群模式 Operator 的版本
- **新增** `Mcamel-Redis` 展示 common Redis 集群
- **新增** `Mcamel-Redis` Operator 对接 chart-syncer
- **新增** `Mcamel-Redis` 哨兵模式/单实例模式备份
- **新增** `Mcamel-Redis` 哨兵模式恢复
- **新增** `Mcamel-Redis` 支持 LoadBalancer 类型
- **新增** `Mcamel-Redis` 支持接入链路追踪
- **新增** `Mcamel-Redis` 详情页面展示相关的事件
- **新增** `Mcamel-Redis` 列表接口支持 Cluster 与 Namespace 字段过滤
- **新增** `Mcamel-Redis` 自定义角色

#### 修复

- **优化** `Mcamel-Redis` 密码校验调整为 MCamel 低等密码强度
- **优化** `Mcamel-Redis` 提升哨兵模式的版本依赖，v1.1.1=>v1.2.2,重要变成，支持k8s 1.25+
- **优化** `Mcamel-Redis` 集群模式operator 修改镜像和更新charts版本和apiserver依赖的版本
- **优化** `Mcamel-Redis` 集群模式 redis 的版本
- **优化** `Mcamel-Redis` 当目标ns带有特定anntations的时候会提前给出提示
- **优化** `Mcamel-Redis` 镜像拉取策略为IfNotPresent
- **修复** `mcamel-redis` 优化 调度策略增加滑动按钮
- **修复** `Mcamel-Redis` 更新 Redis 时校验部分字段错误
- **修复** `Mcamel-Redis` 服务地址展示错误
- **修复** `Mcamel-Redis` 当镜像包含大写和数字不能被扫描到
- **修复** `Mcamel-Redis` 前端镜像tag和operator的tag冲突，导致不需要改到的镜像被修改了
- **修复** `Mcamel-Redis` 集群模式的probe没有设置成功，导致operator 报错
- **修复** `Mcamel-Redis` exporter 的离线镜像不生效的问题
- **修复** `Mcamel-Redis` 单例和集群设置nodeport无效的问题
- **修复** `Mcamel-Redis` 集群模式下，从节点不可以设置为0的问题
- **修复** `Mcamel-Redis` Operator的版本和IP地址冲突
- **修复** `Mcamel-Redis` 实例名太长导致自定义资源无法创建的问题
- **修复** `Mcamel-Redis` 工作空间 Editor 用户无法查看实例密码
- **修复** `Mcamel-Redis` 不能解析出正确的 Redis 版本号
- **修复** `Mcamel-Redis` 无法修改 Port 的问题
- **修复** `Mcamel-Redis` Redis 恢复时无法识别到备份文件名
- **升级** `Mcamel-Redis` release notes 脚本 
- **升级** `Mcamel-Redis` 离线镜像检测脚本
- **升级** `Mcamel-Redis` 单实例/集群模式的 Operator 以支持 PVC 扩容
- **升级** `Mcamel-Redis` 哨兵模式的 Operator 以支持备份恢复


## v0.6.2

发布日期：2023-03-29

### 新功能

- **新增** `mcamel-redis` 支持自动化备份恢复。

#### 修复

- **修复** 没有导出备份恢复的离线镜像。
- **修复** `mcamel-redis` 没有导出备份恢复的离线镜像。
- **修复** `mcamel-redis` 修复了若干已知问题，提升了系统稳定性和安全性。

### 文档

- **新增** 新增备份功能使用文档。

## v0.5.0

发布日期：2023-02-23

### API

- **新增** `mcamel-redis` helm-docs 模板文件。
- **新增** `mcamel-redis` 应用商店中的 Operator 只能安装在 mcamel-system。
- **新增** `mcamel-redis` 支持 cloud shell。
- **新增** `mcamel-redis` 支持导航栏单独注册。
- **新增** `mcamel-redis` 支持查看日志。
- **新增** `mcamel-redis` 更新单例/集群模式 Operator 的版本。
- **新增** `mcamel-redis` 展示 common Redis 集群。
- **新增** `mcamel-redis` Operator 对接 chart-syncer。
- **修复** `mcamel-redis` 实例名太长导致自定义资源无法创建的问题。
- **修复** `mcamel-redis` 工作空间 Editor 用户无法查看实例密码。
- **修复** `mcamel-redis` 不能解析出正确的 Redis 版本号。
- **修复** `mcamel-redis` 无法修改 Port 的问题。
- **升级** `mcamel-redis` 升级离线镜像检测脚本。  

### 文档

- **新增** 日志查看操作说明，支持自定义查询、导出等功能。

## v0.4.0

发布日期：2022-12-25

### API

- **新增** `mcamel-redis` NodePort 端口冲突提前检测。
- **新增** `mcamel-redis` 节点亲和性配置。
- **修复** `mcamel-redis` 单例和集群设置 nodeport 无效的问题。
- **修复** `mcamel-redis` 集群模式下，从节点不可以设置为 0 的问题。

## v0.2.6

发布日期：2022-11-28

### API

- **修复** 更新 Redis 时校验部分字段错误
- **改进** 密码校验调整为 MCamel 低等密码强度
- **改进** 提升哨兵模式的版本依赖，v1.1.1=>v1.2.2，重要变更为支持 k8s 1.25+
- **新增** 支持在 ARM 环境安装主备模式的 Redis 集群
- **新增** sc 扩容提示
- **新增** 返回列表或者详情时的公共字段
- **新增** 增加返回告警列表
- **新增** 校验 Service 注释
- **修复** 服务地址展示错误

## v0.2.2

发布日期：2022-10-26

### API

- **新增** 获取用户列表接口
- **新增** 支持 arm 架构
- **新增** redis 实例全生命周期的管理
- **新增** redis 实例的监控部署
- **新增** 支持 redis 哨兵，单例和集群一键部署
- **新增** 支持 ws 权限隔离
- **新增** 支持在线动态扩容
- **升级** release notes 脚本
