# 从"能跑"到"跑得快"：DaoCloud 异构 GPU 上的国产算力优化实践

随着大模型从实验验证走向规模化生产，AI 基础设施正在经历一个明显变化：GPU 不再只是"有多少张卡"的问题，
而逐渐演变为一个涉及硬件、驱动、计算库、AI 框架、推理引擎、调度系统和可观测性的完整系统工程。

对于云原生 AI 平台而言，支持一种新的 GPU，第一步是让 [Kubernetes](https://kubernetes.io/zh-cn/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/) 能够识别和分配 GPU；但真正决定应用价值的，是能否进一步释放 GPU 的计算能力，
让模型获得稳定、可预测的推理性能。这也是国产 GPU 进入生产环境后面临的核心挑战：
**从"能跑"走向"跑得快"，需要优化的不只是 GPU 本身，而是从硬件到软件、从单卡到集群的完整技术栈。**

本文以沐曦 GPU 为例，介绍 DaoCloud 在异构 GPU 环境下围绕资源管理、软件栈适配、推理引擎和性能优化所关注的关键技术。

## 从设备接入到性能释放

在传统 Kubernetes 场景中，GPU 支持通过
[Device Plugin](https://kubernetes.io/zh-cn/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)
将 GPU 暴露为可调度资源，用户通过资源请求将 GPU 分配给工作负载。对于基础 GPU 工作负载来说，这已经足够。

但大模型推理的情况完全不同。
一个现代大模型推理服务背后涉及从 GPU Runtime、GPU Software Stack、AI Framework（如 PyTorch）、推理引擎（如 vLLM），
到 Attention/MoE/GEMM 算子和 GPU Kernel 的完整软件栈。对于云原生 AI 平台而言，Kubernetes 则负责将这些能力以可调度、
可管理的方式交付给工作负载。其中任何一层出现瓶颈，
都可能导致 GPU 利用率不足、推理吞吐下降、首 Token 延迟（TTFT）增加、显存占用过高或多 GPU 通信效率下降。

因此，异构 GPU 的优化不能停留在"Device Plugin 能不能识别设备"这一层，而需要从整个 AI 软件栈进行协同优化。

以沐曦 GPU 为例，其 C 系列 GPU 配套有完整的 [MXMACA](https://www.metax-tech.com/platform.html?cid=4) 软件栈，提供
GPU 编程、计算库以及上层 AI 软件生态所需的基础能力。主流 AI 软件生态长期围绕 CUDA 形成，国产 GPU
需要在保持软件生态兼容性的同时发挥自身硬件能力。目前，沐曦已围绕 [vLLM](https://docs.vllm.ai/) 建设了
[vLLM-MetaX](https://github.com/MetaX-MACA/vLLM-metax) 硬件插件，通过 vLLM 的硬件可插拔机制接入 MetaX GPU，
尽量减少对 vLLM 核心代码的侵入式修改，并持续跟随 vLLM 上游版本演进。异构 GPU 适配正在从"设备级适配"走向"AI Framework 级适配"——
GPU 进入 Kubernetes 只是第一步。要真正释放硬件性能，还需要 GPU Runtime、AI Framework、Inference Engine
和 Kernel 等软件栈协同优化；在集群环境中，还需要 Kubernetes 提供资源调度、拓扑感知和可观测能力。

## 资源感知与拓扑调度

在异构 GPU 集群中，不同厂商、不同型号 GPU 具有不同的计算能力、显存容量和互联拓扑。如果不同 GPU
都仅以简单的扩展资源形式暴露给调度器，调度器能够感知资源数量，却难以进一步理解 GPU 型号、显存容量以及卡间拓扑等更细粒度的属性。

对于普通推理任务而言，GPU 之间可能具有一定的可替代性。但对于 Tensor Parallel、Expert Parallel 等大模型分布式推理任务，
GPU 的型号、显存以及卡间通信能力都可能影响最终性能。调度系统需要回答的不再是"有没有 GPU"，而是"这是什么 GPU？
它在哪里？它与其他 GPU 如何连接？这个工作负载真正需要什么样的 GPU？"

随着模型规模增长，单 GPU 推理已无法满足越来越多场景。当通过 Tensor Parallel 将计算分布到多张 GPU 时，
GPU 之间的通信效率变得至关重要。如果调度过程中没有考虑 GPU 拓扑，选取不同 GPU 组合可能导致不同的通信路径，从而产生明显不同的通信性能。

调度系统不仅需要知道"有几张 GPU"，还应该逐步具备 GPU 型号感知、显存感知、PCIe 拓扑感知、NUMA 感知、
GPU 间互联感知、多 GPU 任务的 Gang Scheduling，以及与模型并行策略结合的拓扑感知调度能力。
最终目标是让 Kubernetes 从一个"资源分配器"成为面向 AI 工作负载的资源优化器。

## 算子优化：从 GPU 利用率到 Kernel 利用率

GPU 利用率高，并不意味着 GPU 性能已经被充分利用。GPU 利用率只是一个粗粒度指标，无法直接反映计算单元利用率、内存带宽利用率、
Kernel 执行效率以及通信开销。因此，进一步优化通常需要进入算子和 Kernel 层。

```text
Memory Access        ███████████████
Kernel Execution     ███████
Compute Utilization  █████
Communication        ████████
```

进一步优化必须进入算子和 Kernel 层。
沐曦公开的算子优化项目已将 DeepSeek V3/R1 所用的 MLA（Multi-Head Latent Attention）
以及 Native Sparse Attention（NSA）列为重点优化对象，并围绕
[TileLang](https://github.com/tile-ai/tilelang) 算子编程框架、MXMACA 软件栈和 C500 GPU
开展算子性能优化。TileLang 提供面向 GPU Kernel 的编程抽象，使开发者能够围绕 Tile 划分、
内存访问和计算调度等方面针对目标硬件进行优化。这些算子恰好对应当前大模型推理中几个最重要的性能热点。

**MoE 与 Fused MoE GEMM**。MoE 模型通过 Router 将 Token 动态分配给不同 Expert，优势是用相对有限的计算激活更大的参数规模。
例如，DeepSeek-V4-Pro 采用超大规模 MoE 架构，总参数规模达到 1.6T，但单 Token 激活参数约 49B。
稀疏激活降低了单 Token 的计算量，但也对 Expert 路由、Grouped GEMM、显存访问和多 GPU 通信提出了更高要求。
这样的稀疏激活机制降低了单 Token 的计算量，但也对 Expert 路由、Grouped GEMM、显存访问和多 GPU 通信提出了更高要求。
但 Router 在运行时动态决定路由，各 Expert 收到的 Token 数量不固定，直接为每个 Expert 执行独立 GEMM
会导致 Kernel Launch 开销显著、小矩阵难以充分利用并行计算单元、反复加载 Expert 权重造成显存带宽浪费。
Fused MoE GEMM 可以将多个 Expert 的矩阵乘法组织为 Grouped GEMM，通过一次或少量 Kernel 调度完成多个
Expert 的计算，减少 Kernel Launch 和数据访问开销，提高 GPU 计算资源利用率。
同一套模型代码在不同 GPU 上并不一定拥有相同的最佳执行方式，硬件特性不同就需要重新设计 Kernel 和优化策略。

**Attention 与显存优化**。随着模型上下文长度不断增加，Attention 和 KV Cache 已经成为大模型推理性能优化的重要方向。
以最新的 DeepSeek-V4 为例，其采用新的混合 Attention 架构，并针对超长上下文和 Agent 场景进行了专门设计。
V4-Pro 和 V4-Flash 均支持百万 Token 级上下文，这对 KV Cache 容量、Attention Kernel、显存访问以及推理调度提出了更高要求。
对 GPU 推理而言，长上下文并不只是增加显存容量的问题。随着上下文长度和并发请求增加，KV Cache 的存储、
Attention计算以及内存访问都会成为性能瓶颈。因此，针对具体 GPU 架构优化 Attention Kernel、
改进 KV Cache 管理和降低内存访问开销，是提升大模型推理性能的重要手段。
这也意味着，面对 DeepSeek-V4 这类新一代大模型，GPU 适配不能停留在“模型能够运行”的层面，
而需要进一步针对模型架构中的新算子和计算模式进行优化。

## 端到端优化与统一管理

算子优化只是端到端性能的一个环节。对于大模型推理平台，[vLLM](https://docs.vllm.ai/) 已成为重要的推理引擎之一，
但仅优化 vLLM 上层逻辑，并不能保证 GPU 获得最佳性能。一个请求从进入推理服务到最终返回 Token，需要经过
Scheduler、Continuous Batching、KV Cache、Attention、MoE/GEMM、GPU Kernel 和 Hardware。
单独优化其中任何一个组件都无法保证端到端性能提升——
Scheduler 优化了但 GPU Kernel 很慢，Kernel 很快但通信效率低，GPU 很快但 KV Cache 导致
Batch Size 上不去——最终的端到端性能仍然可能不理想。

性能优化必须从单组件优化转向端到端优化。同时，如果只针对某一种 GPU 做优化，很容易形成新的资源孤岛。
在实际环境中，不同 GPU 往往对应不同的驱动、Runtime、Device Plugin、监控组件和 AI 软件栈。
用户需要根据不同硬件重新学习驱动、Runtime、Device Plugin、GPU Operator、监控组件、AI Framework、
推理镜像和性能调优方法。这与云原生平台追求的统一资源管理理念并不一致。

因此，平台层需要将不同 GPU 在驱动、Runtime、设备插件和监控等方面的差异尽可能收敛在基础设施层，
为上层工作负载提供统一的资源管理和交付方式。

```text
                 AI Workload
                      │
                      ▼
             ┌────────────────┐
             │    DaoCloud    │
             │  AI Platform   │
             └────────────────┘
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       NVIDIA       MetaX       Other GPU
          │           │           │
          ▼           ▼           ▼
       Runtime     MXMACA       Runtime
          │           │           │
          └───────────┼───────────┘
                      ▼
                 Kubernetes
```

用户不应该因为底层 GPU 型号发生变化，就需要重新设计整个应用交付流程。

## 可观测性与性能评估

如果不知道瓶颈在哪里，就很难知道应该优化什么。一个完整的异构 GPU 平台需要建立从硬件到模型的可观测性：
从硬件层的温度、功耗、显存和利用率，到 Kernel 层的执行时间、内存访问和 Occupancy，再到推理引擎的
TTFT、TPOT、Throughput 和 Batch Size。沐曦生态中已提供包括 `mx-smi`、性能分析和 GPU 监控相关工具
（详见[沐曦开发者文档](https://developer.metax-tech.com/)），
这些工具覆盖了 GPU 状态监控、Kubernetes 集群监控以及性能分析等不同层面，为进一步关联 GPU 指标与 AI 工作负载提供了基础。

对 DaoCloud 而言，更重要的是将这些底层指标与 Kubernetes 工作负载关联起来：哪个 Pod 使用了哪张 GPU？
这张 GPU 当前利用率是多少？哪个模型占用了多少显存？推理延迟升高时，是 Scheduler、KV Cache、Kernel
还是 GPU 通信出现了瓶颈？只有建立这种关联，GPU 可观测性才能真正服务于 AI 性能优化。

在性能评估方面，单纯比较理论算力意义有限，AI 平台更应关注端到端指标：

| 指标 | 含义 |
| --- | --- |
| TTFT | 首 Token 延迟 |
| TPOT | 单 Token 输出延迟 |
| Throughput | 单位时间生成 Token 数 |
| GPU Utilization | GPU 利用率 |
| KV Cache Usage | KV Cache 使用情况 |

## 从单卡到集群

当 GPU 从单机扩展到集群，性能问题会进一步复杂化。单卡阶段主要关注 Kernel、Memory 和 Compute；
多卡阶段需要关注 GPU Topology、Communication、Parallelism 和 Scheduling；
多节点阶段则进一步引入 Network 和 Observability。一个优秀的异构 GPU 平台不应该只是把 GPU"接入 Kubernetes"，
而应该让 Kubernetes 理解 AI 工作负载的需求，将合适的 GPU、拓扑、网络和计算资源组合起来。

国产 GPU 的发展正在经历三个阶段的演进：

1. **"能跑"** —— GPU、Driver、Runtime、Device Plugin，解决 GPU 如何被 Kubernetes 识别和分配。
2. **"跑得快"** —— AI Framework、Inference Engine、Kernel Optimization，解决模型如何充分利用 GPU。
3. **"规模化跑得快"** —— Scheduling、Topology、Observability，解决多 GPU、多节点和异构 GPU 集群如何高效运行。

这一方向并非纸上谈兵。2025 年 3 月，DaoCloud 与沐曦等多家企业联合发布了国产高密度算力机柜
[Shanghai Cube](https://d.run/news/i80bp6njjsg0yhxat1rgbvb7)，采用沐曦曦云 C550 系列 GPU 芯片，
单机柜 128 卡液冷高密度部署。DaoCloud 为 Shanghai Cube 设计了定制化的国产操作系统，提供面向高密度国产算力的调度管理能力。
该系统已成功实现 DeepSeek 671B 满血版大模型的高效推理，是国产算力从"硬件可用"走向"生产级规模化应用"的一次标志性实践。

![shanghai cube](./images/sh-cube.png)

以沐曦 GPU 为代表的国产算力正在形成越来越完整的软件生态——从 [MXMACA](https://www.metax-tech.com/platform.html?cid=4)
到 [vLLM](https://github.com/vllm-project/vllm)，从 GPU 管理到算子优化，从单卡性能到集群调度，
国产 GPU 的能力边界正在从"硬件可用"不断向"软件栈成熟"和"生产级规模化应用"延伸。

真正的异构不应该意味着更多的复杂性，而应该意味着：无论底层使用什么 GPU，
开发者都可以获得统一的云原生体验，平台负责把不同硬件的能力真正释放出来。

**DaoCloud 将持续围绕异构算力、智能调度、推理优化和 AI 可观测性，推动国产算力从"可用"走向"好用"，
从单点性能优化走向集群级效率优化，为大模型训练与推理提供更加开放、高效、统一的云原生基础设施。**
