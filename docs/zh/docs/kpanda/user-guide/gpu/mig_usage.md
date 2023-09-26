# 使用 MIG GPU 资源

本节介绍应用如何使用 MIG GPU 资源。

## 前提条件

- 已经[部署 DCE 5.0](https://docs.daocloud.io/install/index.html) 容器管理平台，且平台运行正常。
- 容器管理模块[已接入 Kubernetes 集群](../clusters/integrate-cluster.md)或者[已创建 Kubernetes 集群](../clusters/create-cluster.md)，且能够访问集群的 UI 界面。
- 已安装 Nvidia Driver 并开启了 MIG 能力，可参考 [Nvidia GPU 驱动安装](./install_nvidia_driver_of_operator.md)
- 集群节点已插入 GPU MIG 卡

## 通过界面使用 MIG GPU

1. 确认集群是否已识别 GPU 卡类型

    进入`集群详情` -> `集群设置` -> `Addon 设置`，查看是否已正确识别，自动识别频率为 `10 分钟` 。

    ![gpu](../../images/gpu_mig01.jpg)

1. 通过镜像部署应用可选择并使用 Nvidia MIG 资源。

    ![mig02](../../images/gpu_mig02.jpg)

    - 开启 `MIG Single` 模式时，添加的资源信息应为：

        ```yaml
        resources:
          limits:
          nvidia.com/gpu: 2
        ```

    - 开启 `MIG  Mixed` 模式时，添加的资源信息应为：

        ```yaml
        resources:
          limits:
          nvidia.com/mig-4g.20gb: 1 # (1)
        ```

        1. 通过 nvidia.com/mig-<slice_count>g.<memory_size>gb 的资源类型公开各个 MIG 设备

1. 进入容器后可以查看只使用了一个 MIG 设备。

    ![mig03](../../images/gpu_mig03.png)
