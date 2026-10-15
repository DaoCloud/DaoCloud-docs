# Clone a Virtual Machine

This article explains how to clone a new virtual machine.

You can clone a new virtual machine. The cloned virtual machine has the same operating system and system configuration as the original virtual machine, which enables rapid deployment and expansion, and allows you to quickly create a new virtual machine with a similar configuration without installing from scratch.

## Prerequisites

The following prerequisites must be met before using the clone feature (the same as the prerequisites for the snapshot feature):

- Only virtual machines that are not in an error state can use the clone feature.
- Install Snapshot CRDs, Snapshot Controller, and CSI Driver.
  For installation steps, refer to [CSI Snapshotter](https://github.com/kubernetes-csi/external-snapshotter?tab=readme-ov-file#usage).
- Wait until the snapshot-controller component is ready. This component monitors VolumeSnapshot and VolumeSnapshotContent events and triggers related operations.
- Wait until the CSI Driver is ready. Make sure that the csi-snapshotter sidecar runs inside the CSI Driver. The csi-snapshotter sidecar monitors VolumeSnapshotContent events and triggers related operations.
    - If the storage is Rook-Ceph, refer to [ceph-csi-snapshot](https://rook.io/docs/rook/latest-release/Storage-Configuration/Ceph-CSI/ceph-csi-snapshot/).
    - If the storage is HwameiStor, refer to [huameistor-snapshot](https://hwameistor.io/cn/docs/volumes/volume_snapshot).

## Clone a Virtual Machine

1. From the left navigation bar, click __Virtual Machines__ -> __Virtual Machines__ in turn to enter the list page, and click __┇__ on the right side of the list to perform the clone operation on a virtual machine that is not in an error state.

    ![Clone a virtual machine](../images/clone01.png)

2. A dialog box pops up, where you need to enter the name and description of the new virtual machine. The clone operation may take some time, which depends on the size of the virtual machine and the storage performance.

    ![Cloning process](../images/clone02.png)

3. After the cloning succeeds, you can view the new virtual machine in the virtual machine list. The newly created virtual machine is powered off. If you need to power it on, perform the operation manually.

    ![New virtual machine](../images/clone03.png)

4. It is recommended to take a snapshot of the original virtual machine before cloning. If you encounter any problem during cloning, check whether the prerequisites are met and try the clone operation again.
