---
MTPE: ModetaNiu
date: 2024-08-01
---

# Dependencies and Prerequisites

This page explains the dependencies and prerequisites for installing virtual machine.

!!! info

    The term __virtnest__ mentioned in the commands or scripts below is the internal development codename for 
    the Global Management module.

## Prerequisites

### Kernel version being above v4.11

The kernel version of all nodes in the target cluster needs to be higher than v4.11. For detail information,
see [kubevirt issue](https://github.com/kubevirt/kubevirt/issues/11886). Run the following command to see the version:

```bash
uname -a
```

Example output:

```output
Linux master 6.5.3-1.el7.elrepo.x86_64 #1 SMP PREEMPT_DYNAMIC Wed Sep 13 11:46:28 EDT 2023 x86_64 x86_64 x86_64 GNU/Linux
```

### CPU supporting x86-64-v2 instruction set or higher

You can use the following script to check if the current node's CPU is usable:

!!! note  

    If you encounter a message like the one shown below, you can safely ignore it as it does not impact the final result.
    
    ```bash title="示例"
    $ sh detect-cpu.sh
    detect-cpu.sh: line 3: fpu: command not found
    ```   
    
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

### All Nodes having hardware virtualization (nested virtualization) enabled

* Run the following command to check if it has been achieved: 

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

* Install virt-host-validate:

    === "On CentOS"

        ```bash
        yum install -y qemu-kvm libvirt virt-install bridge-utils
        ```

    === "On Ubuntu"

        ```bash
        apt install qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils
        ```

* Methods to enable hardware virtualization

    Methods vary from platforms, and this page takes vsphere as an example.
    See [vmware website](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-2A98801C-68E8-47AF-99ED-00C63E4857F6.html).

### If using Docker Engine as the container runtime

If Docker Engine is used as the container runtime, it must be higher than v20.10.10.

### Enabling IOMMU is recommended

To prepare for future functions, it is recommended to enable IOMMU.
