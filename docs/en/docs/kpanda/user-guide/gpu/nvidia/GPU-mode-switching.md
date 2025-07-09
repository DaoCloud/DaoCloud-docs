# GPU Mode Switching

This document explains how to switch between full GPU mode, virtualization mode, and MIG mode.

## Prerequisites

* GPU devices are correctly installed on the cluster nodes.
* The [gpu-operator component](https://docs.daocloud.io/kpanda/user-guide/gpu/nvidia/install_nvidia_driver_of_operator.html) and [Nvidia-vgpu component](https://docs.daocloud.io/kpanda/user-guide/gpu/nvidia/vgpu/vgpu_addon.html) are properly installed in the cluster.
* The GPU mode on the nodes in the cluster includes one of the following types: NVIDIA-vGPU, NVIDIA GPU, or NVIDIA MIG.

## Use Cases for Each Mode

| | Scenario Comparison | Functionality Comparison |
| ---- | -------------- | --------------- |
| NVIDIA Full GPU Mode | Full-card usage, suitable for resource-intensive scenarios like AI training | Resources are exclusively allocated with no extra overhead. NVLink can be used to connect multiple GPU cards. |
| NVIDIA MIG Mode | Can be virtualized into up to 7 instances. Offers high QoS due to physical isolation. Suitable for AI inference workloads. | Memory fragmentation may occur due to MIG slicing. |
| NVIDIA Virtualization Mode | The number of virtual GPUs can be user-defined. Suitable for AI development or inference scenarios. | The more virtual GPUs are created and used concurrently, the more resource contention occurs, especially with frequent context switching. Ideal for testing and usage in environments with few GPUs but many users. Oversubscription is supported to increase user capacity. |

## Switching GPU Modes

!!! note

    NVIDIA's vGPU functionality supports node-level switching between full GPU, vGPU, and MIG modes, allowing different workloads within the same cluster to use different GPU modes.

1. On the **Clusters** page, select the target cluster and click its name to enter the cluster details page. In the left navigation panel, click **Nodes**, find the target node, click the **┇** action icon on the right, and select **GPU Mode** from the dropdown menu.

    <!-- ![GPU Mode 1](../images/gpumodel1.png) -->

2. After switching the mode and clicking **Confirm**, the node status will change to **Switching GPU Mode**. Once the GPU mode label is correctly displayed in the node list, the switch is complete (i.e., the `hami-nvidia-vgpu-device-plugin` pod for vGPU has started successfully).

    <!-- ![GPU Mode 2](../images/vgpuaddon2.png)

    ![GPU Mode 3](../images/vgpuaddon3.png) -->

3. After the node successfully switches GPU modes, you can [deploy applications using vGPU resources](vgpu_user.md).
   **Note**: There may be a slight delay during the switching process. Please wait until the node label is correctly displayed before deploying applications.
