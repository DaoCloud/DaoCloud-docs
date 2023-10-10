# NVIDIA GPU 卡使用模式

NVIDIA 作为业内知名的图形计算供应商，为算力的提升提供了诸多软硬件解决方案，其中 NVIDIA 在 GPU 的使用方式上提供了如下三种解决方案：

#### 整卡（Full GPU）

整卡是指将整个 NVIDIA GPU 分配给单个用户或应用程序。在这种配置下，应用可以完全占用 GPU 的所有资源，并获得最大的计算性能。整卡适用于需要大量计算资源和内存的工作负载，如深度学习训练、科学计算等。

#### vGPU（Virtual GPU）

vGPU 是一种虚拟化技术，允许将一个物理 GPU 划分为多个虚拟 GPU，每个虚拟 GPU 分配给不同的虚拟机或用户。vGPU 使多个用户可以共享同一台物理 GPU，并在各自的虚拟环境中独立使用 GPU 资源。每个虚拟 GPU 可以获得一定的计算能力和显存容量。vGPU 适用于虚拟化环境和云计算场景，可以提供更高的资源利用率和灵活性。

#### MIG（Multi-Instance GPU）

MIG 是 NVIDIA Ampere 架构引入的一项功能，它允许将一个物理 GPU 划分为多个物理 GPU 实例，每个实例可以独立分配给不同的用户或工作负载。
每个 MIG 实例具有自己的计算资源、显存和 PCIe 带宽，就像一个独立的虚拟 GPU。
MIG 提供了更细粒度的 GPU 资源分配和管理，可以根据需求动态调整实例的数量和大小。MIG 适用于多租户环境、容器化应用程序和批处理作业等场景。

无论是在虚拟化环境中使用 vGPU，还是在物理 GPU 上使用 MIG，NVIDIA 为用户提供了更多的选择和优化 GPU 资源的方式。
Daocloud 容器管理平台全面兼容了上述 NVIDIA 的能力特性，用户只需通过简单的界面操作，就能够获得全部 NVIDIA GPU 的计算能力，从而提高资源利用率并降低成本。

- **Single 模式**，节点仅在其所有 GPU 上公开单一类型的 MIG 设备，节点上的所有 GPU 必须：
  - 属于同一个型号（例如 A100-SXM-40GB），只有同一型号 GPU 的 MIG Profile 才是一样的
  - 启用 MIG 配置，需要重启机器才能生效
  - 为在所有产品中公开“完全相同”的 MIG 设备类型，创建相同的GI 和 CI
- **Mixed 模式**，节点在其所有 GPU 上公开混合 MIG 设备类型。请求特定的 MIG 设备类型需要设备类型提供的计算切片数量和内存总量。
  - 节点上的所有 GPU 必须：属于同一产品线（例如 A100-SXM-40GB）
  - 每个 GPU 可启用或不启用 MIG，并且可以自由配置任何可用 MIG 设备类型的混合搭配。
  - 在节点上运行的 k8s-device-plugin 将：
    - 使用传统的 `nvidia.com/gpu` 资源类型公开任何不处于 MIG 模式的 GPU
    - 使用遵循架构 `nvidia.com/mig-<slice_count>g.<memory_size>gb` 的资源类型公开各个 MIG 设备

开启配置详情参考： [GPU Operator 离线安装](install_nvidia_driver_of_operator.md)



## 如何使用

您可以参考以下链接，快速使用 Daocloud 关于 NVIDIA GPU 卡的管理能力。

- **[NVIDIA GPU 整卡使用](./full_gpu_userguide.md)**
- **[NVIDIA vGPU 使用](./vgpu_user.md)**
- **[NVIDIA MIG 使用](./mig_usage.md)**

