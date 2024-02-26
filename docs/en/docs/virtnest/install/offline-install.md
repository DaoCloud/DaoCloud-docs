# Offline Upgrade of the Virtual Machine Module

This page explains how to install or upgrade the Virtual Machine module after downloading it from the [Download Center](../../download/index.md).

!!! info

    The term "virtnest" appearing in the following commands or scripts is
    the internal development code name for the Virtual Machine module.

## Load Images from the Installation Package

You can load the images using one of the following two methods. When there is an
container registry available in your environment, it is recommended to choose the
chart-syncer method for synchronizing the images to the container registry, as it is
more efficient and convenient.

### Synchronize Images to the container registry using chart-syncer

1. Create __load-image.yaml__ file.

    !!! note

        All parameters in this YAML file are mandatory. You need a private container registry and modify the relevant configurations.

    === "Chart Repo Installed"

        If the chart repo is already installed in your environment, chart-syncer also supports exporting the chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: virtnest-offline # (1)
        target:
          containerRegistry: 10.16.10.111 # (2)
          containerRepository: release.daocloud.io/virtnest # (3)
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

        1. The relative path to run the charts-syncer command, not the relative path between this YAML file and the offline package.
        2. Change to your container registry URL.
        3. Change to your container registry.
        4. It can also be any other supported Helm Chart repository type.
        5. Change to the chart repo URL.
        6. Your container registry username.
        7. Your container registry password.
        8. Your container registry username.
        9. Your container registry password.

    === "Chart Repo Not Installed"

        If the chart repo is not installed in your environment, chart-syncer also supports exporting the chart as a tgz file and storing it in the specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: virtnest-offline # (1)
        target:
          containerRegistry: 10.16.10.111 # (2)
          containerRepository: release.daocloud.io/virtnest # (3)
          repo:
            kind: LOCAL
            path: ./local-repo # (4)
          containers:
            auth:
              username: "admin" # (5)
              password: "Harbor12345" # (6)
        ```

        1. The relative path to run the charts-syncer command, not the relative path between this YAML file and the offline package.
        2. Change to your container registry URL.
        3. Change to your container registry.
        4. Local path of the chart.
        5. Your container registry username.
        6. Your container registry password.

2. Run the command to synchronize the images.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### Load Images Directly using Docker or containerd

Unpack and load the image files.

1. Unpack the tar archive.

    ```shell
    tar xvf virtnest.bundle.tar
    ```

    After successful extraction, you will have three files:

    - hints.yaml
    - images.tar
    - original-chart

2. Load the images from the local file to Docker or containerd.

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr -n k8s.io image import images.tar
        ```

!!! note

    Perform the Docker or containerd image loading operation on each node.
    After loading is complete, tag the images to match the Registry and Repository used during installation.

## Upgrade

There are two upgrade methods available. You can choose the appropriate upgrade method based on the prerequisites:

=== "Upgrade via helm repo"

    1. Check if the Virtual Machine Helm repository exists.

        ```shell
        helm repo list | grep virtnest
        ```

        If the result is empty or shows the following message, proceed to the next step. Otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    1. Add the Virtual Machine Helm repository.

        ```shell
        helm repo add virtnest http://{harbor url}/chartrepo/{project}
        ```

    1. Update the Virtual Machine Helm repository.

        ```shell
        helm repo update virtnest # (1)
        ```

        1. If the helm version is too low, it may fail. If it fails, try executing `helm update repo`.

    1. Choose the version of the Virtual Machine you want to install (it is recommended to install the latest version).

        ```shell
        helm search repo virtnest/virtnest --versions
        ```

        ```none
        [root@master ~]# helm search repo virtnest/virtnest --versions
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        virtnest/virtnest  0.2.0          v0.2.0       A Helm chart for virtnest
        ...
        ```

    1. Back up the `--set` parameters.

        Before upgrading the Virtual Machine version, it is recommended to run the following command to backup the `--set` parameters of the previous version.

        ```shell
        helm get values virtnest -n virtnest-system -o yaml > bak.yaml
        ```

    1. Update the virtnest CRDs.

        ```shell
        helm pull virtnest/virtnest --version 0.2.0 && tar -zxf virtnest-0.2.0.tgz
        kubectl apply -f virtnest/crds
        ```

    1. Run `helm upgrade`.

        Before upgrading, it is recommended to replace the `global.imageRegistry` field in __bak.yaml__ with the current container registry address.

        ```shell
        export imageRegistry={your container registry}
        ```

        ```shell
        helm upgrade virtnest virtnest/virtnest \
          -n virtnest-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.2.0
        ```

=== "Upgrade via chart package"

    1. Back up the `--set` parameters.

        Before upgrading the Virtual Machine version, it is recommended to run the following command to backup the `--set` parameters of the previous version.

        ```shell
        helm get values virtnest -n virtnest-system -o yaml > bak.yaml
        ```

    1. Update the virtnest CRDs.

        ```shell
        kubectl apply -f ./crds
        ```

    1. Run `helm upgrade`.

        Before upgrading, it is recommended to replace the `global.imageRegistry` field
        in __bak.yaml__ with the current container registry address.

        ```shell
        export imageRegistry={your container registry}
        ```

        ```shell
        helm upgrade virtnest . \
          -n virtnest-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
        ```
