---
hide:
  - toc
---

# Token 工厂

Token 工厂是 DaoCloud 面向 AI 智算场景打造的一体化平台，围绕大模型推理、算力调度和集群运维提供端到端能力支撑。
平台深度整合大模型服务平台与 InferX 推理引擎，向上承接模型部署与推理加速，向下依托容器管理实现 GPU 算力的精细化调度与资源编排；
同时借助可观测性模块全方位监控推理性能、算力利用率与基础设施健康度，
通过全局管理完成用户权限、工作空间、审计日志的统一治理，构建起从算力接入到模型服务的完整业务闭环。

作为面向智算中心打造的高效能 AI Token 生产及经营系统，Token 工厂助力传统算力中心向高效、可盈利的 Token 生产运营模式升级。
平台统一纳管英伟达及国产异构算力，依靠智能调度与推理优化，把分散 GPU 算力转化为低成本、高稳定、可交易的标准化 Token 服务；
依托 Token 工厂管家与统一运营体系，完成资源、生产、成本、供需的全局管控，面向终端用户、管理者、运营者、运维者提供能力，
推动智算中心业务定位从 “提供算力” 升级为 “生产和运营 Token”。

## 模块详情

<div class="grid cards" markdown>

- :simple-themodelsresource: **[Token 工厂管理](../hydra/intro/index.md)**

    ---

    提供模型托管、版本管理和在线推理服务，支持多种主流大模型的快速部署与弹性扩缩容。

- :material-speedometer: **[InferX 推理引擎](../inferx/index.md)**

    ---

    针对 GPU 推理场景深度优化，通过算子融合、动态批处理和显存复用等技术显著提升推理吞吐量，降低单次推理延迟。

- :octicons-container-16: **[容器管理](../kpanda/intro/index.md)**

    ---

    基于 Kubernetes 提供 GPU 资源池化、多租户隔离和优先级调度，实现算力资源的高效分配与回收。

- :material-monitor-dashboard: **[可观测性](../insight/intro/index.md)**

    ---

    覆盖集群、节点、容器和应用的多维度监控，提供指标采集、日志检索和链路追踪能力，帮助快速定位推理瓶颈与系统异常。

- :fontawesome-solid-user-group: **[全局管理](../ghippo/intro/index.md)**

    ---

    管理用户权限、多租户、账号、审计日志等。

- :material-train-car-container: **[虚拟机](../virtnest/intro/index.md)**

    ---

    基于 KubeVirt 提供容器化虚拟机管理，支持虚拟机的创建、克隆、快照和热迁移，统一纳管容器与虚拟机工作负载。

- :material-table-refresh: **[服务网格](../mspider/intro/index.md)**

    ---

    基于 Istio 提供非侵入式服务治理能力，包括流量管理、安全策略和可观测性，支持多集群网格统一管理。

- :shrimp: **[ClawOS 智能体](../clawos/intro/index.md)**

    ---

    智能体治理平台，提供 Skill 市场、OpenClaw 实例管理和企业级集成能力，支持飞书、Microsoft Teams 等协作平台。

- :material-slot-machine: **[AI Lab](../baize/intro/index.md)**

    ---

    训推一体化平台，提供 Notebook 开发环境、训练任务调度、模型管理和 GPU 资源池化，支持分布式训练与超参调优。

</div>

## 运营中心

![Token 工厂运营中心](./images/tf01.png)

Token 工厂运营中心是 AI 时代的智能生产驾驶舱，将 Token 生产全链路转化为可量化、可追踪、可优化的实时数据视图，
让运营团队对平台的每一秒运转都了如指掌。驾驶舱以毫秒级数据刷新呈现平台实时运转状态。
