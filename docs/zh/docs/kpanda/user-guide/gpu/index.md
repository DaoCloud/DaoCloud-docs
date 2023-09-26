---
hide:
  - toc
---

# GPU 管理概述

本文介绍 Daocloud 容器管理平台对 GPU为代表的异构资源统一运维管理能力。

## 背景信息

随着 AI 应用、大模型、人工智能、自动驾驶等新兴技术的快速发展，企业面临着越来越多的计算密集型任务和数据处理需求。以 CPU 为代表的传统计算架构已无法满足企业日益增长的计算需求。此时，以 GPU 为代表的异构计算因在处理大规模数据、进行复杂计算和实时图形渲染方面具有独特的优势被广泛应用。

与此同时，由于缺乏异构资源调度管理等方面的经验和专业的解决方案，导致了 GPU 设备的资源利用率极低，给企业带来了高昂的 AI 生产成本。如何降本增效，提高 GPU 等异构资源的利用效率，成为了当前众多企业亟需跨越的一道难题。

## Daocloud GPU 管理能力介绍

Daocloud 容器管理平台支持对 GPU、NPU 等异构资源进行统一调度和运维管理，充分释放 GPU 资源算力，加速企业 AI 等新兴应用发展。Daocloud GPU 管理能力如下：

- 支持统一纳管 NVIDIA、华为昇腾、天数等国内外厂商的异构计算资源。
- 支持同一集群多卡异构调度，并支持集群 GPU 卡自动识别。
- 支持 NVIDIA GPU、vGPU、MIG 等 GPU 原生管理方案，并提供云原生能力。
- 支持单块物理卡切分给不同的租户使用，并支持对租户和容器使用 GPU 资源按照算力、显存进行 GPU 资源配额。
- 支持集群、节点、应用等多维度 GPU 资源监控，帮助运维人员管理 GPU 资源。
- 兼容 TensorFlow、pytorch 等多种训练框架。

## Daocloud GPU 支持矩阵

| GPU 厂商 | 类型                | 支持 GPU 型号                                                | 在线版适配的操作系统及内核版本 | 在线版推荐操作系统及内核                                     | 推荐的操作系统 | 推荐的系统内核 | 安装文档                                                     |
| -------- | ------------------- | ------------------------------------------------------------ | ------------------------------ | ------------------------------------------------------------ | -------------- | -------------- | ------------------------------------------------------------ |
| NVIVIDA  | NVIVIDA GPU（整卡） | NVIDIA Fermi (2.1)架构。如NVIDIA GeForce 400 系列、NVIDIA Quadro 4000 系列、NVIDIA Tesla 20 系列 | CentOS 7                       | 操作系统支持的版本范围即可。Kernel 3.10.0-123 ~ 3.10.0-1160  | CentOS 7.9     | `3.10.0-1160`  | [内核参考文档](https://blog.csdn.net/weixin_42915431/article/details/105845001) |
|          |                     |                                                              | CentOS 8                       | Kernel 4.18.0-80~4.18.0-348                                  |                |                |                                                              |
|          |                     |                                                              | Ubuntu 20.04                   | Kernel 5.4                                                   |                |                |                                                              |
|          | NVIVIDA GPU（vGPU） |                                                              | Ubuntu 22.04                   | Kernel 5.19                                                  |                |                |                                                              |
|          |                     |                                                              | RHEL 7                         | Kernel 3.10.0-123~3.10.0-1160                                |                |                |                                                              |
|          |                     |                                                              | RHEL 8                         | Kernel 4.18.0-80~4.18.0-348                                  |                |                |                                                              |
|          | NVIVIDA MIG         | NVIDIA Ampere架构系列。如：A100,A800,H100等                  | CentOS 7                       | Kernel 3.10.0-123 ~ 3.10.0-1160                              | CentOS 7.9     | `3.10.0-1160`  |                                                              |
|          |                     |                                                              | CentOS 8                       | Kernel 4.18.0-80~4.18.0-348                                  |                |                |                                                              |
|          |                     |                                                              | Ubuntu 20.04                   | Kernel 5.4                                                   |                |                |                                                              |
|          |                     |                                                              | Ubuntu 22.04                   | Kernel 5.19                                                  |                |                |                                                              |
|          |                     |                                                              | RHEL 7                         | Kernel 3.10.0-123~3.10.0-1160                                |                |                |                                                              |
|          |                     |                                                              | RHEL 8                         | Kernel 4.18.0-80~4.18.0-348                                  |                |                |                                                              |
| 天数     | Iluvatar vGPU       | BI100、MR100                                                 | CentOS 7                       | Kernel 3.10.0-957.el7.x86_64~3.10.0-1160.42.2.el7.x86_64     | CentOS 7.9     | `3.10.0-1160`  | 补充中                                                       |
|          |                     |                                                              | CentOS 8                       | Kernel 4.18.0-80.el8.x86_64~ 4.18.0-305.19.1.el8_4.x86_64 （详情参考文档） |                |                |                                                              |
|          |                     |                                                              | Ubuntu 20.04                   | Kernel 4.15.0-20-generic ~4.15.0-160-genericKernel 5.4.0-26-generic ~5.4.0-89-generic Kernel 5.8.0-23-generic ~5.8.0-63-generic详情参考文档 |                |                |                                                              |
|          |                     |                                                              | Ubuntu 21.04                   |                                                              |                |                |                                                              |
|          |                     |                                                              | openEuler 22.03 LTS            | Kernel 版本⼤于等于 5.1 且⼩于等于 5.10                      |                |                |                                                              |
| 昇腾     | Ascend 310          | Ascend 310/Ascend 310P                                       | Ubuntu20.04                    | 详情参考：[内核版本要求](https://www.hiascend.com/document/detail/zh/quick-installation/22.0.0/quickinstg/800_3010/quickinstg_800_3010_x86_0005.html) | CentOS 7.9     | `3.10.0-1160`  | [300和310P驱动文档](https://www.hiascend.com/document/detail/zh/quick-installation/22.0.0/quickinstg/800_3010/quickinstg_800_3010_x86_0041.html) |
|          |                     |                                                              | CentOS 7.6                     |                                                              |                |                |                                                              |
|          |                     |                                                              | CentOS 8.2                     |                                                              |                |                |                                                              |
|          |                     |                                                              | KylinV10SP1 操作系统           |                                                              |                |                |                                                              |
|          |                     |                                                              | openEuler操作系统              |                                                              |                |                |                                                              |
|          | Ascend 310P         | Ascend 910                                                   | Ubuntu20.04                    | 详情参考:[ 内核版本要求](https://www.hiascend.com/document/detail/zh/quick-installation/22.0.0/quickinstg/800_9010/quickinstg_800_9010_x86_0005.html) | CentOS 7.9     | `3.10.0-1160`  | [910驱动文档](https://www.hiascend.com/document/detail/zh/quick-installation/22.0.0/quickinstg/800_9010/quickinstg_800_9010_x86_0049.html) |
|          |                     |                                                              | CentOS 7.6                     |                                                              |                |                |                                                              |
|          |                     |                                                              | CentOS 8.2                     |                                                              |                |                |                                                              |
|          |                     |                                                              | KylinV10SP1 操作系统           |                                                              |                |                |                                                              |
|          |                     |                                                              | openEuler操作系统              |                                                              |                |                |                                                              |
