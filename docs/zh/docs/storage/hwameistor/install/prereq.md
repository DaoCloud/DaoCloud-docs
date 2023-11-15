---
hide:
  - toc
---

# 准备工作

## 平台准备

- Kubernetes 容器平台版本兼容性：
    | Kubernetes     | v0.4.3 | >=v0.5.0 | >= 0.13.0 |
    | -------------- | ------ | -------- | --------- |
    | >=1.18&&<=1.20 | 是     | 否       |否       |
    | 1.21           | 是     | 是       |否       |
    | 1.22           | 是     | 是       |否       |
    | 1.23           | 是     | 是       |否       |
    | 1.24           | 是     | 是       |是       |
    | 1.25           | 否     | 是       |是       |
    | 1.26   | 否     | 是      | 是      |
    | 1.27           | 否     | 否       | 是       |
    | 1.28           | 否     | 否       | 是       |

- 已部署 CoreDNS

- 高可用功能需要安装和当前运行的 Kernel 版本一致的 `kernel-devel`，可通过命令检查：

    ```console
    uname -r
    3.10.0-1160.el7.x86_64
    yum list installed |grep kernel
    kernel.x86_64                        3.10.0-1160.el7                @anaconda   
    kernel-tools.x86_64                  3.10.0-1160.el7                @anaconda   
    kernel-tools-libs.x86_64             3.10.0-1160.el7                @anaconda  
    ```

    如不一致，可通过如下方式安装：

    ```console
    yum install -y kernel-devel-$(uname -r) # 安装 kernel-devel
    ```

- 已安装 `LVM2`，如未安装请参考如下安装方式:

=== "CentOS/RHEL、Rocky 和 Kylin"
  
    ```console
    yum install -y lvm2
    ```
    
=== "Ubuntu"
    
    ```console
    apt-get install -y lvm2
    apt-get install -y linux-headers-$(uname -r)
    ```

## 支持的操作系统

| **架构** | **支持操作系统**    | 推荐                      |
| -------- | ------------------- | ------------------------- |
| AMD 64   | centos 7.4+         | 操作系统推荐 CentOS 7.9   |
|          | Redhat 8.4+         | 操作系统推荐 Redhat 8.4   |
|          | Redhat 7.4+         | 操作系统推荐 Redhat 7.9   |
|          | Ubuntu 19+          | 操作系统推荐 Ubuntu 20.04 |
| ARM 64   | 银河麒麟 OS V10 SP2 | 银河麒麟 OS V10 SP2       |

## Secure Boot

高可用功能暂时不支持 `Secure Boot`，确认 `Secure Boot` 是 `disabled` 状态：

```console
$ mokutil --sb-state
SecureBoot disabled

$ dmesg | grep secureboot
[    0.000000] secureboot: Secure boot disabled
```

## 磁盘类型

HwameiStor 支持物理硬盘 (HDD)、固态硬盘 (SSD) 和 NVMe 闪存盘.

测试环境里，每个主机必须要有至少一块空闲的 `10GiB` 数据盘。

生产环境里，建议每个主机至少要有一块空闲的 `200GiB` 数据盘，而且建议使用固态硬盘 (SSD)。

## 网络规划

生产环境里，开启高可用模式后，建议使用有冗余保护的`万兆 TCP/IP` 网络。
可通过[修改网卡的方式指定网卡 IP](storage-eth.md) 提前进行规划。
