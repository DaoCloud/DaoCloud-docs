# Overview of NVIDIA Multi-Instance GPU (MIG)

## MIG Scenarios

- **Multi-Tenant Cloud Environments**:

   MIG allows cloud service providers to partition a physical GPU into multiple independent GPU instances, which can be allocated to different tenants. This enables resource isolation and independence, meeting the GPU computing needs of multiple tenants.

- **Containerized Applications**:

   MIG enables finer-grained GPU resource management in containerized environments. By partitioning a physical GPU into multiple MIG instances, each container can be assigned with dedicated GPU compute resources, providing better performance isolation and resource utilization.

- **Batch Processing Jobs**:

   For batch processing jobs requiring large-scale parallel computing, MIG provides higher computational performance and larger memory capacity. Each MIG instance can utilize a portion of the physical GPU's compute resources, accelerating the processing of large-scale computational tasks.

- **AI/Machine Learning Training**:

   MIG offers increased compute power and memory capacity for training large-scale deep learning models. By partitioning the physical GPU into multiple MIG instances, each instance can independently carry out model training, improving training efficiency and throughput.

In general, NVIDIA MIG is suitable for scenarios that require finer-grained allocation and management of GPU resources. It enables resource isolation, improved performance utilization, and meets the GPU computing needs of multiple users or applications.

## Overview of MIG

NVIDIA Multi-Instance GPU (MIG) is a new feature introduced by NVIDIA on H100, A100, and A30 series GPUs. Its purpose is to divide a physical GPU into multiple GPU instances to provide finer-grained resource sharing and isolation. MIG can split a GPU into up to seven GPU instances, allowing a single physical GPU card to provide separate GPU resources to multiple users, maximizing GPU utilization.

This feature enables multiple applications or users to share GPU resources simultaneously, improving the utilization of computational resources and increasing system scalability.

With MIG, each GPU instance's processor has an independent and isolated path throughout the entire memory system, including cross-switch ports on the chip, L2 cache groups, memory controllers, and DRAM address buses, all uniquely allocated to a single instance.

This ensures that the workload of individual users can run with predictable throughput and latency, along with identical L2 cache allocation and DRAM bandwidth. MIG can partition available GPU compute resources (such as streaming multiprocessors or SMs and GPU engines like copy engines or decoders) to provide defined quality of service (QoS) and fault isolation for different clients such as virtual machines, containers, or processes. MIG enables multiple GPU instances to run in parallel on a single physical GPU.

MIG allows multiple vGPUs (and virtual machines) to run in parallel on a single GPU instance while retaining the isolation guarantees provided by vGPU. For more details on using vGPU and MIG for GPU partitioning, refer to [NVIDIA Multi-Instance GPU and NVIDIA Virtual Compute Server](https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/solutions/resources/documents1/TB-10226-001_v01.pdf).

## MIG Architecture

The following diagram provides an overview of MIG, illustrating how it virtualizes one physical GPU card into seven GPU instances that can be used by multiple users.



## Important Concepts

* __SM__ (Streaming Multiprocessor): The core computational unit of a GPU responsible for executing graphics rendering and general-purpose computing tasks. Each SM contains a group of CUDA cores, as well as shared memory, register files, and other resources, capable of executing multiple threads concurrently. Each MIG instance has a certain number of SMs and other related resources, along with the allocated memory slices.
* __GPU Memory Slice__ : The smallest portion of GPU memory, including the corresponding memory controller and cache. A GPU memory slice is approximately one-eighth of the total GPU memory resources in terms of capacity and bandwidth.
* __GPU SM Slice__ : The smallest computational unit of SMs on a GPU. When configuring in MIG mode, the GPU SM slice is approximately one-seventh of the total available SMs in the GPU.
* __GPU Slice__ : The GPU slice represents the smallest portion of the GPU, consisting of a single GPU memory slice and a single GPU SM slice combined together.
* __GPU Instance__ (GI): A GPU instance is the combination of a GPU slice and GPU engines (DMA, NVDEC, etc.). Anything within a GPU instance always shares all GPU memory slices and other GPU engines, but its SM slice can be further subdivided into Compute Instances (CIs). A GPU instance provides memory QoS. Each GPU slice contains dedicated GPU memory resources, limiting available capacity and bandwidth while providing memory QoS. Each GPU memory slice gets one-eighth of the total GPU memory resources, and each GPU SM slice gets one-seventh of the total SM count.
* __Compute Instance__ (CI): A Compute Instance represents the smallest computational unit within a GPU instance. It consists of a subset of SMs, along with dedicated register files, shared memory, and other resources. Each CI has its own CUDA context and can run independent CUDA kernels. The number of CIs in a GPU instance depends on the number of available SMs and the configuration chosen during MIG setup.
* __Instance Slice__ : An Instance Slice represents a single CI within a GPU instance. It is the combination of a subset of SMs and a portion of the GPU memory slice. Each Instance Slice provides isolation and resource allocation for individual applications or users running on the GPU instance.

## Key Benefits of MIG

- **Resource Sharing**: MIG allows a single physical GPU to be divided into multiple GPU instances, providing efficient sharing of GPU resources among different users or applications. This maximizes GPU utilization and enables improved performance isolation.

- **Fine-Grained Resource Allocation**: With MIG, GPU resources can be allocated at a finer granularity, allowing for more precise partitioning and allocation of compute power and memory capacity.

- **Improved Performance Isolation**: Each MIG instance operates independently with its dedicated resources, ensuring predictable throughput and latency for individual users or applications. This improves performance isolation and prevents interference between different workloads running on the same GPU.

- **Enhanced Security and Fault Isolation**: MIG provides better security and fault isolation by ensuring that each user or application has its dedicated GPU resources. This prevents unauthorized access to data and mitigates the impact of faults or errors in one instance on others.

- **Increased Scalability**: MIG enables the simultaneous usage of GPU resources by multiple users or applications, increasing system scalability and accommodating the needs of various workloads.

- **Efficient Containerization**: By using MIG in containerized environments, GPU resources can be effectively allocated to different containers, improving performance isolation and resource utilization.

Overall, MIG offers significant advantages in terms of resource sharing, fine-grained allocation, performance isolation, security, scalability, and containerization, making it a valuable feature for various GPU computing scenarios.
