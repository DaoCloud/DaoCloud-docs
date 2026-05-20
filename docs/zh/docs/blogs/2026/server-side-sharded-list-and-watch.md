# Kubernetes v1.36：服务端分片 List 与 Watch

> 原英文博客位于 [k8s.io](https://kubernetes.io/blog/2026/05/06/kubernetes-v1-36-server-side-sharded-list-and-watch/)

随着 Kubernetes 集群规模增长到数万个节点，监视（watch）像 Pod 这样高基数资源的控制器会遇到扩容瓶颈。
每个横向扩容后的控制器副本都会从 API 服务器接收完整的事件流，并为反序列化所有对象付出 CPU、内存和网络开销，
最终却丢弃掉那些不属于自身负责范围的对象。扩容控制器副本数量并不会降低单个副本的成本；反而会将成本成倍放大。

Kubernetes v1.36 引入了 **服务端分片 List 与 Watch** 这一 Alpha 特性
（[KEP-5866](https://github.com/kubernetes/enhancements/issues/5866)）。
启用此特性后，API 服务器在源头过滤事件，使每个控制器副本只接收到其负责的那部分资源集合。

这个 Alpha 新特性能够解决超大规模集群中控制器横向扩容后带来的巨大资源浪费问题。

- 以前：每个控制器副本都要接收“全量对象列表 + 全量事件流”，再自己过滤。
- 现在：API 服务器直接帮你按分片过滤，只下发属于这个副本的数据。

## 以前使用客户端分片的问题

诸如 [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics)
这些控制器已经支持水平分片。每个副本会被分配一部分键空间，并丢弃不属于自己的对象。
虽然这种方式在功能上可行，但并不能减少从 API 服务器流出的数据量：

- **N 个副本 × 完整事件流** ：每个副本都会反序列化并处理所有事件，然后丢弃自己不需要的部分。
- **网络带宽消耗会随着副本数量扩缩容** ，而不是随着分片大小扩缩容。
- **用于反序列化的 CPU 开销** 会浪费在最终被丢弃的数据上。

服务端分片 List 与 Watch 通过将过滤逻辑前移到 API 服务器来解决这个问题。
每个副本告诉 API 服务器自己负责的哈希范围，而 API 服务器只发送匹配的事件。

## 服务端分片的工作原理

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

## 性能和消耗对比

传统 List/Watch 与服务端分片 List/Watch 对比：

| 对比项 | 传统 List/Watch | 服务端分片 List/Watch |
|---|---|---|
| 数据获取方式 | 所有控制器获取全量数据 | 每个控制器只获取自己的分片 |
| List 行为 | 返回全集群所有对象 | 仅返回分片内对象 |
| Watch 行为 | 接收所有对象事件 | 仅接收分片内事件 |
| 数据过滤位置 | 客户端过滤 | API 服务器服务端过滤 |
| 网络流量 | `副本数 × 全量流量` | 接近“总量不变，仅切分” |
| API 服务器 fan-out | 每个事件广播给所有副本 | 仅发送给相关分片 |
| Informer 缓存 | 每个副本缓存全部对象 | 每个副本仅缓存部分对象 |
| 内存占用 | 很高，随副本数线性增长 | 明显降低 |
| CPU 消耗 | 大量 JSON 解码 + 丢弃 | 仅处理需要的数据 |
| etcd Watch 压力 | Watch 数据流数量巨大 | 显著减少 |
| 控制器横向扩容 | 扩容越多浪费越严重 | 可真正横向扩容 |
| 客户端复杂度 | 需要自行过滤 | 基本无需客户端过滤 |
| 超大规模集群适应性 | 较差 | 专为百万级对象设计 |
| 典型问题 | “收到再扔掉” | “不属于你的根本不发” |
| Kubernetes v1.36 新能力 | ❌ | ✅ `ShardedListAndWatch` |

资源消耗对比：

| 资源 | 传统模式 | 服务端分片 |
|---|---|---|
| 网络 | 🔴 非常高 | 🟢 大幅降低 |
| 控制器 CPU | 🔴 很高 | 🟢 更低 |
| 控制器内存 | 🔴 全量缓存 | 🟢 分片缓存 |
| API 服务器压力 | 🔴 fan-out 巨大 | 🟢 显著下降 |
| etcd 压力 | 🔴 大量 watch | 🟢 更可控 |
| 集群扩容能力 | 🔴 容易瓶颈 | 🟢 更容易扩容 |
