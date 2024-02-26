# Install Dependencies

This page explains the dependencies and prerequisites for installing the virtual machine module.

!!! info

    The term `virtnest` appearing in the following commands or scripts is the internal development code name for the global management module.

## Prerequisites

Before installing the virtual machine module, the following prerequisites need to be met:

1. The operating system kernel version needs to be above 3.15.

2. The CPU needs to support the x86-64-v2 and above instruction sets.

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

3. Check if hardware virtualization (nested virtualization) for virtual machines is enabled:

    ```sh
    lsmod | grep kvm
    # kvm_intel             245760  9
    # kvm                   745472  51 kvm_intel
    # irqbypass              16384  14 kvm
    ls /dev/ | grep kvm
    # kvm
    ```

    - Install virtualization tools (libvirt and qemu packages)

        ```sh
        # CentOS
        yum install -y qemu-kvm libvirt virt-install bridge-utils
        # Ubuntu
        apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils
        ```

    - Check if the node supports KVM hardware virtualization

        ```sh
        virt-host-validate qemu
        # Successful scenario
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
        
        # Failed scenario
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

    - If the node does not support, try executing the following command

        ```sh
        kubectl -n kubevirt patch kubevirt kubevirt --type=merge --patch '{"spec":{"configuration":{"developerConfiguration":{"useEmulation":true}}}}'
        ```
