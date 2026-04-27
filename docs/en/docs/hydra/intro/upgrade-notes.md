# Upgrade Notes

This page describes important considerations when upgrading Hydra to a new version.

## Upgrading from v0.12.1 (or earlier) to v0.13.1

Starting from v0.13.1, hydra-agent no longer includes the dataset component by default. It must be installed separately via the addon repository. To ensure that existing dataset CRs are not lost after the upgrade, follow the steps below.

!!! note

    The following upgrade steps must be executed on each sub-cluster.

1. Check the currently installed hydra-agent and all datasets

    ```bash
    cloudshell-worker-ct8cbvdtb6:~# helm ls -n hydra-system | grep agent
    hydra-agent     hydra-system    1               2026-03-16 10:02:15.663202599 +0000 UTC deployed        hydra-agent-v0.12.3             v0.12.3           

    cloudshell-worker-ct8cbvdtb6:~# kubectl get datasets.dataset.baizeai.io -A
    NAMESPACE      NAME           TYPE          URI                            PHASE
    hydra-system   qwen3-0-6b-1   MODEL_SCOPE   modelscope://Qwen/Qwen3-0.6B   PROCESSING
    ```

1. Run the following command to modify the CRD (you can also edit the CRD YAML in the UI to add annotations)

    Use Helm’s `resource-policy=keep` to ensure this resource is skipped during upgrade. Also update the dataset CRD release-related fields to avoid errors when installing dataset separately later.

    ```bash
    cloudshell-worker-ct8cbvdtb6:~# kubectl annotate crd datasets.dataset.baizeai.io  \
    meta.helm.sh/release-name=dataset \
    meta.helm.sh/release-namespace=dataset-system \
    helm.sh/resource-policy=keep \
    --overwrite
    customresourcedefinition.apiextensions.k8s.io/datasets.dataset.baizeai.io annotated
    ```

1. Run the following command to modify the CRs

    !!! note

        It is recommended to use the CLI to update all resources at once; otherwise, each CR must be modified individually.

    ```bash
    cloudshell-worker-ct8cbvdtb6:~# kubectl annotate datasets.dataset.baizeai.io -A --all helm.sh/resource-policy=keep
    dataset.dataset.baizeai.io/qwen3-0-6b-1 annotated
    ```

1. Start the upgrade

    !!! note

        hydra-agent removes the dataset component from v0.12.1 to v0.13.1.

    Go to the **Helm Apps** -> **Helm Apps** page in the workload cluster, find the **hydra-agent** plugin, and upgrade it.

1. Verify dataset

    ```bash
    cloudshell-worker-ct8cbvdtb6:~# kubectl get datasets.dataset.baizeai.io -A
    NAMESPACE      NAME           TYPE          URI                            PHASE
    hydra-system   qwen3-0-6b-1   MODEL_SCOPE   modelscope://Qwen/Qwen3-0.6B   PROCESSING
    ```

1. Install the dataset Helm app

    Go to the **Helm Apps** -> **Helm Templates** page in the workload cluster, find the **dataset** plugin, and install it.

1. Remove the `keep` annotations

    ```bash
    cloudshell-worker-l2vhhlz6f4:~# kubectl annotate crd datasets.dataset.baizeai.io helm.sh/resource-policy-
    customresourcedefinition.apiextensions.k8s.io/datasets.dataset.baizeai.io annotated

    cloudshell-worker-l2vhhlz6f4:~# kubectl annotate datasets.dataset.baizeai.io -A --all helm.sh/resource-policy-
    dataset.dataset.baizeai.io/qwen3-0-6b-1 annotated
    ```

1. Update dataset

    To ensure the old CRD definition is consistent with the latest dataset version, update the dataset plugin.

    !!! note

        No parameter changes are required; simply perform the update.
