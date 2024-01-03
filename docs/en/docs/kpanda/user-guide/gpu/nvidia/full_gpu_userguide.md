# Using the Whole NVIDIA GPU Card for an Application

This section describes how to allocate the entire NVIDIA GPU card to a single application on the DCE 5.0 platform.

## Prerequisites

- DCE 5.0 container management platform has been [deployed](https://docs.daocloud.io/install/index.html) and is running properly.
- The container management module has been [connected to a Kubernetes cluster](../../clusters/integrate-cluster.md) or a Kubernetes cluster has been [created](../../clusters/create-cluster.md), and you can access the UI interface of the cluster.
- GPU Operator has been offline installed and NVIDIA DevicePlugin has been enabled on the current cluster. Refer to [Offline Installation of GPU Operator](install_nvidia_driver_of_operator.md) for instructions.
- The GPU card in the current cluster has not undergone any virtualization operations or been occupied by other applications.

## Procedure

### Configuring via the User Interface

1. Check if the cluster has detected the GPU cards. Click the corresponding __Clusters__ -> __Cluster Settings__ -> __Addon Plugins__ to see if it has automatically enabled and detected the corresponding GPU types.
   Currently, the cluster will automatically enable __GPU__ and set the __GPU Type__ as __Nvidia GPU__ .

    

2. Deploy a workload. Click the corresponding __Clusters__ -> __Workloads__ , and deploy the workload using the image method. After selecting the type ( __Nvidia GPU__ ), configure the number of physical cards used by the application:

    **Physical Card Count (nvidia.com/gpu)**: Indicates the number of physical cards that the current pod needs to mount. The input value must be an integer and **less than or equal to** the number of cards on the host machine.

    
    
    > If the above value is configured incorrectly, scheduling failures and resource allocation issues may occur.

### Configuring via YAML

To request GPU resources for a workload, add the __nvidia.com/gpu: 1__ parameter to the resource request and limit configuration in the YAML file. This parameter configures the number of physical cards used by the application.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: full-gpu-demo
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      app: full-gpu-demo
  template:
    metadata:
      labels:
        app: full-gpu-demo
    spec:
      containers:
      - image: chrstnhntschl/gpu_burn
        name: container-0
        resources:
          requests:
            cpu: 250m
            memory: 512Mi
            nvidia.com/gpu: 1   # Number of GPUs requested
          limits:
            cpu: 250m
            memory: 512Mi
            nvidia.com/gpu: 1   # Upper limit of GPU usage
      imagePullSecrets:
      - name: default-secret
```

!!! note

    When using the `nvidia.com/gpu` parameter to specify the number of GPUs, the values for requests and limits must be consistent.
