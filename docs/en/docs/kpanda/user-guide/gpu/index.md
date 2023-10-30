---
hide:
  - toc
---

# Overview of GPU Management

This article introduces the capability of DaoCloud container management platform in unified operations and management of heterogeneous resources, with a focus on GPUs.

## Background

With the rapid development of emerging technologies such as AI applications, large-scale models, artificial intelligence, and autonomous driving, enterprises are facing an increasing demand for compute-intensive tasks and data processing. Traditional compute architectures represented by CPUs can no longer meet the growing computational requirements of enterprises. At this point, heterogeneous computing represented by GPUs has been widely applied due to its unique advantages in processing large-scale data, performing complex calculations, and real-time graphics rendering.

Meanwhile, due to the lack of experience and professional solutions in scheduling and managing heterogeneous resources, the utilization efficiency of GPU devices is extremely low, resulting in high AI production costs for enterprises. The challenge of reducing costs, increasing efficiency, and improving the utilization of GPUs and other heterogeneous resources has become a pressing issue for many enterprises.

## Introduction to GPU Capabilities

The DaoCloud container management platform supports unified scheduling and operations management of GPUs, NPUs, and other heterogeneous resources, fully unleashing the computational power of GPU resources, and accelerating the development of enterprise AI and other emerging applications. The GPU management capabilities of DaoCloud are as follows:

- Support for unified management of heterogeneous computing resources from domestic and foreign manufacturers such as NVIDIA, Huawei Ascend, and Days.
- Support for multi-card heterogeneous scheduling within the same cluster, with automatic recognition of GPU cards in the cluster.
- Support for native management solutions for NVIDIA GPUs, vGPUs, and MIG, with cloud-native capabilities.
- Support for partitioning a single physical card for use by different tenants, and allocate GPU resources to tenants and containers based on computing power and memory quotas.
- Support for multi-dimensional GPU resource monitoring at the cluster, node, and application levels, assisting operators in managing GPU resources.
- Compatibility with various training frameworks such as TensorFlow and PyTorch.

## Introduction to GPU Operator

Similar to regular computer hardware, NVIDIA GPU cards, as physical devices, need to have the NVIDIA GPU driver installed in order to be used. To reduce the cost of using GPUs on Kubernetes, NVIDIA provides the NVIDIA GPU Operator component to manage various components required for using NVIDIA GPUs. These components include the NVIDIA driver (for enabling CUDA), NVIDIA container runtime, GPU node labeling, DCGM-based monitoring, and more. In theory, users only need to plug the GPU card into a compute device managed by Kubernetes, and they can use all the capabilities of NVIDIA GPUs through the GPU Operator. For more information about NVIDIA GPU Operator, refer to the [NVIDIA official documentation](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/index.html). For deployment instructions, refer to [Offline Installation of GPU Operator](nvidia/install_nvidia_driver_of_operator.md).

Architecture diagram of NVIDIA GPU Operator:


