# Offline Upgrade Service Mesh Module

This page explains how to install or upgrade after [downloading the Service Mesh module](../../download/modules/mspider.md).

!!! info

    The __mspider__ mentioned in the following commands or scripts is the internal development code name of the Service Mesh module.

## Load Image from Installation Package

You can load the image in one of the following two ways. When there is a container registry in the environment, it is recommended to use __chart-syncer__ to synchronize the image to the container registry, as this method is more efficient and convenient.

### Synchronize Image to Container Registry with chart-syncer

1. Create load-image.yaml

    !!! note  

        All parameters in this YAML file are required. You need a private container registry and modify the relevant configuration.

    === "Chart Repo Installed"

        If the current environment has installed the chart repo, chart-syncer also supports exporting the chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mspider-offline # (1)
        target:
          containerRegistry: 10.16.10.111 # (2)
          containerRepository: release.daocloud.io/mspider # (3)
          repo:
            kind: HARBOR # (4)
            url: http://10.16.10.111/chartrepo/release.daocloud.io # (5)
            auth:
              username: "admin" # (6)
              password: "Harbor12345" # (7)
          containers:
            auth:
              username: "admin" # (6)
              password: "Harbor12345" # (7)
        ```

        1. Relative path to run the charts-syncer command, not the relative path between this YAML file and the offline package
        2. Change to your container registry url
        3. Change to your container registry
        4. Can be any other supported Helm Chart repository category
        5. Change to chart repo url
        6. Your container registry username
        7. Your container registry password

    === "Chart Repo Not Installed"

        If the current environment does not have a chart repo installed, chart-syncer also supports exporting the chart as a tgz file and storing it in a specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mspider-offline # (1)
        target:
          containerRegistry: 10.16.10.111 # (2)
          containerRepository: release.daocloud.io/mspider # (3)
          repo:
            kind: LOCAL
            path: ./local-repo # (4)
          containers:
            auth:
              username: "admin" # (5)
              password: "Harbor12345" # (6)
        ```

        1. Relative path to run the charts-syncer command, not the relative path between this YAML file and the offline package
        2. Change to your container registry url
        3. Change to your container registry
        4. Local path of the chart
        5. Your container registry username
        6. Your container registry password

1. Run the command to synchronize the image.

    ```bash
    charts-syncer sync --config load-image.yaml
    ```

### Directly Load with Docker or containerd

Unpack and load the image file.

1. Unpack the tar compressed file.

    ```bash
    tar xvf mspider.bundle.tar
    ```

    After successful unpacking, you will get 3 files:

    - hints.yaml
    - images.tar
    - original-chart

2. Load the image from local to Docker or containerd.

    === "Docker"

        ```bash
        docker load -i images.tar
        ```

    === "containerd"

        ```bash
        ctr -n k8s.io image import images.tar
        ```

!!! note

    Each node needs to perform the Docker or containerd image loading operation,
    after loading, you need to tag the image to keep the Registry, Repository consistent with the installation.

## Upgrade

Before upgrading, make sure to back up the grid's configuration file, which is the `--set` parameter, to avoid problems caused by configuration loss during the upgrade.

### Check if mspider-release repository exists locally

```bash
helm repo list | grep mspider-release
```

If the result is empty or shows as follows, proceed to the next step; otherwise, skip the next step and proceed directly to the update.

```none
Error: no repositories to show
```

### Add Helm Repo

```bash
helm repo add mspider-release http://{harbor_url}/chartrepo/{project}
```

Update the helm repo for the Service Mesh.

```bash
helm repo update mspider-release
```

Choose the version of the Service Mesh you want to install (it is recommended to install the latest version).

```bash
# Update the image version in the mspider-release repository
helm update repo

# Get the latest version
helm search repo mspider-release/mspider --versions
NAME                      CHART VERSION  APP VERSION  DESCRIPTION
mspider-release/mspider   v0.20.1        v0.20.1      Mspider management plane application, deployed ...
...
```

### Back up `--set` Parameters

Before upgrading the Service Mesh version, it is recommended to run the following command to back up
the `--set` parameters of the old version.

```bash
helm get values mspider -n mspider-system -o yaml > bak.yaml
```

### Update mspider

```bash
helm upgrade --install --create-namespace \
    -n mspider-system mspider mspider-release/mspider \
    --cleanup-on-fail \
    --version=v0.20.1 \
    --set global.imageRegistry=release.daocloud.io/mspider \
    -f mspider.yaml
```

### Run `helm upgrade`

Before upgrading, it is recommended to update the __global.imageRegistry__ field in bak.yaml
to the current container registry address.

```bash
export imageRegistry={YOUR_IMAGE_REGISTRY}
```

```bash
helm upgrade mspider mspider-release/mspider \
    -n mspider-system \
    -f ./bak.yaml \
    --set global.imageRegistry=$imageRegistry \
    --version 0.20.1
```
