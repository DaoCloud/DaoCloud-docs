# GPU Resource Dynamic Regulation

GPU resource dynamic adjustment is provided, allowing you to adjust already allocated vGPU resources in real time and dynamically without reloading, resetting, or restarting the entire running environment.
This feature is designed to minimize the impact on business operations, ensure that your business can continue to run stably, and flexibly adjust GPU resources according to actual needs.

## Use Cases

- **Elastic Resource Allocation**: When business needs or workloads change, GPU resources can be adjusted quickly to meet new performance requirements.
- **Instant Response**: When facing sudden high loads or business needs, GPU resources can be increased rapidly without interrupting business operations, ensuring service stability and performance.

## Procedure

The following is a specific operation example showing how to dynamically adjust the computing power and memory of a vGPU without restarting the vGPU Pod:

### Create a vGPU Pod

First, use the following YAML to create a vGPU Pod, whose computing power is initially unlimited and whose memory limit is 200 MB.

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

Check the GPU resource allocation in the `Pod` before adjustment:

![gpu-dynamic-regulation-before.png](./images/gpu-dynamic-regulation-before.png)

### Dynamically Adjust the Computing Power

If you need to change the computing power to 10%, follow the steps below:

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

    The program will take effect. Note that you must not exit the current Bash terminal.

### Dynamically Adjust the Memory

If you need to change the memory to 300 MB, follow the steps below:

1. Enter the container:

    ```bash
    kubectl exec -it <pod-name> -- /bin/bash
    ```

1. Execute the following commands to set the memory limit:

    ```bash
    export CUDA_DEVICE_MEMORY_LIMIT_0=300m
    export CUDA_DEVICE_MEMORY_SHARED_CACHE=/usr/local/vgpu/d.cache
    ```

    !!! note

        Each time you change the memory size, the file name `d.cache` needs to be changed, for example to `a.cache`, `1.cache`, etc., to avoid cache conflicts.

1. Run directly in the current terminal:

    ```bash
    ./gpu_burn 60
    ```

    The program will take effect. Likewise, you must not exit the current Bash terminal.

Check the GPU resource allocation in the `Pod` after adjustment:

![gpu-dynamic-regulation-after.png](./images/gpu-dynamic-regulation-after.png)

Through the above steps, you can dynamically adjust the computing power and memory of a vGPU Pod without restarting it, thereby meeting business needs more flexibly and optimizing resource utilization.
