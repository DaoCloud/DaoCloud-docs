---
MTPE: ModetaNiu
Date: 2024-08-01
---

# Snapshot Management

This guide explains how to create snapshots for virtual machines and restore them.

You can create snapshots for virtual machines to save the current state of the virtual machine. A snapshot can be restored multiple times, and each time the virtual machine will be reverted to the state when the snapshot was created. Snapshots are commonly used for backup, recovery and rollback.

## Prerequisites

Before using the snapshots, the following prerequisites need to be met:

- Only virtual machines in a non-error state can use the snapshot function.
- Install Snapshot CRDs, Snapshot Controller, and CSI Driver.
  For detailed installation steps, refer to [CSI Snapshotter](https://github.com/kubernetes-csi/external-snapshotter?tab=readme-ov-file#usage).
- Wait for the snapshot-controller component to be ready. This component monitors events related to VolumeSnapshot 
  and VolumeSnapshotContent and triggers specific actions.
- Wait for the CSI Driver to be ready. Ensure that the csi-snapshotter sidecar is running within the CSI Driver. 
  The csi-snapshotter sidecar monitors events related to VolumeSnapshotContent and triggers specific actions. 
    - If the storage is rook-ceph, refer to [ceph-csi-snapshot](https://rook.io/docs/rook/latest-release/Storage-Configuration/Ceph-CSI/ceph-csi-snapshot/).
    - If the storage is HwameiStor, refer to [huameistor-snapshot](https://hwameistor.io/cn/docs/volumes/volume_snapshot).

## Create a Snapshot

1. Click __Container Management__ in the left navigation menu, then click __Virtual Machines__ to access the list page. Click the __┇__ on the right side of the list for a virtual machine to perform snapshot operations (only available for non-error state virtual machines).

    ![Create Snapshot](../images/snapshot01.png)

2. A dialog box will pop up, prompting you to input a name and description for the snapshot. Please note that the creation process may take a few minutes, during which you won't be able to perform any operations on the virtual machine.

    ![Snapshot Name](../images/snapshot02.png)

3. After successfully creating the snapshot, you can view its details within the virtual machine's information section. Here, you have the option to edit the description, recover from the snapshot, delete it, among other operations.

    ![Virtual Machine Details](../images/snapshot03.png)

## Restore from a Snapshot

1. Click __Restore from Snapshot__ and provide a name for the virtual machine recovery record. The recovery operation may take some time to complete, depending on the size of the snapshot and other factors. After a successful recovery, the virtual machine will be restored to the state when the snapshot was created.

    ![Snapshot Recovery](../images/snapshot04.png)

2. After some time, you can scroll down to the snapshot information to view all the recovery records for the current snapshot. It also provides a way to locate the position of the recovery.

    ![Recovery Record](../images/snapshot05.png)
