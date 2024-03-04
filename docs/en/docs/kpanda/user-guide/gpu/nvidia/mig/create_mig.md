---
MTPE: Fan-Lin
Date: 2024-01-23
---

# Enabling MIG Function

This section describes how to enable NVIDIA MIG function. NVIDIA currently provides two strategies for exposing MIG devices on Kubernetes nodes:

- **Single mode** : Nodes expose a single type of MIG device on all their GPUs.
- **Mixed mode** : Nodes expose a mixture of MIG device types on all their GPUs.

!!! tip

    After disabling MIG mode, the physical node needs to be restarted in order to use the whole card mode properly.

For more details, refer to the [NVIDIA GPU Card Usage Modes](../index.md).

## Prerequisites

- Check the system requirements for the GPU driver installation on the target node: [GPU Support Matrix](../../gpu_matrix.md)
- Ensure that the cluster nodes have GPUs of the corresponding models
  ([NVIDIA H100](https://www.nvidia.com/en-us/data-center/h100/),
  [A100](https://www.nvidia.com/en-us/data-center/a100/),
  and [A30](https://www.nvidia.com/en-us/data-center/products/a30-gpu/) Tensor Core GPUs).
  For more information, see the [GPU Support Matrix](gpu_matrix.md).
- All GPUs on the nodes must belong to the same product line (e.g., A100-SXM-40GB).

## Enable GPU MIG single mode

1. [Enable MIG Single mode](../install_nvidia_driver_of_operator.md) through the Operator. Configure the parameters in the installation interface:

2. After the installation is complete, it is necessary to label the corresponding node (the node where the GPU card is inserted) with the partitioning specifications. If this step is not executed, it will default to no partitioning.

    !!! tip

        The Single mode can only be partitioned in a single mode. It is recommended to use the default strategy, but you can also [customize the partitioning strategy](#_2).

    **UI Configuration**:

    1. Search for `default-mig-parted-config` in the ConfigMap, enter the details, and find the partitioning specifications corresponding to the GPU card model.


    2. Find the corresponding node, select __Modify Labels__, and add __nvidia.com/mig.config="all-1g.10gb"__. If you choose another specification, then partition according to that specification.

        ![single02](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/user-guide/gpu/images/single02.jpg)

    **CLI Configuration**:

    ```sh
    kubectl label nodes {node} nvidia.com/mig.config="all-1g.10gb" --overwrite
    ```

3. Check the configuration result:

    ```sh
    kubectl get node 10.206.0.17 -o yaml|grep nvidia.com/mig.config
    ```

After the setup is complete, you can confirm the deployment of the application and then [use GPU MIG resources](mig_usage.md).

## Enable GPU MIG Mixed mode

1. [Enable MIG Mixed mode](../install_nvidia_driver_of_operator.md) through the Operator.
   Configure the parameters in the installation interface:

    ![mixed](../../images/mixed.png)

    - Set __DevicePlugin__ to __enable__
    - Set __MIG strategy__ to __mixed__
    - Enable the __enabled__ parameter under __Mig Manager__
    - Set __MigManager Config__ to the default MIG partitioning strategy __default-mig-parted-config__ ,
      or customize the partitioning strategy configuration file.

1. After the installation is complete, it is necessary to label the corresponding node (the node where the GPU card is inserted) with the partitioning specifications. If this step is not executed, it will default to no partitioning.

    !!! tip

        It is recommended to use the default strategy, but you can also [customize the partitioning strategy](#_2).

    **UI Configuration**:

    1. Search for default-mig-parted-config in the ConfigMap, enter the details, and find the partitioning specifications corresponding to the GPU card model.

    2. Find the corresponding node, select __Modify Labels__, and add __nvidia.com/mig.config="all-1g.10gb"__. If you choose another specification, then partition according to that specification.

        ![single02](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/user-guide/gpu/images/single02.jpg)

    **CLI Configuration**:

    ```sh
    kubectl label nodes {node} nvidia.com/mig.config="all-1g.10gb" --overwrite
    ```

1. Check the configuration result

    ```sh
    kubectl get node 10.206.0.17 -o yaml|grep nvidia.com/mig.config
    ```

After the setup is complete, you can confirm the deployment of the application and then [use GPU MIG resources](mig_usage.md).

## Custom Partitioning Strategy

You can customize the partitioning strategy configuration file, with a maximum of 7 instances per card. This needs to be created before installing the GPU Operator and specified during installation with the ConfigMap name.

1. Create a custom partitioning strategy in the ConfigMap, which needs to be in the same namespace as the GPU operator during deployment. The file name you create cannot be the same as the default __default-mig-parted-config__. The configuration data can be referenced in the following YAML.


    ??? note "Click to view detailed YAML configuration instructions"

        The following YAML is an example of a custom configuration named __custom-mig-parted-config__. The key in the configuration data is as shown in the content of __config.yaml__ below, and you can customize and add other partitioning strategies.

        ```yaml title="config.yaml"
          ## Custom split GI instance configuration
          version: v1
          mig-configs:
            all-disabled:
              - devices: all
                mig-enabled: false

            # A100-40GB, A800-40GB
              all-1g.5gb:
                - devices: all
                  mig-enabled: true
                  mig-devices:
                    "1g.5gb": 7

            all-1g.5gb.me:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "1g.5gb+me": 1

            all-2g.10gb:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "2g.10gb": 3

            all-3g.20gb:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "3g.20gb": 2

            all-4g.20gb:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "4g.20gb": 1

            all-7g.40gb:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "7g.40gb": 1

            # H100-80GB, H800-80GB, A100-80GB, A800-80GB, A100-40GB, A800-40GB
            all-1g.10gb:
              # H100-80GB, H800-80GB, A100-80GB, A800-80GB
              - device-filter: ["0x233010DE", "0x233110DE", "0x232210DE", "0x20B210DE", "0x20B510DE", "0x20F310DE", "0x20F510DE"]
                devices: all
                mig-enabled: true
                mig-devices:
                  "1g.10gb": 7

              # A100-40GB, A800-40GB
              - device-filter: ["0x20B010DE", "0x20B110DE", "0x20F110DE", "0x20F610DE"]
                devices: all
                mig-enabled: true
                mig-devices:
                  "1g.10gb": 4

            # H100-80GB, H800-80GB, A100-80GB, A800-80GB
            all-1g.10gb.me:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "1g.10gb+me": 1

            # H100-80GB, H800-80GB, A100-80GB, A800-80GB
            all-1g.20gb:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "1g.20gb": 4

            all-2g.20gb:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "2g.20gb": 3

            all-3g.40gb:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "3g.40gb": 2

            all-4g.40gb:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "4g.40gb": 1

            all-7g.80gb:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "7g.80gb": 1

            # A30-24GB
            all-1g.6gb:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "1g.6gb": 4

            all-1g.6gb.me:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "1g.6gb+me": 1

            all-2g.12gb:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "2g.12gb": 2

            all-2g.12gb.me:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "2g.12gb+me": 1

            all-4g.24gb:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "4g.24gb": 1

            # H100 NVL, H800 NVL
            all-1g.12gb:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "1g.12gb": 7

            all-1g.12gb.me:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "1g.12gb+me": 1

            all-2g.24gb:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "2g.24gb": 3

            all-3g.47gb:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "3g.47gb": 2

            all-4g.47gb:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "4g.47gb": 1

            all-7g.94gb:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "7g.94gb": 1

            # H100-96GB, PG506-96GB
            all-3g.48gb:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "3g.48gb": 2

            all-4g.48gb:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "4g.48gb": 1

            all-7g.96gb:
              - devices: all
                mig-enabled: true
                mig-devices:
                  "7g.96gb": 1

            # H100-96GB, H100 NVL, H800 NVL, H100-80GB, H800-80GB, A800-40GB, A800-80GB, A100-40GB, A100-80GB, A30-24GB, PG506-96GB
            all-balanced:
              # H100 NVL, H800 NVL
              - device-filter: ["0x232110DE", "0x233A10DE"]
                devices: all
                mig-enabled: true
                mig-devices:
                  "1g.12gb": 1
                  "2g.24gb": 1
                  "3g.47gb": 1

              # H100-80GB, H800-80GB, A100-80GB, A800-80GB
              - device-filter: ["0x233010DE", "0x233110DE", "0x232210DE", "0x20B210DE", "0x20B510DE", "0x20F310DE", "0x20F510DE"]
                devices: all
                mig-enabled: true
                mig-devices:
                  "1g.10gb": 2
                  "2g.20gb": 1
                  "3g.40gb": 1

              # A100-40GB, A800-40GB
              - device-filter: ["0x20B010DE", "0x20B110DE", "0x20F110DE", "0x20F610DE"]
                devices: all
                mig-enabled: true
                mig-devices:
                  "1g.5gb": 2
                  "2g.10gb": 1
                  "3g.20gb": 1

              # A30-24GB
              - device-filter: "0x20B710DE"
                devices: all
                mig-enabled: true
                mig-devices:
                  "1g.6gb": 2
                  "2g.12gb": 1

              # H100-96GB, PG506-96GB
              - device-filter: ["0x233D10DE", "0x20B610DE"]
                devices: all
                mig-enabled: true
                mig-devices:
                  "1g.12gb": 2
                  "2g.24gb": 1
                  "3g.48gb": 1

           # After setting, the CI instance will be partitioned according to the set specifications 
            custom-config:    
              - devices: all
                mig-enabled: true
                mig-devices:
                  "1g.10gb": 4
                  "1g.20gb": 2

        ```

        Set __custom-config__ in the above __YAML__, and after setting, the __CI__ instance will be partitioned according to the specification.

        ```yaml
        custom-config:
             devices: all
            mig-enabled: true
            mig-devices:
              1c.3g.40gb: 6
        ```

1. Specify this ConfigMap during the installation of the GPU Operator.

