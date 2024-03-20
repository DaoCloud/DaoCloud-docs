# 快照管理

本文将介绍如何为虚拟机创建快照，并从快照中恢复的。

用户可以为虚拟机创建快照，保存虚拟机当下的状态，一个快照可以支持多次恢复，每次恢复时，虚拟机将被还原到快照创建时的状态。通常可以用于备份、恢复、回滚等场景。

## 前提条件

使用快照功能之前，需要满足以下前提条件：

- 只有非错误状态下的虚拟机才能使用快照功能。
- 安装 CSI Snapshotter,首先，确保部署了 CSI Snapshotter 组件。snapshot-controller 会监控 VolumeSnapshot 和VolumeSnapshotContent 对象，并触发相关操作。
- 安装 Snapshot CRDs、Snapshot Controller、CSI Driver。可参考[CSI Snapshotter](https://github.com/kubernetes-csi/external-snapshotter?tab=readme-ov-file#usage)。
- 等待 csi-snapshotter 和 snapshot-controller 组件准备就绪。


## 创建快照

1. 点击左侧导航栏上的 __容器管理__ ，然后点击 __虚拟机__ ，进入列表页面，点击列表右侧的 __︙__ ，可以对非错误状态下的虚拟机执行快照操作。

    ![创建快照](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/snapshot01.png)

2. 弹出弹框，需要填写快照的名称和描述，创建快照大概需要几分钟的时间，在此期间无法对虚拟机做任何操作。

    ![快照名称](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/snapshot02.png)

3. 创建成功后可以在虚拟机详情内查看快照信息，支持编辑描述、从快照中恢复、删除等操作。

    ![虚拟机详情](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/snapshot03.png)

## 从快照中恢复

1. 点击 __从快照恢复__ ，需要填写虚拟机恢复记录的名称，同时恢复操作可能需要一些时间来完成，具体取决于快照的大小和其他因素。恢复成功后，虚拟机将回到快照创建时的状态。

    ![快照恢复](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/snapshot04.png)

2. 一段时间后，下拉快照信息，可以查看当前快照的所有恢复记录，并且支持展示定位恢复的位置。

    ![恢复记录](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/virtnest/images/snapshot05.png)