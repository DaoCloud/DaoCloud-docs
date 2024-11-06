# RHEL 9.2 离线安装 gpu-operator 驱动

前提条件：已安装 gpu-operator v23.9.0+2 及更高版本

RHEL 9.2 驱动镜像不能直接安装，官方的驱动脚本存在一点问题，在官方修复之前，提供如下的步骤来实现离线安装驱动。

## 禁用nouveau驱动

在 RHEL 9.2 中存在 `nouveau` 非官方的 `Nvidia` 驱动，因此需要先禁用。 

```shell
# 创建一个新的文件
sudo vi /etc/modprobe.d/blacklist-nouveau.conf
# 添加以下两行内容:
blacklist nouveau
options nouveau modeset=0
# 禁用Nouveau
sudo dracut --force
# 重启vm
sudo reboot
# 检查是否已经成功禁用
lsmod | grep nouveau
```

## 自定义驱动镜像

先在本地创建 `nvidia-driver` 文件：

<details>
<summary>点击查看完整的 nvidia-driver 文件内容</summary>

```shell 
#! /bin/bash -x
# Copyright (c) 2018-2020, NVIDIA CORPORATION. All rights reserved.

set -eu

RUN_DIR=/run/nvidia
PID_FILE=${RUN_DIR}/${0##*/}.pid
DRIVER_VERSION=${DRIVER_VERSION:?"Missing DRIVER_VERSION env"}
KERNEL_UPDATE_HOOK=/run/kernel/postinst.d/update-nvidia-driver
NUM_VGPU_DEVICES=0
NVIDIA_MODULE_PARAMS=()
NVIDIA_UVM_MODULE_PARAMS=()
NVIDIA_MODESET_MODULE_PARAMS=()
NVIDIA_PEERMEM_MODULE_PARAMS=()
TARGETARCH=${TARGETARCH:?"Missing TARGETARCH env"}
USE_HOST_MOFED="${USE_HOST_MOFED:-false}"
DNF_RELEASEVER=${DNF_RELEASEVER:-""}
RHEL_VERSION=${RHEL_VERSION:-""}
RHEL_MAJOR_VERSION=9

OPEN_KERNEL_MODULES_ENABLED=${OPEN_KERNEL_MODULES_ENABLED:-false}
[[ "${OPEN_KERNEL_MODULES_ENABLED}" == "true" ]] && KERNEL_TYPE=kernel-open || KERNEL_TYPE=kernel

DRIVER_ARCH=${TARGETARCH/amd64/x86_64} && DRIVER_ARCH=${DRIVER_ARCH/arm64/aarch64}
echo "DRIVER_ARCH is $DRIVER_ARCH"

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
source $SCRIPT_DIR/common.sh

_update_package_cache() {
    if [ "${PACKAGE_TAG:-}" != "builtin" ]; then
        echo "Updating the package cache..."
        if ! yum -q makecache; then
            echo "FATAL: failed to reach RHEL package repositories. "\
                 "Ensure that the cluster can access the proper networks."
            exit 1
        fi
    fi
}

_cleanup_package_cache() {
    if [ "${PACKAGE_TAG:-}" != "builtin" ]; then
        echo "Cleaning up the package cache..."
        rm -rf /var/cache/yum/*
    fi
}

_get_rhel_version_from_kernel() {
    local rhel_version_underscore rhel_version_arr
    rhel_version_underscore=$(echo "${KERNEL_VERSION}" | sed 's/.*el\([0-9]\+_[0-9]\+\).*/\1/g')
    # For e.g. :- from the kernel version 4.18.0-513.9.1.el8_9, we expect to extract the string "8_9"
    if [[ ! ${rhel_version_underscore} =~ ^[0-9]+_[0-9]+$ ]]; then
        echo "Unable to resolve RHEL version from kernel version" >&2
        return 1
    fi
    IFS='_' read -r -a rhel_version_arr <<< "$rhel_version_underscore"
    if [[ ${#rhel_version_arr[@]} -ne 2 ]]; then
        echo "Unable to resolve RHEL version from kernel version" >&2
        return 1
    fi
    RHEL_VERSION="${rhel_version_arr[0]}.${rhel_version_arr[1]}"
    echo "RHEL VERSION successfully resolved from kernel: ${RHEL_VERSION}"
    return 0
}

_resolve_rhel_version() {
    _get_rhel_version_from_kernel || RHEL_VERSION="${RHEL_MAJOR_VERSION}"
    # set dnf release version as rhel version by default
    if [[ -z "${DNF_RELEASEVER}" ]]; then
        DNF_RELEASEVER="${RHEL_VERSION}"
    fi
    return 0
}

# Resolve the kernel version to the form major.minor.patch-revision.
_resolve_kernel_version() {
    echo "Resolving Linux kernel version..."
    local version=$(yum -q list available --showduplicates kernel-headers |
      awk -v arch=$(uname -m) 'NR>1 {print $2"."arch}' | tac | grep -E -m1 "^${KERNEL_VERSION/latest/.*}")

    if [ -z "${version}" ]; then
        echo "Could not resolve Linux kernel version" >&2
        return 1
    fi
    KERNEL_VERSION="${version}"
    echo "Proceeding with Linux kernel version ${KERNEL_VERSION}"
    return 0
}

# Install the kernel modules header/builtin/order files and generate the kernel version string.
_install_prerequisites() (
    local tmp_dir=$(mktemp -d)

    trap "rm -rf ${tmp_dir}" EXIT
    cd ${tmp_dir}

    echo "Installing elfutils..."
    if ! dnf install -q -y elfutils-libelf.$DRIVER_ARCH; then
        echo "FATAL: failed to install elfutils packages. RHEL entitlement may be improperly deployed."
        exit 1
    fi
    if ! dnf install -q -y elfutils-libelf-devel.$DRIVER_ARCH; then
        echo "FATAL: failed to install elfutils packages. RHEL entitlement may be improperly deployed."
        exit 1
    fi    

    rm -rf /lib/modules/${KERNEL_VERSION}
    mkdir -p /lib/modules/${KERNEL_VERSION}/proc

    echo "Enabling RHOCP and EUS RPM repos..."
    if [ -n "${OPENSHIFT_VERSION:-}" ]; then
        dnf config-manager --set-enabled rhocp-${OPENSHIFT_VERSION}-for-rhel-9-$DRIVER_ARCH-rpms || true
        if ! dnf makecache --releasever=${DNF_RELEASEVER}; then
            dnf config-manager --set-disabled rhocp-${OPENSHIFT_VERSION}-for-rhel-9-$DRIVER_ARCH-rpms || true
        fi
    fi

    dnf config-manager --set-enabled rhel-9-for-$DRIVER_ARCH-baseos-eus-rpms  || true
    if ! dnf makecache --releasever=${DNF_RELEASEVER}; then
            dnf config-manager --set-disabled rhel-9-for-$DRIVER_ARCH-baseos-eus-rpms || true
    fi

    # try with EUS disabled, if it does not work, then try just major version
    if ! dnf makecache --releasever=${DNF_RELEASEVER}; then
      # If pointing to DNF_RELEASEVER does not work, we point to the RHEL_MAJOR_VERSION as a last resort
      if ! dnf makecache --releasever=${RHEL_MAJOR_VERSION}; then
        echo "FATAL: failed to update the dnf metadata cache after multiple attempts with releasevers ${DNF_RELEASEVER}, ${RHEL_MAJOR_VERSION}"
        exit 1
      else
        DNF_RELEASEVER=${RHEL_MAJOR_VERSION}
      fi
    fi

    echo "Installing Linux kernel headers..."
    dnf -q -y --releasever=${DNF_RELEASEVER} install kernel-headers-${KERNEL_VERSION} kernel-devel-${KERNEL_VERSION} --allowerasing > /dev/null
    ln -s /usr/src/kernels/${KERNEL_VERSION} /lib/modules/${KERNEL_VERSION}/build

    echo "Installing Linux kernel module files..."
    dnf -q -y --releasever=${DNF_RELEASEVER} install kernel-core-${KERNEL_VERSION} > /dev/null

    # Prevent depmod from giving a WARNING about missing files
    touch /lib/modules/${KERNEL_VERSION}/modules.order
    touch /lib/modules/${KERNEL_VERSION}/modules.builtin

    depmod ${KERNEL_VERSION}

    echo "Generating Linux kernel version string..."
    if [ "$TARGETARCH" = "arm64" ]; then
        gunzip -c /lib/modules/${KERNEL_VERSION}/vmlinuz | strings | grep -E '^Linux version' | sed 's/^\(.*\)\s\+(.*)$/\1/' > version
    else
        extract-vmlinux /lib/modules/${KERNEL_VERSION}/vmlinuz | strings | grep -E '^Linux version' | sed 's/^\(.*\)\s\+(.*)$/\1/' > version
    fi
    if [ -z "$(<version)" ]; then
        echo "Could not locate Linux kernel version string" >&2
        return 1
    fi
    mv version /lib/modules/${KERNEL_VERSION}/proc

    # Parse gcc version
    # gcc_version is expected to match x.y.z
    # current_gcc is expected to match 'gcc-x.y.z-rel.el8.x86_64
    local gcc_version=$(cat /lib/modules/${KERNEL_VERSION}/proc/version | grep -Eo "gcc \(GCC\) ([0-9\.]+)" | grep -Eo "([0-9\.]+)")
    local current_gcc=$(rpm -qa gcc)
    echo "kernel requires gcc version: 'gcc-${gcc_version}', current gcc version is '${current_gcc}'"

    if ! [[ "${current_gcc}" =~ "gcc-${gcc_version}"-.* ]]; then
        dnf install -q -y --releasever=${DNF_RELEASEVER} "gcc-${gcc_version}"
    fi
)

# Cleanup the prerequisites installed above.
_remove_prerequisites() {
    true
    if [ "${PACKAGE_TAG:-}" != "builtin" ]; then
        dnf -q -y remove kernel-headers-${KERNEL_VERSION} kernel-devel-${KERNEL_VERSION} > /dev/null
        # TODO remove module files not matching an existing driver package.
    fi
}

# Check if the kernel version requires a new precompiled driver packages.
_kernel_requires_package() {
    local proc_mount_arg=""

    echo "Checking NVIDIA driver packages..."

    [[ ! -d /usr/src/nvidia-${DRIVER_VERSION}/${KERNEL_TYPE} ]] && return 0
    cd /usr/src/nvidia-${DRIVER_VERSION}/${KERNEL_TYPE}

    proc_mount_arg="--proc-mount-point /lib/modules/${KERNEL_VERSION}/proc"
    for pkg_name in $(ls -d -1 precompiled/** 2> /dev/null); do
        is_match=$(../mkprecompiled --match ${pkg_name} ${proc_mount_arg})
        if [ "${is_match}" == "kernel interface matches." ]; then
            echo "Found NVIDIA driver package ${pkg_name##*/}"
            return 1
        fi
    done
    return 0
}

# Compile the kernel modules, optionally sign them, and generate a precompiled package for use by the nvidia-installer.
_create_driver_package() (
    local pkg_name="nvidia-modules-${KERNEL_VERSION%%-*}${PACKAGE_TAG:+-${PACKAGE_TAG}}"
    local nvidia_sign_args=""
    local nvidia_modeset_sign_args=""
    local nvidia_uvm_sign_args=""

    trap "make -s -j ${MAX_THREADS} SYSSRC=/lib/modules/${KERNEL_VERSION}/build clean > /dev/null" EXIT

    echo "Compiling NVIDIA driver kernel modules..."
    cd /usr/src/nvidia-${DRIVER_VERSION}/${KERNEL_TYPE}

    if _gpu_direct_rdma_enabled; then
        ln -s /run/mellanox/drivers/usr/src/ofa_kernel /usr/src/
        # if arch directory exists(MOFED >=5.5) then create a symlink as expected by GPU driver installer
        # This is required as currently GPU driver installer doesn't expect headers in x86_64 folder, but only in either default or kernel-version folder.
        # ls -ltr /usr/src/ofa_kernel/
        # lrwxrwxrwx 1 root root   36 Dec  8 20:10 default -> /etc/alternatives/ofa_kernel_headers
        # drwxr-xr-x 4 root root 4096 Dec  8 20:14 x86_64
        # lrwxrwxrwx 1 root root   44 Dec  9 19:05 5.4.0-90-generic -> /usr/src/ofa_kernel/x86_64/5.4.0-90-generic/
        if [[ -d "/run/mellanox/drivers/usr/src/ofa_kernel/$(uname -m)/$(uname -r)" ]]; then
            if [[ ! -e "/usr/src/ofa_kernel/$(uname -r)" ]]; then
                ln -s "/run/mellanox/drivers/usr/src/ofa_kernel/$(uname -m)/$(uname -r)" /usr/src/ofa_kernel/
            fi
        fi
    fi

    make -s -j ${MAX_THREADS} SYSSRC=/lib/modules/${KERNEL_VERSION}/build nv-linux.o nv-modeset-linux.o > /dev/null

    echo "Relinking NVIDIA driver kernel modules..."
    rm -f nvidia.ko nvidia-modeset.ko
    ld -d -r -o nvidia.ko ./nv-linux.o ./nvidia/nv-kernel.o_binary
    ld -d -r -o nvidia-modeset.ko ./nv-modeset-linux.o ./nvidia-modeset/nv-modeset-kernel.o_binary

    if [ -n "${PRIVATE_KEY}" ]; then
        echo "Signing NVIDIA driver kernel modules..."
        donkey get ${PRIVATE_KEY} sh -c "PATH=${PATH}:/usr/src/linux-headers-${KERNEL_VERSION}/scripts && \
          sign-file sha512 \$DONKEY_FILE pubkey.x509 nvidia.ko nvidia.ko.sign &&                          \
          sign-file sha512 \$DONKEY_FILE pubkey.x509 nvidia-modeset.ko nvidia-modeset.ko.sign &&          \
          sign-file sha512 \$DONKEY_FILE pubkey.x509 nvidia-uvm.ko"
        nvidia_sign_args="--linked-module nvidia.ko --signed-module nvidia.ko.sign"
        nvidia_modeset_sign_args="--linked-module nvidia-modeset.ko --signed-module nvidia-modeset.ko.sign"
        nvidia_uvm_sign_args="--signed"
    fi

    echo "Building NVIDIA driver package ${pkg_name}..."
    ../mkprecompiled --pack ${pkg_name} --description ${KERNEL_VERSION}                              \
                                        --proc-mount-point /lib/modules/${KERNEL_VERSION}/proc       \
                                        --driver-version ${DRIVER_VERSION}                           \
                                        --kernel-interface nv-linux.o                                \
                                        --linked-module-name nvidia.ko                               \
                                        --core-object-name nvidia/nv-kernel.o_binary                 \
                                        ${nvidia_sign_args}                                          \
                                        --target-directory .                                         \
                                        --kernel-interface nv-modeset-linux.o                        \
                                        --linked-module-name nvidia-modeset.ko                       \
                                        --core-object-name nvidia-modeset/nv-modeset-kernel.o_binary \
                                        ${nvidia_modeset_sign_args}                                  \
                                        --target-directory .                                         \
                                        --kernel-module nvidia-uvm.ko                                \
                                        ${nvidia_uvm_sign_args}                                      \
                                        --target-directory .
    mkdir -p precompiled
    mv ${pkg_name} precompiled
)

_assert_nvswitch_system() {
    [ -d /proc/driver/nvidia-nvswitch ] || return 1
    entries=$(ls -1 /proc/driver/nvidia-nvswitch/devices/*)
    if [ -z "${entries}" ]; then
        return 1
    fi
    return 0
}

# For each kernel module configuration file mounted into the container,
# parse the file contents and extract the custom module parameters that
# are to be passed as input to 'modprobe'.
#
# Assumptions:
# - Configuration files are named <module-name>.conf (i.e. nvidia.conf, nvidia-uvm.conf).
# - Configuration files are mounted inside the container at /drivers.
# - Each line in the file contains at least one parameter, where parameters on the same line
#   are space delimited. It is up to the user to properly format the file to ensure
#   the correct set of parameters are passed to 'modprobe'.
_get_module_params() {
    local base_path="/drivers"
    # nvidia
    if [ -f "${base_path}/nvidia.conf" ]; then
       while IFS="" read -r param || [ -n "$param" ]; do
           NVIDIA_MODULE_PARAMS+=("$param")
       done <"${base_path}/nvidia.conf"
       echo "Module parameters provided for nvidia: ${NVIDIA_MODULE_PARAMS[@]}"
    fi
    # nvidia-uvm
    if [ -f "${base_path}/nvidia-uvm.conf" ]; then
       while IFS="" read -r param || [ -n "$param" ]; do
           NVIDIA_UVM_MODULE_PARAMS+=("$param")
       done <"${base_path}/nvidia-uvm.conf"
       echo "Module parameters provided for nvidia-uvm: ${NVIDIA_UVM_MODULE_PARAMS[@]}"
    fi
    # nvidia-modeset
    if [ -f "${base_path}/nvidia-modeset.conf" ]; then
       while IFS="" read -r param || [ -n "$param" ]; do
           NVIDIA_MODESET_MODULE_PARAMS+=("$param")
       done <"${base_path}/nvidia-modeset.conf"
       echo "Module parameters provided for nvidia-modeset: ${NVIDIA_MODESET_MODULE_PARAMS[@]}"
    fi
    # nvidia-peermem
    if [ -f "${base_path}/nvidia-peermem.conf" ]; then
       while IFS="" read -r param || [ -n "$param" ]; do
           NVIDIA_PEERMEM_MODULE_PARAMS+=("$param")
       done <"${base_path}/nvidia-peermem.conf"
       echo "Module parameters provided for nvidia-peermem: ${NVIDIA_PEERMEM_MODULE_PARAMS[@]}"
    fi
}

# Load the kernel modules and start persistenced.
_load_driver() {
    echo "Parsing kernel module parameters..."
    _get_module_params

    local nv_fw_search_path="$RUN_DIR/driver/lib/firmware"
    local set_fw_path="true"
    local fw_path_config_file="/sys/module/firmware_class/parameters/path"
    for param in "${NVIDIA_MODULE_PARAMS[@]}"; do
        if [[ "$param" == "NVreg_EnableGpuFirmware=0" ]]; then
          set_fw_path="false"
        fi
    done

    if [[ "$set_fw_path" == "true" ]]; then
        echo "Configuring the following firmware search path in '$fw_path_config_file': $nv_fw_search_path"
        if [[ ! -z $(grep '[^[:space:]]' $fw_path_config_file) ]]; then
            echo "WARNING: A search path is already configured in $fw_path_config_file"
            echo "         Retaining the current configuration"
        else
            echo -n "$nv_fw_search_path" > $fw_path_config_file || echo "WARNING: Failed to configure the firmware search path"
        fi
    fi

    echo "Loading ipmi and i2c_core kernel modules..."
    modprobe -a i2c_core ipmi_msghandler ipmi_devintf

    echo "Loading NVIDIA driver kernel modules..."
    set -o xtrace +o nounset
    modprobe nvidia "${NVIDIA_MODULE_PARAMS[@]}"
    modprobe nvidia-uvm "${NVIDIA_UVM_MODULE_PARAMS[@]}"
    modprobe nvidia-modeset "${NVIDIA_MODESET_MODULE_PARAMS[@]}"
    set +o xtrace -o nounset

    if _gpu_direct_rdma_enabled; then
        echo "Loading NVIDIA Peer Memory kernel module..."
        set -o xtrace +o nounset
        modprobe -a nvidia-peermem "${NVIDIA_PEERMEM_MODULE_PARAMS[@]}"
        set +o xtrace -o nounset
    fi

    echo "Starting NVIDIA persistence daemon..."
    nvidia-persistenced --persistence-mode

    if [ "${DRIVER_TYPE}" = "vgpu" ]; then
        echo "Copying gridd.conf..."
        cp /drivers/gridd.conf /etc/nvidia/gridd.conf
        if [ "${VGPU_LICENSE_SERVER_TYPE}" = "NLS" ]; then
            echo "Copying ClientConfigToken..."
            mkdir -p  /etc/nvidia/ClientConfigToken/
            cp /drivers/ClientConfigToken/* /etc/nvidia/ClientConfigToken/
        fi

        echo "Starting nvidia-gridd.."
        LD_LIBRARY_PATH=/usr/lib64/nvidia/gridd nvidia-gridd

        # Start virtual topology daemon
        _start_vgpu_topology_daemon
    fi

    if _assert_nvswitch_system; then
        echo "Starting NVIDIA fabric manager daemon..."
        nv-fabricmanager -c /usr/share/nvidia/nvswitch/fabricmanager.cfg
    fi
}

# Stop persistenced and unload the kernel modules if they are currently loaded.
_unload_driver() {
    local rmmod_args=()
    local nvidia_deps=0
    local nvidia_refs=0
    local nvidia_uvm_refs=0
    local nvidia_modeset_refs=0
    local nvidia_peermem_refs=0

    echo "Stopping NVIDIA persistence daemon..."
    if [ -f /var/run/nvidia-persistenced/nvidia-persistenced.pid ]; then
        local pid=$(< /var/run/nvidia-persistenced/nvidia-persistenced.pid)

        kill -SIGTERM "${pid}"
        for i in $(seq 1 50); do
            kill -0 "${pid}" 2> /dev/null || break
            sleep 0.1
        done
        if [ $i -eq 50 ]; then
            echo "Could not stop NVIDIA persistence daemon" >&2
            return 1
        fi
    fi

    if [ -f /var/run/nvidia-gridd/nvidia-gridd.pid ]; then
        echo "Stopping NVIDIA grid daemon..."
        local pid=$(< /var/run/nvidia-gridd/nvidia-gridd.pid)

        kill -SIGTERM "${pid}"
        for i in $(seq 1 10); do
            kill -0 "${pid}" 2> /dev/null || break
            sleep 0.1
        done
        if [ $i -eq 10 ]; then
            echo "Could not stop NVIDIA Grid daemon" >&2
            return 1
        fi
    fi

    if [ -f /var/run/nvidia-fabricmanager/nv-fabricmanager.pid ]; then
        echo "Stopping NVIDIA fabric manager daemon..."
        local pid=$(< /var/run/nvidia-fabricmanager/nv-fabricmanager.pid)

        kill -SIGTERM "${pid}"
        for i in $(seq 1 50); do
            kill -0 "${pid}" 2> /dev/null || break
            sleep 0.1
        done
        if [ $i -eq 50 ]; then
            echo "Could not stop NVIDIA fabric manager daemon" >&2
            return 1
        fi
    fi

    echo "Unloading NVIDIA driver kernel modules..."
    if [ -f /sys/module/nvidia_modeset/refcnt ]; then
        nvidia_modeset_refs=$(< /sys/module/nvidia_modeset/refcnt)
        rmmod_args+=("nvidia-modeset")
        ((++nvidia_deps))
    fi
    if [ -f /sys/module/nvidia_uvm/refcnt ]; then
        nvidia_uvm_refs=$(< /sys/module/nvidia_uvm/refcnt)
        rmmod_args+=("nvidia-uvm")
        ((++nvidia_deps))
    fi
    if [ -f /sys/module/nvidia/refcnt ]; then
        nvidia_refs=$(< /sys/module/nvidia/refcnt)
        rmmod_args+=("nvidia")
    fi
    if [ -f /sys/module/nvidia_peermem/refcnt ]; then
        nvidia_peermem_refs=$(< /sys/module/nvidia_peermem/refcnt)
        rmmod_args+=("nvidia-peermem")
        ((++nvidia_deps))
    fi
    if [ ${nvidia_refs} -gt ${nvidia_deps} ] || [ ${nvidia_uvm_refs} -gt 0 ] || [ ${nvidia_modeset_refs} -gt 0 ] || [ ${nvidia_peermem_refs} -gt 0 ]; then
        echo "Could not unload NVIDIA driver kernel modules, driver is in use" >&2
        return 1
    fi

    if [ ${#rmmod_args[@]} -gt 0 ]; then
        rmmod ${rmmod_args[@]}
    fi
    return 0
}

# Link and install the kernel modules from a precompiled package using the nvidia-installer.
_install_driver() {
    local install_args=()

    echo "Installing NVIDIA driver kernel modules..."
    cd /usr/src/nvidia-${DRIVER_VERSION}
    rm -rf /lib/modules/${KERNEL_VERSION}/video

    if [ "${ACCEPT_LICENSE}" = "yes" ]; then
        install_args+=("--accept-license")
    fi
    IGNORE_CC_MISMATCH=1 nvidia-installer --kernel-module-only --no-drm --ui=none --no-nouveau-check -m=${KERNEL_TYPE} ${install_args[@]+"${install_args[@]}"}
    # May need to add no-cc-check for Rhel, otherwise it complains about cc missing in path
    # /proc/version and lib/modules/KERNEL_VERSION/proc are different, by default installer looks at /proc/ so, added the proc-mount-point
    # TODO: remove the -a flag. its not needed. in the new driver version, license-acceptance is implicit
    #nvidia-installer --kernel-module-only --no-drm --ui=none --no-nouveau-check --no-cc-version-check --proc-mount-point /lib/modules/${KERNEL_VERSION}/proc ${install_args[@]+"${install_args[@]}"}
}

# Mount the driver rootfs into the run directory with the exception of sysfs.
_mount_rootfs() {
    echo "Mounting NVIDIA driver rootfs..."
    mount --make-runbindable /sys
    mount --make-private /sys
    mkdir -p ${RUN_DIR}/driver
    mount --rbind / ${RUN_DIR}/driver

    echo "Check SELinux status"
    if [ -e /sys/fs/selinux ]; then
        echo "SELinux is enabled"
        echo "Change device files security context for selinux compatibility"
        chcon -R -t container_file_t ${RUN_DIR}/driver/dev
    else
        echo "SELinux is disabled, skipping..."
    fi
}

# Unmount the driver rootfs from the run directory.
_unmount_rootfs() {
    echo "Unmounting NVIDIA driver rootfs..."
    if findmnt -r -o TARGET | grep "${RUN_DIR}/driver" > /dev/null; then
        umount -l -R ${RUN_DIR}/driver
    fi
}

# Write a kernel postinst.d script to automatically precompile packages on kernel update (similar to DKMS).
_write_kernel_update_hook() {
    if [ ! -d ${KERNEL_UPDATE_HOOK%/*} ]; then
        return
    fi

    echo "Writing kernel update hook..."
    cat > ${KERNEL_UPDATE_HOOK} <<'EOF'
#!/bin/bash

set -eu
trap 'echo "ERROR: Failed to update the NVIDIA driver" >&2; exit 0' ERR

NVIDIA_DRIVER_PID=$(< /run/nvidia/nvidia-driver.pid)

export "$(grep -z DRIVER_VERSION /proc/${NVIDIA_DRIVER_PID}/environ)"
nsenter -t "${NVIDIA_DRIVER_PID}" -m -- nvidia-driver update --kernel "$1"
EOF
    chmod +x ${KERNEL_UPDATE_HOOK}
}

_shutdown() {
    if _unload_driver; then
        _unmount_rootfs
        rm -f ${PID_FILE} ${KERNEL_UPDATE_HOOK}
        return 0
    fi
    return 1
}

_find_vgpu_driver_version() {
    local count=""
    local version=""
    local drivers_path="/drivers"

    if [ "${DISABLE_VGPU_VERSION_CHECK}" = "true" ]; then
        echo "vgpu version compatibility check is disabled"
        return 0
    fi
    # check if vgpu devices are present
    count=$(vgpu-util count)
    if [ $? -ne 0 ]; then
         echo "cannot find vgpu devices on host, pleae check /var/log/vgpu-util.log for more details..."
         return 0
    fi
    NUM_VGPU_DEVICES=$(echo "$count" | awk -F= '{print $2}')
    if [ $NUM_VGPU_DEVICES -eq 0 ]; then
        # no vgpu devices found, treat as passthrough
        return 0
    fi
    echo "found $NUM_VGPU_DEVICES vgpu devices on host"

    # find compatible guest driver using driver catalog
    if [ -d "/mnt/shared-nvidia-driver-toolkit/drivers" ]; then
        drivers_path="/mnt/shared-nvidia-driver-toolkit/drivers"
    fi
    version=$(vgpu-util match -i "${drivers_path}" -c "${drivers_path}/vgpuDriverCatalog.yaml")
    if [ $? -ne 0 ]; then
        echo "cannot find match for compatible vgpu driver from available list, please check /var/log/vgpu-util.log for more details..."
        return 1
    fi
    DRIVER_VERSION=$(echo "$version" | awk -F= '{print $2}')
    echo "vgpu driver version selected: ${DRIVER_VERSION}"
    return 0
}

_start_vgpu_topology_daemon() {
    type nvidia-topologyd > /dev/null 2>&1 || return 0
    echo "Starting nvidia-topologyd.."
    nvidia-topologyd
}

_prepare() {
    if [ "${DRIVER_TYPE}" = "vgpu" ]; then
        _find_vgpu_driver_version || exit 1
    fi

    # Install the userspace components and copy the kernel module sources.
    sh NVIDIA-Linux-$DRIVER_ARCH-$DRIVER_VERSION.run -x && \
        cd NVIDIA-Linux-$DRIVER_ARCH-$DRIVER_VERSION && \
        sh /tmp/install.sh nvinstall && \
        mkdir -p /usr/src/nvidia-$DRIVER_VERSION && \
        mv LICENSE mkprecompiled ${KERNEL_TYPE} /usr/src/nvidia-$DRIVER_VERSION && \
        sed '9,${/^\(kernel\|LICENSE\)/!d}' .manifest > /usr/src/nvidia-$DRIVER_VERSION/.manifest

    echo -e "\n========== NVIDIA Software Installer ==========\n"
    echo -e "Starting installation of NVIDIA driver version ${DRIVER_VERSION} for Linux kernel version ${KERNEL_VERSION}\n"
}

_prepare_exclusive() {
    _prepare

    exec 3> ${PID_FILE}
    if ! flock -n 3; then
        echo "An instance of the NVIDIA driver is already running, aborting"
        exit 1
    fi
    echo $$ >&3

    trap "echo 'Caught signal'; exit 1" HUP INT QUIT PIPE TERM
    trap "_shutdown" EXIT

    _unload_driver || exit 1
    _unmount_rootfs
}

_build() {
    # Install dependencies
    if _kernel_requires_package; then
        _update_package_cache
        _install_prerequisites
        _create_driver_package
        #_remove_prerequisites
        _cleanup_package_cache
    fi

    # Build the driver
    _install_driver
}

_load() {
    _load_driver
    _mount_rootfs
    _write_kernel_update_hook

    echo "Done, now waiting for signal"
    sleep infinity &
    trap "echo 'Caught signal'; _shutdown && { kill $!; exit 0; }" HUP INT QUIT PIPE TERM
    trap - EXIT
    while true; do wait $! || continue; done
    exit 0
}

init() {
    _prepare_exclusive

    _build

    _load
}

build() {
    _prepare

    _build
}

load() {
    _prepare_exclusive

    _load
}

update() {
    exec 3>&2
    if exec 2> /dev/null 4< ${PID_FILE}; then
        if ! flock -n 4 && read pid <&4 && kill -0 "${pid}"; then
            exec > >(tee -a "/proc/${pid}/fd/1")
            exec 2> >(tee -a "/proc/${pid}/fd/2" >&3)
        else
            exec 2>&3
        fi
        exec 4>&-
    fi
    exec 3>&-

    # vgpu driver version is chosen dynamically during runtime, so pre-compile modules for
    # only non-vgpu driver types
    if [ "${DRIVER_TYPE}" != "vgpu" ]; then
        # Install the userspace components and copy the kernel module sources.
        if [ ! -e /usr/src/nvidia-${DRIVER_VERSION}/mkprecompiled ]; then
            sh NVIDIA-Linux-$DRIVER_ARCH-$DRIVER_VERSION.run -x && \
                cd NVIDIA-Linux-$DRIVER_ARCH-$DRIVER_VERSION && \
                sh /tmp/install.sh nvinstall && \
                mkdir -p /usr/src/nvidia-$DRIVER_VERSION && \
                mv LICENSE mkprecompiled ${KERNEL_TYPE} /usr/src/nvidia-$DRIVER_VERSION && \
                sed '9,${/^\(kernel\|LICENSE\)/!d}' .manifest > /usr/src/nvidia-$DRIVER_VERSION/.manifest
        fi
    fi

    echo -e "\n========== NVIDIA Software Updater ==========\n"
    echo -e "Starting update of NVIDIA driver version ${DRIVER_VERSION} for Linux kernel version ${KERNEL_VERSION}\n"

    trap "echo 'Caught signal'; exit 1" HUP INT QUIT PIPE TERM

    _update_package_cache
    _resolve_kernel_version || exit 1
    _install_prerequisites
    if _kernel_requires_package; then
        _create_driver_package
    fi
    _remove_prerequisites
    _cleanup_package_cache

    echo "Done"
    exit 0
}

# Wait for MOFED drivers to be loaded and load nvidia-peermem whenever it gets unloaded during MOFED driver updates
reload_nvidia_peermem() {
    if [ "$USE_HOST_MOFED" = "true" ]; then
        until  lsmod | grep mlx5_core > /dev/null 2>&1 && [ -f /run/nvidia/validations/.driver-ctr-ready ];
        do
            echo "waiting for mellanox ofed and nvidia drivers to be installed"
            sleep 10
        done
    else
        # use driver readiness flag created by MOFED container
        until  [ -f /run/mellanox/drivers/.driver-ready ] && [ -f /run/nvidia/validations/.driver-ctr-ready ];
        do
            echo "waiting for mellanox ofed and nvidia drivers to be installed"
            sleep 10
        done
    fi
    # get any parameters provided for nvidia-peermem
    _get_module_params && set +o nounset
    if chroot /run/nvidia/driver modprobe nvidia-peermem "${NVIDIA_PEERMEM_MODULE_PARAMS[@]}"; then
        if [ -f /sys/module/nvidia_peermem/refcnt ]; then
            echo "successfully loaded nvidia-peermem module, now waiting for signal"
            sleep inf
            trap "echo 'Caught signal'; exit 1" HUP INT QUIT PIPE TERM
        fi
    fi
    echo "failed to load nvidia-peermem module"
    exit 1
}

# probe by gpu-operator for liveness/startup checks for nvidia-peermem module to be loaded when MOFED drivers are ready
probe_nvidia_peermem() {
    if lsmod | grep mlx5_core > /dev/null 2>&1; then
        if [ ! -f /sys/module/nvidia_peermem/refcnt ]; then
            echo "nvidia-peermem module is not loaded"
            return 1
        fi
    else
        echo "MOFED drivers are not ready, skipping probe to avoid container restarts..."
    fi
    return 0
}

usage() {
    cat >&2 <<EOF
Usage: $0 COMMAND [ARG...]

Commands:
  init   [-a | --accept-license] [-m | --max-threads MAX_THREADS]
  build  [-a | --accept-license] [-m | --max-threads MAX_THREADS]
  load
  update [-k | --kernel VERSION] [-s | --sign KEYID] [-t | --tag TAG] [-m | --max-threads MAX_THREADS]
EOF
    exit 1
}

if [ $# -eq 0 ]; then
    usage
fi
command=$1; shift
case "${command}" in
    init) options=$(getopt -l accept-license,max-threads: -o am: -- "$@") ;;
    build) options=$(getopt -l accept-license,tag:,max-threads: -o a:t:m: -- "$@") ;;
    load) options="" ;;
    update) options=$(getopt -l kernel:,sign:,tag:,max-threads: -o k:s:t:m: -- "$@") ;;
    reload_nvidia_peermem) options="" ;;
    probe_nvidia_peermem) options="" ;;
    *) usage ;;
esac
if [ $? -ne 0 ]; then
    usage
fi
eval set -- "${options}"

ACCEPT_LICENSE=""
MAX_THREADS=""
KERNEL_VERSION=$(uname -r)
PRIVATE_KEY=""
PACKAGE_TAG=""

for opt in ${options}; do
    case "$opt" in
    -a | --accept-license) ACCEPT_LICENSE="yes"; shift 1 ;;
    -k | --kernel) KERNEL_VERSION=$2; shift 2 ;;
    -m | --max-threads) MAX_THREADS=$2; shift 2 ;;
    -s | --sign) PRIVATE_KEY=$2; shift 2 ;;
    -t | --tag) PACKAGE_TAG=$2; shift 2 ;;
    --) shift; break ;;
    esac
done
if [ $# -ne 0 ]; then
    usage
fi

_resolve_rhel_version || exit 1

$command
```

</details>

使用官方的镜像来二次构建自定义镜像，如下是一个 `Dockerfile` 文件的内容：

```dockerfile
FROM nvcr.io/nvidia/driver:535.183.06-rhel9.2
COPY nvidia-driver /usr/local/bin
RUN chmod +x /usr/local/bin/nvidia-driver
CMD ["/bin/bash", "-c"]
```

构建命令并推送到火种集群：

```bash
docker build -t {火种registry}/nvcr.m.daocloud.io/nvidia/driver:535.183.06-01-rhel9.2 -f Dockerfile .
docker push {火种registry}/nvcr.m.daocloud.io/nvidia/driver:535.183.06-01-rhel9.2
```

## 安装驱动

1. 安装 gpu-operator addon
2. 设置 `driver.version=535.183.06-01`
