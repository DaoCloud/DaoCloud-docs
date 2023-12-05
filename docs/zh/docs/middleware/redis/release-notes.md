# Redis 缓存服务 Release Notes

本页列出 Redis 缓存服务的 Release Notes，便于您了解各版本的演进路径和特性变化。

## 2023-11-30

### v0.13.0

#### 优化

- **新增** 支持记录操作审计日志
- **优化** 实例列表未获取到列表信息时的提示
- **优化** Mcamel-Redis 监控 Dashboard 的中英文展示

## 2023-10-31

### v0.12.0

#### 优化

- **新增** 离线升级。
- **新增** 实例重启功能。
- **新增** 参数模版功能
- **新增** 跨集群恢复实例
- **优化** 主从延迟的计算方式
- **修复** cloudshell 权限问题。

## 2023-08-31

### v0.11.0

#### 优化

- **优化** KindBase 语法兼容。
- **优化** operator 创建过程的页面展示。

## 2023-07-31

### v0.10.0

#### 新功能

- **新增** `mcamel-redis` 访问白名单配置。

#### 优化

- **优化** `mcamel-redis` 创建实例对话框添加默认反亲和标签值，简化配置过程。
- **优化** `mcamel-redis` 数据恢复界面。
- **优化** `mcamel-redis` 前端界面权限展示信息。

#### 修复

- **修复** `mcamel-redis` 关闭节点亲和性失败。

## 2023-06-30

### v0.9.0

#### 新功能

- **新增** `mcamel-redis` 不同命名空间下无法创建同名 Redis。
- **新增** `mcamel-redis` 非 MCamel 纳管的 Redis 可能被误操作的问题。

#### 优化

- **优化** `mcamel-redis` 备份管理页面结构样式展示。
- **优化** `mcamel-redis` 备份 Job 中的密码展示问题。
- **优化** `mcamel-redis` 监控图表，去除干扰元素并新增时间范围选择。
- **优化** `mcamel-redis` ServiceMonitor 闭环安装。

## 2023-05-30

### v0.8.0

#### 新功能

- **新增** `mcamel-redis` 可配置实例反亲和性。
- **新增** `mcamel-redis` 对接全局管理审计日志模块。
- **修复** `mcamel-redis` 删除 Redis 后，备份相关内容残留。

#### 修复

- **修复** `mcamel-redis` 哨兵集群的 Service 地址展示错误。

## 2023-04-27

### v0.7.1

### 新功能

- **新增** `mcamel-redis` 详情页面展示相关的事件
- **新增** `mcamel-redis` 列表接口支持 Cluster 与 Namespace 字段过滤
- **新增** `mcamel-redis` 自定义角色

#### 修复

- **修复** `mcamel-redis` 优化 调度策略增加滑动按钮

## 2023-03-29

### v0.6.2

#### 新功能

- **新增** `mcamel-redis` 支持自动化备份恢复。

##### 修复

- **修复** 没有导出备份恢复的离线镜像。
- **修复** `mcamel-redis` 没有导出备份恢复的离线镜像。
- **修复** `mcamel-redis` 修复了若干已知问题，提升了系统稳定性和安全性。

#### 文档

- **新增** 新增备份功能使用文档。

## 2023-02-23

### v0.5.0

#### API

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

#### 文档

- **新增** 日志查看操作说明，支持自定义查询、导出等功能。

## 2022-12-25

### v0.4.0

#### API

- **新增** `mcamel-redis` NodePort 端口冲突提前检测。
- **新增** `mcamel-redis` 节点亲和性配置。
- **修复** `mcamel-redis` 单例和集群设置 nodeport 无效的问题。
- **修复** `mcamel-redis` 集群模式下，从节点不可以设置为 0 的问题。

## 2022-11-28

### v0.2.6

#### API

- **修复** 更新 Redis 时校验部分字段错误
- **改进** 密码校验调整为 MCamel 低等密码强度
- **改进** 提升哨兵模式的版本依赖，v1.1.1=>v1.2.2，重要变更为支持 k8s 1.25+
- **新增** 支持在 ARM 环境安装主备模式的 Redis 集群
- **新增** sc 扩容提示
- **新增** 返回列表或者详情时的公共字段
- **新增** 增加返回告警列表
- **新增** 校验 Service 注释
- **修复** 服务地址展示错误

## 2022-10-26

### v0.2.2

#### API

- **新增** 获取用户列表接口
- **新增** 支持 arm 架构
- **新增** redis 实例全生命周期的管理
- **新增** redis 实例的监控部署
- **新增** 支持 redis 哨兵，单例和集群一键部署
- **新增** 支持 ws 权限隔离
- **新增** 支持在线动态扩容
- **升级** release notes 脚本
