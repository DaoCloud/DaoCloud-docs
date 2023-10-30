# GPU Operator Offline Installation

DCE 5 provides a GPU Operator offline package with CentOS 7.9 and kernel version 3.10.0-1160 preinstalled. This article explains how to deploy the GPU Operator offline. This section covers parameter configurations for various usage modes of NVIDIA GPUs.

- GPU Full Mode
- GPU vGPU Mode
- GPU MIG Mode

For more details, please refer to [NVIDIA GPU Card Usage Modes](index.md). This article demonstrates the installation using AMD architecture on CentOS 7.9 (3.10.0-1160). If you want to deploy on RedHat 8.4, please refer to [Uploading RedHat GPU Operator Offline Images to Ignition Nodes](./push_image_to_repo.md) and [Building RedHat 8.4 Offline Yum Repository](./upgrade_yum_source_redhat8_4.md).

## Prerequisites

1. The user has already installed addon offline package v0.12.0 or above on the platform.
2. The kernel versions of the nodes in the cluster, where GPU Operator will be deployed, must be identical. The distribution and GPU card models should be within the scope of the [GPU Support Matrix](../gpu_matrix.md).

## Steps

Follow the steps below to install the GPU Operator plugin on the cluster.

1. Log in to the platform and go to `Container Management` --> `Cluster Details` of the cluster where GPU Operator will be installed.

2. On the `Helm Template` page, select `All Repositories` and search for `gpu-operator`.

3. Select `gpu-operator` and click `Install`.

4. Configure the installation parameters for `gpu-operator` based on the instructions below to complete the installation.

## Parameter Configuration

### Basic Parameter Configuration

- `Name`: Enter the plugin name.
- `Namespace`: Select the namespace for installing the plugin.
- `Version`: Plugin version, for example, `23.6.10`.
- `Ready-wait`: When enabled, all associated resources must be in a ready state for the application installation to be marked as successful.
- `Failure-delete`: If the installation fails, delete the already installed associated resources. By enabling this, `Ready-wait` is automatically enabled.
- `Detail Logs`: When enabled, detailed logs of the installation process will be recorded.

### Advanced Parameter Configuration

#### DevicePlugin Parameter Configuration

1. `DevicePlugin.enable`: Configure whether to enable the Kubernetes [DevicePlugin](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/) feature. Determine whether to enable it based on your use case.

    - Enable it for GPU Full mode.
    - Disable it for GPU vGPU mode.
    - Enable it for GPU MIG mode.

    !!! note

        Note:
        1. Only one GPU card mode can be used in a cluster, so before deploying the GPU Operator, please confirm the GPU card usage mode to decide whether to enable the `DevicePlugin` feature.
        2. When using vGPU mode (disabling this parameter), the daemon `nvidia-operator-validator` will remain in the "Waiting" state for a long time. This is normal and does not affect the use of vGPU functionality.

#### Driver Parameter Configuration

2. `Driver.enable`: Configure whether to deploy NVIDIA drivers on the nodes. It is enabled by default. If you have already deployed the NVIDIA driver on the nodes before using the GPU Operator, please disable it.

3. `Driver.image`: Configure the GPU driver image. The recommended default image is `nvidia/driver`.

4. `Driver.repository`: Configure the repository where the GPU driver image is located. The default repository is nvidia's `nvcr.io`.

5. `Driver.version`: Configure the version of the GPU driver image. For offline deployment, use the default parameters. Only configure this for online installation. The driver image versions for different operating systems have the following differences:

    - For RedHat systems, the naming convention is usually composed of the CUDA version and OS version. For example, if the kernel is `4.18.0-305.el8.x86_64`, the Driver.version value for RedHat 8.4 would be `525.105.17`.
    - For Ubuntu systems, the naming convention is `<driver-branch>-<linux-kernel-version>-<os-tag>`.
    For example, `525-5.15.0-69-ubuntu22.04`, where `525` is the CUDA version, `5.15.0-69` is the kernel version, and `ubuntu22.04` is the OS version.
    Note: For Ubuntu, the Driver image version must be strongly consistent with the node's kernel version, including minor version numbers.

    - For CentOS systems, the naming convention is usually composed of the CUDA version and the kernel version. For example, if the kernel is `3.10.0-1160`, the Driver.version value for CentOS 7.9 would be `465.19`.

6. `Driver.installKernelModule`: Configure whether to install the NVIDIA kernel module. It is enabled by default. If you have already installed the NVIDIA kernel module on the nodes before using the GPU Operator, please disable it.

6. `Driver.RepoConfig.ConfigMapName`: This parameter is used to record the name of the offline yum source configuration file for GPU Operator. When using the pre-installed offline package, refer to "Using the yum source configuration of any node in the Global cluster".

    ??? note "Using the yum source configuration of any node in the Global cluster"

        1. Use SSH or another method to access any node in the Global cluster and retrieve the platform's offline source configuration file `extension.repo`:

            ```bash
            cat /etc/yum.repos.d/extension.repo # View the contents of extension.repo.
            ```

            The expected output should look like this:

            ```bash
            [extension-0]
            async = 1
            baseurl = http://x.x.x.x:9000/kubean/centos/$releasever/os/$basearch
            gpgcheck = 0
            name = kubean extension 0

            [extension-1]
            async = 1
            baseurl = http://x.x.x.x:9000/kubean/centos-iso/$releasever/os/$basearch
            gpgcheck = 0
            name = kubean extension 1
            ```

        2. Copy the contents of the `extension.repo` file mentioned above. In the `gpu-operator` namespace of the cluster where GPU Operator will be deployed, create a new config map named `local-repo-config`. Refer to [Creating ConfigMaps](../../configmaps-secrets/create-configmap.md) for creating the config map.
        **Note: The `key` value must be `CentOS-Base.repo`, and the `value` value should contain the contents of the offline source configuration file `extension.repo`.**

    For other operating systems or kernels, refer to the following links to create the yum source file:

    - [Building CentOS 7.9 Offline Yum Source](./Upgrade_yum_source_of_preset_offline_package.md)

    - [Building RedHat 8.4 Offline Yum Source](./upgrade_yum_source_redhat_8.4.md)

7. **MIG Configuration Parameters**

    For detailed configuration, please refer to [Enabling MIG Functionality](mig/create_mig.md).

    - `MigManager.enabled`: Enable or disable MIG capability feature.
    - `Mig.strategy`: The strategy for exposing MIG devices on the GPU cards of the nodes. NVIDIA provides two strategies for exposing MIG devices (`single` and `mixed`). For more details, refer to [NVIDIA GPU Card Mode Explanation](index.md).
    - `MigManager.Config`: Used to configure MIG partitioning parameters and default values.
        - `default`: The default partitioning configuration used by nodes. It is set to `all-disabled` by default.
        - `name`: The name of the MIG partitioning configuration file that defines the (GI, CI) partitioning strategy for MIG. It is set to `default-mig-parted-config` by default. For custom parameters, refer to [Enabling MIG Functionality](mig/create_mig.md).

8. `Node-Feature-Discovery.enableNodeFeatureAPI`: Enable or disable the Node Feature API (Node Feature Discovery API).

     - When set to `true`, the Node Feature API is enabled.
     - When set to `false` or not set, the Node Feature API is disabled.

### Next Steps

After completing the parameter configurations and creations mentioned above:

1. If you are using **Full GPU mode**, follow the instructions in [Using GPU Resources in Application Creation](full_gpu_userguide.md).

2. If you are using **vGPU mode**, after completing the parameter configurations and creations mentioned above, proceed to [vGPU Addon Installation](vgpu/vgpu_addon.md).

3. If you are using **MIG mode** and need to allocate specific GPU nodes according to a certain partitioning specification, assign the following label to the corresponding node:

    - For **single** mode, assign the label as follows:

        ```sh
        kubectl label nodes {node} nvidia.com/mig.config="all-1g.10gb" --overwrite
        ```

    - For **mixed** mode, assign the label as follows:

        ```sh
        kubectl label nodes {node} nvidia.com/mig.config="custom-config" --overwrite
        ```

    After partitioning, applications can use [MIG GPU Resources](mig/mig_usage.md).
