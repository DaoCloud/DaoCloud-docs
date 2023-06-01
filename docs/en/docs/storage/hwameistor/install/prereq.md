---
hide:
   - toc
---

# Preparation

## Platform Preparation

- Kubernetes container platform version 1.18 or higher

- CoreDNS must be deployed

- For high availability, `kernel-devel` consistent with the currently running Kernel version should be installed

- If `LVM2` is not installed, please refer to the appropriate installation method below:

=== "CentOS/RHEL, Rocky and Kylin"
  
    ```console
    yum install -y lvm2
    yum install -y kernel-devel-$(uname -r)
    ```
  
=== "Ubuntu"
  
    ```console
    apt-get install -y lvm2
    apt-get install -y linux-headers-$(uname -r)
    ```

## Node Configuration

| **Architecture** | **Operating System** | **Kernel Version** | Remarks |
| -------- | ------------------- | -------------------- ---------------------- | ----------------------- |
| AMD 64 | CentOS 7.X | Kernel 3.10.0-1127.el7.x86_64 on x86_64 architecture | Recommended operating system: CentOS 7.9 |
| | Red Hat Enterprise Linux (RHEL) 8.X | 4.18.0-305.el8.x86_64 | Recommended operating system: RHEL 8.4 |
| | RHEL 7.X | 3.10.0-1160.e17.x86 | Recommended operating system: RHEL 7.9 |
| ARM 64 | Galaxy Kirin OS V10 SP2 | 4.19.90-24.4.v2101.ky10.aarch64 | - |

## Disk Types

HwameiStor supports physical hard disk drives (HDD), solid-state drives (SSD), and NVMe flash drives.

In a test environment, each host must have at least one free `10GiB` data disk.

In a production environment, it is recommended that each host have at least one free `200GiB` data disk, and it is recommended to use a solid-state drive (SSD).

## Network Planning

In a production environment, after enabling high availability mode, it is recommended to use `10 Gigabit TCP/IP` network with redundancy protection. The network can be planned in advance by specifying the network card IP through [modifying the network card](storage-eth.md).
