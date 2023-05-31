---
hide:
   - toc
---

# Preparation

## Platform preparation

- Kubernetes container platform version 1.18+

- CoreDNS deployed

- The high availability function needs to install `kernel-devel` consistent with the currently running Kernel version

- `LVM2` has been installed, if not installed, please refer to the following installation method:

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

## node configuration

| **Architecture** | **Operating System** | **Kernel Version** | Remarks |
| -------- | ------------------- | -------------------- ---------------------- | ----------------------- |
| AMD 64 | centos 7.X | Kernel 3.10.0-1127.el7.x86_64 on an x86_64 | Operating system recommended CentOS 7.9 |
| | Redhat 8.X | 4.18.0-305.el8.x86_64 | Recommended operating system Redhat 8.4 |
| | Redhat 7.X | 3.10.0-1160.e17.x86 | Recommended Operating System Redhat 7.9 |
| ARM 64 | Galaxy Kirin OS V10 SP2 | 4.19.90-24.4.v2101.ky10.aarch64 | - |

## disk type

HwameiStor supports physical hard disk drives (HDD), solid state drives (SSD) and NVMe flash drives.

In the test environment, each host must have at least one free `10GiB` data disk.

In a production environment, it is recommended that each host has at least one free `200GiB` data disk, and it is recommended to use a solid-state drive (SSD).

## Network Planning

In the production environment, after the high availability mode is enabled, it is recommended to use `10 Gigabit TCP/IP` network with redundancy protection.
It can be planned in advance through [specify the network card IP by modifying the network card](storage-eth.md).
