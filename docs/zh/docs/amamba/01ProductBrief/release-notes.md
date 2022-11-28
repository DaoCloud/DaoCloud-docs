# 应用工作台 Release Notes

本页列出应用工作台的 Release Notes，便于您了解各版本的演进路径和特性变化。

## v0.9

发布日期：2022-11-18

- **新增** jenkins-agent 镜像持续发布
- **新增** 添加了使用中间件的数据库的选项
- **修复** rollout 在不同 workspace 下无法区分的问题
- **修复** gitops 模块未鉴权的问题
- **修复** 偶现的 pipeline step 状态不正确的问题
- **修复** 获取 helmchart 的 description 为空的问题
- **修复** 创建 namespace 没有校验 storage 的问题
- **修复** list argocd repository 出现的无序和分页问题的修复
- **修复** from-jar 上传超过 32M 文件失败的问题的修复
- **修复** 获取 pipeline 日志的时候如果日志量过大则无法获取全量日志的问题
- **优化** 获取 rollout 镜像列表，应用组列表，原生应用列表等性能优化
- **优化** from-jar 用到的 image 不再写死在源代码中，通过 env 的方式传递，并保证安装器能正确获取
- **升级** jenkins 从 2.319.1 升级到 2.346.2,kubernetes plugin 升级到 3734.v562b_b_a_627ea_c，相关的 plugins 也作了升级

## v0.8

发布日期：2022-11-04

### API

- **新增** 获取和更新 application json 的接口
- **新增** argocd application 的创建、列表、查询、修改和删除接口
- **新增** 获取持续部署健康状态和同步状态的接口
- **新增** 同步 argocd application 的接口
- **新增** helm release 接口
- **新增** 同步 workspace 下的资源到 argocd 中，包括 workspace,cluster 和 namespace
- **新增** 查询 Workload 支持 appgroup 的匹配 && workload name 的模糊匹配
- **新增** 创建和更新应用时支持对接微服务相关功能，包括服务注册，服务治理，指标监控和链路追踪
- **新增** 列出 workspace 绑定的 namespace 接口支持搜索和排序
- **修复** 创建 Application 失败之后，新增了回滚功能
- **修复** from-git、from-jar 可以在前端不传递 imageTag 字段
- **修复** 在全新的 workspace 创建 credential 失败
- **修复** from-jar 和 from-git 的 dag 图在没有 registry credential 的情况下部分无法显示的问题
- **修复** 流水线里含有空的 cron 字符串的时候，空指针错误
- **修复** 创建 Application 之后,去 pipeline 模块进行更新，如果名字超出限制会报错的 bug
- **修复** 创建 namespace 失败但是没有回滚删除的问题
- **修复** 获取运行后某个 step 的日志，在某些特殊情况下，step_id 非整形的处理
- **修复** 修改流水线名字的时候，旧名字和新名字一样的时候，页面显示修改失败的处理
- **修复** image 里含有端口号的时候，校验误认为是 image-tag 的修复
- **优化** argocd 的初始化认证和连接

### 基础设施

- **新增** arm 架构的基础镜像持续发布
- **修复** 更改 jenkins agent 可以拉起的 pod 数量为 100，更改 connectTimeout 和 readTimeout 2 个超时参数
- **新增** 添加 jenkins 部署在非 Global 集群的文档
- **新增** 添加非 docker 运行时的方案文档

## v0.7

发布日期：2022-9-28

### API

- **新增** 支持在 containerd 运行时的集群上运行流水线
- **新增**  worksapce 角色操作鉴权
- **新增** 添加列出应用组的接口
- **新增** 添加创建 ResourceQuota 的接口
- **新增** 添加获取集群插件安装信息的接口
- **新增** 添加获取 rollout 的 container 镜像的接口
- **新增** 增加 metircs 接口，提供 go gc 和 prometheus 默认的指标，以及 jenkins event 的 counter
- **新增** 支持对包含多个端口的 workload 进行灰度发布
- **新增** 创建 application 的时候 svc 支持 NodePort 和 Loadbalance
- **修复** 创建命名空间时报 Namespace 不存在，ResourceQuota 不存在的错误导致创建 Namespace 失败
- **修复** 选择 workspace 关联集群和命名空间错误

### 基础设施

- **新增** 添加工作空间鉴权以及部署资源所在 cluster、namespace 鉴权
- **修复** image 字段只校验了长度，没有按照需求校验
- **新增** 部署的时候安装 argo cd
- **优化** amamba charts 安装完成提示语优化
- **优化** amamba charts 离线安装优化

## v0.6

发布日期：2022-9-21

### API

- **新增** 金丝雀发布列表、更新和删除接口
- **新增** 金丝雀详情信息页
- **新增** 新增 core apigroup，将 workspace 和 namespace 相关的接口移至该 group 下
- **新增** helm 创建及相关接口（获取集群的 registry，指定 chart 的详情和版本信息）
- **新增** 流水线，流水线运行记录搜索
- **修复** 修改命名空间 label 时报错配额检查错误

### API 服务

- **新增** 通过 chart 安装时会一并安装 GProductNavigator 和 GProductPorxy 等 CR
- **优化** 优化 XML 的序列化与反序列化，gorm 的查询语法，pageutil 模型统一化

### 基础设施

- **新增** 凭证 CRUD 和流水线运行 CRUD 接口的 E2E
- **优化** 优化 workload 列表的实现，性能大幅提升
- **新增** 更新应用工作台简介、快速创建流水线、使用图形化编辑流水和功能总览产品文档

## v0.5

发布日期：2022-8-21

- **新增** 添加删除原生应用的接口
- **新增** 获取 secretReference 列表、验证 secret、镜像仓库是否正确、获取镜像 tag 列表
- **新增** 列出开启了灰度发布的 deployment 名称
- **新增** 添加命名空间相关接口，包括列出命名空间列表，创建，更新，删除命名空间
- **新增** 绑定命名空间至 workspace
- **新增** 列出所有的非 grpc-gateway 的 URL
- **新增** 运行流水线的 http 接口，支持所有 build parameter，包括文件参数
- **移除** 因为新增运行流水线的 http 接口,运行流水线的 gprc-gateway 接口被移除
- **新增** 当创建的 rollout 没有指定的内置分析模板时自动安装
- **新增** 流水线添加 webhook 的触发方式
- **新增** workload 跳转 kpanda
- **修复** 重命名流水线时流水线运行记录未修改
- **修复** 修改 mysql 的默认时区为东八区

## v0.4

发布日期：2022-7-25

- **新增** 基于 git 创建应用、生成流水线
- **新增** 基于 jar 包创建应用、生成流水线
- **新增** 在运行到需要审核的步骤时，指定的用户可以进行审核：批准/取消
- **新增** 流水线创建字段的校验
- **新增** 前端页面获取 jenkinsjson，修改 jenkinsjson 后保存到 db，以及 jenkinsfile 和 jenkinsjson 修改的同步
- **新增** 添加列出工作负载的 API 接口
- **新增** 进入流水线运行记录详情页，点击`运行报告` tab 页，查看任务状态
- **优化** 当流水线设置不允许并发构建且存在运行中的流水线时返回错误
- **优化** 获取流水线参数接口性能优化至 ms 级
- **优化** 使用 `Generic Event Plugin` 插件实现流水线配置及流水线运行状态实时同步

## v0.3

发布日期：2022-7-08

- **新增** 基于镜像创建应用、列出所有原生的工作负载的 API 接口
- **新增** 支持 kubeconfig、访问令牌的密钥创建
- **新增** 提供可见 workspace 列表，创建 ns 和 ns 列表的 API
- **新增** 流水线创建支持构建设置、触发器设置（定时触发和代码源触发）、基于 git 仓库 jenkinsfile 的单分支流水线、Jenkinsfile 校验
- **新增** 流水线运行记录详情、全量和分步骤日志、支持删除、重放和取消操作
- **新增** E2E 测试覆盖率自动计算、持续性能测试报告、自动更新依赖
