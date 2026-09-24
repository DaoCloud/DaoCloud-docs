# From KV Cache Affinity to Token-aware Routing: How llm-d Avoids LLM Inference Hotspots

> Source: the original llm-d.ai blog post, [Sticky Until Saturated: Token-Aware Routing in llm-d](https://llm-d.ai/blog/sticky-until-saturated-token-aware-routing)

Before reading, get familiar with a few concepts:

- **KV Cache**: The precomputed Key/Value intermediates during inference. Requests with the same prefix can reuse these results, avoiding repeated computation.
- **KV Cache Affinity**: Route requests preferentially to the instance that already holds the corresponding cache, hitting the cache and reducing computation.
- **Inference Hotspot**: Requests keep piling onto the same set of instances, overloading them with queues while other instances sit idle — overall throughput actually drops.
- **Token-aware Routing**: Ignore request count; decide where to send a request based on the Token-level real compute load.

In traditional Kubernetes services, load balancing usually doesn't need to understand the request itself.

Round-robin, Least Request, and similar strategies only need to track request count, connection count, or queue length to distribute traffic across service instances.

But LLM inference changes this.

A request may carry tens of thousands of tokens or an even longer context; multi-turn conversations and agent workflows repeatedly reuse the same Prompt prefix. For inference engines that support Prefix Caching, if a request can be routed to the Model Server that already caches the corresponding KV Cache, it avoids repeated Prefill computation, thereby lowering TTFT and improving GPU utilization.

Therefore, LLM inference routing starts caring about a question traditional load balancers don't ask:
**Which GPU holds this request's KV Cache?**

This is exactly one of the directions [llm-d](https://llm-d.ai/) has long explored. Its Router can use Prefix Cache Affinity to route requests preferentially to the Model Server that already owns the corresponding cache, called [Prefix-Cache Aware Routing](https://llm-d.ai/docs/0.7/architecture/advanced/kv-management/prefix-cache-aware-routing).

But a new problem follows:
**If we keep chasing KV Cache Affinity, could it actually create hotspots?**

## KV Cache Affinity: The Conflict Between Cache Hit Rate and Load Balancing

Suppose a cluster has 4 LLM inference instances:

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

If Replica A has already cached the Prompt Prefix for the request, sending the request to A is usually optimal.

This reuses the existing KV Cache and avoids repeated Prefill computation.

But as requests keep arriving, the situation may become:

```text
Replica A   ████████████████████  Saturated
Replica B   ███████
Replica C   █████
Replica D   ████
```

If the Router keeps sending requests to Replica A just because "there's a cache here," then Cache Affinity turns from a performance optimization into a new load hotspot.

This is a very typical conflict in LLM inference routing:
**Cache hits want the request to "stick" to the same instance, while load balancing wants requests to spread out in time.**

llm-d had previously built AI-aware routing around signals like Prefix Cache Affinity and KV Cache utilization. As real workloads grow more complex, the problem evolves further into: **when should we insist on Cache Affinity, and when should we give it up?**

## Sticky Until Saturated

llm-d's latest technical exploration gives a very intuitive answer:
**Sticky Until Saturated.**

That is:

```text
                 Request
                    │
                    ▼
          Prefix Cache Affinity
                    │
                    ▼
          ┌─────────────────┐
          │  Has the        │
          │  Endpoint       │
          │  saturated?     │
          └───────┬─────────┘
                  │
           ┌──────┴──────┐
           │             │
          No            Yes
           │             │
           ▼             ▼
        Stay sticky      Release stickiness
           │             │
           │             ▼
           │       Token-aware
           │         Routing
           │             │
           └──────┬──────┘
                  ▼
             Model Server
```

The core idea is simple:
**As long as the Endpoint that holds the Cache still has headroom, reuse the Cache as much as possible; once the saturation threshold is hit, stop creating hotspots just for cache hit rate.**

In other words:
**Sticky → Saturated → Release**

This is easier to understand than naively combining a fixed weight between Cache Affinity and Load Balancing.

## From Request-aware to Token-aware

What's truly worth noting: **how exactly should "saturated" be defined?**

One of the biggest differences between LLM workloads and traditional HTTP services is that the compute cost varies enormously between requests.

A 1,000-Token request and a 100,000-Token request are both just one HTTP Request, yet their compute and memory pressure on the GPU are completely different.

Therefore, simply counting:

* Request count
* Connection count
* Queue depth

does not accurately describe the real load on an LLM inference instance.

llm-d's approach is to go further and focus on **Token Load**.

For different workload types, you can choose different load signals:

| Workload | Main bottleneck | Load signal |
|----------|-----------------|-------------|
| Prefill-bound | Prefill compute | In-flight / Uncached Tokens |
| Decode-bound | Decode compute | Active Requests |
| Mixed / high volatility | Multiple factors | Latency Predictor |

The logic behind this is simple:
**Prefill cares more about Tokens; Decode cares more about Requests.**

Therefore, the Router shouldn't only ask:
"How many requests does this instance have?"

It should ask further:
**"How much actual compute load are these requests putting on the GPU?"**

This is also an important step in the evolution from traditional **Request-aware Routing** to **Token-aware Routing**.

## Why Can't We Just Use a Fixed Threshold?

Another noteworthy design point: the saturation threshold is not a fixed number that works for all models and all GPUs.

Different models have different compute characteristics, and different GPUs have different compute power, memory bandwidth, and kernel performance.

For example:

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

Therefore, a more reasonable approach is to calibrate per **Model + Accelerator**, finding the right saturation point for that combination.

This way, the Router's decision no longer relies entirely on human experience, but is built on the actual hardware and model performance characteristics.

This is also what makes llm-d's design interesting:
**Routing strategy is moving from "generic load balancing" toward "performance scheduling oriented to specific models and hardware."**

## Where Does the 2–3× Throughput Gain Come From?

This does not mean "Token-aware Routing is inherently 2–3× faster than Round-robin."

What truly matters is:
**whether the routing strategy matches the actual bottleneck of the current workload.**

In llm-d's official tests, for **Prefill-bound workloads**, choosing the right Token Load signal for the bottleneck delivered about **2–3× throughput improvement** versus Kubernetes Service's Round-robin under the test configuration, while keeping TTFT stable.

The reason behind this can be understood as:

```text
Round-robin

Request ──→ A
Request ──→ B
Request ──→ C
Request ──→ D

        ≠

GPU actual compute load
```

Whereas Token-aware Routing tries to make:

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
Endpoint better suited to current load
```

Ultimately making the request distribution closer to what the GPU can actually handle.

## What Does This Mean for Kubernetes?

Traditional Kubernetes Service load balancing doesn't know:

* How long the Prompt is;
* How much Prefix the request has already cached;
* Which Pod holds the corresponding KV Cache;
* How much more Prefill computation a request still needs;
* Whether the current GPU is Prefill-bound or Decode-bound.

For ordinary microservices, this information is usually unnecessary.

But for LLM inference, this information may directly determine performance.

Therefore, LLM inference is driving changes in Kubernetes' upper-layer scheduling system:

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

llm-d's Router keeps expanding in this direction.

It doesn't simply replace Kubernetes Service; rather, it adds a routing layer on top of the Kubernetes AI inference scenario that understands the **LLM workload state**.

This is also why llm-d's design is increasingly resembling an **Inference Control Plane**, not just a traditional load balancer.

llm-d's official documentation now treats Prefix Cache Affinity, KV Cache Indexing, KV Offloading, and similar capabilities as important parts of its [KV Cache management system](https://llm-d.ai/docs/0.7/architecture/advanced/kv-management).

## From "Cache Hits" to "Overall Performance"

In LLM inference optimization, a very easy trap is:
**higher KV Cache hit rate is always better.**

In reality, not necessarily.

If, in pursuit of 100% Cache Affinity, you concentrate a large number of requests onto a GPU that is already near saturation, the benefit from Cache Hits may quickly be offset by queueing and compute bottlenecks.

A more reasonable goal should be:
**finding a dynamic balance between Cache Reuse and Load Balance.**

This is also the most noteworthy aspect of "Sticky Until Saturated."

It doesn't simply negate Cache Affinity, nor does it return to traditional Round-robin; instead it adds a very clear judgment:
**Cache Affinity has value, but only when the Endpoint still has compute headroom.**

After the Endpoint saturates:
**Load Balancing priority should outweigh Cache Affinity.**

This is in fact an important shift in LLM inference scheduling from "cache-aware" further toward "performance-aware."

## DaoCloud's Contributions to llm-d

The KV Cache management, P/D disaggregation, and Router capabilities described above are exactly the directions DaoCloud is deeply involved in.

DaoCloud joined the llm-d project as a **Contributor** starting in 2025, listed as a contributor in [ADOPTERS.md](https://github.com/llm-d/llm-d/blob/main/ADOPTERS.md). Its core contributions revolve around **P/D disaggregation and the KV-cache architecture**, and these capabilities have been deployed into DaoCloud's d.run MaaS platform.

The following are currently active DaoCloud contributors to the llm-d project (statistics as of August 2026, covering merged PRs in the llm-d and llm-d-incubation repositories):

| Contributor | Merged PRs | Main contribution areas |
|-------------|------------|------------------------|
| [yankay](https://github.com/yankay) | 38 | KV-cache UDS Tokenization, CI/release workflows, infrastructure version upgrades, P/D disaggregation architecture; also serves as llm-d-kv-cache reviewer and llm-d-modelservice maintainer |
| [weizhoublue](https://github.com/weizhoublue) | 31 | vLLM 0.21 KV-offload migration compatibility, infrastructure fixes, KV-cache scheduling and offloading, Router bug fixes |
| [Iceber](https://github.com/Iceber) | 9 | Router feature improvements and bug fixes, KV-cache adaptation, main repo maintenance |
| [learner0810](https://github.com/learner0810) | 8 | Router feature development and bug fixes |
| [Alex-ai-future](https://github.com/Alex-ai-future) | 6 | llm-d-kv-cache feature development and optimization |
| [setsunakute](https://github.com/setsunakute) | 4 | inference-sim test improvements, KV-cache and Router adaptation |
| [Phil-OSophy-42](https://github.com/Phil-OSophy-42) | 2 | Workload Autoscaler development, Router feature improvements |
| [ErikJiang](https://github.com/ErikJiang) | 2 | Router feature development, infrastructure improvements |
| [carlory](https://github.com/carlory) | 2 | Router bug fixes |
| [panpan0000](https://github.com/panpan0000) | 1 | DisaggregatedSet deployment path development (Wide-EP support) |
| [kebe7jun](https://github.com/kebe7jun) | 1 | NIXL decode scenario prefill cached tokens fix |
| [bzsuni](https://github.com/bzsuni) | 1 | Infrastructure improvements |
| [nicole-lihui](https://github.com/nicole-lihui) | 1 | Router feature development |
| [yyzxw](https://github.com/yyzxw) | 1 | KV-cache fix |
| [my-git9](https://github.com/my-git9) | 1 | KV-cache feature development |
| [Frapschen](https://github.com/Frapschen) | 1 | KV-cache feature development |

Among them, yankay and weizhoublue lead in commit volume and are core contributors. Beyond code-level contributions, yankay also serves as **reviewer for llm-d-kv-cache** (see [kv-cache CODEOWNERS](https://github.com/llm-d/llm-d-kv-cache/blob/main/CODEOWNERS)) and **maintainer for llm-d-modelservice** (see [modelservice CODEOWNERS](https://github.com/llm-d-incubation/llm-d-modelservice/blob/main/.github/CODEOWNERS)), playing an important role in project governance.

Iceber's contributions span multiple sub-projects — the llm-d main repo, llm-d-router, and llm-d-kv-cache — with fairly broad coverage and a notable PR count. Alex-ai-future's contributions focus on the llm-d-kv-cache sub-project, centered on KV Cache-related feature development.

The DaoCloud team's work concentrates on `llm-d-kv-cache`, `llm-d-router`, and the `llm-d` main repo, closely aligned with the KV Cache management and routing/scheduling directions discussed in this article.

## Wrapping Up

Load balancing for LLM inference is becoming less and less like the load balancing of traditional web services.

Request count can no longer fully describe the workload, and GPU utilization is no longer the only metric to watch.

The factors that truly affect inference performance are gradually becoming:
**Request + Token + KV Cache + GPU Capacity + Workload Bottleneck.**

From Prefix Cache Affinity to Token-aware Routing, and then to performance calibration for specific models and hardware, llm-d is exploring a scheduling approach that is closer to the AI workload itself.

**For LLM inference, the best routing is not to let requests forever "stick" to the GPU where the cache lives, but to find the best balance between cache reuse and GPU load.**

This may well be:
**Sticky Until Saturated.**
