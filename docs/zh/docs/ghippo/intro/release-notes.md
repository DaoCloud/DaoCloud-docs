# 全局管理 Release Notes

本页列出全局管理各版本的 Release Notes，便于您了解各版本的演进路径和特性变化。

## 2022-12-30

### v0.13.2

#### 修复

- 界面补充了缺少权限说明的英文文案
- 修复数据库表更新时，可能因为数据库编码导致报错

## 2022-12-28

### v0.13.0

#### 新功能

- 支持在 DCE5.0 前面部署一个国密网关, 并用国密浏览器来访问 DCE5.0
- 在 helm values 里设置开关, 可以一键开关 istio sidecar 功能
- 工作空间与层级增加 Workspace and Folder Owner 角色
- 拥有 Workspace/Folder Admin 和 Kpanda Owner 权限的用户才可进行资源绑定
- 对所用的库，进行开源 License 扫描
- 用户列表新增 `状态` 列
- 对内提供离线安装文档
- SDK 单元测试达 65%
- 界面支持发送测试邮件和无账号密码邮件服务器
- 界面支持对不符合系统要求的用户名进行提示

#### 优化

- Ghippo 鉴权代码优化(减少内存使用量)
- 前端界面低网络情况下预加载机制优化

#### 修复

- 修复 OpenAPI cycle 为必填参数问题, 修复后为可选参数

## 2022-11-30

### v0.12.1

#### 优化

- 通过 CI 自动构建纯离线包
- 优化 GHippo 升级文档

## 2022-11-28

### v0.12.0

#### 新功能

- 资源组里的 `模块` 改为 `来源`
- SDK 提供 Workspace 和 Resource 的绑定变化通知
- 完整对接 Insight metrics 和 otel tracing(加入 keycloak 和 db 链路)
- Keycloak 改成 Quarkus 架构
- Keycloak 镜像升级成 20.0.1 版本

#### 优化

- 重构导出审计日志 http 接口为 gprc stream 接口
- SDK 内存使用量优化, 峰值减少 50%
- 审计日志部分代码优化
- e2e 的 kind 镜像切到 1.25
- 提高资源使用效率到 40% 以上

#### 修复

- 修复强绑定集群问题
- 修复配置身份提供商界面选择 `Client secret sent as basic auth` 没有保存到 keycloak 里的问题

## 2022-11-01

### v0.11.2

#### 修复

- 关闭资源组绑定集群功能
- 修复无工作空间时无法创建工作空间问题

## 2022-10-28

### v0.11.0

#### 新功能

- 给第三方应用提供接口在 Keycloak 创建 SSO 对接 Client
- 支持 Mysql8
- 对接 Insight(metrics, log, otel tracing)
- License 模块名支持 i18n
- 支持一个 License 中可以包含多个 GProduct
- 资源组新增绑定集群类型资源
- 资源组列表增加“模块”字段
- 资源组列表增加已绑定标识
- 资源绑定接口支持 Registry 资源种类。

#### 优化

- 资源种类改枚举
- GProduct license 是否需要灌入变量改为可配
- 优化 CICD 流程

#### 修复

- 修复已经删除的集群依然存在问题
- 修复 keycloak jwks 变化后没有重置 istio 缓存问题
- 修复用户组创建时间零值问题
- 修复访问密钥`最后使用时间`字段在未使用时返回空字符

## 2022-09-28

### v0.10.0

#### 新功能

- 支持登录
- 支持忘记密码
- 支持站内信增删改查功能
- 支持 SMTP 设置邮件服务器
- 支持顶部导航栏获取查询
- 支持顶部导航栏更新
- 支持用户角色权限管理 CRUD
- 工作空间 -> 生命周期管理（创建/编辑/删除/查看/列表）
- 工作空间 -> 层级关系管理（绑定/列表）
- 工作空间 -> 工作空间与资源关系管理（绑定/解绑/列表）
- 工作空间 -> 工作空间和角色和用户（组）关系管理（绑定/解绑/列表）（API/SDK）
- 工作空间 -> 鉴权（API/SDK）
- 工作空间 -> GProduct 资源名字注册
- 关于 -> 产品版本（创建/编辑/删除/查看/列表）
- 关于 -> 开源软件（列表/初始化）
- 关于 -> 技术团队（列表/初始化）
- 许可证 -> 生命周期管理（创建/编辑/删除/查看/列表）
- 许可证 -> 获取 ESN 序列号
- 许可证 -> 未灌入或错误情况处理
- 工作空间 -> 资源配额管理（创建/编辑/删除/查看/列表/计算已分配）
- 工作空间 -> GProduct 资源配额注册
- 用户与访问控制 -> 鉴权（APIServer/SDK）
- 审计日志 -> 展示（查看/列表/清理设置/导出）
- 审计日志 -> 批量插入
- 身份提供商 -> 对接 LDAP -> 用户/用户组同步设置（创建/编辑/删除/查看/同步）
- 平台设置 -> 安全策略 -> 密码策略设置
- 个人中心 -> 访问密钥(创建/编辑/删除/查看/列表)
- 审计日志 -> 全局管理操作插入审计日志
- 审计日志 -> 对接 Insight 来收集审计日志
- 平台设置 -> 安全策略 -> 账号锁定策略
- 平台设置 -> 安全策略 -> 浏览器关闭策略
- 身份提供商 -> 对接 IDP (OIDC 协议)
- 工作空间 -> 共享集群权限管理
- 工作空间 -> 共享集群配额管理 -> 存储
- 平台设置 -> 顶部导航外观定制 -> 重置功能
- 平台设置 -> 安全策略 -> 会话超时策略
- 审计日志 -> 自动清理功能
- 平台设置 -> 安全策略-账号锁定策略
- 平台设置 -> 顶部导航外观定制-还原功能
- 平台设置 -> 登录页外观定制-还原功能
- 产品导航 -> 首页仅对 admin 用户展示
- 工作空间 -> 用户仅能查看有权限的 workspace & folder 树状结构
- Keycloak 高可用
- 邮件服务器配置 -> 支持 Insight 和应用工作台发送邮件
- 满足 Helm 规范，支持安装器和离线化
- 审计日志 -> 数据库自动创建和合并分区
- 支持 ARM64 架构
- 支持 https
- 登录 -> 背景 theme 支持动画
- 授权鉴权 -> 给前端提供当前登录用户的权限列表
- 关于 -> 软件版本 -> 模块支持中文名
- 添加整体双语文档站结构及主要内容
- - 文档站新增页面：[什么是全局管理](what.md)、[常见术语](../intro/glossary.md)、[功能总览](features.md)、[快速入门/创建用户和授权](../user-guide/access-control/user.md)、[什么是用户访问和控制](../user-guide/access-control/iam.md)、[用户](../user-guide/access-control/user.md)、[创建用户组并授权](../user-guide/access-control/group.md)、[用户组](../user-guide/access-control/group.md)、[登录](../user-guide/login.md)、[密码重置](../user-guide/password.md)、[全局管理角色](../user-guide/access-control/global.md)、[资源管理（按工作空间）](../user-guide/workspace/ws-best-practice.md)、[资源管理（按角色）](../user-guide/workspace/quota.md)、[身份提供商](../user-guide/access-control/idprovider.md)、[邮件服务器设置](../user-guide/platform-setting/mail-server.md)、[外观定制](../user-guide/platform-setting/appearance.md)、[LDAP](../user-guide/access-control/ldap.md)、[OIDC](../user-guide/access-control/oidc.md)、[关于平台](../user-guide/platform-setting/about.md)、[审计日志](../user-guide/audit-log.md)、[访问密钥](../user-guide/personal-center/password.md)、[语言设置](../user-guide/personal-center/language.md)、[安全设置](../user-guide/personal-center/security-setting.md) 等文档

#### 优化

- 授权鉴权 -> 提供一个 job 来确保 db 和 cr 的同步
- LDAP -> 配置错误检查
- 各功能操作反馈和提示语报错支持中英文
- 工作空间及层级 -> 删除前对是否存在子资源进行检查
- 优化 keycloak jvm 参数
- 通过 mockery 框架简化 mock
