# 中间件 Release Notes

本页汇总所有中间件模块的 Release Notes。

*[Elasticsearch]: 分布式全文搜索与分析引擎，适用于日志检索、监控与复杂查询分析。
*[Kafka]: 高吞吐、分布式的流式消息平台，适用于实时数据处理和日志收集。
*[MinIO]: 兼容 S3 接口的高性能对象存储系统，适合存储非结构化数据如图像、视频与备份文件。
*[MongoDB]: 面向文档的 NoSQL 数据库。
*[MySQL]: 广泛使用的关系型数据库。
*[PostgreSQL]: 一个开源的对象关系型数据库，支持复杂查询、事务处理与扩展性强的数据建模。
*[RabbitMQ]: 支持多种协议的消息中间件，适合构建可靠的异步通信系统。
*[Redis]: 高性能键值对存储系统，广泛用于缓存、会话管理和分布式锁。
*[RocketMQ]: 高可靠、可扩展的分布式消息中间件，适用于事务消息和顺序消息场景。

## 2025-02-28

### Elasticsearch v0.24.0

- **新增** 支持创建 v8.17.1 版本的 `Elasticsearch` 实例

### Kafka v0.23.0

- **优化** 将 Kafka 管理工具由 `CMAK` 更新为 `kafka-ui`

### MySQL v0.26.0

- **优化** 升级 `mysqld-exporter` 镜像，并支持 `MySQL-MGR` 的告警规则

### Redis v0.27.0

- **新增** 支持创建 `7.2.7` 版本的 `Redis` 实例

### RocketMQ v0.14.0

- **新增** 支持为 RocketMQ 实例配置静态 IP
- **优化** 支持配置 时区的环境变量
- **优化** 升级 operator 镜像
- **修复** 名称服务器重启后控制台连接错误的问题

## 2024-11-30

### Elasticsearch v0.23.0

- **优化** 默认不启用 geoip 数据库以避免健康状态为 yellow

### Kafka v0.21.0

- **优化** 升级 kafka-operator 镜像版本到 0.40.0，并支持创建 3.7.0 版本的 kafka 实例
- **优化** 增加 kafka-operator 的内存限制量

### Redis v0.24.0

- **优化** 支持部署 7.2.6 版本的 Redis 实例
- **优化** Redis 哨兵模式支持设置非动态参数
- **修复** Redis 哨兵模式重启后无法启动的问题

## 2024-09-30

### Elasticsearch v0.21.0

- **新增** 创建实例时支持选择 HTTPS / HTTP 协议
- **修复** 部分操作无审计日志的问题
- **修复** 安装器创建的 Elasticsearch 实例纳管失败的问题

### Kafka v0.19.0

- **修复** 选择工作空间查询 Kafka 列表时权限泄漏的问题
- **修复** 部分操作无审计日志的问题

### MinIO v0.19.0

- **修复** 选择工作空间查询 MinIO 列表时权限泄漏的问题
- **修复** 部分操作无审计日志的问题

### MongoDB v0.14.0

- **优化** 备份恢复的新实例中 Express 节点的服务类型默认为 NodePort
- **修复** 选择工作空间查询 MongoDB 列表时权限泄漏的问题
- **修复** 部分操作无审计日志的问题
- **修复** 恢复 MongoDB 失败的问题

### MySQL v0.22.0

- **新增** 支持手动切换主从节点
- **新增** MGR 实例支持配置 Router 节点
- **修复** 部分操作无审计日志的问题

### PostgreSQL v0.16.0

- **修复** 选择工作空间查询 PostgreSQL 列表时权限泄漏的问题
- **修复** 部分操作无审计日志的问题

### RabbitMQ v0.24.0

- **修复** 部分操作无审计日志的问题
- **修复** 修改实例集群名称后导致无法查询监控数据的问题

### Redis v0.22.0

- **修复** 选择工作空间查询 Redis 列表时权限泄漏的问题
- **修复** 部分操作无审计日志的问题

### RocketMQ v0.11.0

- **修复** 容器组列表未展示实例中所有相关的容器组
- **修复** 选择工作空间查询 Redis 列表时权限泄漏的问题
- **修复** 部分操作无审计日志的问题

## 2024-08-31

### MinIO v0.18.1

- **优化** 创建实例时不可选择异常的集群
- **修复** `minio operator` 多副本退出机制存在缺陷，调整为单副本

### MongoDB v0.13.0

!!! warning

    升级 mongodb-operator 到 v0.10.0 会导致已有的实例进行重启。

- **优化** 创建实例时不可选择异常的集群
- **优化** 恢复的新实例的控制台访问方式默认为 Nodeport
- **优化** 升级 mongodb-operator 版本到 0.10.0，基础镜像均使用 ubi-minimal:8.6-994。
- **修复** 恢复 MongoDB 实例失败的问题

### MySQL v0.21.0

- **优化** 创建实例时不可选择异常的集群
- **优化** 接口中权限泄露的问题

### PostgreSQL v0.15.0

- **优化** 创建实例时不可选择异常的集群
- **修复** 纳管 PostgreSQL 实例时内存为空导致失败的问题

### RabbitMQ v0.23.0

- **优化** 创建实例时不可选择异常的集群

<span id="history"></span>

## 历史版本链接

- [Elasticsearch 历史版本的 Release Notes](./elasticsearch/release-notes.md)
- [Kafka 历史版本的 Release Notes](./kafka/release-notes.md)
- [MinIO 历史版本的 Release Notes](./minio/release-notes.md)
- [MongoDB 历史版本的 Release Notes](./mongodb/release-notes.md)
- [MySQL 历史版本的 Release Notes](./mysql/release-notes.md)
- [PostgreSQL 历史版本的 Release Notes](./postgresql/release-notes.md)
- [RabbitMQ 历史版本的 Release Notes](./rabbitmq/release-notes.md)
- [Redis 历史版本的 Release Notes](./redis/release-notes.md)
- [RocketMQ 历史版本的 Release Notes](./rocketmq/release-notes.md)
