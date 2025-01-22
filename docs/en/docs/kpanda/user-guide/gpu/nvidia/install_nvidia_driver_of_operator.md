---
MTPE: Fan-Lin
Date: 2024-01-24
---

# Offline Install gpu-operator

DCE 5.0 comes with pre-installed `driver` images for the following three operating systems: Ubuntu 22.04, Ubuntu 20.04,
and CentOS 7.9. The driver version is `535.104.12`. Additionally, it includes the required `Toolkit` images for each
operating system, so users no longer need to manually provide offline `toolkit` images.

This page demonstrates using AMD architecture with CentOS 7.9 (3.10.0-1160). If you need to deploy on Red Hat 8.4, refer to
[Uploading Red Hat gpu-operator Offline Image to the Bootstrap Node Repository](./push_image_to_repo.md)
and [Building Offline Yum Source for Red Hat 8.4](./upgrade_yum_source_redhat8_4.md).

## Prerequisites

- The kernel version of the cluster nodes where the gpu-operator is to be deployed must be
  completely consistent. The distribution and GPU card model of the nodes must fall within
  the scope specified in the [GPU Support Matrix](../gpu_matrix.md).
- The user has already installed v0.20.0 or above of the
  [addon offline package](../../../../download/addon/history.md) on the platform
  (Addon has supported installing the gpu-operator since v0.12, but the gpu-operator only has built-in support for CentOS 7.9).
- When installing the gpu-operator, select v23.9.0+2 or above.

## Steps

To install the gpu-operator plugin for your cluster, follow these steps:

1. Log in to the platform and go to __Container Management__ -> __Clusters__ , check cluster eetails.

2. On the __Helm Charts__ page, select __All Repositories__ and search for __gpu-operator__ .

3. Select __gpu-operator__ and click __Install__ .

4. Configure the installation parameters for __gpu-operator__ based on the instructions below to complete the installation.

## Configure parameters

- __systemOS__ : Select the operating system for the host. The current options are
  `Ubuntu 22.04`, `Ubuntu 20.04`, `Centos 7.9`, and `other`. Please choose the correct operating system.

### Basic information

- __Name__ : Enter the plugin name
- __Namespace__ : Select the namespace for installing the plugin
- **Version**: The version of the plugin. Here, we use version **v23.9.0+2** as an example.
- **Failure Deletion**: If the installation fails, it will delete the already installed associated
  resources. When enabled, **Ready Wait** will also be enabled by default.
- **Ready Wait**: When enabled, the application will be marked as successfully installed only
  when all associated resources are in a ready state.
- **Detailed Logs**: When enabled, detailed logs of the installation process will be recorded.

### Advanced settings

#### Operator parameters

- __InitContainer.image__ : Configure the CUDA image, recommended default image: __nvidia/cuda__
- __InitContainer.repository__ : Repository where the CUDA image is located, defaults to __nvcr.m.daocloud.io__ repository
- __InitContainer.version__ : Version of the CUDA image, please use the default parameter

#### Driver parameters

- __Driver.enable__ : Configure whether to deploy the NVIDIA driver on the node, default is enabled. If you have already deployed the NVIDIA driver on the node before using the gpu-operator, please disable this.
- __Driver.image__ : Configure the GPU driver image, recommended default image: __nvidia/driver__ .
- __Driver.repository__ : Repository where the GPU driver image is located, default is nvidia's __nvcr.io__ repository.
- __Driver.usePrecompiled__ : Enable the precompiled mode to install the driver.
- __Driver.version__ : Version of the GPU driver image, use default parameters for offline deployment.
   Configuration is only required for online installation. Different versions of the Driver image exist for
   different types of operating systems. For more details, refer to
   [Nvidia GPU Driver Versions](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/driver/tags).
   Examples of `Driver Version` for different operating systems are as follows:

    !!! note

        When using the built-in operating system version, there is no need to modify the image version. For other operating system versions, please refer to [Uploading Images to the Bootstrap Node Repository](./push_image_to_repo.md).
        note that there is no need to include the operating system name such as Ubuntu, CentOS, or Red Hat in the version number. If the official image contains an operating system suffix, please manually remove it.

        - For Red Hat systems, for example, `525.105.17`
        - For Ubuntu systems, for example, `535-5.15.0-1043-nvidia`
        - For CentOS systems, for example, `525.147.05`

- __Driver.RepoConfig.ConfigMapName__ : Used to record the name of the offline yum repository configuration file
   for the gpu-operator. When using the pre-packaged offline bundle, refer to the following documents for
   different types of operating systems.

    - [Building CentOS 7.9 Offline Yum Repository](./upgrade_yum_source_centos7_9.md)
    - [Building Red Hat 8.4 Offline Yum Repository](./upgrade_yum_source_redhat8_4.md)

#### Toolkit parameters

__Toolkit.enable__ : Enabled by default. This component allows containerd/docker
to support running containers that require GPUs.

#### MIG parameters

For detailed configuration methods, refer to [Enabling MIG Functionality](mig/create_mig.md).

**MigManager.Config.name** : The name of the MIG split configuration file, used to define the MIG (GI, CI)
split policy. The default is __default-mig-parted-config__ . For custom parameters, refer to
[Enabling MIG Functionality](mig/create_mig.md).

### Next Steps

After completing the configuration and creation of the above parameters:

- If using **full-card mode** , [GPU resources can be used when creating applications](full_gpu_userguide.md).

- If using **vGPU mode** , after completing the above configuration and creation,
  proceed to [vGPU Addon Installation](vgpu/vgpu_addon.md).

- If using **MIG mode** and you need to use a specific split specification for individual GPU nodes,
  otherwise, split according to the __default__ value in `MigManager.Config`.

    - For **single** mode, add label to nodes as follows:

        ```sh
        kubectl label nodes {node} nvidia.com/mig.config="all-1g.10gb" --overwrite
        ```

    - For **mixed** mode, add label to nodes as follows:

        ```sh
        kubectl label nodes {node} nvidia.com/mig.config="custom-config" --overwrite
        ```

    After spliting, applications can [use MIG GPU resources](mig/mig_usage.md).
