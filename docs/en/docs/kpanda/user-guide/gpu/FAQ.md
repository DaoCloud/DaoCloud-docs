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

## Updating Historical Workload GPU Type Causes Pod Scheduling Failure

Q: In a cluster with only physical-card mode nodes, I created a workload using that GPU type, scaled replicas to 0, switched all cluster nodes to vGPU mode, and then updated the workload to use vGPU. Why did the Pod show scheduling failure, and why does the Pod spec contain both GPU limit types?

```yaml
resources:
  limits:
    cpu: 250m
    memory: 512Mi
    nvidia.com/gpu: '1'  # Historical GPU type
    nvidia.com/gpucores: '5'
    nvidia.com/gpumem: 100k
    nvidia.com/vgpu: '1'
```

A: When switching the GPU mode of cluster nodes, the platform will check if there are Pods with different GPU modes on the nodes. Scaling the replica of this workload to 0 avoids this situation. When updating the workload, the frontend clears non-user-selected GPU types from the Pod based on the GPU types existing in the cluster. Since the historical GPU type no longer exists in the cluster, this problem occurred.

Solution:
- Manually delete the historical GPU type labels in the workload's `resources.limit`.
