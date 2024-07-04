---
hide:
  - toc
---

# GPU 支持矩阵

本页说明 DCE 5.0 支持的 GPU 及操作系统所对应的矩阵。

## NVIDIA GPU

<table>
<tr>
<th>GPU 厂商及类型</th>
<th>支持 GPU 型号</th>
<th>适配的操作系统(在线)</th>
<th>推荐内核</th>
<th>推荐的操作系统及内核</th>
<th>安装文档</th>
</tr>
<tr>
<td><strong>NVIDIA GPU（整卡/vGPU）</strong></td>
<td>
<ul>
<li>NVIDIA Fermi (2.1)架构：</li>
<li>NVIDIA GeForce 400 系列</li>
<li>NVIDIA Quadro 4000 系列</li>
<li>NVIDIA Tesla 20 系列</li>
<li>NVIDIA Ampere 架构系列(A100;A800;H100)</li>
</ul>
</td>
<td>CentOS 7</td>
<td>
<ul>
<li>Kernel 3.10.0-123 ~ 3.10.0-1160</li>
<li><a href="https://docs.nvidia.com/grid/15.0/product-support-matrix/index.html#abstract__ubuntu">内核参考文档</a></li>
<li><strong>建议使用操作系统<br />对应 Kernel 版本</strong></li>
</ul>
</td>
<td>操作系统：CentOS 7.9；<br />内核版本： <strong>3.10.0-1160</strong> </td>
<td><a href="nvidia/install_nvidia_driver_of_operator.md">GPU Operator 离线安装</a></td>
</tr>
<tr>
<td></td>
<td></td>
<td>CentOS 8</td>
<td>Kernel 4.18.0-80 ~ 4.18.0-348</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Ubuntu 20.04</td>
<td>Kernel 5.4</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Ubuntu 22.04</td>
<td>Kernel 5.19</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>RHEL 7</td>
<td>Kernel 3.10.0-123 ~ 3.10.0-1160</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>RHEL 8</td>
<td>Kernel 4.18.0-80 ~ 4.18.0-348</td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>NVIDIA MIG</strong></td>
<td>
<ul>
<li>Ampere 架构系列：</li>
<li>A100</li>
<li>A800</li>
<li>H100</li>
</ul>
</td>
<td>CentOS 7</td>
<td>Kernel 3.10.0-123 ~ 3.10.0-1160</td>
<td>操作系统：CentOS 7.9；<br />内核版本： <strong>3.10.0-1160</strong> </td>
<td><a href="nvidia/install_nvidia_driver_of_operator.md">GPU Operator 离线安装</a></td>
</tr>
<tr>
<td></td>
<td></td>
<td>CentOS 8</td>
<td>Kernel 4.18.0-80 ~ 4.18.0-348</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Ubuntu 20.04</td>
<td>Kernel 5.4</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Ubuntu 22.04</td>
<td>Kernel 5.19</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>RHEL 7</td>
<td>Kernel 3.10.0-123 ~ 3.10.0-1160</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>RHEL 8</td>
<td>Kernel 4.18.0-80 ~ 4.18.0-348</td>
<td></td>
<td></td>
</tr>
</table>

## 昇腾（Ascend）NPU

<table>
<tr>
<th>GPU 厂商及类型</th>
<th>支持 NPU 型号</th>
<th>适配的操作系统(在线)</th>
<th>推荐内核</th>
<th>推荐的操作系统及内核</th>
<th>安装文档</th>
</tr>
<tr>
<td><strong>昇腾(Ascend 310)</strong></td>
<td>
<ul>
<li>Ascend 310;</li>
<li>Ascend 310P；</li>
</ul>
</td>
<td>Ubuntu20.04</td>
<td>详情参考：<a href="https://www.hiascend.com/document/detail/zh/quick-installation/22.0.0/quickinstg/800_3010/quickinstg_800_3010_x86_0005.html">内核版本要求</a></td>
<td>操作系统：CentOS 7.9；<br />内核版本： <strong>3.10.0-1160</strong> </td>
<td><a href="https://www.hiascend.com/document/detail/zh/quick-installation/22.0.0/quickinstg/800_3010/quickinstg_800_3010_x86_0041.html">300 和 310P 驱动文档</a></td>
</tr>
<tr>
<td></td>
<td></td>
<td>CentOS 7.6</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>CentOS 8.2</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>KylinV10SP1 操作系统</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>openEuler 操作系统</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>昇腾(Ascend 910)</strong></td>
<td>Ascend 910B</td>
<td>Ubuntu20.04</td>
<td>详情参考<a href="https://www.hiascend.com/document/detail/zh/quick-installation/22.0.0/quickinstg/800_9010/quickinstg_800_9010_x86_0005.html">内核版本要求</a></td>
<td>操作系统：CentOS 7.9；<br />内核版本： <strong>3.10.0-1160</strong> </td>
<td><a href="https://www.hiascend.com/document/detail/zh/quick-installation/22.0.0/quickinstg/800_9010/quickinstg_800_9010_x86_0049.html">910 驱动文档</a></td>
</tr>
<tr>
<td></td>
<td></td>
<td>CentOS 7.6</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>CentOS 8.2</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>KylinV10SP1 操作系统</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>openEuler 操作系统</td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

## 天数智芯（Iluvatar） GPU

<table>
<tr>
<th>GPU 厂商及类型</th>
<th>支持 的 GPU 型号</th>
<th>适配的操作系统(在线)</th>
<th>推荐内核</th>
<th>推荐的操作系统及内核</th>
<th>安装文档</th>
</tr>
<tr>
<td><strong>天数智芯(Iluvatar vGPU)</strong></td>
<td>
<ul>
<li>BI100;</li>
<li>MR100；</li>
</ul>
</td>
<td>CentOS 7</td>
<td>
<ul>
<li>Kernel 3.10.0-957.el7.x86_64 ~ 3.10.0-1160.42.2.el7.x86_64</li>
</ul>
</td>
<td>操作系统：CentOS 7.9；<br />内核版本： <strong>3.10.0-1160</strong> </td>
<td>补充中</td>
</tr>
<tr>
<td></td>
<td></td>
<td>CentOS 8</td>
<td>
<ul>
<li>Kernel 4.18.0-80.el8.x86_64 ~ 4.18.0-305.19.1.el8_4.x86_64</li>
</ul>
</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Ubuntu 20.04</td>
<td>
<ul>
<li>Kernel 4.15.0-20-generic ~ 4.15.0-160-generic</li>
<li>Kernel 5.4.0-26-generic ~ 5.4.0-89-generic</li>
<li>Kernel 5.8.0-23-generic ~ 5.8.0-63-generic</li>
</ul>
</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>Ubuntu 21.04</td>
<td>
<ul>
<li>Kernel 4.15.0-20-generic ~ 4.15.0-160-generic</li>
<li>Kernel 5.4.0-26-generic ~ 5.4.0-89-generic</li>
<li>Kernel 5.8.0-23-generic ~ 5.8.0-63-generic</li>
</ul>
</td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>openEuler 22.03 LTS</td>
<td>
<ul>
<li>Kernel 版本⼤于等于 5.1 且⼩于等于 5.10</li>
</ul>
</td>
<td></td>
<td></td>
</tr>
</table>
