---
MTPE: Fan-Lin
Date: 2024-01-24
---

# Install GPU Operator Offline

DCE 5.0 provides a GPU Operator offline package with CentOS 7.9 and kernel version 3.10.0-1160 preinstalled. This article explains how to deploy the GPU Operator offline. This section covers parameter configurations for various usage modes of NVIDIA GPUs.

- GPU Full Mode
- GPU vGPU Mode
- GPU MIG Mode

Please refer to [NVIDIA GPU Card Usage Modes](index.md) for more details. This article demonstrates the installation using AMD architecture on CentOS 7.9 (3.10.0-1160). If you want to deploy on Red Hat 8.4, refer to [Uploading Red Hat GPU Operator Offline Images to Bootstrap Nodes](./push_image_to_repo.md) and [Building Red Hat 8.4 Offline Yum Repository](./upgrade_yum_source_redhat8_4.md).

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
4. __Driver.version__ : Version of the GPU driver image, use default parameters for offline deployment.
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

5. __Driver.RepoConfig.ConfigMapName__ : Used to record the name of the offline yum source profile for the GPU Operator. When using pre-installed offline packages, the global cluster can directly run the following command. Worker clusters should refer to the yum source configuration of any node in the Global cluster.

    - Configuration for the global cluster

        ```sh
        kubectl create configmap local-repo-config  -n gpu-operator --from-file=CentOS-Base.repo=/etc/yum.repos.d/extension.repo
        ```
   
    - Configuration for the worker cluster

    ??? note "Using the yum source configuration of any node in the Global cluster"

        1. Use SSH or another method to access any node in the Global cluster and retrieve the platform's offline source profile __extension.repo__ :

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

        2. Copy the contents of the __extension.repo__ file mentioned above. In the __gpu-operator__ namespace of the cluster where GPU Operator will be deployed, create a new config map named __local-repo-config__ . Refer to [Creating ConfigMaps](../../configmaps-secrets/create-configmap.md) for creating the config map.

            !!! note

                The configuration __key__ value must be __CentOS-Base.repo__, and the __value__ should be the content of the offline source configuration file __extension.repo__.

    For other operating systems or kernels, refer to the following links to create the yum source file:

    - [Building CentOS 7.9 Offline Yum Source](./Upgrade_yum_source_of_preset_offline_package.md)
    - [Building Red Hat 8.4 Offline Yum Source](./upgrade_yum_source_redhat_8.4.md)

#### Toolkit Parameters

1. __Toolkit.enable__ : Default is enabled. This component enables containerd/docker to support running containers that require GPU.

2. __Toolkit.image__ : Configure the Toolkit image, recommended default image: __nvidia/k8s/container-toolkit__ .

3. __Toolkit.repository__ : Repository where the Toolkit image is located, defaults to __nvcr.m.daocloud.io__ repository.

4. __Toolkit.version__ : Version of the Toolkit image, keep the version consistent with the official website. By default, it uses the CentOS image. If using Ubuntu, you need to manually modify the yaml of the addon, changing CentOS to Ubuntu. Refer to [NVIDIA Container Toolkit](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/k8s/containers/container-toolkit/tags) for specific models.

#### MIG Parameters

For detailed configuration, refer to [Enabling MIG Functionality](mig/create_mig.md)

1. __MigManager.enabled__ : Whether to enable MIG capability feature.
2. **MigManager.Config.name** : Name of the MIG partitioning profile, used to
   define the (GI, CI) partitioning strategy for MIG. Default is __default-mig-parted-config__ .
   For custom parameters, refer to [Enabling MIG Functionality](mig/create_mig.md).
3. __Mig.strategy__ : Public strategy for MIG devices on GPU cards on the node. NVIDIA provides
   two policies for exposing MIG devices: __single__ , __mixed__ policies, details can be found
   in [NVIDIA GPU Card Mode Explanation](index.md).

#### Node-Feature-Discovery Parameters

__Node-Feature-Discovery.enableNodeFeatureAPI__ : Enable or disable the Node Feature API.

- When set to __true__ , the Node Feature API is enabled.
- When set to __false__ or not set, the Node Feature API is disabled.

### Next steps

After completing the parameter configurations and creations mentioned above:

1. If you are using **Full GPU mode** , follow the instructions in [Using GPU Resources in Application Creation](full_gpu_userguide.md).

2. If you are using **vGPU mode** , after completing the parameter configurations and creations mentioned above, proceed to [vGPU Addon Installation](vgpu/vgpu_addon.md).

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
