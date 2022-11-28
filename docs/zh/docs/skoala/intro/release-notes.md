# 微服务引擎 Release Notes

本页列出微服务引擎的 Release Notes，便于您了解各版本的演进路径和特性变化。

## v0.11

发布日期：2022-11-25

- 通过 client-go 管理网关生命周期
- 通过 client-go 管理网关 serviceMonitor 生命周期
- 支持操作 KIND
- 网关创建失败后 revert 资源
- 更新 CR/ContourConfiguration
- 网关添加 Trace 能力
- 网关 granafa 双语支持

## v0.10

发布日期：2022-10-28

- 修复托管 Nacos 服务实例治理健康状态字段问题
- 修复托管 Nacos Grafana 地址问题
- 添加托管 Nacos 认证状态展示支持
- 添加托管 Nacos 相关 E2E 测试用例
- 添加托管网关相关 E2E 测试用例
- 修复 Nacos Operator 的定义问题
- 修复 Sentinel 规则 ID 的问题
- 修复 Nacos 及网关 Chart 未接入 CI 的问题

## v0.9

发布日期：2022-9-25

- 修复托管 Nacos 服务治理健康状态问题
- 修复 Agent 请求体的问题
- 添加根据 Grafana 模版自定义资源判断是否安装模版的逻辑
- 添加托管注册中心查询缓存

## v0.8

发布日期：2022-8-24

### 漏洞修复

- 完善托管 Nacos 节点类型的信息
- 保持与 Nacos 本身逻辑一致修改默认 Nacos Namespace ID 为空字符串
- 修复删除 Nacos 配置接口参数不生效的问题
- 优化网关 API 策略的时间限制条件
- 修复查询 Mesh 服务列表错误的问题
- 修复更新网关 API 可能出现的错误
- 修复获取实例列表多集群下的问题
- 优化托管 Nacos 的接入 Insight 的请求数据结构
- 修复 API 中引用的 Insight 版本
- 修复 Sentinel NodePort 展示问题
- 修复托管 Nacos 列表页治理字段阻塞 API 的问题

### 功能特性

- 添加托管 Nacos 节点的扩展信息
- 添加 Nacos 托管注册中心接入 Mesh 插件相关接口
- 添加获取网关日志下载链接的接口
- 添加网关 API 的 JWT 验证相关字段
- 添加网关 API 状态相关字段
- 增加根据服务名称查询 Mesh 服务的 API
- 添加 Mesh 资源获取的 API
- 重构微服务 Insight 接入相关 API 及逻辑
- 添加获取托管 Nacos Chart 及镜像信息的接口
- 添加托管 Nacos 集群下线接口
- 修改 Nacos 端口设置方式的逻辑
- 插件接口增加显示 Mesh 插件类型
- 在插件中心里添加 Mesh 详情
- 添加创建 Nacos 时是否创建接入 Insight 的字段
- 增加获取容器日志接口
- 添加微服务托管资源安装的前置检测
- 添加获取网关相关 Chart 及镜像的 API
- 重构网关认证插件生命期管理相关 API
- 添加网关 Listener 绑定证书逻辑
- 修改 Agent 支持传入字符串数组
- 添加第一个注册中心或者删除最后一个注册中心时向全局管理报备的逻辑
- 添加托管 Nacos 的 Grafana 面板支持
- 添加删除服务实例的治理 API
- 添加托管 Nacos 服务列表是否治理字段
- 添加 Sentinel 插件从配置文件或请求参数读取镜像
- 重构 Sentinel 插件逻辑
- 重构 Nacos helm value 模版
- Sentinel Dashboard 添加 JMX 集成
- 添加 Sentinel 治理能力的 Grafana 面板获取的 API

### 基础设施

- 增加所有自研组件的 ARM 支持
- 添加基于 Chart 创建网关支持
- 添加 Nacos 的 ARM 支持
- 更新各配置项的默认值

### 文档

- 添加 Release 流程文档
- 更新 2022 年 11 月至 2023 年 4 月的研发计划

## v0.7

发布日期：2022-7-23

### 漏洞修复

- 修复 Nacos Operator 针对 Sentinel 的配置问题
- 修复接入的注册中心服务 API 不显示服务名的问题
- 更新增删改操作 API 返回数据符合规范
- 修复托管 nacos 创建配置文件同名时会更新的问题
- 修复托管 nacos 获取实例列表如果为启用 sentinel 会报错的问题
- 修复 protobuf 名称定义问题
- 更新网关资源命名格式
- 修改 Skoala 菜单排序权重
- 修复 Skoala Chart README 文件的问题
- 修复 Skoala Chart 的版本问题
- 修复 Skoala Init Chart 安装问题
- 重命名 Skoala Initor 为 Skoala Init
- 将 Contour Provisioner Prereq 的部署命名空间改为 gateway-system
- 修复 API 模块不能正常集成的问题

### 功能特性

- 增加纳管服务 address 字段的详情
- 服务列表 address 字段调整为数组
- 增强 API 更新后状态和之前的一致性
- 修复 Swagger 修复 BaseURL 错误的问题
- 优化 API 详情并展示接入服务的服务名称
- 增加部分 proto 文件注释
- 增加 API 级别的请求头调整策略
- 增加 API 级别的响应头调整策略
- 增加服务熔断策略
- 增加服务路由镜像策略
- 域名管理增加 TLS 证书管理
- 增加服务 TLS 支持
- 添加托管 Nacos 服务更新 API
- 添加托管 Nacos 服务删除 API
- 添加托管 Nacos 实例更新 API
- 添加托管 Nacos 配置监听列表
- 添加托管 Sentinel 中服务的实例详情 API
- 更改托管 Sentinel 状态字段
- 添加托管 Nacos 服务详情 API
- 重构接入注册中心的 Insight 集成 API
- 添加托管注册中心的 Insight 集成 API
- 添加托管 Nacos 插件中心相关 API
- 添加托管 Nacos 相关集群列表 API
- 添加托管 Sentinel 插件的熔断规则 API
- 添加托管 Sentinel 插件的热点规则 API
- 添加托管 Sentinel 插件的授权规则 API
- 添加托管 Sentinel 插件的系统规则 API
- 添加托管 Nacos 重名检查
- 添加托管 Nacos 创建命名空间重名检查
- 增加 Secret 列表信息的 API
- 增加服务列表服务命名空间筛选
- 增加 API 分组功能与 API 分组列表 API
- 使用 Contour Provisioner 重构网关生命周期管理 API
- 增加基于网关名生成 Ingress Name 的 API 逻辑
- 域名列表和域名详情增加 tls 证书相关信息
- 根据 Insight 调整网关日志查询逻辑
- 增加网关日志导出基本实现
- 网关 API 相关 Swagger 文档分组
- 网关排序优化，现只有一个排序条件，默认为请求开始时间
- 完成网关日志导出接口

### 基础设施

- 为 Agent Chart 添加自定义名称支持
- 将所有使用的 Chart 和镜像都做成可配置
- 添加 Skoala Init Chart
- 将相关 Chart 合并如 Skoala Init Chart 作为子 Chart
- 添加 Nacos Operator 的日常构建
- 为 Skoala Init 和 Contour Operator 添加 CI 流程
- 升级 Ghippo 版本至 0.9.41
- 更新 Demo 程序的 Sentinel 配置规则
- 将 Contour Provisioner Chart 合并入 Init chart
- 添加 Contour Provisioner Chart CI 流程
- 将 Contour CRD 从 Contour Provisioner Prereq 移动到 Contour Provisioner
- 增加被网关管理的资源的标签规则
- 网关 API 上下线字段更新
- 将 Nacos 实例修改为 Chart 模式管理
- 为 Nacos 实例增加 Insight Service Monitor 支持
- 增加部署 Nacos 实例时可使用配置的 Chart 和镜像
- 修复增加部分 ut
- 添加 Sesame Instance Chart
- 使用 Contour Provisioner 重构网关生命周期管理
- 基于网关名生成 Ingress Name

## v0.6

发布日期：2022-6-26

### 漏洞修复

- 优化数据库 uid 生成方式
- 修复服务列表报错时错误未抛出的问题
- 修复部分接口返回的时间类型数据由毫秒变为秒
- 优化部分代码提升性能
- 修复托管 Nacos 配置列表 API 的参数问题
- 修复托管 Nacos API 对于 Public 命名空间处理的问题
- 修复托管 Nacos API 请求不规范的问题
- 修复托管 Nacos 配置创建的问题
- 优化 Kubernetes 注册中心代码结构
- 修复 Cluster Namespace 重复的问题
- 修复托管 Nacos 挂载存储的问题
- 修复 API 详情展示中请求头重复的问题
- 修复托管 Nacos 获取配置历史的问题
- 修复网关管理 API 不正常的问题
- 修复获取 endpoint 出错时,应用 crash 问题
- 修复网关日志字段不完整的问题
- 网关服务列表数据字段优化
- 优化创建网关接口细节
- 优化网关实例列表 API
- 网关服务详情字段优化
- 修复服务不存在时 API 详情查询错误的问题
- 修复更新服务失败的问题
- 优化网关 API 结构并在创建 API 中删除 all 方法
- 优化网关 API 创建并新增支持高级策略在 API 创建时配置
- 更新网关 API 代码优化
- 修复域名配置更新时网关 API 不会同步更新的错误
- 将 Trivy 镜像漏洞扫描修改为严重问题时失败
- Kpanda 集成代码重构
- 修复各组件 Trivy 扫描问题
- 修改 API 结构适应新功能
- 根据 Helm Chart 规范调整 Chart 细节

### 功能特性

- 为网关 API 增加健康检查策略
- 服务列表部分字段名称优化
- 优化重试策略详情的获取
- 增加部分单元测试
- 添加托管 Nacos 微服务详情 API
- 添加托管 Nacos 服务实例列表 API
- 添加托管 Nacos 获取命名空间详情 API
- 添加托管 Nacos 创建命名空间 API
- 添加托管 Nacos 更新命名空间 API
- 添加托管 Nacos 删除命名空间 API
- 添加托管 Nacos 检查命名空间 ID 重名 API
- 添加托管 Nacos 服务订阅者列表 API
- 添加托管 Nacos 配置列表 API
- 添加托管 Nacos 配置详情 API
- 添加托管 Nacos 配置历史版本列表 API
- 添加托管 Nacos 配置历史版本详情 API
- 添加托管 Nacos 创建配置 API
- 添加托管 Nacos 更新配置 API
- 添加托管 Nacos 删除配置 API
- 添加托管 Nacos 检查配置是否存在 API
- 添加网关全局限流部署 Chart
- 添加托管 Nacos 获取接口列表 API
- 添加托管 Nacos 创建接口列表 API
- 添加托管 Nacos 修改接口列表 API
- 添加托管 Nacos 删除接口列表 API
- 添加 Kubernetes 服务及实例列表缓存
- 增加 API 重试策略配置
- 创建 API 时允许添加高级策略
- 添加微服务接口文档数据定义及 API 结构定义
- 添加网格类型网关服务的创建和查询
- 添加网格托管服务的详情信息
- 添加 Sentinel 流控相关 API
- 添加查询网关管理命名空间的 API
- 添加托管 Nacos 支持挂在 Volume
- 添加获取 PVC 的 API
- 添加托管 Nacos 的重启接口
- 负载均衡策略增加 Hash 负载均衡
- 增加根据 Mesh 实例 ID 查询 Mesh Namespace 的接口
- 增加根据 Mesh 实例 ID 和 Mesh Namespace 查询 Mesh 服务的接口
- 增加网关域名本地限流高级策略
- 创建网关域名跨域策略
- 网关 API 创建时可以直接创建高级策略
- 增加网关 Websocket 支持
- 优化网关日志的查询，满足原型要求
- 优化网关 API 接口结构
- 添加网关服务接入搜索功能
- 添加注册中心接入相关接口的鉴权
- 添加托管 Nacos 相关接口的鉴权
- 完成 Agent 代理请求功能
- 完成通过 Agent 获取 Nacos 服务列表功能
- 完成通过 Agent 获取 Nacos 命名空间列表功能
- 添加 Agent 自动部署
- 添加网关全局限流功能
- 拆分网关 API 上线和下线接口
- 增加域名删除的条件判断使已绑定 API 的域名不允许删除
- 添加网关验证服务器生命周期管理接口

### 基础设施

- 添加 Skoala Chart 针对正式环境的 Values 文件
- 添加通过配置指定 Ghippo 集群地址功能
- 将研发集成环境 Kubeconfig 加入默认 Chart Values 中
- 添加 Nacos Operator
- 添加安装 Contour 网关前置资源 Chart
- 为 Skoala Chart 添加 Ghippo 资源相关 RBAC 权限支持
- 为整体项目添加 Sonarqube 扫描
- 为 agent 镜像添加镜像漏洞扫描
- 为 Skoala Chart 添加 Ghippo 扩展配置参数
- 更新 Kpanda SDK 版本至 0.8.9
- nacos 列表支持通过名称模糊查询
- 在托管 Nacos 管理 API URL 中添加集群和命名空间字段
- 为 Nacos 及 Sentinel Demo 添加更多说明内容
- 添加 hive 访问 agent 获取 nacos 服务列表以及命名空间列表接口
- 为托管 Nacos 添加 Sentinel 插件能力
- 添加 Agent 部署 Stage 和 e2e 环境
- 修改 Agent 的 API Group Name 为 agent.skoala.daocloud.io

### 文档

- 添加托管注册中心相关操作文档
- 完成 v2 版本架构和数据流图
- 添加网关域名管理相关操作文档

### 测试

- 添加 Mesh 相关 e2e 测试
- 为压力测试请求添加 Token
- 重构网关 e2e
- 添加网关相关 e2e 测试
- 优化网关 e2e 测试逻辑
- 梳理测试用例移除无效用例

## v0.5

发布日期：2022-5-25

### 漏洞修复

- 修复 Zookeeper 为注册中心时的性能问题
- 修复 API Proto 文件带有中杠带来的 TS SDK 问题
- 统一修改 gatewayName 为 Name
- 修复实例 enabled 为 false 之后查询不出单个实例的问题
- 修复修改实例接口不生效的问题
- 修复命名空间为空时默认查询所有服务和实例的问题
- 修复 Mesh 类型注册中心 Ping 接口问题
- 服务列表去除 externalName 类型服务
- 修复创建 API 不能选择 OPTIONS 的问题
- 修复查询 zk 和 ek 的时候需要命名空间的问题
- 修复注册中心服务总数还存在 externalName 类型服务的问题
- 修复网关实例列表不正确的问题
- 修复没有设置外部服务开启能力的参数问题
- 修复名字空间列表 crash
- 修复健康检查时获取服务列表 crash
- 修复 hive 创建 helm client 错误
- 优化网关资源名称规则
- 升级 Hive 和 Sesame 的基础镜像版本来修复镜像扫描爆出的问题
- 修复 Stage 环境部署不正常问题
- 修复 Sentinel Demo 中的服务名配置
- 修复 Dubbo Sentinel Demo 中 Comsumer Project Name 配置默认丢失问题
- 修复 Skoala Chart 镜像地址配置问题
- 更新修复 Chart 中的产品模块对接地址
- 移除 Skoala Chart 中的 Namespace 资源 Yaml，建议使用 Helm 命令进行 Namespace 操作
- 将 Istio 边车注入开关移动到 Deployment 中

### 功能特性

- 添加托管 Nacos 获取服务列表 API
- 添加服务网格 mesh 的代理
- 添加网关服务管理功能
- 添加网关 API 负载均衡配置能力
- 添加网关 API 超时配置能力
- 添加网关 API 请求路径重写配置能力
- 为服务列表 Insight 数据添加缓存
- 增加更新网关 api 策略的接口，实现超时，负载均衡，路径重写的策略配置
- 增加网关日志的查询接口
- 更新 insight 的 sdk 版本为 0.7.1
- 优化之前的调用 isight 接口，兼容最新版本 insight
- 修改 k8s 获取 namespace 规则,现在通过 ghippo 获取
- 优化网关 API 逻辑
- 添加域名管理增删改查 API
- 更新 API 中的资源情况数据接口为 Kubernetes 格式
- 移除废弃的网关安装器
- 将网关信息存放位置由 Labels 修改为 Annoations
- 资源名称和网关名称分开处理
- 重构网关配置信息的逻辑
- 优化前端 API 的参数和逻辑
- 为网关安装和更细提供安装前 Hook 能力
- 通过命名空间查询网关列表
- 添加集群命名空间的过滤及分页
- 添加集群分页支持
- 更换获取集群命名空间 API
- 添加获取网关拥有 API 数量字段到网关详情
- 重构获取网关状态接口
- 添加 accesslog 配置参数
- 网关列表接口的状态设置为枚举值
- 为网关 accesslog 添加挂载存储
- 为 contour 添加诊断模式
- 为网关添加 metric 信息
- 参数重命名:k8s_debug -> kubernertes_debug
- 过滤无权限的管辖名字空间
- 重构包:ghippo
- 基于 ghippo 过滤网关所在名字空间及集群
- ListClusterGateway HTTP Method get -> post

### 基础设施

- 为网关域名管理功能添加 CRD
- 优化流水线步骤提高 CI 效率
- 添加变更合并到主分支后更新 e2e 环境
- 在 Nightly Pipeline 中添加 Trivy 镜像安全扫描
- 添加 agent 程序代码
- 添加 agent 程序 Helm Chart
- 添加 agent 程序 CI/CD
- 添加 Skoala Chart 的网格边车注入开关
- 添加 Skoala Agent Chart 的网格边车注入开关
- 为 Skoala Chart 添加 mspider 的配置支持

### 文档

- 添加文档站集成如主文档站的能力
- 完善概述中文档内容
- 完善英文文档的结构
- 添加英文文档站与主文档站对接支持
- 为 Sentinel 集成 Demo 添加 Namespace、Group、Cluster 等 Nacos 维度信息支持
- 将 Nacos 和 Sentinel Demo 合并，减少维护成本
- 添加网关生命周期管理文档

### 测试

- 添加 Nacos 托管资源生命周期管理 e2e 测试
- 添加网关生命周期管理相关 e2e 测试
- 添加 mesh 相关测试用例
- 添加网关 API 生命周期管理相关 e2e 测试
- 优化网关生命周期管理相关 e2e 测试

## v0.4

发布日期：2022-4-22

### 漏洞修复

- 修复 TS SDK proto 文件路径不正确的问题
- 修复注册中心实例数不对的问题
- 修复 detail 信息重复问题
- 修复 eureka ping k8s 地址会成功的问题
- 修复压力测试性能降低导致失败的问题，改成纪录到文件
- 修复由于分页规则修改带来的 e2e 测试失败的问题
- 修改注册中心对接集成文档的问题
- 修复由于 Insight 升级导致的问题并升级 Insight 版本至 0.6.0
- 修复集成 Kubernetes 的 e2e 测试问题
- 修复服务发现的逻辑问题
- 修复 Insight 数据模型并保持同类数据的结构一致性
- 修复 ClusterIP 模式无法正常创建网关的问题
- 修复 nacos standalone 能创建多个副本的问题
- 修复 workspace 分页问题
- 修复更新不存在 nacos 会新增的问题
- 修复 sentinel nodeport 问题
- 修复 sentinel update 问题

### 功能特性

- 创建网关 api 接口实现
- 修改网关 api 接口实现
- 网关 api 列表查询实现
- 网关 api 详情实现
- 网关 api 删除实现
- 网关 api 定义实现
- 实例列表的端口字段由单个值变为 int 类型的数组
- 添加 nacos 上下线接口
- 实例添加最后更新时间字段
- 服务列表添加健康实例数字段
- 添加注册中心，服务，实例接口分页规则符合内部规范
- 为服务详情 API 添加 start 和 end 两个时间选择参数，用于查询链路指标数据
- 添加服务和实例列表的查询
- 添加 k8s 服务和实例的 detail 信息
- 添加 ext_id 字段储存 k8s 集群 id 和 mesh id
- 添加增删改查 nacos 的 API
- 添加 nacos 创建时选择 service 的 type(clusterIP,NodePort)
- 接入 ghippo workspace
- 添加通过 workspaceId 获取单个 workspace 详情

### 基础设施

- API 定义文件及 SDK 自动同步到 skoala-api 仓库
- 添加每日压力测试
- 跟新 Java 构建基础镜像并加入内部 Nexus 仓库支持及相关基础包
- 添加 kpanda mock 功能帮助单元测试脱离真实环境
- 在 Chart 中添加 ghippo 集成 CR 文件
- 添加应用工作台集成的 Demo 及相关说明文档
- 添加集成依赖组件版本检查工具
- 添加 Spring Cloud 应用程序集成 Sentinel 流量治理的 Demo 代码及相关说明
- 添加 Dubbo 应用程序集成 Sentinel 流量治理的 Demo 代码及相关说明
- 增加 Sentinel Operator CRD 的 Nacos 配置
- 增加 Sentinel Operator CRD 的资源配置
- 增加 Sentinel Operator CRD 的 Service 类型配置
- 添加 Sentinel Operator Chart 相关配置
- 添加 Sentinel Operator Chart 命名空间支持
- 为 Dubbo Nacos 集成 Demo 添加 Mesh 兼容能力
- 添加 Sentinel 实例管理增删改查 API
- 手动管理 Contour CRDs
- helm 配置参数 改用 values.ymal 提供
- 实现 check 网关状态
- 组件(contour/envoy)版本展示
- 网关基本设配置
- 网关高级配置
- API 定义文件及 SDK 自动同步到 skoala-api 仓库
- 添加每日压力测试
- 完成 Sentinel Operator
- 完成 Sentinel Operator Dockerfile
- 完成 Sentinel Operator Helm Chart
- 完成 Sentinel Operator CI 及发布流程
- 添加 Replay 的支持及 Demo
- 注册中心 chart 增加 springcloud 应用，以 k8s 为注册中心，接入 otle
- 更新注册中心 chart，增加 nacos-server 中注册服务的 insight 接入
- 暴露更多的配置项
- 统一 deployment 资源配置

### 文档

- 添加单元测试最佳实践文档
- 添加概述，最新动态，组件信息等文档内容
- 添加托管注册中心创建流程文档内容
- 添加接入注册中心的流程介绍内容

## v0.3

发布日期：2022-3-25

### 漏洞修复

- 修复 Nacos 缓存的命名空间可以被取到服务信息的问题
- 修复实例列表 API 字段数据不准确问题
- 修复 eureka 注册中心状态不正常的问题
- 修复添加命名空间会多一个空字符的问题
- 修复 k8s 命名空间不生效的问题

### 功能特性

- 修改 Nacos Namespace 为结构体
- 修改 Create、Update、Ping API 中的数据为结构化数据，便于前端使用
- 添加服务和实例列表的分页
- 添加注册中心按类型查询功能
- 添加注册中心按名称查询功能
- 将注册中心类型设置为枚举类型
- 将分页设置为从 1 开始
- 修改注册中心添加和删除后的返回结果，只包含注册中心 ID
- 添加注册中心的接入时间和更新时间
- 添加注册中心形式（托管或接入）字段
- 添加注册中心运行状态字段
- 修改 Ping 接口可以传入现有命名空间列表以查询增量命名空间内容
- 重构 API 结构
- 添加网关 API Proto 文件及内容
- 添加托管 Nacos API Proto 文件及内容
- 添加 Workspace API Proto 内容
- 添加 Sentinel API Proto 文件及内容
- 添加 workspace 字段
- 添加 version 字段和 state 字段
- 添加 health_ins_count 字段和 total_ins_count 字段

### 基础设施

- 集成 Insight SDK 及调用验证
- 更新 chart 包，将 Insight 地址作为变量
- 集成 Ghippo SDK
- 完成 Workspace 的数据获取
- 更新 chart 包，增加 Ghippo 的地址作为变量
- 添加 Insight ServiceMonitor
- 服务接入 insight-agent
- 添加 Dubbo 服务的 Insight 集成
- 添加微服务 API 支持 Insight 数据
- 添加发布 TS SDK 到 NPM 站流程

### 安装

- 完成 contour 安装器
- 集成 kpanda API
- 添加 Workspace API
- 添加 Cluster API
- 定义完成网关 API
- 实现网关创建/更新/删除接口

### 其他

- 为文档站添加美化插件
- 重构代码目录结构
- 使用官方 embed 组件

## v0.2

发布日期：2022-2-28

### 漏洞修复

- 修复删除注册中心的逻辑问题
- 修复 ping nacos 错误地址问题
- 修复使用自动化脚本再次删除重建的同名注册中心报错
- 修复获取全部实例异常的问题

### 功能特性

- 注册中心检测接口添加返回的服务个数及相关命名空间信息
- 添加实例 framework 信息
- 修改 api url 结构使其符合产品规范
- 修改 nacos-client 的结构
- 添加对服务和实例列表的缓存
- 重构注册发现代码

### 基础设施

- 废弃 hive chart 并使用 skoala chart 部署前后端所有内容
- 添加自动化发布工具
- 完善自动化发布流程

### 测试

- 完成 nightly e2e 测试流程
- 完成 nacos 注册中心接入流程 e2e 场景
- 完成 eureka 和 zookeeper 的注册中心接入流程 e2e 场景
- 添加实例数获取 e2e 场景 (nacos/eureka/zookeeper)
- 添加服务数获取 e2e 场景 (nacos/eureka)
- 添加接入注册中心后进行查看修改和删除的全流程验证 e2e 场景 (nacos/eureka/zookeeper)
- 添加重复接入同一个注册中心(name 不同)e2e 场景 (nacos/eureka/zookeeper)
- 添加重新接入已删除的同名注册中心 e2e 场景 (nacos/eureka/zookeeper)
- 添加测试 ping 接口 type 与 address 不匹配 e2e 场景 (nacos/eureka/zookeeper)
- 实例数获取 e2e 场景中添加 frameworkType 检查点
- 修改 e2e 测试脚本来适应新的 nacos 服务发现逻辑
- 为 e2e 逻辑中的注册中心名添加随机性来避免数据冲突导致的失败

### 其他

- 添加整体双语文档站结构及主要内容
- 完成 ROADMAP 内容
- 将文档 ROADMAP 内容合并如总 ROADMAP 文件
- 更新文档结构
- 添加架构图
- 整理 README 文档并添加 demo-dev 和 demo-alpha 两个环境信息
- 将单元测试的目标值调整至 40%
