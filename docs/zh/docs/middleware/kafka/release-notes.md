# Kafka 消息队列 Release Notes

本页列出 Kafka 消息队列的 Release Notes，便于您了解各版本的演进路径和特性变化。

## v0.4.0

发布日期：2023-03-28

### API

- **新增** `mcamel-kafka` 支持中间件链路追踪适配。
- **优化** `mcamel-kafka` 优化 Kafka 的默认配置。

### 文档

- **新增** 安装 `mcamel-kafka` 根据参数配置启用链路追踪。

### 其他

- **升级** golang.org/x/net 到 v0.7.0
- **升级** GHippo SDK 到 v0.14.0

## v0.3.0

发布日期：2023-02-23

### API

- **新增** `mcamel-kafka` helm-docs 模板文件。
- **新增** `mcamel-kafka` 应用商店中的 Operator 只能安装在 mcamel-system。
- **新增** `mcamel-kafka` 支持 cloud shell。
- **新增** `mcamel-kafka` 支持导航栏单独注册。
- **新增** `mcamel-kafka` 支持查看日志。
- **新增** `mcamel-kafka` Operator 对接 chart-syncer。
- **修复** `mcamel-kafka` 实例名太长导致自定义资源无法创建的问题。
- **修复** `mcamel-kafka` 工作空间 Editor 用户无法查看实例密码。
- **升级** `mcamel-kafka` 升级离线镜像检测脚本。  

### 文档

- **新增** 日志查看操作说明，支持自定义查询、导出等功能。

## v0.2.0

发布日期：2022-12-25

### API

- **新增** `mcamel-kafka` NodePort 端口冲突提前检测。
- **新增** `mcamel-kafka` 节点亲和性配置。
- **优化** `mcamel-kafka` manager 去掉 probe，防止 kafka 没准备好不能打开 manager。  
- **优化** `mcamel-kafka` zooEntrance 重新打包镜像地址为 1.0.0。  

## v0.1.6

发布日期：2022-11-28

### API

- **改进** 完善优化复制功能
- **改进** 实例详情 - 访问设置，移除集群 IPv4
- **改进** 中间件密码校验难度调整
- **新增** 对接告警能力
- **新增** 新增判断 sc 是否支持扩容并提前提示功能
- **优化** 优化安装环境检测的提示逻辑 & 调整其样式
- **优化** 中间件样式走查优化
- **修复** 离线镜像有数字和大写无法被扫描到

## v0.1.4

发布日期：2022-11-08

### API

- **修复** 更新时无法校验到正确字段，如 managerPass
- **改进** 密码校验调整为 MCamel 低等密码强度
- **新增** 返回是否可以更新 sc 容量的校验
- **新增** 返回列表或者详情时的公共字段
- **新增** 返回告警
- **新增** 校验 Service 注释
- **修复** operator 用名字选择
- **修复** 服务地址展示错误
- **修复** Kafka 使用 NodePort 时，创建失败

## v0.1.2

发布日期：2022-10-28

- **新增** 同步 Pod 状态到实例详情页
- **优化** workspace 界面逻辑调整
- **优化** 不符合设计规范的样式调整
- **优化** password 获取逻辑调整
- **优化** cpu&内存请求量应该小于限制量逻辑调整

## v0.1.1

发布日期：2022-9-25

- **新增** 支持 kafka 列表查询，状态查询，创建，删除和修改
- **新增** 支持 kafka-manager 对 kafka 进行管理
- **新增** 支持 kafka 的指标监控，查看监控图表
- **新增** 支持 ghippo 权限联动
- **新增** `mcamel-elasticsearch` 获取用户列表接口
- **优化** 更新 release note 脚本，执行 release-process 规范
