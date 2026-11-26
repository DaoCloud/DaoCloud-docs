# Kubernetes v1.38 抢先看：cgroup 旧机制退场与资源管理进阶

> 原英文博客位于 [k8s.io/blog/](https://kubernetes.io/blog/2026/11/23/kubernetes-v1-38-sneak-peek/)

Kubernetes v1.38 正在收敛为一次围绕 **配置机制精简与资源管理进阶** 的版本更新：
`kubectl` 移除了两处遗留的配置项，kubelet 默认要求容器运行时通过 CRI 报告 cgroup 驱动，
cgroup v1 的退出也进入倒计时。
与此同时，kuberc、Pod 级别资源和 DRA 可分区设备三项能力预计进阶到稳定版，
EvictionRequest API 则以 Alpha 形态带来更协调的 Pod 驱逐方式。

本文梳理了值得平台团队和集群运维人员优先关注的 v1.38 计划内变更。
以下内容反映的是当前发布周期的状态，实际发布日期前仍可能调整。

!!! tip

    - 如果你的集群仍在使用 cgroup v1，应将迁移纳入近期计划；
    - 如果自行管理节点或节点镜像，应在升级前确认容器运行时支持 CRI `RuntimeConfig`；
    - 如果工作负载启用了 Pod 级别资源并依赖交换内存，应在升级前完成兼容性验证。

## 一分钟了解 v1.38

| 领域 | 变更要点 |
| --- | --- |
| kubectl | `KUBECTL_REMOTE_COMMAND_WEBSOCKETS` 和 `KUBECTL_PORT_FORWARD_WEBSOCKETS` 环境变量被移除；kuberc 预计进阶到稳定版，凭证插件允许列表条目的 `name` 字段随之退出。 |
| 节点与运行时 | kubelet 默认要求容器运行时通过 CRI `RuntimeConfig` 报告 cgroup 驱动，运行时须先于 kubelet 启动；对 cgroup v1 的支持继续退场。 |
| 调度与资源 | Pod 级别资源和 DRA 可分区设备预计进阶到稳定版；`LimitedSwap` 节点的交换内存限制改为按 Pod 级别内存设置计算。 |
| 新特性 | EvictionRequest API（Alpha）引入可协调的 Pod 驱逐，让应用有机会在被终止前完成清理。 |

## Kubernetes v1.38 的弃用项和移除项

### kubectl：用于关闭 WebSocket 的环境变量被移除

自 v1.30 起，`kubectl exec`、`attach` 和 `cp` 默认使用 WebSocket 而非 SPDY；
自 v1.31 起，`kubectl port-forward` 也是如此。
`KUBECTL_REMOTE_COMMAND_WEBSOCKETS` 和 `KUBECTL_PORT_FORWARD_WEBSOCKETS`
环境变量可以让你关闭这一行为。这些变量将在 v1.38 中被移除。
届时 `kubectl` 将始终优先尝试 WebSocket，并在需要时回退到 SPDY
（与当前的默认行为相同）。如果你的脚本或 CI 环境设置了这两个环境变量中的任意一个，
可以将其移除，因为它们将不再有任何作用。参阅
[KEP-4006：从 SPDY 过渡到 WebSocket](https://kubernetes.dev/resources/keps/4006)。

### kubectl：kuberc 凭证插件允许列表条目中的 `name` 字段被移除

`kuberc` 文件将 kubectl 用户偏好与 kubeconfig 中的集群凭证分开存放，
其中包括一份允许列表，用于指定 `kubectl` 可以运行哪些凭证插件。
在 Beta 阶段的 `kubectl.config.k8s.io/v1beta1` API 中，
允许列表条目可以使用 `name` 作为 `command` 的别名。
自 v1.36 起，`name` 字段（而非 `command`）已被弃用。

`kuberc` 预计将在 v1.38 中进阶到稳定版，新的 `kubectl.config.k8s.io/v1` API 将不再包含 `name`。
如果你的任何允许列表条目使用了 `name`，请立即改为 `command`。

参阅
[KEP-3104：将 kubectl 用户偏好与集群配置分开](https://kubernetes.dev/resources/keps/3104)。

## 持续进行中的重大变更

### 未来将移除对 cgroup v1 的支持

对 cgroup v1 的支持正被逐步淘汰。自 v1.35 起，
对于使用 cgroup v1 的节点，除非你在 kubelet 配置中设置 `failCgroupV1: false`，
否则 kubelet 将无法启动。此选项在 v1.38 中仍然可用，但应将其视为一种短期修复方案，
因为对 cgroup v1 的支持计划在未来的某个版本中被移除。
如果你尚未开始，请规划迁移到
[cgroup v2](https://kubernetes.io/zh-cn/docs/concepts/architecture/cgroups/)。
参阅 [KEP-5573：移除 cgroup v1 支持](https://kubernetes.dev/resources/keps/5573)。

### 准入 Webhook 不再接收身份验证和鉴权审查请求

自 v1.37 起，`ExcludeAdmissionWebhookVirtualResources` 特性门控已默认启用。
启用后，验证和变更准入 Webhook 不再接收对 TokenReview、SelfSubjectReview、
SubjectAccessReview、SelfSubjectAccessReview、LocalSubjectAccessReview
或 SelfSubjectRulesReview 的（虚拟）写入请求。
如果创建或更新 Webhook 配置时，其规则指定了这些资源之一，操作会返回一条弃用警告；
API 服务器在启动时也会记录受影响的现有配置。

如果你依赖某个 Webhook 来查看这些请求，可以暂时关闭该特性门控，
但请注意，当此特性进阶到稳定版时，该门控计划锁定为启用状态。参阅
[KEP-5793：基于清单的准入控制配置](https://kubernetes.dev/resources/keps/5793)。

## Kubernetes v1.38 中的破坏性变更

### 容器运行时必须报告 cgroup 驱动

v1.37 及更早的受支持版本中的 kubelet 提供了一种用于配置 cgroup 驱动的传统机制。
现代的做法是通过 CRI `RuntimeConfig` RPC，由容器运行时报告其建议使用的 cgroup 驱动。
在 v1.38 中，kubelet 默认不再允许使用这种传统的配置机制：
除非显式重新启用，否则该机制既被弃用又不可用。
因此，v1.38 节点实际上要求你的容器运行时在 kubelet 启动 **之前** 就已运行
（以便查询预期的 cgroup 驱动）；如果 kubelet 即使重试后仍无法从运行时获取 cgroup 驱动，
它将在注册节点之前就以错误状态退出。

作为本次即将发布的版本的一部分，kubelet 配置文件中的 `cgroupDriver` 字段将被弃用。
不仅指定该字段会被弃用，而且除非你通过启用（临时的）`LegacyCgroupDriverFallback`
特性门控重新激活传统机制，否则 kubelet 实际上会拒绝该字段。
kubeadm 工具也不再默认将 `cgroupDriver` 设置为 `systemd`；
如果运行时不支持该 RPC，kubeadm 的预检将报告错误。
如果你的任何节点运行的是较旧的、不兼容的容器运行时，
请遵照 v1.38 官方发布说明中关于如何升级的指示操作。参阅
[KEP-4033：从 CRI 发现 cgroup 驱动](https://kubernetes.dev/resources/keps/4033)和
[kubernetes/kubernetes#136731](https://github.com/kubernetes/kubernetes/pull/136731)。

### Pod 级别资源：`LimitedSwap` 节点上的交换行为发生变化   {#pod-level-resources-swap}

如果你在使用 cgroup v2 且配置了 `LimitedSwap` 的 Linux 节点上使用 Pod 级别资源，
那么 v1.38 中的 kubelet 将开始根据 Pod 的 Pod 级别内存设置来施加交换内存限制。
这意味着，Pod 级别内存请求等于其内存限制的 Pod
将完全得不到交换内存（无论对 Pod 本身还是对其中的每个容器都是如此），
即使某个容器将其内存请求设置得低于其限制。
升级之前，请检查所有依赖交换内存的工作负载，
并务必阅读 v1.38 的官方发布说明以获取详细建议。参阅
[KEP-2837：Pod 级别资源规约](https://kubernetes.dev/resources/keps/2837)。

## Kubernetes v1.38 的重点增强项

以下增强特性列表很可能会包含在即将发布的 v1.38 版本中。
这不是一种承诺，发布内容可能会发生变化。

### kubectl 用户偏好设置（kuberc）进阶到稳定版

kuberc 是一个独立的 kubectl 配置文件，用于存放别名、默认选项和凭证插件策略等用户偏好设置，
预计将在 v1.38 中进阶到稳定版。参阅
[kubectl 用户偏好设置（kuberc）](https://kubernetes.io/zh-cn/docs/reference/kubectl/kuberc/)或参阅
[KEP-3104：将 kubectl 用户偏好与集群配置分开](https://kubernetes.dev/resources/keps/3104)。

### Pod 级别资源进阶到稳定版

Pod 级别资源允许你为整个 Pod 设置 CPU、内存和巨页的请求与限制，
预计将在 v1.38 中进阶到稳定版。
如果你运行的是配置了 `LimitedSwap` 的 Linux 节点，
请在升级前参阅上文的[交换行为变更](#pod-level-resources-swap)。参阅
[分配 Pod 级别 CPU 和内存资源](https://kubernetes.io/zh-cn/docs/tasks/configure-pod-container/assign-pod-level-resources/)，
或参阅 [KEP-2837：Pod 级别资源规约](https://kubernetes.dev/resources/keps/2837)。

### DRA 对可分区设备的支持进阶到稳定版

可分区设备允许
[动态资源分配](https://kubernetes.io/zh-cn/docs/concepts/resource-management/dynamic-resource-allocation/)（DRA）
驱动将 GPU 等设备既作为整体、也作为更小的分区来公布，调度器只会分配能容纳于该物理设备之内的组合。
此特性预计将在 v1.38 中进阶到稳定版，届时 `DRAPartitionableDevices` 特性门控将被锁定为启用状态。
参阅[可分区设备](https://kubernetes.io/zh-cn/docs/concepts/resource-management/dynamic-resource-allocation/dra-features/#partitionable-devices)，
或参阅 [KEP-4815：DRA：增加对可分区设备的支持](https://kubernetes.dev/resources/keps/4815)。

### EvictionRequest API（Alpha）

驱逐 Pod 并不总是像终止它那么简单。有些应用可能正在进行重要的工作，
例如数据迁移或清理，如果不给它们留出准备时间就终止，可能会造成中断。

EvictionRequest API 引入了一种更协调的 Pod 驱逐方式，
它在 Pod 被驱逐之前给应用和控制器留出准备时间。
例如，当需要排空某个节点或将某个 Pod 迁移到另一个节点时，
控制器可以创建一个 EvictionRequest，以表明该 Pod 需要被驱逐。

驱逐请求控制器会与为 Pod 配置的响应方协调。
这些响应方可以在 Pod 被终止之前执行特定于应用的任务，
例如完成正在进行的工作、清理资源或迁移数据。

如果没有可用的自定义响应方，或者响应方未能完成该过程，
Kubernetes 可以回退到现有的 API 发起的驱逐机制，该机制仍然遵循
PodDisruptionBudget（PDB）。EvictionRequest API 并不取代 PDB，
它为应用提供了参与驱逐过程的机会。

由于这是 Alpha 特性，你需要启用 `EvictionRequestAPI` 特性门控 **以及** 相关的 Alpha API 组。
待 v1.38 的发布说明和文档可用后，请查看它们以确认具体要求。参阅
[KEP-4563：EvictionRequest API](https://kubernetes.dev/resources/keps/4563)。

## DaoCloud 与 Kubernetes 社区：参与治理、技术与传播

Kubernetes 的持续演进，离不开全球贡献者在治理、技术实现和社区传播等多个层面的长期投入。
DaoCloud 团队也持续参与其中：

- **[Paco Xu](https://github.com/pacoxu)** 作为 Kubernetes Steering Committee 委员
  （2023 年当选、2025 年连任至 2027），参与项目治理与社区领导工作，
  同时担任 CNCF TAG Workloads Foundation Chair 和 CNCF Ambassador。
- **[Baofa Fan](https://github.com/carlory)** 持续投入 Kubernetes 技术特性与工程实践，
  为社区的技术演进贡献专业经验。
- **[Wei Cai](https://github.com/iceber)** 和 **[Michael Yao](https://github.com/windsonsea)**
  均为 CNCF Ambassador，连接开发者、用户与社区贡献者。
  多次组织 KCD 等社区活动，担任 KubeCon Program Committee 成员，
  评审 Kubernetes 生态项目的各类 PR 和 Issue，持续参与社区建设工作。
- **[Weizhou Lan](https://github.com/weizhoublue)** 和 **[yankay](https://github.com/yankay)**
  分别聚焦网络与调度方向，多次以 Speaker 身份登上 KubeCon 舞台，
  分享云原生基础设施领域的实践与思考。
- DaoCloud 还有十多位 Maintainer 分布在 Kubernetes 各个 SIG 小组参与核心代码贡献，
  并累计 6 人次获得 Kubernetes 年度贡献者奖。

按 CNCF DevStats 的统计口径，DaoCloud 在 Kubernetes 核心代码贡献量 **稳居全球前三、中国第一** ；
在 `kubernetes/kubernetes` 主仓的全球贡献者百强中，DaoCloud 工程师占据多个席位。
此外，DaoCloud 还深度参与 HAMi、Kueue、llm-d 等 AI 算力调度与推理项目，
帮助更多企业将社区的新能力转化为稳定、可落地的生产实践。

作为早在 2017 年就通过 CNCF 官方认证的 Kubernetes Certified Service Provider（KCSP），
DaoCloud 的认证资质与新版本适配情况，参阅
[DaoCloud 是 Kubernetes 及 AI Platform 认证服务商](../../dce/kcsp.md)。

## 了解更多？

新特性和弃用项也会在 Kubernetes 发布说明中公布。
我们将作为该版本 CHANGELOG 的一部分，正式公布
[Kubernetes v1.38](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.38.md) 中的新内容。

Kubernetes v1.38 版本计划于 **2026 年 12 月 16 日（星期三）** 发布。敬请关注更新！

你可以在以下版本的发布说明中查看其他变更公告：

- [Kubernetes v1.37](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.37.md)
- [Kubernetes v1.36](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md)
- [Kubernetes v1.35](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md)
