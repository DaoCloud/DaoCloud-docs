# PostgreSQL Release Notes

本页列出 PostgreSQL 数据库的 Release Notes，便于您了解各版本的演进路径和特性变化。

*[Mcamel-PostgreSQL]: Mcamel 是 DaoCloud 所有中间件的开发代号，PostgreSQL 是一种功能丰富的关系型数据库。

## 2024-05-31

### v0.11.0

- **新增** 删除任务时可以不删除远程备份
- **新增** 参数模板导入、导出功能
- **优化** 删除备份时可选是否删除 S3 中备份数据
- **优化** 支持批量修改实例参数
- **优化** 支持配置从节点的同步个数

## 2024-04-30

### v0.11.0

- **优化** 删除备份的时候，可以选择删除在 s3 里的备份数据
- **优化** 增加命名空间配额的提示

## 2024-03-31

### v0.10.0

- **新增** 参数模板管理
- **新增** 支持通过模板创建 MongoDB 实例
- **修复** 配置访问设置的注释无效的问题

## 2024-01-31

### v0.9.0

#### 优化

- **优化** 在全局管理中增加 PostgreSQL 版本展示

## 2023-12-31

### v0.8.0

- **优化** 监控面板支持中文
- **修复** 创建实例时部分输入框填写特殊字符的校验未生效的问题

## 2023-11-30

### v0.7.0

- **新增** Mcamel-PostgreDB 支持访问白名单设置
- **新增** 支持记录操作审计日志
- **优化** 实例列表未获取到列表信息时的提示

## 2023-10-31

### v0.6.0

- **新增** 离线升级
- **新增** 实例重启功能
- **新增** 纳管外部实例
- **修复** Pod 列表展示地址为 Host IP
- **修复** cloudshell 权限问题

## 2023-08-31

### v0.5.0

- **优化** KindBase 语法兼容
- **优化** operator 创建过程的页面展示

## 2023-07-31

### v0.4.0

- **新增** 备份管理能力
- **优化** 监控图表，去除干扰元素并新增时间范围选择
- **修复** 监控图表部分 Panel 无法展示的问题

## 2023-06-30

### v0.3.0

- **新增** 对接全局管理审计日志模块
- **优化** 监控图表，去除干扰元素并新增时间范围选择

## 2023-04-27

### v0.1.2

- **新增** __Mcamel-PostgreSQL__  UI 模块上线，支界面化管理
- **新增** 安装 __Mcamel-PostgreSQL__  PgAdmin 离线镜像版本能力
- **新增** __Mcamel-PostgreSQL__  PgAdmin 支持 LoadBalancer 类型
- **优化** __Mcamel-PostgreSQL__  在 IPv6 的情况下 Exporter 没有权限连接到 PostgreSQL
- **优化** __Mcamel-PostgreSQL__  调度策略增加滑动按钮

## 2023-04-20

### v0.1.1

- **新增** __Mcamel-PostgreSQL__  支持 快速启动 PostgreSQL 集群
- **新增** __Mcamel-PostgreSQL__  支持 ARM 环境下部署
- **新增** __Mcamel-PostgreSQL__  支持 自定义角色
- **新增** __Mcamel-PostgreSQL__  支持 PostgreSQL 生命周期管理的后端接口
- **新增** __Mcamel-PostgreSQL__  支持 查看日志
- **新增** __Mcamel-PostgreSQL__  支持 PostgreSQL 15
- **新增** __Mcamel-PostgreSQL__  支持 PostgreSQL UI 管理界面

## 2023-03-29

### v0.0.2

- **新增** __Mcamel-PostgreSQL__  支持 PostgreSQL 实例创建
