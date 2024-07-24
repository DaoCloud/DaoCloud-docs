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
