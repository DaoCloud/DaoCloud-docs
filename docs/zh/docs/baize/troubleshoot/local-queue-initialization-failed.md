# 本地队列初始化失败

## 问题现象

在创建 Notebook、训练任务或者推理服务时，当队列是首次在该命名空间使用时，会提示需要一键初始化队列，但是初始化失败。

![local-queue-initialization-failed](./images/kueue-init-localqueue.png)

## 问题分析

在智能算力中，队列管理能力由 `Kueue` 提供，而 Kueue 提供了 两种队列管理资源，一种是 `ClusterQueue`，一种是 `LocalQueue`。

- ClusterQueue 是集群级别的队列，主要用于管理队列中的资源配额，包含了 CPU、内存、GPU 等资源。
- LocalQueue 是命名空间级别的队列，需要指向到一个 ClusterQueue，用于使用队列中的资源分配。

在智能算力中，如果创建服务时，发现指定的 `Namespace` 不存在 `LocalQueue`，则会提示需要初始化队列。

在极少数情况下，可能由于特殊原因会导致 `LocalQueue` 初始化失败。

### 解决方案

检查 `Kueue` 是否正常运行，如果 `kueue-controller-manager` 未运行，可以通过以下命令查看。

```bash
kubectl get deploy kueue-controller-manager -n baize-sysatem 
```

如果 `kueue-controller-manager` 未正常运行，请先修复 `Kueue`。

### 相关信息

- [ClusterQueue](https://kueue.sigs.k8s.io/docs/concepts/cluster_queue/)
- [LocalQueue](https://kueue.sigs.k8s.io/docs/concepts/local_queue/)
