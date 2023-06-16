---
hide:
  - toc
---

# 添加实例

在开始使用多云编排模块提供的各种功能之前，必须先添加一个多云实例，通过该实例才能管理各种多云资源。

!!! note

    - 由于 DCE 5.0 多云编排模块借用了开源项目 [Karmada](https://karmada.io/) 的能力，所以创建多云实例时会自动创建一个 Karmada 实例。

    - 新建的多云实例默认位于[全局管理集群](../../kpanda/user-guide/clusters/cluster-role.md)，以虚拟集群的形式存在，用户无感知。
    
    - 为便于和真实集群进行区分，所有多云实例对应的虚拟集群的名称都带有 `k-` 前缀。

添加多云实例的步骤如下：

1. 在多云实例列表中，点击右上角的`添加多云实例`。

    ![add](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/add01.png)

2. 参考下列信息填写各项配置，最后在右下角点击`确定`。

    - 管理面集群：可选的集群列表来自于[容器管理](../../kpanda/intro/what.md)模块中接入或创建的集群。如果没有想选的集群，可以去容器管理模块中[接入](../../kpanda/user-guide/clusters/integrate-cluster.md)或[创建](../../kpanda/user-guide/clusters/create-cluster.md)集群。
    - 实例释放：如果勾选，删除多云实例时会同步删除对应的 Karmada 实例。如果不删除，可以继续通过终端使用，但无法在 DCE 5.0 的多云编排模块内管理该 Karmada 实例。建议同步删除。

        ![Management](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/instance-guanli.png)
