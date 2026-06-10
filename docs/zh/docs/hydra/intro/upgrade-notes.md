# 升级注意事项

本页说明将 hydra 升级到新版本时需要注意的相关事项。

## 从 v0.14.1（或更低版本）升级到 v0.15.0

hydra 从 0.15.0 版本开始，在 knoway 网关中集成了 higress，以提供 AI 安全、token 限额等能力，升级时需要注意以下事项：

1. 默认 higress 是禁用的，需要在 hydra-agent 的 helm value 中配置开启：

   ``` yaml
    knoway:
      higress:
        enabled: true
   ```

2. 0.15.0 版本，全局服务集群安装的 hydra 和子集群的 hydra-agent 版本是绑定的，升级全局集群的 hydra 或者子集群中的 hydra-agent 的任意组件，都必须同步升级。否则会影响用量上报和计费功能。

3. 在启用了 higress 后，默认内置了产品必须的 wasm plugin CR，因此需要首先在安装 hydra-agent 的集群中手动 apply CRD，否则会导致 hydra-agent 安装失败，apply 步骤如下（在对应的子集群中执行）：

   ```bash
   helm repo add hydra https://release.daocloud.io/chartrepo/hydra
   helm repo update hydra
   helm pull hydra/hydra-agent --version v0.15.0 --untar
   kubectl apply -f hydra-agent/crds/
   ```

## 从 v0.12.1（或更低版本）升级到 v0.13.1

Hydra-agent 从 0.13.1 版本开始不再内置 dataset 组件，需要单独通过 addon 仓库安装，为保证以前的 dataset CR 在升级之后不会丢失，请参考下述步骤进行升级。

!!! note

```
以下升级操作需要在每个子集群都执行一遍。
```

1. 查看目前安装的 hydra-agent 以及所有的 dataset
   ```bash
   cloudshell-worker-ct8cbvdtb6:~# helm ls -n hydra-system | grep agent
   hydra-agent     hydra-system    1               2026-03-16 10:02:15.663202599 +0000 UTC deployed        hydra-agent-v0.12.3             v0.12.3           


   cloudshell-worker-ct8cbvdtb6:~# kubectl get datasets.dataset.baizeai.io -A
   NAMESPACE      NAME           TYPE          URI                            PHASE
   hydra-system   qwen3-0-6b-1   MODEL_SCOPE   modelscope://Qwen/Qwen3-0.6B   PROCESSING
   ```
2. 执行以下命令修改 CRD，也可以在界面上编辑 CRD 的 yaml 添加 annotation 实现

   通过 helm 的机制 resource-policy=keep 使得 helm 升级的时候跳过此资源，同时修改 dataset 这个 CRD 的 release 相关字段，确保后续单独安装 dataset 不报错。
   ```bash
   cloudshell-worker-ct8cbvdtb6:~# kubectl annotate crd datasets.dataset.baizeai.io  \
   meta.helm.sh/release-name=dataset \
   meta.helm.sh/release-namespace=dataset-system \
   helm.sh/resource-policy=keep \
   --overwrite
   customresourcedefinition.apiextensions.k8s.io/datasets.dataset.baizeai.io annotated
   ```
3. 执行以下命令修改 CR

   !!! note
   ```
    推荐使用命令行的形式,可以一键修改，否则每个 CR 都需要改一遍。
   ```
   ```bash
   cloudshell-worker-ct8cbvdtb6:~# kubectl annotate datasets.dataset.baizeai.io -A --all helm.sh/resource-policy=keep
   dataset.dataset.baizeai.io/qwen3-0-6b-1 annotated
   ```
4. 开始升级

   !!! note
   ```
    Hydra-agent 从 v0.12.1 -> v0.13.1，移除了 dataset 组件。
   ```
   进入工作集群 的 **Helm 应用** -> **Helm 应用** 页面，找到 **hydra-agent** 插件并更新。
5. 验证 dataset
   ```bash
   cloudshell-worker-ct8cbvdtb6:~# kubectl get datasets.dataset.baizeai.io -A
   NAMESPACE      NAME           TYPE          URI                            PHASE
   hydra-system   qwen3-0-6b-1   MODEL_SCOPE   modelscope://Qwen/Qwen3-0.6B   PROCESSING
   ```
6. 安装 dataset helm 应用

   进入工作集群 的 **Helm 应用** -> **Helm 模板** 页面，找到 **dataset** 插件并安装。
7. 此时可以去掉 keep 的 annotation 了
   ```bash
   cloudshell-worker-l2vhhlz6f4:~# kubectl annotate crd datasets.dataset.baizeai.io helm.sh/resource-policy-
   customresourcedefinition.apiextensions.k8s.io/datasets.dataset.baizeai.io annotated

   cloudshell-worker-l2vhhlz6f4:~# kubectl annotate datasets.dataset.baizeai.io -A --all helm.sh/resource-policy-
   dataset.dataset.baizeai.io/qwen3-0-6b-1 annotated
   ```
8. 更新 dataset

   为了确保旧的 CRD 的定义和最新的 dataset 保持一致，需要更新 dataset 插件。

   !!! note
   ```
    不需要改任何参数，直接更新即可。
   ```

