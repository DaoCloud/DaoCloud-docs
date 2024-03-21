# 安装依赖和前提条件

本页说明安装虚拟机模块的依赖和前提条件。

!!! info

    下述命令或脚本内出现的 __virtnest__ 字样是全局管理模块的内部开发代号。

## 前提条件

目标集群所有节点的操作系统内核版本需要大于 3.15。您可以通过运行以下命令查看内核版本：

1. 操作系统内核版本需要在 3.15 以上。

    ```bash
    uname -a
    ```

    示例输出：

    ```output
    Linux master 6.5.3-1.el7.elrepo.x86_64 #1 SMP PREEMPT_DYNAMIC Wed Sep 13 11:46:28 EDT 2023 x86_64 x86_64 x86_64 GNU/Linux
    ```

2. CPU 需支持 x86-64-v2 及以上的指令集。您可以使用以下脚本检查当前节点的 CPU 是否支持：

    ```sh
    cat <<EOF > detect-cpu.sh
    #!/bin/sh -eu
    
    flags=$(cat /proc/cpuinfo | grep flags | head -n 1 | cut -d: -f2)
    
    supports_v2='awk "/cx16/&&/lahf/&&/popcnt/&&/sse4_1/&&/sse4_2/&&/ssse3/ {found=1} END {exit !found}"'
    supports_v3='awk "/avx/&&/avx2/&&/bmi1/&&/bmi2/&&/f16c/&&/fma/&&/abm/&&/movbe/&&/xsave/ {found=1} END {exit !found}"'
    supports_v4='awk "/avx512f/&&/avx512bw/&&/avx512cd/&&/avx512dq/&&/avx512vl/ {found=1} END {exit !found}"'
    
    echo "$flags" | eval $supports_v2 || exit 2 && echo "CPU supports x86-64-v2"
    echo "$flags" | eval $supports_v3 || exit 3 && echo "CPU supports x86-64-v3"
    echo "$flags" | eval $supports_v4 || exit 4 && echo "CPU supports x86-64-v4"
    EOF
    chmod +x detect-cpu.sh
    sh detect-cpu.sh
    ```

3. 所有节点必须启用硬件虚拟化（嵌套虚拟化）。您可以通过运行以下命令检查：

    ```sh
    virt-host-validate qemu
    ```

    ```sh
    # 成功的情况
    QEMU: Checking for hardware virtualization                                 : PASS
    QEMU: Checking if device /dev/kvm exists                                   : PASS
    QEMU: Checking if device /dev/kvm is accessible                            : PASS
    QEMU: Checking if device /dev/vhost-net exists                             : PASS
    QEMU: Checking if device /dev/net/tun exists                               : PASS
    QEMU: Checking for cgroup 'cpu' controller support                         : PASS
    QEMU: Checking for cgroup 'cpuacct' controller support                     : PASS
    QEMU: Checking for cgroup 'cpuset' controller support                      : PASS
    QEMU: Checking for cgroup 'memory' controller support                      : PASS
    QEMU: Checking for cgroup 'devices' controller support                     : PASS
    QEMU: Checking for cgroup 'blkio' controller support                       : PASS
    QEMU: Checking for device assignment IOMMU support                         : PASS
    QEMU: Checking if IOMMU is enabled by kernel                               : PASS
    QEMU: Checking for secure guest support                                    : WARN (Unknown if this platform has Secure Guest support)
    
    # 失败的情况
    QEMU: Checking for hardware virtualization                                 : FAIL (Only emulated CPUs are available, performance will be significantly limited)
    QEMU: Checking if device /dev/vhost-net exists                             : PASS
    QEMU: Checking if device /dev/net/tun exists                               : PASS
    QEMU: Checking for cgroup 'memory' controller support                      : PASS
    QEMU: Checking for cgroup 'memory' controller mount-point                  : PASS
    QEMU: Checking for cgroup 'cpu' controller support                         : PASS
    QEMU: Checking for cgroup 'cpu' controller mount-point                     : PASS
    QEMU: Checking for cgroup 'cpuacct' controller support                     : PASS
    QEMU: Checking for cgroup 'cpuacct' controller mount-point                 : PASS
    QEMU: Checking for cgroup 'cpuset' controller support                      : PASS
    QEMU: Checking for cgroup 'cpuset' controller mount-point                  : PASS
    QEMU: Checking for cgroup 'devices' controller support                     : PASS
    QEMU: Checking for cgroup 'devices' controller mount-point                 : PASS
    QEMU: Checking for cgroup 'blkio' controller support                       : PASS
    QEMU: Checking for cgroup 'blkio' controller mount-point                   : PASS
    WARN (Unknown if this platform has IOMMU support)
    ```

4. 安装 virt-host-validate：

    1. 在 CentOS 上安装：

        ```bash
        yum install -y qemu-kvm libvirt virt-install bridge-utils
        ```

    2. 在 Ubuntu 上安装：

        ```bash
        apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils
        ```

5. 如果集群使用 Docker Engine 作为容器运行时，则 Docker Engine 版本需要大于 20.10.10。
   并且为了后续功能做准备，建议开启 IOMMU。
