# DCE 5.0 社区版 Release Notes

![DCE 5.0 ](images/rn01.png)

由于 DCE 5.0 社区版 release notes 详细的内容比较庞杂，所以本章将按以下模块列出一些主要的特性变化：

- [全局管理](../ghippo/01ProductBrief/WhatisGhippo.md)
- [容器管理](../kpanda/03ProductBrief/WhatisKPanda.md)
- [CloudTTY](../community/cloudtty.md)
- [Clusterpedia](../community/clusterpedia.md)
- [Kubean](../community/kubean.md)
- [KLTS](../community/klts.md)
- [SpiderNetwork](../community/spiderpool.md)
- [HwameiStor](../community/hwameistor.md)

## 容器管理

以下 release notes 可能会出现 kpanda 字样，kpanda 是容器管理模块的内部开发代号。

### 基础设施

**新增** `kpanda`增加 release-notes 生成功能

**改进** 修改 e2e 为调用 SDK 的方式

**改进** ginkgo 组件升级到 ginkgoV2

**改进** 优化已有 case，提升性能和通过率

**改进** 优化 e2ecase 提升稳定性

**改进** 更新测试用例文档

**新增** `kpanda`增加 release-notes 生成功能

**新增** `helm install` 后打印 helm notes

**新增** 新增 PutNodeTaints，PutNodeLabels 等接口 e2e 测试

**新增** 新增 configmap，namespace，secret 等接口 e2e 测试

**新增** secret 等接口 e2e 测试

**新增** 新增 BeforeSuit 检查 clusterpedia 是否 ready

**改进** 优化轮询方法,增加重启 clusterpedia

**新增** 新增 markdown 详情测试用例

**新增** 新增 getclusterkubeconfig、validatekubeconfig 等接口 e2e 测试用例

**新增** 新增 k8s 兼容性 e2e 测试

**新增** 新增 namespace 场景测试用例

**新增** 新增 deployment 的 create,list,get 接口

**新增** 新增 ingress case

**新增** 新增 Secrets 等接口 e2e 用例

**新增** 新增自动扫描 gomod 文件中依赖库版本,并官方最新发布版本做对比

**新增** 新增 job & cron job 等接口测试用例

**优化** 拆分 kpanda 的安装脚本

**改进** 修复部分 e2ecase 常见问题

**改进** pr e2e 时减少子集群部署数量

**改进** 更新维护 openshift 接入测试

**新增** 拆分测试 e2e 与 pr e2e

**新增** 更新 e2e markdown 用例

**新增** 新增 crd 相关 e2e 测试

**新增** 新增 openshift 接入测试

**新增** 新增 hpt 相关 e2e 测试

**新增** 新增 deployment restart 等 e2e 测试

**新增** 新增 ListClusterEvents 等 e2e 测试

**新增** 新增删除 job 等 e2e 测试

**新增** e2e 鉴权模式改为 RBAC ,新增 getConfigMap 权限测试

**改进** 删除合并 e2e 多余的文件

**改进** 修复 listpodsbyservice 测试用例

**改进** 修复 redis config yaml 导致的 e2e 角色权限问题

**改进** 修复 k8s1.18 兼容性问题的 case

**新增** 新增 aliyun ack 兼容性 e2e 测试

**新增** 更新接入兼容性 e2e 测试

**新增** 新增 kind 创建集群失败重试

**新增** 新增 e2e 测试

### API

**新增** `kpanda`增加 configmap CRUD

**新增** `kpanda`支持工作负载全生命周期管理

**新增** CRD、CR 的 crud 支持

**新增** `kpanda`可安装在任意 namespace 下

**优化** `listWorkload`、`listAllWorkload`和`listClusterWorkload` 三个接口进行拆分，细分到具体的 workload kind

**优化** `kpanda` engine 层 get 请求走 clusterpedia

**优化** `kpanda` proto 文件注释补全

**新增** `kpanda`增加节点查看、编辑 yaml 功能

**新增** `kpanda`支持节点列表根据状态筛选功能

**新增** `kpanda`支持 Job、CronJob、Ingress、Pod 事件列表

**新增** `kpanda`新增支持 HPA CRUD

**新增** `kpanda`新增支持 插件检测 controller

**新增** `kpanda`新增支持 pvc storageClass CRUD

**新增** `kpanda`新增支持 volume snapshot CRUD

**新增** `kpanda`所有资源增加名称模糊搜索功能

**新增** `kpanda`支持配额管理功能

**新增** `kpanda`新增 all namesapces 的 list pvc 和快照 接口

**新增** `kpanda`新增支持 返回 pvc list 中的 pvc 是否支持快照，和扩容

**修复** `kpanda`clustersummary 空指针问题

**优化** `kpanda`对 insight 的依赖改为弱依赖

**新增** `kpanda` 新增 CRD 和 CR 详情

**新增** `kpanda` 新增修改集群设置的 api

**新增** `kpanda` ListCluster AND GetCluster 接入 clustersetting

**新增** `kpanda` 新增 支持 集群状态检索

**新增** `kpanda` 新增 支持 label selector 和 field selector

**修复** `kpanda` 修复 global cluster 重复显示

**修复** `kpanda` 修复 ListClusterRoleBindings 根据 name 查询返回为空

**修复** `kpanda` 修复修改集群接入的 kube-config 后，不能够生效

**修复** `kpanda` 修复 global cluster secret 不刷新的问题

**修复** `kpanda` 用户获取集群 config 信息，用户填入什么信息，获取什么信息，不在初始化

**新增** `kpanda` helm repo 支持设置自动刷新频率

**新增** `kpanda` 通过 annotation 区分来自 addon、应用商店、用户手动 helm install 的 release

**新增** `kpanda` addon 安装支持 --atomic --debug 参数

**新增** `kpanda` 集群概览展示指定 helmRepo 下安装的 helmRelease

**新增** `kpanda` 新增 dual stack 网络参数支持

**新增** `kpanda` 新增获取用户组接口

**新增** `kpanda` 新增获取用户接口

**新增** `kpanda` 针对不同版本 k8s 进行兼容

**新增** `kpanda` 新增重启 Job 接口

**优化** `kpanda` list pod 接口可以动态获取 pod 所属的工作负载

**优化** `kpanda` get cluster 接口可以动态获取网络模式

### api-service

**新增** `kpanda`增加权限管理 CRUD

**新增** `kpanda`新增 redis chart

**新增** `kpanda`新增 bindingsync controller

**新增** `kpanda`支持 rabc 精细化授权

**新增** `kpanda`支持 rabc 精细化鉴权

**新增** `kpanda`支持 AccessScopeList 精细化查询

**新增** 添加 `cloudshell` 的 helm 部署方式并集成到 `kpanda` 中

**新增** 添加 `cloudshell` 的 创建查询删除的 API

**新增** 使用 GProductProxy 的形式进行对 cloudshell 的 svc 进行负载

**新增** 支持多窗口显示和日志滚动

**新增** `kpanda`利用 fake clusterpedia 增加单元测试

**改进** 使用 cloudtty 的 virtualService 模式来暴露服务

**新增**  权限调整 有一个 ns 权限就要返回这个 cluster

**新增** `kpanda` 上报 cluster 和 namespace 信息到 CRD 中

**新增** `kpanda` 对接 ghippo 模块 API

**新增** `kpanda` watch workspace 变化信息给对应 workspace role 创建 RBAC

**修复** `kpanda`支持跨集群可见性搜索支持原生 sql 查询

**修复** `kpanda`修复 ListNamespaceSummary

**改进** 升级 cloudtty ，增加 readiness 的功能

**修复** `kpanda` 下载证书优化(支持集群 pod 外部访问)

**优化** `kpanda` 缩短打开 cloudshell 的时间

### work-api

**新增** 和前端对接按照 insight 的接口类型，新增 cpu 资源使用率，node 资源使用率，workload 资源使用率，pod 资源使用率 接口

**修复** BFF 中的 node 相关 clust 相关，pod 相关的接口中添加了 insight 的数据

**优化** 修复了 insight 的部分数据返回类型错误的 bug

**优化** insight 日志接口使用 kubesystem_id 作为查询 cluster 的 key

**优化** 添加了查询日志的 filter 过滤器

**优化** 修复了日志查询时不传入 workload 没有数据的问题

**优化** 修复了 node 的指标数据需要重复传入 node 的问题

### controller

**改进** 优化 egress，在 cluster 未就绪时不需要尝试分配 port

**新增** `kpanda` 将鉴权移至 grpc

**新增** `kpanda` 新增 bindingsync gc 逻辑

**新增** `kpanda` 将 namespace quota 上报 gproductresources

**新增** `kpanda` 新增 gproductresources gc 多余 ns 逻辑

## 全局管理

全局管理模块（开发代号 Ghippo）包含了用户、用户组、角色、权限等访问控制，具体特性变化如下：

**改进** 通过 mockery 框架简化 mock

**新增** 完成 user、login、group、等 e2e 测试

**新增** Ghippo 支持 OPA 权限管理

**新增** 工作空间 - 生命周期管理(创建/编辑/删除/查看/列表)

**新增** 工作空间 - 层级关系管理(绑定/列表)

**新增** 工作空间 - 工作空间与资源关系管理(绑定/解绑/列表)

**新增** 工作空间 - 工作空间和角色和用户(组)关系管理(绑定/解绑/列表)(API/SDK)

**新增** 工作空间 - 鉴权(API/SDK)

**新增** 工作空间 - GProduct 资源名字注册

**新增** 关于 - 产品版本(创建/编辑/删除/查看/列表)

**新增** 关于 - 开源软件(列表/初始化)

**新增** 关于 - 技术团队(列表/初始化)

**新增** 许可证 - 生命周期管理(创建/编辑/删除/查看/列表)

**新增** 许可证 - 获取 ESN 序列号

**新增** 工作空间 - 资源配额管理(创建/编辑/删除/查看/列表/计算已分配)

**新增** 工作空间 - GProduct 资源配额注册

**新增** 用户与访问控制 - 鉴权(APIServer/SDK)

**新增** 审计日志 - 展示(查看/列表/清理设置/导出)

**新增** 审计日志 - 批量插入

**新增** 身份提供商 - 对接 LDAP-用户/用户组同步设置(创建/编辑/删除/查看/同步)

**新增** 平台设置 - 安全策略-密码策略设置

**优化** 工作空间 - 代码架构调整

### API

**新增** Ghippo 登录页面更新配置接口

**新增** Ghippo 支持登录

**新增** Ghippo 支持忘记密码

**新增** Ghippo 支持站内信增删改查功能

**新增** Ghippo 支持 smtp 设置邮件服务器

**新增** Ghippo 支持顶部导航栏获取查询

**新增** Ghippo 支持顶部导航栏更新

**新增** Ghippo 支持 user role 权限管理 CRUD

## CloudTTY

CloudTTY 是「DaoCloud 道客」独立开发的开源项目，请参阅 [CloudTTY Release Notes](https://github.com/cloudtty/cloudtty/releases)。

## Clusterpedia

Clusterpedia 是「DaoCloud 道客」独立开发的开源项目，请参阅 [Clusterpedia Release Notes](https://github.com/clusterpedia-io/clusterpedia/releases)。

## Kubean

Kubean 是「DaoCloud 道客」独立开发的开源项目，请参阅 [Kubean Release Notes](https://github.com/kubean-io/kubean/releases)。

## KLTS

KLTS 是「DaoCloud 道客」独立开发的开源项目，请参阅 [KLTS Release Notes](https://github.com/klts-io/kubernetes-lts/releases)。

## Spiderpool

Spiderpool 是「DaoCloud 道客」独立开发的开源项目，请参阅 [Spiderpool Release Notes](https://github.com/spidernet-io/spiderpool/releases)。

## HwameiStor

HwameiStor 是「DaoCloud 道客」独立开发的开源项目，请参阅 [HwameiStor Release Notes](https://github.com/hwameistor/hwameistor/releases)。

## 文档站

**新增** GitLab 第一次文档站上线：容器管理、全局管理、文档站模板、产品文档站

**新增** GitLab 文档站按 feature 特性新编页面

**新增** DCE 5.0 社区版发版，所有 Scrum 文档迁移到 GitHub

**新增** 文档站编译器从 GitBook 迁移到 MkDocs

**新增** 部分英文页面
