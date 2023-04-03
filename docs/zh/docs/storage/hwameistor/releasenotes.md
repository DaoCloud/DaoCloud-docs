# Hwameistor Release Notes

本页列出 Hwameistor 相关的 Release Notes，便于您了解各版本的演进路径和特性变化。

## 2023-3-30

### v0.9.2

#### 优化

- **新增** UI relok8s。

### v0.9.1

#### 优化

- **新增** Volume Status 监控。[#741](https://github.com/hwameistor/hwameistor/pull/741)
- **修复** Local Storage 部署参数。[#742](https://github.com/hwameistor/hwameistor/pull/742)

### v0.9.0

#### 新功能

- **新增** 磁盘 Owner。[#681](https://github.com/hwameistor/hwameistor/pull/681)
- **新增** Grafana DashBoard。 [#733](https://github.com/hwameistor/hwameistor/pull/733)
- **新增** Operator 安装方式，安装时自动拉取 UI  。[#679](https://github.com/hwameistor/hwameistor/pull/679)
- **新增** UI 应用 Label。[#710](https://github.com/hwameistor/hwameistor/pull/710)

#### 优化

- **新增** 磁盘的已使用容量。[#681](https://github.com/hwameistor/hwameistor/pull/681)
- **优化** 当未发现可用磁盘时，跳过打分机制。 [#724](https://github.com/hwameistor/hwameistor/pull/724)
- **设置** DRDB 端口默认为 43001。[#723](https://github.com/hwameistor/hwameistor/pull/723)



## 2023-1-30

### v0.8.0

#### 优化

- **优化** 中文文档。
- **优化** value.yaml 文件。
- **更新** Roadmap。
- **优化**：当安装失败时，设置默认的失败策略。

## 2022-12-30

### v0.7.1

#### 新功能

- **新增** Hwameistor DashBoard UI，可展现存储资源、存储节点等使用状态。

- **新增** 界面管理 Hwameistor 存储节点、本地磁盘、迁移记录。

- **新增** 存储池管理功能，支持界面展现存储池基本信息，及存储池对应节点信息。

- **新增** 本地卷管理功能 ，支持界面执行数据卷迁移、高可用转换。

#### 优化

- **优化** 数据迁移前不必要的日志，并规避其他 Namespace 下的 Job 执行影响。
