# Fluid

## 简介

[Fluid](http://pasa-bigdata.nju.edu.cn/fluid/zh/) 是一个开源的 Kubernetes 原生的分布式数据集编排和加速引擎，主要服务于云原生场景下的数据密集型应用，例如大数据应用、AI应用等。

通过 Kubernetes 服务提供的数据层抽象，可以让数据像流体一样在诸如 HDFS、OSS、Ceph 等存储源和 Kubernetes 上层云原生应用计算之间灵活高效地移动、复制、驱逐、转换和管理。而具体数据操作对用户透明，用户不必再担心访问远端数据的效率、管理数据源的便捷性，以及如何帮助 Kuberntes 做出运维调度决策等问题。用户只需以最自然的 Kubernetes 原生数据卷方式直接访问抽象出来的数据，剩余任务和底层细节全部交给 Fluid 处理。

## 核心概念

- Dataset 数据集：通俗地说，就是应用要访问的数据集合。不同应用对应的数据集类型不同。

- Runtime 分布式缓存系统运行时：Runtime 是 Fluid 部署分布式缓存系统的一个标准框架，具体部署的分布式缓存系统就是具体的Runtime。
    AlluxioRuntime
    JuiceFSRuntime
    JinboFSRuntime
    GooseFSRuntime
    EFCRuntime
    ThinRuntime
    ...

- Data access 用户数据访问：Fluid 提供了一个统一的 Fuse 接口给用户应用，该接口完全兼容 POSIX 协议。用户应用就像访问本地数据一样，访问远程数据集。

## 通过 Helm 模板部署 Fluid

DCE 5.0 支持了 Fluid， 并将其作为 Addon 集成了应用商店中。

1. 进入`容器管理`模块，在`集群列表`中找到需要安装 Fluid， 的集群，点击该集群的名称。

    ![点击集群名称](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/storage/images/fluid01.png)

2. 在左侧导航栏中选择 `Helm 应用` -> `Helm 模板`，找到并点击 `Fluid`。

    ![fluid-helm](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/storage/images/fluid02.png)

3. 在安装界面，填写所需的安装参数，最后在右下角点击`确定`按钮。

    ![填写配置](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/storage/images/fluid03.png)

    - 名称：组件的名称，可以输入 `fluid`。

    - 命名空间：选择`新建命名空间`，必须将名称设置为 `fluid-system`，否则部署会失败。

    - 版本：目前仅支持了 `0.9.2`。

    - 其他参数配置，使用默认参数即可。

4. 前往 Helm 应用查看部署结果。

    ![完成创建](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/storage/images/fluid04.png)

5. 也可以在当前集群详情左侧菜单栏的 `工作负载` -> `容器组`，选择命名空间为 `fluid-system`，查看所有容器组的状态。

    ![pod](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/storage/images/fluid05.png)

有关 Fulid 如何加速数据访问的 demo 请前往官网查看：https://fluid-cloudnative.github.io/#demo 。
