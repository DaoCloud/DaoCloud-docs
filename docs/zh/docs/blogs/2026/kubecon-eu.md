# KubeCon + CloudNativeCon Europe 2026 见闻录

23-26 March | Amsterdam, The Netherlands

## DRA

Dynamic Resource Allocation enables simple and efficient configuration, sharing, and allocation of acclerators and other specialized devices.

- 2019 年 Intel 和 NVIDIA 的开发者们开始讨论这个能力，
- 2022 年在 Kubernetes v1.26 中首次发布了 Alpha 版的 DRA
- 2024 年
    - 在 Kubernetes v1.30 中重新设计了结构化参数
    - 成立了新的 WG 工作组 Device Management
    - 在 Kubernetes v1.32 中 DRA 进阶至 Beta
- 2025 年，DRA 进阶至成熟的 GA

## Kubernetes AI Conformance Program

Program launch at KubeCon NA 2025; now a SIG Architecture subproject

Built on top of Kubernetes Conformance
- Accelerators/DRA, networking/inference, scheduling/orchestration, observability, security, etc.

Same release cadence as Kubernetes

KAR (Kubernetes AI-conformance Requirements): similar to KEP
- SHOULD & MUST requirements

DaoCloud 早在 2025 年 10 月就积极通过了 Kubernetes AI Conformance Program 的各项认证，其主打产品 DCE 被 CNCF 组织认为是经认证的 AI Platform

Kubernetes AI Conformance¶
随着 AI/ML 工作负载对计算资源和硬件加速的需求爆发式增长，CNCF 推出 Kubernetes AI Conformance 认证标准，在基础 Kubernetes Conformance 认证之上，定义了 AI 场景专属的功能、API 和配置要求，为 AI 工作负载的跨环境移植、高效运行提供统一基准。

通过认证的平台可获得 CNCF 官方授权使用 AI Conformance 标识，成为行业认可的 AI 友好型 Kubernetes 发行版。

作为国内开源事业的领军企业，DaoCloud 紧跟云原生 AI 发展潮流。在社区推出 Kubernetes AI Conformance 合规标准后，率先针对目前广泛使用的 Kubernetes v1.33 启动 DCE 5.0 平台的 AI Conformance 测试，并于 2025 年 10 月成功通过认证， 成为国内首个在该版本获得认证的企业级 AI/ML 平台。

https://docs.daocloud.io/dce/kcsp/

## 接下来

1.36: Inference：

- KAR-0010: High-Performance Pod-to-Pod Communication
- KAR-0011: Advanced Inference Ingress
- KAR-0041: Disaggregated Inference Support

Automate tests

```bash
go test -v ./test [-run <TestName>] \
  [-kubeconfig=<path/to/kubeconfig>] [-accelerator-type=<type>]
```

We need more conformance tests for specific areas, and more standardization for an unified/cohesive experience.

## OSS Model Ecosystem

Models, explosion in parameters and reasoning capability
Agents, multi-turn and huge token demand

- 2022 No oss models
- 2022, the foundation, Liama 1, Alpaca, Falcon, Grok 1, Mistral, Vicuna, Mixtra & Granile
- 2022, Multimodality, Gemma 1 & 2, Qwen 1.5 & 2.5, Stable LM 2, Liama 3, 3.2 & 3.3, Phi-3 & 3.5, DeepSeek-V2 & V3, Falcon 2, Mistral Large 2, Nemotron-4
- 2022, Reasoning era, DeepSeek R1 & DeepSeek V3.2, Kimi K2, GPT-OSS, Qwen 3, Gemma 3 & 3.5, Phi-4, Liama 4 Scount & Maverick, Mistral NeMo 2, Granite 4, SmoiLM3
- 2026, Agentic frontiers, DeepSeek-V3.2 Terminus, GLM-4.7, Kimi K2.5, Nemotron 3 Nano, Jamba 2 3B

## The challenge of scaling inference

Distributed inference is essential for cost-effective scaling of AI, but introduces unique **operationalization** challenges

*   Load balancing **variable, resource-heavy** and hardware-affinity nature of requests
*   Ensuring SLO and maintaining low latency under multi-tenant traffic
*   Leveraging and managing **heterogenous** hardware for better cost-efficiency
*   Managing distributed KV cache state at scale as key part in inference efficiency
*   Orchestrating prefill and decode phases; and multi-node serving

- Request to LLM
- Gateway
- Kubernetes cluster
- Node Pool
- Pending request queue
- LLM
- KVCache Utilization
- GPU/TPUs

## llm-d

## LWS Operator

## HAMi insight on AI workloads

## K8s 近些年的主要变化

1.30.0
ProvisioningRequest v1beta1 API implemented, integration with Kueue.
1.31.0
ProvisioningRequest API graduated to v1.
Cluster Autoscaler can now react to changes in controller replica count, before Pods are created and marked unschedulable by kube-scheduler.
1.32.0
Experimental support for Dynamic Resource Allocation (DRA) is added.
1.34.0
CapacityBuffer v1alpha1 API implemented.
1.35.0
CapacityBuffer v1beta1 API implemented.
Support for taking Container Storage Interface (CSI) volume limits into account during scaling decisions added.
Support for DRA is production-ready.

## 前方现场消息

[图片]
[图片]
[图片]
[图片]
[图片]
[图片]
[图片]
[图片]
[图片]
[图片]
今天是 KubeCon Europe 2026 的第二天。更准确地说，2026 年 3 月 23 日这一天还属于 CNCF-hosted co-located events day，地点在阿姆斯特丹 RAI，会场当天并行展开了 Agentics Day、CiliumCon、Cloud Native AI + Kubeflow Day、Kubernetes on Edge Day、Platform Engineering Day、Observability Day、Open Source SecurityCon、WasmCon 等一系列专题活动。
还只是 co-located events day，现场就已经热得不得了。人多到什么程度？最直观的感受就是，整个展馆虽然非常大，但几乎每个房间都挤满了人，热门场次门口要排队，连公共区域和厕所都明显比往年更拥挤。KubeCon Europe 2026 官方对外介绍的整体规模是 超过 12,000 名开发者、IT 从业者和技术负责人，到了现场之后，确实能感受到这种全球性大会的密度和能量。
更让人印象深刻的，不只是人多，而是“人从哪里来、在讨论什么”。来参会的人天南海北，什么国家的都有，什么行业的人都有，做平台的、做安全的、做网络的、做 AI 的、做边缘计算的，全都汇聚在这里。你会明显感觉到，KubeCon 早就不是一个只属于 Kubernetes 工程师的小圈子活动，而是整个全球云原生生态的年度交汇点。
而今年最强烈的一个信号，就是 AI 是主线中的主线。
从官方当天的安排就能看出来，Cloud Native AI + Kubeflow Day 和 Agentics Day: MCP + Agents 都是非常核心的专题；与此同时，Sched 上还能直接看到不少非常有代表性的热门议题，比如 “MCP in 2026: Context is All You Need”、“The New AI Coding Fabric”、“Is AIOps the Future of Operations? Real Use Cases From the Trenches”、以及 “Expl(AI)n Like I'm 5: An Introduction To AI-Native Networking”。这些题目本身就已经说明，今年大家讨论的重点，早就不只是传统意义上的容器编排，而是 Kubernetes 与 AI、Agent、开发流程、运维体系、网络架构的深度融合。
所以你会看到一个非常鲜明的现场现象：讲 Agent 的房间，人多得连进去都很困难（上面有个排队的图）；讲 AI、AIOps、AI-native networking 的场次，也都是高密度人流。这个变化很说明问题——Kubernetes 正在从“云原生基础设施”进一步演进为“AI 时代的生产底座”。今天现场最火的，不只是 Kubernetes 本身，而是 Kubernetes 如何承接推理、Agent、模型上下文、开发协同、智能运维和企业级治理。
在这样的背景下，DaoCloud 今天的两场分享就显得很有代表性。

## Hongbing Zhang, DaoCloud, about KubeEdge

March 25, 2026 11:45 - 12:15 CET

Solving Industrial Challenges With KubeEdge: A Post-Graduation Report - Yue Bao, Huawei; Hongbing Zhang, DaoCloud; Yin Ding, VMware by Broadcom

Following its graduation within the CNCF, KubeEdge has solidified its position as the premier platform for extending Kubernetes to the edge. In this session, project maintainers will explore KubeEdge's evolution, offering a deep dive into the core architecture that enables efficient management of edge workloads.

Attendees will gain insights from real-world deployments across diverse sectors, including Smart Cities, Industrial IoT (IIoT), Edge AI, Robotics, and Retail. Beyond success stories, the talk will cover critical technical updates, including the newly introduced Certified KubeEdge conformance test, recent technological advancements, and the latest updates on community governance.

张红兵的那场，是你给我的这个 session 链接对应的分享。虽然 Sched 的短链正文无法直接抓取，但从公开索引和 DaoCloud 对外预告里可以确认，这场是由 Hongbing Zhang（DaoCloud） 与 Huawei 的讲者共同参与，重点围绕 边缘工作负载管理架构、多域场景案例，以及社区和产业协作 展开。DaoCloud 的公开预告也明确提到，张红兵会和其他核心贡献者一起讨论如何建设一个 多厂商、更多元的社区，以及如何把这条能力延伸到不同产业场景。

## Weizhou Lan, DaoCloud, about network

March 26, 2026 14:30 - 15:00 CET

Making topology-aware scheduling practical for AI workloads: from discovery to simulation at scale - Weizhou Lan, DaoCloud

In large-scale AI inference clusters, multi-tenant workloads require both efficient GPU utilization and dynamic RDMA networking. However, heterogeneous GPU interconnect technologies inevitably lead to multi-level network topologies, such as scale-up networks and RDMA spine–leaf structures.
These diverse topologies introduce several challenges: Dynamic topology discovery and health detection across multiple layers, including scale-up, RDMA spine, and RDMA leaf. Second, Topology-aware scheduling that supports priority-based placement and ensures GPUs leverage optimal communication paths.Third, Validation at scale, requiring cost-effective simulation of large, multi-level topologies instead of relying on expensive hardware.
In this talk, it will share practical approach of topology discovery to help Kueue to achieve topology-aware scheduling, and showcase how Kwok simulates thousands of virtual nodes with multi-level topologies, enabling large-scale validation at zero hardware cost.

蓝维洲的那场则更直接，也更“硬核”。他的 session 是 CiliumCon 的闪电演讲，题目是 “Closing the Gap: Fair North–South Bandwidth Management for Tenants”。公开页面和 Cilium 的预告都写得很清楚：这场分享聚焦的是多租户 Kubernetes 集群里的 租户级入口带宽公平治理，并且采用的是 Cilium CNI + Spiderpool 的轻量方式，不需要额外外部组件。

这个题目看起来像网络问题，实际上本质上讲的是平台治理能力。因为当 Kubernetes 进入多租户、大规模、复杂生产环境以后，问题不再只是“网络能不能通”，而是“资源能不能被公平治理”“平台能不能稳定承载不同租户和不同业务”“底层能力能不能原生内建，而不是靠很多外挂组件去拼”。蓝围州这场的价值就在于，它体现的是 DaoCloud 在底层平台工程、网络控制和多租户精细化治理上的持续积累。
如果把今天 3 月 23 日 的热门内容再挑几个给大家看，我觉得至少有四类特别值得关注。
第一类，是 Agent / MCP / Agentic infrastructure。
像 “MCP in 2026: Context is All You Need” 这样的题目，本身就说明 Agent 已经从概念热度走向工程问题：上下文怎么组织，模型如何连接工具与系统，生产里的 Agent 应该怎么运行。
第二类，是 AI 开发与 AI 运维。
“The New AI Coding Fabric” 和 “Is AIOps the Future of Operations? Real Use Cases From the Trenches” 这类议题说明，AI 已经不只是模型团队的事，而是在重塑开发流程和运维流程。
第三类，是 AI-native networking。
“Expl(AI)n Like I'm 5: An Introduction To AI-Native Networking” 这样的议题很有代表性，说明网络已经不再只是“底层 plumbing”，而是在主动适配 AI 工作负载。
第四类，是 边缘、平台工程和安全。
官方当天专门把 Kubernetes on Edge Day、Platform Engineering Day、Open Source SecurityCon 独立成会，本身就说明边缘、平台化和安全治理已经不是配角，而是 Kubernetes 继续扩张边界时必须同步做深的三条主线。
如果把这些观察放在一起看，今天给我最深的感受其实不是简单的“人多”或者“热闹”，而是：全球云原生正在进入一个新的阶段。 这个阶段里，一边是 AI、Agent、Inference 正在快速进入 Kubernetes 的主叙事，另一边是边缘、多租户治理、平台工程和安全也在同步深化。谁能把上层新趋势和底层生产能力真正连起来，谁就更有机会站在下一轮基础设施竞争的主线上。
而从 DaoCloud 今天的两场分享来看，这种价值已经体现得很清楚了：一场在讲边缘和多方协同，一场在讲网络和租户治理；一场代表向外延展，一场代表向下扎根。它们不是彼此割裂的，而是共同指向一个方向：DaoCloud 既在参与社区，也在面向真实生产环境给出答案。 在 KubeCon 这样一个全球云原生的中心舞台上，这种存在感和宣传价值，本身就是非常有分量的。
与此同时，现场也越来越能感受到中国力量。无论是中国公司的身影、中国工程师在社区中的活跃度，还是中国团队在创新和创造上的持续投入，都比以往更容易被看见。放在这样一个国际化程度极高、知名度极高的大会里，这种变化会被放大得更加明显。KubeCon 的影响力本来就已经覆盖全球，而中国技术力量在这里的存在感，也正在变得越来越强。
KubeCon Europe 2026 的第二天，还只是开始。
但仅仅是这一天，就已经足够让人看清楚很多事情：未来的竞争，不会只是某一个技术点的竞争，而是“云原生底座 + AI 新能力 + 边缘延展 + 企业级治理”的综合竞争。 在这条主线上，DaoCloud 的价值、技术积累和品牌存在感，都在被进一步放大。