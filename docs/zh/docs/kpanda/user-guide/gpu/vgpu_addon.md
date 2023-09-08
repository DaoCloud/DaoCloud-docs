# vGPU Addon 安装

本节介绍如何在 `DCE5.0` 平台使用 `vGPU` 能力。

## 前提条件

- 确认集群节点上具有对应型号的 GPU 卡（[NVIDIA H100](https://www.nvidia.com/en-us/data-center/h100/)、
  [A100](https://www.nvidia.com/en-us/data-center/a100/) 和
  [A30](https://www.nvidia.com/en-us/data-center/products/a30-gpu/) Tensor Core GPU）
- 当前集群已通过 Operator 或手动方式部署，具体参考 [Nvidia 驱动部署](driver.md)

## 操作步骤

1. 功能模块路径：容器管理 => 集群管理 => 点击目标集群 => Helm应用 => Helm 仓库 => 搜索 nvidia-vgpu。![Alt text](./images/vgpu-addon.png)

2.  在安装 vGPU 的过程中提供了几个基本修改的参数，如果需要修改高级参数点击 YAML 列进行修改：

   - `deviceMemoryScaling`：浮点数类型，预设值是1。NVIDIA装置显存使用比例，可以大于1（启用虚拟显存，实验功能）。对于有*M*显存大小的NVIDIA GPU，如果我们配置`devicePlugin.deviceMemoryScaling`参数为*S*，在部署了我们装置插件的Kubenetes集群中，这张GPU分出的vGPU将总共包含 `S * M` 显存。

   - `deviceSplitCount`:
     整数类型，预设值是10。GPU的分割数，每一张GPU都不能分配超过其配置数目的任务。若其配置为N的话，每个GPU上最多可以同时存在N个任务。

   - `Resources`：就是对应 vgpu-device-plugin 和 vgpu-schedule pod 的资源使用量。

     ![Alt text](./images/vgpu-pararm.png)

3. 安装成功之后会在指定 `Namespace` 下出现如下两个类型的 `Pod`，即表示 Nvidia GPU 插件已安装成功：![Alt text](./images/vgpu-pod.png)



