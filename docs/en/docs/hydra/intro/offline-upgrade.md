# Offline Upgrade of the LLM Studio

This page explains how to install or upgrade after [downloading the LLM Studio module](../../../download/modules/hydra.md).

!!! info

    The term __hydra__ appearing in the following commands or scripts is the internal development codename for the LLM Studio module.

## Extract the downloaded package to get the bundle package

```shell
tar -xvf hydra_v0.9.0_amd64.tar
```

After extraction, you will get three bundle.tar packages: hydra, hydra-agent, and web-search-agent.

```shell
$ ll hydra_v0.9.0_amd64
-rw-r--r--@ 1 nicole  staff    72M Sep 12 12:05 hydra_v0.9.0.bundle.tar
-rw-r--r--@ 1 nicole  staff   502M Sep 12 12:05 hydra-agent_v0.9.0.bundle.tar
-rw-r--r--@ 1 nicole  staff   105M Sep 12 12:05 web-search-agent_v0.9.0.bundle.tar
```

## Load images from the installation package

You can load images using one of the two methods below. When a registry exists in your environment, it is recommended to use
**chart-syncer** to sync images to the registry, as this method is more efficient and convenient.

### chart-syncer sync images to the registry

1. Create load-image.yaml

    !!! note

        All parameters in this YAML file are required. You need a private registry and must modify the relevant configurations.

    === "Chart repo installed"

        If a chart repo is already installed in the current environment, chart-syncer also supports exporting charts as tgz files.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: hydra-offline # (1)!
        target:
          containerRegistry: 10.16.10.111 # (2)!
          containerRepository: release.daocloud.io/hydra # (3)!
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

        1. The relative path to execute the charts-syncer command, not the relative path between this YAML file and the offline package
        2. Must be changed to your registry URL
        3. Must be changed to your registry
        4. Can also be any other supported Helm Chart repository type
        5. Must be changed to the chart repo URL
        6. Your registry username
        7. Your registry password
        8. Your registry username
        9. Your registry password

    === "Chart repo not installed"

        If a chart repo is not installed in the current environment, chart-syncer also supports exporting charts as tgz files and storing them in a specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: hydra-offline # (1)!
        target:
          containerRegistry: 10.16.10.111 # (2)!
          containerRepository: release.daocloud.io/hydra # (3)!
          repo:
            kind: LOCAL
            path: ./local-repo # (4)!
          containers:
            auth:
              username: "admin" # (5)!
              password: "Harbor12345" # (6)!
        ```

        1. The relative path to execute the charts-syncer command, not the relative path between this YAML file and the offline package
        2. Must be changed to your registry URL
        3. Must be changed to your registry
        4. Local path of the chart
        5. Your registry username
        6. Your registry password

2. Run the sync image command.

    ```bash
    charts-syncer sync --config load-image.yaml
    ```

### Load directly with Docker or containerd

Extract and load the image file.

1. Extract the tar package.

    ```bash
    tar xvf hydra.bundle.tar
    ```

    After successful extraction, you will get three files:

    * hints.yaml
    * images.tar
    * original-chart

2. Load the image locally into Docker or containerd.

    === "Docker"

        ```bash
        docker load -i images.tar
        ```

    === "containerd"

        ```bash
        ctr -n k8s.io image import images.tar
        ```

!!! note

    Each node needs to perform the Docker or containerd image loading operation.
    After loading, you need to tag the images to keep the Registry and Repository consistent with the installation.

## Upgrade

Before upgrading, be sure to back up the mesh configuration file (i.e., the `--set` parameters) to avoid problems caused by configuration loss during the upgrade.

### Check if the hydra-release repository exists locally

```bash
helm repo list | grep hydra-release
```

If the result is empty or shows the following message, proceed to the next step; otherwise, skip to the update step directly.

```none
Error: no repositories to show
```

### Add helm repository

```bash
helm repo add hydra-release http://{harbor_url}/chartrepo/{project}
```

Update the LLM Studio helm repository.

```bash
helm repo update hydra-release
```

Choose the version of the LLM Studio you want to install (it is recommended to install the latest version).

```bash
# Update image versions in the hydra-release repository
helm update repo

# Get the latest version of the LLM Studio
helm search repo hydra-release/hydra --versions

# LLM Studio components for the worker cluster
helm search repo hydra-release/hydra-agent --versions

# Optional web search component for the worker cluster
helm search repo hydra-release/web-search-agent --versions
```

```output
NAME                          CHART VERSION    APP VERSION    DESCRIPTION
hydra-release/hydra           v0.9.0           v0.9.0         A Helm chart for Kubernetes
...
```

### Back up the `--set` parameters

Before upgrading the LLM Studio version, it is recommended to run the following command
to back up the old version’s `--set` parameters.

```bash
helm get values hydra -n hydra-system -o yaml > bak.yaml
```

### Run `helm upgrade`

Before upgrading, it is recommended to overwrite the `global.imageRegistry` field in bak.yaml
with the currently used registry address.

```bash
export imageRegistry={YOUR_IMAGE_REGISTRY}
```

```bash
helm upgrade hydra hydra-release/hydra 
    -n hydra-system 
    -f ./bak.yaml 
    --set global.imageRegistry=$imageRegistry 
    --version v0.9.0
```
