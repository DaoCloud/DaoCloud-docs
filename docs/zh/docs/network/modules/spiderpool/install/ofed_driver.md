# 安装 Nvidia OFED 驱动

本文将介绍如何通过以 Kubernetes 和 手动 的方式在节点安装英伟达 OFED 驱动.

## 环境检查

- 请确保主机具备 Mellanox 系列网卡，可通过在主机终端执行以下命令确认:

    ```shell
    $ lspci -nn | grep Eth | grep Mellanox
    3b:00.0 Ethernet controller [0200]: Mellanox Technologies MT27800 Family [ConnectX-5] [15b3:1017]
    3b:00.1 Ethernet controller [0200]: Mellanox Technologies MT27800 Family [ConnectX-5] [15b3:1017]
    ```

    以上输出表示主机具备两张 Mellanox 系列网卡, 其型号是 ConnectX-5。

- 确认主机是否已经正确安装 OFED 驱动

    ```shell
    $ ofed_info -s
    MLNX_OFED_LINUX-23.07-0.5.1.2:
    ```

    以上输出说明当前主机已经安装 OFED 驱动，如果提示命令不存在则说明未安装。如果有以上输出进一步检查 RDMA 设备是否正确识别:

    ```shell
    $ rdma link show
    link mlx5_0/1 state ACTIVE physical_state LINK_UP netdev enp4s0f0np0
    link mlx5_1/1 state ACTIVE physical_state LINK_UP netdev enp4s0f1np1

    $ ibdev2netdev
    mlx5_0 port 1 ==> enp4s0f0np0 (Up)
    mlx5_1 port 1 ==> enp4s0f1np1 (Up)
    ```

    以上输出说明该主机的 RDMA 环境已经就绪。否则先检查网卡的物理状态（比如是否正常接入到交换机等等）。
    如果物理链路没问题，按照下面的步骤安装 OFED 驱动。

## 安装驱动

主机的操作系统不同，安装的方式也所不同。为了尽量满足不同的环境安装驱动，下面分别介绍通过 Kubernetes 和 手动两种方式安装 OFED 驱动。

### 通过 Kubernetes DaemonSet 安装

我们可以通过在集群中创建一个 DaemonSet, 由这个 DaemonSet 来帮助安装驱动，但需要注意以下几点事项:

- 目前支持镜像列表只支持 Ubuntu22.04、Ubuntu20.04、Ubuntu18.04 以及 Centos8、RHEL8、RHEL9 系列的操作系统版本。
  并且只支持 x86 架构。对于其他操作系统和架构，可按照手动安装 OFED 驱动章节。

    | OS            | 内核版本 | 镜像名称                                                            |
    | ------------- | -------- | ------------------------------------------------------------------- |
    | ubuntu22.04   | 5.15     | daocloud.io/nvidia/mellanox/mofed:23.10-0.5.5.0-ubuntu22.04-amd64   |
    | ubuntu20.04   | 5.4      | daocloud.io/nvidia/mellanox/mofed:23.10-0.5.5.0-ubuntu22.04-amd64   |
    | ubuntu18.04   | 4.15     | daocloud.io/daocloud/mellanox-mofed:23.07-0.5.0.0-ubuntu18.04-amd64 |
    | RHEL9         | 5.14.0   | daocloud.io/daocloud/mellanox-mofed:23.10-0.5.5.0-rhel9.0-amd64     |
    | RHEL8/Centos8 | 4.18.0   | daocloud.io/daocloud/mellanox-mofed:23.10-0.5.5.0-rhel8.8-amd64     |

- 集群不同节点的操作系统或架构可能是不同的，同一个镜像可能无法适用于集群所有节点。这种情况下，
  我们应该确保 Pod 运行在指定的节点。否则因为节点操作系统和架构的不同而导致安装驱动失败。

下面是 DaemonSet 的部署清单文件，注意修改 nodeSelector 字段以确保 Pod 调度到需要安装驱动的节点上：

这里以节点的操作系统为 Ubuntu22.04，架构为 x86 为例：

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: mofed
  namespace: kube-system
spec:
  selector:
    matchLabels:
      driver-pod: mofed-22.04-0.5.3.3.1
    metadata:
      name: mofed
      labels:
        app: mofed-ubuntu22.04
        driver-pod: mofed-22.04-0.5.3.3.1
        nvidia.com/ofed-driver: ""
    spec:
      containers:
        - image: nvcr.io/nvidia/mellanox/mofed:23.10-0.5.5.0-rhel8.6-amd64
          imagePullPolicy: IfNotPresent
          name: mofed-container
          securityContext:
            privileged: true
            seLinuxOptions:
              level: s0
          volumeMounts:
            - mountPath: /run/mellanox/drivers
              mountPropagation: Bidirectional
              name: run-mlnx-ofed
            - mountPath: /etc/network
              name: etc-network
            - mountPath: /host/etc
              name: host-etc
            - mountPath: /host/usr
              name: host-usr
            - mountPath: /host/lib/udev
              name: host-udev
            - mountPath: /host/lib/modules
              name: host-lib-modules
      hostNetwork: true
      volumes:
        - hostPath:
            path: /run/mellanox/drivers
            type: ""
          name: run-mlnx-ofed
        - hostPath:
            path: /etc/network
            type: ""
          name: etc-network
        - hostPath:
            path: /etc
            type: ""
          name: host-etc
        - hostPath:
            path: /usr
            type: ""
          name: host-usr
        - hostPath:
            path: /lib/udev
            type: ""
          name: host-udev
        - hostPath:
            path: /lib/modules
            type: ""
          name: host-lib-modules
```

!!! note 

    创建后可通过查看 mofed Pod 的日志查看驱动安装过程

    如果安装驱动失败，Pod 会不断重启尝试重新安装驱动。

    如果安装成功，Pod 将会无限期 Sleep, 可进入到 Pod 执行 `ofed_info` 查看驱动安装情况。

### 手动安装

对于无法通过 Kubernetes 安装驱动的场景: 比如镜像不支持等。我们可以选择手动方式安装:

- 检查主机操作系统和版本和 CPU 架构

    ```yaml
    Static hostname: 10-20-1-20
      Icon name: computer-server
      Chassis: server
        Machine ID: 12998dac94434e66aaf6546cb42b9c93
        Boot ID: 852a0d1c0382438a98e84591f322fc36
    Operating System: Ubuntu 22.04.3 LTS
        Kernel: Linux 5.15.0-91-generic
        Architecture: x86-64
    Hardware Vendor: Lenovo
    Hardware Model: -_7X06CTO1WW_-
    ```

- 在[英伟达官网](https://network.nvidia.com/products/infiniband-drivers/linux/mlnx_ofed/)下载主机架构、操作系统对应的 OFED 驱动版本：

    ![下载驱动](../../../images/nvidia_ofed.png)

    !!! note

        注意目前需要匹配到主机的发行版、架构以及操作系统版本。

        如果想要下载早期版本，请点击 Archive Version 切换。

- 本文以下载 iso 文件为例，下载文件并上传到主机。挂载到 `/mnt` 路径并执行安装命令。

    ```shell
    root@10-20-1-20:~/install# mount MLNX_OFED_LINUX-23.10-1.1.9.0-ubuntu22.04-x86_64.iso /mnt/
    mount: /mnt: WARNING: source write-protected, mounted read-only.
    root@10-20-1-20:/mnt# ./mlnxofedinstall --with-nvmf --with-nfsrdma --all
    Logs dir: /tmp/MLNX_OFED_LINUX.86055.logs
    General log file: /tmp/MLNX_OFED_LINUX.86055.logs/general.log

    Below is the list of MLNX_OFED_LINUX packages that you have chosen
    (some may have been added by the installer due to package dependencies):

    ofed-scripts
    mlnx-tools
    mlnx-ofed-kernel-utils
    mlnx-ofed-kernel-dkms
    iser-dkms
    isert-dkms
    srp-dkms
    mlnx-nfsrdma-dkms
    mlnx-nvme-dkms
    rdma-core
    libibverbs1
    ibverbs-utils
    ibverbs-providers
    libibverbs-dev
    libibverbs1-dbg
    libibumad3
    libibumad-dev
    ibacm
    librdmacm1
    rdmacm-utils
    librdmacm-dev
    mstflint
    ibdump
    libibmad5
    libibmad-dev
    libopensm
    opensm
    opensm-doc
    libopensm-devel
    libibnetdisc5
    infiniband-diags
    mft
    kernel-mft-dkms
    perftest
    ibutils2
    ibsim
    ibsim-doc
    ucx
    sharp
    hcoll
    knem-dkms
    knem
    openmpi
    mpitests
    dpcp
    srptools
    mlnx-ethtool
    mlnx-iproute2
    rshim
    ibarr

    This program will install the MLNX_OFED_LINUX package on your machine.
    Note that all other Mellanox, OEM, OFED, RDMA or Distribution IB packages will be removed.
    Those packages are removed due to conflicts with MLNX_OFED_LINUX, do not reinstall them.

    Do you want to continue?[y/N]:
    ```

    !!! note

        1. 输入 y 开始安装驱动，大概需要 20 分钟，请耐心等待
        2. '--with-nvmf' 和 '--with-nfsrdma' 是可选参数，按需配置。可输入 --help 查看详情

- 如果您的网卡固件版本低于当前驱动固件版本，则会自动更新固件。
  当驱动安装成功后，提示重启驱动 `/etc/init.d/openibd restart`

    ```shell
    ...
    Device (86:00.0):
        86:00.0 Infiniband controller: Mellanox Technologies MT27800 Family [ConnectX-5]
        Link Width: x16
        PCI Link Speed: 8GT/s

    Device (86:00.1):
        86:00.1 Ethernet controller: Mellanox Technologies MT27800 Family [ConnectX-5]
        Link Width: x16
        PCI Link Speed: 8GT/s

    Device (af:00.0):
        af:00.0 Ethernet controller: Mellanox Technologies MT27800 Family [ConnectX-5]
        Link Width: x8
        PCI Link Speed: 8GT/s

    Device (af:00.1):
        af:00.1 Ethernet controller: Mellanox Technologies MT27800 Family [ConnectX-5]
        Link Width: x8
        PCI Link Speed: 8GT/s

    Installation passed successfully
    To load the new driver, run:
    /etc/init.d/openibd restart
    Note: In order to load the new nvme-rdma and nvmet-rdma modules, the nvme module must be reloaded.
    ```

- 重新启动驱动

    ```shell
    $ /etc/init.d/openibd restart
    Unloading HCA driver:                                      [  OK  ]
    Loading HCA driver and Access Layer:                       [  OK  ]
    ```

    如果执行失败，可参考以下错误：

    1. 由于 opensm 仍然在运行导致重启驱动失败。

        ```shell
        $ /etc/init.d/openibd restart
        Please stop "opensm" and all applications running over InfiniBand.

        Please stop the following applications still using Infiniband devices:
        opensm(1632) user root is using device issm0
        opensm(1632) user root is using device umad0


        Error: Cannot unload the Infiniband driver stack due to the above issue(s)!

        Once the above issue(s) resolved, run:
        # /etc/init.d/openibd restart
        ```

        手动执行 `systemctl stop opensmd` 可修复这个问题。

    2. 内核 module 正被引用，无法移除导致重启失败

        ```shell
        $ /etc/init.d/openibd restart
        Unloading mlx_compat                                       [FAILED]
        rmmod: ERROR: Module mlx_compat is in use by: nvme_core nvme_fabrics
        ```

        通过 lsmod 查看 module: nvme_core 和 nvme_fabrics 之间相互依赖关系，按顺序依次卸载这些 modules 后，解决这个问题。

        ```shell
        $ rmmod nvme_fabrics
        $ rmmod nvme_core
        $ rmmod mlx_compat
        $ /etc/init.d/openibd restart
        Unloading HCA driver:                                      [  OK  ]
        Loading HCA driver and Access Layer:                       [  OK  ]
        ```

- 检查驱动是否安装成功

    ```shell
    $ ofed_info
    MLNX_OFED_LINUX-23.10-1.1.9.0 (OFED-23.10-1.1.9):

    clusterkit:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/clusterkit-1.11.442-1.2310055.src.rpm

    dpcp:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/dpcp-1.1.43-1.2310055.src.rpm

    hcoll:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/hcoll-4.8.3223-1.2310055.src.rpm

    ibarr:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/ibarr-0.1.3-1.2310055.src.rpm

    ibdump:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/ibdump-6.0.0-1.2310055.src.rpm

    ibsim:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/ibsim-0.12-1.2310055.src.rpm

    ibutils2:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/ibutils2-2.1.1-0.1.MLNX20231105.g79770a56.2310055.src.rpm

    iser:
    mlnx_ofed/mlnx-ofa_kernel-4.0.git mlnx_ofed_23_10
    commit a675be032c722b022cd9166921fbc6195e7fe8ff

    isert:
    mlnx_ofed/mlnx-ofa_kernel-4.0.git mlnx_ofed_23_10
    commit a675be032c722b022cd9166921fbc6195e7fe8ff

    kernel-mft:
    mlnx_ofed_mft/kernel-mft-4.26.1-3.src.rpm

    knem:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/knem-1.1.4.90mlnx3-OFED.23.10.0.2.1.1.src.rpm

    libvma:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/libvma-9.8.40-1.src.rpm

    libxlio:
    /sw/release/sw_acceleration/xlio/libxlio-3.20.8-1.src.rpm

    mlnx-dpdk:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/mlnx-dpdk-22.11.0-2310.1.0.2310055.src.rpm

    mlnx-en:
    mlnx_ofed/mlnx-ofa_kernel-4.0.git mlnx_ofed_23_10
    commit a675be032c722b022cd9166921fbc6195e7fe8ff

    mlnx-ethtool:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/mlnx-ethtool-6.4-1.2310055.src.rpm

    mlnx-iproute2:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/mlnx-iproute2-6.4.0-1.2310055.src.rpm

    mlnx-nfsrdma:
    mlnx_ofed/mlnx-ofa_kernel-4.0.git mlnx_ofed_23_10
    commit a675be032c722b022cd9166921fbc6195e7fe8ff

    mlnx-nvme:
    mlnx_ofed/mlnx-ofa_kernel-4.0.git mlnx_ofed_23_10
    commit a675be032c722b022cd9166921fbc6195e7fe8ff

    mlnx-ofa_kernel:
    mlnx_ofed/mlnx-ofa_kernel-4.0.git mlnx_ofed_23_10
    commit a675be032c722b022cd9166921fbc6195e7fe8ff

    mlnx-tools:
    https://github.com/Mellanox/mlnx-tools mlnx_ofed
    commit d3edfb102ad4c3103796192b3719a5f9cd24c7f9
    mlx-steering-dump:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/mlx-steering-dump-1.0.0-0.2310055.src.rpm

    mpitests:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/mpitests-3.2.21-8418f75.2310055.src.rpm

    mstflint:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/mstflint-4.16.1-2.2310055.src.rpm

    multiperf:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/multiperf-3.0-3.0.2310055.src.rpm

    ofed-docs:
    docs.git mlnx_ofed-4.0
    commit 3d1b0afb7bc190ae5f362223043f76b2b45971cc

    openmpi:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/openmpi-4.1.7a1-1.2310055.src.rpm

    opensm:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/opensm-5.17.0.MLNX20231105.d437ae0a-0.1.2310055.src.rpm

    openvswitch:
    https://gitlab-master.nvidia.com/sdn/ovs mlnx_ofed_23_10
    commit c5eb44be9b4d8ee0f6b367b439c582f3487cc741

    perftest:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/perftest-23.10.0-0.29.g0705c22.2310055.src.rpm

    rdma-core:
    mlnx_ofed/rdma-core.git mlnx_ofed_23_10
    commit 6c404a661569eb130be94df67f8a98e6794c0c35
    rshim:
    mlnx_ofed_soc/rshim-2.0.17-0.g0caa378.src.rpm

    sharp:
    mlnx_ofed_sharp/sharp-3.5.1.MLNX20231116.7fcef5af.tar.gz

    sockperf:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/sockperf-3.10-0.git5ebd327da983.2310055.src.rpm

    srp:
    mlnx_ofed/mlnx-ofa_kernel-4.0.git mlnx_ofed_23_10
    commit a675be032c722b022cd9166921fbc6195e7fe8ff

    ucx:
    mlnx_ofed_ucx/ucx-1.16.0-1.src.rpm

    xpmem-lib:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/xpmem-lib-2.7-0.2310055.src.rpm

    xpmem:
    /sw/release/mlnx_ofed/IBHPC/MLNX_OFED_LINUX-23.10-0.5.5/SRPMS/xpmem-2.7.3-1.2310055.src.rpm


    Installed Packages:
    -------------------
    ii  dpcp                                  1.1.43-1.2310055                         amd64        Direct Packet Control Plane (DPCP) is a library to use Devx
    ii  hcoll                                 4.8.3223-1.2310055                       amd64        Hierarchical collectives (HCOLL)
    ii  ibacm                                 2307mlnx47-1.2310119                     amd64        InfiniBand Communication Manager Assistant (ACM)
    ii  ibarr:amd64                           0.1.3-1.2310055                          amd64        Nvidia address and route userspace resolution services for Infiniband
    ii  ibdump                                6.0.0-1.2310055                          amd64        Mellanox packets sniffer tool
    ii  ibsim                                 0.12-1.2310055                           amd64        InfiniBand fabric simulator for management
    ii  ibsim-doc                             0.12-1.2310055                           all          documentation for ibsim
    ii  ibutils2                              2.1.1-0.1.MLNX20231105.g79770a56.2310055 amd64        OpenIB Mellanox InfiniBand Diagnostic Tools
    ii  ibverbs-providers:amd64               2307mlnx47-1.2310119                     amd64        User space provider drivers for libibverbs
    ii  ibverbs-utils                         2307mlnx47-1.2310119                     amd64        Examples for the libibverbs library
    ii  infiniband-diags                      2307mlnx47-1.2310119                     amd64        InfiniBand diagnostic programs
    ii  iser-dkms                             23.10.OFED.23.10.1.1.9.1-1               all          DKMS support fo iser kernel modules
    ii  isert-dkms                            23.10.OFED.23.10.1.1.9.1-1               all          DKMS support fo isert kernel modules
    ii  kernel-mft-dkms                       4.26.1.3-1                               all          DKMS support for kernel-mft kernel modules
    ii  knem                                  1.1.4.90mlnx3-OFED.23.10.0.2.1.1         amd64        userspace tools for the KNEM kernel module
    ii  knem-dkms                             1.1.4.90mlnx3-OFED.23.10.0.2.1.1         all          DKMS support for mlnx-ofed kernel modules
    ii  libibmad-dev:amd64                    2307mlnx47-1.2310119                     amd64        Development files for libibmad
    ii  libibmad5:amd64                       2307mlnx47-1.2310119                     amd64        Infiniband Management Datagram (MAD) library
    ii  libibnetdisc5:amd64                   2307mlnx47-1.2310119                     amd64        InfiniBand diagnostics library
    ii  libibumad-dev:amd64                   2307mlnx47-1.2310119                     amd64        Development files for libibumad
    ii  libibumad3:amd64                      2307mlnx47-1.2310119                     amd64        InfiniBand Userspace Management Datagram (uMAD) library
    ii  libibverbs-dev:amd64                  2307mlnx47-1.2310119                     amd64        Development files for the libibverbs library
    ii  libibverbs1:amd64                     2307mlnx47-1.2310119                     amd64        Library for direct userspace use of RDMA (InfiniBand/iWARP)
    ii  libibverbs1-dbg:amd64                 2307mlnx47-1.2310119                     amd64        Debug symbols for the libibverbs library
    ii  libopensm                             5.17.0.MLNX20231105.d437ae0a-0.1.2310055 amd64        Infiniband subnet manager libraries
    ii  libopensm-devel                       5.17.0.MLNX20231105.d437ae0a-0.1.2310055 amd64        Development files for OpenSM
    ii  librdmacm-dev:amd64                   2307mlnx47-1.2310119                     amd64        Development files for the librdmacm library
    ii  librdmacm1:amd64                      2307mlnx47-1.2310119                     amd64        Library for managing RDMA connections
    ii  mlnx-ethtool                          6.4-1.2310055                            amd64        This utility allows querying and changing settings such as speed,
    ii  mlnx-iproute2                         6.4.0-1.2310055                          amd64        This utility allows querying and changing settings such as speed,
    ii  mlnx-nfsrdma-dkms                     23.10.OFED.23.10.1.1.9.1-1               all          DKMS support for NFS RDMA kernel module
    ii  mlnx-nvme-dkms                        23.10.OFED.23.10.1.1.9.1-1               all          DKMS support for nvme kernel module
    ii  mlnx-ofed-kernel-dkms                 23.10.OFED.23.10.1.1.9.1-1               all          DKMS support for mlnx-ofed kernel modules
    ii  mlnx-ofed-kernel-utils                23.10.OFED.23.10.1.1.9.1-1               amd64        Userspace tools to restart and tune mlnx-ofed kernel modules
    ii  mlnx-tools                            23.10.0-1.2310119                        amd64        Userspace tools to restart and tune MLNX_OFED kernel modules
    ii  mpitests                              3.2.21-8418f75.2310055                   amd64        Set of popular MPI benchmarks and tools IMB 2018 OSU benchmarks ver 4.0.1 mpiP-3.3
    ii  mstflint                              4.16.1-2.2310055                         amd64        Mellanox firmware burning application
    ii  openmpi                               4.1.7a1-1.2310055                        all          Open MPI
    ii  opensm                                5.17.0.MLNX20231105.d437ae0a-0.1.2310055 amd64        An Infiniband subnet manager
    ii  opensm-doc                            5.17.0.MLNX20231105.d437ae0a-0.1.2310055 amd64        Documentation for opensm
    ii  perftest                              23.10.0-0.29.g0705c22.2310055            amd64        Infiniband verbs performance tests
    ii  rdma-core                             2307mlnx47-1.2310119                     amd64        RDMA core userspace infrastructure and documentation
    ii  rdmacm-utils                          2307mlnx47-1.2310119                     amd64        Examples for the librdmacm library
    ii  rshim                                 2.0.17-0.g0caa378.2310119                amd64        driver for Mellanox BlueField SoC
    ii  sharp                                 3.5.1.MLNX20231116.7fcef5af-1.2310119    amd64        SHArP switch collectives
    ii  srp-dkms                              23.10.OFED.23.10.1.1.9.1-1               all          DKMS support fo srp kernel modules
    ii  srptools                              2307mlnx47-1.2310119                     amd64        Tools for Infiniband attached storage (SRP)
    ii  ucx                                   1.16.0-1.2310119                         amd64        Unified Communication X
    ```

    以上输出列出了安装的 OFED 驱动版本和已经安装的 package，这表明驱动已经被正确的安装。
