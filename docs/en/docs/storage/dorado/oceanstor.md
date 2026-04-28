---
hide:
  - navigation
---

# OceanStor A Series Storage and DaoCloud d.run Computing Scheduling Platform Compatibility Test Report

## 1 Environment Configuration

### 1.1 Verification Network Diagram

![img](./images/clip_image008.png)

<div style="text-align:center;">Figure 1-1 Functional Verification Network Diagram</div>

### 1.2 Hardware and Software Configuration

#### 1.2.1 Storage System Configuration

This test requires a set of Huawei OceanStor A800 storage system, configuration reference as follows:

Table 1-1 OceanStor A800 Configuration

| Name | Description | Model | Unit Height | Quantity |
| --- | ------- | -------- | -------- | -------- |
| AI Storage | OceanStor A800 <br />Control enclosure: 2 controllers <br />CPU per controller: 4*Kunpeng920-7260X <br />Memory per controller: 1TB <br />Disk: 1.746TB NVMe PALM disk 20 pieces <br />Network: 4 * 2-port 25GE RoCE NIC; 2 * 4-port 25GE ETH NIC | OceanStor A800 | 8U | 1 |

#### 1.2.2 Supporting Test Hardware

Table 1-2 Supporting Hardware Configuration

| Name | Description | Model | Unit Height | Quantity |
| --- | --- | -----| ------ | ---- |
| Inference Server | <br />CPU: 2 * HUAWEI Kunpeng 920 <br />NPU: 8 * Ascend 910B (64G VRAM) <br />NIC 1: 4 * 2-port 200GE ROCE NIC (parameter plane, optional) <br />NIC 2: 1 * 2-port 25GE ROCE NIC (data plane) <br />NIC 3: 1 * 4-port 25GE ETH NIC (business plane) <br />System Disk: 2 * 480GB SATA SSD | Atlas 800T A2 | 4U | 1 |
| Business Switch | Used for connecting business and storage plane network | CE6865 | 1U | 1 |
| Parameter Plane Switch (not required for single node) | Used for computing server parameter plane network, using 400GE 1-to-2 cable to connect computing server | XH9210 | 1U | 1 |

#### 1.2.3 Test Software and Tools

Table 1-3 Test Software and Tools
