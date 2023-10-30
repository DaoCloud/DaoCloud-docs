# GPU Quota Management

This section describes how to use vGPU capabilities on the DCE 5.0 platform.

## Prerequisites

The corresponding GPU driver (NVIDIA GPU, NVIDIA MIG, Days, Ascend) has been deployed on the current cluster either through an Operator or manually.

## Procedure

Follow these steps to manage GPU quotas in DCE 5.0:

1. Go to Namespaces and click `Quota Management` to configure the GPU resources that can be used by a specific namespace.

    

2. The currently supported card types for quota management in a namespace are: NVIDIA vGPU, NVIDIA MIG, Days, and Ascend.

   - **NVIDIA vGPU Quota Management**: Configure the specific quota that can be used. This will create a ResourcesQuota CR.

        - Physical Card Count (nvidia.com/vgpu): Indicates the number of physical cards that the current pod needs to mount. The input value must be an integer and **less than or equal to** the number of cards on the host machine.
        - GPU Core Count (nvidia.com/gpucores): Indicates the GPU compute power occupied by each card. The value ranges from 0 to 100. If configured as 0, it is considered not to enforce isolation. If configured as 100, it is considered to exclusively occupy the entire card.
        - GPU Memory Usage (nvidia.com/gpumem): Indicates the amount of GPU memory occupied by each card. The value is in MB, with a minimum value of 1 and a maximum value equal to the entire memory of the card.

    
