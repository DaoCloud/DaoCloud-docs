---
hide:
  - navigation
---

# AI & 视频加速卡驱动下载

授权组织：DaoCloud

本页列出加速卡各版本的驱动供用户下载。

## 2024-05

### k8s_v0.0.4-1

!!! note "版本说明 20240530"

    K8s Docker 支持 DC1000 多卡环境

| 板卡类型 | 软件类型 | OS | 架构 | 文件大小 | 下载 | md5  | 发布时间 |
| :-----: | :-----: | :-----: | :----: | :-----: | :--: | :----: | :-----: |
| SG100 | Driver | Linux | arm | 72.24 MB | [:arrow_down: v0.0.4-1.tar.gz](https://harbor-test2.cn-sh2.ufileos.com/docs/drivers/v0.0.4-1.tar.gz) | f96b90e0629b91451086fef82336cd61 | **2024-05-30** 10:58:11 |

### tools_3.0.1-20240430-vaqual_sg-aarch64-mfg

!!! note "版本说明 20240529"

    此版本仅用于工厂测试。

    - 测试工具依赖板卡 PCIe 驱动，驱动安装：参考测试指导手册 2.3 DKMS 和 2.4 PCIe 驱动安装章节
    - 板卡压力测试和功耗测试：参考测试指导手册 3.2.13 功耗测试章节（此版本不依赖于 GPU DDK 驱动，测试请跳过步骤 1-3）
    - 板卡显存测试：参考测试指导手册 3.2.10 DDR 带宽测试章节

| 板卡类型 | 软件类型 | OS | 架构 | 文件大小 | 下载 | md5  | 发布时间 |
| :-----: | :-----: | :-----: | :----: | :-----: | :--: | :----: | :-----: |
| VG1000 | Driver | Linux | arm | 5.63 MB| [:arrow_down: va-pci-mainline-hwtype-0_00.24.01.15_aarch64.rpm](https://harbor-test2.cn-sh2.ufileos.com/docs/drivers/va-pci-mainline-hwtype-0_00.24.01.15_aarch64.rpm) | 3088c42bc2fd79b77ecc6f59e706a560 | **2024-05-29** 12:25:42 |
| VG1000 | Driver | Linux | arm | 4.52 MB | [:arrow_down: va-pci-mainline-hwtype-0_00.24.01.15_aarch64.deb](https://harbor-test2.cn-sh2.ufileos.com/docs/drivers/va-pci-mainline-hwtype-0_00.24.01.15_aarch64.deb) | 331399104cd5df7de02a1c3ee51e5a9c | **2024-05-29** 12:25:42 |
| VG1000 | Driver | Linux | arm | 269.62 MB | [:arrow_down: tools_3.0.1-20240430-vaqual_sg-aarch64-mfg.tar.gz](https://harbor-test2.cn-sh2.ufileos.com/docs/drivers/tools_3.0.1-20240430-vaqual_sg-aarch64-mfg.tar.gz) | ea44811c92ef880adb3e5d67d9bb56ba | **2024-05-29** 12:25:42 |

参阅 [DC1000 加速卡测试指导手册_A1.pdf](https://harbor-test2.cn-sh2.ufileos.com/docs/drivers/DC1000-test-manual_A1.pdf)。

### VAGPU-KP-24.01.02.09-DC

!!! note "版本说明 20240516"

    - 解决崩坏星铁优化导致的渲染错误
    - 解决高负载下删除容器导致的驱动报错
    - 增加驱动版本号在内核态和用户态的查询
    - 删除 fps_lock 对应的相关代码
    - 解决 ion_linux.ko 无法卸载的问题
    - 解决高德地图 3D 渲染错误
    - kernel 5.10.0-136.12 和 5.10.0-182 使用相同的 ko

| 板卡类型 | 软件类型 | OS | 架构 | 文件大小 | 下载 | md5  | 发布时间 |
| :-----: | :-----: | :-----: | :----: | :-----: | :--: | :----: | :-----: |
| SG100 | Driver | Linux | arm | 285.22 MB | [:arrow_down: VAGPU-KP-24.01.02.09-DC.tgz](https://harbor-test2.cn-sh2.ufileos.com/docs/drivers/VAGPU-KP-24.01.02.09-DC.tgz) | f16714db3a86e1a03c3407dfd065a425 | **2024-05-16** 16:34:41 |

### VAGPU-KP-24.01.02.08-DC

!!! note "版本说明 20240516"

    - 解决崩坏星铁优化导致的渲染错误
    - 解决高负载下删除容器导致的驱动报错
    - 增加驱动版本号在内核态和用户态的查询
    - 删除 fps_lock 对应的相关代码
    - 解决 ion_linux.ko 无法卸载的问题
    - 解决高德地图 3D 渲染错误

| 板卡类型 | 软件类型 | OS | 架构 | 文件大小 | 下载 | md5  | 发布时间 |
| :-----: | :-----: | :-----: | :----: | :-----: | :--: | :----: | :-----: |
| SG100 | Driver | Linux | arm | 303.85 MB | [:arrow_down: VAGPU-KP-24.01.02.08-DC.tgz](https://harbor-test2.cn-sh2.ufileos.com/docs/drivers/VAGPU-KP-24.01.02.08-DC.tgz) | b4e0a259b540a65506cb5f7bff3a8b67 | **2024-05-16** 14:12:06 |

## 2024-04

### tools_3.0.1-20240430-vaqual_sg-aarch64

!!! note "版本说明 20240430"

    解决功耗压测过程中解码超时问题。

| 板卡类型 | 软件类型 | OS | 架构 | 文件大小 | 下载 | md5  | 发布时间 |
| :-----: | :-----: | :-----: | :----: | :-----: | :--: | :----: | :-----: |
| VG1000 | Application | Linux | arm | 269.68 MB | [:arrow_down: tools_3.0.1-20240430-vaqual_sg-aarch64.tar.gz](https://harbor-test2.cn-sh2.ufileos.com/docs/drivers/tools_3.0.1-20240430-vaqual_sg-aarch64.tar.gz) | 8d825f1127d8101c4d4167db3db9ba99 | **2024-04-30** 13:23:45 |

### VAGPU-KP-24.01.02.07-DC

!!! note "版本说明 20240426"

    - 修复一些 dEQP 崩溃问题
    - 更新 HWC SDK 以进行 NDK 构建
    - 更新 gpu_config.sh 以用于 k8s 部署

| 板卡类型 | 软件类型 | OS | 架构 | 文件大小 | 下载 | md5  | 发布时间 |
| :-----: | :-----: | :-----: | :----: | :-----: | :--: | :----: | :-----: |
| SG100 | Driver | Linux | arm | 286.06 MB | [:arrow_down: VAGPU-KP-24.01.02.07-DC.tgz](https://harbor-test2.cn-sh2.ufileos.com/docs/drivers/VAGPU-KP-24.01.02.07-DC.tgz) | 8d825f1127d8101c4d4167db3db9ba99 | **2024-04-26** 12:54:32 |

### VAGPU-KP-24.01.02.06-DC

!!! note "版本说明 20240419"

    - 修复高负载下重启容器系统卡住的问题
    - 修复显存使用过高导致的驱动错误和系统崩溃
    - 修复使用工具查询解码率错误的问题
    - 修改 SDK 头文件适配 NDK 编译

| 板卡类型 | 软件类型 | OS | 架构 | 文件大小 | 下载 | md5  | 发布时间 |
| :-----: | :-----: | :-----: | :----: | :-----: | :--: | :----: | :-----: |
| SG100 | Driver | Linux | arm | 146.86 MB| [:arrow_down: VAGPU-KP-24.01.02.06-DC.tgz](https://harbor-test2.cn-sh2.ufileos.com/docs/drivers/VAGPU-KP-24.01.02.06-DC.tgz) | 4762c05b45c5a62f69013c7ca730116d | **2024-04-19** 21:13:59 |

### VAGPU-KP-24.01.02.05-DC

!!! note "版本说明 20240412"

    - 增加 5.10.0-136.12.0 和 5.10.0-182.0.0 两个 kernel 对应的 ion_linux.ko
    - 更新 va_gfx.ini 文件来解决抖音播放绿屏的问题
    - 不再提供 libstagefright.so/libstagefright_omx.so，需要客户根据 omx release 里对应的 patch 进行集成

| 板卡类型 | 软件类型 | OS | 架构 | 文件大小 | 下载 | md5  | 发布时间 |
| :-----: | :-----: | :-----: | :----: | :-----: | :--: | :----: | :-----: |
| SG100 | Driver | Linux | arm | 157.67 MB| [:arrow_down: VAGPU-KP-24.01.02.05-DC.tgz](https://harbor-test2.cn-sh2.ufileos.com/docs/drivers/VAGPU-KP-24.01.02.05-DC.tgz) | 799dd7e30daf2a7460da644f6699f5db | **2024-04-12** 18:46:56 |

## 2024-03

### VAGPU-KP-24.01.02.04-DC

!!! note "版本说明 20240329"

    优化编码时延，解决小米手机上解码时延高的问题。

| 板卡类型 | 软件类型 | OS | 架构 | 文件大小 | 下载 | md5  | 发布时间 |
| :-----: | :-----: | :-----: | :----: | :-----: | :--: | :----: | :-----: |
| SG100 | Driver | Linux | arm | 160.30 MB | [:arrow_down: VAGPU-KP-24.01.02.04-DC.tgz](https://harbor-test2.cn-sh2.ufileos.com/docs/drivers/VAGPU-KP-24.01.02.04-DC.tgz) | d24f598c5a82820d9f8b54a277d72755 | **2024-03-29** 16:23:47 |

### VAGPU-KP-24.01.02.03-DC

!!! note "版本说明 20240319"

    - 修复多卡出流重连失败问题
    - 增加 ffmpeg 打印到 logcat，优化 log 打印等级

| 板卡类型 | 软件类型 | OS | 架构 | 文件大小 | 下载 | md5  | 发布时间 |
| :-----: | :-----: | :-----: | :----: | :-----: | :--: | :----: | :-----: |
| SG100 | Driver | Linux | arm | 279.25 MB | [:arrow_down: VAGPU-KP-24.01.02.03-DC.tgz](https://harbor-test2.cn-sh2.ufileos.com/docs/drivers/VAGPU-KP-24.01.02.03-DC.tgz) | 1be5c82eb13cbfb881968dbd8750e2b8 | **2024-03-19** 16:45:54 |

### VAGPU-KP-24.01.02.02-DC

!!! note "版本说明 20240308"

    - 优化了界面滑动过程中的显示效果及使用体验
    - 增加了静态画面连续送帧功能

    使用属性 displayServer.maxInterval 的默认值，不需要额外设置！

| 板卡类型 | 软件类型 | OS | 架构 | 文件大小 | 下载 | md5  | 发布时间 |
| :-----: | :-----: | :-----: | :----: | :-----: | :--: | :----: | :-----: |
| DC1000 | Driver | Linux | arm | 141.28 MB | [:arrow_down: VAGPU-KP-24.01.02.02-DC.tgz](https://qiniu-download-public.daocloud.io/gpu-tools/VAGPU-KP-24.01.02.02-DC/VAGPU-KP-24.01.02.02-DC.tgz) | 2c2c376e6da30972d19f6e5d63a61084 | **2024-03-08** 15:45:31 |

## 2024-02

### GPU-tools-docs-datasets-24.02.07

!!! note "版本说明 20240207"

    GPU 配套工具以及相关文档和数据集。

| 板卡类型 | 软件类型 | OS | 架构 | 文件大小 | 下载 | md5  | 发布时间 |
| :-----: | :-----: | :-----: | :----: | :-----: | :--: | :----: | :-----: |
| DC1000 | Driver | Linux | arm | 234.00 B | [:arrow_down: README.txt](https://qiniu-download-public.daocloud.io/gpu-tools/GPU-tools-docs-datasets-24.02.07/README.txt) | c258740c0a7f700aefd100d7afb5141d | **2024-02-07** 11:00:11 |

**附件下载**

| 文件大小 | 下载 | 发布时间 |
| :-----: | :--: | :----: |
| 10.16 GB | [:arrow_down: 2012img_sv100_DC1000.tar](https://qiniu-download-public.daocloud.io/gpu-tools/GPU-tools-docs-datasets-24.02.07/2012img_sv100_sg100.tar) | 2024-02-18 15:58:51 |
| 5.42 GB | [:arrow_down: dc1000_1.0.0_rc2_kunpeng.tar](https://qiniu-download-public.daocloud.io/gpu-tools/GPU-tools-docs-datasets-24.02.07/dc1000_1.0.0_rc2_kunpeng.tar) | 2024-02-18 15:58:51 |

### FW-release-BL02.3.6R-BMCU1.6R-PMCU1.0R

!!! note "版本说明 20240206"

    版本对应关系：

    - BL0: vastai_bl0_DC1000_2.3.6R-20231122
    - BMCU: vastai_bmcu_VG1x00_1.6R-20231127
    - PMCU: vastai_pmcu_VG1x00_1.0R-20231110

| 板卡类型 | 软件类型 | OS | 架构 | 文件大小 | 下载 | md5  | 发布时间 |
| :-----: | :-----: | :-----: | :----: | :-----: | :--: | :----: | :-----: |
| DC1000 | Driver | Linux | arm | 287.54 KB | [:arrow_down: BL0_BMCU_PMCU-24.02.06.01.tar.gz](https://qiniu-download-public.daocloud.io/gpu-tools/FW-release-BL02.3.6R-BMCU1.6R-PMCU1.0R/BL0_BMCU_PMCU-24.02.06.01.tar.gz) | 83395b33b5411048852e786cd7c7b5d0 | **2024-02-06** 18:19:38 |

### VAGPU-KP-24.01.02.01-DC

!!! note "版本说明"

    VAGPU-KP-24.01.02.01

| 板卡类型 | 软件类型 | OS | 架构 | 文件大小 | 下载 | md5  | 发布时间 |
| :-----: | :-----: | :-----: | :----: | :-----: | :--: | :----: | :-----: |
| DC1000 | Driver | Linux | arm | 139.18 MB | [:arrow_down: VAGPU-KP-24.01.02.01-Android11.tgz](https://qiniu-download-public.daocloud.io/gpu-tools/VAGPU-KP-24.01.02.01-DC/VAGPU-KP-24.01.02.01-Android11.tgz) | 7a032236d6a3846d587cc47eb98d388f | **2024-02-05** 09:53:46 |
