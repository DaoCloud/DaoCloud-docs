# Using NVIDIA vGPU in Applications

This section explains how to use the vGPU capability in the DCE 5.0 platform.

## Prerequisites

- The nodes in the cluster have GPUs of the corresponding models.
- vGPU Addon has been successfully installed. Refer to [Installing GPU Addon](vgpu_addon.md) for details.
- GPU Operator is installed, and the `Nvidia.DevicePlugin` capability is **disabled**. Refer to [Offline Installation of GPU Operator](../install_nvidia_driver_of_operator.md) for details.

## Procedure

### Using vGPU through the UI

1. Confirm if the cluster has detected the GPU cards. Click the corresponding `Cluster` -> `Cluster Settings` -> `Addon Plugins` and check if the GPU plugin has been automatically enabled and the corresponding GPU type has been detected. Currently, the cluster will automatically enable the `GPU` addon and set the `GPU Type` as `Nvidia vGPU`.

    

2. Deploy a workload by clicking on the corresponding `Cluster` -> `Workloads`. When deploying a workload using an image, select the type `Nvidia vGPU`, and you will be prompted with the following parameters:

    - **Number of Physical Cards (nvidia.com/vgpu)**: Indicates how many physical cards need to be mounted by the current pod. The input value must be an integer and **less than or equal to** the number of cards on the host machine.
    - **GPU Cores (nvidia.com/gpucores)**: Indicates the GPU cores utilized by each card, with a value range from 0 to 100. 
      Setting it to 0 means no enforced isolation, while setting it to 100 means exclusive use of the entire card.
    - **GPU Memory (nvidia.com/gpumem)**: Indicates the GPU memory occupied by each card, with a value in MB. The minimum value is 1, and the maximum value is the total memory of the card.

    > If there are issues with the configuration values above, it may result in scheduling failure or inability to allocate resources.



### Using vGPU through YAML Configuration

Refer to the following workload configuration and add the parameter `nvidia.com/vgpu: '1'` in the resource requests and limits section to configure the number of physical cards used by the application.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: full-vgpu-demo
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      app: full-vgpu-demo
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: full-vgpu-demo
    spec:
      containers:
        - name: full-vgpu-demo1
          image: chrstnhntschl/gpu_burn
          resources:
            limits:
              nvidia.com/gpucores: '20'   # Request 20% of GPU cores for each card
              nvidia.com/gpumem: '200'   # Request 200MB of GPU memory for each card
              nvidia.com/vgpu: '1'   # Request 1 GPU card
          imagePullPolicy: Always
      restartPolicy: Always
```

This YAML configuration requests the application to use vGPU resources. It specifies that each card should utilize 20% of GPU cores, 200MB of GPU memory, and requests 1 GPU card.
