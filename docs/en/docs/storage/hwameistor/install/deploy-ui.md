---
hide:
   - toc
---

# Install via interface

This page describes how to install Hwameistor through the platform interface.

## Prerequisites

- Free HDD and SSD disks have been prepared on the nodes to be used
- Completed the items in [Preparation](prereq.md)
- If you need to use highly available data volumes, please complete [DRDB installation](drbdinstall.md) in advance
- If the deployment environment is a production environment, please read [Resource Requirements for Production Environment](proresource.md) in advance
- If your Kubernetes distribution uses a different `kubelet` directory, please confirm `kubeletRootDir` in advance.
   For details, please refer to [Customize Kubelet root directory](customized-kubelet.md).

## Steps

Please confirm that your cluster has successfully connected to `container management` platform, and then perform the following steps to install Hwameistor.

1. On the left navigation bar, click `Container Management` —> `Cluster List`, and find the name of the cluster where Hwameistor is to be installed.

2. In the left navigation bar, select `Helm Apps` -> `Helm chart`, find and click `Hwameistor`.

3. In `Version Selection`, select the version you want to install, and click `Install`.

4. On the installation interface, fill in the required installation parameters. If you need to deploy a production environment, it is recommended to adjust the resource configuration: [Production environment resource requirements](proresource.md).

    - `Global Setting` —> `global container registry`:
    
        Set the registry addresses of all mirrors, and the available online registrys have been filled in by default.
        If it is a privatized environment, it can be modified to a private registry address.
       
    - `Global Setting` —> `K8s container registry`:
    
        Set the address of the K8S container registry, and the available online registry has been filled in by default.
        If the environment is privatized, it can be modified to a private registry address.
       
    - `Global Setting` —> `Kubelet Root Dir`:
    
        The default `kubelet` directory is `/var/lib/kubelet`.
        If your Kubernetes distribution uses a different `kubelet` directory, the parameter `kubeletRootDir` must be set.
        For details, please refer to [Customize Kubelet root directory](customized-kubelet.md).
       
    - `Config Settings` —> `DRDBStartPort`:
    
        The default starts with 43001. When `DRDB` is enabled, each time a highly available data volume is created, a set of ports on the node where the primary copy data volume is located needs to be occupied.
        Please complete [DRDB Installation](drbdinstall.md) before installation.
       
    - **Storage Class Configuration**
    
        After Hwameistor is deployed, Storage Class will be created automatically.
    
        - `AllowVolumeExpansion`: It is off by default. After it is turned on, the data volume created based on the Storage Class can be expanded.
        - `DiskType`: the disk type of the created StorageClass (Storage Class), supported types are: HDD, SSD. HDD is the default.
        - `Enable HA`: `HA` is turned off by default, that is, the created data volume is `non-highly available`, when enabled, use this `Storage Class`
        The created data volume can be set as `highly available data volume`. Please complete [DRDB Installation](drbdinstall.md) before opening.
        - `Replicas`: In non-HA mode, the number of `Replicas` is `1`; when the `HA` mode is enabled, the number of `Replicas` can be `1` or `2`, and the number is `1`, which can be converted to `2`.
        - `ReclaimPolicy`: When the data volume is deleted, the data retention policy, the default is `delete`.
       
            1. `Delete`: When deleting a data volume, the data is also deleted.
            2. `Retain`: When deleting a data volume, keep the data.
    
5. After the parameter input is complete, click `OK` to complete the creation. After the creation is complete, you can click `Helm Apps` to view the installation status of `Hwameistor`.
    
6. The installation is complete! To verify the installation effect, please refer to the next chapter [Post-check](./post-check.md).
