# Installation

## Offline Installation

This page describes how to download the ClawOS offline package and install it.

### Download

Download the ClawOS offline package using the following link:

```text
https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/agentclaw_v0.2.0_amd64.tar
```

If a newer version is released, replace `v0.2.0` accordingly.


!!! info

    If you need the armd64 version, please use the link:
    https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/agentclaw_v0.2.0_arm64.tar


### Load Images and Chart Packages from the Offline Bundle

!!! info

    Prerequisite: Upload the offline package to the target node.

You can load images using one of the following two methods.
If a container registry is available in your environment, it is recommended to use **chart-syncer** to sync images to the registry, as it is more efficient and convenient.

#### Sync Images to a Container Registry Using chart-syncer

1. Create `load-image.yaml`

    !!! note

        All parameters in this YAML file are required. You must have a private container registry and update the configuration accordingly.

    === "Chart repo installed"

        If a chart repository is already installed, chart-syncer can also export Charts to the specified repository.

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

        1. Relative path from where `charts-syncer` is executed, not relative to this YAML file
        2. Replace with your container registry URL
        3. Replace with your container repository
        4. Can be any supported Helm Chart repository type
        5. Replace with your chart repo URL
        6. Your registry username
        7. Your registry password
        8. Your registry username
        9. Your registry password

    === "Chart repo not installed"

        If a chart repository is not installed, chart-syncer can export Charts as `.tgz` files to a local path.

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

        1. Relative path from where `charts-syncer` is executed, not relative to this YAML file
        2. Replace with your container registry URL
        3. Replace with your container repository
        4. Local chart output path
        5. Your registry username
        6. Your registry password

1. Run the sync command:

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

#### Load Images Directly Using Docker or containerd

Extract the tar package and load images manually.

1. Extract the tar archive:

    ```shell
    tar xvf agentclaw_0.2.0.bundle.tar
    ```

    After extraction, you will get:

    - hints.yaml: image template
    - images.tar: container images
    - original-chart: chart package

2. Load images into Docker or containerd:

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr -n k8s.io image import images.tar
        ```

!!! note

    Each node must load images into Docker or containerd individually.
    After loading, you must tag images to ensure Registry and Repository match the installation configuration.

### Installation

#### Prerequisites

1. Ensure the target Kubernetes cluster has the required dependencies installed:

    - hydra-apiserver
    - kpanda-apiserver
    - ghippo-apiserver
    - kpanda-clusterpedia-apiserver

2. Update hydra AuthorizationPolicy to allow traffic from `agentclaw-system`:

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

3. Configure kube-state-metrics in `insight-system`:

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
              - --metric-labels-allowlist=nodes=[feature.node.kubernetes.io/cpu-cpuid.HYPERVISOR]
              - '--port=8080'
              - --resources=configmaps,cronjobs,daemonsets,deployments,horizontalpodautoscalers,jobs,limitranges,namespaces,networkpolicies,nodes,persistentvolumeclaims,persistentvolumes,pods,replicasets,replicationcontrollers,resourcequotas,secrets,services,statefulsets,storageclasses
    +         - --metric-annotations-allowlist=deployments=[agentclaw.io/instance-name,agentclaw.io/workspace-id]
    ```

#### Install via Kpanda UI

After successfully syncing images and charts using chart-syncer, you can install directly from the Kpanda **Helm Applications** page.
Update the offline repository, locate the `agentclaw` chart, and install it. No parameter changes are required.

#### Install via Helm CLI

1. Add Helm repository:

    ```bash
    helm repo add agentclaw-release https://release.daocloud.io/chartrepo/clawos
    helm repo update
    ```

2. Install the chart:

    ```bash
    helm upgrade agentclaw agentclaw-release -n agentclaw-system --install --create-namespace
    ```


## Online Installation

!!! info

    The prerequisites for online installation are the same as for offline installation.


### Install via Kpanda UI

First, add the `agentclaw-release` repository in **Helm Apps** - **Helm Repositories**: `https://release.daocloud.io/chartrepo/agentclaw`,
then find the `agentclaw` chart in **Helm Charts** and click **Install**. No parameter changes are required during installation.


### Install via Helm

1. Add the repository:

    ```bash
    helm repo add agentclaw-release https://release.daocloud.io/chartrepo/agentclaw
    helm repo update
    ```

2. Install the chart:

    ```bash
    helm upgrade agentclaw agentclaw-release -n agentclaw-system --install --create-namespace
    ```
