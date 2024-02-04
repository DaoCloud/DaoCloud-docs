# Hwameistor Release Notes

本页列出 Hwameistor 相关的 Release Notes，便于您了解各版本的演进路径和特性变化。

## 2024-01-31

### v0.14.1

#### 优化

- __优化__ 忽略失败策略时会跳过一些定义了SC 但并没 SC 实例的卷
- __优化__ 使用前检查本地磁盘是否存在
- __优化__ 更新快照客户端
- __优化__ Hwameictl 命令行支持快照
- __优化__ Hwameictl 命令行支持快照添加集群

#### 修复

- __修复__ 修复 getnode api 的问题
- __修复__ 修复 ctl disk_list 的问题
- __修复__ 修复快照控制错误

## 2023-12-31

### v0.14.0

#### 优化

- __优化__ 移除无意义的 poolType 的使用
- __优化__ 添加 VolumeSnapshotClass
- __优化__ Hwameictl 命令行支持了 `snapshot` 参数

#### 修复

- __修复__ Volume Group 始终保持与组中所有卷的可访问性一致
- __修复__ 清理 localvolumemigrate 副本时出现 pending 的错误
- __修复__ 索引器设置失败时添加退出系统语句
- __修复__ StorageNodePoolDiskGet 获取 localdisk 错误的问题
- __修复__ 用户删除 pvc 但未创建 pv 时的音量泄漏

## 2023-11-30

### v0.13.3

#### 新功能

- __新增__ 支持卷克隆
- __新增__ 当快照被发现时会延迟卷删除
- __新增__ 根据源卷可访问性过滤节点

#### 优化

- __优化__ 仅在磁盘可用时记录磁盘声明事件

#### 修复

- __修复__ 在提交任务之前过滤 replicaSnapRestoreName
- __修复__ LocalVolumeConvert 状态转换错误
- __修复__ 索引器添加失败时退出
- __修复__ 迁移卷时使用存储节点 IP
- __修复__ 取消发布后清理副本
- __修复__ 修复 `apiserver getnodedisk` 错误并添加 set-diskowner api

## 2023-10-30

### v0.13.1

#### 新功能

- __新增__ 适配 Kubernetes v1.28 版本

- __新增__ LVM 数据卷快照功能

#### 优化

- __优化__ Hwameistor Operator 新增组件资源配置
- __优化__ 快照恢复超时时间调整
- __优化__ 提高 LDM 默认日志等级

## 2023-8-30

### v0.12.1

#### 新功能

- __新增__ 支持`ext`文件系统
- __新增__ Local Disk 新特性参数
- __新增__ 字段 记录 设备历史信息
- __新增__ SN/ID Path 识别 磁盘
- __新增__ 磁盘自动扩容功能
- __新增__ 系统资源审计功能，如： 集群，存储节点，磁盘，数据卷等

#### 修复

- __修复__ LocalStoragePool 节点的 NVME 磁盘显示问题
- __修复__ 迁移操作丢失副本状态问题
- __修复__ 当 Disk Owner 为空时，磁盘不允许分配问题
- __修复__ Failover功能 `deploy`,`Makefile` 等问题

## 2023-7-05

### v0.11.1

#### 新功能

__新增__ 支持自动检测 `cgroup` 版本

## 2023-6-25

### v0.11.0

#### 新功能

- __新增__ 实现 IO 限制或 QoS

- __新增__ 使用 /virtual/ 检测来识别虚拟块设备

#### 优化

- __修复__ 存储池创建时间字段不一致问题

## 2023-5-26

### v0.10.3

#### 优化

- __优化__ Helm 模板中权限功相关内容

## 2023-5-25

### v0.10.2

#### 优化

- __优化__ Node Name `.` 自动转成 `-` 问题，影响 LDM 心跳检测
- __新增__ Admin 权限功能

## 2023-5-17

### v0.10.0

#### 优化

- __新增__ 识别并设置本地磁盘 Manager Owner 信息
- __优化__ 当接收到 移除时间，将磁盘状态标记为 'inactive'
- __优化__ 磁盘 Smart 指标仪表盘
- __新增__ 本地存储池
- __优化__ UI 组件状态展示
- __优化__ 分离磁盘分配和磁盘状态更新过程
- __优化__ 将Exportor端口重命名为 http-metrics
- __优化__ 在exporter service中添加端口名称

#### 缺陷

- __修复__ LD bound，但是LSN中没有容量的问题
- __修复__ Metrics 端口监听问题
- __修复__ May occur `not found`的问题
- __修复__ Helm 中UI tag 的问题

### v0.9.3

#### 优化

- __优化__ 在使用阶段填充磁盘所有者信息
- __优化__ udev事件触发时合并磁盘自身属性
- __优化__ 给svc添加标签
- __优化__ 分离磁盘分配和磁盘状态更新过程
- __优化__ 将Exportor端口重命名为 http-metrics
- __优化__ 在exporter service中添加端口名称

#### 缺陷

- __修复__ LD bound，但是LSN中没有容量的问题
- __修复__ Metrics 端口监听问题
- __修复__ May occur `not found`的问题
- __修复__ Helm 中UI tag 的问题

## 2023-3-30

### v0.9.2

#### 优化

- __新增__ UI relok8s

### v0.9.1

#### 优化

- __新增__ Volume Status 监控 [Issue #741](https://github.com/hwameistor/hwameistor/pull/741)
- __修复__ Local Storage 部署参数 [Issue #742](https://github.com/hwameistor/hwameistor/pull/742)

### v0.9.0

#### 新功能

- __新增__ 磁盘 Owner [Issue #681](https://github.com/hwameistor/hwameistor/pull/681)
- __新增__ Grafana DashBoard [Issue #733](https://github.com/hwameistor/hwameistor/pull/733)
- __新增__ Operator 安装方式，安装时自动拉取 UI [Issue #679](https://github.com/hwameistor/hwameistor/pull/679)
- __新增__ UI 应用 Label [Issue #710](https://github.com/hwameistor/hwameistor/pull/710)

#### 优化

- __新增__ 磁盘的已使用容量 [Issue #681](https://github.com/hwameistor/hwameistor/pull/681)
- __优化__ 当未发现可用磁盘时，跳过打分机制 [Issue #724](https://github.com/hwameistor/hwameistor/pull/724)
- **设置** DRDB 端口默认为 43001 [Issue #723](https://github.com/hwameistor/hwameistor/pull/723)

## 2023-1-30

### v0.8.0

#### 优化

- __优化__ 中文文档
- __优化__ value.yaml 文件
- **更新** Roadmap
- __优化__ 当安装失败时，设置默认的失败策略

## 2022-12-30

### v0.7.1

#### 新功能

- __新增__ Hwameistor DashBoard UI，可展现存储资源、存储节点等使用状态
- __新增__ 界面管理 Hwameistor 存储节点、本地磁盘、迁移记录
- __新增__ 存储池管理功能，支持界面展现存储池基本信息，及存储池对应节点信息
- __新增__ 本地卷管理功能 ，支持界面执行数据卷迁移、高可用转换

#### 优化

- __优化__ 数据迁移前不必要的日志，并规避其他 Namespace 下的 Job 执行影响
