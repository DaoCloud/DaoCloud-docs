# Reserve disk

This chapter introduces how to reserve a disk on the interface. the use cases of this feature are as follows:

The operation and maintenance administrator has disk planning requirements, and needs to reserve some disks not to be used by Hwameistor, and needs to perform the Reserved operation by himself

## **Instructions for use**

1. There are two statuses for Local Disk usage status and reserved status, any status of LD can be Reserved/Unreserved.
2. Hwameistor will automatically detect the system disk and mark it as Reserved at the beginning of startup
3. LD has only three states: **Pending, Available, Bound**. LD usage status and Reserved status are as follows:

| Usage status | Reserved or not | Scenario description |
| :-------- | :------------ | :--------------------- -------------------------------------- |
| Pending | -- | Initialization state |
| Pending | Reserved | Reserved by the user at the moment of initialization |
| Available | -- | free disk, can be allocated by Hwameistor |
| Available | Reserved | The free disk is planned for other use and cannot be allocated by Hwameistor without a file system, but the disk is already in use and marked as Reserved by the user |
| Bound | -- | The disk used by Hwameistor is used by the system or an external program, and the Reserved status has been removed manually |
| Bound | Reserved | Used by the system or external programs, and the Reserved state is manually removed. It is used by Hwamristor, and the user manually marks it as Reserved. When the data on the disk is released, it will no longer be used by the Hwameistor system |

## Steps

Enter the corresponding `cluster`, select `storage`-->`Hwameistor`; click `node` to enter the node details page, find the corresponding disk; click `...`, select `reserved disk`; click `confirm` to proceed reserved.

The reserved disk will not be used by Hwameistor.

![](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/reserveddisk.jpg)
