# 实时迁移

本文将介绍如何将虚拟机从一个节点移动到另一个节点。

当节点维护或者升级时，用户可以将正在运行的虚拟机无缝迁移到其他的节点上，同时可以保证业务的连续性和数据的安全性。

## 前提条件

使用实时迁移之前，需要满足以下前提条件：

- 只有运行中的虚拟机才能使用实时迁移功能。
- 如果需要使用实时迁移功能，请确保您的 PVC 访问模式为 ReadWriteMany。
- 需要当前集群内节点数量大于等于2个。

## 实时迁移

1. 点击左侧导航栏上的 __容器管理__ ，然后点击 __虚拟机__ ，进入列表页面，点击列表右侧的 __︙__ ，可以对运行状态下的虚拟机进行迁移动作。目前虚拟机所在节点为 __virtnest-rook-ceph-2__ 。

    ![实时迁移](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/live01.png)

2. 弹出弹框，提示在实时迁移期间，正在运行的虚拟机实例会移动到另一个节点，但是无法决定目标节点，同时请确保其他节点资源充足。

    ![迁移提示](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/live02.png)

3. 迁移成功后可以在虚拟机列表内查看节点信息，此时节点迁移到 __virtnest-rook-ceph-1__ 。

    ![迁移结果](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/live03.png)
