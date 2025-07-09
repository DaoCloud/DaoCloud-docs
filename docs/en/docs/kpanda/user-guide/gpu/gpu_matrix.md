---
hide:
  - toc
---

# GPU Support Matrix

This page describes the GPU and OS compatibility matrix for DCE 5.0.

## NVIDIA GPU

| GPU Vendor & Type | Supported GPU Models | Compatible OS (Online) | Recommended Kernel | Recommended OS & Kernel | Installation Guide |
| ------ | -------- | -------- | ------- | ------- | ------- |
| NVIDIA GPU (Full Card / vGPU) | NVIDIA Fermi (2.1) Architecture | CentOS 7 | Kernel 3.10.0-123 to 3.10.0-1160 (refer to OS-specific kernel version recommendations) | OS: CentOS 7.9; Kernel: 3.10.0-1160 | [Offline GPU Operator Installation](./nvidia/install_nvidia_driver_of_operator.md) |
| | NVIDIA GeForce 400 Series | CentOS 8 | Kernel 4.18.0-80 to 4.18.0-348 | | |
| | NVIDIA Quadro 4000 Series | Ubuntu 20.04 | Kernel 5.4 | | |
| | NVIDIA Tesla 20 Series | Ubuntu 22.04 | Kernel 5.19 | | |
| | NVIDIA Ampere Architecture (A100; A800; H100) | RHEL 7 | Kernel 3.10.0-123 to 3.10.0-1160 | | |
| | | RHEL 8 | Kernel 4.18.0-80 to 4.18.0-348 | | |
| NVIDIA MIG | NVIDIA Ampere Architecture (A100, A800, H100) | CentOS 7 | Kernel 3.10.0-123 to 3.10.0-1160 | OS: CentOS 7.9; Kernel: 3.10.0-1160 | [Offline GPU Operator Installation](./nvidia/mig/create_mig.md) |
| | | CentOS 8 | Kernel 4.18.0-80 to 4.18.0-348 | | |
| | | Ubuntu 20.04 | Kernel 5.4 | | |
| | | Ubuntu 22.04 | Kernel 5.19 | | |
| | | RHEL 7 | Kernel 3.10.0-123 to 3.10.0-1160 | | |
| | | RHEL 8 | Kernel 4.18.0-80 to 4.18.0-348 | | |

## Ascend NPU

| Vendor & Type | Supported NPU Models | Compatible OS (Online) | Recommended Kernel | Recommended OS & Kernel | Installation Guide |
| ----- | ----- | --------- | ------- | ------ | ------------- |
| Ascend 310 | Ascend 310 | Ubuntu 20.04 | See kernel version requirements | OS: CentOS 7.9; Kernel: 3.10.0-1160 | Coming soon (docs for 300 and 310P drivers) |
| | Ascend 310P | CentOS 7.6 | | | |
| | | CentOS 8.2 | | | |
| | | Kylin V10 SP1 OS | | | |
| | | Kylin V10 SP2 OS | | | |
| | | Kylin V10 SP3 OS | | | |
| | | openEuler OS | | | |
| Ascend 910 | Ascend 910B | Ubuntu 20.04 | See kernel version requirements | OS: CentOS 7.9; Kernel: 3.10.0-1160 | [910 Driver Documentation](./ascend/ascend_driver_install.md#npu_1) |
| | | CentOS 7.6 | | | |
| | | CentOS 8.2 | | | |
| | | Kylin V10 SP1 OS | | | |
| | | Kylin V10 SP2 OS | | | |
| | | Kylin V10 SP3 OS | | | |
| | | openEuler OS | | | |
| | Ascend 910B3 | | | | |

## Iluvatar GPU

| Vendor & Type | Supported GPU Models | Compatible OS (Online) | Recommended Kernel | Recommended OS & Kernel | Installation Guide |
| ----------- | ------ | --------- | ------ | -------- | ----- |
| Iluvatar vGPU | BI100 | CentOS 7 | Kernel 3.10.0-957.el7.x86_64 to 3.10.0-1160.42.2.el7.x86_64 | OS: CentOS 7.9; Kernel: 3.10.0-1160 | [User Guide](./Iluvatar_usage.md) |
| | MR100 | CentOS 8 | Kernel 4.18.0-80.el8.x86_64 to 4.18.0-305.19.1.el8_4.x86_64 | | |
| | | Ubuntu 20.04 | Kernel 4.15.0-20-generic to 4.15.0-160-generic, Kernel 5.4.0-26-generic to 5.4.0-89-generic, Kernel 5.8.0-23-generic to 5.8.0-63-generic | | |
| | | Ubuntu 21.04 | Same kernel ranges as Ubuntu 20.04 | | |
| | | openEuler 22.03 LTS | Kernel ≥ 5.1 and ≤ 5.10 | | |

## Metax GPU

| Vendor & Type | Supported GPU Models | Compatible OS (Online) | Recommended Kernel | Recommended OS & Kernel | Installation Guide |
| ------------- | ------------------ | ------- | ----- | ------- | -------- |
| Metax (Full Card / vGPU) | Xiyun C500 | | | | [Metax GPU Installation Guide](./metax/usemetax.md) |

## Enflame GPU

| Vendor & Type | Supported GPU Models | Compatible OS (Online) | Recommended Kernel | Recommended OS & Kernel | Installation Guide |
| ------- | --------- | ---------- | ---------- | -------- | ------- |
| Enflame (Full Card) | S60 | Ubuntu 22.04 | | | |
| |  CloudFlame T Series | | | | |
| |  CloudFlame I Series | | | | |

## Birentech GPU

| Vendor & Type | Supported GPU Models | Compatible OS (Online) | Recommended Kernel | Recommended OS & Kernel | Installation Guide |
| ----- | ------ | -------- | ------- | ------- | ------ |
| Birentech (Full Card) | Biren 110E | Ubuntu 22.04 | | | |
| | Biren 106M | | | | |
| | Biren 106B, 106C | | | | |
