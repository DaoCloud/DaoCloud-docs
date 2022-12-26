---
hide:
  - toc
---

# PVs and PVCs

PV (PersistentVolume, persistent volume) is an abstraction of storage resources, which defines storage as a resource that can be used by container applications.
PVs are created and configured by administrators and are directly related to specific implementations of storage providers, such as file storage, block storage, object storage, or DRBD, etc.,
Managed through a plug-in mechanism for access and use by applications. Except for volumes of type EmptyDir, the lifecycle of a PV is independent of the Pods that use it.

PVC (PersistentVolumeClaim, persistent volume claim) is a user's application for storage resources.
Just like Pod consumes Node's resources, PVC consumes PV's resources. The size (Size) and access mode (such as ReadWriteOnce, ReadOnlyMany, or ReadWriteMany) of the storage space that a PVC can apply for.

The storage space applied for using PVC still does not meet the various needs of applications for storage devices.
In many cases, applications have different requirements on the characteristics and performance of storage devices, including requirements for read and write speed, concurrent performance, and data redundancy.
This requires the use of the resource object StorageClass, which is used to mark storage resources and performance, and dynamically provide appropriate PV resources according to the needs of PVC.
After the improvement of StorageClass and the dynamic supply mechanism of storage resources, the on-demand creation of storage volumes is realized, which is an important step in the automatic management process of shared storage.

Please also refer to the official Kubernetes documentation:

- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)
- [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/)
- [Dynamic Volume Provisioning](https://kubernetes.io/docs/concepts/storage/dynamic-provisioning/)