# Kubernetes v1.37 抢先看：迁移准备、安全与资源管理

Kubernetes v1.37 正在收敛为一次兼顾 **迁移准备、运行时安全和资源管理** 的版本更新：
`kube-proxy` 的 ipvs 模式进入弃用周期，CGroup v1 的退出需要尽早规划，
SELinux 卷标签机制也将带来需要提前验证的行为变化。
与此同时，Metrics API、Rootless kubelet 和卷健康监控等能力持续成熟，
为可观测性和更安全的节点运行时打下基础。

本文梳理了值得平台团队和集群运维人员优先关注的 v1.37 计划内变更。
以下内容反映的是当前发布周期的状态，实际发布日期前仍可能调整。

> 如果你的集群仍在使用 ipvs 或 CGroup v1，应将迁移纳入近期计划；
> 如果工作负载启用了 SELinux 并共享存储卷，应在升级前完成兼容性验证。

## 一分钟了解 v1.37

- **网络**：`kube-proxy` 的 ipvs 模式开始弃用，预计 v1.40 默认禁用、v1.43 完全移除；应尽早评估替代模式。
- **节点运行时**：CGroup v1 已进入退出阶段；Rootless kubelet 预计升级到 Beta，为降低主机级 root 权限依赖提供新的选择。
- **存储与安全**：SELinuxMount 预计默认启用。使用不同 SELinux 标签共享同一卷的 Pod 需要重点回归测试；卷健康监控则重新以 Alpha 形态推进。
- **可观测性**：`metrics.k8s.io` API 预计结束近九年的 Beta 阶段，升级为稳定版（GA）。

## Kubernetes v1.37 的弃用和移除

### kubectl：`kubectl run --filename/-f` 将被弃用

`kubectl run` 的 `--filename`（或 `-f`）参数将被弃用，
因为生成的 Pod 始终纯粹由 `NAME` 和 `--image` 等 CLI 参数构建。

原始 Issue 和讨论请参见
[kubernetes/kubernetes#138671](https://github.com/kubernetes/kubernetes/issues/138671)。

### kubelet：静态 Pod 不再能引用 Secret 或 ConfigMap

静态 Pod 从未打算直接读取 API 资源，因为它们不是通过 API 服务器创建的 ——
但一个缺陷曾允许它们通过 `configMapRef` 或 `secretRef` 等字段引用 Secret 或 ConfigMap。
该缺陷现已修复：从 v1.37 起，这些引用被严格禁止，
并且先前用于绕过此限制的 `PreventStaticPodAPIReferences` 特性门控已被移除。

原始 Issue 和讨论请参见
[kubernetes/kubernetes#140226](https://github.com/kubernetes/kubernetes/issues/140226)。

### 弃用 kube-proxy 对 `ipvs` 模式的支持

`kube-proxy` 对 `ipvs` 模式的支持是在 v1.8 中引入的，旨在解决 `iptables` 性能瓶颈。
然而，由于内核 `ipvs` API 单独无法完全实现 Kubernetes Service，
`ipvs` 模式在底层仍继续使用 `iptables`
（[KEP-3866，“kube-proxy 的 ipvs 模式救不了我们”](https://github.com/kubernetes/enhancements/blob/master/keps/sig-network/3866-nftables-proxy/README.md#the-ipvs-mode-of-kube-proxy-will-not-save-us)）。

在 ipvs 模式下（或在 KubeProxyConfiguration 中设置 `mode: ipvs`）运行 `kube-proxy` 的集群，
现在会在启动时记录一条弃用警告。弃用时间表如下：

- 到 v1.40，`kube-proxy` 的 `ipvs` 模式预计将默认禁用（仍可通过特性门控选择）
- 到 v1.43，对 `ipvs` 模式的支持将被完全移除
  [KEP-5495，毕业标准](https://github.com/kubernetes/enhancements/blob/master/keps/sig-network/5495-deprecate-ipvs-mode-in-kube-proxy/README.md#graduation-criteria)。

要确认你当前运行的是哪种模式，请使用：

```bash
kubectl -n kube-system get configmap kube-proxy -o jsonpath='{.data.config\.conf}' | grep 'mode:'
```

要了解此次弃用背后的基本原理，请参见
[KEP-5495：弃用 kube-proxy 中的 ipvs 模式](https://kubernetes.dev/resources/keps/5495)。

## 持续进行中的重大变更：未来将移除对 CGroup v1 的支持

随着现代 Linux 发行版和容器运行时使用
[CGroup v2](https://kubernetes.io/zh-cn/docs/concepts/architecture/cgroups/) 作为默认值，
对旧版 CGroup v1 的支持正被正式逐步淘汰。
自 v1.35 版本起，`failCgroupV1` 设置默认为 true。
因此，`kubelet` 将在任何仍依赖 CGroup v1 的节点上初始化失败，
除非应用显式的配置覆写。

```yaml
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
failCgroupV1: false # 临时覆写
```

使用此覆写应被视为一种短期修复。
高级资源管理能力，例如就地 Pod 调整大小（In-Place Pod Resizing）和
分层内存保护（Tiered Memory Protection），完全依赖于 CGroup v2。
虽然该覆写在 Kubernetes v1.37 中仍然可用，但鼓励用户迁移到 CGroup v2，
因为对 CGroup v1 的支持计划在未来的某个版本中被移除。

要了解有关此弃用的更多信息，请参阅
[KEP-5573：移除 CGroup v1 支持](https://kubernetes.dev/resources/keps/5573)。

## Kubernetes v1.37 中的破坏性变更

### SELinux 卷重新标记（"SELinuxMount"）进入 GA  {#SELinuxMount-GA}

SELinuxMount 预计将在 v1.37 中达到 GA 并默认启用。
届时卷将使用 `-o context=<label>`（挂载选项默认值）挂载，
而不是被递归地重新标记，但**仅当**卷的 CSI 驱动通过设置
`.spec.seLinuxMount: true` 的 CSIDriver 选择加入时才如此。

由于单个挂载只能持有一个 SELinux 上下文，
在同一节点上共享一个卷、具有不同 SELinux 标签的 Pod
（先前在递归重新标记下可以共存）现在可能无法启动。
要为特定工作负载保留先前的递归行为，请在 Pod 规约中设置
`seLinuxChangePolicy: Recursive`。

未启用 SELinux 的集群完全不受影响。
要了解更多信息，请查看
[SELinux 卷标签变更进入 GA 阶段（以及 v1.37 中可能的影响）](https://kubernetes.io/zh-cn/blog/2026/04/22/breaking-changes-in-selinux-volume-labeling/)

## Kubernetes v1.37 的重点增强

### Metrics API 进入 GA

`metrics.k8s.io` API 在 Beta 阶段停留近九年后，
预计将在 Kubernetes v1.37 中毕业至稳定版（GA）。
该 API 提供了一种标准方式来检索 Pod 和节点的 CPU 和内存使用情况，
为广泛使用的 Kubernetes 特性（例如水平 Pod 自动扩缩器（HPA））
以及 `kubectl top` 等命令提供支持。

此次毕业认可了该 API 的稳定性和广泛采用，预计不会有功能性变更。
在过渡期间，`v1` 和 `v1beta1` 都将继续可用，
使开发者能够按自己的节奏采用稳定版 API，而不会破坏现有工作流。

要了解有关此增强的更多信息，请参阅
[KEP-5207：metrics.k8s.io API 定义](https://www.kubernetes.dev/resources/keps/5207/)。

### UserNS 中的 kubelet，即 Rootless 模式

传统上，Kubernetes 节点组件（例如 `kubelet`）在主机上以 root 特权运行。
虽然这对许多部署是必要的，但这也意味着这些组件中某个组件的漏洞可能会对底层系统产生更大的影响。

在 Kubernetes v1.37 中，用户命名空间中的 kubelet
（即 Rootless 模式）预计将毕业至 Beta。
此增强允许 Kubernetes 节点组件在 Linux 用户命名空间内以主机上的非特权用户身份运行，
同时在命名空间内仍表现为 root。
通过减少对主机级 root 特权的需求，它增加了一层额外的隔离，
并有助于限制影响节点组件的潜在漏洞的影响范围。

要了解有关此增强的更多信息，请参阅
[KEP-2033：UserNS 中的 Kubelet（即 Rootless 模式）](https://kubernetes.dev/resources/keps/4960)。

### 卷健康监控

历史上，Kubernetes 一直缺乏一个供 CSI 驱动报告存储故障的 API，
这些故障仅通过挂载失败或 I/O 挂起才变得明显。
由于修复控制器没有机器可读的内容可供处理，
找出此类故障背后根本原因的唯一方法是将 Kubernetes
对象与外部供应商仪表板进行交叉比对。

在 Kubernetes v1.37 中，此 KEP 在 v1.21 初步实现后将毕业状态重置为 Alpha，
并引入了四个新的 CSI RPC。控制器插件使用
`ControllerListVolumeHealth`（列出不健康的卷）和
`ControllerGetVolumeHealth`（检查特定卷）来报告存储卷的健康状况。
控制器侧的健康监控器轮询这些 CSI 控制器，并将结果存储在
`PersistentVolumeClaim.status.healthStatus` 中。

在节点侧，kubelet 调用 `NodeGetVolumeHealth` 来获取该节点上各个卷的健康状况，
并将其记录在 `Pod.status.volumeHealth` 中；
而 `NodeGetStorageHealth` 将注册到节点的驱动的健康状况报告在
`CSINode.status.storageHealth` 中。

错误词汇表保持简单、可扩展且机器可解析（`Inaccessible`、`Degraded` 等），
并可通过 `reason` 和 `message` 提供更多特定于驱动的详细说明。
最后，控制器侧和节点侧的报告保持独立，因此分开显示，
从而为使用者提供更全面的存储健康状况视图。

要了解有关此增强的更多信息，请参阅
[KEP-1432：卷健康监控](https://kubernetes.dev/resources/keps/1432)。

## DaoCloud 与 Kubernetes 社区：参与治理、技术与传播

Kubernetes 的持续演进，离不开全球贡献者在治理、技术实现和社区传播等多个层面的长期投入。
DaoCloud 团队也持续参与其中：

- **[Paco Xu](https://github.com/pacoxu)** 作为 Kubernetes Steering Committee 委员，参与项目治理与社区领导工作，推动社区的开放协作和可持续发展。
- **[Baofa Fan](https://github.com/carlory)** 持续投入 Kubernetes 技术特性与工程实践，为社区的技术演进贡献专业经验。
- **[Wei Cai](https://github.com/iceber)** 作为 CNCF Ambassador，多次组织 KCD（Kubernetes Community Days）活动，连接开发者、用户与社区贡献者。
- **[Weizhou Lan](https://github.com/weizhoublue)** 和 **[yankay](https://github.com/yankay)** 分别聚焦网络与调度方向，多次以 Speaker 身份登上 KubeCon 舞台，分享云原生基础设施领域的实践与思考。
- DaoCloud 还有十多位 Maintainer 分布在 Kubernetes 各个 SIG 小组参与核心代码贡献。

从版本特性讨论到线下技术交流，DaoCloud 希望与更多开发者一起，将社区的新能力转化为稳定、可落地的生产实践。

## 了解更多？

新特性和弃用也会在 Kubernetes 发布说明中公布。
我们将作为该版本 CHANGELOG 的一部分，正式公布
[Kubernetes v1.37](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.37.md) 中的新内容。

Kubernetes v1.37 版本计划于 **2026 年 8 月 26 日（星期三）** 发布。敬请关注更新！

你可以在以下版本的发布说明中查看变更公告：

* [Kubernetes v1.36](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md)
* [Kubernetes v1.35](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md)
* [Kubernetes v1.34](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md)
* [Kubernetes v1.33](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.33.md)
