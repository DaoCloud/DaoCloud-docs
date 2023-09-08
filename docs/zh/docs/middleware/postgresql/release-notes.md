# PostgreSQL Release Notes

本页列出 PostgreSQL 数据库的 Release Notes，便于您了解各版本的演进路径和特性变化。

## 2023-08-31

### v0.5.0

#### 优化

- **优化** KindBase 语法兼容。
- **优化** operator 创建过程的页面展示。

## 2023-07-31

### v0.4.0

#### 新增

- **新增** 备份管理能力。

#### 优化

- **优化** 监控图表，去除干扰元素并新增时间范围选择

#### 修复

- **修复** 监控图表部分 Panel 无法展示的问题。

## 2023-06-30

### v0.3.0

#### 新功能

- **新增** 对接全局管理审计日志模块

#### 优化

- **优化** 监控图表，去除干扰元素并新增时间范围选择

## 2023-04-27

### v0.1.2

#### 新功能

- **新增** `Mcamel-PostgreSQL` UI 模块上线，支界面化管理
- **新增** 安装 `Mcamel-PostgreSQL` PgAdmin 离线镜像版本能力。
- **新增** `Mcamel-PostgreSQL` PgAdmin 支持 LoadBalancer 类型。

#### 优化

- **优化** `Mcamel-PostgreSQL` 在 IPV6 的情况下 Exporter 没有权限连接到 PostgreSQL
- **优化** `Mcamel-PostgreSQL` 调度策略增加滑动按钮

## 2023-04-20

### v0.1.1

### 新功能

- **新增** `Mcamel-PostgreSQL` 支持 快速启动 PostgreSQL 集群
- **新增** `Mcamel-PostgreSQL` 支持 ARM 环境下部署
- **新增** `Mcamel-PostgreSQL` 支持 自定义角色
- **新增** `Mcamel-PostgreSQL` 支持 PostgreSQL 生命周期管理的后端接口
- **新增** `Mcamel-PostgreSQL` 支持 查看日志
- **新增** `Mcamel-PostgreSQL` 支持 PostgreSQL 15
- **新增** `Mcamel-PostgreSQL` 支持 PostgreSQL UI 管理界面

## 2023-03-29

### v0.0.2

### 新功能

- **新增** `Mcamel-PostgreSQL` 支持 PostgreSQL 实例创建
