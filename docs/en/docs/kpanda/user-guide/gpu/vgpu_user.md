# Using vGPU Resources for Applications

This section describes how to use vGPU capabilities on the DCE 5.0 platform.

## Prerequisites

- The cluster has already been deployed either through the operator or manually. Please refer to [Nvidia Driver Installation](vgpu_driver.md) for specific deployment steps.
- The vGPU addon has been installed on the cluster. Please refer to [vGPU Addon Installation](vgpu_addon.md).

## Procedure

1. Confirm if the cluster has detected the GPU card. Click on the corresponding `Cluster` -> `Cluster Settings`
   -> `Addon Plugins`, and check if the GPU type is automatically enabled and detected. Currently,
   the cluster will automatically enable `GPU` and set the `GPU Type` as `Nvidia vGPU`.

    ![Alt text](./images/vgpu-cluster.png)

2. Deploy a workload. Click on the corresponding `Cluster` -> `Workloads`. Deploy the workload using an image, and after selecting the type as `Nvidia vGPU`, the following parameters will automatically appear:

    - Physical Card Quantity (`nvidia.com/vgpu`): Specifies the number of physical cards
      that the current pod needs to mount, which should be less than or equal to the number of cards on the host machine.
    - GPU Cores (`nvidia.com/gpucores`): Represents the amount of GPU cores occupied by each card,
      with values ranging from 0 to 100. If configured as 0, it is considered non-isolated;
      if configured as 100, it is considered as exclusive access to the entire card.
    - GPU Memory (`nvidia.com/gpumem`): Represents the amount of GPU memory occupied by each card,
      with values in MB. The minimum value is 1, and the maximum value is the total memory capacity of the card.

    > If there are any issues with the above configurations, it may result in
    > scheduling failures and resource allocation issues.

    If deploying the workload using a custom YAML file, please use the corresponding resource keys as mentioned above.

    ![Alt text](./images/vgpu-deployment.png)
