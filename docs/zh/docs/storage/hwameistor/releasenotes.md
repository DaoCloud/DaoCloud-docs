# Hwameistor Release Notes

本页列出 Hwameistor 相关的 Release Notes，便于您了解各版本的演进路径和特性变化。

## 2023-8-30

### v0.12.1

#### 新功能

- **新增** 支持`ext`文件系统
- **新增** Local Disk 新特性参数
- **新增** 字段 记录 设备历史信息
- **新增** SN/ID Path 识别 磁盘
- **新增** 磁盘自动扩容功能
- **新增** 系统资源审计功能，如： 集群，存储节点，磁盘，数据卷等

#### 优化

- **修复** LocalStoragePool 节点的 NVME 磁盘显示问题
- **修复** 迁移操作丢失副本状态问题
- **修复** 当 Disk Owner 为空时，磁盘不允许分配问题
- **修复** Failover功能 `deploy`,`Makefile` 等问题

## 2023-7-05

### v0.11.1

#### 新功能

**新增** 支持自动检测 `cgroup` 版本

## 2023-6-25

### v0.11.0

#### 新功能

- **新增** 实现 IO 限制或 QoS

- **新增** 使用 /virtual/ 检测来识别虚拟块设备

#### 优化

- **修复** 存储池创建时间字段不一致问题

## 2023-5-26

### v0.10.3

#### 优化

- **优化** Helm 模板中权限功相关内容

## 2023-5-25

### v0.10.2

#### 优化

- **优化** Node Name `.` 自动转成 `-` 问题，影响 LDM 心跳检测
- **新增** Admin 权限功能

## 2023-5-17

### v0.10.0

#### 优化

- **新增** 识别并设置本地磁盘 Manager Owner 信息
- **优化** 当接收到 移除时间，将磁盘状态标记为 'inactive'
- **优化** 磁盘 Smart 指标仪表盘
- **新增** 本地存储池
- **优化** UI 组件状态展示
- **优化** 分离磁盘分配和磁盘状态更新过程
- **优化** 将Exportor端口重命名为 http-metrics
- **优化** 在exporter service中添加端口名称

#### 缺陷

- **修复** LD bound，但是LSN中没有容量的问题
- **修复** Metrics 端口监听问题
- **修复** May occur `not found`的问题
- **修复** Helm 中UI tag 的问题

### v0.9.3

#### 优化

- **优化** 在使用阶段填充磁盘所有者信息
- **优化** udev事件触发时合并磁盘自身属性
- **优化** 给svc添加标签
- **优化** 分离磁盘分配和磁盘状态更新过程
- **优化** 将Exportor端口重命名为 http-metrics
- **优化** 在exporter service中添加端口名称

#### 缺陷

- **修复** LD bound，但是LSN中没有容量的问题
- **修复** Metrics 端口监听问题
- **修复** May occur `not found`的问题
- **修复** Helm 中UI tag 的问题

## 2023-3-30

### v0.9.2

#### 优化

- **新增** UI relok8s

### v0.9.1

#### 优化

- **新增** Volume Status 监控 [Issue #741](https://github.com/hwameistor/hwameistor/pull/741)
- **修复** Local Storage 部署参数 [Issue #742](https://github.com/hwameistor/hwameistor/pull/742)

### v0.9.0

#### 新功能

- **新增** 磁盘 Owner [Issue #681](https://github.com/hwameistor/hwameistor/pull/681)
- **新增** Grafana DashBoard [Issue #733](https://github.com/hwameistor/hwameistor/pull/733)
- **新增** Operator 安装方式，安装时自动拉取 UI [Issue #679](https://github.com/hwameistor/hwameistor/pull/679)
- **新增** UI 应用 Label [Issue #710](https://github.com/hwameistor/hwameistor/pull/710)

#### 优化

- **新增** 磁盘的已使用容量 [Issue #681](https://github.com/hwameistor/hwameistor/pull/681)
- **优化** 当未发现可用磁盘时，跳过打分机制 [Issue #724](https://github.com/hwameistor/hwameistor/pull/724)
- **设置** DRDB 端口默认为 43001 [Issue #723](https://github.com/hwameistor/hwameistor/pull/723)

## 2023-1-30

### v0.8.0

#### 优化

- **优化** 中文文档
- **优化** value.yaml 文件
- **更新** Roadmap
- **优化** 当安装失败时，设置默认的失败策略

## 2022-12-30

### v0.7.1

#### 新功能

- **新增** Hwameistor DashBoard UI，可展现存储资源、存储节点等使用状态
- **新增** 界面管理 Hwameistor 存储节点、本地磁盘、迁移记录
- **新增** 存储池管理功能，支持界面展现存储池基本信息，及存储池对应节点信息
- **新增** 本地卷管理功能 ，支持界面执行数据卷迁移、高可用转换

#### 优化

- **优化** 数据迁移前不必要的日志，并规避其他 Namespace 下的 Job 执行影响
