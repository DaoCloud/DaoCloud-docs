# Offline Upgrade Container Registry Module

This page explains how to install or upgrade the container registry module after [downloading it from the Download Center](../../download/modules/kangaroo.md).

!!! info

    The word `kangaroo` appearing in the following commands or scripts is the internal development code name of the container registry module.

## Load Images from the Installation Package

You can load the images in one of the following two ways. When an container registry exists in the environment, it is recommended to choose the chart-syncer to synchronize the images to the container registry, as this method is more efficient and convenient.

### Synchronize Images to the Container Registry using chart-syncer

1. Create load-image.yaml

    !!! note  

        All parameters in this YAML file are mandatory. You need a private container registry and modify the relevant configurations.

    === "Installed chart repo"

        If the current environment has an installed chart repo, chart-syncer also supports exporting the chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: kangaroo-offline # (1)
        target:
          containerRegistry: 10.16.10.111 # (2)
          containerRepository: release.daocloud.io/kangaroo # (3)
          repo:
            kind: HARBOR # (4)
            url: http://10.16.10.111/chartrepo/release.daocloud.io # (5)
            auth:
            username: "admin" # (6)
            password: "Harbor12345" # (7)
          containers:
            auth:
              username: "admin" # (8)
              password: "Harbor12345" # (9)
        ```

        1. Go to the relative path where the charts-syncer command is executed, instead of the relative path between this YAML file and the offline package.
        2. Modify it to your container registry URL.
        3. Modify it to your container registry.
        4. It can also be any other supported Helm Chart repository category.
        5. Modify it to the chart repo URL.
        6. Your container registry username.
        7. Your container registry password.
        8. Your container registry username.
        9. Your container registry password.

    === "If chart repo is not installed"

        If the chart repo is not installed in the current environment, chart-syncer also supports exporting the chart as a tgz file and storing it in the specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: kangaroo-offline # (1)
        target:
          containerRegistry: 10.16.10.111 # (2)
          containerRepository: release.daocloud.io/kangaroo # (3)
          repo:
            kind: LOCAL
            path: ./local-repo # (4)
          containers:
            auth:
              username: "admin" # (5)
              password: "Harbor12345" # (6)
        ```

        1. Provide the relative path to execute the charts-syncer command, instead of the relative path between this YAML file and the offline package.
        2. Change it to your container registry URL.
        3. Change it to your container registry.
        4. Local path of the chart.
        5. Your container registry username.
        6. Your container registry password.

1. Run the command to synchronize images.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### Directly load with Docker or containerd

Extract and load the image files.

1. Extract the tar compressed package.

    ```shell
    tar xvf kangaroo.bundle.tar
    ```

    After successful extraction, you will get 3 files:

    - hints.yaml
    - images.tar
    - original-chart

2. Load the images from local to Docker or containerd.

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr image import images.tar
        ```

!!! note

    Each node needs to perform the image loading operation with Docker or containerd.
    After loading, the image needs to be tagged to keep the Registry, Repository consistent with the installation.

## Upgrade

There are two ways to upgrade. You can choose the corresponding upgrade method based on the prerequisite steps:

=== "Upgrade through helm repo"

    1. Check if the global helm repository exists.

        ```shell
        helm repo list | grep kangaroo
        ```

        If the result is empty or shows the following prompt, proceed to the next step; otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    1. Add the global helm repository.

        ```shell
        helm repo add kangaroo http://{harbor url}/chartrepo/{project}
        ```

    1. Update the global helm repository.

        ```shell
        helm repo update kangaroo # (1)
        ```

        1. If the helm version is too low, it may fail. If it fails, try executing `helm update repo`.

    1. Select the global management version you want to install (it is recommended to install the latest version).

        ```shell
        helm search repo kangaroo/kangaroo --versions
        ```

        ```none
        [root@master ~]# helm search repo kangaroo/kangaroo --versions
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        kangaroo/kangaroo  0.9.0          v0.9.0       A Helm chart for Kangaroo
        ...
        ```

    1. Backup the `--set` parameters.

        Before upgrading the global management version, it is recommended to run the following command to backup the `--set` parameters of the old version.

        ```shell
        helm get values kangaroo -n kangaroo-system -o yaml > bak.yaml
        ```

    1. Check the version update records. If there are updates to CRDs, update the kangaroo CRDs.

        ```shell
        helm pull kangaroo/kangaroo --version 0.9.0 && tar -zxf kangaroo-0.9.0.tgz
        kubectl apply -f kangaroo/crds
        ```

    1. Execute `helm upgrade`.

        Before upgrading, it is recommended to replace the `global.imageRegistry` field in bak.yaml with the current container registry address.

        ```shell
        export imageRegistry={你的镜像仓库}
        ```

        ```shell
        helm upgrade kangaroo kangaroo/kangaroo \
          -n kangaroo-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
          --version 0.9.0
        ```

=== "Upgrading via chart package"

    1. Back up the `--set` parameters.

        Before upgrading the global management version, it is recommended to run the following command to backup the `--set` parameters of the old version.

        ```shell
        helm get values kangaroo -n kangaroo-system -o yaml > bak.yaml
        ```

    1. Check the version update records. If there are updates to CRDs, update the kangaroo CRDs.

        ```shell
        kubectl apply -f ./crds
        ```

    1. Execute `helm upgrade`.

        Before upgrading, it is recommended to replace the `global.imageRegistry` field in bak.yaml with the current container registry address.

        ```shell
        export imageRegistry={your_image_repository}
        ```

        ```shell
        helm upgrade kangaroo . \
          -n kangaroo-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
        ```
