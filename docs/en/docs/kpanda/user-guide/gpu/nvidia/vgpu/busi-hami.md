# Install the Commercial HAMi NVIDIA vGPU Addon

The commercial HAMi NVIDIA vGPU Addon is used to virtualize an NVIDIA GPU into multiple vGPUs in a Kubernetes cluster and allocate them to different workloads on demand.

The installation procedure of the commercial edition is basically the same as that of the [open-source NVIDIA vGPU Addon](vgpu_addon.md). The main difference is that after the commercial edition is installed, you need to import a valid License and complete activation before the related commercial capabilities can be used normally.

## Differences Between the Commercial Edition and the Open-source Edition

### Installation Differences

| Item | Open-source Edition | Commercial Edition |
| --- | --- | --- |
| Installation entry | Helm Chart installation | Helm Chart installation |
| Helm chart | `nvidia-vgpu` | `nvidia-vgpu-commercial` |
| Installation parameters | Basically the same | Basically the same |
| GPU mode switching | Supports switching to vGPU mode or MIG mode | Supports switching to vGPU mode or MIG mode |
| License | Not required | A License must be imported and activated |

### Feature Differences

| Feature | Open-source Edition | Commercial Edition | Description |
| --- | --- | --- | --- |
| Heterogeneous card support | All NVIDIA | All NVIDIA;<br>All PPU;<br>Ascend 910A, 910B2, 910B3, 910B4, 910B4-1, 910C (slicing not supported), 310P;<br>Metax Xiyun series GPU (including C550/C500/C500X/C290/C280/N260 and other models);<br>Hygon;<br>Cambricon;<br>Enflame;<br>Kunlunxin;<br>Moore Threads;<br>Iluvatar and more | — |
| vGPU resource slicing | Computing power slicing | Computing power slicing;<br>Memory slicing | — |
| Scheduling capability | For NVIDIA GPU:<br>Binpack/Spread<br>Specify the GPU card model<br>Specify a specific card | For NVIDIA GPU:<br>Binpack/Spread<br>Specify the GPU card model<br>Specify a specific card<br>Task priority | — |
| Monitoring capability | Supported | Supported | Can be integrated with the observability module via ServiceMonitor |
| Enterprise-level support | Open-source community support | Commercial support | — |
| License management | No License required | License activation required | — |

## Prerequisites

Before installation, confirm the following:

- Refer to the [GPU Support Matrix](../../gpu_matrix.md) to confirm that the cluster nodes have NVIDIA GPU cards of the corresponding model.
- The GPU Operator has been deployed in the current cluster through a Helm app. For details, refer to [Offline Install GPU Operator](../install_nvidia_driver_of_operator.md).
- For the commercial HAMi, you need to [apply for a License](https://github.com/dynamia-ai/workshop/blob/main/lab1-load-license.md) from HAMi in advance.

## Installation Steps

The installation method of the commercial Addon is the same as that of the open-source edition. The difference lies in the Helm chart name and the License activation after installation.

1. Access the target cluster.

    Path: __Container Management__ -> __Clusters__ -> click the target cluster name.

    ![Access the Cluster](../../images/busihami1.png)

2. Go to the Helm Chart page and select the commercial Addon.

    Path: __Helm Apps__ -> __Helm Chart__ , search for and select the Addon corresponding to `nvidia-vgpu-commercial`.

    ![Search for the Commercial Addon](../../images/busihami2.png)

3. Configure the installation parameters.

    The common parameters are as follows:

    | Parameter | Description |
    | --- | --- |
    | `deviceCoreScaling` | The GPU computing power usage ratio, with a default value of 1. A value greater than 1 indicates that virtual computing power is enabled. If configured as S, the total computing power of the vGPUs sliced from a single GPU is S × 100%. |
    | `deviceMemoryScaling` | The GPU memory usage ratio, with a default value of 1. A value greater than 1 indicates that virtual memory is enabled. If the physical memory of the GPU is M, when configured as S, the total memory of the sliced vGPUs is S × M. |
    | `deviceSplitCount` | The maximum number of tasks that can be sliced from a single GPU, with a default value of 10. At most N tasks can exist simultaneously on each GPU (where N is the value of this parameter). |
    | `Resources` | The resource requests and limits of components such as vgpu-device-plugin and vgpu-scheduler. |
    | `ServiceMonitor` | Disabled by default. Once enabled, you can go to the observability module to view vGPU-related monitoring. If you need to enable it, make sure that insight-agent is installed and running; otherwise, the NVIDIA vGPU Addon installation will fail. |

    To modify advanced parameters, you can edit them directly in the YAML column.

4. Submit the installation.

5. Confirm that the Addon-related Pods are running properly.

    ```bash
    kubectl get pod -n <the namespace where HAMi is located>
    ```

    Expected result: Pods of components such as the HAMi scheduler and device plugin are all in the Running state.

6. Switch the node GPU mode to vGPU.

    Click __Nodes__ in the left navigation bar, find the target node, click __Switch GPU Mode__ , and switch to vGPU mode.

    !!! note

        NVIDIA's vGPU capability supports node-level GPU mode switching (full GPU/vGPU/MIG mode), meeting the different GPU mode requirements of different workloads in the same cluster.

    After clicking __Confirm__ , the node status changes to __Switching GPU Mode__ . After the switch is complete (that is, the hami-nvidia-vgpu-device-plugin Pod for vGPU has started up), the node status changes to __Nvidia-vGPU__ .

    After the node GPU mode is switched successfully, you can refer to [Use NVIDIA vGPU in Applications](vgpu_user.md) to deploy workloads. The switching process has a slight delay, so deploy applications only after the node labels are displayed correctly.

## Import a License and Activate It

After the commercial HAMi is installed, you must import a License to activate the commercial capabilities.

### Obtain the License Application Information

Before or after installation, you need to prepare the License application information (such as the GPU UUID) as required by HAMi. For the detailed steps to obtain the application information, import the License, and complete activation, refer to [Obtain the Commercial HAMi License Information and Complete the Import](https://github.com/dynamia-ai/workshop/blob/main/lab1-load-license.md).

## Verify the Installation

After completing the installation, GPU mode switching, and License activation, you can verify the installation in the following ways:

1. In __Nodes__ , confirm that the GPU mode of the target node is __Nvidia-vGPU__ .
2. Run `kubectl get pod -n <the namespace where HAMi is located>` and confirm that all related components are in the Running state.
3. Deploy a test workload and confirm that resources such as `nvidia.com/vgpu` can be requested normally.
