# Release Notes

本页列出服务网格的 Release Notes，便于您了解各版本的演进路径和特性变化。

## v0.10

### API

- **改进** 边车升级接口新增工作负载与边车升级信息字段：
    - 请求新增字段：`is_hot_upgrade`、`workload_id`
    - 返回新增字段：`upgrade_info`
- **新增** 滚动重启定义的 annotation 字段 `controller.mspider.io/rollout-restart-at`
- **新增** 服务相关指标接口
- **新增** 接口字段 `sidecar_versions`、`is_upgradable`、`expand_result`
- **新增** 字段 WorkloadShadow.Status.SidecarVersions
- **新增** 对所有请求参数添加校验
- **新增** API 的 Pipeline，用于单独发布 mspider-api 的 sdk 版本
- **新增** `/apis/mspider.io/v3alpha1/meshes/{mesh_id}/environment-statuses` 所选升级版本支持的 kubernetes 版本范围，从小到大排序
- **新增** 更新网格接口增加网格版本字段
- **新增** 网格可升级版本接口
- **新增** 网格环境检测接口
- **新增** 网格升级过程中的升级结果检测接口
- **新增** 网格列表中网格是否可以被升级字段
- **新增** 边车升级检测接口：`/apis/mspider.io/v3alpha1/meshes/{mesh_id}/clusters/{cluster}/sidecar-management/-/upgrade-detection`
- **新增** 边车热升级版本列表：`/apis/mspider.io/v3alpha1/meshes/{mesh_id}/sidecar-management/-/supported-hot-upgrade-versions`
- **修复** 获取网格网关列表对 cluster 字段的校验，该字段为可选字段
- **修复** 获取集群命名空间列表对 cluster 字段的校验规则
- **修复** 获取工作负载实例列表对 cluster 字段的校验规则
- **修复** 无法创建服务网格的问题

### API 服务

- **新增** 网格升级详细实现
- **新增** 边车升级相关接口实现：获取边车升级版本列表、检测边车升级集群
- **新增** 网格升级环境检测接口提供所选升级版本支持的 kubernetes 版本范围，从小到大排序
- **新增** 原生原地边车升级实现
- **修复** 网格网关镜像 `hub` 字段没有应用
- **修复** 边车升级整体状态，当存实例升级失败时，状态为 Failed。并且返回整体错误信息
- **修复** 边车升级时，`pods`、`workloads`、`namespace` 三个字段都为空时，将会升级全部边车
- **修复** 升级过程中，环境检测状态不正确的问题
- **修复** 更新网格报错
- **优化** 网格是否可用升级接口，增加对权限的判断
- **优化** 升级信息，引入 operator status

### 基础设施

- **修复** 网格控制面版本不带 `-mspider` 后缀的问题

### 控制器

- **修复** 无限重复 reinstall mcpc
- **修复** 升级完成后，实例版本没有更新
- **修复** 网格版本显示不正确，同时优化没有找到 istiod 时的网格版本，和所填参数一致
- **修复** 不存在 workloadShadow 导致的空指针问题
- **修复** 从网格中移除后，MeshCluster 的 Status 未被清理
- **移除** CKube 依赖 Remote APIServer kubeconfig 的 configmap 逻辑
- **优化** mcpc controller 重试，避免重试过快导致因处理顺序产生的处理错误没有被在正确的顺序处理
- **优化** workloadShadow statues 更新逻辑，当没有 istio injector configmap 的时候为未注入，而不是报错

### 外部

- **升级** 前端版本至 v0.9.0

### 安装

- **改进** 构建流程，使用本地的 go 编译器加速构建
- **修复** ARM 64 镜像错误的问题。
- **修复** ckube 无法在非 root 用户下运行的问题
- **修复** ARM 64 镜像的基础镜像依然为 AMD 64
- **修复** 修复调用 ckube 无权限问题，ckube AuthorizationPolicy 配置中组件端口错误，端口为 8080
- **修复** istio.custom_params 错误拼写的问题

### 文档

- **新增** istio 资源 e2e 测试用例（网关规则、请求身份认证、对等身份认证、授权策略、服务条目）
- **改进** ckube/ckube-remote 映射端口 80 -> 8080

## v0.9

### API

- **改进** 服务列表接口 page.search 只支持 字段搜索，不支持 ckube 索引搜索。
- **改进** 统一未知 MeshVersion 为 "unknown"
- **新增** 服务列表工作负载接口和边车管理工作负载接口 `services` 字段
- **新增** 获取全局监控、性能监控、服务监控、工作负载监控的 API
- **新增** istiooperators 索引 loadBalancerIP
- **新增** gateways 索引 port
- **新增** authorizationpolicies 索引 action
- **新增** 服务相关指标接口。
- **新增** API 引入 protoc-gen-validate，以保证接口入参校验
- **新增** 网格和 RegProxy 相关接口加上字段校验
- **新增** 创建网格时增加负载均衡 IP 设置
- **新增** 获取集群列表接口新增字段 is_hosted_owner，过滤是否包含托管控制面集群，接口为 /apis/mspider.io/v3alpha1/clusters
- **修复** 统一监控面板，时间为秒
- **修复** 资源名 Regex 没有包含 `.` 的问题
- **修复** 将 RegProxy 相关接口移动到控制平面
- **升级** Insight API 到 v0.9.2

### API 服务

- **改进** 网格创建接口优化集群校验逻辑
- **新增** 服务监控相关指标实现
- **新增** 网关管理相关 e2e 测试用例
- **新增** 注册中心代理操作接口实现
- **新增** 注册中心代理操作接口 UT
- **新增** Grafana Dashboard URL 相关接口具体实现
- **新增** 拓扑新增健康状态，并且增加无数据的服务节点与除去无效节点与线
- **新增** 集群列表 is_hosted_owner 代码实现
- **新增** 更新托管网格时支持修改负载均衡 IP
- **修复** 东西网关循环 Reconcile 更新问题
- **修复** 外部网格模式删除检测不需要检测网格网关与边车资源
- **修复** admin 判断无效，导致无法获取正确的集群和命名空间数据
- **修复** authorizationpolicies 资源中 .spec.action 为 ALLOW 时，字段为空，导致无法搜索其的相关资源
- **移除** 命名空间接口的系统命名空间（istio-system, mspider-system等）的过滤
- **优化** 集群列表接口根据用户名和其所在用户组授权情况进行对应展示
- **优化** 工作空间绑定资源流程，避免出现和 ghippo 资源绑定不同步的情况

### work-api

- **改进** 服务列表允许 namespaces 字段代表所有命名空间，在 admin 权限下才能填充所有命名空间，其他非 admin 用户由 Auth 中间件填充
- **新增** 服务增加传统微服务标记
- **修复** 删除注册中心代理，请求返回响应码 500
- **修复** 修复服务列表接口中获取命名空间列表错误导致空指针异常
- **修复** Yaml 的列表未缩进导致前端无法折叠

### 基础设施

- **改进** 将 CKube 的索引配置移动到单独的文件，方便维护
- **改进** 所有的 UT 都引用独立的 CKube 索引文件
- **改进** ckube 内部认证 token 改造成 AuthorizationPolicy
- **新增** istio 1.15.0 支持
- **新增** istio 1.15.0 热升级支持
- **新增** arm64 版本镜像构建
- **新增** 镜像 trivy 扫描
- **新增** envoy b3 协议 headers 传递
- **新增** 支持在发布的时候生成 Changelog
- **新增** 切换 Go 到 1.19
- **新增** GRPC Server 校验 Proto
- **新增** license 检查
- **新增** 内建搜索支持多个条件判断
- **新增** 从 istio.io/api 自动同步 istio proto 的能力
- **修复** helm 在 arm64 是安装经常出问题，使用 gzip 代替 tar
- **修复** Istio Proto 同步失败的问题
- **升级** ckube 版本至 v1.2.1
- **升级** kpanda 接口至 v0.9.9 版本
- **优化** CI 流程，build test 不会推送镜像
- **优化** releasenotes 的格式检查
- **优化** build test 不构建 arm 镜像，加快速度

### 控制器

- **改进** 移除 "HOSTED_CLUSTER" MeshCluster 角色，判断 MeshCluster 是否安装托管控制面，通过 `MeshCluster.Spec.MeshedParams[].IsHostedOwner == true` 判断
- **改进** 由于移除 "HOSTED_CLUSTER"，控制器需要在 "FREE_CLUSTER" 角色下判断是否是托管控制面集群，完成托管控制面系列操作
- **新增** 集群健康状态细节设计实现
- **新增** `workloadShadow services` 字段，同一个工作负载可以绑定多个 service
- **新增** 为 Istio 自动设置版本号
- **新增** 托管集群 istiod 增加负载均衡 IP 设置
- **修复** 托管模式下，Mcpc Controller 组件在工作集群中无法正常运行，控制器忽略托管集群，无法正确获取工作集群信息
- **修复** MeshVersion 获取不正确
- **修复** 重新添加集群时可能出现之前纳管资源残留的情况，导致服务的某些显示状态不准确
- **移除** controller 默认对于系统命名空间的过滤，否则不会创建 workloadShadow 等
- **优化** 使用 kpanda 新的 stream cluster 代替轮询的方式来获取集群信息和状态

### 外部

- **改进** 将 Ckube 换成私有仓库和镜像
- **修复** 修复 istiod 指标无法捕捉问题，其 ServiceMonitor 无法被 insight 捕捉，其监控 labels 没有匹配
- **升级** 前端版本至 v0.6.1
- **升级** 前端版本至 v0.7.0

### 安装

- **改进** 服务网格在全局导航栏的顺序
- **改进** 删除 1.14.2 版本支持，新增 1.14.4 版本支持
- **新增** 默认将 tracing 发往 Insight
- **新增** 在不设置 global.imageRegistry 的情况下，默认全部使用公网镜像，不再使用 release.daocloud.io/mspider 作为默认镜像仓库
- **新增** 在 Mspider 相关 Pod 上新增 label: sidecar.istio.io/inject: "true"，解决Mspider 默认注入无效问题
- **新增** Istio 1.14.4 的 patch 文件
- **修复** 服务面板第一行默认被折叠的问题
- **修复** MSpider 部署无法接受 ui.version 参数导致开发环境 UI 镜像被回滚
- **移除** Mspider 相关 Pod 上新增 annotation: sidecar.istio.io/inject: "true"
- **优化** 统一 Grafana 面板的自动刷新时间枚举：5s、10s、30s、1m、5m、15m、30m、1h、2h、1d

## v0.8

### API

- **新增** `/apis/mcpc.mspider.io/v3alpha1/meshes/{mesh_id}/istio-resources/{type}` 接口 namespaces 字段，用法和之前不变，同时可以查询多个 namespace，用逗号隔开
- **新增** `/apis/mspider.io/v3alpha1/meshes/{mesh_id}/clusters/{name}/namespaces` 接口
- **新增** `/apis/mspider.io/v3alpha1/meshes/{mesh_id}/clusters/{cluster}/sidecar-management/workloads` 接口 namespaces 字段，用法和之前不变，同时可以查询多个 namespace，用逗号隔开
- **新增** 【获取集群命名空间列表】增加 `with_istio_coltrol_plane_info` 字段，用于获取带有 Istio 控制器信息的集群命名空间列表
- **新增** 为集群命名空间对象 ClusterNamespace 增加 `include_istio_coltrol_plane` 字段（仅当入参 `with_istio_coltrol_plane_info` 为 true 时有效）
- **新增** `controller.mspider.io/legacy-service-type` 和 `controller.mspider.io/legacy-service-config` 两个 Annotation，用于传统微服务支持
- **新增** 注册中心代理操作接口
- **新增** 获取当前可用 Istio 版本列表接口
- **新增** 创建网格和网格详情中增加 deployNamespace 字段
- **新增** Sidecar 热升级接口
- **新增** 工作空间绑定网格实例、网格命名空间接口
- **修复** 修改【获取集群命名空间列表】接口入参对象名为 ClusterNamespaceQuery，原为 ClusterNameQuery
- **修复** 错误的拼写，`include_istio_coltrol_plane => include_istio_control_plane`
- **修复** 错误的拼写，`with_istio_coltrol_plane_info => with_istio_control_plane_info`
- **修复** `/apis/mcpc.mspider.io/v3alpha1/meshes/{meshId}/govern/workloads/{workloadId}/instances` 接口 namespace 为 required
- **升级** Insight API 到 v0.8.1
- **移除** 移除获取网格网关列表请求字段 status, 通过 page.search 搜索状态，例如：page.search="status=RUNNING"

### API 服务

- **新增** 网格集群命名空间接口的权限控制
- **新增** grpc 请求支持根据用户名做授权
- **新增** 监控指标查询增加 Mesh 维度
- **新增** Grafana Dashboards 增加 Mesh 维度变量
- **新增** 新增网格网关 status 搜索实现， 通过 page.search 搜索状态，例如：page.search="status=RUNNING"
- **新增** mspider 分页 page.sort 新增多字段排序，如 "namespace,name"
- **新增** 实现边车热升级
- **新增** 边车热升级可通过 GRPC 或者 HTTP 长链接的方式调用
- **新增** 实现获取集群命名空间是否安装有 Istio 接口
- **修复** 工作空间资源绑定/解除绑定，同时优化流程
- **修复** 集群命名空间异常报错
- **修复** 修复创建网关服务默认为 ClusterIP 类型
- **修复** 修复网格网关在 Mesh Hosted 模式下，没有连接远程 istiod 问题
- **修复** 修复网格网关资源检测问题
- **修复** 网格网关状态无法显示创建中、删除中问题
- **修复** 多命名空间注入控制
- **修复** 边车管理查询工作负载接口输入错误的 cluster 接口仍然返回 200
- **修复** 边车管理查询工作负载边车情况接口输入错误的 cluster 接口仍然返回 200
- **修复** 边车管理控制工作负载边车注入接口输入错误的 cluster 仍然能够注入成功
- **修复** 工作空间网格、命名空间列表用户权限展示不正确
- **修复** 工作空间资源解绑，不需要传 workspaceID
- **升级** Insight API 到 v0.8.1
- **优化** 边车管理工作负载注入，提升性能
- **优化** 网格列表支持 user group

### work-api

- **新增** grpc 请求支持根据用户名做授权。
- **修复** 查询服务详情接口，replicas和availableReplicas都为0，为其添加实例信息
- **修复** 请求修改服务列表中【不存在的服务】的端口协议接口时，返回200
- **优化** 优化AggregationService{}逻辑
- **优化** 生成服务端口名时，增加端口列表的命名唯一检测优化：追加端口号
- **优化** 命名空间列表支持 user group。

### 基础设施

- **新增** MSpider 自身组件在 GSC 集群使用 AuthorizationPolicy 控制权限
- **新增** helm-docs, 生成对应 helm 文档 README.gen.md
- **新增** 为 RBAC 资源增加 alias 和扩展展示列，便于使用
- **新增** 构建可以热升级的 Istio
- **修复** HTTP 错误请求参数无法返回
- **修复** 当发生分页错误时，返回统一的 Error Code，便于前端忽略错误
- **修复** proto 排序无法排序没有值的 field 的问题
- **升级** ghippo 版本至 v0.9.25
- **升级** Helm 到 3.9.2，解决升级 chart 时，更新 Service 失败的问题
- **升级** Istio 默认版本到 1.14.2
- **移除** ci image dockerfile 移除 annotation_prep 工具
- **优化** MSpider 自身组件默认自动注入

### 控制器

- **新增** 同步 ghippo 权限资源可选。
- **新增** Eureka 支持
- **新增** GlobalMesh 支持创建指定版本的 Istio
- **新增** 实现 RegProxy 实例的事件消费，同步到 Service Annotation
- **新增** 网格健康状态检查
- **新增** 注册中心代理支持配置服务 FDNQ 作为 upstream
- **修复** 同步 ghippo 权限
- **修复** mcpc controller 创建集群 controller 逻辑，只会控制 workload clusters
- **修复** 工作空间资源绑定/解除绑定没有正确删除资源
- **修复** SpringCloud 调用 delta 接口导致请求未被代理
- **修复** Eureka 注册的服务无法写入 Service 信息
- **修复** 注册中心 envoyfilter 使用了固定的 cluster ID
- **修复** 全局边车资源限制中 memory limit 无法限制
- **修复** 一个可能会影响 workloadShadow 正确更新的情况
- **修复** 工作空间 role permission 的更新不正确

### 外部

- **新增** 将原有 DSM 边车热升级核心代码移动过来，但是架构不适配，后面在基于此逻辑修改，方便看出直观差别
- **升级** 前端镜像到 v0.6.0
- **升级** Insight API 到 0.7.1
- **升级** KPanda API 到 0.8.9

### 安装

- **新增** manifests 中 global.imageRegistry
- **新增** helm 增加通用参数： resources, imagePullPolicy, imagePullSecrets
- **新增** helm chart 包新增 _common.tpl, 用于定义通用的模板:
    - 核心原则：
        - .Values > .Values.global
        - common.images.pullSecrets: 按照优先级合并 imagePullSecrets
        - common.images.resources: 按照优先级推测最高优先级的 resources
- **修复** 托管网格同时部署在一个集群的时候会失败
- **升级** Insight Prometheus Monitor Operator 监控 Label: operator.insight.io/managed-by: insight
- **优化** 工作负载中 .template.spec.containers.resources
- **优化** 工作负载中 istio-operator 组件中默认 hub: grc.io -> gcr.m.daocloud.io
- **优化** manifests 组件镜像版本采用 Chart.Version
- **优化** Prometheus Monitor Operator 增加 watchLabels 变量，用于灵活指定抓取 Label

### 文档

- **改进** 8 月文档页面：虚拟服务、网关规则、目标规则、授权策略、对等身份认证、请求身份认证
- **新增** 增加网格网关相关 e2e 测试（ingress/egress）
- **新增** 增加网格统计信息 e2e 测试
- **新增** 增加获取 Grafana Dashboards 地址链接 e2e 测试 (ZH/EN language)
- **新增** 增加服务治理相关接口 e2e 测试
- **更新** 更新网格相关测试 docs
- **新增** 9 月文档页面：添加集群、移除集群、创建网格网关、删除网格网关、新增截图无数

## v0.7

### API

- **新增** 新增根据集群 ID 获取其所在网格信息接口
- **新增** 获取 Grafana UI 路径接口
- **新增** 指标查询参数新增可选字段 step：设置时间段间隔
- **新增** 统一服务治理的配置文件接口定义及简单说明
- **新增** 服务详情实例，实例为错误状态下失败原因字段 `failure_reason`
- **修复** 获取 Grafana Dashboards URL 方法名

### API 服务

- **新增** 新增根据集群 ID 获取其所在网格信息接口实现
- **新增** 新增根据集群 ID 获取其所在网格信息接口单元测试
- **新增** 服务详情实例错误时失败原因
- **新增** 获取 Grafana UI 路径实现
- **新增** 网格详情页指标表查询：ISTIO_PROXY_VCPU, ISTIO_PROXY_MEMORY_USAGE, ISTIO_PROXY_BYTES_TRANSFERRED，TOP_5_SERVICES_BY_RPM, TOP_5_SERVICES_BY_ERRORS_RATE, TOP_5_SERVICES_BY_AVG_LATENCY 六种指标实现
- **新增** 新增网格概览接口实现
- **修复** 删除网格条件判断中，网关的判断应该是网关实例，而不是 Gateway 资源
- **修复** 获取 Grafana Dashboards URL 未实现问题
- **修复** Page.Page = -1, 越界导致程序异常退出

### work-api

- **修复** 查询服务详情接口，replicas和availableReplicas都为0，为其添加实例信息

### 基础设施

- **改进** 默认指标端口 8090
- **新增** Istio Grafana Dashboards 资源与对应 CRD
- **新增** 如果外部镜像已经在仓库存在，将不再拉取到本地，节省 release.daocloud.io 的带宽，降低 CI 失败率
- **新增** 为控制面组件增加 HPA
- **新增** 增加控制面组件高可用部署方案文档
- **新增** `api-service`、`work-api`、`mcpc-controller`、`gsc-controller`、`reg-proxy` 指标接口 `/metrics`
- **新增** 组件 `api-service`、`work-api`、`mcpc-controller`、`gsc-controller`、`reg-proxy` 组件 Up 指标：`up` Component up status. type: `Gauge`.  
- **新增** 组件 `api-service` 与 `work-api` http 相关指标如下：
    - `http_request_duration_seconds` The latency of the HTTP requests. type: `Histogram`.
    - `http_response_size_bytes` The size of the HTTP responses. type: `Histogram`.
    - `http_requests_inflight` The number of inflight requests being handled at the same time. type: `Gauge`.  

### 控制器

- **新增** Istio 监控指标添加标签 `source_mesh_id`、`destination_mesh_id`
- **新增** 支持同时 Watch 多集群资源和查询的聚合查询器
- **新增** 对 Dubbo 协议的 EnvoyFilter 管理实现
- **新增** 给 mcpc controller 新增 `--leader-election` 参数，设置 `--leader-election=false` 时可以禁用 leader 选举，在开发的时候使用
- **新增** 实现 UnifiedProtocolConfig 到 EnvoyFilter Patch 的转换
- **修复** 托管网格中缺少 EnvoyFilter，导致可观测性不可用，暂时将 EnvoyFilter 放到 base 组件中解决，后期可能需要更好的方案，比如我们自己版本的 Operator
- **修复** 删除托管网格之后再创建同名托管网格的情况下，创建失败的问题
- **修复** GlobalMesh 在 config 阶段失败不会重试的问题
- **修复** workloadShadow status 逻辑，即将被 delete 的 pod 不应该计入 workloadShadow 的 status 中，导致某一时段 status 混乱
- **修复** 命名空间启用/禁用注入但还未重启工作负载时，工作负载的状态不正确显示
- **优化** 更新资源过程，避免一些不必要的更新
- **优化** 服务 `controller.mspider.io/workload-id` 逻辑，如果 workload 已被删除应该清除该 workload ID
- **优化** pod sidecar version 的 annotation 更新逻辑，当一定时间后 pod 已经注入 sidecar 后再检查 Envoy 的 configdump，否则 portforward 可能会失败
- **优化** 使用泛型实现了 Watcher + Queue，减少重复代码，后续方便使用

### 外部

- **升级** 升级 CKube 到 1.0.11，支持 go template 渲染索引
- **升级** 前端版本至 v0.5.2

### 文档

- **新增** 增加api benchmark测试, 此测试只做接口benchmark稳定  
- **新增** 多区域负载均衡与区域容灾治理文档
- **新增** 文档页面描述：系统架构、服务管理、网关规则、目标规则、虚拟服务、对等身份认证、请求身份认证、授权策略等  

## v0.6

### api

- **改进** 目前某些字段还保留了下划线模式，但是同时增加了一个驼峰模式的 Key  
- **改进** 查询服务版本列表返回参数 items 类型由 string 变更为 Subset 对象  
- **改进** 将 `mspider.io/synced-from` 的 Label 定义移动到 api
- **改进** Page 参数，按照第五代产品规范，重新修改分页逻辑，page_size = -1 表示全量，原有的 page=0&page_size=0 表示全量的逻辑废弃，在这种情况下，将视为默认参数（page=1&page_size=10）
- **新增** 网格网关创建失败时的失败原因字段 `failure_reason`
- **新增**  新增获取 ServiceInstance 列表接口实现
- **新增** 新增拓扑接口定义，并引入 insight graph.proto 定义
- **新增** 将 Istio 的 extensions、telemetry、security 的 proto 定义加入 ts sdk  
- **新增** global.mesh_capacity 参数，用于定义网格规模
- **新增** 新增网格网关 API 定义
- **新增** 新增网格更新接口
- **新增** 指标查询接口定义
- **新增** 网格统计信息接口定义
- **新增**  新增获取 ServiceInstance 列表接口
- **新增** 将 TS 生成的 OneOf 类型 export，便于前端使用
- **新增** 网格列表，网格为失败情况下失败原因字段 `failure_reason`
- **新增** 集群纳管列表，集群接入失败时失败原因字段 `failure_reason`
- **新增** 工作负载边车列表，边车注入失败时失败原因字段 `failure_reason`
- **新增** 为 MeshCluster 的 Status 增加 ClusterID 字段，用于在 Insight 中查询集群相关的指标
- **新增** 新增 Mesh Gateway 相关 Label: `mspider.io/component`
- **新增** 重构 IstioCrd 接口，将所有接口统一，减少不必要的接口和实现
- **新增** 注册中心代理组件 CRD 设计
- **修复** 将接口的全部改为驼峰格式，弃用原有的下划线模式
- **修复** 将所有 CKube 的 index key 改为驼峰模式，便于前端统一
- **修复** 修复 DELETE 方法 SDK 无法拼接 query, 改为 body 传递参数
- **修复** 在某些时候命名执行了 make gen，却还是报 Gen Check Error，是因为没有在 gen-proto 之前执行 format proto。 ([Issue #67](https://gitlab.daocloud.cn/ndx/mspider/-/issues/67)) 
- **修复** sidecar 接口无效
- **修复** 因为合并时序问题导致更新网格接口的风格没有修改
- **升级** 更新 insight version to v0.6.2
- **移除** 网格网关的未使用的字段 `version_status`
- **优化** 优化 mesh-gateway 字段
- **优化** 将边车管理接口独立到 `apis/management-api/sidecar` 位置

### api-service

- **新增** mspider 权限实现
- **新增** 网格网关相关实现
- **新增**  新增获取 ServiceInstance 列表接口单元测试
- **新增** 新增网格更新实现
- **新增** 网格接入、集群纳管、工作负载边车、全局边车失败原因
- **新增** 新增拓扑接口实现，通过调用 insight graph server
- **新增** 新增 Mesh Gateway 相关单元测试
- **新增** mesh gateway 错误信息
- **修复** gateway server 返回 response 时里面的值不是 snake case 的问题，同时暂时禁用 rbacManager，等 auth 完成后再启用
- **修复** 边车注入状态的判断，如果有 label 的话应该覆盖 annotation
- **修复** 当网格为专有模式，无法创建网格网关实例
- **修复** 未传 namespace 参数导致权限泄露
- **修复** 命名空间边车管理不应该显示系统命名空间
- **修复** istio gateway CRD 版本 v1alpha3 不支持导致网格删除检测接口 500 异常
- **修复** 创建网格网关失败。原因：没有添加集群与网格字段
- **修复** 网格网关 NodePort 一直为 0 问题
- **修复** 网格列表接口 crash
- **修复** 命名空间 `istio-injection` 为空时没有注入状态
- **修复** 全局角色 rolebinding 没有被正确删除
- **修复** mesh-namespace 角色有超出其权限范围内的命名空间的操作没有被禁止
- **修复** 查询边车管理工作负载接口，注入状态显示不准确
- **修复** 获取网格集群时传入不存在网格仍然相应 200 状态码的问题
- **修复** 全局边车管理传入不存在的 cluster 未报错的问题
- **修复** 边车资源限制，返回的 CPU 单位为(m)，内存单位为(bytes)，设置的时候也应该返回相同单位的数值
- **修复** 边车列表空指针问题
- **优化** 网格列表接口，如果用户只有部分网格权限只会返回部分网格
- **优化** 所有接口启用认证
- **优化** 网格网关的失败原因，和其他部分统一。
- **优化** Mesh Gateway 配置 configuration.service.ports[].protocol 默认值为 TCP
- **优化** Mesh Gateway 相关代码

### work-api

- **新增** mspider 权限实现
- **新增** Nacos 注册中心适配
- **修复** 服务地址没有对应排序字段导致的组件crash
- **修复** work-api 因分页问题导致的 crash
- **修复** namespace 角色可以获取全部 namespace
- **修复** page.Search 驼峰格式报错问题
- **修复** 服务列表查询错误，并优化了通用分页函数，支持 []string 类型
- **修复** service version 获取逻辑不对问题
- **修复** 切换 istio networking 组的资源为 v1beta1, 并增加非版本提示
- **优化** 网格命名空间列表接口，如果用户只有部分网格命名空间权限只会返回部分命名空间
- **优化** 所有接口启用认证

### 基础设施

- **新增** 支持解析在配置文件中解析 string 类型的 FeatureGateID
- **新增** 自动从 Insight repo 同步 graph 的 proto 配置
- **修复** rbacManager 的 UT
- **修复** 接口返回错误的时候，总是显示 500 错误
- **修复** make gen 错误
- **修复** 默认 sort 在不同机器上行为不一致的问题
- **优化** grpc-gateway 的 protoc 插件替换为 grpc-gateway v2，能使用新的 patterns 等功能
- **优化** gen-external-charts 的调用顺序，一面影响主要的 gen 流程

### 控制器

- **新增** ghippo 权限资源同步器，将 ghippo 全局角色和 workspace 角色同步到网格 RBAC 权限体系中
- **新增** 全局角色 Editor 和 Mesh-Editor，不具有任何删除的权限
- **新增** 支持外部服务网格接入的逻辑
- **新增** 使用 `mspider.io/synced-from: ghippo` 标记资源由 Ghippo 同步过来，syncer 删除的时候也只删除该类资源
- **新增** 支持自定义 Pilot IP
- **新增** RegProxy Controller 实现
- **新增** RegProxy 实例支持 RegProxy CRD 动态创建和删除
- **新增** 实现 ClusterID 的同步逻辑，为适配 Insight 做准备
- **修复** workloadShadow 的创建逻辑，即使没有注入 sidecar 我们也应该创建 workloadShadow
- **修复** interceptor 某些请求被错误拦截的情况
- **修复** InternalToken 没有被正确使用的情况（方便e2e测试）
- **修复** 自定义 Pilot IP 同时会影响到主 Istiod 的情况
- **修复** 集群在某些情况下无法移除
- **修复** 缺少聚合集群 kube config 状态判断
- **修复** 在没有 injection annotation 的情况下注入状态不正确的情况
- **修复** 控制集群存在已移除集群的命名空间
- **修复** 代理 Hosted APIServer 的时候，导致 TargetPort 总是 6443，造成在有多个托管网格的情况下出错
- **修复** ghippo syncer 应该给与 workspace 中的 mesh-namespace admin, viewer 基本的查看所属网格的权限
- **修复** user crd 被异常删除
- **修复** 在移除集群时同步的 workloadShadow 资源没有同步移除的情况。
- **修复** 更新 workloadShadow status 的一个错误
- **修复** workloadShadow inject 信息不正确
- **修复** 在 MeshID 和 Role 修改的情况下，MeshCluster 不会重新安装组件
- **修复** 某些情况下 MCPC Version 没有被渲染到 values
- **修复** workloadShadow 忽略 inject label 的情况
- **改进** leaderelection
- **优化** workloadShadow 的状态更新，并兼容 revision label 的情况
- **优化** 重置 kpanda 定时同步集群时间为 1 分钟
- **优化** workloadShadow 清理逻辑，定时清理不纳管集群的 workloadShadow，而非只有移出集群的时候清理

### 外部

- **新增** GProductNavigator、GProductProxy添加spec.gproduct字段
- **修复** 无法同步所有 KPanda 集群信息
- **修复** GHippo 删除了 iconName 字段，等待新 icon 被提供出来
- **升级** KPanda API 版本
- **升级** 前端版本至 v0.3.0
- **升级** 前端版本至 v0.4.0

### 安装

- **改进** 全局菜单栏侧边显示支持国际化
- **新增** 增加 GProductVersion 的 CR。 ([Issue #62](https://gitlab.daocloud.cn/ndx/mspider/-/issues/62)) 
- **移除** BFF Service，应该是以前复制代码的时候没注意

### 文档

- **改进** 把e2e test合并到nightly test，merge request可选择跑e2e test
- **改进** 拆分网格管理 API
    1. 网格管理
    2. 网格中集群管理
    3. 全局边车管理
    4. 工作负载边车管理
    5. 命名空间边车管理  
- **新增** 文档站页面：[创建托管网格](../03UserGuide/servicemesh/createmanaged.md)、[创建专用网格](../03UserGuide/servicemesh/creatededicated.md)、[删除网格](../03UserGuide/servicemesh/delete.md)、[集群纳管](../03UserGuide/08ClusterManagement/README.md)、[命名空间边车管理](../03UserGuide/07SidecarManagement/NamespaceSidecar.md)、[工作负载边车管理](../03UserGuide/07SidecarManagement/WorkloadSidecar.md)  
- **新增** 针对不同集群的主要k8s资源check  
- **新增** istio resource 虚拟服务, 以及部分目标规则e2e测试  
- **新增** 某些 Istio 资源的翻译，按照原型的说明进行对应
- **新增** 中英 pages.yml 文件，作为文档站总站对外目录的一部分  
- **新增** 注册中心代理组件设计文档
- **新增** 部署mspider环境，增加创建sleep资源，用于网格sidecar注入的e2e测试使用  
- **新增** 更新e2e测试用例代码跳转链接  

## v0.5

### API

- **新增** 将 Istio 的 Proto 定义手动生成到 TS SDK
- **新增** Istio VirtualService 、DestinationRule、GateWay 新增字段 `create_time`
- **新增** Gateway 索引 hosts
- **新增** AuthorizationPolicy、PeerAuthentication、RequestAuthentication 索引 match_labels
- **新增** 集群移除检测接口
- **新增** 集群状态增加 MANAGED_RECONCILING，MANAGED_EVICTING 两个状态，分别表示接入中和解除接入中
- **修复** Swagger 文档中错误返回的数据结构
- **移除** 从 TS SDK 中移除 Google 的包，不然前端解析会出错
- **优化** 重构网格删除检测接口

### API 服务

- **新增** mspider 用户权限认证内部实现
- **新增** 集群移除检测接口实现
- **新增** 网格删除检测接口实现
- **修复** 全局边车注入控制无效的情况
- **修复** 当集群名字包含 `.` 的时候，无法获取命名空间列表
- **修复** 获取网格集群列表接口逻辑，只要 Cluster 的 MeshID 为当前 Mesh 即表示属于此网格
- **修复** 之前的 `utils.ProtoEqual` 用法有问题，使用 JSONEq 代替
- **修复** 获取命名空间注入情况时的 503 错误
- **修复** 边车管理中边车版本接口，同时优化性能
- **修复** 边车管理接口工作负载边车注入无效
- **修复** 边车管理接口关键字重叠导致查询不到的情况，以及缺失 total
- **修复** DEDICATED Mesh 一些接口的问题
- **优化** 使用 batch 优化 ListMeshes 接口性能

### work-api

- **改进** 服务地址信息能够展现多集群的访问 IP, 将 `accessIp` 修改为 `accessIps` 类型似为 string 数组
- **修复** 服务列表中实例数不正确问题
- **修复** 修复服务协议更新失败。失败原因是当 Service.Spec.Ports[].Name 为协议类型时，如 http 或 https 时，将更新协议失败
- **修复** 工作负载边车注入情况显示不正确
- **修复** 查询工作负载接口排序缺失 total 字段
- **修复** 服务端口协议更新 http2、https 、tls、grpc 更新失败问题
- **优化** 服务列表加速，通过 Service Annotation 获取服务实例相关信息
- **优化** 迁移自定义 Annotation 到 apis/annotation 中
- **优化** ListVirtualServices 允许全部命名空间

### 基础设施

- **新增** 在发布版本的脚本中，增加自动发布 GitLab Release 的操作
- **新增** 切换 Go 到 1.18.2
- **新增** 使用 Nexus Cache Go Module
- **优化** 使用泛型优化 PaginateRes 分页函数，保证更好的可读性

### 控制器

- **新增** 服务包含的 workload 的状态的同步，通过 `controller.mspider.io/workload-status` 注解
- **优化** controller.mspider.io/workload-id，包含服务所包含的所有 workload 的 workload-id
- **新增** 将 Istio 相关 CRD 在 MCPC 的 Hosted apiserver 中创建
- **新增** 对集群状态进行检测，以保证同一个集群部署不产生冲突
- **新增** controller.mspider.io/proxy-version 注解，用于标注 pod 上的实际边车注入版本
- **新增** 集群 Phase 状态同步
- **修复** mcpc-controller 对于命名空间的过滤问题，可以通过 `-denied-namespaces` 指定不需要同步的命名空间
- **修复** mcpc-controller 启动时 --deniedNamespaces 默认命名空间无效的问题
- **修复** namespace informer 无效导致的 ns 没有在托管控制集群创建的问题，改用 watcher
- **修复** 网格就绪条件判断，避免在托管网格未就绪的情况下，无法获得 Pilot IP 而导致 Workload 集群无法安装
- **修复** 创建托管网格后，一直处于CREATING状态，因为没有配置 DeployNamespace，为其设置默认值 `istio-system`
- **修复** Annotation 位置之后代码没更新
- **修复** DEDICATED 模式下 MCPC Controller 因为 ConfigMap 为空导致无法启动
- **修复** 网格配置更新后，会覆盖掉 Workload 集群原有的配置，如 Sidecar 资源用量等
- **修复** 网格一直处于刷新中的状态，无法完全删除
- **修复** MeshCluster 删除逻辑，避免删不掉的情况
- **修复** 工作负载资源显示不正确
- **修复** 新接入集群时没有给 workloadShadow 添加 service 的情况，同时优化添加 service 的流程，避免 conflict 导致的更新失败
- **修复** 同步 kpanda 集群状态时空指针异常
- **优化** mcpc-controller 对于已经存在 service 名称的 workloadShadow 的逻辑

### 外部

- **升级** 前端版本
- **升级** 前端版本至 v0.2.0

### 安装

- **新增** Istio CRD Ckube 配置

### 文档

- **改进** 网格管理服务 api 测试用例：a. 网格/添加集群增删查; b. 工作负载/命名空间以及 global 的 sidecar 的配置及获取信息
- **新增** mspider work api NodePort SVC 在部署 mspider 环境时
- **新增** 目标规则、网关规则、yaml资源、虚拟服务 api 测试用例
- **新增** istio 资源管理、网格边车管理测试覆盖率
- **新增** 文档页面：产品优势、适用场景、功能总览、常见术语以及和两个基础知识（流量治理和虚拟服务）

## v0.4

### API

- **新增** common-protos/istio 定义, 并增加软连接 apis/networking 与 apis/type
- **新增** google/api/field_behavior.proto 与 google/protobuf/wrappers.proto
- **新增** Istio VirtualService 资源接口文档
- **新增** Istio DestinationRule 资源接口文档
- **新增** Istio Gateway 资源接口文档
- **新增** 服务详情接口
- **新增** Istio VirtualService 、DestinationRule、GateWay 新增字段 `create_time`
- **新增** 集群状态增加 MANAGED_RECONCILING，MANAGED_EVICTING 两个状态，分别表示接入中和解除接入中
- **新增** 将 Istio 的 Proto 定义手动生成到 TS SDK
- **新增** 集群移除检测接口
- **优化** 重构网格删除检测接口
- **移除** 从 TS SDK 中移除 Google 的包，不然前端解析会出错
- **新增** Gateway 索引 hosts
- **新增** AuthorizationPolicy、PeerAuthentication、RequestAuthentication 索引 match_labels
- **修复** Swagger 文档中错误返回的数据结构

### API 服务

- **修复** 修复网格集群列表为空时，显示超量集群问题
- **新增** 新增网格删除检测接口实现
- **修复** 边车管理中边车版本接口，同时优化性能
- **修复** 边车管理接口关键字重叠导致查询不到的情况，以及缺失 total
- **修复** 修复了 DEDICATED Mesh 一些接口的问题
- **优化** 使用 batch 优化 ListMeshes 接口性能
- **新增** 新增集群移除检测接口实现。
- **修复** 修正获取网格集群列表接口逻辑，只要 Cluster 的 MeshID 为当前 Mesh 即表示属于此网格
- **修复** 之前的 `utils.ProtoEqual` 用法有问题，使用 JSONEq 代替
- **修复** 获取命名空间注入情况时的 503 错误
- **新增** mspider 用户权限认证内部实现
- **修复** 边车管理接口工作负载边车注入无效
- **修复** 全局边车注入控制无效的情况
- **修复** 当集群名字包含 `.` 的时候，无法获取命名空间列表

### work-api

- **新增** 新增服务版本列表接口实现
- **修复** 网格集群为空时，服务列表全量获取远程集群服务
- **修复** 工作负载 Status 空指针异常
- **修复** 查询工作负载接口排序使结果混乱、重复覆盖的原因
- **优化** work-api 命名空间列表过滤
- **新增** Istio CRD VirtualService 相关接口实现
- **新增** Istio CRD VirtualService 、DestinationRule 索引、VirtualService: hosts、gateways、 DestinationRule：host。
- **新增** Istio CRD DestinationRule、Gateway 相关接口实现
- **新增** Istio CRD Yaml 相关接口实现
- **修复** 独立部署模式下服务列表异常退出：获取 PodList 超时退出
- **修复** 查询工作负载接口排序缺失 total 字段
- **优化** 服务列表加速，通过 Service Annotation 获取服务实例相关信息
- **优化** 迁移自定义 Annotation 到 apis/annotation 中
- **优化** ListVirtualServices 允许全部命名空间
- **改进** 服务地址信息能够展现多集群的访问 IP , 将 `accessIp` 修改为 `accessIps` 类型似为 string 数组
- **修复** 服务列表中实例数不正确问题
- **修复** 服务端口协议更新 http2、https 、tls、grpc 更新失败问题
- **修复** 修复服务协议更新失败。失败原因是当 Service.Spec.Ports[].Name 为协议类型时，如 http 或 https 时，将更新协议失败
- **修复** 工作负载边车注入情况显示不正确

### 基础设施

- **新增** 对 releasenotes 格式的检查，禁止多个不同类型的releasenotes
- **新增** 在发布版本的脚本中，增加自动发布 GitLab Release 的操作
- **新增** 使用 Nexus Cache Go Module
- **新增** 切换 Go 到 1.18.2
- **优化** 使用泛型优化 PaginateRes 分页函数，保证更好的可读性

### 控制器

- **新增** 对 workloadShadow 的API部分新增的状态的同步，同时对 workloadShadow 的资源情况进行同步
- **新增** 服务 annotation "controller.mspider.io/workload-id"，用于关联 workloadShadow，避免 service 多次不必要的查询
- **新增** 为 controller 的 serviceAccount 新增一些关键的权限，比如 deployment 的 CRUD 等等
- **修复** mcpc-controller 没有正确同步 service 的问题
- **修复** mcpc-controller status 不正确的问题
- **修复** workloadShadow controller 没有正确启动问题（ckube watch导致）
- **修复** remote-kube-api-server 的 configmap 中多余的config，由于托管集群可被纳管导致
- **修复** controller 未能正确识别托管模式的问题，导致 wls 被创建到 ownerCluster 中
- **修复** 独立部署集群无法注入 Sidecar，mutatingwebhookconfigurations 的逻辑已经在 IOP 的 Template 中处理
- **优化** 去除一些暂时不需要的 remote ckube 的 config watch，否则会有很多报错的 log
- **新增** 服务包含的 workload 的状态的同步，通过 `controller.mspider.io/workload-status` 注解
- **优化** controller.mspider.io/workload-id，包含服务所包含的所有 workload 的 workload-id
- **新增** 将 Istio 相关 CRD 在 MCPC 的 Hosted apiserver 中创建
- **新增** 集群 Phase 状态同步
- **修复** mcpc-controller 对于命名空间的过滤问题，可以通过 `-denied-namespaces` 指定不需要同步的命名空间
- **新增** 对集群状态进行检测，以保证同一个集群部署不产生冲突
- **新增** controller.mspider.io/proxy-version 注解，用于标注 pod 上的实际边车注入版本
- **修复** mcpc-controller 启动时 --deniedNamespaces 默认命名空间无效的问题
- **修复** namespace informer 无效导致的 ns 没有在托管控制集群创建的问题，改用 watcher
- **修复** 创建托管网格后，一直处于CREATING状态，因为没有配置 DeployNamespace，为其设置默认值 `istio-system`
- **修复** 网格一直处于刷新中的状态，无法完全删除
- **修复** 同步 kpanda 集群状态时空指针异常
- **优化** mcpc-controller 对于已经存在 service 名称的 workloadShadow 的逻辑
- **修复** Annotation 位置之后代码没更新
- **修复** DEDICATED 模式下 MCPC Controller 因为 ConfigMap 为空导致无法启动
- **修复** 网格就绪条件判断，避免在托管网格未就绪的情况下，无法获得 Pilot IP 而导致 Workload 集群无法安装
- **修复** MeshCluster 删除逻辑，避免删不掉的情况
- **修复** 新接入集群时没有给 workloadShadow 添加 service 的情况，同时优化添加 service 的流程，避免 conflict 导致的更新失败

### 外部

- **升级** Ckube 到 1.0.5，增加可以在 ckube 里面使用 kubectl 操作多集群资源的能力
- **升级** Ckube 到 1.0.7，修复 CKube watch 可能错误的问题

### 安装

- **新增** 开发环境 CI 不修改 ui 版本
- **新增** 新增 Istio CRD Ckube 配置

### 文档

- **新增** e2e 冒烟测试
- **改进** e2e 自动创建kind集群->部署mspider->e2e冒烟测试->e2e API测试->clear集群 的 nightly test
- **改进** 网格管理服务api测试用例：a. 网格/添加集群增删查; b. 工作负载/命名空间以及global的sidecar的配置及获取信息
- **新增** 新增目标规则、网关规则、yaml资源、虚拟服务 api测试用例
- **新增**  新增istio资源管理、网格边车管理测试覆盖率
- **新增** 文档页面：产品优势、适用场景、功能总览、常见术语以及和两个基础知识（流量治理和虚拟服务）

## v0.3

### API

- **新增** 在 apis 下新增 label 与 annotation 定义，并且添加对应的自动化生成工具
- **新增** Istio 内建资源接口文档
- **新增** 增减网格和集群相关接口
- **新增** 增加或者修改网格服务管理的接口包括：命名空间列表、服务列表、服务工作负载列表、服务工作负载详情列表、服务地址列表、修改服务端口协议
- **新增** `Workload` 增加 `Resources` 资源字段
- **新增** TypeScript SDK
- **新增** 服务详情接口
- **新增** `/apis/mspider.io/v3alpha1/clusters` 接口中提供集群命名空间边车注入信息的能力，通过 `with_injection_details` 字段确认，需同时带有 meshID 的信息
- **新增** 服务状态新增 `WARNING` 类型。当服务能够正常运行，但存在部分工作实例异常情况下，提示告警
- **新增** 网格删除检测接口
- **新增** 服务版本列表接口
- **新增** 从老的 DSM 迁移 RBAC 的 CRD 过来
- **新增** workloadShadow CRD 中 `availableInjectedReplicas` 字段，用于表示当前工作负载已注入实例
- **优化** 将 WorkAPI 的接口路径地址改为 /apis/mcpc-mspider.io 以便于 GHippo 路由
- **优化** 将接口路径改为 /apis/mspider 开头以适配 GHippo 的路由
- **优化** 把所有与 API 或者 Client 相关的东西移动到 apis 目录
- **优化** Service 中治理协议扩充，支持协议有：TCP | HTTP | HTTP2 | HTTPS | TLS | GRPC
- **优化** Service 更新服务端口协议，增加 Cluster 字段，用于修正 服务协议
- **优化** 服务管理接口与对应字段
- **优化** 使用 github.com/golang/protobuf/jsonpb 代替 gogo protobuf
- **优化** enum 的字段，统一所有 enum 为大写加下划线命名法的常用规范（可能导致前段部分 enum 失效）,同时为没有注释的值增加注释
- **优化** 边车管理相关 api，查询时从 workload 名称变成了 workload_id
- **优化** 资源对象，和 kpandas 中统一，提供的 CPU 资源的数值单位为（m），提供的内存的数值的单位为（Mi * 1000）
- **改进** 将 CRD 的 Status 和 Spec 字段换成 Pointer，防止 NoCopy 导致的问题
- **修复** enum 默认值问题，将所有 enumerate 类型默认值（0）设置为 `Unspecified`
- **修复** 因 enum 改动而影响的代码逻辑、测试逻辑
- **修复** MeshStatusPhase 的 SUCCEEDED 错误命名，与 CRD 的 enumerate 冲突
- **修复** 命名空间边车管理 api 路径缺少 `mesh_id`
- **修复** 一些使用不规范的 POST，将路径改为 `/-/actions` 表示创建一个新动作
- **移除** 边车全局管理部分中的全局是否注入接口，添加到网格详细信息的接口中

### API 服务

- **新增** 边车管理相关功能，包括命名空间、工作负载、全局管理，以及边车注入和资源限制等操作
- **修复** `apis/mspider/v3alpha1/clusters/kapada-cluster/namespaces` 接口未校验集群名称
- **修复** API 无法删除网格

### work-api

- **新增** 服务版本列表接口实现
- **修复** 服务列表接口无法使用 search 和 sort
- **修复** 更新服务协议 HTTPS | HTTP2 | GRPC | TLS 无效的情况

### 基础设施

- **新增** 为 hosted etcd 增加 pv 防止数据丢失
- **新增** 发布版本时自动发布 js sdk
- **新增** 在CI中增加gomod依赖包版本自动扫描job, 此job定义为gitlab CI schedule每个月执行一次; 如扫描出更新版本, 则自动创建PR由开发人员评判是否合入此PR更新依赖包版本
- **新增** 静态检查增加 helm chart render 检查
- **新增** 自动发布版本的时候，在 tag 里面带上 release notes
- **新增** 按照大版本划分 release-notes 目录
- **优化** 使用 GProductProxy 代替原生 VirtualService 和 Authz Policy
- **优化** 优化 Client 的 QPS，避免在大量情况的情况下，被限流的问题
- **修复** 在 `gitlab-ci.yaml` 文件中配置 job 触发条件为 `$CI_COMMIT_BRANCH == "main" && $CI_PIPELINE_SOURCE != "schedule"` 以保证 `schedule pipelin`e 只执行依赖包扫描 job
- **修复** 之前的 Node 版本不支持 `npm publish`

### 控制器

- **新增** WorkloadShadow CRD，用于在 MCPC 集群同步多种 Workload 的信息，便于接口进行使用
- **新增** mcpc-controller 同步工作负载，创建对应的 workloadShadow CRDs 至管理集群
- **新增** mcpc-controller workloadShadow 同步 CRD 信息至其相关联的工作负载，如注入状态、资源信息等
- **新增** 多个部分的多个测试，包括 api-service, work-api, mcpc-controller, tools 等
- **新增** 增加 Phase 和 MeshVersion 字段的初始化
- **新增** KPanda 集群状态同步到 MeshCluster
- **新增** 同步 GlobalMesh 的 Phase 状态
- **新增** helm 在安装 chart 之前通过 template 判断是否需要更新 manifest
- **新增** 实现网格删除逻辑
- **新增** 适配 kpanda v0.5.5，kubeConfig 改为 kubeConfigString
- **新增** 支持一个集群同时作为 hosted owner 集群和 workload 集群，降低接入代价
- **新增** 支持从网格移除集群
- **新增** 当 GSC Controller 版本升级之后，自动升级子集群组件版本。 这可能会引起一些问题，不过暂时为了方便先这样
- **修复** MCPC Controller mode 错误
- **修复** controller map 未初始化导致 nil pointer error
- **修复** controller status 同步问题
- **修复** 多集群多 kubeconfig 时的启动问题
- **修复** 独立部署模式下 GlobalMesh Reconcile 的 MeshCluster 角色不对
- **修复** WorkloadShadow 生成 Kubernetes CRD 中枚举类型，将 `type` 字段重命名为 `kind`，并增加对应 kubebuilder 注释。 问题现象：枚举类型为 integer，导致无法  MCPC Controller 创建与更新 WorkloadShadow
- **修复** MCPC Controller informer 没有数据同步的问题
- **修复** GSC Controller reconcileIOPConfigParams 安装参数 `global.clusterRole` 错误
- **修复** 某些情况下，Globalmesh 资源没有被 Reconcile，修改为，只要不是成功或失败的情况下，都每隔 10s Reconcile 一次
- **修复** WorkloadShadow CRD 没在 VirtualCluster 安装的问题
- **优化** mcpc-controller 在管理集群中的启动流程，并增加 readyz 的检查接口
- **优化** 减少在 reconcile 错误的情况下，频繁重试，降低为 30s 一次
- **优化** Istio Operator 安装失败之后无限重试
- **优化** MCPC Controller 整体 remoteClient 定义问题，为了避免误用 client
- **优化** MCPC Controller 启动：cmHolder client 优化；增加 namespace 实时同步
- **优化** sed 替换 go 程序处理 CRD Enum 类型
- **改进** manifests/hosted-apiserver pv 与 pvc 增加字段 storageClassName

### 外部

- **升级** Ckube 到 1.0.3，修复当 API 断开时，可能出现获取到空资源的情况
- **升级** Ckube 到 1.0.4，修复当配置变更时，老的 Watcher 依然存在，导致 Server 负载过高的问题
- **升级** Ckube 到 1.0.5，增加可以在 ckube 里面使用 kubectl 操作多集群资源的能力
- **修复** KPanda Service 名字错误

### 安装

- **新增** 开发环境 CI 不修改 ui 版本

### 文档

- **新增** 文档站，部署了 [honkit](https://github.com/honkit)
- **新增** 中英文档站的大纲
- **新增** 文档站的 roadmap
- **新增** 4-9 月的 RoadMap 文档
- **新增** e2e测试用例的 coverage
- **新增** MSpider 权限设计文档
- **新增** 梳理 release notes 到文档站，方便项目跟踪和展示
