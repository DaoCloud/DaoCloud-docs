# Upgrading the Offline Service Mesh Module

This page explains how to install or upgrade the service mesh module after [downloading](../../download/modules/mspider.md) it.

!!! info

    The term "mspider" mentioned in the following commands or scripts refers to the internal development code name for the service mesh module.

## Loading Images from the Installation Package

You can load the images in one of the following two ways. When a container registry exists in the environment, it is recommended to use __chart-syncer__ to synchronize the images to the registry as it is more efficient and convenient.

### Synchronizing Images to a Container Registry using chart-syncer

1. Create __load-image.yaml__ .

    !!! note

        All parameters in this YAML file are required. You need a private container registry and modify the relevant configurations.

    === "Chart Repo Installed"

        If a chart repo is already installed in the current environment, __chart-syncer__ also supports exporting the chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mspider-offline # The relative path to the directory where the __charts-syncer__ command is executed, not the relative path between this YAML file and the offline package
        target:
          containerRegistry: 10.16.10.111 # Change this to your container registry URL
          containerRepository: release.daocloud.io/mspider # Change this to your container repository
          repo:
            kind: HARBOR # This can also be any other supported Helm Chart repository type
            url: http://10.16.10.111/chartrepo/release.daocloud.io # Change this to your chart repo URL
            auth:
              username: "admin" # Your container registry username
              password: "Harbor12345" # Your container registry password
          containers:
            auth:
              username: "admin" # Your container registry username
              password: "Harbor12345" # Your container registry password
        ```

    === "Chart Repo Not Installed"

        If a chart repo is not installed in the current environment, __chart-syncer__ also supports exporting the chart as a tgz file and storing it in the specified path.

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

        1. The relative path to the directory where the __charts-syncer__ command is executed, not the relative path between this YAML file and the offline package
        2. Change this to your container registry URL
        3. Change this to your container repository
        4. Chart local path
        5. Your container registry username
        6. Your container registry password

1. Run the command to synchronize the images.

    ```bash
    ~ charts-syncer sync --config load-image.yaml
    ```

### Loading Directly into Docker or containerd

Extract and load the image files.

1. Uncompress the tar archive.

    ```bash
    ~ tar xvf mspider.bundle.tar
    ```

    After a successful extraction, you will have three files:

    - hints.yaml
    - images.tar
    - original-chart

2. Load the images from the local directory to Docker or containerd.

    === "Docker"

        ```bash
        ~ docker load -i images.tar
        ```

    === "containerd"

        ```bash
        ~ ctr -n k8s.io image import images.tar
        ```

!!! note

    Each node needs to perform Docker or containerd image loading operations. After loading is complete, tag the images to maintain consistency in the registry and repository used during installation.

## Upgrading

Before upgrading, it is important to backup the mesh configuration file, which includes the `--set` parameters, to avoid configuration loss during the upgrade.

### Checking the Existence of the mspider-release Repository Locally

```bash
~ helm repo list | grep mspider-release
```

If the result is empty or shows the following prompt, proceed to the next step. Otherwise, skip the next step and proceed with the upgrade directly.

```none
Error: no repositories to show
```

### Adding the Helm Repository

```bash
~ helm repo add mspider-release http://{harbor_url}/chartrepo/{project}
```

Update the helm repository for the service mesh.

```bash
~ helm repo update mspider-release
```

Choose the version of the service mesh you want to install (it is recommended to install the latest version).

```bash
# Update the image versions in the mspider-release repository
~ helm update repo

# Get the latest versions
~ helm search repo mspider-release/mspider --versions
NAME                      CHART VERSION  APP VERSION  DESCRIPTION
mspider-release/mspider   v0.20.1        v0.20.1      Mspider management plane application, deployed ...
...
```

### Backing up the `--set` Parameters

Before upgrading the service mesh version, it is advisable to back up the `--set` parameters of the older version using the following command.

```bash
~ helm get values mspider -n mspider-system -o yaml > bak.yaml
```

### Updating mspider

```bash
~ helm upgrade --install --create-namespace \
    -n mspider-system mspider mspider-release/mspider \
    --cleanup-on-fail \
    --version=v0.20.1 \
    --set global.imageRegistry=release.daocloud.io/mspider \
    -f mspider.yaml
```

### Executing `helm upgrade` 

Before upgrading, it is recommended to update the __global.imageRegistry__ field in __bak.yaml__ with the current container registry address.

```bash
~ export imageRegistry={YOUR_IMAGE_REGISTRY}
```

```bash
~ helm upgrade mspider mspider-release/mspider \
    -n mspider-system \
    -f ./bak.yaml \
    --set global.imageRegistry=$imageRegistry \
    --version 0.20.1
```
