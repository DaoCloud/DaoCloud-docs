# Offline Upgrade - Postgresql Module

This page explains how to install or upgrade the middleware - Postgresql module after downloading it from the [Download Center](../../../download/index.md).

!!! info

    The term `mcamel` used in the following commands or scripts is the internal development code name for the middleware module.

## Load Images from Installation Package

You can load the images using either of the two methods described below. It is recommended to choose the chart-syncer method if there is an image repository available in your environment, as it is more efficient and convenient.

### Sync Images to Image Repository using chart-syncer

1. Create `load-image.yaml`.

    !!! note

        All parameters in this YAML file are mandatory. You need to have a private image repository and modify the relevant configuration.

    === "Installed chart repo"

        If you have an installed chart repo in the current environment, chart-syncer also supports exporting charts as tgz files.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mcamel-offline # the relative path to where you execute the `charts-syncer` command, not the relative path between this YAML file and the offline package
        target:
          containerRegistry: 10.16.10.111 # replace with your image repository url
          containerRepository: release.daocloud.io/mcamel # replace with your image repository
          repo:
            kind: HARBOR # or any other supported Helm Chart repository type
            url: http://10.16.10.111/chartrepo/release.daocloud.io # replace with chart repo url
            auth:
              username: "admin" # your image repository username
              password: "Harbor12345" # your image repository password
          containers:
            auth:
              username: "admin" # your image repository username
              password: "Harbor12345" # your image repository password
        ```

    === "Uninstalled chart repo"

        If you don't have an installed chart repo in the current environment, chart-syncer also supports exporting charts as tgz files and storing them in the specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mcamel-offline # the relative path to where you execute the `charts-syncer` command, not the relative path between this YAML file and the offline package
        target:
          containerRegistry: 10.16.10.111 # replace with your image repository url
          containerRepository: release.daocloud.io/mcamel # replace with your image repository
          repo:
            kind: LOCAL
            path: ./local-repo # local path to the chart
          containers:
            auth:
              username: "admin" # your image repository username
              password: "Harbor12345" # your image repository password
        ```

2. Run the command to sync the images.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### Load Directly from Docker or containerd

Extract and load the image files.

1. Extract the tar archive.

    ```shell
    tar -xvf mcamel-postgresql_0.5.1_amd64.tar
    cd mcamel-postgresql_0.5.1_amd64
    tar -xvf mcamel-postgresql_0.5.1.bundle.tar
    ```

    After successful extraction, you will have three files:

    - hints.yaml
    - images.tar
    - original-chart

2. Load the images to Docker or containerd from the local directory.

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr -n k8s.io image import images.tar
        ```

!!! note

    Docker or containerd image loading operations need to be performed on each node.
    After loading is complete, tag the images to maintain consistency with the Registry and Repository used during installation.

## Upgrade

There are two ways to upgrade. You can choose the corresponding upgrade method based on the prerequisite operations:

=== "Upgrade via helm repo"

    1. Check if the helm repository exists.

        ```shell
        helm repo list | grep postgresql
        ```

        If the result is empty or shows the following prompt, proceed to the next step; otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    1. Add the helm repository.

        ```shell
        helm repo add mcamel-postgresql http://{harbor url}/chartrepo/{project}
        ```

    1. Update the helm repository.

        ```shell
        helm repo update mcamel/mcamel-postgresql # This may fail if the helm version is too low. In that case, try executing `helm update repo` instead.
        ```
  
    1. Select the version you want to install (we recommend installing the latest version).

        ```shell
        helm search repo mcamel/mcamel-postgresql --versions
        ```

        ```none
        [root@master ~]# helm search repo mcamel/mcamel-postgresql --versions
        NAME                            CHART VERSION   APP VERSION     DESCRIPTION               
        mcamel/mcamel-postgresql     0.5.1           0.5.1           A Helm chart for Kubernetes
        ...
        ```

    1. Backup the `--set` parameters.

        Before upgrading the version, it is recommended to execute the following command to backup the `--set` parameters of the old version.

        ```shell
        helm get values mcamel-postgresql -n mcamel-system -o yaml > mcamel-postgresql.yaml
        ```

    1. Run `helm upgrade`.

        Before upgrading, it is recommended to replace the `global.imageRegistry` field in `mcamel-postgresql.yaml` with the address of the image repository you are currently using.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade mcamel-postgresql mcamel/mcamel-postgresql \
          -n mcamel-system \
          -f ./mcamel-postgresql.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.5.1
        ```

=== "Upgrade via chart package"

    1. Backup the `--set` parameters.

        Before upgrading the version, it is recommended to execute the following command to backup the `--set` parameters of the old version.

        ```shell
        helm get values mcamel-postgresql -n mcamel-system -o yaml > mcamel-postgresql.yaml
        ```

    1. Run `helm upgrade`.

        Before upgrading, it is recommended to replace the `global.imageRegistry` field in `mcamel-postgresql.yaml` with the address of the image repository you are currently using.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade mcamel-postgresql . \
          -n mcamel-system \
          -f ./mcamel-postgresql.yaml \
          --set global.imageRegistry=${imageRegistry} \
          --set console_image.registry=${imageRegistry} \ 
          --set operator_image.registry=${imageRegistry}
        ```
