# Creating MIG (Multi-Instance GPU) via GPU Operator

NVIDIA currently provides two strategies for exposing MIG devices on Kubernetes nodes:

- **Single mode**: Nodes only expose a single type of MIG device on all their GPUs. All GPUs on the node must:
    - Belong to the same model (e.g., A100-SXM-40GB), and only GPUs of the same model have the same MIG profile.
    - Have MIG configuration enabled, which requires a machine restart to take effect.
    - Create the same GI and CI to expose "identical" MIG device types across all products.

- **Mixed mode**: Nodes expose mixed MIG device types on all their GPUs. Requesting a specific MIG device type requires the number of compute slices and total memory provided by the device type.
    - All GPUs on the node must belong to the same product line (e.g., A100-SXM-40GB).
    - Each GPU can have MIG enabled or disabled and can be freely configured with a mixture of available MIG device types.
    - The k8s-device-plugin running on the node will:
        - Expose any GPUs not in MIG mode using the traditional [nvidia.com/gpu](http://nvidia.com/gpu) resource type.
        - Expose individual MIG devices using resource types following the pattern nvidia.com/mig-<slice_count>g.<memory_size>gb.

Note: Currently, GPU Operator only supports online deployment.

## Prerequisites

- Ensure that the cluster nodes have the corresponding model of GPUs ([NVIDIA H100](https://www.nvidia.com/en-us/data-center/h100/), [A100](https://www.nvidia.com/en-us/data-center/a100/), and [A30](https://www.nvidia.com/en-us/data-center/products/a30-gpu/) Tensor Core GPU).
- The cluster should have network connectivity.

## Enabling GPU MIG Single Mode

1. Enable MIG Single mode using the Operator:

    ```shell
    helm repo add nvidia https://helm.ngc.nvidia.com/nvidia
    helm repo update
    helm upgrade -i gpu-operator -n gpu-operator --create-namespace nvidia/gpu-operator --set migStrategy=single --set node-feature-discovery.image.repository=k8s.m.daocloud.io/nfd/node-feature-discovery --set driver.version=525-5.15.0-78-generic # Set MIG mode to 'single' using the 'set' command
    ```

2. Assign the partitioning specification to the corresponding node (the node with the inserted GPU card):

    ```shell
    kubectl label nodes {node} nvidia.com/mig.config="all-1g.10gb" --overwrite
    ```

3. Check the configuration result:

    ```shell
    kubectl get node 10.206.0.17 -o yaml | grep nvidia.com/mig.config
    ```

## Enabling GPU MIG Mixed Mode

1. Enable MIG Mixed mode using the Operator:

    ```shell
    helm repo add nvidia https://helm.ngc.nvidia.com/nvidia
    helm repo update
    helm install --generate-name --set migStrategy=mixed --set allowDefaultNamespace=true nvidia/nvidia-device-plugin --set node-feature-discovery.image.repository=k8s.m.daocloud.io/nfd/node-feature-discovery # Set MIG mode to 'mixed' using the 'set' command
    ```

2. Configure the `config.yaml` file to set the MIG GI instance partitioning specification.

    ```yaml
    version: v1
    mig-configs:
      all-disabled:
        - devices: all
          mig-enabled: false
      all-enabled:
        - devices: all
          mig-enabled: true
          mig-devices: {}
      all-1g.10gb:
        - devices: all
          mig-enabled: true
          mig-devices:
            1g.5gb: 7
      all-1g.10gb.me:
        - devices: all
          mig-enabled: true
          mig-devices:
            1g.10gb+me: 1
      all-1g.20gb:
        - devices: all
          mig-enabled: true
          mig-devices:
            1g.20gb: 4
      all-2g.20gb:
        - devices: all
          mig-enabled: true
          mig-devices:
            2g.20gb: 3
      all-3g.40gb:
        - devices: all
          mig-enabled: true
          mig-devices:
            3g.40gb: 2
      all-4g.40gb:
        - devices: all
          mig-enabled: true
          mig-devices:
            4g.40gb: 1
      all-7g.80gb:
        - devices: all
          mig-enabled: true
          mig-devices:
            7g.80gb: 1
      all-balanced:
        - device-filter: ["0x233110DE", "0x232210DE", "0x20B210DE", "0x20B510DE", "0x20F310DE", "0x20F510DE"]
          devices: all
          mig-enabled: true
          mig-devices:
            1g.10gb: 2
            2g.20gb: 1
            3g.40gb: 1
      custom-config:    # CI instances will be partitioned accordingly after configuration
        - devices: all
          mig-enabled: true
          mig-devices:
            3g.40gb: 2
    ```

3. Set the `custom-config` in the aforementioned `config.yaml`. After setting it, the CI instances will be partitioned according to the specifications.

    ```yaml title="config.yaml"
    custom-config:
      - devices: all
        mig-enabled: true
        mig-devices:
          1c.3g.40gb: 6
    ```

4. Customize the settings according to the modified `config.yaml`:

    ```sh
    kubectl create configmap -n gpu-operator custome-mig-parted-config --from-file=config.yaml
    helm install gpu-operator -n gpu-operator --create-namespace nvidia/gpu-operator --set migManager.config.name=mig-config --set node-feature-
    discovery.image.repository=k8s.m.daocloud.io/nfd/node-feature-discovery
    ···
    
    or
    
    ···sh
    helm upgrade -i gpu-operator nvidia/gpu-operator -n gpu-operator --set mig.strategy=mixed --set migManager.config.name=custome-mig-parted-config --set node-feature-discovery.image.repository=k8s.m.daocloud.io/nfd/node-feature-discovery
    ```

5. After completing the settings, assign the partitioning specifications to the corresponding node:

    ```sh
    kubectl label nodes {node} nvidia.com/mig.config="custom-config" --overwrite
    ```

6. Check the configuration result:

    ```sh
    kubectl get node 10.206.0.17 -o yaml | grep nvidia.com/mig.config
    ```

   Once the settings are applied, you can utilize the GPU MIG resources when deploying applications.
