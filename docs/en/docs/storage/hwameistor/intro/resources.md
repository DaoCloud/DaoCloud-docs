---
MTPE: WANG0608GitHub
Date: 2024-08-27
hide:
  - toc
---

# Resources

Based on the existing PV and PVC object classes in Kubernetes, Hwameistor defines a richer set of
object classes to associate PV/PVC with local data disks.

|Name|Abbr|Kind|Function|
|----|----|----|--------|
|clusters|hmcluster|Cluster|HwameiStor cluster|
|events|evt|Event|Audit logs of HwameiStor cluster|
|localdiskclaims|ldc|LocalDiskClaim|Filter and allocate local data disks|
|localdisknodes|ldn|LocalDiskNode|Storage pool for disk volumes|
|localdisks|ld|LocalDisk|Data disks on nodes and automatically find which disks are available|
|localdiskvolumes|ldv|LocalDiskVolume|Disk volumes|
|localstoragenodes|lsn|LocalStorageNode|Storage pool for LVM volumes|
|localvolumeconverts|lvconvert|LocalVolumeConvert|Convert common LVM volume to highly available LVM volume|
|localvolumeexpands|lvexpand|LocalVolumeExpand|Expand the capacity of LVM volume.|
|localvolumegroups|lvg|LocalVolumeGroup|LVM volume groups|
|localvolumemigrates|lvmigrate|LocalVolumeMigrate|Migrate LVM volume|
|localvolumereplicas|lvr|LocalVolumeReplica|Replicas of LVM volume|
|localvolumereplicasnapshotrestores|lvrsrestore,lvrsnaprestore|LocalVolumeReplicaSnapshotRestore|Restore snapshots of LVM volume Replicas|
|localvolumereplicasnapshots|lvrs|LocalVolumeReplicaSnapshot|Snapshots of LVM volume Replicas|
|localvolumes|lv|LocalVolume|LVM volumes|
|localvolumesnapshotrestores|lvsrestore,lvsnaprestore|LocalVolumeSnapshotRestore|Restore snapshots of LVM volume|
|localvolumesnapshots|lvs|LocalVolumeSnapshot|Snapshots of LVM volume|
|resizepolicies||ResizePolicy|PVC automatic expansion policy|

You can use the following command to view api-resources:

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
