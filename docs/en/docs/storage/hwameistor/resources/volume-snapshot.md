# Volume Snapshot

In HwameiStor, users can create snapshots of data volumes (VolumeSnapshot), and restore or roll back
based on these snapshots.

!!! note

    Currently, only LVM volumes without high availability support snapshot creation.

    To avoid data inconsistency, please pause or stop I/O operations before taking a snapshot.

Please follow the steps below to create a VolumeSnapshotClass and VolumeSnapshot for use.

## Create a New VolumeSnapshotClass

By default, HwameiStor does not automatically create a VolumeSnapshotClass during installation,
so you need to create a VolumeSnapshotClass manually.

```yaml
kind: VolumeSnapshotClass
apiVersion: snapshot.storage.k8s.io/v1
metadata:
  name: hwameistor-storage-lvm-snapshot
  annotations:
    snapshot.storage.kubernetes.io/is-default-class: "true"
parameters:
  snapsize: "1073741824" # Specify the size of the VolumeSnapshot to be created
driver: lvm.hwameistor.io
deletionPolicy: Delete
```

!!! note

    If the snapsize parameter is not specified, the size of the created snapshot will be the same
    as that of the source volume.

After creating the VolumeSnapshotClass, you can use it to create a VolumeSnapshot.

## Create VolumeSnapshot Using VolumeSnapshotClass

A sample VolumeSnapshot is as follows:

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: snapshot-local-storage-pvc-lvm
spec:
  volumeSnapshotClassName: hwameistor-storage-lvm-snapshot
  source:
    persistentVolumeClaimName: local-storage-pvc-lvm # Specify the PVC for which to create the snapshot
```

After creating the VolumeSnapshot, you can check the VolumeSnapshot using the following command.

```console
$ kubectl get vs
NAME                             READYTOUSE   SOURCEPVC               SOURCESNAPSHOTCONTENT   RESTORESIZE   SNAPSHOTCLASS                     SNAPSHOTCONTENT                                    CREATIONTIME   AGE
snapshot-local-storage-pvc-lvm   true         local-storage-pvc-lvm                           1Gi           hwameistor-storage-lvm-snapshot   snapcontent-0fc17697-68ea-49ce-8e4c-7a791e315110   53y            2m57s
```

After creating a VolumeSnapshot, you can check the Hwameistor LocalvolumeSnapshot using the following command.

```console
$ kubectl get lvs
NAME                                               CAPACITY     SOURCEVOLUME                               STATE   MERGING   INVALID   AGE
snapcontent-0fc17697-68ea-49ce-8e4c-7a791e315110   1073741824   pvc-967baffd-ce10-4739-b996-87c9ed24e635   Ready                       5m31s
```

- CAPACITY: The capacity size of the snapshot
- SOURCEVOLUME: The source volume name of the snapshot
- MERGING:  Whether the snapshot is in a merged state (usually triggered by __rollback operation__)
- INVALID: Whether the snapshot is invalidated (usually triggered when __the snapshot capacity is full__)
- AGE: The actual creation time of the snapshot (different from the CR creation time, this time is the
  creation time of the underlying snapshot data volume)

After creating a VolumeSnapshot, you can restore and rollback the VolumeSnapshot.

## Restore VolumeSnapshot

You can create PVC to restore VolumeSnapshot, as follows:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: local-storage-pvc-lvm-restore
spec:
  storageClassName: local-storage-hdd-lvm
  dataSource:
    name: snapshot-local-storage-pvc-lvm
    kind: VolumeSnapshot
    apiGroup: snapshot.storage.k8s.io
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

## Rollback VolumeSnapshot

!!! note

    To perform a rollback on the snapshot, you must first **stop I/O on the source volume**, such as by
    stopping the application, waiting for the rollback operation to complete, and then **confirming data
    consistency** before using the rolled-back data volume.

VolumeSnapshot can be rolled back by creating the resource LocalVolumeSnapshotRestore, as follows:

```yaml
apiVersion: hwameistor.io/v1alpha1
kind: LocalVolumeSnapshotRestore
metadata:
  name: rollback-test
spec:
  sourceVolumeSnapshot: snapcontent-0fc17697-68ea-49ce-8e4c-7a791e315110 # Specify the local volume snapshot to roll back
  restoreType: "rollback"
```

Observing the created LocalVolumeSnapshotRestore, you can understand the entire rollback process through
the state. After the rollback is complete, the corresponding LocalVolumeSnapshotRestore will be deleted.

```console
$ kubectl get LocalVolumeSnapshotRestore -w
NAME            TARGETVOLUME                               SOURCESNAPSHOT                                     STATE        AGE
restore-test2   pvc-967baffd-ce10-4739-b996-87c9ed24e635   snapcontent-0fc17697-68ea-49ce-8e4c-7a791e315110   Submitted    0s
restore-test2   pvc-967baffd-ce10-4739-b996-87c9ed24e635   snapcontent-81a1f605-c28a-4e60-8c78-a3d504cbf6d9   InProgress   0s
restore-test2   pvc-967baffd-ce10-4739-b996-87c9ed24e635   snapcontent-81a1f605-c28a-4e60-8c78-a3d504cbf6d9   Completed    2s
```
