# Kubernetes 1.27：加快了 Pod 启动速度

**投稿**：[Paco Xu](https://github.com/pacoxu)、[Michael Yao](https://github.com/windsonsea)

如何在大型集群中加快节点上的 Pod 启动？这是企业中集群管理员常常会面临的问题。

这篇博文重点介绍了从 kubelet 一侧加快 Pod 启动的方法。此方法不涉及通过
kube-apiserver 由 controller-manager 创建 Pod 所用的时间段，
也不包含 Pod 的调度时间或在其上执行 Webhook 的时间。

本文从 kubelet 的角度考虑，提及了一些重要的影响因素，但并不会详尽罗列所有诱因。

Kubernetes v1.27 已正式发布，本文也强调了 v1.27 中有助于加快 Pod 启动的一些主要变更。

## 并行容器镜像拉取

拉取镜像总是需要一些时间的，更糟的是镜像拉取默认是以串行方式作业的。
换言之，kubelet 一次只会向镜像服务发送一个镜像拉取请求。
其他的镜像拉取请求必须等到正在处理的拉取请求被完成才能进行。

要启用并行镜像拉取，请在 kubelet 配置中将 `serializeImagePulls` 字段设置为 false。
当 `serializeImagePulls` 被禁用时，将立即向镜像服务发送镜像拉取请求，并可以并行拉取多个镜像。

### 设定并行镜像拉取最大值有助于防止节点因镜像拉取而过载

我们在 kubelet 中引入了一个新特性，可以在节点级别设置并行镜像拉取的限值。
此限值限制了可以同时拉取的最大镜像数量。如果有个镜像拉取请求超过了这个限值，
该请求将被阻止，直到其中一个正在进行的镜像拉取完成为止。
在启用此特性之前，请确保容器运行时的镜像服务可以有效处理并行镜像拉取。

要限制并行镜像拉取的数量，你可以在 kubelet 中配置 `maxParallelImagePulls` 字段。
将 `maxParallelImagePulls` 的值设置为 **n** 后，并行拉取的镜像数将不能超过 **n** 个。
超过此限值的任何其他镜像拉取请求都需要等到至少一个正在进行的拉取被完成为止。

你可以在关联的 KEP 中找到更多细节：
[Kubelet 并行镜像拉取数限值](https://kep.k8s.io/3673) (KEP-3673)。

## 提高了 kubelet 默认 API 每秒查询限值

为了在节点上具有多个 Pod 的场景中加快 Pod 启动，特别是在突然扩缩的情况下，
kubelet 需要同步 Pod 状态并准备 ConfigMap、Secret 或卷。这就需要大带宽访问 kube-apiserver。

在 v1.27 之前的版本中，`kubeAPIQPS` 的默认值为 5，`kubeAPIBurst` 的默认值为 10。
然而在 v1.27 中，kubelet 为了提高 Pod 启动性能，将这些默认值分别提高到了 50 和 100。
值得注意的是，提高 kubelet 的 API QPS 限值并不是唯一的原因。

1. 现在它有可能会被大幅限制（默认 QPS = 5）
2. 在大型集群中，它们仍然可能产生相当大的负载，因为数量很多
3. 有一个专用的 PriorityLevel 和 FlowSchema，这点我们可以轻松控制

以前在具有 50 个以上 Pod 的节点中，我们经常在 Pod 启动期间在 kubelet 上遇到 `volume mount timeout`。
特别是在使用裸金属节点时，我们建议集群操作员将 `kubeAPIQPS` 提高到 20，`kubeAPIBurst` 提高到 40。

更多细节请参阅 KEP <https://kep.k8s.io/1040> 和
[PR#116121](https://github.com/kubernetes/kubernetes/pull/116121)。

## 事件驱动的容器状态更新

在 v1.27 中，`Evented PLEG`
（PLEG 是英文 Pod Lifecycle Event Generator 的缩写，表示 “Pod 生命周期事件生成器”）
进阶至 Beta 阶段。Kubernetes 为 kubelet 提供了两种方法来检测 Pod 的生命周期事件，
例如容器中最后一个进程关闭。在 Kubernetes v1.27 中，**基于事件的** 机制已进阶至 Beta，
但默认被禁用。如果你显式切换为基于事件的生命周期变更检测，则 kubelet
能够比依赖轮询的默认方法更快地启动 Pod。默认的轮询生命周期更改机制会增加明显的开销，
这会影响 kubelet 处理不同任务的并行能力，并导致性能和可靠性问题。
出于这些原因，我们建议你将节点切换为使用基于事件的 Pod 生命周期变更检测。

更多细节请参阅 KEP <https://kep.k8s.io/3386>
和[容器状态从轮询切换为基于 CRI 事件更新](https://kubernetes.io/docs/tasks/administer-cluster/switch-to-evented-pleg/)。

## 必要时提高 Pod 资源限值

在启动时，某些 Pod 可能会消耗大量的 CPU 或内存。
如果 CPU 限值较低，则可能会显著降低 Pod 启动过程的速度。
为了改善内存管理，Kubernetes v1.22 引入了一个名为 MemoryQoS 的特性门控。
该特性使 kubelet 能够在容器、Pod 和 QoS 级别上设置内存 QoS，以便更好地保护和确保内存质量。
尽管此特性门控有所好处，但如果 Pod 启动消耗大量内存，启用此特性门控可能会影响 Pod 的启动速度。

Kubelet 配置现在包括 `memoryThrottlingFactor`。该因子乘以内存限制或节点可分配内存，
可以设置 cgroupv2 memory.high 值来执行 MemoryQoS。
减小该因子将为容器 cgroup 设置较低的上限，同时增加了回收压力。
提高此因子将减少回收压力。默认值最初为 0.8，并将在 Kubernetes v1.27 中更改为 0.9。
调整此参数可以减少此特性对 Pod 启动速度的潜在影响。

更多细节请参阅 KEP <https://kep.k8s.io/2570>。

## 更多说明

在 Kubernetes v1.26 中，新增了一个名为 `pod_start_sli_duration_seconds` 的直方图指标，
用于显示 Pod 启动延迟 SLI/SLO 详情。此外，kubelet 日志现在会展示更多与 Pod 启动相关的时间戳信息，如下所示：

```
Dec 30 15:33:13.375379 e2e-022435249c-674b9-minion-group-gdj4 kubelet[8362]: I1230 15:33:13.375359    8362
pod_startup_latency_tracker.go:102] "Observed pod startup duration" pod="kube-system/konnectivity-agent-gnc9k"
podStartSLOduration=-9.223372029479458e+09 pod.CreationTimestamp="2022-12-30 15:33:06 +0000 UTC"
firstStartedPulling="2022-12-30 15:33:09.258791695 +0000 UTC m=+13.029631711"
lastFinishedPulling="0001-01-01 00:00:00 +0000 UTC"
observedRunningTime="2022-12-30 15:33:13.375009262 +0000 UTC m=+17.145849275"
watchObservedRunningTime="2022-12-30 15:33:13.375317944 +0000 UTC m=+17.146157970"
```

SELinux 挂载选项重标记功能在 v1.27 中升至 Beta 版本。
该特性通过挂载具有正确 SELinux 标签的卷来加快容器启动速度，
而不是递归地更改卷上的每个文件。更多细节请参阅 KEP <https://kep.k8s.io/1710>。

为了确定 Pod 启动缓慢的原因，分析指标和日志可能会有所帮助。
其他可能会影响 Pod 启动的因素包括容器运行时、磁盘速度、节点上的 CPU 和内存资源。

SIG Node 负责确保快速的 Pod 启动时间，而解决大型集群中的问题则属于 SIG Scalability 的范畴。
