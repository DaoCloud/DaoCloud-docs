# 沐曦 GPU 组件安装与使用

本章节提供沐曦 metax-gpu-extensions、metax-operator 等组件的安装指导和沐曦 GPU 整卡和 vGPU 两种模式的使用方法。

## 前提条件

- 已经[部署 DCE 5.0](../../../../install/index.md) 容器管理平台，且平台运行正常。
- 容器管理模块[已接入 Kubernetes 集群](../../clusters/integrate-cluster.md)或者[已创建 Kubernetes 集群](../../clusters/create-cluster.md)，且能够访问集群的 UI 界面。
- 当前集群内 GPU 卡未进行任何虚拟化操作且未被其它 App 占用。

## 组件介绍

DCE 5.0 内置了两个 helm-chart 包，一个是 metax-gpu-extensions，一个是 metax-operator，根据使用场景可选择安装不同的组件。

1. metax-gpu-extensions：包含 gpu-device 和 gpu-label 两个组件。在使用 Metax-extensions 方案时，用户的应用容器镜像需要基于 MXMACA® 基础镜像构建。且仅适用于 GPU 整卡使用场景。
2. metax-operator：包含 gpu-device、gpu-label、driver-manager、container-runtime、operator-controller 这些组件。
   使用这个方案时，用户可选择制作不包含 MXMACA® SDK 的应用容器镜像。它适用于 GPU 整卡和 vGPU 场景。

## 操作步骤

### metax-gpu-extensions

1. 通过左侧导航栏 __容器管理__ -> __集群管理__ ，点击目标集群的名称
2. 从左侧导航栏点击 __Helm 应用__ -> __Helm 模板__ -> 搜索 __metax-gpu-extensions__
3. 出现对应组件，开始安装。

    ![安装gpu-extensions](../images/metax-gpu-extensions.png)
  
    部署成功之后，可以在节点上查看到资源。

    ![查看资源](../images/metax-node.png)

     在 DCE 5.0 平台的节点列表上看到带有 `Metax GPU` 的标签
  
    ![metax节点标签](../images/metax-node1.png)

### metax-operator

与安装 gpu-extensions 类似，搜索 __metax-operator__，找到后直接开始安装。

![安装metax-operator](../images/metax-operator.png)

## 使用 GPU

安装后可在工作负载中[使用沐曦 GPU](../../workloads/create-deployment.md#_5)。注意启用 GPU 后，需选择GPU类型为 Metax GPU

![使用 GPU](../images/metax-use.png)

进入容器，执行 mx-smi 可查看 GPU 的使用情况.

![使用 GPU](../images/metax-use2.png)
