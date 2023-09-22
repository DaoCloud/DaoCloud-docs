# GPU Quota Management

This section describes how to use vGPU capabilities on the DCE 5.0 platform.

## Prerequisites

The cluster has already deployed the corresponding type of GPU driver (Nvidia GPU, Nvidia MIG, AMD, Ascend) either through the operator or manually.

## Procedure

1. Go to the Namespaces section and click `Quota Management` to configure the GPU resources that can be used by a specific namespace.

    ![Alt text](./images/cluster-ns.png)

2. The current namespace quota management covers the following card types: Nvidia vGPU, Nvidia MIG, AMD, Ascend.

    - **Nvidia vGPU Quota Management**: Configure the specific quotas that can be used. This will create a ResourcesQuota CR:

        - Physical Card Quantity (`nvidia.com/vgpu`): Specifies the number of physical cards that the current pod needs to mount, which should be less than or equal to the number of cards on the host machine.
        - GPU Cores (`nvidia.com/gpucores`): Represents the amount of GPU cores occupied by each card, with values ranging from 0 to 100. If configured as 0, it is considered non-isolated; if configured as 100, it is considered as exclusive access to the entire card.
        - GPU Memory (`nvidia.com/gpumem`): Represents the amount of GPU memory occupied by each card, with values in MB. The minimum value is 1, and the maximum value is the total memory capacity of the card.

    ![Alt text](./images/vgpu-quota.png)
