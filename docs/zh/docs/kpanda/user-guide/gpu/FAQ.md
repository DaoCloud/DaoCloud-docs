---
hide:
  - toc
---

# GPU 相关 FAQ

## Pod 内 nvidia-smi 看不到 GPU 进程

Q: 在使用 GPU 的 Pod 内执行 `nvidia-smi` 命令看不到使用 GPU 的进程信息，包括整卡模式、vGPU 模式等。

A: 因为有 `PID namespace` 隔离，导致在 Pod 内查看不到 GPU 进程，如果要查看 GPU 进程有如下几种方法：

- 在使用 GPU 的工作负载配置 `hostPID: true`，使其可以查看到宿主机上的 PID
- 在 gpu-operator 的 driver Pod 中执行 `nvidia-smi` 命令查看进程
- 在宿主机上执行 `chroot /run/nvidia/driver nvidia-smi` 命令查看进程

## 更新历史工作负载的GPU type导致Pod调度失败

Q: 在集群中只有整卡模式的节点时，创建一个该GPU类型工作负载，副本缩为0，集群所有节点模式切换为vGPU模式，更新该工作负载使其使用vGPU，为什么Pod显示调度失败，并且Pod spec中含有两个类型的GPU limit信息？

```yaml
resources:
  limits:
    cpu: 250m
    memory: 512Mi
    nvidia.com/gpu: '1'  # 历史GPU type
    nvidia.com/gpucores: '5'
    nvidia.com/gpumem: 100k
    nvidia.com/vgpu: '1'
```

A: 当集群节点GPU模式切换时，平台会检测节点上是否存在不同GPU模式的Pod，副本缩为0规避了此情形。当更新负载时，前端此处根据集群中存在的GPU type抹除Pod中非用户选择的GPU type。因集群中已不存在历史GPU type，发生了此问题。

解决方法：
- 手动删除工作负载的`resources.limit`中的历史GPU type的标签即可。