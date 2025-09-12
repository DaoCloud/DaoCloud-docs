# HAMi 企业版安装和配置指南

本文介绍如何在 DCE 5.0 平台上安装和配置 HAMi（异构 AI 计算虚拟化中间件）企业版，实现 GPU 虚拟化功能。

!!! note

    本文适用于已部署 DCE 5.0 平台的企业用户，需要启用 GPU 虚拟化功能以支持多容器共享 GPU 资源。
    HAMi 企业版提供更强大的 GPU 资源管理和虚拟化能力，详细信息请参考 [HAMi 项目官网](https://project-hami.io)。

## 前提条件

在开始安装 HAMi 企业版之前，请确保满足以下条件：

### 系统要求

- 已成功部署 DCE 5.0 平台
- Kubernetes 集群版本 1.20 或更高
- 集群中至少有一个配置了 GPU 的节点 （本文以 NVIDIA GPU 卡为例）
- 具有集群管理员权限

### GPU 硬件要求

- 推荐 NVIDIA GPU 卡（支持 CUDA），参阅 [HAMi 企业版支持的 GPU 类型](https://project-hami.io/docs/userguide/Device-supported)。
- GPU 驱动程序已正确安装
- 支持 GPU 虚拟化的硬件架构

!!! warning

    在开始安装之前，请确保已备份重要数据，并在测试环境中验证安装过程。

## 获取 GPU UUID

在安装 HAMi 企业版之前，需要获取 GPU 设备的 UUID 用于许可证申请。根据您的环境配置，可以选择以下两种方法之一。

### 方法一：宿主机直接获取（推荐）

如果 GPU 驱动程序直接安装在宿主机上，可以使用以下命令获取 GPU UUID：

```bash
# 列出所有 GPU 设备及其 UUID
nvidia-smi -L
```

预期输出示例：

```console
GPU 0: NVIDIA H800 (UUID: GPU-12345678-1234-1234-1234-123456789abc)
GPU 1: NVIDIA H800 (UUID: GPU-87654321-4321-4321-4321-cba987654321)
```

从输出中提取 UUID 信息：

```bash
# 仅显示 UUID
nvidia-smi -L | grep -oP 'UUID: \K[^)]*'
```

预期输出：

```console
GPU-12345678-1234-1234-1234-123456789abc
GPU-87654321-4321-4321-4321-cba987654321
```

### 方法二：容器内获取

如果 GPU 驱动程序不是直接安装在宿主机上，需要将 GPU 设备挂载到容器中获取 UUID：

```bash
# 创建临时容器并挂载 GPU 设备
docker run --rm --gpus all nvidia/cuda:11.8-base-ubuntu20.04 nvidia-smi -L
```

或者使用 Kubernetes Pod 的方式：

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: gpu-uuid-checker
spec:
  containers:
    - name: cuda
      image: nvidia/cuda:11.8-base-ubuntu20.04
      command: ["nvidia-smi", "-L"]
      resources:
        limits:
          nvidia.com/gpu: 1
  restartPolicy: Never
```

应用 Pod 配置并查看输出：

```bash
# 创建 Pod
kubectl apply -f gpu-uuid-checker.yaml

# 查看 Pod 日志获取 UUID
kubectl logs gpu-uuid-checker

# 清理临时 Pod
kubectl delete pod gpu-uuid-checker
```

!!! tip

    建议记录所有 GPU 设备的 UUID，这些信息将用于后续的许可证申请和配置过程。
    如果您有多个 GPU 节点，需要分别在每个节点上执行上述操作。

## 许可证申请和管理

HAMi 企业版需要有效的许可证才能正常运行。本节介绍如何申请和管理许可证。

### 申请企业版许可证

1. **准备 GPU UUID 信息**

   使用上一节获取的 GPU UUID 信息，准备许可证申请所需的设备清单。

2. **联系 HAMi 技术支持**

   通过以下方式申请企业版许可证：

   - 访问 [HAMi 项目官网](https://project-hami.io) 获取联系方式
   - 提供 GPU UUID 列表和使用场景描述
   - 说明预期的 GPU 虚拟化需求

### 许可证文件部署

HAMi 企业版的许可证已内置到镜像中，对于基本安装无需额外配置。如果需要为其他 GPU 设备添加许可证，请按以下步骤操作：

1. **找到许可证目录**

    在每个 GPU 节点上找到许可证存储目录：

    ```bash
    # 在 GPU 节点上执行
    sudo mkdir -p /usr/local/vgpu
    ```

2. **部署许可证文件**

    将获取的许可证文件复制到指定目录：

    ```bash
    # 复制主许可证文件
    sudo cp <license> /usr/local/vgpu/

    # 复制设备特定的许可证文件（一个许可证可包含申请的一个或多个设备）
    sudo cp GPU-12345678-1234-1234-1234-123456789abc.lic /usr/local/vgpu/
    ```

## 安装 HAMi 企业版

本节介绍如何移除现有的 GPU 操作器并安装 HAMi 企业版。

### 移除现有的 nvidia-vgpu Operator

在安装 HAMi 企业版之前，需要先移除集群中现有的 nvidia-vgpu Operator 以避免冲突。

检查现有 Operator，如果有请根据合理的方式进行卸载。

```bash
# 查看现有的 GPU 相关操作器
kubectl get pods -A | grep -i nvidia
kubectl get pods -A | grep -i vgpu
```

### 准备 HAMi 企业版安装包

!!! note

    HAMi 企业版可支持多种安装方式。本文以镜像为主，如有其他需要可联系交付人员获取支持。

1. **获取安装包**

    确保您已获得 `hami_commercial.tar` 安装包文件。

2. **解压安装包**

    ```bash
    # 解压 HAMi 企业版安装包
    tar -xvf hami_commercial.tar
    ```

### 部署 HAMi 企业版

使用 Helm 命令部署 HAMi 企业版：

使用 `helm upgrade` 命令更新安装包；注意修改 `values.yaml`配置：

- 将 `resourceName` 从 `nvidia.com/gpu` 改为 `nvidia.com/vgpu`
- 修改 `Chart` 中需要的镜像和版本，主要涉及：
    - /projecthami/jettech/kube-webhook-certgen
    - /projecthami/kube-webhook-certgen
    - /projecthami/hami:vX.Y.Z-commercial

```bash
helm upgrade --install hami-commercial ./ \
  -n hami-commercial \
  --create-namespace \
  -f ./values.yaml
```

部署过程中的预期输出：

```console
Release "hami-commercial" does not exist. Installing it now.
NAME: hami-commercial
LAST DEPLOYED: Mon Jan 15 10:30:00 2024
NAMESPACE: hami-commercial
STATUS: deployed
REVISION: 1
TEST SUITE: None
```

### 验证部署状态

1. **检查 Pod 状态**

    ```bash
    # 查看 HAMi 企业版相关 Pod 状态
    kubectl -n hami-commercial get pod
    ```

    预期输出示例：

    ```console
    NAME                                READY   STATUS    RESTARTS   AGE
    hami-device-plugin-daemonset-xxxxx  1/1     Running   0          2m
    hami-scheduler-xxxxx                1/1     Running   0          2m
    hami-webhook-xxxxx                  1/1     Running   0          2m
    ```

!!! note

    部署完成后，HAMi 企业版将自动开始管理集群中的 GPU 资源。
    原有的 `nvidia.com/gpu` 资源将被转换为 `nvidia.com/vgpu` 资源。

## 切换节点 GPU 模式

HAMi 企业版部署完成后，需要进行一些后续配置以确保系统正常运行。

### 在容器管理界面切换 GPU 模式

1. **登录 DCE 5.0 管理界面**

    使用管理员账户登录 DCE 5.0 平台的 Web 管理界面。

2. **进入容器管理模块**

    导航到 **容器管理** → **集群列表** → 选择目标集群。

3. **切换 GPU 模式**

    在集群详情页面中：

    - 找到 **节点管理** 选项
    - 选择包含 GPU 的节点
    - 在节点详情中找到 **GPU 配置** 选项
    - 将 GPU 模式从 `GPU` 切换为 `vGPU`
    - 保存配置更改

4. **确认模式切换**

    切换完成后，可以在节点详情页面确认 GPU 模式已更改为 `vGPU`。

### 验证系统配置

1. **检查 GPU 资源**

    验证 GPU 资源已正确转换为 vGPU 资源：

    ```bash
    # 查看节点的 GPU 资源
    kubectl describe nodes | grep -A 5 -B 5 "nvidia.com/vgpu"
    ```

    预期输出应显示 `nvidia.com/vgpu` 资源而不是 `nvidia.com/gpu`。

2. **验证设备插件状态**

    ```bash
    # 检查设备插件是否正常运行
    kubectl -n hami-commercial get pods -l app=hami-device-plugin
    ```

3. **查看系统事件**

    ```bash
    # 查看相关的系统事件
    kubectl get events -n hami-commercial --sort-by='.lastTimestamp'
    ```

## 验证和测试

完成 HAMi 企业版安装后，可创建测试应用程序来验证 GPU 虚拟化功能是否正常工作。

### 创建 vGPU 测试应用

1. **创建测试应用配置文件**

    创建一个使用 vGPU 资源的测试应用：

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: vgpu-test-app
      namespace: default
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: vgpu-test-app
      template:
        metadata:
          labels:
            app: vgpu-test-app
        spec:
          containers:
            - name: pytorch-container
              image: release.daocloud.io/zestu/pytorch:2.5.1-cuda12.4-cudnn9-runtime
              command: ["sleep", "3600"]
              resources:
                limits:
                  nvidia.com/vgpu: 1 # 申请 1 个 vGPU
                  nvidia.com/gpumem: 4096 # 申请 4GB GPU 内存
                  nvidia.com/gpucores: 50 # 申请 50% GPU 算力
                requests:
                  nvidia.com/vgpu: 1
                  nvidia.com/gpumem: 4096
                  nvidia.com/gpucores: 50
          nodeSelector:
            gpu: "on"
    ```

2. **部署测试应用**

    ```bash
    # 应用测试配置
    kubectl apply -f vgpu-test-app.yaml
    ```

### GPU 资源分配验证

1. **进入测试容器**

    ```bash
    # 进入测试容器
    kubectl exec -it deployment/vgpu-test-app -- bash
    ```

2. **检查 GPU 可见性**

    在容器内执行以下命令：

    ```bash
    # 检查 CUDA 设备
    nvidia-smi

    # 检查 GPU 内存限制
    nvidia-smi --query-gpu=memory.total,memory.used,memory.free --format=csv
    ```

    预期输出应显示分配的 4GB GPU 内存限制。

3. **验证 GPU 算力限制**

    ```bash
    # 检查 GPU 利用率限制
    nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits
    ```

### GPU 内存验证

为了更详细地验证 GPU 内存分配和使用情况，可以使用以下 Python 脚本进行测试。

#### 创建验证脚本

创建一个名为 `use_3gb_gpu_for_5min.py` 的 Python 脚本：

```python
#!/usr/bin/env python3
"""
HAMi 企业版 GPU 内存验证脚本
此脚本用于验证 vGPU 环境中的 GPU 内存分配和使用情况
"""
import torch
import time

def use_3_5gb_gpu_for_5min():
    print("CUDA available:", torch.cuda.is_available())
    print("CUDA device count:", torch.cuda.device_count())

    for i in range(torch.cuda.device_count()):
        print(f"Allocating memory on GPU {i}...")
        device = torch.device(f"cuda:{i}")
        # 获取当前 GPU 的显存大小
        total_memory = torch.cuda.get_device_properties(device).total_memory
        print(f"Total memory on GPU {i}: {total_memory / (1024 ** 3):.2f} GB")

        # 设置目标显存占用量为 3.5GB
        target_memory = 3.5 * (1024 ** 3)  # 3.5GB
        print(f"Target memory to allocate: {target_memory / (1024 ** 3):.2f} GB")

        allocated_memory = 0
        tensors = []
        while allocated_memory < target_memory:
            tensor = torch.empty(1024, 1024, device=device)
            allocated_memory += tensor.storage().nbytes()
            tensors.append(tensor)
            print(f"Allocated {allocated_memory / (1024 ** 3):.2f} GB on GPU {i}")

        print(f"GPU {i} is now filled with approximately 3.5GB of tensors.")

        # 设置运行时间为 5 分钟
        run_time = 5 * 60  # 5 分钟
        print(f"Running for {run_time / 60:.2f} minutes...")
        start_time = time.time()

        while time.time() - start_time < run_time:
            # 在这里可以添加一些简单的计算任务，以保持 GPU 活跃
            torch.cuda.synchronize(device)
            time.sleep(1)  # 每秒同步一次，避免过度占用 CPU

        print(f"Finished running for {run_time / 60:.2f} minutes.")
        print(f"Releasing memory on GPU {i}...")
        del tensors
        torch.cuda.empty_cache()
        print(f"Memory released on GPU {i}.")

if __name__ == "__main__":
    use_3_5gb_gpu_for_5min()
```

## 下一步

HAMi 企业版安装完成后，您可以：

- 在生产环境中部署需要 GPU 资源的应用程序
- 配置更复杂的 GPU 资源分配策略
- 监控 GPU 资源使用情况和性能指标
- 根据业务需求扩展 GPU 节点规模

!!! success

    恭喜！您已成功完成 HAMi 企业版的安装和配置。
    现在可以充分利用 GPU 虚拟化功能，提高 GPU 资源的利用率和管理效率。

## 相关参考

- [HAMi 项目官网](https://project-hami.io) - HAMi 项目的官方网站和文档
- [HAMi GitHub 仓库](https://github.com/Project-HAMi/HAMi) - 源代码和问题反馈
- [DCE 5.0 容器管理文档](../user-guide/clusters/create-cluster.md) - DCE 5.0 集群创建和管理指南
