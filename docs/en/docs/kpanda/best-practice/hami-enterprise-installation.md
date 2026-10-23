# HAMi Enterprise Installation and Configuration Guide

This article introduces how to install and configure HAMi (Heterogeneous AI Computing Virtualization Middleware) Enterprise Edition on the DCE platform to enable GPU virtualization functionality.

!!! note

    This article applies to enterprise users who have deployed DCE platform and need to enable GPU virtualization to support multi-container shared GPU resources.
    HAMi Enterprise Edition provides more powerful GPU resource management and virtualization capabilities. For more details, refer to [HAMi Project Website](https://project-hami.io).

## Prerequisites

Before installing HAMi Enterprise Edition, ensure the following conditions are met:

### System Requirements

- DCE platform successfully deployed
- Kubernetes cluster version 1.20 or higher
- At least one node with GPU configured in the cluster (this article takes NVIDIA GPU cards as an example)
- Have cluster administrator permissions

### GPU Hardware Requirements

- Recommended NVIDIA GPU cards (CUDA supported), refer to [HAMi Enterprise Edition Supported GPU Types](https://project-hami.io/docs/userguide/Device-supported).
- GPU driver correctly installed
- Hardware architecture supporting GPU virtualization

!!! warning

    Before starting installation, ensure important data is backed up and the installation process is verified in a test environment.

## Obtain the GPU UUID

Before installing HAMi Enterprise Edition, you need to obtain the UUID of the GPU device for license application. Depending on your environment configuration, you can choose one of the following two methods.

### Method 1: Obtain Directly on the Host (Recommended)

If the GPU driver is installed directly on the host, you can use the following command to obtain the GPU UUID:

```bash
# List all GPU devices and their UUIDs
nvidia-smi -L
```

The expected output is as follows:

```console
GPU 0: NVIDIA H800 (UUID: GPU-12345678-1234-1234-1234-123456789abc)
GPU 1: NVIDIA H800 (UUID: GPU-87654321-4321-4321-4321-cba987654321)
```

Extract the UUID information from the output:

```bash
# Display only the UUID
nvidia-smi -L | grep -oP 'UUID: \K[^)]*'
```

Expected output:

```console
GPU-12345678-1234-1234-1234-123456789abc
GPU-87654321-4321-4321-4321-cba987654321
```

### Method 2: Obtain Within a Container

If the GPU driver is not installed directly on the host, you need to mount the GPU device into a container to obtain the UUID:

```bash
# Create a temporary container and mount the GPU device
docker run --rm --gpus all nvidia/cuda:11.8-base-ubuntu20.04 nvidia-smi -L
```

Alternatively, use a Kubernetes Pod:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: gpu-uuid-checker
spec:
  containers:
    - name: cuda
      image: nvidia/cuda:11.8-base-ubuntu20.04
      command: ["nvidia-smi", "-L"]
      resources:
        limits:
          nvidia.com/gpu: 1
  restartPolicy: Never
```

Apply the Pod configuration and view the output:

```bash
# Create the Pod
kubectl apply -f gpu-uuid-checker.yaml

# View the Pod logs to obtain the UUID
kubectl logs gpu-uuid-checker

# Clean up the temporary Pod
kubectl delete pod gpu-uuid-checker
```

!!! tip

    It is recommended to record the UUIDs of all GPU devices, as this information will be used in the subsequent license application and configuration process.
    If you have multiple GPU nodes, you need to perform the above operations on each node separately.

## License Application and Management

HAMi Enterprise Edition requires a valid license to run properly. This section describes how to apply for and manage licenses.

### Apply for an Enterprise Edition License

1. **Prepare the GPU UUID Information**

   Use the GPU UUID information obtained in the previous section to prepare the device list required for the license application.

2. **Contact HAMi Technical Support**

   Apply for an Enterprise Edition license through the following methods:

   - Visit the [HAMi Project Website](https://project-hami.io) to obtain contact information
   - Provide the GPU UUID list and a description of your use case
   - Describe the expected GPU virtualization requirements

### Deploy the License File

The license of HAMi Enterprise Edition is built into the image, so no additional configuration is required for a basic installation. If you need to add licenses for other GPU devices, follow the steps below:

1. **Locate the License Directory**

    Find the license storage directory on each GPU node:

    ```bash
    # Run on the GPU node
    sudo mkdir -p /usr/local/vgpu
    ```

2. **Deploy the License File**

    Copy the obtained license file to the specified directory:

    ```bash
    # Copy the main license file
    sudo cp <license> /usr/local/vgpu/

    # Copy the device-specific license file (a single license can cover one or more devices applied for)
    sudo cp GPU-12345678-1234-1234-1234-123456789abc.lic /usr/local/vgpu/
    ```

## Install HAMi Enterprise Edition

This section describes how to remove the existing GPU Operator and install HAMi Enterprise Edition.

### Remove the Existing nvidia-vgpu Operator

Before installing HAMi Enterprise Edition, you need to remove the existing nvidia-vgpu Operator from the cluster to avoid conflicts.

Check for existing Operators, and uninstall them in a reasonable way if any exist.

```bash
# View existing GPU-related Operators
kubectl get pods -A | grep -i nvidia
kubectl get pods -A | grep -i vgpu
```

### Prepare the HAMi Enterprise Edition Installation Package

!!! note

    HAMi Enterprise Edition supports multiple installation methods. This article focuses on the image-based method. If you have other requirements, contact the delivery team for support.

1. **Obtain the Installation Package**

    Make sure you have obtained the `hami_commercial.tar` installation package file.

2. **Extract the Installation Package**

    ```bash
    # Extract the HAMi Enterprise Edition installation package
    tar -xvf hami_commercial.tar
    ```

### Deploy HAMi Enterprise Edition

Use the Helm command to deploy HAMi Enterprise Edition:

Use the `helm upgrade` command to update the installation package; note that you need to modify the `values.yaml` configuration:

- Change `resourceName` from `nvidia.com/gpu` to `nvidia.com/vgpu`
- Modify the images and versions required in the `Chart`, mainly involving:
    - /projecthami/jettech/kube-webhook-certgen
    - /projecthami/kube-webhook-certgen
    - /projecthami/hami:vX.Y.Z-commercial

```bash
helm upgrade --install hami-commercial ./ \
  -n hami-commercial \
  --create-namespace \
  -f ./values.yaml
```

The expected output during deployment is as follows:

```console
Release "hami-commercial" does not exist. Installing it now.
NAME: hami-commercial
LAST DEPLOYED: Mon Jan 15 10:30:00 2024
NAMESPACE: hami-commercial
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

### Verify the Deployment Status

1. **Check the Pod Status**

    ```bash
    # View the status of Pods related to HAMi Enterprise Edition
    kubectl -n hami-commercial get pod
    ```

    The expected output is as follows:

    ```console
    NAME                                READY   STATUS    RESTARTS   AGE
    hami-device-plugin-daemonset-xxxxx  1/1     Running   0          2m
    hami-scheduler-xxxxx                1/1     Running   0          2m
    hami-webhook-xxxxx                  1/1     Running   0          2m
    ```

!!! note

    After the deployment is complete, HAMi Enterprise Edition automatically starts managing GPU resources in the cluster.
    The original `nvidia.com/gpu` resources are converted into `nvidia.com/vgpu` resources.

## Switch the Node GPU Mode

After HAMi Enterprise Edition is deployed, some follow-up configuration is required to ensure the system runs properly.

### Switch the GPU Mode in the Container Management UI

1. **Log In to the DCE Management UI**

    Log in to the DCE platform web management UI with an administrator account.

2. **Go to the Container Management Module**

    Navigate to __Container Management__ -> __Clusters__ -> select the target cluster.

3. **Switch the GPU Mode**

    On the cluster details page:

    - Locate the __Nodes__ option
    - Select the node that contains a GPU
    - Locate the __GPU Configuration__ option in the node details
    - Switch the GPU mode from `GPU` to `vGPU`
    - Save the configuration changes

4. **Confirm the Mode Switch**

    After the switch is complete, you can confirm on the node details page that the GPU mode has changed to `vGPU`.

### Verify the System Configuration

1. **Check the GPU Resources**

    Verify that the GPU resources have been correctly converted into vGPU resources:

    ```bash
    # View the GPU resources of the node
    kubectl describe nodes | grep -A 5 -B 5 "nvidia.com/vgpu"
    ```

    The expected output should show `nvidia.com/vgpu` resources instead of `nvidia.com/gpu`.

2. **Verify the Device Plugin Status**

    ```bash
    # Check whether the device plugin is running properly
    kubectl -n hami-commercial get pods -l app=hami-device-plugin
    ```

3. **View System Events**

    ```bash
    # View related system events
    kubectl get events -n hami-commercial --sort-by='.lastTimestamp'
    ```

## Verification and Testing

After completing the installation of HAMi Enterprise Edition, you can create a test application to verify whether the GPU virtualization functionality works properly.

### Create a vGPU Test Application

1. **Create the Test Application Configuration File**

    Create a test application that uses vGPU resources:

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: vgpu-test-app
      namespace: default
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: vgpu-test-app
      template:
        metadata:
          labels:
            app: vgpu-test-app
        spec:
          containers:
            - name: pytorch-container
              image: release.daocloud.io/zestu/pytorch:2.5.1-cuda12.4-cudnn9-runtime
              command: ["sleep", "3600"]
              resources:
                limits:
                  nvidia.com/vgpu: 1 # Request 1 vGPU
                  nvidia.com/gpumem: 4096 # Request 4 GB of GPU memory
                  nvidia.com/gpucores: 50 # Request 50% of the GPU computing power
                requests:
                  nvidia.com/vgpu: 1
                  nvidia.com/gpumem: 4096
                  nvidia.com/gpucores: 50
          nodeSelector:
            gpu: "on"
    ```

2. **Deploy the Test Application**

    ```bash
    # Apply the test configuration
    kubectl apply -f vgpu-test-app.yaml
    ```

### Verify GPU Resource Allocation

1. **Enter the Test Container**

    ```bash
    # Enter the test container
    kubectl exec -it deployment/vgpu-test-app -- bash
    ```

2. **Check GPU Visibility**

    Run the following commands inside the container:

    ```bash
    # Check the CUDA devices
    nvidia-smi

    # Check the GPU memory limits
    nvidia-smi --query-gpu=memory.total,memory.used,memory.free --format=csv
    ```

    The expected output should show the allocated 4 GB GPU memory limit.

3. **Verify the GPU Computing Power Limit**

    ```bash
    # Check the GPU utilization limit
    nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits
    ```

### Verify the GPU Memory

To verify GPU memory allocation and usage in more detail, you can use the following Python script for testing.

#### Create the Verification Script

Create a Python script named `use_3gb_gpu_for_5min.py`:

```python
#!/usr/bin/env python3
"""
HAMi Enterprise Edition GPU memory verification script
This script is used to verify GPU memory allocation and usage in a vGPU environment
"""
import torch
import time

def use_3_5gb_gpu_for_5min():
    print("CUDA available:", torch.cuda.is_available())
    print("CUDA device count:", torch.cuda.device_count())

    for i in range(torch.cuda.device_count()):
        print(f"Allocating memory on GPU {i}...")
        device = torch.device(f"cuda:{i}")
        # Obtain the memory size of the current GPU
        total_memory = torch.cuda.get_device_properties(device).total_memory
        print(f"Total memory on GPU {i}: {total_memory / (1024 ** 3):.2f} GB")

        # Set the target memory usage to 3.5 GB
        target_memory = 3.5 * (1024 ** 3)  # 3.5 GB
        print(f"Target memory to allocate: {target_memory / (1024 ** 3):.2f} GB")

        allocated_memory = 0
        tensors = []
        while allocated_memory < target_memory:
            tensor = torch.empty(1024, 1024, device=device)
            allocated_memory += tensor.storage().nbytes()
            tensors.append(tensor)
            print(f"Allocated {allocated_memory / (1024 ** 3):.2f} GB on GPU {i}")

        print(f"GPU {i} is now filled with approximately 3.5GB of tensors.")

        # Set the running duration to 5 minutes
        run_time = 5 * 60  # 5 minutes
        print(f"Running for {run_time / 60:.2f} minutes...")
        start_time = time.time()

        while time.time() - start_time < run_time:
            # Simple computation can be added here to keep the GPU active
            torch.cuda.synchronize(device)
            time.sleep(1)  # Synchronize once per second to avoid excessive CPU usage

        print(f"Finished running for {run_time / 60:.2f} minutes.")
        print(f"Releasing memory on GPU {i}...")
        del tensors
        torch.cuda.empty_cache()
        print(f"Memory released on GPU {i}.")

if __name__ == "__main__":
    use_3_5gb_gpu_for_5min()
```

## Next Steps

After the installation of HAMi Enterprise Edition is complete, you can:

- Deploy applications that require GPU resources in the production environment
- Configure more complex GPU resource allocation policies
- Monitor GPU resource usage and performance metrics
- Scale GPU nodes according to business requirements

!!! success

    Congratulations! You have successfully completed the installation and configuration of HAMi Enterprise Edition.
    You can now make full use of the GPU virtualization capability to improve GPU resource utilization and management efficiency.

## Related References

- [HAMi Project Website](https://project-hami.io) - The official website and documentation of the HAMi project
