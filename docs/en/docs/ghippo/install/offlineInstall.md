# Offline upgrade global management module

This page explains how to install or upgrade the global management module after downloading it from [Download Center](../../download/dce5.md).

!!! info

    The word `ghippo` appearing in the commands or scripts below is the internally developed code name for the global management module.

## Synchronize image to the container registry

First, synchronize the image to the specified container registry through chart-syncer.

1. Create load-image.yaml

    !!! note

        All parameters in this YAML file are required. You need a private container registry and modify related configurations.

    === "chart repo installed"

        If the current environment has installed the chart repo, chart-syncer also supports exporting the chart as a tgz file.

        ```yaml
        source:
        intermediateBundlesPath: ghippo-offline # relative path to charts-syncer
                                        # But not the relative path between this YAML file and the offline package
        target:
        containerRegistry: 10.16.10.111 # need to be changed to your container registry url
        containerRepository: release.daocloud.io/ghippo # need to be changed to your container registry
        repo:
          kind: HARBOR # Can also be any other supported Helm Chart repository class
          url: http://10.16.10.111/chartrepo/release.daocloud.io # need to change to chart repo url
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
        intermediateBundlesPath: ghippo-offline # relative path to charts-syncer
                                    # But not the relative path between this YAML file and the offline package
        target:
        containerRegistry: 10.16.10.111 # need to be changed to your container registry url
        containerRepository: release.daocloud.io/ghippo # need to be changed to your container registry
        repo:
          kind: LOCAL
          path: ./local-repo # chart local path
        containers:
          auth:
          username: "admin" # Your container registry username
          password: "Harbor12345" # Your container registry password
        ```

1. Execute the synchronous image command.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

## Load image file

Unzip and load the image file.

1. Unzip the tar archive.

    ```shell
    tar xvf ghippo.bundle.tar
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

    After the loading is complete, the tag image is required to keep the Registry and Repository consistent with the installation.

## upgrade

There are two ways to upgrade. You can choose the corresponding upgrade plan according to the pre-operations:

!!! note

    When upgrading from v0.11.x (or lower) to v0.12.0 (or higher), you need to change all keycloak keys in `bak.yaml` to keycloakx.

    Example modification of this key:

    ```yaml
    USER-SUPPLIED VALUES:
    keycloak:
        ...
    ```

    change into:

    ```yaml
    USER-SUPPLIED VALUES:
    keycloakx:
        ...
    ```

=== "upgrade via helm repo"

    1. Check whether the global management helm repository exists.

        ```shell
        helm repo list | grep ghippo
        ```

        If the returned result is empty or as prompted, proceed to the next step; otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    1. Add the globally managed helm repository.

        ```shell
        heml repo add ghippo http://{harbor url}/chartrepo/{project}
        ```

    1. Update the globally managed helm repository.

        ```shell
        helm repo update ghippo # If the helm version is too low, it will fail. If it fails, please try to execute helm update repo
        ```

    1. Select the version of Global Management you want to install (the latest version is recommended).

        ```shell
        helm search repo ghippo/ghippo --versions
        ```

        ```none
        [root@master ~]# helm search repo ghippo/ghippo --versions
        NAME CHART VERSION APP VERSION DESCRIPTION
        ghippo/ghippo 0.9.0 v0.9.0 A Helm chart for GHippo
        ...
        ```

    1. Back up the `--set` parameter.

        Before upgrading the global management version, it is recommended that you execute the following command to back up the `--set` parameter of the old version.

        ```shell
        helm get values ​​ghippo -n ghippo-system -o yaml > bak.yaml
        ```

    1. Execute `helm upgrade`.

        Before upgrading, it is recommended that you override the `global.imageRegistry` field in bak.yaml to the address of the currently used container registry.

        ```shell
        export imageRegistry={your container registry}
        ```

        ```shell
        helm upgrade ghippo ghippo/ghippo \
        -n ghippo-system\
        -f ./bak.yaml \
        --set global.imageRegistry=$imageRegistry
        --version 0.9.0
        ```

=== "upgrade via chart package"

    1. Back up the `--set` parameter.

        Before upgrading the global management version, it is recommended that you execute the following command to back up the `--set` parameter of the old version.

        ```shell
        helm get values ​​ghippo -n ghippo-system -o yaml > bak.yaml
        ```

    1. Execute `helm upgrade`.

        Before upgrading, it is recommended that you overwrite `global.imageRegistry` in bak.yaml to the address of the current image registry.

        ```shell
        export imageRegistry={your container registry}
        ```

        ```shell
        helm upgrade ghippo .\
        -n ghippo-system\
        -f ./bak.yaml \
        --set global.imageRegistry=$imageRegistry
        ```