---
hide:
  - toc
---

# GPU Support Matrix

This page explains the matrix of supported GPUs and operating systems for DCE 5.0.

## NVIDIA GPU

<table>
<tr>
<th>GPU Manufacturer and Type</th>
<th>Supported GPU Models</th>
<th>Compatible Operating System (Online)</th>
<th>Recommended Kernel</th>
<th>Recommended Operating System and Kernel</th>
<th>Installation Documentation</th>
</tr>
<tr>
<td><strong>NVIDIA GPU (Full Card/vGPU)</strong></td>
<td>
<ul>
<li>NVIDIA Fermi (2.1) Architecture:</li>
<li>NVIDIA GeForce 400 Series</li>
<li>NVIDIA Quadro 4000 Series</li>
<li>NVIDIA Tesla 20 Series</li>
<li>NVIDIA Ampere Architecture Series (A100; A800; H100)</li>
</ul>
</td>
<td>CentOS 7</td>
<td>
<ul>
<li>Kernel 3.10.0-123 ~ 3.10.0-1160</li>
<li><a href="https://docs.nvidia.com/grid/15.0/product-support-matrix/index.html#abstract__ubuntu">Kernel Reference Document</a></li>
<li><strong>Recommended Operating System <br />with Proper Kernel Version</strong></li>
</ul>
</td>
<td>Operating System: CentOS 7.9; <br />Kernel Version: <strong>3.10.0-1160</strong> </td>
<td><a href="nvidia/install_nvidia_driver_of_operator.md">Offline Installation with GPU Operator</a></td>
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
<li>Ampere Architecture Series:</li>
<li>A100</li>
<li>A800</li>
<li>H100</li>
</ul>
</td>
<td>CentOS 7</td>
<td>Kernel 3.10.0-123 ~ 3.10.0-1160</td>
<td>Operating System: CentOS 7.9; <br />Kernel Version: <strong>3.10.0-1160</strong> </td>
<td><a href="nvidia/install_nvidia_driver_of_operator.md">Offline Installation with GPU Operator</a></td>
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

## Ascend NPU

<table>
<tr>
<th>GPU Manufacturer and Type</th>
<th>Supported NPU Models</th>
<th>Compatible Operating System (Online)</th>
<th>Recommended Kernel</th>
<th>Recommended Operating System and Kernel</th>
<th>Installation Documentation</th>
</tr>
<tr>
<td><strong>Ascend (Ascend 310)</strong></td>
<td>
<ul>
<li>Ascend 310;</li>
<li>Ascend 310P;</li>
</ul>
</td>
<td>Ubuntu 20.04</td>
<td>Details refer to: <a href="https://www.hiascend.com/document/detail/zh/quick-installation/22.0.0/quickinstg/800_3010/quickinstg_800_3010_x86_0005.html">Kernel Version Requirements</a></td>
<td>Operating System: CentOS 7.9; <br />Kernel Version: <strong>3.10.0-1160</strong> </td>
<td><a href="https://www.hiascend.com/document/detail/zh/quick-installation/22.0.0/quickinstg/800_3010/quickinstg_800_3010_x86_0041.html">300 and 310P Driver Documentation</a></td>
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
<td>KylinV10SP1 Operating System</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>openEuler Operating System</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><strong>Ascend (Ascend 910P)</strong></td>
<td>Ascend 910</td>
<td>Ubuntu 20.04</td>
<td>Details refer to: <a href="https://www.hiascend.com/document/detail/zh/quick-installation/22.0.0/quickinstg/800_9010/quickinstg_800_9010_x86_0005.html">Kernel Version Requirements</a></td>
<td>Operating System: CentOS 7.9; <br />Kernel Version: <strong>3.10.0-1160</strong> </td>
<td><a href="https://www.hiascend.com/document/detail/zh/quick-installation/22.0.0/quickinstg/800_9010/quickinstg_800_9010_x86_0049.html">910 Driver Documentation</a></td>
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
<td>KylinV10SP1 Operating System</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td></td>
<td></td>
<td>openEuler Operating System</td>
<td></td>
<td></td>
<td></td>
</tr>
</table>

## Iluvatar GPU

<table>
<tr>
<th>GPU Manufacturer and Type</th>
<th>Supported GPU Models</th>
<th>Compatible Operating System (Online)</th>
<th>Recommended Kernel</th>
<th>Recommended Operating System and Kernel</th>
<th>Installation Documentation</th>
</tr>
<tr>
<td><strong>Iluvatar (Iluvatar vGPU)</strong></td>
<td>
<ul>
<li>BI100;</li>
<li>MR100;</li>
</ul>
</td>
<td>CentOS 7</td>
<td>
<ul>
<li>Kernel 3.10.0-957.el7.x86_64 ~ 3.10.0-1160.42.2.el7.x86_64</li>
</ul>
</td>
<td>Operating System: CentOS 7.9; <br />Kernel Version: <strong>3.10.0-1160</strong> </td>
<td>Coming Soon</td>
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
<li>Kernel version >= 5.1 and <= 5.10</li>
</ul>
</td>
<td></td>
<td></td>
</tr>
</table>
