---
hide:
 - toc
---

# GPU 支持矩阵

## NVIDIA GPU

| GPU 厂商及类型 | 支持 GPU 型号 | 适配的操作系统(在线) | 推荐内核 | 推荐的操作系统及内核 | 安装文档 |
| ------------ | ------------ | ----------------- | ------- | ---------------- | ------- |
| **NVIDIA GPU<br />（整卡/vGPU）** | NVIDIA Fermi (2.1)架构：<br />NVIDIA GeForce 400 系列；<br />NVIDIA Quadro 4000 系列；<br />NVIDIA Tesla 20 系列； | CentOS 7 | Kernel 3.10.0-123 ~ 3.10.0-1160<br />[内核参考文档](https://docs.nvidia.com/grid/15.0/product-support-matrix/index.html#abstract__ubuntu)<br />**建议使用操作系统<br />对应 Kernel 版本**<br /> | 操作系统： CentOS 7.9；<br />内核版本： __3.10.0-1160__ | [GPU Operator 离线安装](nvidia/install_nvidia_driver_of_operator.md) |
| | | CentOS 8 | Kernel 4.18.0-80~4.18.0-348 | | |
| | | Ubuntu 20.04 | Kernel 5.4 | | |
| | | Ubuntu 22.04 | Kernel 5.19 | | |
| | | RHEL 7 | Kernel 3.10.0-123~3.10.0-1160 | | |
| | | RHEL 8 | Kernel 4.18.0-80~4.18.0-348 | | |
| **NVIDIA MIG** | Ampere 架构系列:<br />A100;<br />A800;<br />H100；<br /> 参考：[支持 MIG 的 GPU 卡型号](gpu_matrix.md/#支持 MIG 的 GPU 卡型号) | CentOS 7 | Kernel 3.10.0-123 ~ 3.10.0-1160 | 操作系统： CentOS 7.9；<br />内核版本： __3.10.0-1160__ | [GPU Operator 离线安装](nvidia/install_nvidia_driver_of_operator.md) |
| | | CentOS 8 | Kernel 4.18.0-80~4.18.0-348 | | |
| | | Ubuntu 20.04 | Kernel 5.4 | | |
| | | Ubuntu 22.04 | Kernel 5.19 | | |
| | | RHEL 7 | Kernel 3.10.0-123~3.10.0-1160 | | |
| | | RHEL 8 | Kernel 4.18.0-80~4.18.0-348 | | |

### 支持 MIG 的 GPU 卡型号

从 NVIDIA Ampere 一代开始的 GPU支持 MIG。下表提供了支持 MIG 的 GPU 列表：

| GPU 型号 | 架构 | 微架构 | 计算能力 | 内存大小 | 最大 GI 实例数 |
| -------- | ---- | ----- | ------ | ------- | ------------ |
| H100-SXM5 H100-SXM5 | Hopper | GH100 | 9.0 | 80GB | 7 |
| H100-PCIE H100-PCIE | Hopper | GH100 | 9.0 | 80GB | 7 |
| A100-SXM4 A100-SXM4 | NVIDIA Ampere | GA100 | 8.0 | 40GB | 7 |
| A100-SXM4 A100-SXM4 | NVIDIA Ampere | GA100 | 8.0 | 80GB | 7 |
| A100-PCIE A100-PCIE | NVIDIA Ampere | GA100 | 8.0 | 40GB | 7 |
| A100-PCIE A100-PCI | NVIDIA Ampere | GA100 | 8.0 | 80GB | 7 |
| A30 | NVIDIA Ampere | GA100 | 8.0 | 24GB | 4 |

## 昇腾(Ascend) NPU

| GPU 厂商及类型 | 支持 NPU 型号 | 适配的操作系统(在线) | 推荐内核 | 推荐的操作系统及内核 | 安装文档 |
| ------------ | ------------ | ----------------- | ------ | ----------------- | ------- |
| **昇腾(Ascend 310)** | Ascend 310;<br />Ascend 310P； | Ubuntu20.04 | 详情参考：[内核版本要求](https://www.hiascend.com/document/detail/zh/quick-installation/22.0.0/quickinstg/800_3010/quickinstg_800_3010_x86_0005.html) | 操作系统： CentOS 7.9；<br />内核版本： __3.10.0-1160__ | [300 和 310P 驱动文档](https://www.hiascend.com/document/detail/zh/quick-installation/22.0.0/quickinstg/800_3010/quickinstg_800_3010_x86_0041.html) |
| | | CentOS 7.6 | | | |
| | | CentOS 8.2 | | | |
| | | KylinV10SP1 操作系统 | | | |
| | | openEuler操作系统 | | | |
| **昇腾(Ascend 910P)** | Ascend 910 | Ubuntu20.04 | 详情参考[内核版本要求](https://www.hiascend.com/document/detail/zh/quick-installation/22.0.0/quickinstg/800_9010/quickinstg_800_9010_x86_0005.html) | 操作系统： CentOS 7.9；<br />内核版本： __3.10.0-1160__ | [910 驱动文档](https://www.hiascend.com/document/detail/zh/quick-installation/22.0.0/quickinstg/800_9010/quickinstg_800_9010_x86_0049.html) |
| | | CentOS 7.6 | | | |
| | | CentOS 8.2 | | | |
| | | KylinV10SP1 操作系统 | | | |
| | | openEuler操作系统 | | | |

## 天数智芯(Iluvatar) GPU

| GPU 厂商及类型 | 支持 的 GPU 型号 | 适配的操作系统(在线) | 推荐内核 | 推荐的操作系统及内核 | 安装文档 |
| ------------ | --------------- | ----------------- | ------ | ----------------- | -------- |
| **天数智芯(Iluvatar vGPU)** | BI100;<br />MR100； | CentOS 7 | Kernel 3.10.0-957.el7.x86_64~3.10.0-1160.42.2.el7.x86_64 | 操作系统： CentOS 7.9；<br />内核版本： __3.10.0-1160__ | 补充中 |
| | | CentOS 8 | Kernel 4.18.0-80.el8.x86_64~ 4.18.0-305.19.1.el8_4.x86_64 | | |
| | | Ubuntu 20.04 | Kernel 4.15.0-20-generic ~4.15.0-160-generic<br />Kernel 5.4.0-26-generic ~5.4.0-89-generic<br /> Kernel 5.8.0-23-generic ~5.8.0-63-generic<br /> | | |
| | | Ubuntu 21.04 | Kernel 4.15.0-20-generic ~4.15.0-160-generic<br />Kernel 5.4.0-26-generic ~5.4.0-89-generic<br /> Kernel 5.8.0-23-generic ~5.8.0-63-generic<br /> | | |
| | | openEuler 22.03 LTS | Kernel 版本⼤于等于 5.1 且⼩于等于 5.10 | | |
