# 为 Notebook 定制开发环境镜像

**Notebook** 提供了一套功能强大的在线开发环境。为了满足不同算法模型对特定依赖（如不同版本的 CUDA 等）的需求，平台内置的标准化 **Notebook** 环境可能无法覆盖所有场景。

基于 **AI Lab** 提供的基础镜像，通过构建、推送并注册一个包含自定义开发环境的 **Notebook** 镜像，从而使用户在创建 **Notebook** 实例时，能够灵活选择所需的环境。

*[Baize]: AI Lab 组件的开发代号

## 前置条件

在开始操作前，请确保您已具备以下条件：

*   **权限要求**
    *   拥有目标 Kubernetes 集群的 `kubectl` 管理权限，能够访问并编辑 `baize-system` 命名空间下的资源。
    *   拥有一个可用的内部镜像仓库（如 Harbor），并具备向该仓库推送镜像的权限。
*   **工具要求**
    *   本地或服务器上已安装 `docker` 或 `podman` 等容器构建工具。
    *   本地已配置好 `kubectl` 命令行工具并连接到目标集群。


## 操作步骤

整个过程分为四个核心步骤：获取基础镜像、定制开发环境、注册新镜像、使用新环境。

### 1. 获取当前版本的基础 Notebook 镜像

首先，我们需要找到当前 **AI Lab** 版本所依赖的基础 **Notebook** 镜像地址。这个地址将作为我们定制镜像的 `FROM` 指令。

!!! note

    **AI Lab** 基础 **Notebook** 镜像内置了丰富的开发与交互工具，为您提供了坚实的基础环境。主要包括：

    *   **开发工具**：`jupyter` 和 `vscode`
    *   **平台交互**：`baizectl` (AI Lab 命令行交互工具)
    *   **数据集工具**：`data-loader` (AI Lab 数据集工具)

1.  通过 SSH 登录到 Kubernetes 集群的管理节点（例如火种节点）。

2.  执行以下命令，查看已安装的 **AI Lab** Chart 版本。这将帮助我们定位对应版本的镜像。

    ```bash
    helm list -n baize-system | grep baize
    ```

    您将看到类似如下的输出，请记下 `APP VERSION` 列的版本号（例如 `v0.19.1`）。

    ```text
    NAME    NAMESPACE     REVISION   UPDATED                                  STATUS     CHART           APP VERSION
    baize   baize-system  5          2025-08-18 11:39:12.328965189 +0800 CST  deployed   baize-v0.19.1   v0.19.1
    ```

3.  执行以下命令，从 **AI Lab** 的 `ConfigMap` 中查找并复制 `notebook` 镜像的完整地址。

    ```bash
    kubectl get cm baize -n baize-system -o yaml
    ```

4.  在输出的 YAML 内容中，找到 `notebook_images` 或类似字段，定位到与您版本号匹配的镜像地址。例如：`192.168.157.30/release.daocloud.io/baize/baize-notebook:v0.19.1`。请复制此地址备用。如下图所示：
    ![查看 YAML](./images/custom-image-01.png)
   

### 2. 定制 Notebook 开发环境 (构建 Dockerfile)
接下来，我们将创建一个 `Dockerfile` 文件，以步骤一中获取的基础镜像为源，安装您需要的额外依赖。

1.  在您的工作目录下，创建一个名为 `Dockerfile` 的文件。本示例演示如何安装特定 CUDA 版本的 PyTorch。

    ```dockerfile
    # 使用从步骤一获取的基础镜像地址
    FROM 192.168.157.30/release.daocloud.io/baize/baize-notebook:v0.19.1

    # 安装您需要的依赖，例如支持 CUDA 11.8 的 PyTorch
    # 建议指定国内或内部的 pip 源以加速下载
    RUN pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118
    ```

2.  使用 `docker` 或 `podman` 构建并推送您的定制镜像。请将镜像地址替换为您的内部镜像仓库地址，并为其设定一个清晰可辨的标签。

    ```bash
    # 定义新镜像的完整名称和标签
    export CUSTOM_IMAGE_NAME="<your-registry-address>/baize/baize-notebook:v0.19.1-cuda11.8-torch2.0.1"

    # 构建镜像
    podman build -t ${CUSTOM_IMAGE_NAME} -f Dockerfile .

    # 推送镜像到您的仓库
    podman push ${CUSTOM_IMAGE_NAME}
    ```

### 3. 向 AI Lab 注册新的 Notebook 镜像

镜像推送到仓库后，我们需要修改 **AI Lab** 的配置，让平台“知道”这个新环境的存在。

1.  执行以下命令，进入 **baize** `ConfigMap` 的编辑模式。

    ```bash
    kubectl edit cm baize -n baize-system
    ```

2.  在打开的编辑器中，找到 `data.config.yaml` 下的 `notebook_images` 列表。在列表中添加一个新的条目，指向推送的定制镜像。

    ```yaml
    # ... (已有配置)
    data:
      config.yaml: |-
        ...
        notebook_images:
          # - name: ... (已有的内置镜像)
          # - name: ... (已有的内置镜像)
          - name: <your-registry-address>/baize/baize-notebook:v0.19.1-cuda11.8-torch2.0.1
            type: JUPYTER
        ...
    # ... (其他配置)
    ```

    *   `name`: 镜像的完整地址。
    *   `type`: 指定镜像在 UI 中的分类。如果主要用于 Jupyter，请设置为type： `JUPYTER`。


4.  保存并退出编辑器。此操作会即时更新`kubectl` 集群中的配置信息。

5.  为了让正在运行的 **AI Lab** 服务加载并应用最新的配置，需要手动重启相关服务。请依次执行以下命令：

    ```bash
    # 重启 baize-apiserver
    kubectl rollout restart deployment baize-apiserver -n baize-system

    # 重启 baize-notebook-ssh
    kubectl rollout restart deployment baize-notebook-ssh -n baize-system
    ```

### 4. 在 AI Lab UI 中使用新的 Notebook 环境

完成以上所有步骤后，您的新环境就已经准备就绪了。

1.  登录平台。
2.  导航至创建 **Notebook** 实例的功能页面。
3.  在选择“镜像版本”或类似下拉菜单中，您现在应该能看到刚刚添加的自定义镜像选项（例如 `...:v0.19.1-cuda11.8-torch2.0.1`）。

    ![查看自定义镜像的选项](./images/custom-image-02.png)

4.  选择该镜像，并根据需要配置其他资源（如 CPU, GPU, 内存等），然后创建实例。

启动后的 **Notebook** 实例将具备您在 `Dockerfile` 中定义的所有开发环境。


## 验证

要验证新环境是否成功配置，您可以在新创建的 **Notebook** 实例的终端或代码单元格中，执行命令来检查您所安装库的版本。例如，对于本指南中安装的 PyTorch：

```python
import torch

print(torch.__version__)
print(torch.cuda.is_available())
```

如果输出了正确的版本号以及 `True`，则证明您的自定义环境已成功生效。