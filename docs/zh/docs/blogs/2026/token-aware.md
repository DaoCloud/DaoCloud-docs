# 从 KV Cache Affinity 到 Token-aware Routing：llm-d 如何避免 LLM 推理热点

> 素材为 llm-d.ai 原英文博客：[Sticky Until Saturated: Token-Aware Routing in llm-d](https://llm-d.ai/blog/sticky-until-saturated-token-aware-routing)

阅读之前，先了解几个概念：

- **KV Cache**：推理时预先算好的 Key/Value 中间结果。相同前缀的请求可以复用这些结果，省掉重复计算。
- **KV Cache Affinity**：把请求优先发给已经持有对应缓存的实例，命中缓存、减少计算。
- **推理热点（Inference Hotspot）**：请求一直往同一组实例堆，导致这些实例过载排队，其他实例却闲着——整体吞吐反而下降。
- **Token-aware Routing**：不看请求数量，看 Token 级真实计算负载来决定请求往哪发。

在传统的 Kubernetes 服务中，负载均衡通常并不需要理解请求本身。

Round-robin、Least Request 等策略只需要关注请求数量、连接数或队列长度，就可以在多个服务实例之间分配流量。

但 LLM 推理改变了这个问题。

一个请求可能携带数万甚至更长的上下文；多轮对话和 Agent 工作流又会不断重复相同的 Prompt 前缀。
对于支持 Prefix Caching 的推理引擎而言，如果请求能够被路由到已经缓存对应 KV Cache 的实例，
就可以避免重复的 Prefill 计算，从而降低 TTFT，并提高 GPU 利用率。

因此，LLM 推理路由开始关注一个传统负载均衡器并不关心的问题：
**这个请求的 KV Cache 在哪台 GPU 上？**

这正是 [llm-d](https://llm-d.ai/) 长期探索的方向之一。其 Router 可以利用 Prefix Cache Affinity，
将请求优先路由到已经拥有对应缓存的 Model Server。称为
[Prefix-Cache Aware Routing](https://llm-d.ai/docs/0.7/architecture/advanced/kv-management/prefix-cache-aware-routing)。

但新的问题随之而来：
**如果一直追求 KV Cache Affinity，会不会反而造成热点？**

## KV Cache Affinity：缓存命中率与负载均衡的矛盾

假设一个集群中有 4 个 LLM 推理实例：

```text
Request
  │
  ▼
┌──────────────┐
│    Router    │
└──────┬───────┘
       │
       ├──────────────┬──────────────┬──────────────┐
       ▼              ▼              ▼              ▼
Replica A          Replica B      Replica C      Replica D
KV Cache ✓         KV Cache ✗     KV Cache ✗     KV Cache ✗
```

如果 Replica A 已经缓存了请求对应的 Prompt Prefix，那么将请求发送到 A 通常是最优选择。

这样可以复用已有 KV Cache，减少重复 Prefill 计算。

但随着请求不断到来，情况可能变成：

```text
Replica A   ████████████████████  Saturated
Replica B   ███████
Replica C   █████
Replica D   ████
```

如果 Router 仍然因为“这里有 Cache”而不断把请求发送到 Replica A，那么 Cache Affinity 就从性能优化手段变成了新的负载热点。

这就是 LLM 推理路由中一个非常典型的矛盾：
**Cache 命中希望请求“黏”在同一个实例上，负载均衡却希望请求能够及时分散。**

llm-d 此前已经围绕 Prefix Cache Affinity、KV Cache 利用率等信号构建了 AI 感知路由。
随着实际工作负载越来越复杂，这个问题进一步演化为：**什么时候应该坚持 Cache Affinity？什么时候应该放弃？**

## Sticky Until Saturated

llm-d 最新的技术探索给出了一个非常直观的答案：
**Sticky Until Saturated（在饱和之前保持黏性）。**

也就是：

```text
                 Request
                    │
                    ▼
          Prefix Cache Affinity
                    │
                    ▼
          ┌─────────────────┐
          │ Endpoint 是否    │
          │ 已经达到饱和？     │
          └───────┬─────────┘
                  │
           ┌──────┴──────┐
           │             │
          No            Yes
           │             │
           ▼             ▼
        保持黏性       释放黏性
           │             │
           │             ▼
           │       Token-aware
           │         Routing
           │             │
           └──────┬──────┘
                  ▼
             Model Server
```

核心思路并不复杂：
**只要拥有 Cache 的 Endpoint 还有余量，就尽可能复用 Cache；一旦达到饱和阈值，就不再为了 Cache 命中率继续制造热点。**

也就是说：
**Sticky → Saturated → Release**

这比简单地在 Cache Affinity 和 Load Balancing 之间做固定权重组合更加容易理解。

## 从 Request-aware 到 Token-aware

真正值得关注的是：**“饱和”到底应该怎么定义？**

LLM 工作负载与传统 HTTP 服务最大的区别之一，就是不同请求的计算成本差异非常大。

一个 1000 Token 的请求和一个 100,000 Token 的请求，都只是一个 HTTP Request，但它们对 GPU 造成的计算和显存压力完全不同。

因此，仅仅统计：

* Request 数量
* Connection 数量
* Queue Depth

并不能准确描述 LLM 推理实例的真实负载。

llm-d 的思路是进一步关注 **Token Load**。

对于不同类型的工作负载，可以选择不同的负载信号：

| 工作负载          | 主要瓶颈       | 负载信号                        |
| ------------- | ---------- | --------------------------- |
| Prefill-bound | Prefill 计算 | In-flight / Uncached Tokens |
| Decode-bound  | Decode 计算  | Active Requests             |
| Mixed / 高波动   | 多种因素       | Latency Predictor           |

这背后的逻辑很简单：
**Prefill 更关注 Token，Decode 更关注 Request。**

因此，Router 不应该只问：
“这个实例有多少请求？”

而应该进一步问：
**“这些请求正在给 GPU 带来多少实际计算负载？”**

这也是从传统 **Request-aware Routing** 向 **Token-aware Routing** 演进的重要一步。

## 为什么不能简单地使用一个固定阈值？

另一个值得注意的设计是：饱和阈值并不是一个对所有模型、所有 GPU 都通用的固定数字。

不同模型的计算特征不同，不同 GPU 的计算能力、显存带宽和 Kernel 性能也不同。

例如：

```text
Model A + GPU A
        │
        └── Saturation Threshold = X

Model A + GPU B
        │
        └── Saturation Threshold = Y

Model B + GPU A
        │
        └── Saturation Threshold = Z
```

因此，更合理的方式是针对 **Model + Accelerator** 进行校准，找到该组合下合适的饱和点。

这样，Router 的决策就不再完全依赖人工经验，而是建立在实际硬件和模型性能特征之上。

这也是 llm-d 这套设计比较有意思的地方：
**路由策略开始从“通用负载均衡”走向“面向具体模型和硬件的性能调度”。**

## 2–3× 吞吐提升来自哪里？

这并不意味着“Token-aware Routing 天生比 Round-robin 快 2–3 倍”。

真正重要的是：
**路由策略是否匹配了当前 workload 的实际瓶颈。**

在 llm-d 官方测试中，对于 **Prefill-bound workload**，针对瓶颈选择合适的 Token Load 信号，
在测试配置下相比 Kubernetes Service 的 Round-robin 获得了约 **2–3× 的吞吐提升**，
同时保持 TTFT。

这背后的原因可以理解为：

```text
Round-robin

Request ──→ A
Request ──→ B
Request ──→ C
Request ──→ D

        ≠

GPU 实际计算负载
```

而 Token-aware Routing 尝试让：

```text
Request
   │
   ▼
KV Cache Affinity
   │
   ▼
Saturation Check
   │
   ▼
Token Load
   │
   ▼
更适合当前负载的 Endpoint
```

最终让请求分布更加接近 GPU 真正能够处理的工作量。

## 这对 Kubernetes 意味着什么？

传统 Kubernetes Service 的负载均衡并不知道：

* Prompt 有多长；
* 请求已经缓存了多少 Prefix；
* 哪个 Pod 拥有对应 KV Cache；
* 一个请求还需要多少 Prefill 计算；
* 当前 GPU 是 Prefill-bound 还是 Decode-bound。

对于普通微服务，这些信息通常没有必要。

但对于 LLM 推理，这些信息可能直接决定性能。

因此，LLM 推理正在推动 Kubernetes 上层调度体系发生变化：

```text
Traditional Service Routing
          │
          ▼
    Request-aware
          │
          ▼
   KV Cache-aware
          │
          ▼
    Token-aware
          │
          ▼
  Bottleneck-aware
          │
          ▼
Model + Hardware-aware
```

llm-d 的 Router 正是在这个方向上不断扩展。

它并不是简单地替代 Kubernetes Service，而是在 Kubernetes AI 推理场景中增加一层理解 **LLM workload state** 的路由能力。

这也是为什么 llm-d 的设计越来越接近一个 **Inference Control Plane**，而不只是传统意义上的负载均衡器。

llm-d 官方文档目前已经将 Prefix Cache Affinity、KV Cache Indexing、KV Offloading 等能力作为其 [KV Cache 管理体系](https://llm-d.ai/docs/0.7/architecture/advanced/kv-management)的重要组成部分。

## 从“缓存命中”到“整体性能”

LLM 推理优化中，一个很容易出现的误区是：
**KV Cache 命中率越高越好。**

实际上并不一定。

如果为了追求 100% 的 Cache Affinity，把大量请求集中到一个已经接近饱和的 GPU 上，那么 Cache Hit 带来的收益可能很快被排队和计算瓶颈抵消。

更合理的目标应该是：
**在 Cache Reuse 与 Load Balance 之间找到动态平衡。**

这也是 “Sticky Until Saturated” 最值得关注的地方。

它没有简单地否定 Cache Affinity，也没有回到传统 Round-robin，而是增加了一个非常明确的判断：
**Cache Affinity 有价值，但只有在 Endpoint 还有计算余量时才有价值。**

当 Endpoint 饱和之后：
**负载均衡优先级应该超过 Cache Affinity。**

这其实也是 LLM 推理调度从“缓存感知”进一步走向“性能感知”的一个重要变化。

## DaoCloud 在 llm-d 中的贡献

上述 KV Cache 管理、P/D 分离和 Router 能力，正是 DaoCloud 深度参与的方向。

DaoCloud 自 2025 年起作为 **Contributor** 加入 llm-d 项目，在 [ADOPTERS.md](https://github.com/llm-d/llm-d/blob/main/ADOPTERS.md) 中被列为贡献者，其核心贡献围绕 **P/D 分离与 KV-cache 架构** 展开，并将这些能力落地到 DaoCloud 的 d.run MaaS 平台中。

以下是目前在 llm-d 项目中活跃的 DaoCloud 贡献者（统计截至 2026 年 8 月，涵盖 llm-d 及 llm-d-incubation 仓库的已合并 PR）：

| 贡献者 | 合并 PR 数 | 主要贡献方向 |
|-------|-------|------------|
| [yankay](https://github.com/yankay) | 38 | KV-cache UDS Tokenization、CI/发布工作流、基础设施版本升级、P/D 分离架构；同时担任 llm-d-kv-cache reviewer 与 llm-d-modelservice maintainer |
| [weizhoublue](https://github.com/weizhoublue) | 31 | vLLM 0.21 KV-offload 迁移兼容性、基础设施修复、KV-cache 调度与卸载、Router bug 修复 |
| [Iceber](https://github.com/Iceber) | 9 | Router 功能改进与 bug 修复、KV-cache 适配、主仓库维护 |
| [learner0810](https://github.com/learner0810) | 8 | Router 功能开发与 bug 修复 |
| [Alex-ai-future](https://github.com/Alex-ai-future) | 6 | llm-d-kv-cache 功能开发与优化 |
| [setsunakute](https://github.com/setsunakute) | 4 | inference-sim 测试改进、KV-cache 与 Router 适配 |
| [Phil-OSophy-42](https://github.com/Phil-OSophy-42) | 2 | Workload Autoscaler 开发、Router 功能改进 |
| [ErikJiang](https://github.com/ErikJiang) | 2 | Router 功能开发、基础设施改进 |
| [carlory](https://github.com/carlory) | 2 | Router bug 修复 |
| [panpan0000](https://github.com/panpan0000) | 1 | DisaggregatedSet 部署路径开发（Wide-EP 支持） |
| [kebe7jun](https://github.com/kebe7jun) | 1 | NIXL decode 场景下 prefill cached tokens 修复 |
| [bzsuni](https://github.com/bzsuni) | 1 | 基础设施改进 |
| [nicole-lihui](https://github.com/nicole-lihui) | 1 | Router 功能开发 |
| [yyzxw](https://github.com/yyzxw) | 1 | KV-cache 修复 |
| [my-git9](https://github.com/my-git9) | 1 | KV-cache 功能开发 |
| [Frapschen](https://github.com/Frapschen) | 1 | KV-cache 功能开发 |

其中，yankay 和 weizhoublue 的提交量领先，是核心贡献者。yankay 不仅在代码层面持续贡献，还担任 **llm-d-kv-cache 的 reviewer**（见 [kv-cache CODEOWNERS](https://github.com/llm-d/llm-d-kv-cache/blob/main/CODEOWNERS)）和 **llm-d-modelservice 的 maintainer**（见 [modelservice CODEOWNERS](https://github.com/llm-d-incubation/llm-d-modelservice/blob/main/.github/CODEOWNERS)），在项目治理层面也发挥着重要作用。

Iceber 的贡献覆盖 llm-d 主仓库、llm-d-router 和 llm-d-kv-cache 多个子项目，方向较为广泛，PR 数量也较为可观。Alex-ai-future 的贡献集中在 llm-d-kv-cache 子项目，围绕 KV Cache 相关功能开发展开。

DaoCloud 团队的工作集中在 `llm-d-kv-cache`、`llm-d-router` 和 `llm-d` 主仓库，与本文讨论的 KV Cache 管理和路由调度方向高度一致。

## 写在最后

LLM 推理的负载均衡正在变得越来越不像传统 Web 服务的负载均衡。

请求数量不再能够完整描述工作负载，GPU 利用率也不再是唯一需要关注的指标。

真正影响推理性能的因素正在逐渐变成：
**Request + Token + KV Cache + GPU Capacity + Workload Bottleneck。**

从 Prefix Cache Affinity 到 Token-aware Routing，再到针对不同模型和硬件进行性能校准，
llm-d 正在探索一种更接近 AI 工作负载本身的调度方式。

**对于 LLM 推理而言，最好的路由并不是让请求永远“黏”在缓存所在的 GPU 上，而是在缓存复用和 GPU 负载之间找到最佳平衡。**

这或许就是：
**Sticky Until Saturated。**
