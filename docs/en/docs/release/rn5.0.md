# DCE 5.0 社区版 Release Notes - 202209



2022 年 DCE 5.0 社区版发布，由于 release notes 详细的内容比较庞杂，所以本页按以下模块列出一些主要的特性变化：

- [容器管理](#容器管理)
- [全局管理](#全局管理)
- [CloudTTY](#cloudtty)
- [Clusterpedia](#clusterpedia)
- [Kubean](#kubean)
- [KLTS](#klts)
- [Spiderpool](#spiderpool)
- [HwameiStor](#hwameistor)

## 容器管理

以下 release notes 可能会出现 kpanda 字样，kpanda 是容器管理模块的内部开发代号。

### 基础设施

**新增** `kpanda` 增加 release-notes 生成功能

**改进** 修改 e2e 为调用 SDK 的方式

**改进** ginkgo 组件升级到 ginkgoV2

**改进** 优化已有 case，提升性能和通过率

**改进** 优化 e2ecase 提升稳定性

**改进** 更新测试用例文档

**新增** `kpanda` 增加 release-notes 生成功能

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

**改进** 修复 e2e 部署失败任然 job succeeded 的问题

**改进** 提升 pr 识别运行 e2e 精准度

**改进** 修复每日构建 benchmark 失败的问题

**改进** pr 识别 e2e 过滤 md 文件

**新增** 新增 quota 相关 e2ecase

### API

**新增** `kpanda` 增加 [configmap](../kpanda/07UserGuide/ConfigMapsandSecrets/UsedConfigMap.md) CRUD

**新增** `kpanda` 支持[工作负载全生命周期管理](../kpanda/07UserGuide/Workloads/CreateDeploymentByImage.md)

**新增** CRD、CR 的 crud 支持

**新增** `kpanda` 可安装在任意 namespace 下

**优化** `listWorkload`、`listAllWorkload` 和 `listClusterWorkload` 三个接口进行拆分，细分到具体的 workload kind

**优化** `kpanda` engine 层 get 请求走 [clusterpedia](../community/clusterpedia.md)

**优化** `kpanda` proto 文件注释补全

**新增** `kpanda` 增加[节点](../kpanda/07UserGuide/Nodes/AddNode.md)查看、编辑 yaml 功能

**新增** `kpanda` 支持节点列表根据状态筛选功能

**新增** `kpanda` 支持 Job、CronJob、Ingress、Pod 事件列表

**新增** `kpanda` 新增支持 HPA CRUD

**新增** `kpanda` 新增支持插件检测 controller

**新增** `kpanda` 新增支持 pvc storageClass CRUD

**新增** `kpanda` 新增支持 volume snapshot CRUD

**新增** `kpanda` 所有资源增加名称模糊搜索功能

**新增** `kpanda` 支持配额管理功能

**新增** `kpanda` 新增 all namesapces 的 list pvc 和快照接口

**新增** `kpanda` 新增支持返回 pvc list 中的 pvc 是否支持快照和扩容

**修复** `kpanda` clustersummary 空指针问题

**优化** `kpanda` 对 insight 的依赖改为弱依赖

**新增** `kpanda` 新增 CRD 和 CR 详情

**新增** `kpanda` 新增修改集群设置的 api

**新增** `kpanda` ListCluster 和 GetCluster 接入 clustersetting

**新增** `kpanda` 新增支持集群状态检索

**新增** `kpanda` 新增支持 label selector 和 field selector

**修复** `kpanda` 修复 global cluster 重复显示

**修复** `kpanda` 修复 ListClusterRoleBindings 根据 name 查询返回为空

**修复** `kpanda` 修复修改集群接入的 kube-config 后不能够生效的问题

**修复** `kpanda` 修复 global cluster secret 不刷新的问题

**修复** `kpanda` 用户获取集群 config 信息，用户填入什么信息，获取什么信息，不再初始化

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

**改进** `kpanda` 在创建 Helm 应用时进行名称校验

**新增** `kpanda` secret 列表新增根据类型筛选

**新增** `kpanda` 支持显示全部的 Repo

**新增** `kpanda` ListConfigMaps 和 ListSecrets 接口提供只返回 metadata 的功能

**新增** `kpanda` 支持网络模式为 none

**新增** `kpanda` 支持 ntp 网络参数配置

**新增** `kpanda` 支持节点角色筛选

**新增** `kpanda` 新增默认参数 `calico_feature_detect_override`

**新增** `kpanda` 新增 cilium 参数

**新增** `kpanda` 新增 helm release 历史版本及回滚功能

**新增** `kpanda` 新增 NetworkPolicy 的 CRUD

**新增** `kpanda` 新增 cluster 列表针对 kubernetesVersion 和 managedBy 的模糊搜索、namespace 列表针对 workspaceAlias 的模糊搜索

**新增** `kpanda` 除工作负载外所有 list 接口移植 customEngine

**新增** `kpanda` 创建升级集群时记录 k8s 版本号

**新增** `kpanda` 新增 LimitRange 的 CRUD

**新增** `kpanda` 新增支持 cluster 的 lableSelect 的操作

**新增** `kpanda` 新增支持 node 的 cpu 和 memory 的 request 和 limit 从 k8s 获取

**新增** `kpanda` 支持 clusterlcm 离线安装

**优化** `kpanda` 将 apiResourcesList 移动到 cluster 的 status.APIEnablements

### Api-service

**新增** `kpanda` 增加权限管理 CRUD

**新增** `kpanda` 新增 redis chart

**新增** `kpanda` 新增 bindingsync controller

**新增** `kpanda` 支持 rabc 精细化授权

**新增** `kpanda` 支持 rabc 精细化鉴权

**新增** `kpanda` 支持 AccessScopeList 精细化查询

**新增** 添加 `cloudshell` 的 helm 部署方式并集成到 `kpanda` 中

**新增** 添加 `cloudshell` 的 创建查询删除的 API

**新增** 使用 GProductProxy 的形式进行对 cloudshell 的 svc 进行负载

**新增** 支持多窗口显示和日志滚动

**新增** `kpanda` 利用 fake clusterpedia 增加单元测试

**改进** 使用 cloudtty 的 virtualService 模式来暴露服务

**新增**  权限调整有一个 ns 权限就要返回这个 cluster

**新增** `kpanda` 上报 cluster 和 namespace 信息到 CRD 中

**新增** `kpanda` 对接 ghippo 模块 API

**新增** `kpanda` watch workspace 变化信息给对应 workspace role 创建 RBAC

**修复** `kpanda` 支持跨集群可见性搜索支持原生 sql 查询

**修复** `kpanda`修复 ListNamespaceSummary

**改进** 升级 cloudtty，增加 readiness 的功能

**修复** `kpanda` 下载证书优化（支持集群 Pod 外部访问）

**优化** `kpanda` 缩短打开 cloudshell 的时间

### work-api

**新增** 和前端对接按照 insight 的接口类型，新增 cpu、node、workload、pod 资源使用率接口

**修复** BFF 中的 node、cluster、pod 相关的接口中添加了 insight 的数据

**优化** 修复了 insight 的部分数据返回类型错误的 bug

**优化** insight 日志接口使用 kubesystem_id 作为查询 cluster 的 key

**优化** 添加了查询日志的 filter 过滤器

**优化** 修复了日志查询时不传入 workload 没有数据的问题

**优化** 修复了 node 的指标数据需要重复传入 node 的问题

### Controller

**改进** 优化 egress，在 cluster 未就绪时不需要尝试分配 port

**新增** `kpanda` 将鉴权移至 grpc

**新增** `kpanda` 新增 bindingsync gc 逻辑

**新增** `kpanda` 将 namespace quota 上报 gproductresources

**新增** `kpanda` 新增 gproductresources gc 多余 ns 逻辑

**修复** `kpanda` 修复 clusterlcm 新增错误节点导致集群无法卸载 bug

**修复** `kpanda` 修复 kubean 版本升级管理集群标签检测失败

**修复** `kpanda` 修复 1.20 以下 k8s 版本无法更新 APIResource

**修复** `kpanda` 修复更新集群 kubeconfig 的 secret 不存在 bug

**修复** `kpanda` 修复 apply 资源失败的 bug

**修复** `kpanda` 修复获取 clusterCIDR 错误的 bug

**修复** `kpanda` insight 安装的 namespace 错误的 bug

### 安装

**新增** `kpanda` 安装时可指定 redis PVC 的 storageClassName

**新增** `kpanda` 支持 arm 架构

## 全局管理

全局管理模块（开发代号 Ghippo）包含了用户、用户组、角色、权限等访问控制，具体特性变化如下：

**改进** 通过 mockery 框架简化 mock

**新增** 完成 user、login、group、等 e2e 测试

**新增** Ghippo 支持 OPA 权限管理

**新增** 工作空间 - 生命周期管理（创建/编辑/删除/查看/列表）

**新增** 工作空间 - 层级关系管理（绑定/列表）

**新增** 工作空间 - 工作空间与资源关系管理（绑定/解绑/列表）

**新增** 工作空间 - 工作空间和角色和用户（组）关系管理（绑定/解绑/列表）(API/SDK)

**新增** 工作空间 - 鉴权 (API/SDK)

**新增** 工作空间 - GProduct 资源名字注册

**新增** 关于 - 产品版本（创建/编辑/删除/查看/列表）

**新增** 关于 - 开源软件（列表/初始化)

**新增** 关于 - 技术团队（列表/初始化）

**新增** 许可证 - 生命周期管理（创建/编辑/删除/查看/列表）

**新增** 许可证 - 获取 ESN 序列号

**新增** 工作空间 - 资源配额管理（创建/编辑/删除/查看/列表/计算已分配）

**新增** 工作空间 - GProduct 资源配额注册

**新增** 用户与访问控制 - 鉴权 (APIServer/SDK)

**新增** 审计日志 - 展示（查看/列表/清理设置/导出）

**新增** 审计日志 - 批量插入

**新增** 身份提供商 - 对接 LDAP - 用户/用户组同步设置（创建/编辑/删除/查看/同步）

**新增** 平台设置 - 安全策略 - 密码策略设置

**优化** 工作空间 - 代码架构调整

**新增** 个人中心 - 访问密钥（创建/编辑/删除/查看/列表）

**新增** 审计日志 - 全局管理操作插入审计日志

**新增** 审计日志 - 对接 insight 来收集审计日志

**新增** 平台设置 - 安全策略 - 账号锁定策略

**新增** 平台设置 - 安全策略 - 浏览器关闭策略

**新增** 身份提供商 - 对接 IDP（OIDC 协议）

**新增** 工作空间 - 共享集群权限管理

**新增** 工作空间 - 共享集群配额管理 - 存储

**新增** 平台设置 - 顶部导航外观定制 - 重置功能

**新增** 平台设置 - 安全策略 - 会话超时策略

**新增** 审计日志 - 自动清理功能

**新增** 平台设置 - 安全策略 - 账号锁定策略

**新增** 平台设置 - 顶部导航外观定制 - 还原功能

**新增** 平台设置 - 登录页外观定制 - 还原功能

**新增** 产品导航 - 首页仅对 admin 用户展示

**新增** 工作空间 - 用户仅能查看有权限的 WS & folder 树状结构

**新增** Keycloak 高可用

**新增** 邮件服务器配置 - 支持 insight 和应用工作台发送邮件

**新增** 满足 Helm 规范，支持安装器和离线化

**新增** 许可证 - 未灌入或错误情况处理

**新增** 审计日志 - 数据库自动创建和合并分区

**新增** 支持 arm64 架构

**新增** 支持 https

**新增** 登录 - 背景 theme 支持动画

**新增** 授权鉴权 - 给前端提供当前登录用户的 permissions 列表

**优化** 授权鉴权 - 提供一个 job 来确保 db 和 cr 的同步

**新增** 关于 - 软件版本 - 模块支持中文名

**优化** LDAP - 配置错误检查

**优化** 各功能操作反馈和提示语报错支持中英文

**优化** 工作空间及层级 - 删除前对是否存在子资源进行检查

**优化** 优化 keycloak jvm 参数

### API

**新增** Ghippo 登录页面更新配置接口

**新增** Ghippo 支持登录

**新增** Ghippo 支持忘记密码

**新增** Ghippo 支持站内信增删改查功能

**新增** Ghippo 支持 smtp 设置邮件服务器

**新增** Ghippo 支持顶部导航栏获取查询

**新增** Ghippo 支持顶部导航栏更新

**新增** Ghippo 支持 user role 权限管理 CRUD

### 开发进展 2022-10

**修复** 修复资源组接口按资源类型筛选数据库报错问题

**新增** 给第三方应用提供接口在 Keycloak 创建 SSO 对接 client
  
**新增** 支持 MySQL 8.0
  
**新增** 对接 Insight (metrics, log, otel tracing)
  
**新增** License 模块名支持 i18n
  
**新增** 支持一个 License 中可以包含多个 Gproduct
  
**新增** 资源组新增绑定集群类型资源
  
**新增** 资源组列表增加`模块`字段
  
**新增** 资源组列表增加已绑定标识
  
**新增** 资源绑定接口支持 registry 资源种类
  
**优化** 资源种类改枚举
  
**优化** GProduct license 是否需要灌入变量改为可配
  
**优化** 优化 CICD 流程
  
**修复** 修复已经删除的集群依然存在问题
  
**修复** 修复 keycloak jwks 变化后没有重置 Istio 缓存问题
  
**修复** 修复用户组创建时间零值问题
  
**修复** 修复访问密钥`最后使用时间`字段在未使用时返回空字符

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

### Spiderpool 2022-10

**新增** gRPC 最大传输数据量 20M

**新增** `spiderpool` 相关 API

**新增** `spidernet-ui` chart 模板

**新增** 为 SpiderEndpoint 新增修改性质的 Webhook，参见 [PR 933](https://github.com/spidernet-io/spiderpool/pull/933)

**新增** 为 SpiderSubnet Informer 启用了 RESYNC 机制，参见 [PR 931](https://github.com/spidernet-io/spiderpool/pull/931)

**新增** 支持在自动创建的 spiderippool 中扩缩 IP，参见 [PR 834](https://github.com/spidernet-io/spiderpool/pull/834)

**修复** 修复了标记 IP 分配会失败的问题，参见 [PR 929](https://github.com/spidernet-io/spiderpool/pull/929)

**修复** 修复了 SpiderSubnet 中无法移除空闲 IP 地址的问题，参见 [PR 936](https://github.com/spidernet-io/spiderpool/pull/936)

### 相关 CNI 插件  2022-10

**新增** 碎片扫描功能，参见 [PR 53](https://github.com/spidernet-io/cni-plugins/pull/53)

**修复** 当删除规则不存在时忽略错误的问题，参见 [PR 48](https://github.com/spidernet-io/cni-plugins/pull/48)

**新增** 新增 e2e kind，参见 [PR 62](https://github.com/spidernet-io/cni-plugins/pull/62)

**新增** 新增 GitHub 操作流，参见 [PR 65](https://github.com/spidernet-io/cni-plugins/pull/65)

**修复** 修复了 Pod 和主机之间 IPv6 通信失败的问题，参见 [PR 44](https://github.com/spidernet-io/cni-plugins/pull/44)

**修复** e2e 加载镜像错误，参见 [PR 67](https://github.com/spidernet-io/cni-plugins/pull/67)

**修复** e2e kind-init 初始化问题，参见 [PR 70](https://github.com/spidernet-io/cni-plugins/pull/70)

**修复** 修复和优化 CI，参见 [PR 78](https://github.com/spidernet-io/cni-plugins/pull/78) 和 [PR 79](https://github.com/spidernet-io/cni-plugins/pull/79)

## HwameiStor

HwameiStor 是「DaoCloud 道客」独立开发的开源项目，请参阅 [HwameiStor Release Notes](https://github.com/hwameistor/hwameistor/releases)。

## 文档站

**新增** GitLab 第一次文档站上线：容器管理、全局管理、文档站模板、产品文档站

**新增** GitLab 文档站按 feature 特性新编页面

**新增** DCE 5.0 社区版发版，所有 Scrum 文档迁移到 GitHub

**新增** 文档站编译器从 GitBook 迁移到 MkDocs

**新增** 部分英文页面
