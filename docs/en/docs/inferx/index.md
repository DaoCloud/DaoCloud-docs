# InferX Introduction

InferX is a cloud-native AI inference engine extension and management tool designed to simplify the deployment, scheduling, and operations of large language models (LLMs) on Kubernetes clusters. It deeply integrates high-performance networking and storage capabilities from the Kubernetes ecosystem, providing users with stable and scalable inference service infrastructure.

## Core Capabilities

- **High-Performance Inference Networking**: Based on Kubernetes Gateway API Inference Extension (GAIE), supports high-performance inference request routing and traffic management.
- **Flexible Model Management**: Supports automatic model weight download and mounting via Dataset (BaizeAI), while also being compatible with PVC, NFS, and other storage methods.
- **Multi-Hardware Adaptation**: Deeply optimized scheduling and GPU memory management for NVIDIA GPUs (supports HAMi vGPU).
- **Offline-Environment Friendly**: Provides complete offline installation packages and synchronization tools to meet deployment needs in private cloud and offline environments.
- **Multi-Model Framework Support**: Compatible with mainstream inference frameworks such as vLLM, supports quickly exposing models as standard OpenAI-compatible interfaces.

## Quick Start

- [Install InferX in Offline Environment](guides/offline.md)
- [Enable Istio GAIE Feature in Cluster](guides/enable-istio-gaie-with-mspider.md)
- [Model Weight Download and Configuration](guides/model-weights-setup.md)
- [Expose Model Service Externally (Hydra/Knoway)](guides/export-by-hydra.md)
- [FAQ](faqs.md)
