# HwameiStor Release Notes

This page lists the Release Notes related to HwameiStor, providing an overview of
the evolution path and feature changes for each version.

## 2024-07-30

### v0.14.8

#### Improvment

- **Improved** the default reclaim policy changed from delete to retain

#### Fixes

- **Fixed** an issue to output the disk along with the partition table.
- **Fixed** an issue where empty pvName was not handled
- **Fixed** an issue with the affinity and taint skip policy

## 2024-06-30

### v0.14.7

#### Improvements

- **Improved** affinity issues and added an option to skip affinity.
- **Improved** and cleaned up the dataset manager code.

## 2024-04-30

### v0.14.6

#### Improvements

- **Improved** Resolve the issue where LVR does not respect pod affinity
- **Improved** Add an option to enable data validation during migration

## 2024-03-31

### v0.14.4

#### Improvements

- **Improved** Delete local mount path when unmounting data volumes
- **Improved** Added PoolHDD FreeCap to the print column

## 2024-01-31

### v0.14.1

#### Improvements

- **Improved** Skip volumes that have defined storage classes but no storage class instances when ignoring failure policy
- **Improved** Check for the existence of local disks before use
- **Improved** snapshot client
- **Improved** Added snapshot support to Hwameictl command-line tool
- **Improved** Added cluster support to Hwameictl command-line tool for snapshots

#### Fixes

- **Fixed** an issue with getnode API
- **Fixed** an issue with ctl disk_list
- **Fixed** an issue with snapshot control error

## 2023-12-31

### v0.14.0

#### Improvements

- **Improved** Removed the use of meaningless poolType
- **Improved** Added VolumeSnapshotClass
- **Improved** Added support for `snapshot` parameter in Hwameictl command-line tool

#### Fixes

- **Fixed** Ensured Volume Group always maintains consistent accessibility with all volumes in the group
- **Fixed** an issue with pending error when cleaning up replicas in localvolumemigrate
- **Fixed** Added system exit statement when indexer setting fails
- **Fixed** an issue with StorageNodePoolDiskGet retrieving localdisk incorrectly
- **Fixed** volume leakage when users delete PVC but do not create PV

## 2023-11-30

### v0.13.3

#### New Features

- **Added** support for volume cloning
- **Added** delayed volume deletion when snapshot is discovered
- **Added** filtering nodes based on source volume accessibility

#### Improvements

- **Improved** logging disk claim events only when the disk is available

#### Fixes

- **Fixed** filtering replicaSnapRestoreName before submitting a job
- **Fixed** incorrect state transition in LocalVolumeConvert
- **Fixed** exiting when indexer addition fails
- **Fixed** using storage node IP when migrating volumes
- **Fixed** cleaning up replicas after canceling publication
- **Fixed** error in `apiserver getnodedisk` and added set-diskowner API

## 2023-10-30

### v0.13.1

#### New Features

- **Added** compatibility with Kubernetes v1.28 version
- **Added** LVM data volume snapshot feature

#### Improvements

- **Improved** HwameiStor Operator with additional component resource configuration
- **Improved** snapshot recovery timeout
- **Improved** default log level for LDM

## 2023-8-30

### v0.12.1

#### New Features

- **Added** Support for `ext` filesystem.
- **Added** New features parameters for Local Disk.
- **Added** Field to record device history information.
- **Added** SN/ID Path recognition for disks.
- **Added** Automatic disk expansion functionality.
- **Added** System resource auditing for cluster, storage nodes, disks, and data volumes

#### Improvements

- **Fixed** Display issue of NVME disks in LocalStoragePool nodes.
- **Fixed** an issue with lost replica status during migration operation.
- **Fixed** Disallow disk allocation when Disk Owner is empty.
- **Fixed** Issues with Failover functionality in `deploy` and `Makefile`

## 2023-7-05

### v0.11.1

#### New Features

- **Added** Support for automatic detection of `cgroup` version.

## 2023-6-25

### v0.11.0

#### New Features

- **Added** Implementation of IO limitation or QoS.
- **Added** Use of `/virtual/` detection to identify virtual block devices.

#### Improvements

- **Fixed** Inconsistency in creation time field for StorageClass.

## 2023-5-26

### v0.10.3

#### Improvements

- **Improved** Permissions-related content in Helm templates.

## 2023-7-05

### v0.11.1

#### New Features

**Added** support for automatic detection of `cgroup` version

## 2023-6-25

### v0.11.0

#### New Features

**Added** implementation of IO limitation or QoS

**Added** identification of virtual block devices using /virtual/

#### Improvements

**Fixed** inconsistency issue with StorageClass creation time field

## 2023-5-26

### v0.10.3

#### Improvements

**Improved** permissions-related content in Helm Charts

## 2023-5-25

### v0.10.2

#### Improvements

**Improved** automatic conversion of Node Name `.` to `-`, affecting LDM heartbeat detection

**Added** Admin permission functionality

## 2023-5-17

### v0.10.0

#### Improvements

- **Added** identification and setting of local disk Manager Owner information
- **Improved** marking disk status as 'inactive' when removal time is received
- **Improved** dashboard for disk Smart indicators
- **Added** local StorageClass
- **Improved** display of UI component statuses
- **Improved** separation of disk allocation and disk status update processes
- **Improved** renaming of Exporter port to http-metrics
- **Improved** addition of port name in exporter service

#### Bug Fixes

- **Fixed** an issue where LD is bound but has no capacity in LSN
- **Fixed** Metrics port listening issue
- **Fixed** an issue that may cause "not found" errors
- **Fixed** an issue with UI tag in Helm

### v0.9.3

#### Improvements

- **Improved** filling of disk owner information during usage
- **Improved** merging of disk self attributes when triggered by udev events
- **Improved** adding labels to svc
- **Improved** separation of disk allocation and disk status update processes
- **Improved** renaming of Exporter port to http-metrics
- **Improved** addition of port name in exporter service

#### Bug Fixes

- **Fixed** an issue where LD is bound but has no capacity in LSN
- **Fixed** Metrics port listening issue
- **Fixed** an issue that may cause "not found" errors
- **Fixed** an issue with UI tag in Helm

## 2023-3-30

### v0.9.2

#### Improvements

- **Added** UI relok8s

### v0.9.1

#### Improvements

- **Added** Volume Status monitoring [Issue #741](https://github.com/hwameistor/hwameistor/pull/741)
- **Fixed** Local Storage deployment parameters [Issue #742](https://github.com/hwameistor/hwameistor/pull/742)

### v0.9.0

#### New Features

- **Added** disk Owner [Issue #681](https://github.com/hwameistor/hwameistor/pull/681)
- **Added** Grafana Dashboard [Issue #733](https://github.com/hwameistor/hwameistor/pull/733)
- **Added** Operator installation method, automatically pulling UI during installation [Issue #679](https://github.com/hwameistor/hwameistor/pull/679)
- **Added** UI application Label [Issue #710](https://github.com/hwameistor/hwameistor/pull/710)

#### Improvements

- **Added** used capacity of disks [Issue #681](https://github.com/hwameistor/hwameistor/pull/681)
- **Improved** skipping scoring mechanism when no available disks are found [Issue #724](https://github.com/hwameistor/hwameistor/pull/724)
- **Set** default DRBD port to 43001 [Issue #723](https://github.com/hwameistor/hwameistor/pull/723)

## 2023-1-30

### v0.8.0

#### Improvements

- **Improved** Chinese documentation
- **Improved** value.yaml file
- **Updated** Roadmap
- **Improved** default failure strategy when installation fails

## 2022-12-30

### v0.7.1

#### New Features

- **Added** HwameiStor Dashboard UI, which displays storage resource and storage node usage status
- **Added** interface for managing HwameiStor storage nodes, local disks, and migration records
- **Added** StorageClass management functionality, displaying basic information about StorageClass and corresponding nodes
- **Added** local volume management functionality, supporting data volume migration and high availability conversion

#### Improvements

- **Improved** unnecessary logging before data migration and avoided interference from Job execution in other namespaces
