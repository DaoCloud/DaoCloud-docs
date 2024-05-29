# Dynamic Allocation of GPU Resources

This feature provides dynamic allocation of GPU resources, allowing you to make real-time changes to allocated vGPU resources without the need to reload, reset, or restart the entire runtime environment. The goal is to minimize the impact on business operations, ensuring continuous and stable operation while flexibly adjusting GPU resources based on actual needs.

## Use Cases

- **Elastic Resource Allocation** : Quickly adjust GPU resources to meet new performance requirements when business needs or workloads change.
- **Immediate Response** : Swiftly increase GPU resources in response to sudden high loads or business demands without interrupting operations, ensuring service stability and performance.

## Steps

Below is a specific operational example demonstrating how to dynamically adjust the compute and memory resources of a vGPU without restarting the vGPU Pod:

### Create a vGPU Pod

First, we create a vGPU Pod using the following YAML, with initial unlimited compute power and a memory limit of 200Mb.

```yaml
kind: Deployment
apiVersion: apps/v1
metadata:
  name: gpu-burn-test
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      app: gpu-burn-test
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: gpu-burn-test
    spec:
      containers:
        - name: container-1
          image: docker.io/chrstnhntschl/gpu_burn:latest
          command:
            - sleep
            - '100000'
          resources:
            limits:
              cpu: 1m
              memory: 1Gi
              nvidia.com/gpucores: '0'
              nvidia.com/gpumem: '200'
              nvidia.com/vgpu: '1'
```

### Dynamic Allocation of Compute Power

To modify the compute power to 10%, follow these steps:

1. Enter the container:

    ```bash
    kubectl exec -it <pod-name> -- /bin/bash
    ```
   
1. Execute:

    ```bash
    export CUDA_DEVICE_SM_LIMIT=10
    ```
   
1. Run directly in the current terminal:

    ```bash
    ./gpu_burn 60
    ```

    The program will take effect immediately. Note that you should not exit the current bash terminal.

### Dynamic Allocation of Memory

To modify the memory to 300Mb, follow these steps:

1. Enter the container:

    ```bash
    kubectl exec -it <pod-name> -- /bin/bash
    ```
   
1. Execute the following commands to set the memory limit:

    ```bash
    export CUDA_DEVICE_MEMORY_LIMIT_0=300m
    export CUDA_DEVICE_MEMORY_SHARED_CACHE=/usr/local/vgpu/d.cache
    ```
   
    **Note**: Each time you change the memory size, the `d.cache` file name needs to be changed, such as to `a.cache`, `1.cache`, etc., to avoid cache conflicts.
   
1. Run directly in the current terminal:

    ```bash
    ./gpu_burn 60
    ```

    The program will take effect immediately. Similarly, do not exit the current bash terminal.

By following these steps, you can dynamically adjust the compute and memory resources of a vGPU without restarting the vGPU Pod, thereby more flexibly meeting business needs and optimizing resource utilization.