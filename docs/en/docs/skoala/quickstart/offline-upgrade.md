# Offline upgrade microservice engine

This page explains how to install or upgrade the microservice engine module after downloading it from [Download Center](../../download/dce5.md).

!!! info

    The word `skoala` appearing in the following commands or scripts is the internal development code name of the microservice engine module.

## Load the image from the installation package

You can load the image in one of the following two ways. When there is a container registry in the environment, it is recommended to select chart-syncer to synchronize the image to the container registry. This method is more efficient and convenient.

### chart-syncer synchronously mirrors to the container registry

1. Create load-image.yaml

    !!! note

        All parameters in this YAML file are required. You need a private container registry and modify related configurations.

    === "chart repo installed"

        If the current environment has installed the chart repo, chart-syncer also supports exporting the chart as a tgz file.

        ```yaml
        source:
          intermediateBundlesPath: skoala-offline # The relative path to execute the charts-syncer command, not the relative path between this YAML file and the offline bundle
        target:
          containerRegistry: 10.16.23.145 # need to be changed to your container registry url
          containerRepository: release.daocloud.io/skoala # need to be changed to your container registry
          repo:
            kind: HARBOR # Can also be any other supported Helm Chart repository class
            url: http://10.16.23.145/chartrepo/release.daocloud.io # need to change to chart repo url
            auth:
            username: "admin" # Your container registry username
            password: "Harbor12345" # Your container registry password
          containers:
            auth:
              username: "admin" # Your container registry username
              password: "Harbor12345" # Your container registry password
        ```

    === "chart repo not installed"

        If the chart repo is not installed in the current environment, chart-syncer also supports exporting the chart as a tgz file and storing it in the specified path.

        ```yaml
        source:
          intermediateBundlesPath: skoala-offline # The relative path to execute the charts-syncer command, not the relative path between this YAML file and the offline bundle
        target:
          containerRegistry: 10.16.23.145 # need to be changed to your container registry url
          containerRepository: release.daocloud.io/skoala # need to be changed to your container registry
          repo:
            kind: LOCAL
            path: ./local-repo # chart local path
          containers:
            auth:
              username: "admin" # Your container registry username
              password: "Harbor12345" # Your container registry password
        ```

1. Execute the synchronous mirroring command.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### docker or containerd direct loading

Unzip and load the image file.

1. Unzip the tar archive.

    ```shell
    tar xvf skoala.bundle.tar
    ```

    After successful decompression, you will get 3 files:

    - hints.yaml
    - images.tar
    - original-chart

2. Load the image locally to Docker or containerd.

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr image import images.tar
        ```

!!! note
    Each node needs to do docker or containerd loading image operation
    After the loading is complete, the tag image is required to keep the Registry and Repository consistent with the installation.

## upgrade

There are two ways to upgrade. You can choose the corresponding upgrade plan according to the pre-operations:

=== "upgrade via helm repo"

    1. Check whether the microservice engine helm repository exists.

        ```shell
        helm repo list | grep skoala
        ```

        If the returned result is empty or as prompted, proceed to the next step; otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    2. Add the helm repository of the microservice engine.

        ```shell
        heml repo add skoala-release http://{harbor url}/chartrepo/{project}
        ```

    3. Update the helm repository of the microservice engine.

        ```shell
        helm repo update skoala-release # If the helm version is too low, it will fail. If it fails, please try to execute helm update repo
        ```

    4. Select the microservice engine version you want to install (the latest version is recommended).

        ```shell
        helm search repo skoala-release/skoala --versions
        ```

        ```none
        [root@master ~]# helm search repo skoala-release/skoala --versions
        NAME CHART VERSION APP VERSION DESCRIPTION
        skoala-release/skoala 0.14.0 v0.14.0 A Helm chart for Skoala
        ...
        ```

    5. Back up the `--set` parameter.

        Before upgrading the microservice engine version, it is recommended that you execute the following command to back up the `--set` parameter of the old version.

        ```shell
        helm get values ​​skoala -n skoala-system -o yaml > bak.yaml
        ```

    6. Execute `helm upgrade`.

        Before upgrading, it is recommended that you override the `global.imageRegistry` field in bak.yaml to the address of the currently used container registry.

        ```shell
        export imageRegistry={your container registry}
        ```

        ```shell
        helm upgrade skoala skoala-release/skoala \
        -n skoala-system \
        -f ./bak.yaml \
        --set global.imageRegistry=$imageRegistry
        --version 0.14.0
        ```

=== "upgrade via chart package"

    1. Back up the `--set` parameter.

        Before upgrading the microservice engine version, it is recommended that you execute the following command to back up the `--set` parameter of the old version.

        ```shell
        helm get values ​​skoala -n skoala-system -o yaml > bak.yaml
        ```

    2. Execute `helm upgrade`.

        Before upgrading, it is recommended that you overwrite `global.imageRegistry` in bak.yaml to the address of the current image registry.

        ```shell
        export imageRegistry={your container registry}
        ```

        ```shell
        helm upgrade skoala . \
        -n skoala-system \
        -f ./bak.yaml \
        --set global.imageRegistry=$imageRegistry
        ```
