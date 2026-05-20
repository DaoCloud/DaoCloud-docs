# Kubernetes v1.36：服务端分片 List 与 Watch

> 原英文博客位于 [k8s.io](https://kubernetes.io/blog/2026/05/06/kubernetes-v1-36-server-side-sharded-list-and-watch/)

随着 Kubernetes 集群规模增长到数万个节点，监视（watch）像 Pod 这样高基数资源的控制器会遇到扩展瓶颈。
每个水平扩展后的控制器副本都会从 API 服务器接收完整的事件流，并为反序列化所有对象付出 CPU、内存和网络开销，
最终却丢弃掉那些不属于自身负责范围的对象。扩展控制器副本数量并不会降低单个副本的成本；反而会将成本成倍放大。

Kubernetes v1.36 引入了 **服务端分片 List 与 Watch** 这一 Alpha 特性
（[KEP-5866](https://github.com/kubernetes/enhancements/issues/5866)）。
启用此特性后，API 服务器在源头过滤事件，使每个控制器副本只接收到其负责的那部分资源集合。

## 使用客户端分片的问题

诸如 [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics)
这些控制器已经支持水平分片。每个副本会被分配一部分键空间，并丢弃不属于自己的对象。
虽然这种方式在功能上可行，但并不能减少从 API 服务器流出的数据量：

- **N 个副本 × 完整事件流** ：每个副本都会反序列化并处理所有事件，然后丢弃自己不需要的部分。
- **网络带宽消耗会随着副本数量扩缩容** ，而不是随着分片大小扩缩容。
- **用于反序列化的 CPU 开销** 会浪费在最终被丢弃的数据上。

服务端分片 List 与 Watch 通过将过滤逻辑前移到 API 服务器来解决这个问题。
每个副本告诉 API 服务器自己负责的哈希范围，而 API 服务器只发送匹配的事件。

## 工作原理

此特性为 `ListOptions` 新增了一个 `shardSelector` 字段。客户端通过 `shardRange()` 函数指定一个哈希范围：

```
shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')
```

API 服务器基于指定字段计算一个确定性的 64 位
[FNV-1a](https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function)
哈希值，并仅返回哈希值落在 `[start, end)` 范围内的对象。此机制同时适用于 List 响应和 Watch 事件流。
由于此哈希函数在所有 API 服务器实例上都会生成相同的结果，因此该特性可以安全地用于多个 API 服务器副本的场景。

目前支持的字段路径包括 `object.metadata.uid` 和 `object.metadata.namespace`。

## 在控制器中使用分片 Watch

控制器通常使用 Informer 对资源执行 List 和 Watch。
为了对工作负载进行分片，每个副本会通过 `WithTweakListOptions` 向
Informer 使用的 `ListOptions` 注入 `shardSelector`：

```go
import (
    metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
    "k8s.io/client-go/informers"
)

shardSelector := "shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')"

factory := informers.NewSharedInformerFactoryWithOptions(client, resyncPeriod,
    informers.WithTweakListOptions(func(opts *metav1.ListOptions) {
        opts.ShardSelector = shardSelector
    }),
)
```

对于包含 2 个副本的 Deployment，选择算符将哈希空间平均分成两半：

```go
// 副本 0：哈希空间的下半部分
"shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')"

// 副本 1：哈希空间的上半部分
"shardRange(object.metadata.uid, '0x8000000000000000', '0x10000000000000000')"
```

单个副本也可以使用 `||` 来涵盖多个不连续的范围：

```go
"shardRange(object.metadata.uid, '0x0000000000000000', '0x4000000000000000') || " +
    "shardRange(object.metadata.uid, '0x8000000000000000', '0xc000000000000000')"
```

## 验证服务端支持情况

当 API 服务器正确处理分片选择算符时，List 响应在响应元数据中包含一个 `shardInfo` 字段，用于回显实际应用的选择算符：

```json
{
  "kind": "PodList",
  "apiVersion": "v1",
  "metadata": {
    "resourceVersion": "10245",
    "shardInfo": {
      "selector": "shardRange(object.metadata.uid, '0x0000000000000000', '0x8000000000000000')"
    }
  },
  "items": [...]
}
```

如果 `shardInfo` 不存在，则表示服务端没有处理该分片选择算符，客户端接收到的是完整、未过滤的资源集合。
在这种情况下，客户端应能够处理完整结果集，例如通过客户端侧过滤来丢弃不属于其分片范围的对象。

## 参与其中

此特性目前处于 Alpha 阶段，需要在 API 服务器上启用 `ShardedListAndWatch` 特性门控。
我们正在征集来自控制器开发者以及运行大规模集群的运维人员的反馈。

- [KEP-5866：服务端分片 List 与 Watch](https://github.com/kubernetes/enhancements/issues/5866)
- [API 概念：分片 List 与 Watch](https://kubernetes.io/docs/reference/using-api/api-concepts/#sharded-list-and-watch)
- [SIG API Machinery](https://github.com/kubernetes/community/tree/master/sig-api-machinery)

如果你有问题或反馈，欢迎加入 [Kubernetes Slack](https://slack.k8s.io/)
中的 `#sig-api-machinery` 频道。
