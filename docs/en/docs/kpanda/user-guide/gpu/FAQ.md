---
hide:
  - toc
---

# GPU FAQs

## GPU processes are not visible while running nvidia-smi inside a pod

Q: When running the `nvidia-smi` command inside a GPU-utilizing pod,
no GPU process information is visible in the full-card mode and vGPU mode.

A: Due to `PID namespace` isolation, GPU processes are not visible inside the Pod.
To view GPU processes, you can use one of the following methods:

- Configure the workload using the GPU with `hostPID: true` to enable viewing PIDs on the host.
- Run the `nvidia-smi` command in the driver pod of the gpu-operator to view processes.
- Run the `chroot /run/nvidia/driver nvidia-smi` command on the host to view processes.
