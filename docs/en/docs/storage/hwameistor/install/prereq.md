---
hide:
   - toc
---

# Preparation

## Platform Preparation

- Kubernetes compatibility:

    | Kubernetes     | Hwameistor V0.4.3 | Hwameistor >=v0.5.0 | Hwameistor >= 0.13.0 |
    | -------------- | ----------------- | ------------------- | -------------------- |
    | >=1.18&&<=1.20 | Yes                | No                  | No                   |
    | 1.21           | Yes                | Yes                  | No                   |
    | 1.22           | Yes                | Yes                  | No                   |
    | 1.23           | Yes                | Yes                  | No                   |
    | 1.24           | Yes                | Yes                  | Yes                   |
    | 1.25           | No                | Yes                  | Yes                   |
    | 1.26           | No                | Yes                  | Yes                   |
    | 1.27           | No                | No                  | Yes                   |
    | 1.28           | No                | No                  | Yes                   |

- CoreDNS must be deployed

- For high availability, `kernel-devel` consistent with the currently running Kernel version should be installed. You can run the following command to check:

    ```console
    uname -r
    3.10.0-1160.el7.x86_64
    yum list installed |grep kernel
    kernel.x86_64                        3.10.0-1160.el7                @anaconda   
    kernel-tools.x86_64                  3.10.0-1160.el7                @anaconda   
    kernel-tools-libs.x86_64             3.10.0-1160.el7                @anaconda  
    ```

    If inconsistent, install `kernel-devel` with the following command:

    ```bash
    yum install -y kernel-devel-$(uname -r)
    ```

- If `LVM2` is not installed, please refer to the appropriate installation method below:

=== "CentOS/RHEL, Rocky, and Kylin"
  
    ```console
    yum install -y lvm2
    ```
    
=== "Ubuntu"
    
    ```console
    apt-get install -y lvm2
    apt-get install -y linux-headers-$(uname -r)
    ```

## Supported Operating Systems

| **Architecture** | **Supported Operating Systems** | Recommended               |
| ---------------- | ------------------------------ | ------------------------- |
| AMD 64           | CentOS 7.4+                     | Recommended: CentOS 7.9  |
|                  | Red Hat 8.4+                    | Recommended: Red Hat 8.4 |
|                  | Red Hat 7.4+                    | Recommended: Red Hat 7.9 |
| ARM 64           | Kylin OS V10 SP2                | Kylin OS V10 SP2          |

## Secure Boot

The high availability feature does not currently support `Secure Boot`.
Please ensure that `Secure Boot` is in a disabled state.

```console
$ mokutil --sb-state
SecureBoot disabled

$ dmesg | grep secureboot
[    0.000000] secureboot: Secure boot disabled
```

## Disk Types

HwameiStor supports physical hard disk drives (HDD), solid-state drives (SSD), and NVMe flash drives.

In a test environment, each host must have at least one free `10GiB` data disk.

In a production environment, it is recommended that each host have at least one free `200GiB` data disk, and it is recommended to use a solid-state drive (SSD).

## Network Planning

In a production environment, after enabling high availability mode, it is recommended to use
`10 Gigabit TCP/IP` network with redundancy protection. The network can be planned in advance
by specifying the network card IP through [modifying the network card](storage-eth.md).
