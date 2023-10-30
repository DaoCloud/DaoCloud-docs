---
hide:
  - toc
---

# GPU Support Matrix

## NVIDIA GPU

| GPU Manufacturer and Model        | Supported GPU Models                                         | Supported OS (Online) | Recommended Kernel                                          | Recommended OS and Kernel                            | Installation Documentation                                   |
| --------------------------------- | ------------------------------------------------------------ | ----------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------------------ |
| **NVIDIA GPU<br />(Full Card/vGPU)** | NVIDIA Fermi (2.1) architecture:<br />NVIDIA GeForce 400 series;<br />NVIDIA Quadro 4000 series;<br />NVIDIA Tesla 20 series; | CentOS 7                             | Kernel 3.10.0-123 ~ 3.10.0-1160<br />[Kernel Reference](https://docs.nvidia.com/grid/15.0/product-support-matrix/index.html#abstract__ubuntu)<br />**Recommended OS with corresponding Kernel version** | OS: CentOS 7.9;<br />Kernel version: `3.10.0-1160` | [Offline Installation of GPU Operator](nvidia/install_nvidia_driver_of_operator.md) |
|                                   |                                                              |                                     |                                                              |                                                      |                                                              |
|                                   |                                                              | CentOS 8                             | Kernel 4.18.0-80~4.18.0-348                                  |                                                      |                                                              |
|                                   |                                                              | Ubuntu 20.04                         | Kernel 5.4                                                   |                                                      |                                                              |
|                                   |                                                              | Ubuntu 22.04                         | Kernel 5.19                                                  |                                                      |                                                              |
|                                   |                                                              | RHEL 7                               | Kernel 3.10.0-123~3.10.0-1160                                |                                                      |                                                              |
|                                   |                                                              | RHEL 8                               | Kernel 4.18.0-80~4.18.0-348                                  |                                                      |                                                              |
| **NVIDIA MIG**                    | Ampere architecture series:<br />A100;<br />A800;<br />H100;<br />Reference: [Supported GPU Models with MIG](gpu_matrix.md/#Supported GPU Models with MIG) | CentOS 7                             | Kernel 3.10.0-123 ~ 3.10.0-1160                              | OS: CentOS 7.9;<br />Kernel version: `3.10.0-1160` | [Offline Installation of GPU Operator](nvidia/install_nvidia_driver_of_operator.md) |
|                                   |                                                              | CentOS 8                             | Kernel 4.18.0-80~4.18.0-348                                  |                                                      |                                                              |
|                                   |                                                              | Ubuntu 20.04                         | Kernel 5.4                                                   |                                                      |                                                              |
|                                   |                                                              | Ubuntu 22.04                         | Kernel 5.19                                                  |                                                      |                                                              |
|                                   |                                                              | RHEL 7                               | Kernel 3.10.0-123~3.10.0-1160                                |                                                      |                                                              |
|                                   |                                                              | RHEL 8                               | Kernel 4.18.0-80~4.18.0-348                                  |                                                      |                                                              |

### Supported GPU Models with MIG

The following table provides a list of GPUs that support MIG starting from the NVIDIA Ampere generation:

| GPU Model            | **Architecture** | **Microarchitecture** | **Compute Capability** | **Memory Size** | **Max. Number of GI Instances** |
| -------------------- | ---------------- | -------------------- | --------------------- | --------------- | ------------------------------ |
| H100-SXM5 H100-SXM5  | Hopper           | GH100                | 9.0                   | 80GB            | 7                              |
| H100-PCIE H100-PCIE  | Hopper           | GH100                | 9.0                   | 80GB            | 7                              |
| A100-SXM4 A100-SXM4  | NVIDIA Ampere    | GA100                | 8.0                   | 40GB            | 7                              |
| A100-SXM4 A100-SXM4  | NVIDIA Ampere    | GA100                | 8.0                   | 80GB            | 7                              |
| A100-PCIE A100-PCIE  | NVIDIA Ampere    | GA100                | 8.0                   | 40GB            | 7                              |
| A100-PCIE A100-PCIE  | NVIDIA Ampere    | GA100                | 8.0                   | 80GB            | 7                              |
| A30                  | NVIDIA Ampere    | GA100                | 8.0                   | 24GB            | 4                              |

## Ascend GPU

| GPU Manufacturer and Model | Supported GPU Models             | Supported OS (Online) | Recommended Kernel                                          | Recommended OS and Kernel                            | Installation Documentation                                   |
| -------------------------- | -------------------------------- | ----------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------------------ |
| **Ascend 310**             | Ascend 310;<br />Ascend 310P     | Ubuntu 20.04                         | Refer to: [Kernel Version Requirements](https://www.hiascend.com/document/detail/en/quick-installation/22.0.0/quickinstg/800_3010/quickinstg_800_3010_x86_0005.html) | OS: CentOS 7.9;<br />Kernel version: `3.10.0-1160` | [Driver Documentation for 300 and 310P](https://www.hiascend.com/document/detail/en/quick-installation/22.0.0/quickinstg/800_3010/quickinstg_800_3010_x86_0041.html) |
|                            |                                  | CentOS 7.6                           |                                                              |                                                      |                                                              |
|                            |                                  | CentOS 8.2                           |                                                              |                                                      |                                                              |
|                            |                                  | Kylin V10SP1 Operating System        |                                                              |                                                      |                                                              |
|                            |                                  | openEuler Operating System           |                                                              |                                                      |                                                              |
| **Ascend 910P**            | Ascend 910                       | Ubuntu 20.04                         | Refer to: [Kernel Version Requirements](https://www.hiascend.com/document/detail/en/quick-installation/22.0.0/quickinstg/800_9010/quickinstg_800_9010_x86_0005.html) | OS: CentOS 7.9;<br />Kernel version: `3.10.0-1160` | [910 Driver Documentation](https://www.hiascend.com/document/detail/en/quick-installation/22.0.0/quickinstg/800_9010/quickinstg_800_9010_x86_0049.html) |
|                            |                                  | CentOS 7.6                           |                                                              |                                                      |                                                              |
|                            |                                  | CentOS 8.2                           |                                                              |                                                      |                                                              |
|                            |                                  | Kylin V10SP1 Operating System        |                                                              |                                                      |                                                              |
|                            |                                  | openEuler Operating System           |                                                              |                                                      |                                                              |

## Iluvatar GPU

| GPU Manufacturer and Model | Supported GPU Models | Supported OS (Online) | Recommended Kernel                                          | Recommended OS and Kernel                           | Installation Documentation |
| -------------------------- | -------------------- | ----------------------------------- | ----------------------------------------------------------- | --------------------------------------------------- | -------------------------- |
| **Iluvatar vGPU**   | BI100;<br />MR100； | CentOS 7                            | Kernel 3.10.0-957.el7.x86_64~3.10.0-1160.42.2.el7.x86_64     | Operating System: CentOS 7.9;<br />Kernel Version: `3.10.0-1160` | In progress                |
|                            |                      | CentOS 8                            | Kernel 4.18.0-80.el8.x86_64~ 4.18.0-305.19.1.el8_4.x86_64    |                                                     |                             |
|                            |                      | Ubuntu 20.04                        | Kernel 4.15.0-20-generic ~4.15.0-160-generic<br />Kernel 5.4.0-26-generic ~5.4.0-89-generic<br />Kernel 5.8.0-23-generic ~5.8.0-63-generic<br /> |                                                     |                             |
|                            |                      | Ubuntu 21.04                        |                                                              |                                                     |                             |
|                            |                      | openEuler 22.03 LTS                 | Kernel version greater than or equal to 5.1 and less than or equal to 5.10                      |                                                     |                             |
