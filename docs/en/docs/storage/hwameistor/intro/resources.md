---
hide:
  - toc
---

# Resources

Based on the existing PV and PVC object classes of Kubernetes, Hwameistor defines richer object classes to associate PV/PVC with local data disks.

|Kind|Abbreviation|Function|
|--|--|--|
|LocalDiskNode|ldn|registered node|
|LocalDisk|ld|Register the data disk on the node and automatically identify the free and available data disk|
|LocalDiskClaim|ldc|Filter and register local data disk|
|LocalStorageNode|lsn|Automatically create StorageClass, that is, LVM logical volume groups|
|LocalVolume|lv|Create LVM logical volume, assign to PersistentVolume|
|LocalDiskExpand|lvexpand|StorageClass Expansion|
