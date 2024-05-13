---
MTPE: windsonsea
date: 2024-05-13
---

# Dependencies and Prerequisites

This page explains the dependencies and prerequisites for installing the virtual machine module.

!!! info

    The term __virtnest__ mentioned in the commands or scripts below is the internal development codename for the global management module.

## Prerequisites

The kernel version of all nodes in the target cluster needs to be greater than 3.15. You can check the kernel version by running the following command:

1. The kernel version needs to be above 3.15.

    ```bash
    uname -a
    ```

    Example output:

    ```output
    Linux master 6.5.3-1.el7.elrepo.x86_64 #1 SMP PREEMPT_DYNAMIC Wed Sep 13 11:46:28 EDT 2023 x86_64 x86_64 x86_64 GNU/Linux
    ```

2. The CPU must support the x86-64-v2 instruction set or higher. You can use the following script to check if the current node's CPU supports this:

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

3. All nodes must have hardware virtualization (nested virtualization) enabled. You can check by running the following command:

    ```sh
    virt-host-validate qemu
    ```

    ```sh
    # Successful case
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
    
    # Failure case
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

4. Install virt-host-validate:

    1. On CentOS:

        ```bash
        yum install -y qemu-kvm libvirt virt-install bridge-utils
        ```

    2. On Ubuntu:

        ```bash
        apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils
        ```

5. If the cluster uses Docker Engine as the container runtime, then the Docker Engine needs to be greater than v20.10.10.

6. To prepare for future functionality, it is recommended to enable IOMMU.
