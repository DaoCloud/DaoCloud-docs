# 升级注意事项

本页说明将 hydra 升级到新版本时需要注意的相关事项。

## 从 v0.12.1（或更低版本）升级到 v0.13.1

Hydra-agent 从 0.13.1 版本开始不再内置 dataset 组件，需要单独通过 addon 仓库安装，为保证以前的 dataset CR 在升级之后不会丢失，请参考下述步骤进行升级。

!!! note

    以下升级操作需要在每个子集群都执行一遍。

1. 查看目前安装的hydra-agent以及所有的dataset

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

        推荐使用命令行的形式,可以一键修改，否则每个 CR 都需要改一遍。

    ```bash
    cloudshell-worker-ct8cbvdtb6:~# kubectl annotate datasets.dataset.baizeai.io -A --all helm.sh/resource-policy=keep
    dataset.dataset.baizeai.io/qwen3-0-6b-1 annotated
    ```

4. 开始升级

    !!! note

        Hydra-agent 从 v0.12.1 -> v0.13.1，移除了 dataset 组件。

    ```bash
    helm repo add hydra https://release-ci.daocloud.io/chartrepo/hydra

    helm repo update

    helm upgrade --install hydra-agent hydra/hydra-agent -n hydra-system --version  v0.13-dev-fdbdb95a --debug --set storageserver.volumeSettings.csi.driver=csi.juicefs.com --set storageserver.volumeSettings.csi.volumeHandle=hydra-storageserver-pv  
    ```

5. 验证dataset 

    ```bash
    cloudshell-worker-ct8cbvdtb6:~# kubectl get datasets.dataset.baizeai.io -A
    NAMESPACE      NAME           TYPE          URI                            PHASE
    hydra-system   qwen3-0-6b-1   MODEL_SCOPE   modelscope://Qwen/Qwen3-0.6B   PROCESSING
    ```

6. 安装 dataset helm 应用

    进入工作集群 的 **Helm 应用** -> **Helm 模板** 页面，找到 **dataset** 插件并安装。

7. 此时可以去掉keep的annotation了

    ```bash
    cloudshell-worker-l2vhhlz6f4:~# kubectl annotate crd datasets.dataset.baizeai.io helm.sh/resource-policy-
    customresourcedefinition.apiextensions.k8s.io/datasets.dataset.baizeai.io annotated

    cloudshell-worker-l2vhhlz6f4:~# kubectl annotate datasets.dataset.baizeai.io -A --all helm.sh/resource-policy-
    dataset.dataset.baizeai.io/qwen3-0-6b-1 annotated
    ```

8. 更新 dataset

    为了确保旧的 CRD 的定义和最新的 dataset 保持一致，需要更新 dataset 插件。

    !!! note

        不需要改任何参数，直接更新即可。