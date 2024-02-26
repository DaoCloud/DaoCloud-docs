---
MTPE: windsonsea
date: 2024-02-19
---

# Offline Upgrade

The Workbench supports offline upgrades. You need to first load the image from the [installation package](../download/modules/amamba.md) and then run the corresponding command to upgrade.

```shell
tar -vxf amamba_x.y.z_amd64.tar
```

After unpacking, you will get a compressed bundle: amamba_x.y.z.bundle.tar

## Load Image from Installation Package

Support loading images in two ways.

### Sync Images via charts-syncer

If there is an image repository in the environment, it is recommended to synchronize the images to the image repository through charts-syncer for more efficient and convenient operation.

1. Create `load-image.yaml` with the following content as the configuration file for charts-syncer.

   All parameters in the `load-image.yaml` file are required. You need a private image repository and refer to the following instructions to modify each configuration. For detailed explanation of the charts-syncer configuration file, refer to its [official documentation](https://github.com/bitnami-labs/charts-syncer).

    === "HARBOR chart repo already installed"

        If the HARBOR chart repo is already installed in the environment, charts-syncer also supports exporting the chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: amamba-offline # (1)
        target:
          containerPrefixRegistry: 10.16.10.111 # (2)
          repo:
            kind: HARBOR # (3)
            url: http://10.16.10.111/chartrepo/release.daocloud.io # (4)
            auth:
              username: "admin" # (5)
              password: "Harbor12345" # (6)
          containers:
            auth:
              username: "admin" # (7)
              password: "Harbor12345" # (8) 
        ```

        1. Relative path to run the charts-syncer command, not the relative path between this YAML file and the offline package
        2. Change to your image repository url
        3. Can also be any other supported Helm Chart repository category
        4. Change to the chart repo project url
        5. Your image repository username
        6. Your image repository password
        7. Your image repository username
        8. Your image repository password

    === "CHARTMUSEUM chart repo already installed"

        If the CHARTMUSEUM chart repo is already installed in the environment, charts-syncer also supports exporting the chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: amamba-offline # (1)
        target:
          containerPrefixRegistry: 10.16.10.111 # (2)
          repo:
            kind: CHARTMUSEUM # (3)
            url: http://10.16.10.111 # (4)
            auth:
              username: "rootuser" # (5)
              password: "rootpass123" # (6)
          containers:
            auth:
              username: "rootuser" # (7)
              password: "rootpass123" # (8) 
        ```

        1. Relative path to run the charts-syncer command, not the relative path between this YAML file and the offline package
        2. Change to your image repository url
        3. Can also be any other supported Helm Chart repository category
        4. Change to chart repo url
        5. Your image repository username, if chartmuseum does not have login authentication enabled, you do not need to fill in auth
        6. Your image repository password
        7. Your image repository username
        8. Your image repository password

    === "Chart repo not installed"

        If the chart repo is not installed in the current environment, charts-syncer also supports exporting the chart as a `tgz` file and storing it in a specified path.

        ```yaml
        source:
          intermediateBundlesPath: amamba-offline # (1)
        target:
          containerRegistry: 10.16.23.145 # (2)
          containerRepository: release.daocloud.io/amamba # (3)
          repo:
            kind: LOCAL
            path: ./local-repo # (4)
          containers:
            auth:
              username: "admin" # (5)
              password: "Harbor12345" # (6)
        ```

        1. Relative path to run the charts-syncer command, not the relative path between this YAML file and the offline package
        2. Change to your image repository url
        3. Change to your image repository
        4. Local path of the chart
        5. Your image repository username
        6. Your image repository password

2. Place amamba_x.y.z.bundle.tar in the amamba-offline folder.

3. Run the command to sync images.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### Load Images Directly via Docker or containerd

1. Unpack the `tar` compressed bundle.

    ```shell
    tar -vxf amamba_x.y.z.bundle.tar
    ```

    After successful unpacking, you will get 3 files:

    - hints.yaml
    - images.tar
    - original-chart

2. Run the following command to load the images from the local to Docker or containerd.

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr -n k8s.io image import images.tar
        ```

!!! note

    - Images need to be loaded via Docker or containerd on each node.
    - After loading, the images need to be tagged to match the Registry, Repository, and installation consistency.

## Upgrade

=== "Upgrade via helm repo"

    1. Check if the Workbench helm repository exists.

        ```shell
        helm repo list | grep amamba
        ```

        If the result is empty or shows the following message, proceed to the next step; otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    2. Add the helm repository for Workbench.

        ```shell
        helm repo add amamba-release http://{harbor url}/chartrepo/{project}
        ```

    3. Update the helm repository for Workbench.

        ```shell
        helm repo update amamba-release # (1)
        ```

        1. If the Helm version is too low and the update fails, try executing helm update repo

    4. Choose the version of the Workbench you want to install (recommended to install the latest version).

        ```shell
        helm search repo amamba-release/amamba --versions
        ```

        ```text
        NAME                    CHART VERSION  APP VERSION  DESCRIPTION
        amamba-release/amamba	 0.24.0         0.24.0       Amamba is the entrypoint to DCE5.0, provides de...
        amamba-release/amamba	 0.23.0         0.23.0       Amamba is the entrypoint to DCE5.0, provides de...
        amamba-release/amamba	 0.22.1         0.22.1       Amamba is the entrypoint to DCE5.0, provides de...
        amamba-release/amamba	 0.22.0         0.22.0       Amamba is the entrypoint to DCE5.0, provides de...
        amamba-release/amamba	 0.21.2         0.21.2       Amamba is the entrypoint to DCE5.0, provides de...
        amamba-release/amamba	 0.21.1         0.21.1       Amamba is the entrypoint to DCE5.0, provides de...
        amamba-release/amamba	 0.21.0         0.21.0       Amamba is the entrypoint to DCE5.0, provides de...
        ...
        ```

    5. Back up the `--set` parameters.

        Before upgrading the Workbench version, it is recommended to run the following command to back up the `--set` parameters of the old version.

        ```shell
        helm get values amamba -n amamba-system -o yaml > bak.yaml
        ```

    6. Run `helm upgrade`.

        Before upgrading, it is recommended to overwrite the `global.imageRegistry` field in bak.yaml with the current image repository address.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade amamba amamba-release/amamba \
          -n amamba-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.24.0
        ```

=== "Upgrade via chart package"

    1. Prepare the `original-chart` (obtained by unpacking amamba_x.y.z.bundle.tar).

    2. Back up the `--set` parameters.

        Before upgrading the Workbench version, it is recommended to run the following command to back up the `--set` parameters of the old version.

        ```shell
        helm get values amamba -n amamba-system -o yaml > bak.yaml
        ```

    3. Run `helm upgrade`.

        Before upgrading, it is recommended to overwrite the `global.imageRegistry` field in bak.yaml with the current image repository address.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade amamba original-chart \
          -n amamba-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
        ```
