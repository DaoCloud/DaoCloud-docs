# 应用使用 vGPU 资源

本节介绍如何在 `DCE5.0` 平台使用 `vGPU` 能力。

## 前提条件

- 当前集群已通过 Operator 或手动方式部署，具体参考 [Nvidia 驱动部署](driver.md)
- 当前集群已安装 [vGPU Addon 安装](vgpu addon.md)

## 操作步骤
1. **确认集群是否已检测 GPU 卡**。点击对应`集群`-->`集群设置`-->`Addon 插件`，查看是否已自动启用并自动检测对应 GPU 类型。目前集群会自动启用 `GPU`， 并且设置 `GPU` 类型为 `Nvidia vGPU`。![Alt text](./images/vgpu-cluster.png)

2. 部署工作负载，点击对应`集群`-->`工作负载`，通过镜像方式部署工作负载，选择类型（Nvidia vGPU）之后，会自动出现如下几个参数需要填写：

- **物理卡数量（nvidia.com/vgpu）**：表示当前POD需要挂载几张物理卡，并且要 小于等于 宿主机上的卡数量。
- **GPU算力（nvidia.com/gpucores）**: 表示每张卡占用的 GPU 算力，值范围为 0-100；如果配置为 0， 则认为不强制隔离；配置为100，则认为独占整张卡。
- **GPU显存（nvidia.com/gpumem）**: 表示每张卡占用的 GPU 显存，值单位为 MB，最小值为1，最大值为整卡的显存值。

> 如果上述值配置的有问题则会出现调度失败，资源分配不了的情况。

如果使用自定义 `Yaml` 部署工作负载请使用如上文字后对应的资源 `Key`。![Alt text](./images/vgpu-deployment.png)

