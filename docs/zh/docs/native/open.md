# 开源项目

本页按字母顺序列出云原生开源项目的动态。

### A, B

- [Acorn：Acorn Labs 开源的 K8s 应用打包和部署框架](https://acorn.io/introducing-acorn/)  

    [Acorn](https://github.com/acorn-io/acorn) 能够将所有应用程序的 Docker 镜像、配置和部署规范打包成一个 Acorn 镜像工件，这个工件可以推送到任何 OCI 镜像仓库。
    因此，开发人员无需切换工具或技术栈就能够将在本地开发应用转移到生产中。
    Acorn 镜像通过在 Acornfile 中描述应用程序的配置来创建，无需 Kubernetes YAML 的样板文件。

- [Aeraki Mesh 服务网格 v1.3.0 发布](https://github.com/aeraki-mesh/aeraki/releases/tag/1.3.0)

    更新内容：支持 Istio 1.16.x 版本、支持多路复用、支持在 Gateway 上提供 MetaProtocol 七层路由能力、Dubbo 服务支持应用级服务治理、支持 Redis 流量管理。

- [Aeraki Mesh 服务网格项目 v1.1.0 发布（CNCF 项目）](https://www.aeraki.net/zh/blog/2022/announcing-1.1.0/)

    该版本主要新特性：支持 Istio 1.12.x 版本；支持 bRPC（better RPC） 协议，bRPC 是百度开源的工业级 RPC 框架；MetaProtocol 支持流式调用、支持采用 MetaData 设置负载均衡 Hash 策略以及在 Response 中回传服务器真实 IP 等。  

- [AlterShield：由蚂蚁集团开源的变更管控平台](https://mp.weixin.qq.com/s/8L2LqxeRK9LCtfSkKG94wg)

    [AlterShield](https://github.com/traas-stack/altershield) 是一款集变更感知、变更防御、变更分析于一身的一站式管控平台。旨在通过定义变更标准协议，规范变更管控流程，使用户快速发现变更中的问题，并及时降低故障影响面。对于云原生场景，AlterShield 提供了 Operator，连接各类 CI/CD 工具到 OCMS（Open Change Management Specification）SDK。同时，Operator 本身也提供了变更流速控制、异常回滚策略控制等能力。

- [Antrea CNI 插件 v1.12.0 发布（CNCF 项目）](https://github.com/antrea-io/antrea/releases/tag/v1.12.0)

    版本特性：拓扑感知功能和节点 IP 地址管理功能从 Alpha 升级到 Beta，且默认启用；支持通过一个新的 Antrea 代理配置参数启用多播功能；在 AntreaProxy 中增加对 ExternalIP 的支持；为多集群增加 WireGuard 隧道模式的支持；为多集群服务增加对 EndpointSlice API 的支持。

- [Antrea CNI 插件 v1.11.0 发布（CNCF 项目）](https://github.com/antrea-io/antrea/releases/tag/v1.11.0)

    版本特性：ClusterSet scoped 策略规则支持命名空间字段、L7 策略规则支持流量日志、支持在 TCP 网络包上处理 DNS 请求、AntreaProxy 的端点切片（EndpointSlice）功能升级为 Beta、AntreaProxy 支持处理终止过程中的端点（ProxyTerminatingEndpoint）、Egress 策略支持限制分配到一个节点上的 Egress IP 数量、多集群网关支持多种流量模式。

- [Antrea CNI 插件 v1.10.0 发布（CNCF 项目）](https://github.com/antrea-io/antrea/releases/tag/v1.10.0)

    该版本主要新特性：增加 L7 网络策略功能、Antrea 的 CRD API 能够在任何 K8s 节点或 ExternalNode 上收集 support bundle 文件、增加对跨集群流量的网络策略的支持、在 Windows 上使用 containerd 作为运行时时，antrea-agent 可作为 DaemonSet 运行。

- [Antrea CNI 插件 v1.9.0 发布（CNCF 项目）](https://github.com/antrea-io/antrea/releases/tag/v1.9.0)

    新增多个多集群功能，包括跨集群 Pod 间连接、节点控制器支持 Gateway 高可用、允许 Pod IP 作为多集群 service 的端点；
    增加类似于 kube-proxy 的 service 健康检查；审计日志添加规则名称；一个 service 支持 800+ 端点。

- [Antrea CNI 插件 v1.8.0 发布（CNCF 项目）](https://github.com/antrea-io/antrea/releases/tag/v1.8.0)  

    该版本主要新特性：增加 ExternalNode 功能、K8s 网络策略增加审计日志支持、支持利用 Antrea ClusterNetworkPolicy 控制 NodePort 服务的外部访问、允许对不同的网络端点进行逻辑分组、每次 Antrea release 都生成新的 Helm Chart 版本、支持拓扑感知 TopologyAwareHints、在 IPPool CRD 中添加状态字段。

- [Antrea CNI 插件 v1.7.0 发布（CNCF 项目）](https://github.com/antrea-io/antrea/releases/tag/v1.7.0)
  
    该版本主要新特性：增加 TrafficControl 功能，控制 Pod 流量的传递；支持 IPsec 证书认证；丰富 Antrea-native 策略；丰富组播功能；增加多集群网关功能；丰富二级网络 IPAM 功能。

- [APISIX 云原生网关 v3.2.0 发布](https://github.com/apache/apisix/releases/tag/3.2.0)

    版本特性：支持四层上的服务发现、新增一个能将 RESTful 请求转成 GraphQL 的插件、支持在每个日志插件上设置日志格式、新增插件支持 JSON 和 XML 之间的互相转换。

- [APISIX 云原生网关 v3.1.0 发布](https://github.com/apache/apisix/blob/release/3.1/CHANGELOG.md#310)

    该版本主要新特性：支持将插件的特定字段加密保存到 etcd 中、允许将敏感信息存储在外部安全服务中、实验性地支持基于 gRPC 的 etcd 配置同步、新增基于 Consul 的服务发现功能、增加了一个内置的调试器插件。
  
- [APISIX 云原生 API 网关 v3.0 发布](https://github.com/apache/apisix/blob/release/3.0/CHANGELOG.md#300)

    v3.0 新增 Consumer Group 用于管理多个消费者、支持配置 DNS 解析域名类型的顺序、新增 AI 平面用于智能分析和可视化配置与流量、全面支持 ARM64、新增 gRPC 客户端、实现数据面与控制面的完全分离、提供控制面的服务发现支持、新增 xRPC 框架、支持更多四层可观测性、集成 OpenAPI 规范、全面支持 Gateway API。

- [APISIX 云原生 API 网关 v2.15.0 发布](https://github.com/apache/apisix/blob/release/2.15/CHANGELOG.md#2150)  

    该版本主要新特性：支持用户自定义插件的优先级、支持通过表达式决定插件是否需要执行、自定义错误响应、允许采集 Stream Route 上的指标。

- [Apollo 分布式配置管理系统 v2.0.0 发布 （CNCF 项目）](https://github.com/apolloconfig/apollo/releases/tag/v2.0.0)  

    该版本主要新特性：主页上增加公共命名空间列表视图、灰度规则支持在 IP 不固定的情况下的标签匹配、启用命名空间的导出/导入功能、大多数列表都新增 `DeletedAt`列支持唯一约束索引。

- [Arbiter：时速云开源基于 K8s 构建的可扩展调度和弹性工具](https://mp.weixin.qq.com/s/xF6Zij2FB2dq3QsZO6ch1g)

    [Arbiter](https://github.com/kube-arbiter/arbiter) 聚合各种类型的数据，用户可以基于这些数据管理、调度或扩展集群中的应用程序。它可以帮助 Kubernetes 用户了解和管理集群中部署的资源，进而提高企业应用程序的资源利用率和运行效率。

- [Argo CD GitOps 工具 v2.9.0 发布（CNCF 项目）](https://github.com/argoproj/argo-cd/releases/tag/v2.9.0)

    版本特性：为 k8s 客户端添加重试逻辑、为 repo 错误添加宽限期、支持 git 请求可配置、支持跨分片动态重新平衡集群功能、支持为 opentelemetry 输入额外属性、为 argocd-k8s-auth 添加 kubelogin 功能。

- [Argo CD 持续部署工具 v2.8.0 发布（CNCF 项目）](https://github.com/argoproj/argo-cd/releases/tag/v2.8.0)

    版本特性：添加 kubelogin 功能、允许用户在任意命名空间中使用 ApplicationSet 资源、为快照卷添加健康检查、新增插件生成器功能、支持从环境变量或命令行参数中指定监听地址、创建 job action、支持刷新 ExternalSecret。

- [Argo CD GitOps 工具 v2.6.0 发布（CNCF 项目）](https://github.com/argoproj/argo-cd/releases/tag/v2.6.0)

    版本特性：ApplicationSet 资源增加渐进式发布策略、允许用户为应用程序提供多个资源、允许多个 CRD 共享健康检查、支持反向代理扩展、argocd CLI 添加跨平台的文件加密工具 bcrypt 的支持。

- [Argo 成为 CNCF 毕业项目](https://mp.weixin.qq.com/s/l8veOjEZV4xlrtqdCWPljg)

    [Argo](https://github.com/argoproj) 让团队能够使用 GitOps，在 Kubernetes 上采用声明方式部署和运行云原生应用和工作流。
    Argo 的采用率自其成为 CNCF 孵化项目以来增长了 250%，并于今年 7 月通过了第三方安全审计，
    已经成为云原生技术堆栈和 GitOps 的重要组成部分。

- [Argo CD GitOps 工具 v2.5.0 发布（CNCF 项目）](https://github.com/argoproj/argo-cd/releases/tag/v2.5.0)

    该版本主要新特性：支持基于集群过滤应用程序、添加 Prometheus 健康检查、添加通知 API、支持 CLI 的自定义应用程序操作、增加对默认容器注释的支持、限制 redis 的出口规则、添加 Gitlab PR 生成器 webhook、新增 ApplicationSet Go 模板、新增 ArgoCD CLI 本地模板。

- [Argo 2022 年项目安全审计结果发布](https://mp.weixin.qq.com/s/m1-bnWKU54SYMfKW_xEkIA)  

    Argo 团队、CNCF 与软件安全公司 Ada Logics 合作，对 Argo 的四个项目进行安全审计。
    共发现 26 个问题：Argo CD 7 个，Argo Workflows 6 个，Argo Events 13 个。为 Argo CD 发布了七个 CVE，Argo Events 两个 CVE。
    截止报告发布时，所有可利用的问题都已修复，并作为安全建议发布在 [GitHub](https://github.com/orgs/argoproj/projects/19) 上。  
    审计报告全文: <https://github.com/argoproj/argoproj/blob/master/docs/argo_security_audit_2022.pdf>

- [Argo CD 持续部署工具 v2.4.0 发布（CNCF 项目）](https://github.com/argoproj/argo-cd/releases/tag/v2.4.0)

    该版本主要新特性：UI 添加 Web 终端——无需离开 Web 界面就能在运行的应用容器中启动一个 shell；引入对 Pod 日志和 Web 终端的访问控制；集成 OpenTelemetry Tracing。

- [Backstage 开发者门户构建平台的安全审计报告和威胁模型发布（CNCF 项目）](https://backstage.io/blog/2022/08/23/backstage-security-audit)  

    [审计](https://backstage.io/blog/assets/22-08-23/X41-Backstage-Audit-2022.pdf)共发现 10 个漏洞。
    在 Backstage [v1.5](https://backstage.io/docs/releases/v1.5.0) 中，其中的 8 个漏洞都已完全修复。
    尚待解决的 4 个问题中，3 个与速率限制和内部 DoS 问题相关。
    [威胁模型](https://backstage.io/docs/overview/threat-model)总结了操作员、开发人员和安全研究人员的主要安全考虑事项，涵盖 Backstage 典型设置中涉及的信任模型和角色、集成者的职责以及常见配置问题等。

- [Backstage 开发者门户构建平台 v1.4.0 发布（CNCF 项目）](https://github.com/backstage/backstage/releases/tag/v1.4.0)  

    该版本主要新特性：Search API 升级到 v1、新增后端系统（实验性）、大量命令行及授权后端符号弃用、增加了对 OpenAPI 规范中 $ref 处理的支持、增加 Apollo Explorer 支持（PoC）。

- [Beyla：Grafana 发布用于应用程序可观测性的开源 eBPF 自动仪表化工具](https://mp.weixin.qq.com/s/H5yw6jSeJdLoLFc32OTeyA)

    Beyla 能够报告 Linux HTTP/S 和 gRPC 服务的跨度信息和 RED 指标（速率-错误-持续时间），且无需插入探针进行代码修改即可完成此操作。Grafana Beyla 支持用 Go、NodeJS、Python、Rust、Ruby、.NET 等编写的 HTTP 和 HTTPS 服务。还支持用 Go 编写的 gRPC 服务。

### C

- [Calico CNI 插件 v3.26.0 发布（CNCF 项目）](https://github.com/projectcalico/calico/blob/v3.26.0/release-notes/v3.26.0-release-notes.md)

    版本特性：将 calico-node 和 calico-cni-plugin 服务账户分开、利用内核级路由过滤减少在系统的 CPU 使用率、支持 Windows Server 2022、支持 OpenStack Yoga。

- [Calico CNI 插件 v3.25.0 发布（CNCF 项目）](https://github.com/projectcalico/calico/blob/v3.25.0/calico/_includes/release-notes/v3.25.0-release-notes.md)

    该版本主要新特性：优化 eBPF 数据平面，确保连接时间负载均衡（Connect Time Load Balancing）在规模更大的、快速变化的环境中工作；Felix 组件支持重写内部 readiness/liveness watchdog 的超时；Typha 组件支持优雅关闭。

- [Calico CNI 插件 v3.24.0 发布（CNCF 项目）](https://github.com/projectcalico/calico/blob/release-v3.24/calico/_includes/release-notes/v3.24.0-release-notes.md)

    该版本主要新特性：支持 IPv6 网络 wireguard 加密、通过 API 暴露 IPAM 配置和 IPAM block 亲和性、operator API 新增字段、支持分割 IP 池、从 pod 安全策略过渡到 pod 安全标准。

- [Carina 云原生本地存储项目 v0.11.0 发布](https://github.com/carina-io/carina/releases/tag/v0.11.0)  

    该版本主要新特性：支持 Cgroup v2、移除 HTTP Server、升级 CSI 官方镜像版本、移除 ConfigMap 同步控制器、carina 镜像移动到单独命名空间、增加 carina e2e 测试用以替代原有的 e2e 测试代码（开发测试中）、优化 Storageclass 参数的 pvc 调度逻辑。

- [Carina 本地存储项目 v0.10.0 发布（CNCF 项目）](https://github.com/carina-io/carina/releases/tag/v0.10.0)

    该版本主要新特性：支持将裸盘挂载到容器内直接使用、velero 备份存储卷支持、新增 CRD 资源 NodeStorageResource 替代原将磁盘设备注册到 Node 节点的方式、使用 job 生成 webhook 证书，替代原有脚本生成证书方式等。

- [cdk8s+：AWS 开源的 Kubernetes 开发框架正式可用](https://aws.amazon.com/blogs/containers/announcing-general-availability-of-cdk8s-plus-and-support-for-manifest-validation/)

    [cdk8s+](https://github.com/cdk8s-team/cdk8s) 允许用户使用熟悉的编程语言和面向对象的 API 来定义 Kubernetes 应用和可复用的抽象。
    相较于去年发布的 beta 版本，正式版本新增功能包括：隔离 pod 网络，只允许指定的通信；改进在同一节点上运行多个 pod的配置机制；集成 [Datree](https://github.com/datreeio/datree-cdk8s) 插件，使用第三方策略执行工具检查 Kubernetes 中的错误配置。

- [Cert-manager 云原生证书管理项目 v1.12.0 发布（CNCF 项目）](https://github.com/cert-manager/cert-manager/releases/tag/v1.12.0)

    版本特性：将二进制文件和测试分离撑独立的 Go 模块、增加对 JSON 日志的支持、支持带有 Vault 的短暂服务账户令牌、支持 ingressClassName 字段、新增标志用于指定哪些资源需要被注入到  Kubernetes 对象中。

- [Cert-manager 云原生证书管理项目 v1.11.0发布（CNCF 项目）](https://github.com/cert-manager/cert-manager/releases/tag/v1.11.0)

    该版本主要新特性：支持使用 Azure Workload Identity Federation 进行认证、支持指定 cert-manager 在与 ACME 服务器通信时使用的信任存储、支持 gateway API v1beta1、启用针对 Kubernetes 1.26 的测试。

- [Cert-manager 云原生证书管理项目 v1.10.0 发布（CNCF 项目）](https://github.com/cert-manager/cert-manager/releases/tag/v1.10.0)

    该版本主要新特性：使用 trivy 扫描本地构建的容器；如果目标 Secret 配置错误或在请求后创建，重新同步签署请求；增加从 Kubernetes Secret 加载 Vault CA Bundle 的选项；支持在 chart 部署的所有资源上添加相同的标签。

- [Cert-manager 云原生证书管理项目升级成为 CNCF 孵化项目](https://www.cncf.io/blog/2022/10/19/cert-manager-becomes-a-cncf-incubating-project/)

    Cert-manager 是 Kubernetes 的一个插件，用于自动管理和颁发各种来源的 TLS 证书，为云原生工作负载提供加密保护。近日，CNCF 技术监督委员会已经投票接受 cert-manager 成为 CNCF 孵化项目。

- [Cert-manager 云原生证书管理项目 v1.9.0 发布（CNCF 项目）](https://github.com/cert-manager/cert-manager/releases/tag/v1.9.0)  

    该版本主要新特性：支持使用cert-manager certificate（alpha）、支持通过 Ingress 资源上的注释配置 ingress-shim 证书。

- [ChaosMeta 云原生自动化混沌工程 v0.6 发布](https://github.com/traas-stack/chaosmeta/releases/tag/v0.6.0)

    版本特性:新增 DNS 异常、日志注入等故障能力；在可视化编排界面中提供对流量注入、度量等各类节点的支持；可视化支撑演练全流程。

- [ChaosMeta 混沌工程 v0.5 发布](https://mp.weixin.qq.com/s/4VG5TkQPotr_BrweIznW_w)

    版本特性：新增平台界面组件，主要提供空间管理、用户权限管理、编排实验、实验结果等功能；新增度量组件，提供对监控项的值、Pod 相关数、http 请求、tcp 请求进行预期判断；新增流量注入组件，当前只支持 HTTP 流量类型的注入，后续会逐步补充 RPC、DB client、redis client 等其他类型的流量注入能力。

- [Chaosblade 混沌工程项目 v1.7.0 发布（CNCF 项目）](https://github.com/rook/rook/releases/tag/v1.10.0)

    该版本主要新特性：添加 time travel 实验、添加插件 zookeeper 和 clickhouse、jvm 性能优化、支持 blade 服务器的 mTLS 认证。

- [Chaos Mesh 混沌工程平台 v2.5.0 发布（CNCF 项目）](https://github.com/chaos-mesh/chaos-mesh/releases/tag/v2.5.0)

    该版本主要新特性：支持多集群混沌实验、HTTPChaos 增加 TLS 支持、允许在 Helm 模板中为 controller manager 和仪表盘配置 Pod 安全上下文、StressChaos 支持 cgroups v2。

- [Chaos Mesh 混沌工程测试平台 v2.2.0 发布（CNCF 项目）](https://github.com/chaos-mesh/chaos-mesh/releases/tag/v2.2.0)

    该版本主要新特性：新增 StatusCheck 功能，用于检查应用程序的健康状况，当应用程序不健康时中止混沌实验；支持使用 `Chaosctl` 进行 outbound 强制恢复、在 dashboard 中新增基于流程图创建工作流的界面等。

- [ChaosMeta：蚂蚁集团开源的云原生自动化混沌工程平台](https://mp.weixin.qq.com/s/QUiWocMwbnSoUyfAu1z-cg)

    [ChaosMeta](https://github.com/traas-stack/chaosmeta) 设计上是包含了完整混沌工程生命周期的一站式演练综合解决方案，涵盖了准入检查、流量注入、故障注入、故障度量、恢复度量和故障恢复等多个阶段。现阶段，ChaosMeta 已经对外开放了丰富的故障注入功能，不仅支持单机部署和 Kubernetes 云原生部署，还支持 Kubernetes 本身和 Operator 等云原生故障场景的实验。

- [Cilium：基于 eBPF 的 CNI 项目 Cilium 升级成为 CNCF 的毕业项目](https://mp.weixin.qq.com/s/zMy5efZc0kf3UWpNAxC8_w)

    Cilium 是一种基于 eBPF 的开源云原生解决方案，用于提供、保护和观测工作负载之间的网络连接。成为 CNCF 毕业项目不是终点，而是创建 Cilium 生态系统的开始。Cilium 计划对非 Kubernetes 工作负载（如裸机和虚拟机）提供支持。

- [Cilium CNI 插件 v1.14.0 发布（CNCF 项目）](https://github.com/cilium/cilium/releases/tag/v1.14.0)

    版本特性：支持双向认证、支持以 DaemonSet 的形式部署 Envoy、支持对节点间的流量进行 WireGuard 加密并且可以在 WireGuard 上使用 Layer 7 策略、Cilium Mesh可以在云端和异构工作负载之间提供一致的网络连接、支持通过 Layer 2 传输协议向本地网络广播外部 IP 地址、支持多个 IPAM 池、BIG TCP 支持 IPv4。

- [Cilium CNI 插件 v1.13.0 发布（CNCF 项目）](https://github.com/cilium/cilium/releases/tag/v1.13.0)

    版本特性：支持 Gateway API v0.5.1、增加 IPv6 BIG TCP 支持、支持 LoadBalancer IP 地址管理、初步支持 SCTP、支持根据标签选择器对节点进行细粒度的配置、支持 k8s 1.26、支持通过 BGP 控制平面宣告 LoadBalancer 服务的功能、支持通过内置 Envoy代理实现现有 Kubernetes service 的 L7 负载均衡、Ingress 资源可以共享 Kubernetes LoadBalancer 资源、datapath 支持 mTLS、支持 Service 内部流量策略、对所有镜像进行 cosign 签名并为每个镜像创建 SBOM。

- [Cilium 发布安全审计报告和模糊测试审计报告](https://www.cncf.io/blog/2023/02/13/a-well-secured-project-cilium-security-audits-2022-published/)

    [安全审计](https://github.com/cilium/cilium.io/blob/main/Security-Reports/CiliumSecurityAudit2022.pdf)和[模糊测试](https://github.com/cilium/cilium.io/blob/main/Security-Reports/CiliumFuzzingAudit2022.pdf)共发现了 30 个问题，并未发现关键风险漏洞。
    其中，两个是中风险问题，第一个问题是缺少易于访问的关于安全运行 Cilium 的文档，该问题 [PR](https://github.com/cilium/cilium/pull/23599) 正在处理中；
    第二个是在配置错误的情况下可能无法解锁互斥锁 mutex，该[问题](https://github.com/cilium/cilium/pull/23077)已修复。其余都是低风险或信息性的问题。

- [Cilium 2022 年度报告发布](https://github.com/cilium/cilium.io/raw/main/Annual-Reports/Cilium%20Annual%20Report%202022.pdf)

    报告记录了 2022 年 Cilium 项目的贡献者增长、版本亮点、用户调查结果、生产落地情况、社区活动，以及 2023 年的发展方向。
    在 2023 年，Cilium service mesh 将发展成熟；通过 eBPF 捕获的内核数据将帮助周边生态为终端用户建立更好的平台；供应链安全功能将得到加强.

- [Cilium CNI 插件 v1.12.0 发布（CNCF 项目）](https://github.com/cilium/cilium/releases/tag/v1.12.0)  

    该版本主要新特性：推出 Cilium Service Mesh（多控制平面、边车/无边车、Envoy CRD)、集成 Ingress Controller、增加 K8s 服务拓扑感知提示、初始 NAT46/64 实现、支持 Pod 启用 BBR 拥堵控制并将带宽管理器移出 beta、支持在集群池 v2 IPAM 模式下动态分配 pod CIDR、支持设置服务后端状态、出口网关升级到稳定状态。

- [Cloud Custodian 云资源管理工具 v0.9.20 发布（CNCF 项目）](https://github.com/cloud-custodian/cloud-custodian/releases/tag/0.9.20.0)

    该版本主要新特性：增加 K8s admission controller 模式、添加角色和集群角色资源。

- [Cloud Custodian 云资源管理工具升级为 CNCF 孵化项目](https://mp.weixin.qq.com/s/Z3knP5tJ4om3nW1nqXEjsA)  

    [Cloud Custodian](https://github.com/cloud-custodian/cloud-custodian)是一个云治理即代码工具，允许用户通过代码来管理和自动执行云安全、合规性、运营和成本优化的策略，包括编写管理 Kubernetes 资源的策略。与其他基于云的治理工具相比，提供了一个非常简单的 DSL 来编写策略及其跨云平台的一致性。

- [Cloud Native App Initializer：阿里巴巴正式开源云原生应用脚手架](https://mp.weixin.qq.com/s/5hsrCfAdO7gBOJcT6fLpbg)

    [云原生应用脚手架](https://github.com/alibaba/cloud-native-app-initializer)基于 Spring 开源的 Initializr 项目构建。
    不仅能够帮助用户管理依赖，还能帮助用户生成测试或者可以直接使用的代码片段，用户创建完工程就可以进行测试，测试完就可以基于示例代码进行项目开发。
    因此，基于云原生应用脚手架构建项目仅需完成：新建工程和运行测试即可。

- [Cluster API 声明式集群生命周期管理工具 v1.5.0 发布（CNCF 项目）](https://github.com/kubernetes-sigs/cluster-api/releases/tag/v1.5.0)

    版本特性：支持微服务预检查以提高集群稳定性、在 classy 集群中支持并发的 MachineDeployment 升级、在 clusterctl 中支持附加提供程序、改进规模化部署时的性能、通过 MachinePool Machine 提高 MachinePool 的可观测性、clusterctl 插件允许从 clusterctl 调用自定义代码、通过自定义 Kube State Metrics 配置可以收集更多指标。

- [Cluster API 声明式集群生命周期管理工具 v1.3.0 发布（CNCF 项目）](https://github.com/kubernetes-sigs/cluster-api/releases/tag/v1.3.0)

    该版本主要新特性：支持自动更新由Kubeadm 控制平面提供商提供的机器证书、可以从新的容器镜像注册中心 registry.k8s.io 发布和消费集群 API 镜像、允许在控制平面节点上创建没有污点的集群、clusterctl 现在可以管理 IPAM 和 RuntimeExtension 提供者。

- [Clusternet 多云多集群管理项目 v0.16.0 发布（CNCF 项目）](https://github.com/clusternet/clusternet/releases/tag/v0.16.0)

    更新内容：支持将工作负载从未就绪的集群迁移到健康的备用集群上、支持为未就绪集群添加污点、可配置集群得分的百分比来进行调度、添加许可证扫描报告和状态、支持记录健康检查的指标数据。

- [Clusternet 多云多集群管理项目 v0.15.0 发布（CNCF 项目）](https://github.com/kubernetes-sigs/cluster-api/releases/tag/v1.4.0)

    版本特性：将所有控制器从 clusternet-hub 中移出，放入一个名为 “clusternet-controller-manager”的新组件中；增加多集群服务发现的功能门；为调度器迁移验证添加单元测试。

- [Clusternet 分布式云原生多集群管理项目入选 CNCF 沙箱项目](https://www.51cto.com/article/748691.html)

    3 月 8 日，[Clusternet](https://github.com/clusternet/clusternet) 通过 CNCF 基金会 TOC 委员会的评定，成功入选 CNCF 沙箱项目。
    Clusternet 通过组件化的、无侵入、轻量化的方式，将Kubernetes 强大的单集群能力扩展至多集群，并且很好地兼容云原生生态。
    未来，Clusternet 将探索更丰富多集群的落地场景，推动建立功能完备、API 标准化的多集群框架。

- [Clusternet 多云多集群管理项目 v0.13.0 发布](https://github.com/clusternet/clusternet/releases/tag/v0.13.0)

    该版本主要新特性：增加从父集群到子集群 pod 的路由功能、添加调度器配置并支持自定义调度器插件、支持 discovery v1beta1、只为 k8s v1.21.0 及更高版本提供发现 endpointslice 的支持、使用阈值聚合工作节点标签、支持按集群 subgroup 进行调度、为在 capi 中运行的 clusternet-agent 更新 RBAC 规则。

- [Constellation：Edgeless Systems 开源首个机密计算 Kubernetes](https://blog.edgeless.systems/hi-open-source-community-confidential-kubernetes-is-now-on-github-2347dedd8b0c)  

    [Constellation](https://github.com/edgelesssys/constellation) 旨在提供一个端到端的机密 K8s 框架。
    它将 K8 集群包裹在一个机密的上下文中，与底层云基础设施屏蔽开。
    其支持运行和扩展所有容器；提供基于 Sigstore 的节点和工件证明；提供基于 Cilium 的网络方案等。

- [Consul 服务发现框架 v1.13.0 发布（CNCF 项目）](https://github.com/hashicorp/consul/releases/tag/v1.13.0)

    该版本主要新特性：移除对 Envoy 1.19 的支持；Cluster Peering 支持联合 Consul 集群用于服务网格和传统服务发现；允许在不修改目录的情况下，通过透明代理模式的终端网关路由出口流量。

- [containerd 容器运行时 v1.7.0 发布（CNCF 项目）](https://github.com/containerd/containerd/releases/tag/v1.7.0)

    版本特性：新增 Sandbox API，简化更高级别的容器组的管理，为 shim 实现和客户端提供了新的扩展点；新增 Transfer Service，可用于在源和目标之间传输工件对象；支持扩展节点资源接口 NRI 的范围，实现常见的可插拔式运行时扩展；增加对 CDI 设备注入的支持；支持 cgroups blockio；为增强型重启管理器增加重启策略；初步支持 gRPC shim。

- [containerd 完成模糊测试审计](https://mp.weixin.qq.com/s/IUgdPaT6OAhPW5uCPlteEA)

    此次 [containerd 审计](https://containerd.io/img/ADA-fuzzing-audit-21-22.pdf)共增加了 28 个模糊测试器（fuzzer），涵盖了广泛的容器运行时功能。
    在此审计过程中，在 OCI 镜像导入程序中发现了一个[漏洞](https://github.com/containerd/containerd/security/advisories/GHSA-259w-8hf6-59c2)：导入恶意镜像可能会导致节点的 DoS 攻击。
    该问题已在 containerd 1.5.18 和 1.6.18 中修复。

- [Contour Kubernetes ingress 控制器 v1.26.0 发布（CNCF 项目）](https://github.com/projectcontour/contour/releases/tag/v1.26.0)

    版本特性：支持两个以上端口的网关监听器、支持输出状态更新负载指标、支持限制 Contour 实例所监测资源的命名空间、引入新的临界访问日志级别、支持定义默认的全局速率限制策略。

- [Contour Kubernetes ingress 控制器 v1.25.0 发布（CNCF 项目）](https://github.com/projectcontour/contour/releases/tag/v1.25.0)

    版本特性：HTTPProxy 支持配置 IP 过滤器、支持将追踪数据导出到 OpenTelemetry、支持所有主机的外部授权、支持内部重定向。

- [Contour Kubernetes ingress 控制器 v1.22.0 发布（CNCF 项目）](https://github.com/projectcontour/contour/releases/tag/v1.22.0)  

    该版本主要新特性：支持 Gateway API v0.5.0、允许在单一的路由中为一组条件配置一个直接响应、可以为用户证书验证启用撤销检查、合并访问记录和 TLS 密码套件验证。

- [Contour Kubernetes ingress 控制器 v1.21.0 发布 （CNCF 项目）](https://github.com/projectcontour/contour/releases/tag/v1.21.0)  

    该版本主要新特性：Contour 访问 leader election 资源的 RBAC 转移至命名空间角色；容器镜像现在只在 GitHub 容器注册中心（GHCR）上发布；新增 `contour gateway-provisioner` 命令和部署清单，用于动态配置 Gateways。

- [CoreDNS DNS 服务器 v1.11.0 发布 （CNCF 项目）](https://github.com/coredns/coredns/releases/tag/v1.11.0)

    版本特性：支持通过 QUIC 协议（doq）接受 DNS 连接、支持对 CNAME 记录的目标进行重写、kubernetes 插件中移除对 Endpoint 和 Endpointslice v1beta 的支持。

- [Cortex Prometheus 长期存储方案 v1.14 发布](https://github.com/cortexproject/cortex/releases/tag/v1.14.0)

    该版本主要新特性：移除对块存储的支持、实验性地支持垂直查询分片、启用 PromQL @修改器、可以使用 OTel 收集器将追踪信息发送到多个目的地、多项性能改进和问题修复。

- [Cortex 分布式 Prometheus 服务 v1.13.0 发布（CNCF 项目）](https://github.com/cortexproject/cortex/releases/tag/v1.13.0)  

    该版本主要新特性：新增元数据 API 查询器的 streaming 功能、为 compactor 提供实验性的shuffle sharding 支持、修复 Distributor 和 Ruler的内存泄漏、在分发请求时加入一个抖动来重置每个 pod 的初始时间。

- [Crane 成本优化工具推出开源云原生应用碳排放计算优化器](https://mp.weixin.qq.com/s/D46-7S20kaMF4CH_H5oTuA)

    碳排放计算优化器基于运行在 Kubernetes 平台上的应用的实际资源消耗，计算对应服务器功耗，进而计算出应用运行所产生的碳排放量。
    此外，还支持提供 Pod 资源配置、workload 副本数、HPA 参数配置等的优化建议，以及优化后的功耗和碳排放推算结果。

- [CRI-O 容器运行时 v1.28.0 发布（CNCF 项目）](https://github.com/cri-o/cri-o/releases/tag/v1.28.0)

    版本特性：允许用户禁用 Pod 的主机端口映射、新增指标以显示 Pod 和容器何时卡在创建的不同阶段、支持指定 kubelet 不要对某些镜像执行垃圾回收、添加版本升级自动化脚本、支持可配置指标输出器的命名空间、支持通过 CRI 的镜像策略验证错误。

- [CRI-O：CNCF 宣布容器运行时项目 CRI-O 毕业](https://mp.weixin.qq.com/s/p7ogT3pAtbj17qrDh7acHQ)

    CRI-O 为 Kubelet 提供了一个安全、高效和稳定的容器运行时接口实现，用于在生产 Kubernetes 环境中编排 Open Container Initiative（OCI）容器。未来，CRI-O 计划改进上游文档、自动化发布过程、增加节点上的 Pod 密度等等。该项目还正在努力将某些部分移动到 Rust 语言。

- [CRI-O 容器运行时 v1.26.0 发布（CNCF 项目）](https://github.com/cri-o/cri-o/releases/tag/v1.26.0)

    该版本主要新特性：移除对 CRI v1alpha2 的支持（支持 v1）、增加对 OTLP 追踪支持、为 OTel 追踪添加日志和 GRPC 错误代码支持、支持 Evented PLEG、增加 seccomp 通知器功能、对没有基础设施的容器增加检查点和恢复容器的支持、允许完全更新运行时配置、允许在重载配置时添加其他运行时以及改变默认运行时。

- [CRI-O 容器运行时 v1.25.0 发布（CNCF 项目）](https://github.com/cri-o/cri-o/releases/tag/v1.25.0)  

    该版本主要新特性：支持设置运行时 pod 的最大日志文件大小、能够执行 Kubelet 的用户命名空间配置、新增注释用于配置容器的电源管理、 增加最小 checkpoint/restore 支持、通过 sigstore 签名来签署静态二进制包。

- [CRI-O 容器运行时 v1.24.0 发布（CNCF 项目）](https://github.com/cri-o/cri-o/releases/tag/v1.24.0)

    该版本主要新特性：默认阻止没有 CAP_SYS_ADMIN 的容器的 `unshare` 系统调用、使用任务集来生成新的 cri-o 运行命令、在 CRI-O HTTP API 中添加暂停和取消暂停功能。

- [Crossplane 云原生控制平面构建框架完成模糊测试安全审计](https://mp.weixin.qq.com/s/BJXg8CCjaHFK29hxWe9W-g)

    此次模糊测试共发现 4 个问题。其中一个问题是：允许部分不受信任的用户控制 crossplane-runtime 在某个状态下分配的内存量，这可能会造成由于资源耗尽而导致 DoS 攻击。该漏洞的修复版本 [crossplane-runtime 0.19.2](https://github.com/crossplane/crossplane-runtime/releases/tag/v0.19.2) 和 [Crossplane 1.11.2](https://github.com/crossplane/crossplane/releases/tag/v1.11.2) 已经发布。

- [CubeFS 分布式存储系统 v3.3.0 发布（CNCF 项目）](https://github.com/cubefs/cubefs/releases/tag/v3.3.0)

    版本特性：添加对 ObjectNode 存储桶策略的支持、为 ObjectNode 添加跨域资源共享（CORS）支持、支持在执行重命名、删除、创建等操作时保证原子性、支持配置和动态调整 MP（多路复，Multiplexing）步长、添加对 UID 空间限制的支持、支持 autofs 挂载功能。

- [CubeFS 分布式存储系统 v3.1.0 发布（CNCF 项目）](https://github.com/cubefs/cubefs/releases/tag/v3.1.0)  

    该版本主要新特性：提供 QoS 服务以完善多租户隔离功能、优化混合云多级读缓存功能、支持两个副本的数据存储、卷支持配置 posixAcl 进行权限管理、为 datanode 添加数据分区总数限制。

- [CubeFS 分布式存储系统从 CNCF 沙箱升级为孵化项目](https://mp.weixin.qq.com/s/sAVaCa-yGEsJk3bUaJizmA)
  
    [CubeFS](https://github.com/cubefs) 是国内首个具备完整的对象及文件存储能力的云原生存储产品。
    CubeFS 支持多副本和纠删码引擎，提供多租户、多 AZ 部署、跨区域复制等特性；适用于大数据、AI、容器平台、数据库及中间件存算分离等广泛场景。

### D

- [Dapr 分布式应用运行时 v1.11.0 发布（CNCF 项目）](https://github.com/dapr/dapr/releases/tag/v1.11.0)

    版本特性：配置构件现在是一个 v1 版稳定的 API；服务调用支持调用非 Dapr 端点；支持在管理 API 中暂停、重启和清除工作流；引入密码学构建块；现在有两个可用的构建版本（包含所有的组件和只包含稳定组件）；Dapr 仪表板不再与控制平面一起安装；提供用于 Windows Server 2022 的容器镜像；应用程序健康检查升级为 stable。

- [Dapr 分布式应用运行时 v1.10.0 发布（CNCF 项目）](https://github.com/dapr/dapr/releases/tag/v1.10.0)

    版本特性：新增 Dapr Workflows 用于跨多个应用建立长期运行的进程或数据流、支持批量发布和订阅信息、允许创建可用任何语言编写的可插拔组件 SDK、新增 Multi-App Run 功能改善本地开发、弹性策略升级为 stable、新增服务调用指标。

- [Dapr 分布式应用运行时 v1.9.0 发布（CNCF 项目）](https://github.com/dapr/dapr/releases/tag/v1.9.0)

    该版本主要新特性：允许自定义可插拔组件、支持 OTel 协议、增加弹性观测指标、支持应用健康检查、支持设置默认弹性策略、允许使用任何中间件组件进行服务见调用、新增 pub/sub 命名空间消费者组、支持 Podman 容器运行时。

- [DeepFlow 自动化云原生可观测平台的首个开源版本正式发布](https://mp.weixin.qq.com/s/79wZ00RKoei_boZfiUmqgg)  

    [DeepFlow](https://github.com/deepflowys/deepflow) 是云杉网络研发的可观测性平台，基于 eBPF 等技术，实现自动同步资源、服务、K8s 自定义 Label 并作为标签统一注入到观测数据中。
    它能够自动采集应用性能指标和追踪数据而无需插码，SmartEncoding 创新机制将标签存储的资源消耗降低 10 倍。
    此外，还能集成广泛的数据源，并基于 SQL 提供北向接口。

- [Devspace K8s 开发工具成为 CNCF 沙箱项目](https://mp.weixin.qq.com/s/7ySQLtyYBX1ZDLvpeVObvQ)

    12 月 15 日，CNCF 宣布 [DevSpace](https://github.com/loft-sh/devspace) 正式成为 CNCF 沙箱项目。
    通过 Devspace，可以直接在 Kubernetes 中构建、测试和调试应用；可以使用热重载进行开发；
    统一团队内部以及跨开发、暂存和生产的部署工作流；自动执行镜像构建和部署的重复性任务。

- [DevSpace K8s 开发工具 v6.0 发布](https://github.com/loft-sh/devspace/releases/tag/v6.0.0)  

    该版本主要新特性：引入 pipeline 用于 管理 devspace.yaml 中的任务、新增导入功能将不同 devspace.yaml 文件合并在一起、新增 proxy command 在本地计算机上运行在容器中执行的命令。

- [Dragonfly 镜像和文件分发系统 v2.1.0 发布 （CNCF 项目）](https://github.com/dragonflyoss/Dragonfly2/releases/tag/v2.1.0)

    版本特性：可视化控制台 v1.0 发布、新增虚拟网络拓扑探索功能、支持 Dragonfly 作为 JuiceFS 的后端存储、支持在 Manager 中控制 Scheduler 的功能、新增个人访问令牌功能、新增 Cluster 资源单位（Cluster 代表一个 P2P 集群）。

### E

- [Envoy v1.28.0 发布（CNCF 项目）](https://www.envoyproxy.io/docs/envoy/v1.28.0/version_history/v1.28/v1.28.0)

    版本特性：工作节点支持延迟集群的创建、增加对 ADS 的 EDS（Endpoint Discovery Service）响应缓存支持、为下游和上游网络过滤器添加了 ECDS（External Configuration Discovery Service）支持、即使在源集群和上游集群的区域数量不同的情况下也支持启用区域感知路由、将在 v1.30 中废弃 OpenTracing 和 OpenCensus。

- [Envoy v1.27.0 发布（CNCF 项目）](https://github.com/envoyproxy/envoy/releases/tag/v1.27.0)

    版本特性：引入新的 golang 网络过滤器、新增用于在资源不足时拒绝请求的负载削减点（Load shed point）、支持 CONNECT-UDP、引入 Open Telemetry 兼容的统计数据收集器、新增用于打印 CEL 表达式的访问日志格式化器。

- [Envoy v1.26.0 发布（CNCF 项目）](https://www.envoyproxy.io/docs/envoy/v1.26.0/version_history/v1.26/v1.26.0)

    版本特性：增加了对通用代理的跟踪支持、支持在 http 过滤器链的任何位置修改请求和响应头信息、支持在动态元数据中设置 JWT 认证失败状态代码和消息、增加过滤器状态输入、支持在 TLS 握手和过滤器匹配之前启用速率限制、支持上游访问日志中的路由信息、支持动态地禁用 TCP 隧道、增加负载均衡器 Maglev 扩展和环形哈希扩展。

- [Envoy v1.23.0 发布（CNCF 项目）](https://www.envoyproxy.io/docs/envoy/v1.23.0/version_history/v1.23/v1.23.0)  

    该版本主要新特性：在一个 SDS 请求中发送多个集群或监听器的 SDS 资源、通过 HTTP 过滤器的配置名称来获取过滤器配置、监听器过滤器统计更新、dns_resolver 增加对多个地址的支持、为监听器过滤器添加动态监听器过滤器配置等。

- [Envoy Gateway API 网关 v0.6 发布](https://github.com/envoyproxy/gateway/releases/tag/v0.6.0)

    版本特性：添加容器端口指标、支持设置全局速率限制的超时和故障开启/关闭、为路由添加 serviceImport 后端、支持负载均衡器类、在 EnvoyProxy 资源下引入并发性、在命名空间模式下为 envoy 网关实现角色和角色绑定、在 EnvoyProxy API 中引入 initContainers 字段、为 CORS 添加 ir 和 xds 转换。

- [Envoy Gateway API 网关 v0.5 发布](https://gateway.envoyproxy.io/v0.5.0/releases/v0.5.html)

    版本特性：添加数据平面代理遥测、支持直接配置 xDS、支持基于 IP 地址的不同速率限制、支持配置 EnvoyProxy Pod 标签、支持配置 EnvoyProxy 部署策略设置、卷和卷挂载、支持将 EnvoyProxy 配置为 NodePort 类型服务、添加 Pprof 调试支持。

- [Envoy Gateway 基于 Envoy 的网关 v0.4 发布](https://gateway.envoyproxy.io/v0.4.0/releases/v0.4.html)

    版本特性：支持通过 Helm 安装 Envoy Gateway；新增初始框架用于扩展 Envoy Gateway；支持基于 IP 子网的速率限制；支持自定义 Envoy 代理引导配置、Envoy 代理镜像和服务配置注释、资源和安全上下文设置等；支持 EDS（Endpoint Discovery Service)。

- [Envoy Gateway v0.3 发布](https://gateway.envoyproxy.io/v0.3.0/releases/v0.3.html)

    版本特性：支持扩展的 Gateway API 字段；支持 TCP 路由 API、UDP 路由 API 和 GRPC 路由 API；支持全局速率限制；支持请求认证。

- [Envoy Gateway API 网关 v0.2 发布](https://github.com/envoyproxy/gateway/releases/tag/v0.2.0)

    该版本主要新特性：支持 Kubernetes、支持 Gateway API 资源。

- [Envoy Gateway 开源](https://blog.envoyproxy.io/introducing-envoy-gateway-ad385cc59532)

    [Envoy Gateway](https://github.com/envoyproxy/gateway) 正式成为 Envoy 代理家族的新成员，该项目旨在降低将 Envoy 作为 API 网关的使用门槛。
    Envoy Gateway 可以被认为是 Envoy Proxy 核心的一个封装器。
    它提供的功能包括：为网关用例提供简化的 API、开箱即用的控制器资源、控制平面资源、代理实例等的生命周期管理能力以及可扩展的 API 平面。

- [Emissary Ingress 云原生 ingress 控制器和 API 网关 v2.3.0 发布（CNCF 项目）](https://github.com/emissary-ingress/emissary/releases/tag/v2.3.0)  

    该版本主要新特性：当使用 lightstep 作为 driver 时，可以在 `TracingService` 的配置中设置`propagation_modes`；支持在 `Host`和`TLSContext`资源中设置`crl_secret`，以比对证书撤销列表检查对等证书；优化与外部日志服务的通信等。

- [eunomia-bpf：eBPF 轻量级开发框架正式开源](https://mp.weixin.qq.com/s/fewVoIKbLn5fYbXUaDyTpQ)

    [eunomia-bpf](https://gitee.com/anolis/eunomia) 由各高校和龙蜥社区共同开发，旨在简化 eBPF 程序的开发、分发、运行。在 eunomia-bpf 中，只需编写内核态代码即可正确运行，在部署时不需要重新编译，并提供 JSON/WASM 的标准化分发方式。

### F, G

- [Falco 运行时安全项目 v0.35.0 发布（CNCF 项目）](https://github.com/falcosecurity/falco/releases/tag/0.35.0)

    版本特性：引入指标快照选项和新的指标配置、支持使用 cosign 对发布的容器镜像进行签名、允许自定义 CA 证书和存储、支持管理 Talos 预构建驱动程序、Mesos 不再支持元数据增强功能。

- [Falco 2023 年安全审计结果发布](https://mp.weixin.qq.com/s/Uae58tOQpqOfV0vCoXBsqw)

    [审计报告](https://github.com/falcosecurity/falco/blob/master/audits/SECURITY_AUDIT_2023_01_23-01-1097-LIV.pdf)发现了一个中等严重程度的漏洞和若干低严重程度和信息严重程度的漏洞，不存在严重程度高的漏洞。所有问题已在 Falco 0.34.0 和 0.34.1 补丁版本中修复。

- [Falco 运行时安全项目 v0.34.0 发布（CNCF 项目）](https://github.com/falcosecurity/falco/releases/tag/0.34.0)

    版本特性：支持手动下载和应用相关的规则 [`application_rules.yaml`](https://github.com/falcosecurity/rules/tree/main/rules)、新检测规则使用 PTRACE 向进程注入代码、规则结果添加编译条件上下文、允许现代 bpf 探针为一个环形缓冲区分配一个以上的 CPU、添加 webserver 端点以检索内部版本号、在 systemd unit 中支持多个驱动。

- [Falco 运行时安全项目 v0.32.0 发布（CNCF 项目）](https://github.com/falcosecurity/falco/releases/tag/0.32.0)

    该版本主要新特性：新增配置项，当检测到规则或配置文件有变化时，触发 Falco 重启；支持检测权限过大的容器；支持检测共享主机 pid 和 IPC 命名空间的 pod 等。

- [Finch：AWS 开源的容器开发客户端命令行工具](https://aws.amazon.com/cn/blogs/opensource/introducing-finch-an-open-source-client-for-container-development/)

    [Finch](https://github.com/runfinch/finch) 可用于构建、运行和发布 Linux 容器。
    它为 Lima、nerdctl、containerd 和 BuildKit 等开源工具提供了原生的、可扩展的 macOS 客户端安装程序，简化在 macOS 上使用 Containerd。
    用户可以使用 Finch 在本地端创建和执行容器，并发布 OCI 容器镜像文件。

- [Flagger 渐进式交付项目 v1.31.0 发布（CNCF 项目）](https://github.com/fluxcd/flagger/blob/main/CHANGELOG.md#1310)

    版本特性：支持服务网格 Linkerd 2.12 及更高版本、删除 OSM e2e 测试。

- [Flagger 渐进式交付项目 v1.22.0 发布（CNCF 项目）](https://github.com/fluxcd/flagger/blob/main/CHANGELOG.md#1220)  

    该版本主要新特性：支持以 KEDA ScaledObjects 替代 HPA、在参数表中添加命名空间参数、为 Canary.Service 添加可选的 `appProtocol` 字段。

- [Fluent Operator 云原生日志收集方案 2.5.0 发布](https://github.com/fluent/fluent-operator/releases/tag/v2.5.0)

    版本特性：新增支持 7 个插件，包括 Prometheus Exporter、Forward、OpenTelemetry、HTTP、MQTT 等；增加对 Fluentd 作为 DaemonSet 运行的支持。

- [Fluent Bit 日志处理工具 v2.0.0 发布 （CNCF 项目）](https://github.com/fluent/fluent-bit/releases/tag/v2.0.0)

    该版本主要新特性：增加对 Traces 的支持（与 Prometheus 和 OpenTelemetry 完全集成）、允许 input 插件在一个单独的线程中运行、所有需启用安全的网络传输层将使用 OpenSSL、input 插件新增原生 TLS 功能、支持将更多的插件类型与 Golang 和 WebAssembly 集成、支持检查流经管道的数据、引入收集和处理内部指标的新 input 插件。

- [Fluentd 日志收集工具 v1.15.0 发布（CNCF 项目）](https://github.com/fluent/fluentd/releases/tag/v1.15.0)

    该版本主要新特性：支持设置日志收集的速率限制规则、支持处理 YAML 配置格式、允许设置重启 worker 的时间间隔。

- [Flux 持续交付工具 v2.0 发布（CNCF 项目）](https://github.com/fluxcd/flux2/releases/tag/v2.0.0)

    版本特性：GitOps 相关的 API 升级为 v1；Flux 控制器增加水平扩展和分片功能；Git bootstrap 功能升级为稳定；Flux项目供应链的构建、发布和证明部分暂时符合 SLSA Build Level 3；与Kubernetes Workload Identity for AWS、Azure和 Google Cloud 完全集成；警报功能优化。

- [Flux 持续交付工具成为 CNCF 毕业项目](https://mp.weixin.qq.com/s/3F3DHuKEZqqd7M6-im6B-A)

    [Flux](https://github.com/fluxcd/flux2) 是一套面向 Kubernetes 的持续渐进交付解决方案，支持开发者和基础设施团队的 GitOps 和渐进交付。自 2021 年 3 月成为 CNCF 孵化项目以来，Flux 及其子项目 Flagger 在用户群、集成、软件使用、用户参与度、贡献等方面增长了 200-500%。

- [Flux 持续交付工具 v0.34.0 发布（CNCF 项目）](https://github.com/fluxcd/flux2/releases/tag/v0.34.0)

    该版本主要新特性：Flux 控制器的日志与 Kubernetes 的结构化日志保持一致、允许为非 TLS 容器仓库定义 OCI 源、从多租户集群的容器仓库处提取 OCI 工件时优先考虑静态凭证而非 OIDC 提供者。

- [Gatekeeper 策略引擎 v3.13.0 发布 （CNCF 项目）](https://github.com/open-policy-agent/gatekeeper/releases/tag/v3.13.0)

    版本特性：支持将审计信息发布到 PubSub 系统中、验证工作负载资源的 ExpansionTemplates 升级为 beta、添加了实验性的 VAP 驱动器用于验证和审查资源对象的合规性、添加了对外部数据提供者审计缓存的支持、支持获得有关准入、审计和 gator CLI 的可观测性统计数据。

- [Gatekeeper 策略引擎 v3.10.0 发布 （CNCF 项目）](https://github.com/open-policy-agent/gatekeeper/releases/tag/v3.10.0)

    该版本主要新特性：移除 Pod 安全策略并迁移到 Pod 安全准入、Mutation 功能升级为稳定、引入工作负载资源的验证（alpha）、性能改进。

- [Gatekeeper 策略引擎 v3.9.0 发布（CNCF 项目）](https://github.com/open-policy-agent/gatekeeper/releases/tag/v3.9.0)  

    该版本主要新特性：增加约束模式验证测试、增加对外部数据提供商的 TLS 支持、增加 pod 安全上下文变量、支持验证子资源、允许在 gator 验证中跳过测试、为 gator 添加 dockerfile、添加 opencensus 和 stackdriver exporter。

- [Gateway API v1.0 发布](https://github.com/kubernetes-sigs/gateway-api/releases/tag/v1.0.0)

    版本特性: 将 CEL 验证规则纳入 CRD、Gateway、GatewayClass 和 HTTPRoute 升级成为 GA 功能、新增对 HTTPRoute 超时、从 Gateway 到后端的 TLS 配置、WebSocket 支持等实验性功能。

### H

- [Harvester 超融合基础设施 v1.2.0 发布](https://github.com/harvester/harvester/releases/tag/v1.2.0)

    版本特性：系统占用空间减少（更适合边缘场景）、支持资源限制自动调整、支持将模拟可信平台模块 (TPM) 添加到虚拟机、支持 SR-IOV 网络虚拟功能、新增 rancher-vcluster 插件和裸机容器支持、支持在 Harvester 集群中安装第三方容器存储接口 (CSI)、每个节点的 Pod 限制增加到 200。

- [HoloInsight：由蚂蚁集团开源的智能可观测平台](https://mp.weixin.qq.com/s/Tx7EKr0P_rhO-kltlW-wuQ)

    [HoloInsight](https://github.com/traas-stack/holoinsight) 是蚂蚁集团观测平台 AntMonitor 的开源版本，它主要聚焦基于日志的实时观测能力、业务指标监控以及时序智能和 AIOps。
    同时，它也融入可观测领域有共识的其他数据类型，比如 Trace，Event 等。

- [HAProxy Kubernetes Ingress Controller v1.8 发布](https://www.haproxy.com/blog/announcing-haproxy-kubernetes-ingress-controller-1-8/)  

    该版本主要新特性：降低容器中所有进程的权限，不再默认运行 privileged 容器；暴露了一个用于查看 pprof 诊断数据的端点；支持收集控制器内部的 Prometheus 指标，如分配的内存量和花费的 CPU 时间；若入口规则不匹配，支持自定义设置后端端口。

- [Harbor 容器镜像仓库 v2.9.0 发布（CNCF 项目）](https://github.com/goharbor/harbor/releases/tag/v2.9.0)

    版本特性：管理员可以访问包括扫描和未扫描的构件数量、危险构件和 CVE 等安全信息；提供更详细的信息来跟踪垃圾回收操作，并支持启用并行删除以加速垃圾回收的触发和执行过程；支持 OCI分发规范 v1.1.0-rc2，并增加了对 Notation 签名和 Nydus 转换的支持；引入一种新的机制，使用 Redis 进行乐观锁以在推送镜像时更新配额。

- [Harbor 容器镜像仓库 v2.8.0 发布（CNCF 项目）](https://github.com/goharbor/harbor/releases/tag/v2.8.0)

    版本特性：支持 OCI distribution spec v1.1.0-rc1、支持通过 CloudEvents 格式发送 Webhook 负载、支持跳过任务扫描器的自动更新拉取时间、移除 helm chart 仓库服务器 ChartMuseum。

- [Harbor 容器镜像仓库 v2.7.0 发布（CNCF 项目）](https://github.com/goharbor/harbor/releases/tag/v2.7.0)

    该版本主要新特性：添加 Jobservice 仪表盘，以监测和控制 job 队列、调度器和 worker；支持按块复制镜像 blob；为工件列表添加 WASM 过滤器。

- [Harbor 容器镜像仓库 v2.6.0 发布（CNCF 项目）](https://github.com/goharbor/harbor/releases/tag/v2.6.0)

    该版本主要新特性：引入缓存层，改善高并发情况下拉取工件的性能；增加 CVE 导出功能，允许项目所有者和成员导出由扫描仪生成的 CBR 数据；支持定期清理审计日志或按需运行，支持转发审计日志到远程系统日志终端；支持 WebAssembly 工件。

- [HashiCorp Vault 私密信息管理工具 1.11 新增 Kubernetes Secret 引擎](https://github.com/hashicorp/vault/blob/main/website/content/docs/secrets/kubernetes.mdx)  

    Kubernetes Secret 引擎可以动态生成 Kubernetes 服务账号令牌、服务账号、角色绑定和角色。创建的服务账号令牌有一个可配置的 TTL 值（Time To Live），当 lease 到期时，Vault 会自动删除创建的对象。对于每一个 lease，Vault 会创建一个连接到定义服务账号的令牌，服务账号令牌会返回给调用者。

- [Helm 完成模糊测试安全审计](https://mp.weixin.qq.com/s/sMPjsKC6gy9VkhXzI2bvzw)

    [本次审计](https://github.com/helm/community/tree/main/security-audit/FUZZING_AUDIT_2022.pdf)共编写了 38 个模糊器，测试范围覆盖 chart 处理、版本存储和仓库发现等关键部分。
    共发现 9 个问题（目前已修复 8 个），其中，4 个 空指针引用问题，4 个内存不足问题，1 个栈溢出问题。

- [Helm 包管理工具 v3.10.0 发布（CNCF 项目）](https://github.com/helm/helm/releases/tag/v3.10.0)  

    该版本主要新特性：支持通过命令行设置 json 值、允许在执行 helm list 的时候不输出表头、增加参数用于配置客户端节流限制、支持控制是否要跳过 kube-apiserver 的证书校验。

- [Helm Dashboard：Komodor 开源 Helm 图形界面](https://github.com/komodorio/helm-dashboard)

    Helm Dashboard 可在本地运行并在浏览器中打开，可用于查看已安装的 Helm Chart，查看其修订历史和相应的 k8s 资源。此外，还可以执行简单的操作，如回滚到某个版本或升级到较新的版本。

- [Helm v3.9.0 发布 （CNCF 项目）](https://github.com/helm/helm/releases/tag/v3.9.0)  

    该版本主要新特性：新增字段以支持向 post renderer 传递参数、签名过程增加了更多检查、更新对 Kubernetes 1.24 的支持。

- [Higress：阿里云开源的云原生网关](https://mp.weixin.qq.com/s/dgvd9TslzhX1ZuUNIH2ZXg)

    [Higress](https://github.com/alibaba/higress) 遵循 Ingress/Gateway API 标准，将流量网关、微服务网关、安全网关三合一，并在此基础上扩展了服务管理插件、安全类插件和自定义插件，高度集成 K8s 和微服务生态，包括 Nacos 注册和配置、Sentinel 限流降级等能力，并支持规则变更毫秒级生效等热更新能力。

- [Horizon：由网易云音乐开源的云原生应用部署平台](https://mp.weixin.qq.com/s/hRuHQ5egP_vzLD4IdKiOvA)

    [Horizon](https://github.com/horizoncd/horizon) 是一个基于 Kubernetes 的云原生持续部署平台，并且全面践行 GitOps。
    平台团队可以自定义创建版本化的服务模板，为业务应用程序和中间件定义符合统一标准的部署和运维。
    开发团队可以选择预先定义的模板，进行自动化的服务部署，确保基于 Kubernetes 的统一最佳实践。通过 Horizon GitOps 机制，确保任意变更（代码、配置、环境）持久化、可回滚、可审计。

- [HwameiStor 云原生本地存储成为 CNCF 沙箱项目](https://mp.weixin.qq.com/s/KvoQq24M8Pv4hDloVLtYVQ)

    6 月 23 日，由「DaoCloud 道客」开源的云原生本地存储 [HwameiStor](https://github.com/hwameistor/hwameistor) 高票入选 CNCF 沙箱项目。HwameiStor 将系统节点上的所有本地磁盘进行统一管理，形成不同类型的本地存储资源池，并通过 CSI 标准接口提供本地数据卷服务，为有状态的云原生应用或组件提供数据持久化能力。

### I

- [iLogtail 可观测数据采集器的全部代码开源](https://mp.weixin.qq.com/s/Cam_OjPWhcEj77kqC0Q1SA)

    近日，阿里云正式发布完整功能的 [iLogtail](https://github.com/alibaba/ilogtail) 社区版。
    本次更新开源全部 C++ 核心代码，该版本在内核能力上首次对齐企业版。新增日志文件采集、容器文件采集、无锁化事件处理、多租户隔离、基于 Pipeline 的新版配置方式等诸多重要特性。

- [ingress2gateway 发布，简化从 Ingress 迁移到 Gateway API](https://kubernetes.io/blog/2023/10/25/introducing-ingress2gateway/)

    [ingress2gateway](https://github.com/kubernetes-sigs/ingress2gateway) 用于将 Ingress 资源转换为 Gateway API 资源（特别是HTTPRoutes），目前暂不支持广泛使用的提供者特定注释和/或 CRD。未来计划引入对更多类型的 Gateway API 路由的支持。

- [Ingress-NGINX Controller v1.7.0 发布](https://github.com/kubernetes/ingress-nginx/releases/tag/controller-v1.7.0)

    版本特性：支持 golang 1.20、移除对 Kubernetes 1.23 的支持、集成 OpenTelemetry 模块。

- [Istio 服务网格 v1.20.0 发布（CNCF 项目）](https://istio.io/latest/news/releases/1.20.x/announcing-1.20/)

    版本特性：完全支持 Gateway API v1.0、新增对 Network 类型 WasmPlugin 的支持、允许流量镜像到多个目的地、对 ExternalName 服务进行增强、引入 Sidecar 容器的 StartupProbe 以加快启动速度、优化 Envoy 过滤器的一致性排序、增强 TCP 元数据交换控制、支持插入式根证书轮换等。

- [Istio 服务网格 1.19 发布（CNCF 项目）](https://istio.io/latest/news/releases/1.19.x/announcing-1.19/)

    版本特性：Gateway API v0.8.0 增加对服务网格的支持；Ambient Mesh 增加对 `ServiceEntry`、`WorkloadEntry`、`PeerAuthentication` 和 DNS 代理的支持；支持可选的客户端证书验证；支持配置非 Istio mTLS流量的密码套件。

- [Istio 社区发布 Istio 1.18 性能测试结果](https://istio.io/latest/docs/ops/deployment/performance-and-scalability/)

    Istio 负载测试网格由 1000 个服务和 2000 个 sidecar 组成，每秒有 70,000 个网格范围的请求。控制平面支持数千个服务，分布在数千个 Pod 中。数据平面性能受到客户端连接数、请求大小和响应大小、代理工作线程数、协议、CPU 核数等多种因素的影响。Istio 注入的每个功能可能会增加代理内部路径长度，以及影响延迟。

- [Istio 项目正式从 CNCF 毕业](https://mp.weixin.qq.com/s/QaHU3OtLVFKPCz69z8176Q)

    作为一个孵化项目进入 CNCF 不到一年的时间，Istio 就成为了 CNCF 的毕业项目，创下 CNCF 历史上最快毕业的项目记录。从 CNCF 毕业意味着，Istio 已经成为现代应用程序网络的关键组件，表明它是一个经过验证的成熟项目，可用于在生产中扩展关键应用程序。

- [Istio 服务网格 v1.18 发布（CNCF 项目）](https://istio.io/latest/news/releases/1.18.x/announcing-1.18/)

    版本特性：发布数据平面模式 —— Ambient Mesh（环境网格）；多项 Kubernetes Gateway API 改进，包括支持 v1beta1 版本、自动部署逻辑不再依赖 pod 注入；实现跨部署类型的并发配置一致性；Istioctl 增强。

- [Istio 服务网格 v1.17 发布（CNCF 项目）](https://istio.io/latest/news/releases/1.17.x/announcing-1.17/)

    版本特性：金丝雀升级的修订标签升级为 Beta、基于 Helm 安装 Istio 升级为 Beta、完全兼容最新版 Kubernetes Gateway API（0.6.1）、优化 IPv4/IPv6 双栈支持、增加对监听器过滤器补丁的支持、支持使用加解密技术 QuickAssist Technology (QAT) PrivateKeyProvider。

- [Istio 公布 2022 年安全审计结果](https://istio.io/latest/blog/2023/ada-logics-security-assessment/)

    本次审计未发现关键问题，共发现 11 个安全问题，所有问题目前都已修复。其中，发现的唯一一个 CVE 漏洞是 [Go 的请求走私漏洞](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41721)，最常见问题与 Istio 通过网络获取文件有关。

- [Istio v1.16 发布（CNCF 项目）](https://istio.io/latest/news/releases/1.16.x/announcing-1.16/)

    该版本主要新特性：三个功能升级为 beta：外部授权功能、Kubernetes Gateway API 实现、基于路由的 JWT 声明；增加对 sidecar 和入口网关的 HBONE 协议的实验性支持、支持 MAGLEV 负载均衡算法、通过 Telemetry API 支持 OpenTelemetry tracing provider。

- [Istio 正式成为 CNCF 孵化项目](https://istio.io/latest/blog/2022/istio-accepted-into-cncf/)  

    [Istio](https://github.com/istio/istio) 指导委员会于今年 4 月向 CNCF 呈递了移交项目的申请。经过近 5 个月的审核，现成为孵化项目。

- [Istio 社区推出无 sidecar 代理的 Istio 数据平面模式 Ambient Mesh](https://mp.weixin.qq.com/s/JpLPuqbPggXsQzFR5pii8A)  

    [Ambient Mesh](https://github.com/istio/istio/tree/experimental-ambient) 将数据面的代理从应用 pod 中剥离出来独立部署，彻底解决 mesh 基础设施和应用部署耦合的问题。
    通过引入零信任隧道（ztunnel）和 Waypoint proxy（路径点代理）实现零信任且减少了网格的资源占用，同时还可以与 sidecar 模式无缝互通，降低了用户的运维开销。

- [Istio v1.14 发布](https://istio.io/latest/news/releases/1.14.x/announcing-1.14/change-notes/)  

    该版本主要新特性：

    - 流量治理：支持向 Envoy 发送未就绪 endpoint；优化 egress 流量拦截功能；放宽设置 SNI 的限制条件；支持 filter 替换虚拟主机；在 Proxy Config 中增加 API `runtimeValues`，用于 Envoy 运行时配置。
    - 安全：支持通过 Envoy SDS API 进行 CA 集成、支持在 SDS 中使用 `PrivateKeyProvider`、支持工作负载的TLS 配置 API。
    - Telemetry：新增 OpenTelemetry 访问日志、在日志中添加 `WorkloadMode` 选项。
    - 扩展：支持 WasmPlugin 通过 `imagePullSecret` 从私有仓库中拉取镜像。

- [iSulad：容器引擎 iSulad 通过 Sandbox API 支持多沙箱运行时 Kuasar，提供高效和稳定的沙箱管理能力](https://mp.weixin.qq.com/s/D2vvEQmi5Lzo7QHDynRDrw)

    [iSulad](https://gitee.com/openeuler/iSulad) 引入了 Sandbox 的语义，新增核心模块 Sandbox ，实现了容器管理与沙箱管理的解耦。Sandbox API 的实现使 iSulad 能够直接通过 Controller 来管理沙箱，因此 Kuasar 容器运行时也无需创建 Pause 容器以兼容 OCI 标准，避免了 Pause 容器的冗余。

### J

- [Jaeger 分布式追踪系统 v1.46.0 发布（CNCF 项目）](https://github.com/jaegertracing/jaeger/releases/tag/v1.46.0)

    版本特性：默认启用 OTLP 接收器、增加对 OpenTelemetry SpanMetrics 连接器的支持。

- [Jaeger 分布式追踪系统 v1.36.0 发布（CNCF 项目）](https://github.com/jaegertracing/jaeger/releases/tag/v1.36.0)  

    该版本主要新特性：支持报告 span size 指标、增加多租户支持。

- [Jaeger v1.35.0 发布（CNCF 项目）](https://github.com/jaegertracing/jaeger/releases/tag/v1.35.0)  

    该版本主要新特性：引入了通过 OpenTelemetry 协议（OTLP）接收 OpenTelemetry 追踪数据的能力、为 GRPC 服务器定义健康服务器、添加 flag 用于在 rollover 时启用/禁用依赖关系、为 Admin Server 添加 TLS 配置。

- [Jaeger 分布式追踪系统 v1.34.0 发布（CNCF 项目）](https://github.com/jaegertracing/jaeger/releases/tag/v1.34.0)  

    该版本主要新特性：为 hotrod 应用添加 kubernetes 实例、新增 streamingSpanWriterPlugin 以提高 grpc 插件的写入性能、MetricsReader 添加 metrics 仪表等。

- [Jakarta EE 10 基于 Java 的框架发布，开启云原生 Java 时代](https://mp.weixin.qq.com/s/BQBy5AWFOc7kS55JBtBjiQ)

    [Jakarta EE 10](https://github.com/jakartaee/jakarta.ee) 引入了用于构建现代化和轻量级云原生 Java 应用的功能。
    具体包括：新增配置文件规范，定义一个用于轻量级 Java 应用和微服务的多供应商平台；针对适合微服务开发的较小运行时，提供了规范子集，包括用于构建应用的新 CDI-Lite 规范；支持多态类型；将 UUID 标准化为基本类型并扩展查询语言和查询 API。

### K

- [k0smotron：Mirantis 开源 Kubernetes 控制平面项目 k0smotron](https://www.mirantis.com/blog/introducing-k0smotron)

    [k0smotron](https://github.com/k0sproject/k0smotron) 本质上是一套 Kubernetes 控制器，能让你在单个 Kubernetes 集群中以 Pod 的形式运行和管理多个 Kubernetes 集群控制平面。实现真正的控制平面和工作平面分离，即在现有集群上运行的控制平面与工作平面没有直接的网络连接。此外，还支持将任何基础设施的工作者节点连接到集群控制平面。

- [k8gb Kubernetes 全局负载均衡器  v0.10.0 发布（CNCF 项目）](https://github.com/k8gb-io/k8gb/releases/tag/v0.10.0)

    该版本主要新特性：可以通过环境变量访问 LeaderElection、支持 OpenTelemetry 的 tracing 方案、支持创建 K8GB 指标的Grafana 仪表盘样本、实现一致的轮询负载均衡策略。

- [KapacityStack：由蚂蚁集团开源的云原生智能容量技术](https://mp.weixin.qq.com/s/Wm4wj1OTANLYZaziRH2sDw)

    [KapacityStack](https://github.com/traas-stack/kapacity) 提供了 IHPA（Intelligent Horizontal Pod Autoscaler）能力：支持在不同场景因地制宜地使用不同的算法进行扩缩容；支持在整个弹性过程中精细化地控制工作负载下每一个 Pod 的状态；在执行扩缩容时支持采用自定义灰度分批的变更策略；支持用户自定义的变更期稳定性检查；整个 IHPA 能力就拆分为了管控、决策、执行三大模块，任一模块都可以做替换或扩展。

- [Karmada 多云多集群容器编排平台 v1.7.0 发布（CNCF 项目）](https://github.com/karmada-io/karmada/blob/master/docs/CHANGELOG/CHANGELOG-1.7.md)

    版本特性：引入 CronFederatedHPA API，用于定时自动调整工作负载的副本数量；引入MultiClusterService API，用于控制服务对多个外部集群的暴露，并实现集群之间的服务发现；支持根据优先级声明预留策略抢占资源；支持在无需容器终止或重启的前提下批量迁移资源；FederatedHPA 支持根据除 CPU 和内存以外的自定义指标来调整副本的数量。

- [Karmada 多云多集群容器编排平台 v1.6.0 发布（CNCF 项目）](https://github.com/karmada-io/karmada/releases/tag/v1.6.0)

    版本特性：引入 FederatedHPA API，以解决跨集群扩展工作负载的要求；支持自动将不健康的应用程序迁移到其他可用的集群；引入新的声明式部署方式 Karmada operator；支持第三方资源解释器。

- [Karmada 多云多集群容器编排平台 v1.5.0 发布（CNCF 项目）](https://github.com/karmada-io/karmada/releases/tag/v1.5.0)

    版本特性：支持多个调度组、默认调度器兼容与任何第三方调度器、内置解释器支持 StatefulSet、默认解释器支持 CronJob 聚合状态以及 Pod 中断预算（PodDisruptionBudget）。

- [Karmada 多云多集群容器编排平台 v1.4.0 发布（CNCF 项目）](https://github.com/karmada-io/karmada/releases/tag/v1.4.0)

    该版本主要新特性：新增声明式资源解释器、支持声明分发策略/集群分发策略的优先级、通过指标和事件增强可观测性能力、故障切换/优雅驱逐 FeatureGate 升级为 Beta 且默认开启。

- [Karmada 多云多集群容器编排平台  v1.3.0 发布（CNCF 项目）](https://github.com/karmada-io/karmada/releases/tag/v1.3.0)  

    该版本主要新特性：支持基于污点的优雅工作负载驱逐、引入多集群资源访问的全局代理、支持集群资源建模、新增基于 Bootstrap token 的集群注册方式、优化系统可扩展性等。

- [Karmada 跨云多集群容器编排平台 v1.2.0 发布（CNCF 项目）](https://github.com/karmada-io/karmada/releases/tag/v1.2.0)  

    该版本主要新特性：优化随时间变化的调度策略；支持跨区域部署工作负载；`karmadactl` 和 `kubectl-karmada`支持更加丰富的命令；新增针对 Kubernetes 资源的分布式搜索和分析引擎（alpha）；实现自定义的资源状态收集。

- [Karpenter 自动扩缩容工具 v0.19.0 发布](https://github.com/aws/karpenter/releases/tag/v0.19.0)

    该版本主要新特性：默认驱逐无控制器的 pod、将 AWS 设置从 CLI Args 迁移到 ConfigMap、支持 IPv6 自动发现、将 webhook和控制器合并为一个二进制文件。

- [Kata Containers 容器安全项目 v3.2.0 发布](https://github.com/kata-containers/kata-containers/releases/tag/3.2.0)

    版本特性：将 CI 转换为 GitHub Actions、启用代理稳定性测试、添加 k0s 支持、添加 CRI-O 测试、为所有支持的 k8s 版本启用 kata-deploy 测试、支持在 K8s 中启用 Kata runtime 来进行 FIO 测试、添加用于非加密机密测试的镜像。

- [Kata Container 容器安全项目 v3.1.0 发布](https://github.com/kata-containers/kata-containers/releases/tag/3.1.0)

    版本特性：支持 AMD SEV-SNP 机密虚拟机；支持 EROFS 文件系统；完善 Docker/Moby 网络支持改进运行时（runtime-rs），包括增加对大页面（hugepages）的支持；增加 QEMU 日志记录功能；兼容 CRI-O 和 containerd 1.6.8；支持 Kubernetes 1.23.1-00。

- [Kata Containers 安全容器运行时 v3.0.0 发布](https://github.com/kata-containers/kata-containers/releases/tag/3.0.0)

    该版本主要新特性：新增 Rust 语言重写的容器运行时组件以及一个可选的集成虚拟机管理组件、支持主流的云原生生态组件（包括 Kubernetes、CRI-O、Containerd 以及 OCI 容器运行时标准等）、支持 cgroupv2、支持最新的 Linux 内核稳定版本。

- [Kata Container 容器安全项目 v2.5.0 发布](https://github.com/kata-containers/kata-containers/releases/tag/2.5.0)  

    该版本主要新特性：支持 containerd shimv2 日志插件、支持 virtio-block 多队列、支持 QEMU 沙箱功能、支持 containerd 的核心调度、kata-runtime iptables 子命令可在 guest 中操作 iptables、支持直接分配的卷。

- [Katalyst 云原生资源管控系统 v0.3.0 发布](https://github.com/kubewharf/katalyst-core/releases/tag/v0.3.0)

    版本特性：KCNR API 增加网络带宽资源的申请、调度、分配能力，并结合 EDT/TC 等限速方案提供网络带宽隔离能力；新增任务执行框架；新增异步执行框架；算法实现多 CPU Region 模式；混部能力增强。

- [Katalyst：字节跳动开源的云原生资源管控系统](https://mp.weixin.qq.com/s/A5_1h3RLmDNazmAddbhYaA)

    [Katalyst](https://github.com/kubewharf/katalyst-core) 的主要特点包括：完全孵化于超大规模混部实践，并在字节服务云原生化的进程中同步接管资源管控链路；搭载字节跳动内部的 Kubernetes 发行版 Enhanced Kubernetes 同步开源；系统基于插件化模式构建，用户可以在 Katalyst Framework 之上自定制各类调度、管控、策略、数据等模块插件等。

- [KCL：配置语言 KCL 成为 CNCF 沙箱项目](https://mp.weixin.qq.com/s/VbIIHj28DZZea3R4tYT66A)

    [KCL](https://github.com/kcl-lang/kcl) 是一个开源的基于约束的记录及函数语言，期望通过成熟的编程语言技术和实践来改进对大量繁杂配置比如云原生 Kubernetes 配置场景的编写，致力于围绕配置的模块化、扩展性和稳定性，打造更简单的逻辑编写体验，构建更简单的自动化和生态集成路径。

- [KEDA：CNCF 宣布 K8s 自动缩放器 KEDA 毕业](https://mp.weixin.qq.com/s/Jkl8bGreQPk77VADOB-MOw)

    KEDA 是一个专门为 Kubernetes 设计的事件驱动自动缩放器。作为一个毕业项目，KEDA 团队计划提高项目的性能、多租户安装、监控和可观测性功能。并计划增加配置缩放行为和指标评估的能力，将碳和能源消耗考虑到缩放评估中，以及预测性自动缩放。

- [KEDA 事件驱动自动伸缩器 v2.11.0 发布（CNCF 项目）](https://github.com/kedacore/keda/releases/tag/v2.11.0)

    更新内容：新增 Solr Scaler；支持暂停自动缩放；改进和扩展普罗米修斯指标；如果有多个带有 CPU 和内存扩展器的扩展器，能够将其扩展为零。

- [KEDA 基于 Kubernetes 事件驱动自动缩放项目公布安全审计结果](https://mp.weixin.qq.com/s/ZwCg-qCeC2CMm7EbxJbi9w)

    审计发现了 Redis Scalers 中的一个重大缺陷，该缺陷可能会影响系统的机密性、完整性或可用性。
    这个问题与加密和绕过 TLS 有关，从而允许潜在的 MitM（中间人）攻击。
    目前，该问题已修复。此外，基于审计结果，KEDA 还更新了现有的安全工具链，引入了 semgrep 工具和 TLS 证书管理。

- [KEDA 事件驱动自动伸缩器 v2.9.0 发布（CNCF 项目）](https://github.com/kedacore/keda/releases/tag/v2.9.0)

    该版本主要新特性：增加 CouchDB、Etcd 和 Loki 扩展器、引入 Grafana 仪表盘用于监控应用的自动缩放、在 KEDA Operator 中整合所有暴露的 Prometheus 指标、实验性的支持在轮询间隔期间为扩展器缓存指标值。

- [KEDA 基于 Kubernetes 的事件驱动自动伸缩工具 v2.8.0 发布（CNCF 项目）](https://github.com/kedacore/keda/releases/tag/v2.8.0)

    该版本主要新特性：支持 NATS streaming、支持自定义 HPA 名称、支持在 ScaledJob 中指定最小 pod 副本数、允许 cpu/memory scaler 只对 pod 中的一个容器进行扩展。

- [KEDA 基于 Kubernetes 事件驱动的扩缩容工具 v2.7.0 发布（CNCF 项目）](https://github.com/kedacore/keda/releases/tag/v2.7.0)

    该版本主要新特性：支持通过 ScaledObject 注释暂停自动缩放、新增基于 ARM 的容器镜像、支持以非 root 身份运行 KEDA 的默认安全模式、CPU、内存、Datadog 扩展器使用全局 `metricType` 代替 `metadata.type`等。

- [Kelemetry：字节跳动开源的面向 Kubernetes 控制面的全局追踪系统](https://mp.weixin.qq.com/s/qgiladzN-l6jGaSwiWZ-_Q)

    [Kelemetry](https://github.com/kubewharf/kelemetry) 从全局视角串联起多个 Kubernetes 组件的行为，追踪单个 Kubernetes 对象的完整生命周期以及不同对象之间的相互影响。通过可视化 K8s 系统内的事件链路，它使得 Kubernetes 系统更容易观测、更容易理解、更容易 Debug。

- [Keptn 云原生应用程序生命周期编排项目 v0.19.0 发布（CNCF 项目）](https://github.com/keptn/keptn/releases/tag/0.19.0)

    该版本主要新特性：Helm-service 和 Jmeter-service 移到 keptn 贡献仓库、支持验证入站事件、引入签名的 Keptn Helm chart、支持通过 sigstore/cosign 签名所有发布/预发布的容器镜像。

- [Keptn 云原生应用程序生命周期编排项目 v0.18.0 发布（CNCF 项目）](https://github.com/keptn/keptn/releases/tag/0.18.0)

    该版本主要新特性：安装/卸载/升级命令不可用，改用 Helm 来操作 Keptn；在资源 API 中，尾部`/`将返回 404；弃用配置服务，所有 Keptn 的核心服务都依赖于资源服务。

- [Keptn 云原生应用生命周期编排引擎升级为 CNCF 孵化项目](https://mp.weixin.qq.com/s/gkv_fSnrRv0ao1AHUzBB5A)  

    [Keptn](https://github.com/keptn/keptn) 是基于事件的控制平面，使用声明式编程方法实现应用的连续交付和自动修复。Keptn 未来将支持 GitOps 和控制仓库的管理方式、RBAC、执行平面的远程管理等。

- [Keptn 云原生应用持续交付和自动化操作工具 v0.16.0 发布（CNCF 项目）](https://github.com/keptn/keptn/releases/tag/0.16.0)  

    该版本主要新特性：`resource-service` 取代 `configuration-service`，以加快响应时间、支持在不停机的情况下升级 Keptn；v0.17 中，CLI 将删除安装/卸载/升级命令；支持直接向 Nats 发送事件；只有当服务连接到控制平面时，才会被视为准备就绪；允许在没有 distributor sideCar 的情况下运行 approval service。

- [Keycloak 身份和访问管理项目 成为 CNCF 孵化项目](https://www.cncf.io/blog/2023/04/11/keycloak-joins-cncf-as-an-incubating-project/)

    [Keycloak](https://github.com/keycloak/keycloak) 提供对应用程序和 API 的集中身份验证和授权。Keycloak 可以与云原生生态系统很好地集成。
    它支持在 Kubernetes 上运行，并可以使用 Operator Framework 构建的操作器进行安装。它还提供 Prometheus 指标，并与标准 Kubernetes 堆栈进行整合。
    CNCF 许多项目直接集成了 Keycloak，用于身份验证和访问，包括 Argo、Envoy 和 Jaeger 等。

- [Kindling 云原生可观测工具 v0.7.0 发布](https://github.com/KindlingProject/kindling/releases/tag/v0.7.0)

    版本特性：提供一个简易版视图来显示 Trace Profiling 数据、为 cpuevents 增加追踪功能、支持 NoAPM Java 应用的附属代理。

- [Kindling 云原生可观测工具 v0.6.0 发布](https://github.com/KindlingProject/kindling/releases/tag/v0.6.0)

    该版本主要新特性：在 cpu 事件中增加 tracing span 数据、增加 Trace Profiling 的调试工具、支持 RocketMQ 协议。

- [Knative 基于 Kubernetes 的 serverless 架构方案 v1.12.0 发布（CNCF 项目）](https://github.com/knative/serving/releases/tag/knative-v1.12.0)

    版本特性：新增状态字段 cluster-local-domain-tls，用于控制集群本地域的 TLS 证书；在启用安全 Pod 默认特性时，验证 Webhook 将允许添加 NET_BIND_SERVICE 或 nil 能力；支持 gRPC 探测；允许为 Knative Service 设置共享进程命名空间功能。

- [Knative 基于 Kubernetes 的 serverless 架构方案 v1.11.0 发布（CNCF 项目）](https://github.com/knative/serving/releases/tag/knative-v1.11.0)

    版本特性：域映射控制器逻辑已与Serving控制器合并、新增字段用于启用 Queue Proxy 时的资源请求和限制（仅适用于 CPU 和内存）、Activator 现在有一个单独的服务账号、支持通过服务级别的注释来配置 Queue Proxy 资源。

- [Knative 模糊测试审计结果公布](https://mp.weixin.qq.com/s/CeGpRJCwYkhrrfwgMR7AFw)

    [Knative 模糊测试报告](https://github.com/knative/docs/blob/main/reports/ADA-knative-fuzzing-audit-22-23.pdf)中披露，此次模糊测试安全审计为 3 个 Knative 子项目编写了 29 个模糊测试器。这些模糊测试器发现了一个第三方依赖项中的问题，该问题目前已得到修复。

- [Knative 基于 Kubernetes 的 serverless 架构方案 v1.8.0 发布（CNCF 项目）](https://github.com/knative/serving/releases/tag/knative-v1.8.0)

    该版本主要新特性：修改默认域、升级 HPA 到 v2 版本、允许设置 seccompProfile 以启用使用受限的安全配置文件、最低 k8s 支持版本升至 v1.23、调和超时时间提高到 30 秒、默认启用 EmptyDir 卷功能参数。

- [Koordinator 云原生混部系统 v1.0 发布](https://github.com/koordinator-sh/koordinator/releases/tag/v1.0.0)

    该版本主要新特性：优化任务调度、优化 ElasticQuota 调度、支持细粒度的设备调度管理机制、支持根据节点的负载水位调整 BestEffort 类型 Pod 的 CPU 资源额度、支持使用 CPU Burst 来提高延迟敏感应用的性能、实现基于内存安全阈值和资源满足的驱逐机制、精细化 CPU 调度、支持在不侵入 Kubernetes 已有的机制和代码前提下预留资源、简化自定义重调度策略的操作。

- [Koordinator 云原生混部系统 v0.6.0 发布](https://github.com/koordinator-sh/koordinator/releases/tag/v0.6.0)

    该版本主要新特性：完善 CPU 精细化编排策略、支持在不侵入 Kubernetes 已有机制和代码的前提下实现资源预留、支持 Pod 腾挪（PodMigrationJob）、发布了全新的 Descheduler 框架。

- [Kruise Rollout 渐进式交付框架 v0.2.0 发布](https://openkruise.io/docs/)  

    该版本主要新特性：支持 Gateway API、支持有状态应用的分批发布、新增了“Pod 批次打标”能力、集成到 KubeVela 之中实现 Helm Charts 金丝雀发布能力。

- [KSOC Labs 发布第一个 Kubernetes 物料清单 (KBOM)](https://www.infoq.com/news/2023/06/kubernetes-bill-of-materials/?topicPageSponsorship=6dafd62c-9925-4408-bfda-e96bc971c941)

    [KBOM](https://github.com/ksoclabs/kbom) 是一款开源标准和命令行工具，可帮助安全团队快速分析集群配置并应对 CVE。该项目包含一份初始规范和实施方案，可跨云供应商、企业内部(on-premise) 及自定义环境使用。安全和规范团队可通过使用 KBOM 对其 Kubernetes 集群（尤其是三方插件）获得更高的可见性，从而快速识别漏洞和维系。

- [Kuasar：由华为云联合多家单位正式开源的多沙箱容器运行时](https://mp.weixin.qq.com/s/pXBZ-U1KF0_bNU8u6MOv8A)

    [Kuasar](https://github.com/kuasar-io/kuasar) 在保留传统容器运行时功能的基础上，通过全面 Rust 化以及优化管理模型和框架等手段，进一步降低管理开销、简化调用链路，扩展对业界主流沙箱技术的支持。此外，通过支持多安全沙箱共节点部署，Kuasar 可以充分利用节点资源，实现降本增效。

- [KubeAdmiral 字节跳动开源的基于 K8s 的新一代多集群编排调度引擎](https://mp.weixin.qq.com/s/aS18urPF8UB4K2I_9ECbHg)

    [KubeAdmiral](https://github.com/kubewharf/kubeadmiral) 是基于 Kubernetes Federation v2 迭代演进而来，旨在提供云原生多云多集群的管理和应用分发能力。KubeAdmiral 在其基础上做了增强：兼容原生 Kubernetes API；提供更灵活的调度框架，支持丰富的调度分发策略；差异化策略；依赖调度/跟随调度；提供状态收集的框架，提供更灵活的状态收集。

- [KubeClipper K8S 集群生命周期管理服务成为 CNCF 沙箱项目](https://mp.weixin.qq.com/s/UEFtUZR8BZX9pK_PYsAWlA)

    [KubeClipper](https://github.com/kubeclipper/kubeclipper) 基于 Kubeadm 封装，用户可以通过 Web 界面、API，或命令行工具（kcctl）来管理主机节点，可以快速创建和删除 K8S 集群，并可以对已存在的 K8S 集群进行纳管、升级、配置变更、应用部署，以及扩、缩容等操作。

- [KubeClipper：九州云开源的 K8s 多集群全生命周期管理工具](https://mp.weixin.qq.com/s/RVUB5Pw6-A5zZAQktl8AcQ)  

    [KubeClipper](https://github.com/KubeClipper-labs) 基于 kubeadm 工具进行二次封装，提供在企业自有基础设施中快速部署 K8S 集群和持续化全生命周期管理（安装、卸载、升级、扩缩容、远程访问等）能力，
    支持在线、代理、离线等多种部署方式，还提供了丰富可扩展的 CRI、CNI、CSI、以及各类 CRD 组件的管理服务。

- [KubeEdge 云原生边缘计算平台 v1.15.0 发布（CNCF 项目）](https://github.com/kubeedge/kubeedge/blob/master/CHANGELOG/CHANGELOG-1.15.md)

    版本特性：支持 Windows 边缘节点、设备 API 升级到 v1beta1、新增对 DMI 数据平面的支持（alpha）、新增映射器开发框架子项目 Mapper-Framework、支持 Kubernetes 原生的静态 Pod、支持依赖于非资源类别请求的 Kubernetes 插件（如 Cilium、Calico）、将 Kubernetes 的依赖升级到了 v1.26.7。

- [KubeEdge Sedna v0.6 & Ianvs 边云协同终身学习方案 v0.2 发布](https://mp.weixin.qq.com/s/OQdNmmzRl4GC_ZssU4vatQ)

    版本特性：支持非结构化数据场景下的开放世界边云协同终身学习；提供开源数据集、基线算法和评价指标的完整测试套件；针对机器人巡检、自动驾驶等场景，开发了新的未知任务识别和处理能力，包括新样本识别、训练数据生成、多模型联合推理等。

- [KubeEdge 达到软件供应链 SLSA L3 等级](https://mp.weixin.qq.com/s/5kpbnE-F__HqlF0JAwCOSg)

    在近期发布的 v1.13.0 版本中，KubeEdge 项目已达到 [SLSA](https://slsa.dev/) L3 等级（包括二进制和容器镜像构件），成为 CNCF 社区首个达到 SLSA L3 等级的项目。
    这意味着，KubeEdge 可以端到端的从源码构建到发布流程进行安全加固，保障用户获取到的二进制或容器镜像产物不被恶意篡改。

- [KubeEdge 云原生边缘计算平台 v1.12 发布（CNCF 项目）](https://github.com/kubeedge/kubeedge/blob/master/CHANGELOG/CHANGELOG-1.12.md)

    该版本主要新特性：引入下一代云原生设备管理接口（DMI）、新版本的轻量级引擎 Edged 升级为 GA、EdgeMesh 新增高可用模式、支持边缘节点从云端升级、支持边缘 Kube-API 端点的授权、支持 GigE Device Mapper。

- [KubeEdge 审计报告发布](https://github.com/kubeedge/community/blob/master/sig-security/sig-security-audit/KubeEdge-security-audit-2022.pdf)  

    OSTIF（Open Source Technology Improvement Fund，开源技术改进基金会）完成了对 KubeEdge 的安全审计。审计发现了 12 个严重程度为中等的问题，建立了威胁模型，并集成到 OSS Fuzz。KubeEdge 安全团队已经在新发布的 v1.11.1、v1.10.2 和 v1.9.4 中对所有问题进行了修复。

- [KubeEdge 云原生边缘计算平台 v1.11.0 发布（CNCF 项目）](https://github.com/kubeedge/kubeedge/blob/master/CHANGELOG/CHANGELOG-1.11.md)  

    该版本主要新特性：新增节点组管理功能；提供边缘设备 Mapper 的 SDK，减少开发 Mapper 的工作量；正式支持容器化部署、离线安全等 Keadm 子命令；边缘节点代理 Edged 适用更多场景。

- [Kubefirst GitOps 基础设施及应用交付平台 v2.3.0 发布](https://github.com/kubefirst/kubefirst/releases/tag/v2.3.0)

    版本特性：为安全问题添加 SECURITY.md 文件、添加一个工作流程来验证 Markdown 语法、在错误问题模板中添加 DNS 信息、添加一个 Markdown 链接检查器操作。

- [Kubeflow：Kubernetes 机器学习平台 Kubeflow 升级成为 CNCF 孵化项目](https://mp.weixin.qq.com/s/8bZr2Edmyh-unE5ghIBhJg)

    Kubeflow 是一个开源、社区驱动的项目，用于在 Kubernetes 上部署和管理机器学习（ML）堆栈。Kubeflow 社区积极开发和支持面向 Kubernetes 的 MLOps，为其用户开发和部署流行的框架，包括 TensorFlow、PyTorch、XGBoost、Apache MXNet 等分布式机器学习（ML）。

- [KubeKey 集群部署工具 v3.0 发布](https://github.com/kubesphere/kubekey/releases/tag/v3.0.0)

    该版本主要新特性：为 docker 构建和推送添加 GitHub 工作流、支持执行自定义设置脚本、添加 k3s 控制平面控制器和启动控制器、添加 k3s 容器运行时配置、添加 k3s e2e 测试支持、自定义 OpenEBS 基本路径、重构 KubeKey 项目、支持更多的 Kubernetes 和 k3s 版本。

- [KubeKey 集群部署工具 v2.3.0 发布](https://github.com/kubesphere/kubekey/releases/tag/v2.3.0)

    该版本主要新特性：添加 kubelet pod pid 限制、使用 Jenkins Pipeline 替代 GitHub Actions、在创建集群或添加节点时增加安全增强命令、删除集群或节点时清理 vip、支持 kube-vip BGP 模式、支持清理 CRI、支持  kube-vip、支持 k8s 最近发布的补丁版本。

- [KubeKey 集群部署工具 v2.1.0 发布（KubeSphere 社区开源）](https://github.com/kubesphere/kubekey/releases/tag/v2.1.0)

    该版本主要新特性：根据 OCI 标准实现了镜像的拉取、上传和归档保存等功能，使其在制作和使用 KubeKey 制品时不依赖额外的容器运行时；支持初始化操作系统命令（kk init os）使用制品进行离线本地源安装操作系统依赖；支持同一个 K8s 集群中同时包含 ARM64 节点和 AMD64 节点等。

- [Kube-OVN CNI 插件 v1.12.0 发布（CNCF 项目）](https://github.com/kubeovn/kube-ovn/releases/tag/v1.12.0)

    版本特性：优化底层调用 OVN 接口的方式；支持流量远程镜像；支持使用 IPSec 对集群内跨节点通信的流量进行加密；支持通过 kubectl-ko 插件一键收集所有 Kube-OVN 相关的组件日志、dmesg 信息、iptables 规则等和网络相关的详细信息；实现 Overlay 和 Underlay 网络的互通；新增 IPPool 的 CRD 资源；增加策略 NAT 功能；新增 OVN 原生的网关类型。

- [Kube-OVN CNI 插件 v1.11.0 发布（CNCF 项目）](https://github.com/kubeovn/kube-ovn/releases/tag/v1.11.0)

    该版本主要新特性：Underlay 和 Overlay 子网互通、新增 SR-IOV Network Operator 进行自动化网卡配置、支持自定义 VPC 内部负载均衡、新增 vpc-dns CRD、支持默认 VPC 下的 Load Balancer 类型 Service。

- [Kube-OVN v1.10.0 发布（CNCF 项目）](https://mp.weixin.qq.com/s/e1TW_s3r9__qSgZz6aWmAA)

    该版本主要新特性：在子网新增 ACL 字段，用户可以按照自己的需求编写符合 OVN 流表规范的 ACL 规则； KubeVirt 场景下， VM instance 的地址分配策略采用和 StatefulSet 类似的策略，支持 DPDK、DHCP；集成 Submariner 用于多集群的互联；针对大规模环境，对控制平面性能进行了优化等。

- [Kubernetes Gateway API v0.8.0 发布](https://github.com/kubernetes-sigs/gateway-api/releases/tag/v0.8.0)

    版本特性：引入服务网格支持、支持 CEL 验证(仅 Kubernetes 1.25+ 版本完全支持)。

- [Kubernetes Cluster API v1.4.0 发布](https://github.com/kubernetes-sigs/cluster-api/releases/tag/v1.4.0)

    版本特性：支持在 KCP 控制平面部署失败时自动进行故障恢复、支持将某些标签从 Machine 同步到 Node、以将标签、注释等信息从 ClusterClass 传播到 KubeadmControlPlane/MachineDeployment 和 Machine 中、支持 ClusterClass 和 Managed Topologies 中的变量发现。

- [Kubernetes v1.28 发布](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md)

    版本特性：支持控制平面和节点版本之间的偏差变化、节点非优雅关闭功能 GA、CRD 基于通用表达式语言 (CEL) 的验证规则 Beta、Kube APIServer 混合版本互操作代理 Alpha、 新增通用控制平面存储库 Alpha、设备插件 API 添加对 CDI 标准设备的支持 Alpha、原生支持 Sidecar 容器 Alpha、节点 Swap 内存支持 Beta、新增对 Windows 节点的支持 Beta。

- [Kubernetes v1.27.0 发布](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md#changelog-since-v1260)

    版本特性：冻结 k8s.gcr.io 镜像仓库、SeccompDefault 升级为 GA、Job 可变调度指令升级为 GA、Pod 调度 Readiness 升级为 beta、允许通过 Kubernetes API 访问节点日志、引入新访问模式 ReadWriteOncePod 以将卷访问限制在集群中的单个 Pod 上、VolumeManager 重建升级为 beta。

- [Kubernetes 1.24 的第三方安全审计结果发布](https://www.cncf.io/blog/2023/04/19/new-kubernetes-security-audit-complete-and-open-sourced/)

    [本次审计](https://github.com/kubernetes/sig-security/blob/main/sig-security-external-audit/security-audit-2021-2022/findings/Kubernetes%20v1.24%20Final%20Report.pdf)发现以下问题：在限制用户或网络权限方面存在问题，可能导致管理员混淆特定组件可用的权限；组件间身份验证存在漏洞，恶意用户能够获得集群管理员权限；日志和审计存在缺陷，攻击者可以在控制集群后利用这些缺陷来进行潜在活动；用户输入过滤存在漏洞，允许通过修改 etcd 数据存储的请求来绕过身份验证。

- [Kubernetes v1.26 发布](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.26.md)

    该版本主要新特性：允许用户跨命名空间从卷快照中配置卷、允许使用 CEL 进行 Admission Control、改进拓扑管理器中的多 numa 对齐、为 Pod 调度增加调度就绪的机制、移除 CRI v1alpha2、Auth API 允许获取 User 属性、减少 Kubelet 在 PLEG 中的 CPU 消耗。

- [Kubernetes 发布 Kubernetes CVE 订阅列表](https://kubernetes.io/blog/2022/09/12/k8s-cve-feed-alpha/)

    Kubernetes 现在支持通过订阅一个自动更新的 [JSON feed](https://kubernetes.io/docs/reference/issues-security/official-cve-feed/index.json)，跟踪 Kubernetes 的安全问题（也称为 "CVE"，来自不同产品和供应商的公共安全问题的数据库）。

- [Kubernetes v1.25 发布（CNCF 项目）](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.25.md)  

    该版本主要新特性：升级到 Stable：Pod Security Admission 、临时容器、cgroups v2 支持、网络策略中的 endPort、本地临时存储容量隔离、核心 CSI Migration、CSI 临时卷升级；升级到 Beta：SeccompDefault、CRD 验证表达式语言；引入 KMS v2 API 等。

- [Kubernetes v1.24.0 发布（CNCF 项目）](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md)

    该版本主要新特性：dockershim 组件从 kubelet 中删除；默认情况下关闭新的测试版 API；发布工件使用 cosign进行签名，并且提供验证镜像签名的实验性支持；支持存储容量跟踪以显示当前可用的存储容量和卷扩展；gRPC 探针和 kubelet 凭证提供程序升级到 Beta；允许为服务的静态 IP 地址分配软保留一个范围等。

- [Kubernetes Gateway API v0.5.0 发布](https://github.com/kubernetes-sigs/gateway-api/releases/tag/v0.5.0)  

    该版本主要新特性：三个 API 升级为beta：`GatewayClass`、`Gateway`和`HTTPRoute`；引入了 experimental 和 standard 版本渠道；通过指定端口号，路由可以连接到网关；支持 URL 重写和路径重定向。

- [kube-rs Kubernetes 的 Rust 客户端 v0.79.0 发布（CNCF 项目）](https://github.com/kube-rs/kube/releases/tag/0.79.0)

    版本特性：增加对元数据 api 的支持以减少网络负载、暴露客户端的默认命名空间、允许在不消耗原始的 watcher stream 的情况下从 watcher 订阅事件、支持持久元数据 watch。

- [Kubescape Kubernetes 安全平台 3.0 发布（CNCF 项目）](https://kubescape.io/blog/2023/09/19/introducing-kubescape-3/)

    版本特性：将合规性和容器扫描结果存储为 Kubernetes 集群内的资源；通过命令行界面扫描容器镜像的漏洞；报告集群中所有镜像的漏洞情况；全新的概览安全扫描，支持为集群安全设置基线；突出显示高风险工作负载；新的基于能力的 Helm chart；支持通过 Prometheus Alertmanager 进行告警；支持将数据发送到集群外的托管服务。

- [KubeSkoop：由阿里云开源的 Kubernetes 网络监控工具](https://mp.weixin.qq.com/s/zbAcZCNT5vyzGvp7uTDB1w)

    [KubeSkoop](https://github.com/alibaba/kubeskoop) 支持功能包括：Pod 级别的网络监控，包括流量，应用层连接信息， socket 内存分配状态等；Pod 级别的网络异常状态的指标监控，例如 Pod 内进程对 socket 进行读写操作的等待时间超过 100ms 的次数等；Pod 级别的网络异常事件的现场，提供事件发生的详细信息的观测。

- [KubeSphere 多租户容器平台 v3.4.0 发布（CNCF 项目）](https://github.com/kubesphere/kubesphere/releases/tag/v3.4.0)

    版本特性：添加 golangci-lint 工作流用于节点检查、集成 opensearch v1/v2、为 rulegroup 添加 admission webhook、添加 alerting v2beta1 api、支持使用标签选择器过滤工作区角色、为缓存添加动态选项、添加 helm 执行器通用包、生成 CRD 支持多个版本、支持 gitlab 身份提供者、支持节点和工作负载范围的全局规则、支持支持可插拔的通知功能。

- [KubeSphere v3.3.0 发布（CNCF 项目）](https://github.com/kubesphere/kubesphere/blob/master/CHANGELOG/CHANGELOG-3.3.md)

    该版本主要新特性：

    - DevOps：后端支持独立部署，提供基于 GitOps 的持续部署方案，引入 Argo CD 作为 CD 的后端，可以实时统计持续部署的状态。
    - 网络：集成负载均衡器 OpenELB，即使是在非公有云环境的 K8s 集群下，也可以对外暴露 LoadBalancer 服务。
    - 多租户和多集群：集群应用可以通过一个 ConfigMap 获取到所在集群的名称、支持为集群设置集群成员和集群角色。
    - 可观测性：添加容器进程/线程指标、优化磁盘使用率指标、支持在命名空间自定义监控中导入 Grafana 模板。
    - 存储：支持 PVC 自动扩展策略、支持对卷快照内容和类型进行管理、支持为存储类型设置授权规则。
    - 边缘：集成 KubeEdge。

- [Kubespray Kubernetes 集群部署工具 v2.22.0 发布](https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.22.0)

    版本特性：同一镜像名称下支持多架构镜像、为 cert-manager 增加 DNS 配置、 kube-scheduler 配置中加入 kube-profile 配置、允许配置镜像垃圾收集、支持自定义 ssh 端口、支持启用 kube-vip 的控制平面负载均衡。

- [Kubespray Kubernetes 集群部署工具 v2.20.0 发布](https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.20.0)

    该版本主要新特性：支持 Rocky Linux 8 和 Kylin Linux、在重置角色中添加 “flush ip6tables” 任务、支持 NTP 配置、添加 kubelet systemd 服务加固选项、为 CoreDNS/NodelocalDNS 添加重写插件、为 kubelet 添加 SeccompDefault admission 插件、为 k8s_nodes 增加 extra_groups 参数、新增 ingress nginx webhook、增加对节点和 pod pid 限制的支持、支持启用默认的 Pod 安全配置。

- [KubeVela 混合多云环境应用交付平台 v1.8.0 发布（CNCF 项目）](https://github.com/kubevela/kubevela/releases/tag/v1.8.0)

    版本特性：支持通过多个分片对控制平面进行横向扩展、支持从现有的 KubeVela 定义中生成语言感知的 SDK、新增基于工作流的触发器 kube-trigger、允许应用开发人员以金丝雀发布的风格来协调应用交付过程。

- [KubeVela 升级成为 CNCF 孵化项目](https://mp.weixin.qq.com/s/mhH9u4aXJT2-qVwf06xn5Q)

    [KubeVela](https://github.com/kubevela/kubevela) 采用 Kubernetes 控制平面构建，使跨混合和多云环境部署和操作应用变得更容易、更快速、更可靠。
    未来，KubeVela 社区计划通过交付工作流改善云资源创建和消费的用户体验，增强混合/多集群场景中整个 CI/CD 交付流程的安全，
    支持允许用户轻松与第三方 API 集成的 KubeVela Dynamic API 等等。

- [KubeVela 混合多云环境应用交付平台 v1.6.0 发布（CNCF 项目）](https://github.com/kubevela/kubevela/releases/tag/v1.6.0)

    该版本主要新特性：支持资源交付可视化、提供可观测基础设施搭建、面向应用的可观测、可观测即代码的能力、支持多环境流水线统一管理、支持应用间配置的共享并与第三方外部系统做配置集成。

- [KubeVela 混合多云环境应用交付平台 v1.5.0 发布（CNCF 项目）](https://github.com/kubevela/kubevela/releases/tag/v1.5.0)  

    该版本主要新特性：插件框架优化，提供创建脚手架、打包、推送到插件注册表等整个插件生命周期的管理；支持以 CUE 格式定义插件，并使用 CUE 参数来渲染部分插件；新增大量 vela cli 命令；VelaUX 支持管理由 CLI 创建的应用程序。

- [KubeVela v1.4.0 发布（CNCF 项目）](https://github.com/kubevela/kubevela/releases/tag/v1.4.0)  

    该版本主要新特性：支持多集群认证、使用 kubeconfig 的控制器自动登录、支持更多的授权方式；允许在 GC 策略中按资源类型选择资源、新增策略控制器为 VelaUX 和 CLI 参数生成 OpenAPI 模式；CLI 支持显示资源拓扑结构等。

- [KubeVirt 虚拟机运行项目 v1.1.0 发布（CNCF 项目）](https://github.com/kubevirt/kubevirt/releases/tag/v1.1.0)

    版本特性：网络绑定插件 API 支持 CNI、集群范围内的 CommonInstancetypes 资源现在可以通过 virt-operator 使用、支持动态启用和配置 KSM、添加内存热插拔功能、允许实时更新虚拟机亲和性和节点选择器、为 Slirp 网络引入网络绑定插件、引入 sidecar-shim 容器镜像、增加对基于迁移的 SRIOV 热插拔的支持、为 VMI 添加性能规模基准。

- [KubeVirt 虚拟机运行项目 v1.0 发布（CNCF 项目）](https://github.com/kubevirt/kubevirt/releases/tag/v1.0.0)

    版本特性：移除热插拔 VMI API、引入 CPU 热拔插、实验性支持 AMD 的安全加密虚拟化 (SEV) 、支持在偏好中设置 CPU 和内存最低资源需求、支持 VirtualMachine 对象上网络接口的热拔插、支持指定集群级别的虚拟机行为、增加多架构支持、 允许指定创建的虚拟机的内存、 允许在创建虚拟机时指定卷的启动顺序、克隆和导出虚拟机支持 RBAC 配置。

- [KubeVirt 虚拟机管理插件 v0.58.0 发布（CNCF 项目）](https://github.com/kubevirt/kubevirt/releases/tag/v0.58.0)

    该版本主要新特性：在 cluster-deploy 中默认启用 DataVolume 垃圾回收、能够在启用受限的 Pod 安全标准时运行、添加 tls 配置、修复在有 containerd 的系统上带有 containerdisks 的虚拟机迁移失败问题。

- [KubeVirt 虚拟机管理插件 v0.57.0 发布（CNCF 项目）](https://github.com/kubevirt/kubevirt/releases/tag/v0.57.0)  

    该版本主要新特性：弃用 SR-IOV 热迁移功能门、弃用虚拟机实例预设资源、增加对虚拟机输出资源类型的支持、支持 DataVolume 垃圾回收、允许对配置虚拟机拓扑分布约束的支持。

- [KubeVirt 虚拟机运行项目 v0.55.0 发布（CNCF 项目）](https://github.com/kubevirt/kubevirt/releases/tag/v0.55.0)  

    该版本主要新特性：引入克隆 CRD、控制器和 API、引入弃用策略、增加 virt-launcher 的内存开销、启用内存转储到 VMSnapshot 中、支持监控 VMI 迁移对象从创建到某个特定阶段所需的时间、允许 VMI 从根目录迁移到非根目录。

- [KubeVirt 虚拟机运行项目 v0.55.0 发布（CNCF 项目）](https://github.com/kubevirt/kubevirt/releases/tag/v0.55.0)  

    该版本主要新特性：引入克隆 CRD、控制器和 API、引入弃用策略、增加 virt-launcher 的内存开销、启用内存转储到 VMSnapshot 中、支持监控 VMI 迁移对象从创建到某个特定阶段所需的时间、允许 VMI 从根目录迁移到非根目录。

- [Kubewarden Kubernetes 策略引擎 v1.0.0 发布（CNCF 项目）](https://www.kubewarden.io/blog/2022/06/v1-release/)  

    该版本主要新特性：允许使用 Go、Rust 或 Swift 编写策略、支持使用 Kubewarden 策略取代每一个 Pod Security Policy、集成 OpenTelemetry、 利用 Sigstore 项目实现软件签名和验证。

- [KubeWharf：字节跳动开源云原生项目集](https://mp.weixin.qq.com/s/uNbT3Ss0rBYc9pqlZe3n8Q)

    [KubeWharf](https://github.com/kubewharf) 是一套以 Kubernetes 为基础构建的分布式操作系统，由一组云原生组件构成，专注于提高系统的可扩展性、资源利用率、可观测性、安全性等，支持大规模多租集群、在离线混部、存储等场景。
    KubeWharf 第一批计划开源三个项目：高性能元信息存储系统 KubeBrain、kube-apiserver 七层网关 KubeGateway、轻量级多租户方案 KubeZoo。

- [Kuma 服务网格项目 v2.5.0 发布（CNCF 项目）](https://github.com/kumahq/kuma/releases/tag/2.5.0)

    版本特性：支持区域内和跨区域的地域感知负载均衡能力、支持 Gateway API v1、支持 Envoy 1.28、在Global CP（全局控制平面）和 Zone CP（区域控制平面）协议中使用增量 KDS 显著降低资源消耗、允许从 MeshTrafficPermissions 中获取可访问的服务。

- [Kuma 服务网格项目 v2.2.0 发布（CNCF 项目）](https://github.com/kumahq/kuma/releases/tag/2.2.0)

    版本特性：支持 OpenTelemetry、支持使用 JSONPatch 定义 MeshProxyPatch 策略、支持重试指令和优先级、将底层 Envoy 版本升级到 1.25、新增策略以用于更精细地控制服务间的负载均衡、支持在 Kubernetes 集群中部署通用模式的全局控制平面（由 Postgres 支持）、支持为离线令牌签名和验证提供公钥。

- [Kuma 服务网格 v2.0 发布（CNCF 项目）](https://github.com/kumahq/kuma/releases/tag/2.0.0)

    该版本主要新特性：在 CNI 和 init 容器配置中增加对 eBPF 的支持、新增 3 个“下一代”策略、优化用户界面、支持配置控制平面/API 服务器所支持的 TLS 版本和密码、允许配置多个 UID 使其被流量重定向忽略、允许在使用 iptables 进行流量重定向时开启日志功能。

- [Kuma 服务网格项目 v1.8.0 发布（CNCF 项目）](https://github.com/kumahq/kuma/releases/tag/1.8.0)  

    该版本主要新特性：跨网格网关支持多区域运行、网格网关/内置网关增加可观测性功能、重写 CNI、网格网关支持路径重写和报头添加/删除、支持过滤代理的指标、简化 TCP 流量日志实现、支持 Projected Service Account Tokens。

- [Kurator 分布式云原生平台 v0.5.0 发布](https://github.com/kurator-dev/kurator/releases/tag/v0.5.0)

    版本特性：基于 Velero 提供了统一的备份、还原和迁移方案；基于 Rook 引入分布式云本地存储功能；attachedcluster 新增验证 webhook；新增自定义集群控制器的单元测试；新增集群选择器。

- [Kurator 分布式云原生平台 v0.3.0 发布](https://github.com/kurator-dev/kurator/releases/tag/v0.4.0)

    更新内容：新增模块 application manager，通过 GitOps 方式在整个 Fleet 中分发应用/配置；增加指标插件，支持多集群统一监控；新增策略管理器，提供一致的安全策略。

- [Kurator 分布式云原生平台 v0.3.0 发布](https://github.com/kurator-dev/kurator/releases/tag/v0.3.0)

    版本特性：在 Cluster API 的基础上增加了一个 CRD 集群，用户只需声明一个 API 对象即可管理 kubernetes 集群的生命周期；支持 kubernetes 集群升级；支持 kubernetes 集群扩缩容；支持在本地设置高可用 kubernetes 集群。

- [Kurator 分布式云原生平台 v0.2.0 发布](https://github.com/kurator-dev/kurator/releases/tag/v0.2.0)

    版本特性：支持基于 Thanos 的多集群监控及指标持久化存储；支持基于 Pixie 的实时 K8s 应用监控；新增组件 Cluster Operator，以云原生的方式来管理各种基础设施的 kubernetes 集群生命周期，包括公有云、混合云和本地数据中心。

- [KusionStack：蚂蚁集团开源的可编程云原生协议栈](https://mp.weixin.qq.com/s/EZrVKdZ_hG5-p_HltaTCMg)

    [KusionStack](https://github.com/KusionStack) 通过自研的 DSL（KCL）沉淀运维模型（[Kusion Model](http://github.com/KusionStack/konfig)），将基础设施部分能力的使用方式从白屏转为代码化，同时结合 DevOps 工具链（Kusion CLI）实现配置快速验证和生效，以此提升基础设施的开放性和运维效率。

- [Kusk Gateway 自助式 API 网关 v1.1.0 发布](https://github.com/kubeshop/kusk-gateway/releases/tag/v1.1.0)

    该版本主要新特性：支持指定服务或主机验证 authentication header、支持速率限制策略、通过在 OpenAPI 规范中注释简化 HTTP 缓存的复杂性、由 Envoy 本地处理所有 mocking。

- [Kyma 云原生应用开发平台和运行时 v2.15.0 发布](https://github.com/kyma-project/kyma/releases/tag/2.15.0)

    版本特性：计划将遥测组件重构成一个模块；在 Pod 重启和 webhook 修改的过程中，保持webhook CA 捆绑稳定；新增 HTTP 请求的默认超时；简化了内部 Docker 注册中心的 Serverless 配置；支持 otel-collector 0.77.0。

- [Kyverno 云原生策略引擎 v1.11.0 发布（CNCF 项目）](https://github.com/kyverno/kyverno/releases/tag/v1.11.0)

    版本特性：支持 ValidatingAdmissionPolicy（alpha）；使用 CEL 编写验证规则；使用 CEL 编写兼容的 Kyverno 验证规则时，生成 ValidatingAdmissionPolicy（VAP）；从 VAP 生成策略报告；使用 Kyverno CLI 测试 VAP；基于资源而非策略生成报告；支持 OCI 1.1 和 Cosign 2.0。

- [Kyverno 云原生策略引擎 v1.10.0 发布（CNCF 项目）](https://github.com/kyverno/kyverno/releases/tag/v1.10.0)

    版本特性：将 Kyverno 分成 3 个独立的控制器/Deployment、支持集群内服务调用、支持验证 Notary v2 签名、更新生成和变更现有策略。

- [Kyverno 云原生策略引擎 v1.8.0 发布（CNCF 项目）](https://github.com/kyverno/kyverno/releases/tag/v1.8.0)

    该版本主要新特性：新增 podSecurity 验证子规则，集成 Pod Security Admission 库；支持 YAML 清单签名验证；允许生成规则在单个规则中生成多个资源；支持OpenTelemetry；支持测试生成策略；支持 Kubernetes 1.25。

- [Kyverno 云原生策略引擎升级成为 CNCF 孵化项目](https://mp.weixin.qq.com/s/GijHJm6-JcqfcLn91vSs6g)  

    [Kyverno](https://github.com/kyverno/kyverno) 是为 Kubernetes 打造的策略引擎，为 K8s 配置管理提供了自动化和安全性。
    接下来项目计划添加一些特性，如 YAML 签名和验证、OpenTelemetry 支持、幂等（idempotent）自动生成的 pod 控制器策略、增强的 pod 安全标准集成、基于 OCI 的策略捆绑、集群内 API 调用等。

- [Kyverno 云原生策略引擎 v1.7.0 发布（CNCF 项目）](https://github.com/kyverno/kyverno/releases/tag/v1.7.0)  

    该版本主要新特性：支持通过动态客户端查询`mutate.target`、允许 Kyverno jp 在 Yaml 文件上工作、优化镜像验证签名、在策略更新时 mutate 现有资源、允许用户在上下文中定义内联变量、禁用更新请求控制器的 leader election、在测试中支持 apiCall 以及 CLI 更新等。

### L

- [Lima Linux 虚拟机 v0.14.0 发布（CNCF 项目）](https://github.com/lima-vm/lima/releases/tag/v0.14.0)

    该版本主要新特性：支持虚拟机共享文件系统 virtiofs、支持 Apple 的虚拟化框架 Virtualization.framework、支持 Containerd 命令行工具 nerdctl 1.1.0。

- [Linkerd 服务网格 v2.14.0 发布（CNCF 项目）](https://github.com/linkerd/linkerd2/releases/tag/stable-2.14.0)

    版本特性：新增直接的 Pod 到 Pod 的多集群服务镜像功能、支持 Gateway API HTTPRoute 资源。

- [Linkerd 服务网格项目 v2.13.0 发布（CNCF 项目）](https://github.com/linkerd/linkerd2/releases/tag/stable-2.13.0)

    版本特性：引入客户端策略，包括动态路由和熔断器模式；支持调试基于 HTTPRoute 的策略；引入新的 init 容器 —— network-validator，确保本地 iptables 规则按预期工作。

- [Linkerd 服务网格项目 v2.12.0 发布（CNCF 项目）](https://github.com/linkerd/linkerd2/releases/tag/stable-2.12.0)  

    该版本主要新特性：允许用户以完全零信任的方式定义和执行基于 HTTP 路由的授权策略；支持使用 Kubernetes Gateway API 进行配置；初始化容器增加对 `iptables-nft` 的支持。

- [Litmus 混沌工程框架 3.1.0 发布（CNCF 项目）](https://github.com/litmuschaos/litmus/releases/tag/3.1.0)

    版本特性：在 Pod-network 故障中添加端口黑名单、添加启用和禁用 cron 功能的 UI 更改、添加 Grpc handler 的测试用例、添加 handler 和 service 测试。

- [Litmus：混沌工程框架 3.0 发布（CNCF 项目）](https://github.com/litmuschaos/litmus/releases/tag/3.0.0)

    版本特性：改进用户体验、增加混沌基础设施组织的环境、新增用于简化实验调整的 Chaos Studio、弹性探针现在支持即插即用、支持 MongoDB 高可用性。

- [Litmus 混沌工程框架 v2.14.0 发布（CNCF 项目）](https://github.com/litmuschaos/litmus/releases/tag/2.14.0)

    该版本主要新特性：在 DNS 实验中添加对 containerd CRI 支持、支持在service mesh 环境下执行 http-chaos 实验、在网络实验中增加源和目的端口支持、支持为混沌运行器的 pod 提供自定义标签、优化混沌结果中探针状态模式的描述。

- [Litmus 混沌工程框架 v2.10.0 发布（CNCF 项目）](https://github.com/litmuschaos/litmus/releases/tag/2.10.0)  

    该版本主要新特性：为 Kubernetes 应用增加 HTTP 混沌实验；引入 m-agent（机器代理），现在能够在非 k8s 对象上实施混沌；对混沌期间 应用状态检查失败时 节点警戒线实验的恢复 进行优化；在使用前端 nginx 时增加了对 Envoy 代理的支持；优化日志记录等 Litmusctl 更新。

- [Longhorn 云原生分布式块存储 v1.5.0 发布（CNCF 项目）](https://github.com/longhorn/longhorn/releases/tag/v1.5.0)

    更新内容：推出基于 SPDK（存储性能开发工具包）的 V2 数据引擎、Cluster Autoscaler 功能升级成为 GA、实例管理器引擎和 Replica 合并、支持不同的卷备份压缩方法、自动化卷删除操作、通过 CSI VolumeSnapshot 管理备份镜像、新增快照清理和删除 job、支持 CIFS 备份存储和 Azure 备份存储协议、新增 Kubernetes 升级节点耗尽策略。

- [Longhorn 云原生分布式块存储 v1.4.0 发布（CNCF 项目）](https://github.com/longhorn/longhorn/releases/tag/v1.4.0)

    该版本主要新特性：支持 Kubernetes 1.25、ARM64 的支持升级为 GA、网络文件系统 NFS 的支持升级为 GA、支持卷快照校验、支持卷 Bit-rot 保护、提高卷复制的重建速度、支持通过删除旧快照来回收空间、支持在线卷扩展、允许用户创建一个停留在一致位置的副本卷、增加卷的 I/O 指标、支持备份和恢复 Longhorn 系统。

- [Longhorn 云原生分布式块存储 v1.3.0 发布（CNCF 项目）](https://github.com/longhorn/longhorn/releases/tag/v1.3.0)  

    该版本主要新特性：支持多网络 K8s 集群、兼容全托管 K8s 集群（EKS、GKE、AKS）、新增 Snapshot CRD、新增 Mutating & Validating admission webhooks、支持自动识别并清理无主/未使用的卷、引入 CSI 快照、支持通过 Kubernetes Cluster Autoscaler 进行集群扩展。

### M

- [Merbridge：由 DaoCloud 道客开源的服务网格加速器正式进入 CNCF 沙箱](https://mp.weixin.qq.com/s/Ht1HuLxQ2RngrVD92TBl4Q)

    12 月 14 日，CNCF 基金会宣布 Merbridge 正式被纳入 CNCF 沙箱项目。[Merbridge](https://github.com/merbridge/merbridge) 是目前 CNCF 中唯一专注于使用 eBPF 加速服务网格的开源项目。
    通过 Merbridge 只需要在 Istio 集群执行一条命令，即可直接使用 eBPF 代替 iptables，实现网络加速，提高服务性能。

- [MetalLB Kubernetes 负载均衡器 v1.3.2 发布（CNCF 项目）](https://metallb.universe.tf/release-notes/#version-0-13-2)  

    该版本主要新特性：支持通过 CRD 进行配置（不再支持 ConfigMap）；可以在 L2 或 BGP 模式中广播地址，或者只分配 IP 不广播地址；为 L2 Announcement 和 BGP Announcement 增加节点选择器支持；新增 BGPPeer 选择器；支持使用 kustomize 进行更灵活的部署；增加 LoadBalancerClass 支持；支持多协议 BGP。

- [Microcks API 模拟和测试项目成为 CNCF 沙箱项目](https://mp.weixin.qq.com/s/cdbf_1LUVwb4euldblV14w)

    [Microcks](https://github.com/microcks) 为不同 API 风格和协议 提供了一个事实标准，来加速和确保 API 的交付。Microcks 支持在创建 API contract 之前，使用 “后端即服务”功能测试新的 API，并且支持 REST API、gRPC、GraphQL 和事件驱动的 API 等，无缝集成持续构建或流水线。

- [MicroK8s 轻量级 Kubernetes 发行版 v1.25 发布](https://github.com/canonical/microk8s/releases/tag/v1.25)

    该版本主要新特性：新增“严格限制”（strict confinement）的隔离级别以限制主机系统访问和实施更严格的安全态势、snap 大小减少了 25%、支持镜像侧加载（sideloading）、新增插件 kube-ovn 和 osm-edge。

- [Mimir Prometheus 长期存储项目 v2.4.0 发布](https://github.com/grafana/mimir/releases/tag/mimir-2.4.0)

    该版本主要新特性：引入查询调度器 query-scheduler，并支持 DNS-based 和 ring-based 两种服务发现机制；新增 API 端点暴露每个租户的 limit；增加新的 TLS 配置选项；允许限制最大范围查询长度。

- [Mimir Prometheus 长期存储项目 v2.3.0 发布](https://github.com/grafana/mimir/releases/tag/mimir-2.3.0)

    该版本主要新特性：支持摄取 OpenTelemetry 格式的指标、新增用于元数据查询的租户联盟、简化对象存储配置、支持导入历史数据、优化即时查询功能、默认启用查询分片。

- [Mimir 新功能：将 Graphite、Datadog、Influx 和 Prometheus 的指标纳入统一的存储后端](https://grafana.com/blog/2022/07/25/new-in-grafana-mimir-ingest-graphite-datadog-influx-and-prometheus-metrics-into-a-single-storage-backend/)  

    [Mimir](https://github.com/grafana/mimir) 是 Grafana Labs 在 Cortex 基础上开源的时序数据库。
    Mimir 现在开源了[三个代理](https://github.com/grafana/mimir-proxies)，用于从 Graphite、Datadog 和 InfluxDB 摄取指标，并将这些指标存储在 Mimir 中，这为 Mimir 从任何系统摄取指标奠定了基础。
    未来将支持本地摄取 OpenTelemetry 的 OTLP。

- [MinIO 对象存储工具发布新功能：扩展版本库和正式支持 OPA（CNCF 项目）](https://github.com/minio/minio/releases/tag/RELEASE.2022-05-08T23-50-31Z)

    MinIO 对版本库进行了扩展，排除版本库中的某些前缀和文件夹，以提高 Spark S3A 连接器等应用的性能。此外，应外界广泛要求，MinIO 正式支持 OPA。

### N

- [Nacos 动态服务发现平台 v2.2.0 发布](https://github.com/alibaba/nacos/releases/tag/2.2.0)

    该版本主要新特性：支持批量注册和批量注销服务、支持 openAPI 2.0、增加多数据源插件、增加轨迹追踪插件、支持 Prometheus http 服务发现、支持 Ldaps 认证。

- [Nacos 动态服务发现平台 v2.1.0 发布（CNCF 项目）](https://github.com/alibaba/nacos/releases/tag/2.1.0)

    该版本主要新特性：新增两个 SPI 插件：分别用于配置加解密和认证、支持集群 gRPC 客户端设置线程池大小、支持重置 raft 集群等。

- [Narrows：由 VMware 开源的云原生安全检测器，能够在 Harbor 上增加容器安全的动态扫描](https://mp.weixin.qq.com/s/xJ1Sx5pc0rKkJaYopD-vjw)

    [Narrows](https://github.com/vmware-tanzu/cloud-native-security-inspector) 能够对 Kubernetes 集群和其中的工作负载进行运行时的安全态势评估，发现 Kubernetes 集群的错误配置，终止工作负载运行时中的攻击；对扫描报告进行汇总、聚合和分析并提供开放的API接口；与 Harbor 无缝集成，对于外部公共镜像仓库的镜像，可以自动同步到 Harbor 中，以生成安全数据。

- [nerdctl Containerd 命令行工具 v1.3.0 发布](https://github.com/containerd/nerdctl/releases/tag/v1.3.0)

    版本特性：支持使用 notation 项目进行镜像签名和验证、支持 Port Windows 设备、新的[项目维护者指南](https://github.com/containerd/nerdctl/blob/main/MAINTAINERS_GUIDE.md)正式可用、修复不允许使用 systemd-homed 的无根模式的操作。

- [nerdctl Containerd 命令行工具 v1.2.0](https://github.com/containerd/nerdctl/releases/tag/v1.2.0)

    该版本特性：实验性支持读取 Kubernetes 容器日志、改进编译错误信息、允许在 Windows 上运行 Host Process 容器、添加 Windows HyperV 容器模式。

- [NeuVector 容器安全平台 v5.2.0 发布](https://github.com/neuvector/neuvector/releases/tag/v5.2.0)

    版本特性：新增用于 CVE 查询的搜索 SaaS 服务、支持 NeuVector API 访问令牌、支持针对准入控制的镜像签名、增加对资源限制等自定义准入控制标准的支持、支持通过可插拔扫描仪接口从 Harbor 注册表调用 NeuVector 扫描仪、允许用户禁用网络保护、支持扫描 golang 依赖。

- [NeuVector 容器安全平台 v5.0 发布](https://mp.weixin.qq.com/s/nZ_a7JiryZJskJEPPIEmcw)

    该版本主要新特性：与 SUSE Rancher 集成，也能够与 Amazon EKS、Google GKE 和 Microsoft AKS 等其他企业级容器管理平台对接；支持 Web 应用程序防火墙检测；支持自动化容器保护；支持零漂移进程和文件保护以及对网络、进程/文件进行分割策略模式保护等。

- [Nightingale 夜莺可观测性平台发布 V6 正式版](https://mp.weixin.qq.com/s/ckeaA1JovW43w0jgsj9Y7A)

    版本特性：内置常见的中间件的监控仪表盘和告警规则；支持 LDAP、CAS、OIDC 等多种认证集成；内置支持告警自愈能力；支持灵活的告警规则、屏蔽规则、订阅规则、抑制规则；默认情况下，只需要一个二进制即可对接市面上常见的采集器；集成 ElasticSearch 数据源。

- [Nightgale 夜莺监控 v5.10 发布](https://github.com/ccfos/nightingale/releases/tag/v5.10.0)  

    该版本主要新特性：支持 recording rule 的管理、告警规则支持生效到多集群、仪表盘变量支持 TextBox、告警屏蔽支持更多操作符、更灵活的自定义告警内容。

- [Notification Manager 多租户通知管理系统 2.0.0 发布](https://mp.weixin.qq.com/s/op79OMTp0nxzfxM8fH-nnA)

    [Notification Manager](https://github.com/kubesphere/notification-manager) 能够从 Kubernetes 接收告警、事件、审计，根据用户设置的模板生成通知消息并推送给用户。
    新版本主要功能：新增路由功能，用户通过设置路由规则，将指定的通知发送给指定的用户；新增静默功能，通过配置静默规则，在特定的时间段屏蔽特定的通知；支持动态更新模板等。

- [Nydus 容器镜像加速服务 v2.2.0 发布（CNCF 项目）](https://github.com/dragonflyoss/image-service/releases/tag/v2.2.0)

    版本特性：启用镜像按需加载功能 erofs over fscache、支持 v6 镜像转换、合并子命令支持多个版本的镜像合并、支持将 Nydus 镜像层转换为 tar 文件、增加 BackendProxy 存储后端用于模拟注册表存储后端。

### O

- [OCM 多集群管理平台 v0.9 发布（CNCF 项目）](https://www.cncf.io/blog/2022/10/31/open-cluster-management-november-2022-update/)

    该版本主要新特性：降低托管集群上的worker agent 的权限、支持访问 kube-apiserver 及托管集群中的其他服务、支持使用 AddOn API 参考 AddOn 配置。

- [OPA 通用策略引擎 v0.50.0 发布（CNCF 项目）](https://github.com/open-policy-agent/opa/releases/tag/v0.50.0)

    版本特性：新增内置函数，用于验证 JSON Schema；package 范围内的 schema 注释可以跨模块应用；支持通过一个简单的命令用一个远程捆绑包启动 OPA；引入一个新的 EditTree 数据结构以改善 json.patch 的性能；支持通过状态 API 暴露决策日志错误；所有发布的 OPA 镜像现在都以非 root uid/gid 运行。

- [OPA 通用策略引擎 v0.44.0 发布（CNCF 项目）](https://github.com/open-policy-agent/opa/releases/tag/v0.44.0)  

    该版本主要新特性：修复 3 个 CVE 漏洞、Set Element Addition 优化、内置 Set union 优化、在 OPA 评估命令中添加优化参数、允许将更多的捆绑程序编译到 WASM 中。

- [OPA 通用策略引擎 v0.43.0 发布（CNCF 项目）](https://github.com/open-policy-agent/opa/releases/tag/v0.43.0)

    该版本主要新特性：Rego Object 插入的线性扩展优化、状态和日志插件现在可以接受 HTTP 2xx 状态代码、OPA bundle 命令现在支持 .yml 文件、存储系统修复、Rego 编译器和运行环境 bug 修复和优化。

- [OPA 通用策略引擎 v0.41.0 发布（CNCF 项目）](https://github.com/open-policy-agent/opa/releases/tag/v0.41.0)

    该版本主要新特性：新增一组内置函数用于验证、解析和查证 GraphQL query 和模式；内置函数声明支持通过元数据指定函数参数和返回值的名称和描述；支持根据 OCI 工件的摘要跳过捆绑重载；捆绑签名中删除空清单；单位解析和 token 更新等。

- [OpenClusterManagement（OCM）多集群管理平台 v0.12.0 发布（CNCF 项目）](https://github.com/open-cluster-management-io/ocm/releases/tag/v0.12.0)

    版本特性：新增插件管理功能门、支持 hub 集群和托管集群之间的代理、支持托管模式下的单例、添加 ClusterAnnotations 支持、增加 issue 和 PR 的过期检查。

- [OpenClusterManagement（OCM）多集群管理平台 v0.7 发布（CNCF 项目）](https://mp.weixin.qq.com/s/EQgdnZVOqzfvuxOzg-Q0cQ)

    该版本主要新特性：新增“DefaultClusterSet”功能，所有注册进 OCM 环境中的托管集群都会被默认注册进名叫“default” 的 ClusterSet 中；支持基于 Taint / Toleration 的语义的多集群调度；部署架构调整为“Hosted 部署”模式，即托管集群内将不需要再部署其他的组件，所有的代理控制器均在远端执行。

- [OpenCost 引入多云成本监控](https://www.opencost.io/blog/cloud-costs)

    OpenCost 的新多云成本监控解决方案为跨多个云平台管理成本提供了无缝体验。通过易于使用的界面和简单的 API，OpenCost 让你能够在 Google Cloud、Amazon Web Services（AWS）和 Microsoft Azure 上以统一的视图监控云费用。

- [OpenCost 支持 FinOps 开放成本和使用规范（FOCUS)](https://www.opencost.io/blog/focus)

    FinOps 开放成本和使用规范（FinOps Open Cost and Usage Specification，FOCUS）发布了其规范的第一个版本，以定义云成本、使用和计费数据的开放标准。OpenCost 项目宣布支持这个标准，并已经开始使用这个标准支持初始补丁。

- [OpenEBS 云原生存储 v3.4.0 发布（CNCF 项目）](https://github.com/openebs/openebs/releases/tag/v3.4.0)

    版本特性：支持通过 OpenEBS helm chart 安装 Mayastor、支持在故障检测时按需切换 Mayastor 节点、支持使用 NDM 的 NVMe 虚拟路径检测、修复 LVM LocalPV helm chart 的拉取镜像密钥错误、在 NFS 服务器部署中添加后端卷 PVC 上下文作为标签。

- [OpenEBS 云原生存储 v3.3.0 发布（CNCF 项目）](https://github.com/openebs/openebs/releases/tag/v3.3.0)  

    该版本主要新特性：弃用 arch-specific 容器镜像、为 LocalPV Hostpath 强制执行带有 ext4 文件系统的主机路径配额、增强 NDM 功能、在 cstor 中添加日志以改善调试能力、增加速率限制器以减少 LocalPV LVM 中的日志泛滥问题。

- [OpenFunction 函数即服务项目 v1.0.0 发布（CNCF 项目）](https://github.com/OpenFunction/OpenFunction/releases/tag/v1.0.0)

    版本特性：集成 wasmedge、支持从本地源代码构建、单个 Pod 支持多个函数、支持检测源代码或镜像的变化并重建/重新部署新构建的镜像。

- [OpenKruise 升级为 CNCF 孵化项目](https://mp.weixin.qq.com/s/9knMn8eKJBNdXUU-TcmTQg)

    [OpenKruise](https://github.com/openkruise/kruise/) 是一个扩展的组件套件，专注于应用程序自动化，如部署、升级、运维和可用性保护等方面。OpenKruise 通过其创新的 CRD 扩展帮助具有大型工作负载的组织采用和自动化 Kubernetes 和云原生部署，为 AI / ML 等领域的新用例打开了大门。

- [OpenKruise 云原生应用自动化管理套件 v1.4.0 发布（CNCF 项目）](https://github.com/openkruise/kruise/releases/tag/v1.4.0)

    版本特性：新增 JobSidecarTerminator 功能，可以在主容器退出后终止 sidecar 容器；新增字段用于立即重新创建容器；在 ImagePullJob 的过程中，支持在 PullImage CRI 接口中附加元数据；sidecarSet 控制器支持命名空间选择器；将 Kubernetes 的镜像地址引用从 “k8s.gcr.io” 更改为 “registry.k8s.io”。

- [OpenKruise 云原生应用自动化管理套件 v1.3.0 发布（CNCF 项目）](https://github.com/openkruise/kruise/releases/tag/v1.3.0)

    该版本主要新特性：支持自定义探针并将结果返回给 Pod yaml、SidecarSet 支持在 kube-system 和 kube-public 命名空间下注入 pod、增加对上游 AdvancedCronJob 的 timezone 支持、WorkloadSpread 支持 StatefulSet。

- [OpenKruise 云原生应用自动化管理套件 v1.2.0 发布（CNCF 项目）](https://github.com/openkruise/kruise/releases/tag/v1.2.0)  

    该版本主要新特性：新增 CRD `PersistentPodState`来持久化 Pod 的某些状态，如“固定 IP 调度”；CloneSet 针对百分比形式 partition 计算逻辑变化；在 lifecycle hook 阶段设置 Pod not-ready；支持保护 scale subresource 的任意自定义工作负载；新增大规模集群的性能优化方法等。

- [OSM（Open Service Mesh）开放服务网格项目停止维护](https://mp.weixin.qq.com/s/_eqhL999E1ojmTAoaAOuiQ)

    OSM 采用 Service Mesh Interface （SMI）作为其标准 API，从而允许与支持 SMI 的其他服务网格实现进行兼容，以简化服务网格操作体验。近日，OSM 维护团队宣布 OSM 不再发布新的版本，团队将转向与 Istio 社区共同合作，来推进 Istio 的发展。

- [Open Service Mesh 服务网格 v1.2.0 发布（CNCF 项目）](https://github.com/openservicemesh/osm/releases/tag/v1.2.0)  

    该版本主要新特性：支持自定义信任域（即证书通用名）、Envoy 更新到 v1.22，并且使用 envoyproxy/envoy-distroless 镜像、增加对 Kubernetes 1.23 和 1.24 的支持、支持限制 TCP 连接和 HTTP 请求的本地 per-instance 速率、修复 Statefulset 和 headless service。

- [OpenShift Toolkit 1.0，简化云原生应用的开发](https://cloud.redhat.com/blog/announcing-openshift-toolkit-enhance-cloud-native-application-development-in-ides)

    [OpenShift Toolkit](https://github.com/redhat-developer/vscode-openshift-tools) 是一套 VS Code 和 IntelliJ 扩展。其功能包括：支持连接和配置 OpenShift；提供混合云支持，开发者可以连接到任何正在运行的 OpenShift 实例；可通过本地工作区、git 仓库或默认的 devfile 模板来开发应用程序；允许采用一键式策略，将仓库代码直接部署到 OpenShift；提供 Kubernetes 资源管理、无缝 Kube 配置上下文切换；多平s台支持。

- [OpenTelemetry 可观测项目 v1.21.0 发布（CNCF 项目）](https://github.com/open-telemetry/opentelemetry-specification/releases/tag/v1.21.0)

    版本特性：添加实验性的直方图建议 API、明确记录日志时使用的参数、将 OpenCensus 兼容性规范标记为稳定。

- [OpenTelemetry v1.13.0 发布（CNCF 项目）](https://github.com/open-telemetry/opentelemetry-specification/releases/tag/v1.13.0)  

    该版本主要新特性：在设置 span 时Context 是不可变的、支持实验性的配置 OTLP 指标输出器的默认直方图聚合、允许日志处理器修改日志记录、添加实验性的事件和日志 API 规范、在流程语义约定中添加网络指标、为 GraphQL 添加语义约定。

- [OpenTelemetry Metrics 发布 RC 版本](https://opentelemetry.io/blog/2022/metrics-announcement/)

    Java、.NET、Python 已经发布了 OpenTelemetry 指标的 RC 版本（JS 下周发布）。这意味着， specification、API、SDK 以及以创作、捕获、处理等方式与 metrics 交互的组件，现在拥有完整的 OTel metrics 功能集，并且随时可供使用。

- [OpenTelemetry v1.11.0 发布 （CNCF 项目）](https://github.com/open-telemetry/opentelemetry-specification/releases/tag/v1.11.0)

    该版本主要新特性：用更加了然的 bucket 直方图取代直方图、支持在 OpenMetrics 计数器上显示示例、增加数据库连接池指标的语义规范、允许所有 metrics 规范为同步或异步、添加HTTP/3 等。

- [Openyurt 云原生边缘计算项目 v1.4.0 发布（CNCF 项目）](https://github.com/openyurtio/openyurt/releases/tag/v1.4.0)

    版本特性：支持 HostNetwork 模式的 NodePool、支持多区域工作负载的 NodePool 级别自定义配置、通过 PlatformAdmin 支持构建 EdgeX IoT 系统、支持将 yurt-iot-dock 部署为 IoT 系统组件。

- [Openyurt 云原生边缘计算项目 v1.3.0 发布（CNCF 项目）](https://github.com/openyurtio/openyurt/releases/tag/v1.3.0)

    版本特性：重构 Openyurt 控制平面组件， 新组件 yurt-manager 用于管理多个组件的控制器和 webhook；允许用户为静态 Pod 定义 Pod 模板和升级模型；NodePort Service 支持节点池隔离。

- [Openyurt 云原生边缘计算项目 v1.2.0 发布（CNCF 项目）](https://github.com/openyurtio/openyurt/releases/tag/v1.2.0)

    新增节点池治理组件 Pool-Coordinator，用于降低云边网络带宽，提高云边网络故障时的边缘自治能力；使用 raven 组件来替代 yurt-tunnel 组件解决跨区域网络通信问题；改进证书管理器。

- [Openyurt 云原生边缘计算项目 v1.1.0 发布（CNCF 项目）](https://github.com/openyurtio/openyurt/releases/tag/v1.1.0)

    该版本主要新特性：支持 DaemonSet 工作负载的 OTA/自动升级模式、支持 e2e 测试的自治功能验证、启用数据过滤功能、增加统一云计算边缘通信方案的建议、改进 health checker。

- [Openyurt 云原生边缘计算项目 v1.0.0 发布（CNCF 项目）](https://github.com/openyurtio/openyurt/releases/tag/v1.0.0)  

    该版本主要新特性：NodePool API 版本升级到 v1beta1、使用 CodeCov 跟踪单元测试覆盖率、新增两份 OpenYurt 组件的性能测试报告。

- [OpenKruise 云原生应用自动化管理套件 v1.2.0 发布（CNCF 项目）](https://github.com/openkruise/kruise/releases/tag/v1.2.0)  

    该版本主要新特性：新增 CRD `PersistentPodState`来持久化 Pod 的某些状态，如“固定 IP 调度”；CloneSet 针对百分比形式 partition 计算逻辑变化；在 lifecycle hook 阶段设置 Pod not-ready；支持保护 scale subresource 的任意自定义工作负载；新增大规模集群的性能优化方法等。

- [osm-edge：易衡科技 Flomesh 开源的边缘服务网格](https://mp.weixin.qq.com/s/tbCxbKFQkvx84Ku5IWg38g)

    [osm-edge](https://github.com/flomesh-io/osm-edge) 采用 [osm](https://github.com/openservicemesh/osm) 作为控制平面，可编程网关 [Pipy](https://github.com/flomesh-io/pipy) 作为数据平面。
    支持 SMI 规范；支持 ingress、gateway API、跨集群服务发现的 [fsm](https://github.com/flomesh-io/fsm)，提供“k8s 集群内+多集群”的“东西+南北”流量管理和服务治理能力。
    其开发和测试环境采用 k3s、k8e 等，因此用户可以快速低成本地在 x86、arm、RISC-V、龙芯等硬件平台上部署低资源高性能的服务网格。

### P

- [Paralus Kubernetes 零信任访问服务成为 CNCF 沙箱项目](https://mp.weixin.qq.com/s/hYmMT0mvMdO6-LW6oHxteg)

    [Paralus](https://github.com/paralus/paralus) 专为多集群环境设计，凭借即时服务帐户创建和细粒度的用户凭证管理，保证资源访问的安全性。
    此外，Paralus 还融入了零信任原则，支持多个身份提供商、自定义角色等。

- [Paralus：Rafay Systems 开源的业内首个 Kubernetes 零信任访问服务](https://rafay.co/the-kubernetes-current/paralus-industrys-first-open-source-zero-trust-access-service-for-kubernetes/)

    [Paralus](https://github.com/paralus/paralus) 的主要功能有：能够统一处理多个集群的访问管理、允许与现有的 RBAC 策略和 SSO provider 集成、支持记录组织内用户执行的每一条 kubectl 命令、支持 OIDC、支持创建具有特定权限的自定义角色、允许动态撤销权限等。  

- [Phlare：Grafana 开源的大规模持续性能分析数据库](https://grafana.com/blog/2022/11/02/announcing-grafana-phlare-oss-continuous-profiling-database/)

    [Phlare](https://github.com/grafana/phlare) 是一个水平可扩展、高可用、多租户的持续分析数据聚合系统，与 Grafana 完全集成，可以与指标、日志和追踪等观测指标相关联。安装只需一个二进制文件，无需其他依赖项。
    Phlare 使用对象存储进行长期数据存储，并兼容多种对象存储实现。其原生多租户和隔离功能集允许多个独立团队或业务部门运行一个数据库。

- [PipeCD 成为 CNCF 沙箱项目](https://pipecd.dev/blog/2023/05/19/cncf-sandbox-admission/)

    [PipeCD](https://github.com/pipe-cd/pipecd) 为多云应用提供了一个统一的持续交付解决方案，为任何应用程序提供一致的部署和操作体验.PipeCD 是一个 GitOps 工具，能够通过 Git 上的 pr 请求进行部署操作。

- [Pisanix：SphereEx 开源面向 Database Mesh 的解决方案](https://mp.weixin.qq.com/s/p8bi14s8FWdp7GlqQxKzzw)  

    [Pisanix](https://github.com/database-mesh/pisanix) 帮助用户轻松实现基于 Database Mesh 框架下 SQL 感知的流量治理、面向运行时的资源可编程、数据库可靠性工程等能力，助力用户云上数据库治理。Pisanix目前已支持 MySQL 协议，主要包括 Pisa-Controller、Pisa-Proxy 和 Pisa-Daemon（即将推出）三个组件。

- [Pixie Kubernetes 观测平台 发布 Plugin System](https://www.cncf.io/blog/2022/07/06/easy-observability-with-open-standards-introducing-the-pixie-plugin-system/)  

    [Pixie Plugin System](https://github.com/pixie-io/pixie-plugin) 允许用户将其 Pixie 数据导出到任何支持 OpenTelemetry 的服务中。这意味着用户可以利用外部数据存储长期保留数据，在现有工作流和仪表盘中无缝采用 Pixie，将 Pixie 数据与其他数据流结合。

- [Podman 容器运行时项目 v4.5.0 发布](https://github.com/containers/podman/releases/tag/v4.5.0)

    版本特性：支持对在 Pod 内运行的容器进行自动更新、支持使用 SQLite 数据库作为后端、增加对容器网络堆栈 Netavark 插件的支持、支持带有 Macvlan 和 Netavark 后台的 DHCP。

- [Podman 容器引擎 v4.3.0 发布](https://github.com/containers/podman/releases/tag/v4.3.0)

    命令更新：支持改变容器的资源限制、删除 K8s YAML 创建的 pod 和容器、支持 K8s secret、支持从 URL 读取 YAML、支持 emptyDir 卷类型、支持 ConfigMap 中的二进制数据；支持重复的卷挂载。

- [Podman 容器运行时项目 v4.2.0 发布](https://github.com/containers/podman/releases/tag/v4.2.0)  

    该版本主要新特性：支持 GitLab Runner、新增命令用于创建现有 pod 的副本、新增命令用于同步数据库和任何卷插件之间的状态变化、pod 新增退出策略、自动清理未使用的缓存 Podman 虚拟机镜像、允许不同容器的多个 overlay 卷重复使用同一个 workdir 或 upperdir。

- [Prometheus v2.46.0 发布（CNCF 项目）](https://github.com/prometheus/prometheus/releases/tag/v2.46.0)

    版本特性：添加 PromQL 格式和标签匹配器设置/删除命令、推送指标命令、为 K8s 服务发现的 Endpointslice 和 Endpoints Role 添加了更多标签、PodIP 的状态未设置时不会将 Pod 添加到目标组、支持验证远程写入处理程序中的指标名称和标签、支持将原生直方图存储在快照中。

- [Prometheus v2.45.0 发布（CNCF 项目）](https://github.com/prometheus/prometheus/releases/tag/v2.45.0)

    更新内容：支持限制每个 TSDB 统计项的返回数量、在全局配置中增加限制、支持同时摄入 classic 直方图和 native 直方图、native 直方图支持限制存储桶的大小。

- [Prometheus v2.44.0 发布（CNCF 项目）](https://github.com/prometheus/prometheus/releases/tag/v2.44.0)

    版本特性：每次发送的默认样本数提高到 2,000、支持处理原生直方图数据、在命令行中添加用于检查 Prometheus 服务器健康状态和可用性的功能、添加所有查询加载的样本总数指标。

- [Prometheus v2.43.0 发布（CNCF 项目）](https://github.com/prometheus/prometheus/releases/tag/v2.43.0)

    版本特性：在一个单独的字符串中存储所有的标签和对应的值，以减小内存占用（只在使用 Go tag stringlabels 进行编译时启用）；在查询命令中提供 HTTP 客户端配置；添加从不同文件中导入抓取配置的选项；新增两个 HTTP 客户端配置参数；允许通过 API 动态设置查询的回溯时间。

- [Prometheus v2.42.0 发布（CNCF 项目）](https://github.com/prometheus/prometheus/releases/tag/v2.42.0)

    该版本特性：支持原生直方图、更改原生直方图的 WAL 记录格式、支持选择 TSDB dump 时间序、支持 Float 直方图、为 Kubernetes 的 pod 对象添加容器 ID 作为元标签。

- [Prometheus v2.40.0 发布（CNCF 项目）](https://github.com/prometheus/prometheus/releases/tag/v2.40.0)

    该版本主要新特性：增加对原生直方图的实验性支持、Kubernetes 发现客户端支持使用 protobuf 编码、改善排序速度、增加企业管理分区。

- [Prometheus v2.39.0 发布（CNCF 项目）](https://github.com/prometheus/prometheus/releases/tag/v2.39.0)

    该版本主要新特性：增加对摄取无序样本的实验性支持、优化内存资源用量。

- [Prometheus v2.37.0 发布（CNCF 项目）](https://github.com/prometheus/prometheus/releases/tag/v2.37.0)  

    该版本主要新特性：允许 Kubernetes 服务发现从端点角色向目标添加节点标签、TSDB 内存优化、读取 WAL 时减少睡眠时间、优化签名创建、添加超时和 User-Agent header。

- [Prometheus v2.37.0 发布（CNCF 项目）](https://github.com/prometheus/prometheus/releases/tag/v2.37.0)  

    该版本主要新特性：允许 Kubernetes 服务发现从端点角色向目标添加节点标签、TSDB 内存优化、读取 WAL 时减少睡眠时间、优化签名创建、添加超时和User-Agent header。

- [Prometheus v2.36.0 发布（CNCF 项目）](https://github.com/prometheus/prometheus/releases/tag/v2.36.0)  

    该版本主要新特性：集成 Vultr、添加 Linode SD 故障计数指标和 `prometheus_ready` 指标、在模板 function 中添加 `stripDomain`、promtool 支持在查询标签值时使用匹配器、增加代理模式标识符。

- [Pyroscope 性能持续分析平台 v1.0 发布](https://github.com/grafana/pyroscope/releases/tag/v1.0.0)

    Pyroscope 是一个可水平扩展、高可用、多租户的持续分析聚合系统，其架构与 Grafana Mimir、Loki 和 Tempo 相似；提供 Helm、Tanka 和 docker-compose 安装指南；可使用 Grafana Explore 和仪表盘将持续分析数据与其他可观测数据关联起来。

### R

- [Radius：Azure 开源的云原生应用平台](https://azure.microsoft.com/en-us/blog/the-microsoft-azure-incubations-team-launches-radius-a-new-open-application-platform-for-the-cloud/)

    [Radius](https://github.com/radius-project/radius) 通过支持 Kubernetes 、现有的基础设施工具（如 Terraform 和 Bicep）以及与现有的 CI/CD 系统（如 GitHub Actions）集成，旨在使开发人员和平台工程师能够合作交付和管理符合成本要求及运维和安全最佳实践的云原生应用。目前支持在私有云Azure 和 AWS 等云平台上部署应用，并计划支持更多的云提供商。

- [Rainbond 信创版本的云原生多云应用管理平台发布](https://mp.weixin.qq.com/s/eelPIhoCQdAfBnQOm_YDAg)

    Rainbond 信创版支持部署和管理多个单架构集群。支持 amd64 集群、arm64 集群、amd64 & arm64 混合架构集群的一键部署和管理。兼容主流国产化 CPU，同时与多个国产化操作系统进行了适配。支持传统应用快速迁移到信创环境。云原生应用商店支持发布和安装 arm64 架构的应用。

- [Rainbond 云原生多云应用管理平台 v5.14.0 发布](https://github.com/goodrain/rainbond/releases/tag/v5.14.0-release)

    版本特性：升级各语言源码构建包版本；支持一键删除应用及应用下相关资源；使用集群命令行创建的 Pod 有合理的回收机制；域名配置 https 证书时，增加搜索功能或优先匹配与域名相同的证书；支持配置日志存储路径。

- [Rainbond 云原生多云应用管理平台 v5.12.0 发布](https://github.com/goodrain/rainbond/releases/tag/v5.12.0-release)

    版本特性：支持平台级插件和能力扩展、新增流水线插件、支持通过 OpenAPI 创建组件、优化 Helm 仓库安装应用逻辑。

- [Rainbond 云原生多云应用管理平台 v5.9.0 发布](https://github.com/goodrain/rainbond/releases/tag/v5.9.0-release)

    该版本主要新特性：支持 Containerd 容器运行时、支持使用 grctl 命令更改 cluster API 地址、支持 K8s 1.24 和 1.25、支持 MiniKube 部署、支持自定义监控规则。

- [Rainbond 云原生多云应用管理平台 v5.8.0 发布](https://github.com/goodrain/rainbond/releases/tag/v5.8.0-release)  

    该版本主要新特性：支持一键导入 Kubernetes 集群中已存在的应用、支持直接通过 Jar、War 包或 Yaml 文件部署组件、支持创建 Job/CronJob 类型任务、支持扩展应用和组件支持的属性、支持 Dockerfile 使用私有镜像构建。

- [Rook 云原生存储项目 v1.12.0 发布（CNCF 项目）](https://github.com/rook/rook/releases/tag/v1.12.0)

    版本特性：支持 Kubernetes v1.22+、默认使用 Ceph CSI v3.9、支持 Ceph Reef（v18）、增加用于配置存储桶的 Ceph COSI 驱动程序（实验性）、节点丢失后自动恢复 RBD (RWO) 卷、引入 Multus 网络验证工具、通过放弃容器特权来改进安全性、支持 RGW 作为 CephNFS 后端（实验性）。

- [Rook 云原生存储项目 v1.11.0 发布（CNCF 项目）](https://github.com/rook/rook/releases/tag/v1.11.0)

    版本特性：支持 K8s v1.21 及以上版本、Ceph-CSI v3.8 成为默认部署的版本、移除对机器中断预算（MachineDisruptionBudgets）的支持、对象存储桶的通知和主题功能升至稳定状态、支持在具有重叠 CIDR 的多个集群间进行数据镜像、Ceph exporter 成为 Ceph 性能计数器（performance counter）的指标来源。

### S

- [Sealer 分布式应用交付工具 v0.9.0 发布（CNCF 项目）](https://github.com/sealerio/sealer/releases/tag/v0.9.0)

    该版本主要新特性：支持通过 Clusterfile 配置标签、权限、角色、注册表、集群主机别名；支持 ipv4/ipv6 双栈；支持本地注册表的高可用模式；支持基于 buildah 的 OCI 标准；Kubefile 支持 Helm 包、k8s yaml 文件、shell 脚本等应用类型。

- [Serverless-cd：Serverless Devs 发布基于 Serverless 架构的轻量级 CI/CD 框架——](https://mp.weixin.qq.com/s/ps_ZFsv7KGwV2V61SvvWIA)

    Serverless Devs 是业内首个支持主流 Serverless 服务/框架的云原生全生命周期管理的平台。[Serverless-cd](https://github.com/Serverless-Devs/serverless-cd) 基于 Serverless Devs 打造，完全遵循 Serverless 架构最佳实践，在规范和生态层面参考 Github Action 的实现。其采用 Master Worker 模型和事件驱动的架构，可用于快速构建企业内部应用管理 PaaS 平台。

- [Serverless Devs 进入 CNCF 沙箱，成首个入选的 Serverless 工具项目](https://mp.weixin.qq.com/s/ICVDO3U5Ea1DzP3LFJq8mQ)

    [Serverless Devs](https://github.com/Serverless-Devs/Serverless-Devs) 由阿里云开源，致力于为开发者提供强大的工具链体系。借此，开发者不仅可以一键体验多云 Serverless 产品，极速部署 Serverless 项目，还可以在 Serverless 应用全生命周期进行项目管理，与其他工具/平台集成，提升研发运维效能。

- [Skywalking 应用性能监控系统 v9.6.0 发布](https://github.com/apache/skywalking/releases/tag/v9.6.0)

    版本特性：支持 MQE（Metrics Query Expression），并引入一种新的通知机制；现在可以使用 Loki LogQL 查询语言和 Grafana Loki Dashboard 来查看和分析 SkyWalking 收集的日志；支持基于 OTEL 实现的 MongoDB 服务器/集群监控；改进构建过程，使其具备可复制性，以便于进行自动发布的 CI 流程。

- [Skywalking 应用性能监控系统 v9.5.0 发布](https://github.com/apache/skywalking/releases/tag/v9.5.0)

    版本特性：新的拓扑结构布局图、支持对 Elasticsearch 服务器监控、支持持续分析功能、支持收集进程级相关指标、支持跨线程跟踪分析、支持监控 k8s StatefulSet 和 DaemonSet 的总数量指标、支持 Redis 和 RabbitMQ 监控。

- [Skywalking 应用性能监控系统 v9.3.0 发布](https://github.com/apache/skywalking/releases/tag/v9.3.0)

    该版本主要新特性：增加指标关联功能、可使用 Sharding MySQL 作为数据库、可视化虚拟缓存和消息队列的性能、使用 Skywalking OpenTelemetry 接收器代替 prometheus-fetcher 插件来抓取 Prometheus 指标。

- [Skywalking 应用性能监控系统 v9.2.0 发布](https://github.com/apache/skywalking/releases/tag/v9.2.0)  

    该版本主要新特性：新增 K8s Pod 的 eBPF 网络分析功能、支持 MySQL 和 PostgreSQL 监控、关联事件组件和追踪、日志组件。

- [Skywalking 应用性能监控系统 v9.1.0 发布（CNCF 项目）](https://github.com/apache/skywalking/releases/tag/v9.1.0)  

    该版本主要新特性：更新 eBPF Profiling 任务到服务级别；为事件添加层字段，禁止报告没有层的事件；Zipkin 接收器机制改变，追踪不再流向 OAP 段；SQL 数据库相关更新；移除 InfluxDB 1.x 和 Apache IoTDB 0.X 的存储方案，添加 BanyanDB 存储方案（尙在开发中）。

- [SPIFFE 与 SPIRE 项目正式成为 CNCF 毕业项目](https://www.cncf.io/announcements/2022/09/20/spiffe-and-spire-projects-graduate-from-cloud-native-computing-foundation-incubator/)

    [SPIFFE](https://github.com/spiffe/spiffe) 为现代生产环境中的各种工作负载提供安全身份，消除了机密信息的共享需求，有望成为更高级别的平台中立安全控制方案的实现基础。
    [SPIRE](https://github.com/spiffe/spire)（SPIFFE 运行时环境）则负责在各种平台上实现 SPIFFE 规范，并强制发布身份的多因素证明。

- [Spring Cloud Tencent：腾讯开源一站式微服务解决方案](https://mp.weixin.qq.com/s/A-DcZJY9sJcTQSEoWEibww)  

    [Spring Cloud Tencent](https://github.com/Tencent/spring-cloud-tencent) 依托腾讯开源的一站式微服务解决方案 北极星（Polaris），主要提供微服务领域常见的服务注册与发现、配置中心、服务路由、限流熔断以及元数据链路透传能力。

- [Strimzi 消息中间件 Kafka 的 K8s operator v0.31.0 发布（CNCF 项目）](https://github.com/strimzi/strimzi-kafka-operator/releases/tag/0.31.0)  

    该版本主要新特性：支持 Kafka 3.2.1；可插拔的 Pod 安全配置文件，内置支持受限的 Kubernetes 安全配置文件；支持 leader 选举和运行多个 operator 副本；支持在 Strimzi 签发的证书中使用 IPv6 地址。

- [SuperEdge 边缘容器管理系统 v0.8.0 发布（CNCF 项目）](https://github.com/superedge/superedge/releases/tag/v0.8.0)  

    该版本主要新特性：将 edgeadm 从SuperEdge 项目中分离出来、tunnel 支持 http_proxy 能力、Lite-apiserver 支持在边缘节点缓存一些关键资源（节点、service 等）和 ExternalName Service 转发。

- [Sylva 云原生基础设施堆栈由 Linux 基金会欧洲分部推出，为电信服务奠定云原生的基础](https://www.prnewswire.com/news-releases/linux-foundation-europe-announces-project-sylva-to-create-open-source-telco-cloud-software-framework-to-complement-open-networking-momentum-301678955.html)

    [Sylva](https://gitlab.com/sylva-projects/sylva) 利用容器网络功能（CNF）和 Kubernetes 等云原生平台来创建电信云技术栈，以减少电信和边缘服务的云基础设施的分散性。
    Sylva 提供的技术栈由 5 个部分组成：网络性能（SRIOV、DPDK、指定 CNI 等）、分布式云（多集群 Kubernetes、裸机自动化）、能源效率、安全性（加固和合规性）以及开放性和标准化 API。

### T

- [TDengine 云原生时序数据库 v3.0 发布](https://github.com/taosdata/TDengine/releases/tag/ver-3.0.0.0)  

    该版本主要新特性：支持 10 亿个设备采集的数据、100 个节点；支持存储与计算分离，引入计算节点，并重构了整个计算引擎；优化了对消息队列、流式计算和缓存的支持，引入事件驱动的流式计算；支持容器和 Kubernetes 部署。

- [Tekton 云原生 CI/CD 框架 v0.50.0 发布](https://github.com/tektoncd/pipeline/releases/tag/v0.50.0)

    版本特性：CSI 和计划卷 workspace 功能升级为稳定状态、单独 workspace 功能升级为 beta、支持还原 PVC 创建、添加事件配置映射、引入联合调度（coschedule）功能开关、支持在 PipelineRun 完成后自动删除由其卷声明模板创建的 PVC。

- [Tekton：云原生 CI/CD 框架 v0.43.0 发布](https://github.com/tektoncd/pipeline/releases/tag/v0.43.0)

    该版本主要新特性：支持解析 sidecar 日志以提取结果到任务运行的 CRD 中、默认启用 pipeline 中的自定义任务、增加对 PipelineRun 调节器的支持、允许用户为可信资源配置公钥、PodTemplate 可以用来更新全局的环境变量。

- [Tekton 云原生 CI/CD 框架 v0.42.0 发布](https://github.com/tektoncd/pipeline/releases/tag/v0.42.0)

    该版本主要新特性：支持配置 Webhook 端口号、支持为集群资源设置源值、新增一个和状态治理字段有关的 feature flag、支持记录远程资源的来源、在 reconciler 中添加验证功能。

- [Tekton 云原生 CI/CD 框架 v0.40.0 发布](https://github.com/tektoncd/pipeline/releases/tag/v0.40.0)

    该版本主要新特性：添加任务运行模板、支持在 pipelinerun 中传播 workspace 以简化规范编写、优化 git 远程解析支持、添加集群远程解析器、合并 podtempalte 和 affinity-assistant 的亲和力参数。

- [Telepresence K8s 本地开发工具 v2.14.0 发布（CNCF 项目）](https://www.getambassador.io/docs/telepresence-oss/latest/release-notes#2.14.0)

    版本特性：DNS 配置新增排除字段和映射字段、支持排除环境变量、支持检测和报告客户端计算机上运行的其他 VPN 软件之间的路由冲突。

- [Telepresence K8s 本地开发工具 v2.10.0 发布（CNCF 项目）](https://www.getambassador.io/docs/telepresence/latest/release-notes#2.10.0)

    该版本主要新特性：流量管理器支持被团队模式和单用户模式、在 Helm Chart 中添加拉取镜像的 secret、OSS Helm chart 将被推送到 telepresence 专有仓库（原先为 datawire Helm 仓库）。

- [Tetragon 安全可观测和运行时增强平台 v1.0 发布](https://github.com/cilium/tetragon/releases/tag/v1.0.0)

    版本特性：调整 Kubernetes 中导出的日志 JSON 文件的权限、构建 ARM64 架构的tarball（压缩归档文件）、支持显示 UID 和 GID 信息以及检测进程是否正在以特权执行的方式运行、在 kprobe 事件中添加内核堆栈跟踪功能、在多个系统调用上附加 killer 程序、默认开启命名空间策略和 Pod 标签过滤器的功能。

- [Tetragon 安全可观测和运行时增强平台 v0.11.0 发布](https://github.com/cilium/tetragon/releases/tag/v0.11.0)

    在 Helm Chart 中添加 Tetragon operator 的 deployment、支持 IPv6、支持监视 Kubernetes service、添加访问 K8sResourceWatcher 的功能、删除已删除 Pod 的指标、在带有 Pod 信息的指标中添加工作负载标签、为 Pod 信息 CRD 添加注册逻辑。

- [Tetragon 安全可观测和运行时增强平台 v0.10.0 发布](https://github.com/cilium/tetragon/releases/tag/v0.10.0)

    版本特性：支持在 configmap 更改时重新创建 daemonset Pod、添加用于跟踪策略指标的事件、Pod 标签过滤器支持跟踪策略、支持加载 Linux 安全模块 LSM 和跟踪程序、 启用 bpf 对象的并行构建、为事件添加速率限制、添加套接字跟踪、为文件监控添加策略。

- [Tetragon 安全可观测和运行时增强平台 v0.9.0 发布](https://github.com/cilium/tetragon/releases/tag/v0.9.0)

    版本特性：增加加载 BPF 程序的日志功能、支持使用 cosign 进行容器镜像签名、支持基本的 Cgroups 跟踪功能、支持 pprof http、gRPC 支持使用 unix socket。

- [Tetragon：Isovalent 开源基于 eBPF 的安全可观测性和运行时增强平台](https://isovalent.com/blog/post/2022-05-16-tetragon)  

    [Tetragon](https://github.com/cilium/tetragon) 提供了基于 eBPF 的完全透明的安全可观测性能力以及实时的运行时增强能力。
    Tetragon 基于 eBPF 的内核级收集器中直接内置了智能内核过滤能力和聚合逻辑，因此无需更改应用程序即可以非常低的开销实现深度的可观测性。
    内嵌的运行时执行层不仅能够在系统调用层面进行访问控制，
    而且能够检测到特权、Capabilities 和命名空间的提权逃逸，并实时自动阻止受影响进程的进一步执行。

- [ThreatMapper 云原生安全观测平台 v1.4.0 发布](https://github.com/deepfence/ThreatMapper/releases/tag/v1.4.0)  

    该版本主要新特性：新功能 ThreatGraph 能够结合网络等运行时环境来确定威胁扫描结果的优先级、支持对云资产进行无代理的云安全态势管理、集成云原生环境恶意程序扫描工具 [YaraHunter](https://github.com/deepfence/YaraHunter)。

- [Trivy 容器漏洞扫描工具 v0.46.0 发布（CNCF 项目）](https://github.com/aquasecurity/trivy/releases/tag/v0.46.0)

    版本特性：支持扫描 Kubernetes 控制平面和节点组件中的漏洞、增加对 .NET 项目许可信息的检索功能、向 Kubernetes 资源的扫描报告中添加了元数据、在 CI 流程中添加了一个用于检查依赖项的 Go 版本的工作流。

- [Trivy 容器漏洞扫描工具 v0.44.0 发布（CNCF 项目）](https://github.com/aquasecurity/trivy/releases/tag/v0.44.0)

    版本特性：支持扫描本地仓库、将集成测试超时增加至 15 分钟、支持展示漏洞状态、支持策略捆绑的自定义 URL、支持为 Rego 策略自定义数据。

- [Trivy 容器漏洞扫描工具 v0.41.0 发布（CNCF 项目）](https://github.com/aquasecurity/trivy/discussions/4135)

    版本特性：支持使用 Vulnerability Exploitability Exchange（VEX）来过滤已检测到的漏洞、支持生成虚拟机镜像的 SBOM、支持嵌套 JAR 路径、支持使用自定义的 Docker socket。

- [Trivy 容器漏洞扫描工具 v0.39.0 发布（CNCF 项目）](https://github.com/aquasecurity/trivy/releases/tag/v0.39.0)

    版本特性：OCI 工件下载支持授权功能、支持在 OCI referrer 中发现 SBOM、支持 k8s 并行资源扫描、增加并发处理的 pipeline、增加节点容忍选项。

- [Trivy 容器漏洞扫描工具 v0.35.0 发布（CNCF 项目）](https://github.com/aquasecurity/trivy/releases/tag/v0.35.0)

    该版本主要新特性：为虚拟机镜像新增扫描器、多架构镜像支持 OS 通配符、支持按 digest 扫描镜像、增加慢速模式以降低 CPU 和内存利用率。

- [Trivy 容器漏洞扫描工具 v0.33.0 发布（CNCF 项目）](https://github.com/aquasecurity/trivy/releases/tag/v0.33.0)

    该版本主要新特性：禁用非 amd64 架构的 containerd 集成测试、重构 k8s 自定义报告、支持 non-packaged 二进制文件、修复 golang x/text 漏洞。

- [Trivy 容器漏洞扫描工具 v0.32.0 发布（CNCF 项目）](https://github.com/aquasecurity/trivy/releases/tag/v0.32.0)

    该版本主要新特性：增加对 SPDX 的扫描、支持 Rust 二进制文件的依赖扫描、增加对  gradle.lockfile 和 conan.lock 文件的支持。

- [Trivy 容器漏洞扫描工具 v0.31.0 发布（CNCF 项目）](https://github.com/aquasecurity/trivy/releases/tag/v0.31.0)

    该版本主要新特性：支持扫描 SBOM 证明、为dockerfile 的 misconf 处理程序添加测试、增加对 Cosign 漏洞证明的支持、允许用户为 token 定义一个已有的 secret、增加两个新漏洞。

- [Trivy 容器漏洞扫描工具 v0.30.0 发布（CNCF 项目）](https://github.com/aquasecurity/trivy/releases/tag/v0.30.0)

    该版本主要新特性：支持扫描许可证、推送 canary 构建镜像到注册表、Trivy k8s 支持扫描 single argument 资源、支持扫描 Cyclonedx 软件物料清单（SBOM）、增加 pnpm 支持。

- [Trivy 容器漏洞扫描工具 v0.29.0 发布（CNCF 项目）](https://github.com/aquasecurity/trivy/releases/tag/v0.29.0)  

    该版本主要新特性：支持 RBAC 扫描、支持 K8s secret 扫描、增加对 WASM 模块的支持、增加对 containerd 的支持、支持显示慢速扫描建议、为 pom 文件中的变量评估增加了循环检查、新增 go mod tidy 检查。

- [Trivy 容器漏洞扫描工具现在可以扫描几乎所有与云原生相关的东西（CNCF 项目）](https://thenewstack.io/aqua-securitys-trivy-security-scanner-can-scan-anything-now/)  

    Aqua 称，[Trivy](https://github.com/aquasecurity/trivy) 是当前最全面的漏洞和错误配置扫描工具，
    可用于扫描云原生应用程序和基础设施，如源代码、存储库、镜像、工件注册表、基础设施即代码（IaC）模板和 Kubernetes 环境等。

### V

- [vcluster 虚拟 Kubernetes 集群实现方案 v0.16.0 发布](https://github.com/loft-sh/vcluster/releases/tag/v0.16.0)

    版本特性：支持 Kubernetes v1.28、允许用户自定义的 Pod 条件和节点污点、支持不使用模板创建 vcluster、添加 vcluster 和 vcluster cli 二进制 sbom、改进 coredns 集成。

- [vcluster 虚拟 Kubernetes 集群实现方案 v0.15.0 发布](https://github.com/vmware-tanzu/velero/releases/tag/v1.11.0)

    版本特性：允许用户在 vcluster 内访问所有主机集群服务、新增内置指标服务器、通用同步功能支持从主机集群导入集群范围资源。

- [vcluster 虚拟 Kubernetes 集群实现方案 v0.13.0 发布](https://github.com/loft-sh/vcluster/releases/tag/v0.13.0)

    该版本主要新特性：增加日志和备份功能、增加具有外部数据存储的 k3s 的高可用性支持、vcluster 调度器开启时自动同步 CSI 资源。

- [Velero 备份容灾工具 v1.11.0 发布（CNCF 项目）](https://github.com/vmware-tanzu/velero/releases/tag/v1.11.0)

    版本特性：增加插件进度监控功能、支持过滤备份时要跳过的卷、新增集群范围和命名空间范围的资源过滤器、增加用于设置 Velero 服务器与 k8s API 服务器的超时连接的参数、支持 JSON 格式的备份描述命令输出、用 controller-runtime 重构控制器、CSI 插件会通过检查 `restorePVs` 参数的设置来决定是否从快照中恢复数据。

- [Velero 备份容灾工具 v1.10.0 发布（CNCF 项目）](https://github.com/vmware-tanzu/velero/releases/tag/v1.10.0)

    该版本主要新特性：引入统一存储库架构、集成跨平台备份工具 [Kopia](https://github.com/kopia/kopia)、重构文件系统备份、使用 Kubebuilder v3 对控制器进行重构、允许为卷快照位置添加凭证、增强 CSI 快照的稳健性、支持暂停备份计划、重命名部分模块和参数。

- [Velero 备份容灾工具 v1.9.0 发布（CNCF 项目）](https://github.com/vmware-tanzu/velero/releases/tag/v1.9.0)  

    该版本主要新特性：CSI 支持改进、使用 Kubebuilder v3 对控制器进行了重构、支持恢复所选资源的状态、支持在资源恢复过程中更新现有资源。

- [Virtink：由 SmartX 开源的轻量 Kubernetes 原生虚拟化管理引擎](https://mp.weixin.qq.com/s/LOZ8RhFE_9SZKwcdV90dPw)

    不同于 KubeVirt，[Virtink](https://github.com/smartxworks/virtink) 并不支持遗留硬件设备的模拟以及桌面应用场景能力，而是使用 [Cloud Hypervisor](https://github.com/cloud-hypervisor/cloud-hypervisor) 作为底层虚拟化管理器，只支持现代化的云负载，可以在任何虚拟化 CPU 平台的 Kubernetes 中进行安装，以更安全轻量的方式支撑虚拟化负载。

- [Vitess 云原生数据库系统 v14.0.0 发布（CNCF 项目）](https://github.com/vitessio/vitess/releases/tag/v14.0.0)  

    该版本主要新特性：正式支持 online DDL、Gen4 成为默认的 planner、新增集群管理 API 和 UI——VTAdmin（Beta）、新增一个作为 Vitess 组件运行的 Orchestrator 分支——VTOrc（Beta）、支持跨多个 shard 和 keyspace 的聚合查询。

- [Volcano 云原生批量计算项目 v1.8.0 发布（CNCF 项目）](https://github.com/volcano-sh/volcano/releases/tag/v1.8.0)

    版本特性：添加 JobFlow 支持轻量级工作流编排、支持 vGPU 调度和隔离、支持 GPU 和用户定义资源的抢占能力、支持将 ElasticSearch 监控系统用于节点负载感知的调度和重新调度、添加 Kubernetes 默认调度器插件的启用和禁用开关、提供设备插件异常容错机制、为 Volcano 添加 Helm Chart。

- [Volcano 云原生批量计算项目 v1.7.0 发布（CNCF 项目）](https://github.com/volcano-sh/volcano/releases/tag/v1.7.0)

    该版本主要新特性：增加 Pytorch job 插件、支持为分布式高性能 AI 计算框架 Ray 提供批量调度、丰富调度策略以支持更多长期运行服务的应用场景、支持 Kubernetes v1.25、支持多架构镜像、支持实时查看队列的资源分配信息。

- [Volcano 云原生批量计算项目 v1.6.0 发布（CNCF 项目）](https://github.com/volcano-sh/volcano/releases/tag/v1.6.0)  

    该版本主要新特性：支持基于真实节点负载的动态调度和重调度、支持弹性作业调度、新增 MPI job 插件、允许任务失败时不重试、支持查看 pod 请求的开销、支持在 pod group 入列过程中考虑资源配额、默认特权容器通过 admission webhook 的验证。

### W

- [WasmEdge WebAssembly 运行时 v0.13.0 发布（CNCF 项目）](https://github.com/WasmEdge/WasmEdge/releases/tag/0.13.0)

    更新内容：统一 wasmedge CLI 工具、将 WasmEdge 扩展移植为插件、引入 wasi_logging 插件、编译时支持启用未定义行为检测器、引入了将数据包含到模块实例的新 API、支持异步调用 WASM 函数、引入统一的工具 API。

- [WasmEdge WebAssembly 运行时 v0.12.0 发布（CNCF 项目）](https://github.com/WasmEdge/WasmEdge/releases/tag/0.12.0)

    版本特性：引入了插件上下文和相关的 API、引入了多个 WASI 套接字 API 实现、增加 VM API、增加 wasm_bpf 插件。

- [Wazero：Tetrate 开源的 Go 语言开发的 WebAssembly 运行时](https://mp.weixin.qq.com/s/aozmJpuwD69vGWcM525ucg)

    Wazero 可以让开发者用不同的编程语言编写代码，并在安全的沙箱环境中运行。Wazero 的特点包括：纯 Go，无依赖，支持跨平台和跨架构；遵循 WebAssembly 核心规范 1.0 和 2.0；支持 Go 的特性，如并发安全和上下文传递；提供了丰富的编程接口和命令行工具。

- [werf CI/CD 的 CLI 工具 成为 CNCF 沙箱项目](https://mp.weixin.qq.com/s/DGA1_k16QAQImFmy8mWcDw)

    [werf](https://github.com/werf/werf) 可以与用户现有的任何 CI/CD 系统融合，为 Kubernetes 提供了应用全生命周期管理。
    werf 依赖 Buildah 来构建容器镜像，兼容各种容器注册中心来管理镜像，使用 Helm chart 将应用程序部署到 Kubernetes。
    此外，其还支持自动构建缓存、基于内容的标签、Helm 中增强的资源跟踪功能、智能清理旧的/未使用的容器镜像等功能。

- [Wolfi：Chainguard 发布首个保障软件供应链安全的 Linux 发行版，专为容器和云原生环境设计](https://www.chainguard.dev/unchained/introducing-wolfi-the-first-linux-un-distro)  

    [Wolfi](https://github.com/wolfi-dev) 是一个为云原生设计的精简版 Linux 发行版，但其没有 Linux 内核，而是依靠环境（如容器运行时）来提供内核。主要功能：为所有软件包提供高质量构建时的 SBOM 作为标准；软件包是细粒度和相互独立的，以支持轻量级镜像；使用成熟可靠的 apk 包格式、完全声明性的、可重复的构建系统、支持 glibc 和 musl。

### X, Z

- [Xline 跨云元数据 KV 存储 进入 CNCF 沙箱项目](https://mp.weixin.qq.com/s/Pj8TOStT_oEABZGqFkCVaA)

    [Xline](https://github.com/datenlord/Xline) 是一个开源的分布式的 KV 存储，用来管理少量的关键性数据，并在跨云跨数据中心的场景下仍然保证高性能和数据强一致性。Xline 兼容 etcd 接口，提供 KV 接口，多版本并发控制，同时与 K8S 兼容，让用户使用和迁移更加流畅。

- [Xline 由 DatenLord 开源：实现跨数据中心数据一致性管理](https://mp.weixin.qq.com/s/NqScUOjUA1t4gdNeLEcPwg)

    [Xline](https://github.com/datenlord/Xline) 旨在解决 etcd 无法完全满足跨云跨数据中心场景需求的问题。Xline 是一个分布式的 KV 存储，用来管理少量的关键性数据，并在跨云跨数据中心的场景下仍然保证高性能和数据强一致性。其兼容 etcd 接口，让用户使用和迁移更加流畅。

- [Zadig 云原生持续交付工具 v1.12.0 发布](https://github.com/koderover/zadig/releases/tag/v1.12.0)  

    该版本主要新特性：支持代码扫描、支持服务关联多个构建、K8s YAML 项目支持从现有 K8s 导入服务、支持从 Gitee 代码库中同步服务配置、支持服务配置变更后自动更新环境、支持全局构建模板、K8s Helm Chart 环境支持自测模式、支持集成多个 Jenkins 等。
