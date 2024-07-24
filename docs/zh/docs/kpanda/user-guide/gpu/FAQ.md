# GPU 相关FAQ

## POD 内 nvidia-smi 看不到 GPU 进程

Q: 在使用 `GPU` 的 `Pod` 内执行 `nvidia-smi` 命令不能查看到使用 `GPU` 的进程信息，包括整卡模式、`vGPU` 模式等。

A: 因为有 `PID namespace` 隔离，导致在 `POD` 内查看不到 `GPU` 进程，如果要查看 `GPU` 进程有如下三个方法。

1. 给使用 `GPU` 的工作负载配置上 `hostPID: true`，使其可以查看到宿主机上的 `PID`.
2. 在 `gpu-operator` 的 `driver pod` 中可以执行 `nvidia-smi` 查看进程。
3. 在宿主机上执行 `chroot /run/nvidia/driver nvidia-smi` 可以查看进程。