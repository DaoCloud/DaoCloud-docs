# 开源项目

- [CNI 插件 Antrea v1.9.0 发布（CNCF 项目）](https://github.com/antrea-io/antrea/releases/tag/v1.9.0)

    该版本主要新特性：新增多个多集群功能，包括跨集群 Pod 间连接、节点控制器支持 Gateway 高可用、允许 Pod IP 作为多集群 service 的端点；增加类似于 kube-proxy 的 service 健康检查；审计日志添加规则名称；一个 service 支持 800+ 端点。

- [APISIX v3.0 云原生 API 网关发布](https://github.com/apache/apisix/blob/release/3.0/CHANGELOG.md#300)

    v3.0 新增 Consumer Group 用于管理多个消费者、支持配置 DNS 解析域名类型的顺序、新增 AI 平面用于智能分析和可视化配置与流量、全面支持 ARM64、新增 gRPC 客户端、实现数据面与控制面的完全分离、提供控制面的服务发现支持、新增 xRPC 框架、支持更多四层可观测性、集成 OpenAPI 规范、全面支持 Gateway API。

- [Arbiter：时速云开源基于 K8s 构建的可扩展调度和弹性工具](https://mp.weixin.qq.com/s/xF6Zij2FB2dq3QsZO6ch1g)

    [Arbiter](https://github.com/kube-arbiter/arbiter) 聚合各种类型的数据，用户可以基于这些数据管理、调度或扩展集群中的应用程序。它可以帮助 Kubernetes 用户了解和管理集群中部署的资源，进而提高企业应用程序的资源利用率和运行效率。

- [GitOps 工具 Argo CD v2.5.0 发布（CNCF 项目）](https://github.com/argoproj/argo-cd/releases/tag/v2.5.0)

    该版本主要新特性：支持基于集群过滤应用程序、添加 Prometheus 健康检查、添加通知 API、支持 CLI 的自定义应用程序操作、增加对默认容器注释的支持、限制 redis 的出口规则、添加 Gitlab PR 生成器 webhook、新增 ApplicationSet Go 模板、新增 ArgoCD CLI 本地模板。

- [由 AWS 开源的 Kubernetes 开发框架 cdk8s+ 正式可用](https://aws.amazon.com/blogs/containers/announcing-general-availability-of-cdk8s-plus-and-support-for-manifest-validation/)

    [cdk8s+](https://github.com/cdk8s-team/cdk8s) 允许用户使用熟悉的编程语言和面向对象的 API 来定义 Kubernetes 应用和可复用的抽象。相较于去年发布的 beta 版本，正式版本新增功能包括：隔离 pod 网络，只允许指定的通信；改进在同一节点上运行多个 pod的配置机制；集成 [Datree](https://github.com/datreeio/datree-cdk8s) 插件，使用第三方策略执行工具检查 Kubernetes 中的错误配置。

- [云原生证书管理项目 Cert-manager v1.10.0 发布（CNCF 项目）](https://github.com/cert-manager/cert-manager/releases/tag/v1.10.0)

    该版本主要新特性：使用 trivy 扫描本地构建的容器；如果目标 Secret 配置错误或在请求后创建，重新同步签署请求；增加从 Kubernetes Secret 加载 Vault CA Bundle 的选项；支持在 chart 部署的所有资源上添加相同的标签。

- [云原生证书管理项目 Cert-manager 升级成为 CNCF 孵化项目](https://www.cncf.io/blog/2022/10/19/cert-manager-becomes-a-cncf-incubating-project/)

    Cert-manager 是 Kubernetes 的一个插件，用于自动管理和颁发各种来源的 TLS 证书，为云原生工作负载提供加密保护。近日，CNCF 技术监督委员会已经投票接受 cert-manager 成为 CNCF 孵化项目。

- [Chaos Mesh v2.5.0 混沌工程平台发布（CNCF 项目）](https://github.com/chaos-mesh/chaos-mesh/releases/tag/v2.5.0)

    该版本主要新特性：支持多集群混沌实验、HTTPChaos 增加 TLS 支持、允许在 Helm 模板中为 controller manager 和仪表盘配置 Pod 安全上下文、StressChaos 支持 cgroups v2。

- [Cloud Custodian v0.9.20 云资源管理工具发布（CNCF 项目）](https://github.com/cloud-custodian/cloud-custodian/releases/tag/0.9.20.0)

    该版本主要新特性：增加 K8s admission controller 模式、添加角色和集群角色资源。

- [Clusternet v0.13.0 多云多集群管理项目发布](https://github.com/clusternet/clusternet/releases/tag/v0.13.0)

    该版本主要新特性：增加从父集群到子集群 pod 的路由功能、添加调度器配置并支持自定义调度器插件、支持 discovery v1beta1、只为 k8s v1.21.0 及更高版本提供发现 endpointslice 的支持、使用阈值聚合工作节点标签、支持按集群 subgroup 进行调度、为在 capi 中运行的 clusternet-agent 更新 RBAC 规则。

- [分布式应用运行时 Dapr v1.9.0 发布（CNCF 项目）](https://github.com/dapr/dapr/releases/tag/v1.9.0)

    该版本主要新特性：允许自定义可插拔组件、支持 OTel 协议、增加弹性观测指标、支持应用健康检查、支持设置默认弹性策略、允许使用任何中间件组件进行服务见调用、新增 pub/sub 命名空间消费者组、支持 Podman 容器运行时。

- [API 网关 Envoy Gateway v0.2 发布](https://github.com/envoyproxy/gateway/releases/tag/v0.2.0)

    该版本主要新特性：支持 Kubernetes、支持 Gateway API 资源。

- [eunomia-bpf eBPF 轻量级开发框架正式开源](https://mp.weixin.qq.com/s/fewVoIKbLn5fYbXUaDyTpQ)

    [eunomia-bpf](https://gitee.com/anolis/eunomia) 由各高校和龙蜥社区共同开发，旨在简化 eBPF 程序的开发、分发、运行。在 eunomia-bpf 中，只需编写内核态代码即可正确运行，在部署时不需要重新编译，并提供 JSON/WASM 的标准化分发方式。

- [日志处理工具 Fluent Bit v2.0.0 发布 （CNCF 项目）](https://github.com/fluent/fluent-bit/releases/tag/v2.0.0)

    该版本主要新特性：增加对 Traces 的支持（与 Prometheus 和 OpenTelemetry 完全集成）、允许 input 插件在一个单独的线程中运行、所有需启用安全的网络传输层将使用 OpenSSL、input 插件新增原生 TLS 功能、支持将更多的插件类型与 Golang 和 WebAssembly 集成、支持检查流经管道的数据、引入收集和处理内部指标的新 input 插件。

- [策略引擎 Gatekeeper v3.10.0 发布 （CNCF 项目）](https://github.com/open-policy-agent/gatekeeper/releases/tag/v3.10.0)

    该版本主要新特性：移除 Pod 安全策略并迁移到 Pod 安全准入、Mutation 功能升级为稳定、引入工作负载资源的验证（alpha）、性能改进。

- [Komodor 开源 Helm 图形界面 Helm Dashboard](https://github.com/komodorio/helm-dashboard)

    Helm Dashboard 可在本地运行并在浏览器中打开，可用于查看已安装的 Helm Chart，查看其修订历史和相应的 k8s 资源。此外，还可以执行简单的操作，如回滚到某个版本或升级到较新的版本。

- [Grafana 开源大规模持续性能分析数据库 Phlare](https://grafana.com/blog/2022/11/02/announcing-grafana-phlare-oss-continuous-profiling-database/)

    [Phlare](https://github.com/grafana/phlare) 是一个水平可扩展、高可用、多租户的持续分析数据聚合系统，与 Grafana 完全集成，可以与指标、日志和追踪等观测指标相关联。安装只需一个二进制文件，无需其他依赖项。Phlare 使用对象存储进行长期数据存储，并兼容多种对象存储实现。其原生多租户和隔离功能集允许多个独立团队或业务部门运行一个数据库。

- [**阿里云开源云原生网关 Higress**](https://mp.weixin.qq.com/s/dgvd9TslzhX1ZuUNIH2ZXg)

    [Higress](https://github.com/alibaba/higress) 遵循 Ingress/Gateway API 标准，将流量网关、微服务网关、安全网关三合一，并在此基础上扩展了服务管理插件、安全类插件和自定义插件，高度集成 K8s 和微服务生态，包括 Nacos 注册和配置、Sentinel 限流降级等能力，并支持规则变更毫秒级生效等热更新能力。

- [Istio v1.16 发布（CNCF 项目）](https://istio.io/latest/news/releases/1.16.x/announcing-1.16/)

    该版本主要新特性：三个功能升级为 beta：外部授权功能、Kubernetes Gateway API 实现、基于路由的 JWT 声明；增加对 sidecar 和入口网关的 HBONE 协议的实验性支持、支持 MAGLEV 负载均衡算法、通过 Telemetry API 支持 OpenTelemetry tracing provider。

- [Kubernetes 全局负载均衡器 k8gb v0.10.0 发布（CNCF 项目）](https://github.com/k8gb-io/k8gb/releases/tag/v0.10.0)

    该版本主要新特性：可以通过环境变量访问 LeaderElection、支持 OpenTelemetry 的 tracing 方案、支持创建 K8GB 指标的Grafana 仪表盘样本、实现一致的轮询负载均衡策略。

- [Karpenter v0.19.0 自动扩缩容工具发布](https://github.com/aws/karpenter/releases/tag/v0.19.0)

    该版本主要新特性：默认驱逐无控制器的 pod、将 AWS 设置从 CLI Args 迁移到 ConfigMap、支持 IPv6 自动发现、将 webhook和控制器合并为一个二进制文件。

- [安全容器运行时 Kata Containers v3.0.0 发布](https://github.com/kata-containers/kata-containers/releases/tag/3.0.0)

    该版本主要新特性：新增 Rust 语言重写的容器运行时组件以及一个可选的集成虚拟机管理组件、支持主流的云原生生态组件（包括 Kubernetes、CRI-O、Containerd 以及 OCI 容器运行时标准等）、支持 cgroupv2、支持最新的 Linux 内核稳定版本。

- [基于 Kubernetes 的 serverless 架构方案 Knative v1.8.0 发布（CNCF 项目）](https://github.com/knative/serving/releases/tag/knative-v1.8.0)

    该版本主要新特性：修改默认域、升级 HPA 到 v2 版本、允许设置 seccompProfile 以启用使用受限的安全配置文件、最低 k8s 支持版本升至 v1.23、调和超时时间提高到 30 秒、默认启用 EmptyDir 卷功能参数。

- [Karpenter v0.19.0 自动扩缩容工具发布](https://github.com/aws/karpenter/releases/tag/v0.19.0)

    该版本主要新特性：默认驱逐无控制器的 pod、将 AWS 设置从 CLI Args 迁移到 ConfigMap、支持 IPv6 自动发现、将 webhook和控制器合并为一个二进制文件。

- [Koordinator v1.0 云原生混部系统发布](https://github.com/koordinator-sh/koordinator/releases/tag/v1.0.0)

    该版本主要新特性：优化任务调度、优化 ElasticQuota 调度、支持细粒度的设备调度管理机制、支持根据节点的负载水位调整 BestEffort 类型 Pod 的 CPU 资源额度、支持使用 CPU Burst 来提高延迟敏感应用的性能、实现基于内存安全阈值和资源满足的驱逐机制、精细化 CPU 调度、支持在不侵入 Kubernetes 已有的机制和代码前提下预留资源、简化自定义重调度策略的操作。

- [KubeKey v3.0 集群部署工具发布](https://github.com/kubesphere/kubekey/releases/tag/v3.0.0)

    该版本主要新特性：为 docker 构建和推送添加 GitHub 工作流、支持执行自定义设置脚本、添加 k3s 控制平面控制器和启动控制器、添加 k3s 容器运行时配置、添加 k3s e2e 测试支持、自定义 OpenEBS 基本路径、重构 KubeKey 项目、支持更多的 Kubernetes 和 k3s 版本。

- [集群部署工具 KubeKey v2.3.0 发布](https://github.com/kubesphere/kubekey/releases/tag/v2.3.0)

    该版本主要新特性：添加 kubelet pod pid 限制、使用 Jenkins Pipeline 替代 GitHub Actions、在创建集群或添加节点时增加安全增强命令、删除集群或节点时清理 vip、支持 kube-vip BGP 模式、支持清理 CRI、支持  kube-vip、支持 k8s 最近发布的补丁版本。

- [KubeVela v1.6.0 混合多云环境应用交付平台发布（CNCF 项目）](https://github.com/kubevela/kubevela/releases/tag/v1.6.0)

    该版本主要新特性：支持资源交付可视化、提供可观测基础设施搭建、面向应用的可观测、可观测即代码的能力、支持多环境流水线统一管理、支持应用间配置的共享并与第三方外部系统做配置集成。

- [虚拟机管理插件 KubeVirt v0.58.0 发布（CNCF 项目）](https://github.com/kubevirt/kubevirt/releases/tag/v0.58.0)

    该版本主要新特性：在 cluster-deploy 中默认启用 DataVolume 垃圾回收、能够在启用受限的 Pod 安全标准时运行、添加 tls 配置、修复在有 containerd 的系统上带有 containerdisks 的虚拟机迁移失败问题。

- [Kuma 服务网格 v2.0 发布（CNCF 项目）](https://github.com/kumahq/kuma/releases/tag/2.0.0)

    该版本主要新特性：在 CNI 和 init 容器配置中增加对 eBPF 的支持、新增 3 个“下一代”策略、优化用户界面、支持配置控制平面/API 服务器所支持的 TLS 版本和密码、允许配置多个 UID 使其被流量重定向忽略、允许在使用 iptables 进行流量重定向时开启日志功能。

- [云原生策略引擎 Kyverno v1.8.0 发布（CNCF 项目）](https://github.com/kyverno/kyverno/releases/tag/v1.8.0)

    该版本主要新特性：新增 podSecurity 验证子规则，集成 Pod Security Admission 库；支持 YAML 清单签名验证；允许生成规则在单个规则中生成多个资源；支持OpenTelemetry；支持测试生成策略；支持 Kubernetes 1.25。

- [混沌工程框架 Litmus v2.14.0 发布（CNCF 项目）](https://github.com/litmuschaos/litmus/releases/tag/2.14.0)

    该版本主要新特性：在 DNS 实验中添加对 containerd CRI 支持、支持在service mesh 环境下执行 http-chaos 实验、在网络实验中增加源和目的端口支持、支持为混沌运行器的 pod 提供自定义标签、优化混沌结果中探针状态模式的描述。

- [容器引擎 Podman v4.3.0 发布](https://github.com/containers/podman/releases/tag/v4.3.0)

    命令更新：支持改变容器的资源限制、删除 K8s YAML 创建的 pod 和容器、支持 K8s secret、支持从 URL 读取 YAML、支持 emptyDir 卷类型、支持 ConfigMap 中的二进制数据；支持重复的卷挂载。

- [Prometheus 长期存储项目 Mimir v2.4.0 发布](https://github.com/grafana/mimir/releases/tag/mimir-2.4.0)

    该版本主要新特性：引入查询调度器 query-scheduler，并支持 DNS-based 和 ring-based 两种服务发现机制；新增 API 端点暴露每个租户的 limit；增加新的 TLS 配置选项；允许限制最大范围查询长度。

- [KubeVela v1.6.0 混合多云环境应用交付平台发布（CNCF 项目）](https://github.com/kubevela/kubevela/releases/tag/v1.6.0)

    该版本主要新特性：支持资源交付可视化、提供可观测基础设施搭建、面向应用的可观测、可观测即代码的能力、支持多环境流水线统一管理、支持应用间配置的共享并与第三方外部系统做配置集成。

- [Kuma 服务网格 v2.0 发布（CNCF 项目）](https://github.com/kumahq/kuma/releases/tag/2.0.0)

    该版本主要新特性：在 CNI 和 init 容器配置中增加对 eBPF 的支持、新增 3 个“下一代”策略、优化用户界面、支持配置控制平面/API 服务器所支持的 TLS 版本和密码、允许配置多个 UID 使其被流量重定向忽略、允许在使用 iptables 进行流量重定向时开启日志功能。

- [OCM v0.9 发布多集群管理平台（CNCF 项目）](https://www.cncf.io/blog/2022/10/31/open-cluster-management-november-2022-update/)

    该版本主要新特性：降低托管集群上的worker agent 的权限、支持访问 kube-apiserver 及托管集群中的其他服务、支持使用 AddOn API 参考 AddOn 配置。

- [Openyurt v1.1.0 云原生边缘计算项目发布（CNCF 项目）](https://github.com/openyurtio/openyurt/releases/tag/v1.1.0)

    该版本主要新特性：支持 DaemonSet 工作负载的 OTA/自动升级模式、支持 e2e 测试的自治功能验证、启用数据过滤功能、增加统一云计算边缘通信方案的建议、改进 health checker。

- [OpenShift Toolkit 1.0，简化云原生应用的开发](https://cloud.redhat.com/blog/announcing-openshift-toolkit-enhance-cloud-native-application-development-in-ides)

    [OpenShift Toolkit](https://github.com/redhat-developer/vscode-openshift-tools) 是一套 VS Code 和 IntelliJ 扩展。其功能包括：支持连接和配置 OpenShift；提供混合云支持，开发者可以连接到任何正在运行的 OpenShift 实例；可通过本地工作区、git 仓库或默认的 devfile 模板来开发应用程序；允许采用一键式策略，将仓库代码直接部署到 OpenShift；提供 Kubernetes 资源管理、无缝 Kube 配置上下文切换；多平s台支持。

- [Grafana 开源大规模持续性能分析数据库 Phlare](https://grafana.com/blog/2022/11/02/announcing-grafana-phlare-oss-continuous-profiling-database/)

    该版本主要新特性：引入查询调度器 query-scheduler，并支持 DNS-based 和 ring-based 两种服务发现机制；新增 API 端点暴露每个租户的 limit；增加新的 TLS 配置选项；允许限制最大范围查询长度。

- [Prometheus v2.40.0 发布（CNCF 项目）](https://github.com/prometheus/prometheus/releases/tag/v2.40.0)

    该版本主要新特性：增加对原生直方图的实验性支持、Kubernetes 发现客户端支持使用 protobuf 编码、改善排序速度、增加企业管理分区。

- [Prometheus v2.39.0 发布（CNCF 项目）](https://github.com/prometheus/prometheus/releases/tag/v2.39.0)

    该版本主要新特性：增加对摄取无序样本的实验性支持、优化内存资源用量。

- [Rainbond v5.9.0 云原生多云应用管理平台发布](https://github.com/goodrain/rainbond/releases/tag/v5.9.0-release)

    该版本主要新特性：支持 Containerd 容器运行时、支持使用 grctl 命令更改 cluster API 地址、支持 K8s 1.24 和 1.25、支持 MiniKube 部署、支持自定义监控规则。

- [Serverless Devs 发布基于 Serverless 架构的轻量级 CI/CD 框架——Serverless-cd](https://mp.weixin.qq.com/s/ps_ZFsv7KGwV2V61SvvWIA)

    Serverless Devs 是业内首个支持主流 Serverless 服务/框架的云原生全生命周期管理的平台。[Serverless-cd](https://github.com/Serverless-Devs/serverless-cd) 基于 Serverless Devs 打造，完全遵循 Serverless 架构最佳实践，在规范和生态层面参考 Github Action 的实现。其采用 Master Worker 模型和事件驱动的架构，可用于快速构建企业内部应用管理 PaaS 平台。

- [Sylva 云原生基础设施堆栈由 Linux 基金会欧洲分部推出，为电信服务奠定云原生的基础](https://www.prnewswire.com/news-releases/linux-foundation-europe-announces-project-sylva-to-create-open-source-telco-cloud-software-framework-to-complement-open-networking-momentum-301678955.html)

    [Sylva](https://gitlab.com/sylva-projects/sylva) 利用容器网络功能（CNF）和 Kubernetes 等云原生平台来创建电信云技术栈，以减少电信和边缘服务的云基础设施的分散性。Sylva 提供的技术栈由 5 个部分组成：网络性能（SRIOV、DPDK、指定 CNI 等）、分布式云（多集群 Kubernetes、裸机自动化）、能源效率、安全性（加固和合规性）以及开放性和标准化 API。

- [Tekton v0.42.0 云原生 CI/CD 框架发布](https://github.com/tektoncd/pipeline/releases/tag/v0.42.0)

    该版本主要新特性：支持配置 Webhook 端口号、支持为集群资源设置源值、新增一个和状态治理字段有关的 feature flag、支持记录远程资源的来源、在 reconciler 中添加验证功能。

- [容器漏洞扫描工具 Trivy v0.33.0 发布（CNCF 项目）](https://github.com/aquasecurity/trivy/releases/tag/v0.33.0)

    该版本主要新特性：禁用非 amd64 架构的 containerd 集成测试、重构 k8s 自定义报告、支持 non-packaged 二进制文件、修复 golang x/text 漏洞。

- [Vcluster v0.13.0 虚拟 Kubernetes 集群实现方案发布](https://github.com/loft-sh/vcluster/releases/tag/v0.13.0)

    该版本主要新特性：增加日志和备份功能、增加具有外部数据存储的 k3s 的高可用性支持、vcluster 调度器开启时自动同步 CSI 资源。
