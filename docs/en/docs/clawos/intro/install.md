# Installation

This page describes two installation methods for ClawOS: offline installation and online installation.

!!! warning

    ClawOS only supports WS mode and does not support CSP mode.

## Offline Installation

This page explains how to download the ClawOS offline package and install it.

### Download

Use the following link to download the ClawOS offline package:

```text
https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/agentclaw_v0.2.3_amd64.tar
```

If a newer version is available, replace `v0.2.3` in the URL above with the desired version.

!!! info

    If you need the arm64 version, use the following link:

    ```text
    https://qiniu-download-public.daocloud.io/DaoCloud_Enterprise/agentclaw_v0.2.3_arm64.tar
    ```

### Load Images and Charts from the Offline Package

!!! info

    Prerequisite: Upload the offline package to the target node.

You can load images using either of the following methods. If your environment includes an image registry, using chart-syncer to synchronize images to the registry is recommended because it is more efficient and convenient.

#### Synchronize Images to an Image Registry with chart-syncer

1. Create `load-image.yaml`.

    !!! note

        All parameters in this YAML file are required. You need a private image registry and must modify the corresponding configuration.

    === "Chart repository installed"

        If a chart repository is already installed in the current environment, chart-syncer also supports exporting Charts to the specified repository.

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

        1. Relative to the directory where the `charts-syncer` command is executed, not the relative path between this YAML file and the offline package
        2. Replace with your image registry URL
        3. Replace with your image repository
        4. Can also be any other supported Helm Chart repository type
        5. Replace with your chart repository URL
        6. Your image registry username
        7. Your image registry password
        8. Your image registry username
        9. Your image registry password

    === "Chart repository not installed"

        If no chart repository is installed in the current environment, chart-syncer also supports exporting Charts as `.tgz` files and storing them in the specified path.

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

        1. Relative to the directory where the `charts-syncer` command is executed, not the relative path between this YAML file and the offline package
        2. Replace with your image registry URL
        3. Replace with your image repository
        4. Local path for storing Charts
        5. Your image registry username
        6. Your image registry password

1. Run the image synchronization command.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

#### Load Images Directly with Docker or containerd

Extract the package and load the image files.

1. Extract the tar archive.

    ```shell
    tar xvf agentclaw_0.2.0.bundle.tar
    ```

    After extraction, the following files will be available:

    - `hints.yaml`: image manifest
    - `images.tar`: image package
    - `original-chart`: chart package

2. Load images into Docker or containerd from the local file.

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr -n k8s.io image import images.tar
        ```

!!! note

    You must load the images into Docker or containerd on every node.
    After loading, tag the images so that the Registry and Repository match those used during installation.

### Offline Installation Steps

#### Prerequisites

1. Before installation, ensure that the target Kubernetes cluster has the following required services configured:

    - kpanda (0.45.0+)
    - ghippo (0.48.0+)
    - insight (0.41.0+)
    - hydra (WS version 0.16.0+)

    Note: ClawOS v0.4.0 requires insight 0.42.2.

2. Update the hydra AuthorizationPolicy to allow traffic from `agentclaw-system`.

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

3. Configure the startup arguments for `kube-state-metrics` in the `insight-system` namespace (this configuration must be applied to the cluster where Agent is deployed).

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

#### Install Through the Kpanda UI

After chart-syncer successfully synchronizes the images and Charts, refresh the offline repository in **Helm Apps** within Kpanda, then locate the `agentclaw` Chart and install it. No installation parameters need to be changed.

#### Install with Helm

1. Add the Helm repository.

    ```bash
    helm repo add agentclaw-release https://release.daocloud.io/chartrepo/clawos
    helm repo update
    ```

2. Install the Chart.

    ```bash
    helm upgrade agentclaw agentclaw-release -n agentclaw-system --install --create-namespace
    ```

## Online Installation

!!! info

    The prerequisites for online installation are the same as those for the offline installation.

### Install Through the Kpanda UI

First, add the `agentclaw-release` repository in **Helm Apps** -> **Helm Repositories**:
`https://release.daocloud.io/chartrepo/agentclaw`

Then go to **Helm Templates**, locate the `agentclaw` Chart, and click **Install**. No installation parameters need to be changed.

### Install with Helm

1. Add the repository.

    ```bash
    helm repo add agentclaw-release
    helm repo update
    ```

2. Install the Chart.

    ```bash
    helm upgrade agentclaw agentclaw-release -n agentclaw-system --install --create-namespace
    ```
