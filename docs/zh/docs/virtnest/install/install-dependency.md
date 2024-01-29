# 安装虚拟机模块的依赖和前提条件

本页说明安装虚拟机模块的依赖和前提条件。

!!! info

    下述命令或脚本内出现的 `virtnest` 字样是全局管理模块的内部开发代号。

## 前提条件

安装虚拟机模块之前，需要满足以下前提条件：

1. 操作系统内核版本需要在 3.15 以上。

2. CPU 需要支持 x86-64-v2 及以上指令集。

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

3. 虚拟机开启硬件虚拟化（嵌套虚拟化 nested virtualization）检查是否开启成功：

    ```sh
    lsmod | grep kvm
    # kvm_intel             245760  9
    # kvm                   745472  51 kvm_intel
    # irqbypass              16384  14 kvm
    ls /dev/ | grep kvm
    # kvm
    ```

    - 安装虚拟化工具（libvirt 和 qemu 软件包）
   
        ```sh
        # centos
        yum install -y qemu-kvm libvirt virt-install bridge-utils
        # ubuntu
        apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils
        ```
   
    - 查看节点是否支持kvm硬件虚拟化
   
        ```sh
        virt-host-validate qemu
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

    - 如果节点不支持，尝试执行以下命令

        ```sh
        kubectl -n kubevirt patch kubevirt kubevirt --type=merge --patch '{"spec":{"configuration":{"developerConfiguration":{"useEmulation":true}}}}'
        ```
