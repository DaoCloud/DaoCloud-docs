# 准备工作

## 平台准备

- Kubernetes 容器平台版本为 1.18+
- 已部署 CoreDNS

## 主机配置

- Linux 发行版：

  - CentOS/RHEL 7.4+
  - Rocky Linux 8.4+
  - Ubuntu 18+
  - Kylin 麒麟 V10

- 处理器架构：

  - x86_64
  - ARM64

- 软件依赖：

  1. 已安装 `LVM2`，如未安装请参考如下安装方式
  2. 高可用功能需要安装和当前运行的 Kernel 版本一致的 `kernel-devel`

LVM 安装：

=== "CentOS/RHEL, Rocky 和 Kylin"

    ```console
    yum install -y lvm2
    yum install -y kernel-devel-$(uname -r)
    ```

=== "Ubuntu"

    ```console
    apt-get install -y lvm2
    apt-get install -y linux-headers-$(uname -r)
    ```

### 磁盘类型

HwameiStor 支持物理硬盘(HDD)、固态硬盘(SSD) 和 NVMe 闪存盘.

测试环境里，每个主机必须要有至少一块空闲的 `10GiB` 数据盘。

生产环境里，建议每个主机至少要有一块空闲的 `200GiB` 数据盘，而且建议使用固态硬盘 (SSD)。

### 网络

生产环境里，开启高可用模式后，建议使用有冗余保护的`万兆 TCP/IP` 网络。可通过 [修改网卡的方式指定网卡 IP](StorageEth.md) 提前进行规划。

