---
hide:
  - toc
---

# 资源

Hwameistor 在 Kubernetes 已有的 PV 和 PVC 对象类基础上，Hwameistor 定义了更丰富的对象类，把 PV/PVC 和本地数据盘关联起来。

|名称|缩写|Kind|功能|
|----|----|----|----|
|clusters|hmcluster|Cluster|HwameiStor 集群|
|events|evt|Event|HwameiStor 集群的审计日志|
|localdiskclaims|ldc|LocalDiskClaim|筛选并分配本地数据盘|
|localdisknodes|ldn|LocalDiskNode|裸磁盘类型数据卷的存储节点|
|localdisks|ld|LocalDisk|节点上数据盘，自动识别空闲可用的数据盘|
|localdiskvolumes|ldv|LocalDiskVolume|裸磁盘类型数据卷|
|localstoragenodes|lsn|LocalStorageNode|LVM 类型数据卷的存储节点|
|localvolumeconverts|lvconvert|LocalVolumeConvert|将普通 LVM 类型数据卷转化为高可用 LVM 类型数据卷|
|localvolumeexpands|lvexpand|LocalVolumeExpand|扩容 LVM 类型数据卷的容量|
|localvolumegroups|lvg|LocalVolumeGroup|LVM 类型数据卷组|
|localvolumemigrates|lvmigrate|LocalVolumeMigrate|迁移 LVM 类型数据卷|
|localvolumereplicas|lvr|LocalVolumeReplica|LVM 类型数据卷的副本|
|localvolumereplicasnapshotrestores|lvrsrestore,lvrsnaprestore|LocalVolumeReplicaSnapshotRestore|恢复 LVM 类型数据卷副本的快照|
|localvolumereplicasnapshots|lvrs|LocalVolumeReplicaSnapshot|LVM 类型数据卷副本的快照|
|localvolumes|lv|LocalVolume|LVM 类型数据卷|
|localvolumesnapshotrestores|lvsrestore,lvsnaprestore|LocalVolumeSnapshotRestore|恢复 LVM 类型数据卷快照|
|localvolumesnapshots|lvs|LocalVolumeSnapshot|LVM 类型数据卷快照volume|
|resizepolicies||ResizePolicy|PVC 自动扩容策略|

如有需要，可以使用以下命令查看 api-resources :

```bash
$ kubectl api-resources --api-group=hwameistor.io

NAME                                 SHORTNAMES                   APIVERSION               NAMESPACED   KIND
clusters                             hmcluster                    hwameistor.io/v1alpha1   false        Cluster
events                               evt                          hwameistor.io/v1alpha1   false        Event
localdiskactions                     lda                          hwameistor.io/v1alpha1   false        LocalDiskAction
localdiskclaims                      ldc                          hwameistor.io/v1alpha1   false        LocalDiskClaim
localdisknodes                       ldn                          hwameistor.io/v1alpha1   false        LocalDiskNode
localdisks                           ld                           hwameistor.io/v1alpha1   false        LocalDisk
localdiskvolumes                     ldv                          hwameistor.io/v1alpha1   false        LocalDiskVolume
localstoragenodes                    lsn                          hwameistor.io/v1alpha1   false        LocalStorageNode
localvolumeconverts                  lvconvert                    hwameistor.io/v1alpha1   false        LocalVolumeConvert
localvolumeexpands                   lvexpand                     hwameistor.io/v1alpha1   false        LocalVolumeExpand
localvolumegroups                    lvg                          hwameistor.io/v1alpha1   false        LocalVolumeGroup
localvolumemigrates                  lvmigrate                    hwameistor.io/v1alpha1   false        LocalVolumeMigrate
localvolumereplicas                  lvr                          hwameistor.io/v1alpha1   false        LocalVolumeReplica
localvolumereplicasnapshotrestores   lvrsrestore,lvrsnaprestore   hwameistor.io/v1alpha1   false        LocalVolumeReplicaSnapshotRestore
localvolumereplicasnapshots          lvrs                         hwameistor.io/v1alpha1   false        LocalVolumeReplicaSnapshot
localvolumes                         lv                           hwameistor.io/v1alpha1   false        LocalVolume
localvolumesnapshotrestores          lvsrestore,lvsnaprestore     hwameistor.io/v1alpha1   false        LocalVolumeSnapshotRestore
localvolumesnapshots                 lvs                          hwameistor.io/v1alpha1   false        LocalVolumeSnapshot
resizepolicies                                                    hwameistor.io/v1alpha1   false        ResizePolicy
```
