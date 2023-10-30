# NVIDIA GPU Card Usage Modes

NVIDIA, as a well-known graphics computing provider, offers various software and hardware solutions to enhance computational power. Among them, NVIDIA provides the following three solutions for GPU usage:

#### Full GPU

Full GPU refers to allocating the entire NVIDIA GPU to a single user or application. In this configuration, the application can fully occupy all the resources of the GPU and achieve maximum computational performance. Full GPU is suitable for workloads that require a large amount of computational resources and memory, such as deep learning training, scientific computing, etc.

#### vGPU (Virtual GPU)

vGPU is a virtualization technology that allows one physical GPU to be partitioned into multiple virtual GPUs, with each virtual GPU assigned to different virtual machines or users. vGPU enables multiple users to share the same physical GPU and independently use GPU resources in their respective virtual environments. Each virtual GPU can access a certain amount of compute power and memory capacity. vGPU is suitable for virtualized environments and cloud computing scenarios, providing higher resource utilization and flexibility.

#### MIG (Multi-Instance GPU)

MIG is a feature introduced by the NVIDIA Ampere architecture that allows one physical GPU to be divided into multiple physical GPU instances, each of which can be independently allocated to different users or workloads. Each MIG instance has its own compute resources, memory, and PCIe bandwidth, just like an independent virtual GPU. MIG provides finer-grained GPU resource allocation and management and allows dynamic adjustment of the number and size of instances based on demand. MIG is suitable for multi-tenant environments, containerized applications, batch jobs, and other scenarios.

Whether using vGPU in a virtualized environment or MIG on a physical GPU, NVIDIA provides users with more choices and optimized ways to utilize GPU resources. The Daocloud container management platform fully supports the above NVIDIA capabilities. Users can easily access the full computational power of NVIDIA GPUs through simple UI operations, thereby improving resource utilization and reducing costs.

- **Single Mode**: The node only exposes a single type of MIG device on all its GPUs. All GPUs on the node must:
    - Be of the same model (e.g., A100-SXM-40GB), with matching MIG profiles only for GPUs of the same model.
    - Have MIG configuration enabled, which requires a machine reboot to take effect.
    - Create identical GI and CI for exposing "identical" MIG devices across all products.
- **Mixed Mode**: The node exposes mixed MIG device types on all its GPUs. Requesting a specific MIG device type requires the number of compute slices and total memory provided by the device type.
    - All GPUs on the node must: Be in the same product line (e.g., A100-SXM-40GB).
    - Each GPU can enable or disable MIG individually and freely configure any available mixture of MIG device types.
    - The k8s-device-plugin running on the node will:
        - Expose any GPUs not in MIG mode using the traditional `nvidia.com/gpu` resource type.
        - Expose individual MIG devices using resource types that follow the pattern `nvidia.com/mig-<slice_count>g.<memory_size>gb`.

For detailed instructions on enabling these configurations, refer to [Offline Installation of GPU Operator](install_nvidia_driver_of_operator.md).

## How to Use

You can refer to the following links to quickly start using Daocloud's management capabilities for NVIDIA GPU cards.

- **[Using Full NVIDIA GPU](full_gpu_userguide.md)**
- **[Using NVIDIA vGPU](vgpu/vgpu_user.md)**
- **[Using NVIDIA MIG](mig/mig_usage.md)**
