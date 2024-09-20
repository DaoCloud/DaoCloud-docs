---
hide:
  - toc
---

# GPU 支持矩阵

本页说明 DCE 5.0 支持的 GPU 及操作系统所对应的矩阵。

## NVIDIA GPU

| GPU 厂商及类型 | 支持 GPU 型号 | 适配的操作系统（在线） | 推荐内核 | 推荐的操作系统及内核 | 安装文档 | 
| :--: | :--: | :--: | :--: | :--: | :--: | 
| NVIDIA GPU（整卡/vGPU） | NVIDIA Fermi (2.1) 架构 | CentOS 7 | Kernel 3.10.0-123 ~ 3.10.0-1160内核参考文档建议使用操作系统对应 Kernel 版本 | 操作系统：CentOS 7.9；内核版本： 3.10.0-1160 | GPU Operator 离线安装 | 
| | NVIDIA GeForce 400 系列 | CentOS 8 | Kernel 4.18.0-80 ~ 4.18.0-348 | | | 
| | NVIDIA Quadro 4000 系列 | Ubuntu 20.04 | Kernel 5.4 | | | 
| | NVIDIA Tesla 20 系列 | Ubuntu 22.04 | Kernel 5.19 | | | 
| | NVIDIA Ampere 架构系列(A100;A800;H100) | RHEL 7 | Kernel 3.10.0-123 ~ 3.10.0-1160 | | | 
| | | RHEL 8 | Kernel 4.18.0-80 ~ 4.18.0-348 | | | 
| NVIDIA MIG | NVIDIA Ampere 架构系列（A100、A800、H100） | CentOS 7 | Kernel 3.10.0-123 ~ 3.10.0-1160 | 操作系统：CentOS 7.9；内核版本：3.10.0-1160 | GPU Operator 离线安装 | 
| | | CentOS 8 | Kernel 4.18.0-80 ~ 4.18.0-348 | | | 
| | | Ubuntu 20.04 | Kernel 5.4 | | | 
| | | Ubuntu 22.04 | Kernel 5.19 | | | 
| | | RHEL 7 | Kernel 3.10.0-123 ~ 3.10.0-1160 | | | 
| | | RHEL 8 | Kernel 4.18.0-80 ~ 4.18.0-348 | | |

## 昇腾（Ascend）NPU

  | GPU 厂商及类型 | 支持 NPU 型号 | 适配的操作系统（在线） | 推荐内核 | 推荐的操作系统及内核 | 安装文档 | 
| :--: | :--: | :--: | :--: | :--: | :--: | 
| 昇腾（Ascend 310） | Ascend 310 | Ubuntu 20.04 | 详情参考：内核版本要求 | 操作系统：CentOS 7.9；内核版本：3.10.0-1160 | 300 和 310P 驱动文档 | 
| | Ascend 310P； | CentOS 7.6 | | | | 
| | | CentOS 8.2 | | | | 
| | | KylinV10SP1 操作系统 | | | | 
| | | openEuler 操作系统 | | | | 
| 昇腾（Ascend 910） | Ascend 910B | Ubuntu 20.04 | 详情参考内核版本要求 | 操作系统：CentOS 7.9；内核版本：3.10.0-1160 | 910 驱动文档 | 
| | | CentOS 7.6 | | | | 
| | | CentOS 8.2 | | | | 
| | | KylinV10SP1 操作系统 | | | | 
| | | openEuler 操作系统 | | | |

## 天数智芯（Iluvatar）GPU

 | GPU 厂商及类型 | 支持的 GPU 型号 | 适配的操作系统（在线） | 推荐内核 | 推荐的操作系统及内核 | 安装文档 | 
| :--: | :--: | :--: | :--: | :--: | :--: | 
| 天数智芯(Iluvatar vGPU) | BI100 | CentOS 7 | Kernel 3.10.0-957.el7.x86_64 ~ 3.10.0-1160.42.2.el7.x86_64 | 操作系统：CentOS 7.9；内核版本： 3.10.0-1160 | 补充中 | 
| | MR100； | CentOS 8 | Kernel 4.18.0-80.el8.x86_64 ~ 4.18.0-305.19.1.el8_4.x86_64 | | | 
| | | Ubuntu 20.04 | Kernel 4.15.0-20-generic ~ 4.15.0-160-generic Kernel 5.4.0-26-generic ~ 5.4.0-89-generic Kernel 5.8.0-23-generic ~ 5.8.0-63-generic | | | 
| | | Ubuntu 21.04 | Kernel 4.15.0-20-generic ~ 4.15.0-160-generic Kernel 5.4.0-26-generic ~ 5.4.0-89-generic Kernel 5.8.0-23-generic ~ 5.8.0-63-generic | | | 
| | | openEuler 22.03 LTS | Kernel 版本大于等于 5.1 且小于等于 5.10 | | |
  
## 沐曦（Metax）GPU
| GPU 厂商及类型 | 支持的 GPU 型号 | 适配的操作系统（在线） | 推荐内核 | 推荐的操作系统及内核 | 安装文档 |  
| :--: | :--: | :--: | :--: | :--: | :--: |  
| 沐曦Metax（整卡/vGPU） | 曦云 C500 |  |  |  | [沐曦 GPU 安装使用](./metax/usemetax.md) |
