# 跨集群弹性伸缩

弹性伸缩（FederatedHPA）策略可以跨多个集群扩展/缩小工作负载的副本，旨在根据需求自动调整工作负载的规模。

本文介绍如何实现跨集群弹性伸缩。

## 前提条件

- 需要提前在高级配置中开启弹性伸缩按钮，将自动在控制面集群安装 karmada-metrics-adapter 插件用于提供 metrics API。
- 需要在成员集群中安装 metrics-server 插件用以提供 metrics API。

## 开启弹性伸缩

![开启弹性伸缩](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kairship/images/fhpa01.png)

## 创建多云工作负载

参照 [创建无状态负载](../workload/deployment.md) 创建一个多云工作负载。

!!! note

    1.使用跨集群弹性伸缩功能时，工作负载的调度策略必须为聚合/动态权重。
    2.设置CPU、内存的配置信息。
    3.创建一个多云服务用于压测。

## 跨集群弹性缩容

1. 进入工作负载详情，当前负载正常运行，共4个副本。

   ![工作负载](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kairship/images/fhpa02.png)

2. 点击`弹性伸缩`，检查是否每个工作集群内都安装了 metrics-server 插件。该插件以 `deployment` 的形式在 `kube-system` 命名空间内运行，可以发现目前该插件在所有成员集群内都已经安装并且正常运行。

   ![弹性伸缩列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kairship/images/fhpa03.png)

   ![检查插件](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kairship/images/fhpa04.png)

3. 新建弹性伸缩，根据需要进行配置。

   - 副本范围：定义副本扩缩容的范围。
   - 冷却时间：定义扩缩容操作的间隔时间。
   - 系统指标：定义扩缩容操作的触发条件。

   ![配置弹性伸缩](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kairship/images/fhpa05.png)

4. 规则创建好后，刷新页面，可以查看当前副本的具体数值。因为目前并没有调用该服务，所以实际的 CPU 用量为0，小于目标值，此时为了减少资源浪费，会进行缩容操作，副本由4缩小为1，缩容的范围根据用户定义的副本范围而定。

   ![缩容](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kairship/images/fhpa06.png)

   ![副本分配情况](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kairship/images/fhpa07.png)

## 跨集群弹性扩容

登陆此工作负载所在节点，通过压力测试验证扩容策略是否生效。

1. 检查服务是否正常运行。

   ![检查服务运行情况](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kairship/images/fhpa08.png)

2. 使用`hey -c 1000 -z 10m http://10.111.254.117:8080`命令进行压测。一段时间后，发现 CPU 上升，副本数增多，扩容成功。

   ![扩容](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kairship/images/fhpa09.png) 

   ![副本分布情况](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kairship/images/fhpa10.png)
