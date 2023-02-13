# Preparation

- Kubernetes

    - Kubernetes 1.18+
    - Deploy CoreDNS

- Unsupported platforms

    - Openshift
    - Rancher

!!! note

    The above platforms are not currently supported, but are planned to be supported in the future.

## host configuration

- Linux distributions:

    - CentOS/RHEL 7.4+
    - Rocky Linux 8.4+
    - Ubuntu 18+
    - Kylin Kirin V10

- Processor architecture:

    - x86_64
    - ARM64

- Software dependencies:

    1. Install `LVM2`
    2. The high-availability function needs to install `kernel-devel` that is consistent with the version of the currently running kernel

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

### Data Disk

HwameiStor supports physical hard drives (HDDs), solid state drives (SSDs) and NVMe flash drives.

In the test environment, each host must have at least one free `10GiB` data disk.

In a production environment, it is recommended that each host has at least one free `200GiB` data disk, and it is recommended to use a solid-state drive (SSD).

### Network

In the production environment, after the high availability mode is enabled, it is recommended to use `10 Gigabit TCP/IP` network with redundancy protection.