# LVM

The full name of LVM is Logical Volume Manager, which is a logical volume manager. It adds a logical layer between the disk partition and the file system, provides an abstract volume for the file system to shield the underlying disk partition layout, and establishes a file system on the volume.

LVM can be used to dynamically adjust the size of the file system without repartitioning the disk, and the file system managed by LVM can span disks. When a new disk is added to the server, the administrator does not need to move the original files to the new disk, but directly expands the file system across the disk through LVM. That is, by encapsulating the underlying physical hard disk and presenting it to the upper-layer application as a logical volume.

LVM encapsulates the underlying hard disk. When we operate the underlying physical hard disk, we no longer operate on partitions, but perform underlying disk management operations on it through a thing called a logical volume.

## LVM main components

**Physical storage media (PM, physical media)**: LVM storage media can be partitions, disks, RAID arrays, or SAN disks.

**Physical volume (PV, physical volume): **Physical volume is the basic storage logical block of LVM, but compared with basic physical storage media (such as partitions, disks, etc.), it contains management parameters related to LVM. Create A physical volume can be partitioned by a disk or by the disk itself. Disk devices must be initialized as LVM physical volumes to be used with LVM.

**Volume Group (VG, Volume Group): **LVM volume group consists of one or more physical volumes.

**Logical volume (LV, logical volume): **LV is built on top of VG, and a file system can be built on top of LV.

**Physical extent (PE, physical extents): **The minimum storage unit that can be allocated in the PV physical volume. The size of PE can be specified, and the default is 4MB.

**Logical extent (LE, logical extents): **The smallest storage unit that can be allocated in an LV logical volume. In the same volume group, the size of LE is the same as that of PE, and there is a one-to-one correspondence.

## LVM advantages

- Use volume groups to make multiple hard disk spaces look like one big hard disk
- Using logical volumes, you can partition across multiple hard disk spaces sdb1 sdb2 sdc1 sdd2 sdf
- Using logical volumes, you can dynamically resize it when space is low
- When resizing the logical volume, there is no need to consider the location of the logical volume on the hard disk, and there is no need to worry about the lack of continuous space available
- You can create, delete, and resize LV and VG online, and the file system on LVM also needs to be resized
- Allows creation of snapshots, which can be used to keep backups of the file system
- Combination of RAID + LVM: LVM is a software method of volume management, while RAID is a method of disk management. For important data, use RAID to protect the physical disk from interrupting business due to failure, and then use LVM to achieve healthy management of volumes and better use of disk resources.

## Basic steps to use LVM

1. The physical disk is formatted as PV, that is, the space is divided into individual PEs. A PV contains multiple PEs.
2. Different PVs are added to the same VG, that is, PEs of different PVs all enter the PE pool of the VG. A VG contains multiple PVs.
3. Create an LV logical volume in the VG. This creation process is based on PEs, so the PEs that make up the LV may come from different physical disks. LVs are created based on PEs.
4. LV can be mounted directly after formatting.
5. The scaling of LV is actually to increase or decrease the number of PEs that make up the LV, and the process will not lose the original data.
6. Format the LV and mount it for use.

## LV expansion

First, determine whether there is available expansion space, because the space is created from inside the VG, and the LV cannot be expanded across VGs. If the VG has no capacity, you need to expand the VG first. Proceed as follows:

```bash
$ vgs
VG #PV #LV #SN Attr VSize VFree
vg-sdb1 1 8 1 wz--n- <16.00g <5.39g
$ lvextend -L +100M -r /dev/vg-sdb1/lv-sdb1 #Expand /dev/vg-sdb1/lv-sdb to 100M
```

## VG expansion

If the space in the VG volume group is not enough, you need to add a new disk, run the following commands in sequence:

```bash
$ pvcreate /dev/sdc
$ vgextend vg-sdb1 /dev/sdb3
```

## LV Snapshot

The LVM mechanism provides the function of taking a snapshot of the LV to obtain a state-consistent backup of the file system. LVM adopts Copy-On-Write (COW) technology, which can be backed up without stopping the service or setting the logical volume to read-only. Using the LVM snapshot function can obtain consistent backup without affecting the availability of the server.

The copy-on-write adopted by LVM means that when an LVM snapshot is created, only the metadata of the data in the original volume is copied. In other words, when creating an LVM logical volume, no physical copying of data occurs. In other words, only metadata is copied, not physical data, so snapshots are created almost in real time. When a write operation is performed on the original volume, the snapshot will track the changes of the blocks in the original volume. At this time, the data to be changed on the original volume will be copied to the space reserved by the snapshot before the change.