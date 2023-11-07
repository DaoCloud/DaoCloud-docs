# MySQL Release Notes

本页列出 MySQL 数据库的 Release Notes，便于您了解各版本的演进路径和特性变化。

## 2023-10-31

### v0.12.0

#### 优化

- **新增** 离线升级。
- **新增** 实例重启功能。
- **新增** 工作负载反亲和配置
- **新增** 跨集群恢复实例
- **修复** Pod 列表展示地址为 Host IP
- **修复** cloudshell 权限问题。

## 2023-08-31

### v0.11.0

#### 新功能

- **新增** 参数模板功能。

#### 优化

- **优化** KindBase 语法兼容。
- **优化** operator 创建过程的页面展示。

## 2023-07-31

### v0.10.3

#### 新功能

- **新增** UI 界面的权限访问限制。

## 2023-06-30

### v0.10.0

#### 新功能

- **优化** `mcamel-mysql` 备份管理页面结构样式展示。
- **优化** `mcamel-mysql` 监控图表，去除干扰元素并新增时间范围选择。
- **优化** `mcamel-mysql` 存储容量指标来源，使用中立指标。
- **优化** `mcamel-mysql` ServiceMonitor 闭环安装。

## 2023-05-30

### v0.9.0

#### 新功能

- **新增** `mcamel-mysql` 对接全局管理审计日志模块。
- **新增** `mcamel-mysql` 可配置实例监控数据采集间隔时间。
- **修复** `mcamel-mysql` 安装 MySQL Operator 多副本时，Raft 集群无法正常建立。
- **修复** `mcamel-mysql` 升级 MySQL Operator 多副本时 PodDisruptionBudget 版本到 v1。

## 2023-04-27

### v0.8.2

#### 新功能

- **新增** `mcamel-mysql` 详情页面展示相关的事件
- **新增** `mcamel-mysql` openapi 列表接口支持 Cluster 与 Namespace 字段过滤
- **新增** `mcamel-mysql` 自定义角色
- **新增** `mcamel-mysql` 对接 HwameiStor，支持存储容量展示（需要手动创建 HwameiStor exporter ServiceMonitor）

#### 升级

- **升级** 优化 调度策略增加滑动按钮

## 2023-03-28

### v0.7.0

#### 新功能

- **新增** `mcamel-mysql` 支持中间件链路追踪适配。
- **新增** 安装 `mcamel-mysql` 根据参数配置启用链路追踪。
- **新增** `mcamel-mysql` PhpMyAdmin 支持 LoadBalancer 类型。

#### 升级

- **升级** golang.org/x/net 到 v0.7.0
- **升级** GHippo SDK 到 v0.14.0
- **优化** `mcamel-mysql` common-mysql 支持多个实例优化。
- **优化** `mcamel-mysql` 排障手册增加更多处理方法。

## 2023-02-23

### v0.6.0

### 新功能

- **新增** `mcamel-mysql` helm-docs 模板文件。
- **新增** `mcamel-mysql` 应用商店中的 Operator 只能安装在 mcamel-system。
- **新增** `mcamel-mysql` 支持 cloud shell。
- **新增** `mcamel-mysql` 支持导航栏单独注册。
- **新增** `mcamel-mysql` 支持查看日志。
- **新增** `mcamel-mysql` 更新 Operator 版本。
- **新增** `mcamel-mysql` 展示 common MySQL 在实例列表中。
- **新增** `mcamel-mysql` 支持 MySQL8.0.29。
- **新增** `mcamel-mysql` 支持 LB。
- **新增** `mcamel-mysql` 支持 Operator 对接 chart-syncer。
- **新增** `mcamel-mysql` Operator 的 finalizers 权限以支持 openshift。
- **新增** `UI` 增加 MySQL 主从复制延迟情况展示
- **新增** `文档` 增加 日志查看操作说明，支持自定义查询、导出等功能。

#### 优化

- **升级** `mcamel-mysql` 升级离线镜像检测脚本。  

#### 修复

- **修复** `mcamel-mysql` 实例名太长导致自定义资源无法创建的问题。
- **修复** `mcamel-mysql` 工作空间 Editor 用户无法查看实例密码。
- **修复** `mcamel-mysql` 配置文件里 `expire-logs-days` 参数定义重复。
- **修复** `mcamel-mysql` 8.0 环境下 binlog 过期时间不符合预期。
- **修复** `mcamel-mysql` 备份集列表会展示出同名集群旧的备份集。

## 2022-12-25

### v0.5.0

#### 新功能

- **新增** NodePort 端口冲突提前检测。
- **新增** 节点亲和性配置。
- **新增** 创建备份配置时，可校验 Bucket。

- **修复** arm 环境中无法展示默认配置。
- **修复** 创建实例时 name 校验与前端不一致。
- **修复** 重新接入变更名字的集群后，配置管理地址展示错误。
- **修复** 保存自动备份配置失败。
- **修复** 自动备份集无法展示的问题。

## 2022-11-08

### v0.4.0

### 新功能

- **新增** 增加 MySQL 生命周期管理接口功能
- **新增** 增加 MySQL 详情接口功能
- **新增** 基于 grafana crd 对接 insight
- **新增** 增加与 ghippo 服务对接接口
- **新增** 增加与 kpanda 对接接口
- **新增** 单测覆盖率提升到 30%
- **新增** 新增备份恢复功能
- **新增** 新增备份配置接口
- **新增** 实例列表接口新增备份恢复来源字段
- **新增** 获取用户列表接口
- **新增** `mysql-operator` chart 参数，来指定 metric exporter 镜像
- **新增** 支持 arm64 架构
- **新增** 添加 arm64 operator 镜像打包
- **新增** 支持密码脱敏
- **新增** 支持服务暴露为 nodeport
- **新增** 支持 mtls
- **新增** `文档` 第一次文档网站发布
- **新增** `文档` 基本概念
- **新增** `文档` Concepts
- **新增** `文档` 首次使用 MySQL
- **新增** `文档` 删除 MySQL 实例

#### 优化

- **优化** 将时间戳 api 字段统一调整为 int64

#### 修复

- **修复** 修复备份列表接口模糊搜索无效
- **修复** 修复依赖漏洞
- **修复** 备份 Job 被删除后，无法展示备份任务列表
- **修复** 当镜像有大写和数字时不能被抓取到的问题

## 2022-10-18

### v0.3

#### 新功能

- **新增** 增加 MySQL 生命周期管理接口功能
- **新增** 增加 MySQL 详情接口功能
- **新增** 基于 grafana crd 对接 insight
- **新增** 增加与 ghippo 服务对接接口
- **新增** 增加与 kpanda 对接接口
- **新增** 单测覆盖率提升到 30%
- **新增** 新增备份恢复功能
- **新增** 新增备份配置接口
- **新增** 实例列表接口新增备份恢复来源字段
- **修复** 修复备份列表接口模糊搜索无效
- **优化** 将时间戳 api 字段统一调整为 int64
