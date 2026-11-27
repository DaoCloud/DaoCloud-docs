---
hide:
  - toc
---

# What is Turbo Inference

Turbo Inference is an integrated platform for optimizing the inference performance of large models. Built on heterogeneous GPU computing power and a cloud native foundation, it continuously introduces industry-leading inference architectures and performance optimization techniques to reduce inference costs and improve service efficiency. It also covers the complete lifecycle from model deployment to runtime assurance, helping users build faster, more stable, and more cost-effective large model inference services.

## Architecture Positioning

Turbo Inference sits in the middle of the cloud native AI stack rather than at its edge: below it are Kubernetes clusters and heterogeneous GPUs / domestic accelerator cards, above it are model serving entry points (Knoway, Hydra) and business applications such as agents and RAG. It is the layer where compute is turned into Tokens that applications can consume.

![Where Turbo Inference sits in the cloud native AI stack: bottom-up, heterogeneous compute, cloud native AI platform, Turbo Inference, model serving entry, and business applications](images/inferx-position.svg)

Three things define that position:

- **It does not replace inference frameworks**: on top of mainstream frameworks such as vLLM and llm-d, it improves performance through PD disaggregation, KV Cache offloading, multi-node deployment, and scheduling optimization.
- **It is not tied to a single hardware vendor**: the same deployment model runs on NVIDIA / AMD GPUs and domestic accelerator cards, which keeps replacement and scaling straightforward.
- **Its gains are measurable**: pre-rollout acceptance results for performance and accuracy, plus post-rollout monitoring of degradation and latency jitter, so acceleration gains can be verified and regression-tested.

## Core Capabilities

| Capability | Description |
| --- | --- |
| **Model Deployment** | Rapidly deploy high-performance inference services: compatible with mainstream inference frameworks and heterogeneous GPUs, supports high-performance architectures such as PD disaggregation and KV Cache offload, and quickly adapts to new models, new frameworks, and new GPUs / domestic accelerator cards. |
| **Turbo Inference** | Continuously improve Token production efficiency: based on high-performance inference frameworks, combined with concurrency tuning, long-context, and operator optimization techniques, it improves throughput and GPU utilization while reducing latency and per-Token cost. |
| **Service Acceptance** | Ensure high-quality rollout of model services: before rollout, complete inference performance, model accuracy, API compatibility, and functional tests, and produce standardized acceptance results and performance optimization reports. |
| **Runtime Assurance** | Ensure stable operation of inference services: continuously observe service performance and stability, detect issues such as performance degradation, latency jitter, and traffic bursts in a timely manner, quickly locate runtime risks, and ensure service SLA. |

## Product Advantages

| Advantage | Description |
| --- | --- |
| **Comprehensive Inference Performance Optimization** | Full-stack optimization from orchestration framework to inference engine improves inference throughput and resource utilization on the same hardware. |
| **In-depth Tuning for Domestic Accelerator Cards** | Extensive experience adapting and tuning a variety of domestic accelerator cards fully unlocks the potential of domestic hardware. |
| **Full-lifecycle Service Assurance** | Covers the entire delivery, operations, and O&M workflow, providing end-to-end service assurance for complex production environments. |
| **Cutting-edge Open Source Ecosystem Collaboration** | Active participation in open source communities such as vLLM drives technology evolution and new model adaptation, accelerating the adoption of cutting-edge capabilities. |

## Quick Start

- [Deploy Model Services](model-services/index.md): learn the concepts and deployment paths of model services, and start with an optimized template, a generic template, or a custom `values.yaml`.
- [Install Turbo Inference in Offline Environment](offline.md)
- [Enable Istio GAIE Feature in Cluster](best-practice/enable-istio-gaie-with-mspider.md)
- [Model Weight Download and Configuration](best-practice/model-weights-setup.md)
- [Deploy a PD-disaggregated GLM 5.3 Service](best-practice/llm-d-pd-glm.md)
- [Expose Model Service Externally (Hydra/Knoway)](best-practice/export-by-hydra.md)
- [FAQ](faqs.md)

[Download Center](https://docs.daocloud.io/en/download/){ .md-button }
[Learn about d.run Token Factory](https://docs.daocloud.io/en/tf/){ .md-button }
[Learn about d.run AI OS](https://docs.daocloud.io/en/drun/){ .md-button }
