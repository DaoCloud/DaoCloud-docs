# 安装

本页说明离线和在线安装 ClawOS 的两种安装方式。

## 离线安装

本页说明如何下载 ClawOS 离线包以及如何安装。

### 下载

使用以下链接下载 ClawOS 离线包：

```text
https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/agentclaw_v0.2.0_amd64.tar
```

如果有更新版本，请替换以上 URL 中的 `v0.2.0`。

### 从离线包中加载镜像和 chart 包

!!! info

    前置条件：将离线包上传至目标节点

您可以根据下面两种方式之一加载镜像，当环境中存在镜像仓库时，建议选择 chart-syncer 同步镜像到镜像仓库，该方法更加高效便捷。

#### chart-syncer 同步镜像到镜像仓库

1. 创建 load-image.yaml

    !!! note  

        该 YAML 文件中的各项参数均为必填项。您需要一个私有的镜像仓库，并修改相关配置。

    === "已安装 chart repo"

        若当前环境已安装 chart repo，chart-syncer 也支持将 Chart 导出到指定仓库中。

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: clawos-offline # (1)!
        target:
          containerRegistry: 10.16.10.111 # (2)!
          containerRepository: release.daocloud.io/clawos # (3)!
          repo:
            kind: HARBOR # (4)!
            url: http://10.16.10.111/chartrepo/release.daocloud.io # (5)!
            auth:
              username: "admin" # (6)!
              password: "Harbor12345" # (7)!
          containers:
            auth:
              username: "admin" # (8)!
              password: "Harbor12345" # (9)!
        ```

        1. 到执行 charts-syncer 命令的相对路径，而不是此 YAML 文件和离线包之间的相对路径
        2. 需更改为你的镜像仓库 url
        3. 需更改为你的镜像仓库
        4. 也可以是任何其他支持的 Helm Chart 仓库类别
        5. 需更改为 chart repo url
        6. 你的镜像仓库用户名
        7. 你的镜像仓库密码
        8. 你的镜像仓库用户名
        9. 你的镜像仓库密码

    === "未安装 chart repo"

        若当前环境未安装 chart repo，chart-syncer 也支持将 Chart 导出为 tgz 文件，并存放在指定路径。

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: clawos-offline # (1)!
        target:
          containerRegistry: 10.16.10.111 # (2)!
          containerRepository: release.daocloud.io/clawos # (3)!
          repo:
            kind: LOCAL
            path: ./local-repo # (4)!
          containers:
            auth:
              username: "admin" # (5)!
              password: "Harbor12345" # (6)!
        ```

        1. 到执行 charts-syncer 命令的相对路径，而不是此 YAML 文件和离线包之间的相对路径
        2. 需更改为你的镜像仓库 URL
        3. 需更改为你的镜像仓库
        4. Chart 本地路径
        5. 你的镜像仓库用户名
        6. 你的镜像仓库密码

1. 执行同步镜像命令。

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

#### Docker 或 containerd 直接加载

解压并加载镜像文件。

1. 解压 tar 压缩包。

    ```shell
    tar xvf agentclaw_0.2.0.bundle.tar
    ```

    解压成功后会得到几个文件：

    - hints.yaml: 镜像模版
    - images.tar: 镜像包
    - original-chart: chart 包

2. 从本地加载镜像到 Docker 或 containerd。

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr -n k8s.io image import images.tar
        ```

!!! note

    每个 node 都需要做 Docker 或 containerd 加载镜像操作，
    加载完成后需要 tag 镜像，保持 Registry、Repository 与安装时一致。

### 离线安装步骤

#### 前置条件

1. 安装前请确保目标 Kubernetes 集群已配置必要的依赖服务：

    - hydra-apiserver
    - kpanda-apiserver
    - ghippo-apiserver
    - kpanda-clusterpedia-apiserver

2. 更新 hydra AuthorizationPolicy 允许 agent-claw-system 的流量

    ```shell
    kubectl -n hydra-system edit AuthorizationPolicy hydra-apiserver
    ```

    ```diff
    apiVersion: security.istio.io/v1
    kind: AuthorizationPolicy
    metadata:
      name: hydra-apiserver
      namespace: hydra-system
    spec:
      action: ALLOW
      rules:
      - from:
        - source:
            namespaces:
            - dak-system
    +       - agentclaw-system
    ```

3. 配置 insight-system 的 kube-state-metrics 的启动项（需要给在部署 Agent 的集群添加此配置）

    ```shell
    kubectl -n insight-system edit deployment insight-agent-kube-state-metrics
    ```

    ```diff
    apiVersion: apps/v1
    kind: Deployment
    metadata:
       name: insight-agent-kube-state-metrics
       namespace: insight-system
    spec:
       template:
          spec:
             containers:
             - name: kube-state-metrics
               args:
              args:
                - --metric-labels-allowlist=nodes=[feature.node.kubernetes.io/cpu-cpuid.HYPERVISOR]
                - '--port=8080'
                - --resources=configmaps,cronjobs,daemonsets,deployments,horizontalpodautoscalers,jobs,limitranges,namespaces,networkpolicies,nodes,persistentvolumeclaims,persistentvolumes,pods,replicasets,replicationcontrollers,resourcequotas,secrets,services,statefulsets,storageclasses
    +           - --metric-annotations-allowlist=deployments=[agentclaw.io/instance-name,agentclaw.io/workspace-id]
    ```

#### 通过 Kpanda UI 安装

在 chart-syncer 成功同步镜像和 chart 后可以直接在 Kpanda **Helm 应用** 中先更新离线仓库，然后找到
chart agentclaw 并开始安装, 安装时不需要更改任何参数。

#### 通过 Helm 安装

1. 添加 Helm 仓库

    ```bash
    helm repo add agentclaw-release https://release.daocloud.io/chartrepo/clawos
    helm repo update
    ```

2. 安装 Chart

    ```bash
    helm upgrade agentclaw agentclaw-release -n agentclaw-system --install --create-namespace
    ```

## 在线安装

!!! info

    在线安装的前置条件与[离线安装](#_4)一样。

### 通过 Kpanda UI 安装

先在 **Helm 应用** -> **Helm 仓库** 中添加 `agentclaw-release` 仓库：
`https://release.daocloud.io/chartrepo/agentclaw`,
然后到 **Helm 模板** 中找到 `agentclaw` chart 并点击 **安装** ，安装时不需要更改任何参数。

### 通过 Helm 安装

1. 添加仓库

    ```bash
    helm repo add agentclaw-release 
    helm repo update
    ```

2. 安装 Chart

    ```bash
    helm upgrade agentclaw agentclaw-release -n agentclaw-system --install --create-namespace
    ```
