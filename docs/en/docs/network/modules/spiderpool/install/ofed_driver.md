# Install Nvidia OFED Driver

This article will describe how to install the Nvidia OFED driver on nodes through Kubernetes and manually.

## Environment Check

- Please ensure that the host has Mellanox series network cards by executing the following command in the host terminal:

    ```shell
    $ lspci -nn | grep Eth | grep Mellanox
    3b:00.0 Ethernet controller [0200]: Mellanox Technologies MT27800 Family [ConnectX-5] [15b3:1017]
    3b:00.1 Ethernet controller [0200]: Mellanox Technologies MT27800 Family [ConnectX-5] [15b3:1017]
    ```

    The above output indicates that the host has two Mellanox series network cards, with the model being ConnectX-5.

- Confirm whether the host has correctly installed the OFED driver

    ```shell
    $ ofed_info -s
    MLNX_OFED_LINUX-23.07-0.5.1.2:
    ```

    The above output indicates that the current host has installed the OFED driver. If the command does not exist, it means that it is not installed. If the above output is present, further check whether the RDMA device is correctly recognized:

    ```shell
    $ rdma link show
    link mlx5_0/1 state ACTIVE physical_state LINK_UP netdev enp4s0f0np0
    link mlx5_1/1 state ACTIVE physical_state LINK_UP netdev enp4s0f1np1

    $ ibdev2netdev
    mlx5_0 port 1 ==> enp4s0f0np0 (Up)
    mlx5_1 port 1 ==> enp4s0f1np1 (Up)
    ```

    The above output indicates that the RDMA environment of the host is ready. Otherwise, check the physical status of the network card (such as whether it is properly connected to the switch, etc.). If there is no problem with the physical link, follow the steps below to install the OFED driver.

## Install Driver

Different host operating systems require different installation methods. In order to meet the installation of different environments as much as possible, the following two methods, Kubernetes and manual, are introduced to install the OFED driver.

### Install through Kubernetes DaemonSet

We can create a DaemonSet in the cluster to help install the driver, but the following points should be noted:

- The supported image list currently only supports Ubuntu22.04, Ubuntu20.04, Ubuntu18.04, Centos8, RHEL8, and RHEL9 series operating system versions. And only x86 architecture is supported. For other operating systems and architectures, refer to the manual installation of the OFED driver section.

    | OS            | Kernel Version | Image Name                                                                 |
    | ------------- | -------------- | -------------------------------------------------------------------------- |
    | ubuntu22.04   | 5.15           | daocloud.io/nvidia/mellanox/mofed:23.10-0.5.5.0-ubuntu22.04-amd64         |
    | ubuntu20.04   | 5.4            | daocloud.io/nvidia/mellanox/mofed:23.10-0.5.5.0-ubuntu22.04-amd64         |
    | ubuntu18.04   | 4.15           | daocloud.io/daocloud/mellanox-mofed:23.07-0.5.0.0-ubuntu18.04-amd64       |
    | RHEL9         | 5.14.0         | daocloud.io/daocloud/mellanox-mofed:23.10-0.5.5.0-rhel9.0-amd64           |
    | RHEL8/Centos8 | 4.18.0         | daocloud.io/daocloud/mellanox-mofed:23.10-0.5.5.0-rhel8.8-amd64           |

- The operating systems or architectures of different nodes in the cluster may be different, and the same image may not be applicable to all nodes in the cluster. In this case, we should ensure that the pod runs on the specified node. Otherwise, the installation of the driver will fail due to the difference in the node operating system and architecture.

Below is the deployment manifest file of the DaemonSet. Note that you need to modify the nodeSelector field to ensure that the pod is scheduled to the node that needs to install the driver:

Here, take the node's operating system as Ubuntu22.04 and the architecture as x86 as an example:

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

    After creation, you can view the logs of the mofed pod to view the driver installation process.

    If the driver installation fails, the pod will continuously restart to attempt to reinstall the driver.

    If the installation is successful, the pod will sleep indefinitely. You can enter the pod and execute `ofed_info` to view the driver installation status.

### Manually Install

For scenarios where the driver cannot be installed through Kubernetes, such as unsupported images, we can choose manual installation:

- Check the host operating system, version, and CPU architecture

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

- Download the corresponding OFED driver version for the host architecture and operating system on the [Nvidia official website](https://network.nvidia.com/products/infiniband-drivers/linux/mlnx_ofed/):

    ![Download Driver](../../images/nvidia_ofed.png)

    !!! note

        Note that the current version needs to match the host's distribution, architecture, and operating system version.

        If you want to download earlier versions, click Archive Version to switch.

- Take downloading the ISO file as an example. Download the file and upload it to the host. Mount it to the `/mnt/` path and execute the installation command.

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

        1. Enter y to start the driver installation, which will take about 20 minutes. Please be patient.
        2. '--with-nvmf' and '--with-nfsrdma' are optional parameters, configure them as needed. You can enter --help to view details.

- If the firmware version of your network card is lower than the current driver firmware version, the firmware will be automatically updated.
  After the driver installation is successful, it will prompt to restart the driver `/etc/init.d/openibd restart`

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

- Restart the driver

    ```shell
    $ /etc/init.d/openibd restart
    Unloading HCA driver:                                      [  OK  ]
    Loading HCA driver and Access Layer:                       [  OK  ]
    ```

    If the execution fails, refer to the following errors:

    1. Restarting the driver fails due to opensm still running.

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

        Manually execute `systemctl stop opensmd` to fix this issue.

    2. The kernel module is being referenced and cannot be removed, causing the restart to fail.

        ```shell
        $ /etc/init.d/openibd restart
        Unloading mlx_compat                                       [FAILED]
        rmmod: ERROR: Module mlx_compat is in use by: nvme_core nvme_fabrics
        ```

        Use lsmod to view the modules: nvme_core and nvme_fabrics depend on each other. After uninstalling these modules in order, the problem can be solved.

        ```shell
        $ rmmod nvme_fabrics
        $ rmmod nvme_core
        $ rmmod mlx_compat
        $ /etc/init.d/openibd restart
        Unloading HCA driver:                                      [  OK  ]
        Loading HCA driver and Access Layer:                       [  OK  ]
        ```

- Check whether the driver is installed successfully

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

    The above output lists the installed OFED driver version and installed packages, indicating that the driver has been installed correctly.
