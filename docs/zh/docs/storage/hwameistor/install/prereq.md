---
hide:
  - toc
---

# 准备工作

## 平台准备

- Kubernetes 容器平台版本为 1.18+

- 已部署 CoreDNS

- 高可用功能需要安装和当前运行的 Kernel 版本一致的 `kernel-devel`

- 已安装 `LVM2`，如未安装请参考如下安装方式:

    === "CentOS/RHEL、Rocky 和 Kylin"
  
        ```console
        yum install -y lvm2
        yum install -y kernel-devel-$(uname -r)
        ```
  
    === "Ubuntu"
  
        ```console
        apt-get install -y lvm2
        apt-get install -y linux-headers-$(uname -r)
        ```

## 节点配置

| **架构** | **操作系统**        | **内核版本**                               | 备注                    |
| -------- | ------------------- | ------------------------------------------ | ----------------------- |
| AMD 64   | centos 7.X          | Kernel 3.10.0-1127.el7.x86_64 on an x86_64 | 操作系统推荐 CentOS 7.9 |
|          | Redhat 8.X          | 4.18.0-305.el8.x86_64                      | 操作系统推荐 Redhat 8.4 |
|          | Redhat 7.X          | 3.10.0-1160.e17.x86                        | 操作系统推荐 Redhat 7.9 |
| ARM 64   | 银河麒麟 OS V10 SP2 | 4.19.90-24.4.v2101.ky10.aarch64            | -                       |

## 磁盘类型

HwameiStor 支持物理硬盘 (HDD)、固态硬盘 (SSD) 和 NVMe 闪存盘.

测试环境里，每个主机必须要有至少一块空闲的 `10GiB` 数据盘。

生产环境里，建议每个主机至少要有一块空闲的 `200GiB` 数据盘，而且建议使用固态硬盘 (SSD)。

## 网络规划

生产环境里，开启高可用模式后，建议使用有冗余保护的`万兆 TCP/IP` 网络。
可通过[修改网卡的方式指定网卡 IP](storage-eth.md) 提前进行规划。
