# InferX 介绍

InferX 是一款云原生的 AI 推理引擎扩展与管理工具，旨在简化大模型（LLM）在 Kubernetes 集群上的部署、调度与运维。它深度集成了 Kubernetes 生态系统中的高性能网络与存储能力，为用户提供稳定、可扩展的推理服务基础设施。

## 核心能力

- **高性能推理网络**: 基于 Kubernetes Gateway API Inference Extension (GAIE)，支持高性能的推理请求路由与流量管理。
- **灵活的模型管理**: 支持通过 Dataset (BaizeAI) 自动下载与挂载模型权重，同时兼容 PVC、NFS 等多种存储方式。
- **多种硬件适配**: 深度优化了针对 NVIDIA GPU 的调度与显存管理方案（支持 HAMI vGPU）。
- **离线环境友好**: 提供完整的离线安装包与同步工具，满足私有云及离线环境的部署需求。
- **多模型框架支持**: 兼容 vLLM 等主流推理框架，支持快速将模型对外暴露为标准 OpenAI 兼容接口。

## 快速开始

- [离线环境安装 InferX](guides/offline.md)
- [启用集群的 Istio GAIE 特性](guides/enable-istio-gaie-with-mspider.md)
- [模型权重下载与配置](guides/model-weights-setup.md)
- [模型服务对外暴露 (Hydra / Knoway)](guides/export-by-hydra.md)
- [常见问题解答 (FAQ)](guides/faqs.md)
