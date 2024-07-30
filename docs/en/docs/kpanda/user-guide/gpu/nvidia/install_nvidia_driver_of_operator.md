---
MTPE: Fan-Lin
Date: 2024-01-24
---

# Offline Install GPU Operator

DCE 5.0 comes with pre-installed `driver` images for the following three operating systems: Ubuntu 22.04, Ubuntu 20.04,
and CentOS 7.9. The driver version is `535.104.12`. Additionally, it includes the required `Toolkit` images for each
operating system, so users no longer need to manually provide offline `toolkit` images.

!!! note

    After installation, switching from MIG mode to full-card mode or vGPU mode is not supported.
    Only one-click switching between full-card mode and vGPU mode is supported. Please plan your usage mode in advance.

Refer to [NVIDIA GPU Card Usage Modes](index.md) for more details. This article demonstrates the installation
using AMD architecture on CentOS 7.9 (3.10.0-1160). If you want to deploy on Red Hat 8.4, refer to
[Uploading Red Hat GPU Operator Offline Images to Bootstrap Nodes](./push_image_to_repo.md) and
[Building Red Hat 8.4 Offline Yum Repository](./upgrade_yum_source_redhat8_4.md).

## Prerequisites

1. The user has already installed addon offline package v0.12.0 or above on the platform.
2. The kernel versions of the nodes in the cluster, where GPU Operator will be deployed, must be identical.
   The distribution and GPU card models should be within the scope of the [GPU Support Matrix](../gpu_matrix.md).

## Steps

To install the GPU Operator plugin for your cluster, follow these steps:

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
- __Version__ : Plugin version, for example, __23.6.10__
- __Wait__ : When enabled, all associated resources must be in a ready state for the application installation to be marked as successful
- __Deletion failed__ : If the installation fails, delete the already installed associated resources. By enabling this, __Wait__ is automatically enabled
- __Detail Logs__ : When enabled, detailed logs of the installation process will be recorded

### Advanced settings

#### Operator parameters

1. __InitContainer.image__ : Configure the CUDA image, recommended default image: __nvidia/cuda__
2. __InitContainer.repository__ : Repository where the CUDA image is located, defaults to __nvcr.m.daocloud.io__ repository
3. __InitContainer.version__ : Version of the CUDA image, please use the default parameter

#### Driver parameters

1. __Driver.enable__ : Configure whether to deploy the NVIDIA driver on the node, default is enabled. If you have already deployed the NVIDIA driver on the node before using the GPU Operator, please disable this.
2. __Driver.image__ : Configure the GPU driver image, recommended default image: __nvidia/driver__ .
3. __Driver.repository__ : Repository where the GPU driver image is located, default is nvidia's __nvcr.io__ repository.
4. __Driver.usePrecompiled__ : Enable the precompiled mode to install the driver.
5. __Driver.version__ : Version of the GPU driver image, use default parameters for offline deployment.
   Configuration is only required for online installation. Different versions of the Driver image exist for
   different types of operating systems. For more details, refer to
   [Nvidia GPU Driver Versions](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/driver/tags).
   Examples of `Driver Version` for different operating systems are as follows:

    !!! note

        The system provides the image 525.147.05-centos7 by default. For other images, refer to
        [Upload Image to Bootstrap Node Repository](./push_image_to_repo).
        There is no need to include the operating system name such as Ubuntu, CentOS, Red Hat at the end of the version number. If the official image contains an operating system suffix, manually remove it.

        - For Red Hat systems, for example, `525.105.17`
        - For Ubuntu systems, for example, `535-5.15.0-1043-nvidia`
        - For CentOS systems, for example, `525.147.05`

6. __Driver.RepoConfig.ConfigMapName__ : Used to record the name of the offline yum repository configuration file
   for the GPU Operator. When using the pre-packaged offline bundle, refer to the following documents for
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
