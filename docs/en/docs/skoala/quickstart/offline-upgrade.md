# Upgrade the microservice engine offline

Each DCE 5.0 module is loosely coupled and supports independent installation and upgrade of each module. This document is intended for upgrades that occur after the microservice engine is installed offline.

## Synchronous mirror

After downloading the image to the local node, you need to sync the latest version of the image to your image repository via [ chart-syncer ](https://github.com/bitnami-labs/charts-syncer) or the container runtime. chart-syncer synchronous mirroring is recommended because it is more efficient and convenient.

### chart-syncer synchronous image

1. Create `load-image.yaml` as a chart-syncer profile using the following

     `load-image.yaml` All parameters in the file are mandatory. You need a private Container registry and modify the configurations as described below. See [Official Doc](https://github.com/bitnami-labs/charts-syncer) for a detailed explanation of the chart-syncer profile.

    === "chart repo installed"


        ```yaml
        source:
          intermediateBundlesPath: skoala-offline # (1)
        target:
          containerRegistry: 10.16.23.145 # (2)
          containerRepository: release.daocloud.io/skoala # (3)
          repo:
            kind: HARBOR # (4)
            url: http://10.16.23.145/chartrepo/release.daocloud.io # (5)
            auth:
            username: "admin" # (6)
            password: "Harbor12345" # (7)
          containers:
            auth:
              username: "admin" # (8)
              password: "Harbor12345" # (9)
        ```

        1. A relative path to the executing chart-syncer command, not a relative path between this YAML file and the offline package
        2. Change to your Container registry url
        3. Need to change to your Container registry
        4. It can also be any of the other supported Helm Chart registry categories
        5. Change to chart repo url
        6. Your container registry user name
        7. Your mirror vault password
        8. Your container registry user name
        9. Your mirror vault password

    === "chart repo not installed"

        Chart-syncer also supports exporting chart to a `tgz` file in a specified path if chart repo is not installed in your current environment.

        ```yaml
        source:
          intermediateBundlesPath: skoala-offline # (1)
        target:
          containerRegistry: 10.16.23.145 # (2)
          containerRepository: release.daocloud.io/skoala # (3)
          repo:
            kind: LOCAL
            path: ./local-repo # (4)
          containers:
            auth:
              username: "admin" # (5)
              password: "Harbor12345" # (6)
        ```

        1. A relative path to the executing chart-syncer command, not a relative path between this YAML file and the offline package
        2. Change to your Container registry url
        3. Need to change to your Container registry
        4. chart local path
        5. Your container registry user name
        6. Your mirror vault password

2. Run the mirror synchronization command.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### Docker/containerd Synchronizes images

1. Decompress the `tar` package.

    ```shell
    tar xvf skoala.bundle.tar
    ```

    After successful decompression, you will get 3 files:

    - hints.yaml
    - images.tar
    - original-chart

2. Load the image from the local to a Docker or containerd.

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr image import images.tar
        ```

!!! note
    - The image needs to be loaded via Docker or containerd on each node.
    - After the loading is complete, the tag image is required to keep Registry and Repository consistent with the installation.

## Start upgrading

After mirror synchronization is complete, you can start upgrading the microservice engine.

=== "Upgrade through helm repo"

    1. Check whether microservice engine helm repository exists.

        ```shell
        helm repo list | grep skoala
        ```

        If nothing is returned or the following information is displayed, proceed to the next step. Otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    2. Add helm repository for microservice engine.

        ```shell
        heml repo add skoala-release http://{harbor url}/chartrepo/{project}
        ```

    3. Update helm repository for microservice engine.

        ```shell
        helm repo update skoala-release # (1)
        ```

        1. If the helm version is too low, it will fail. If this fails, try running helm update repo

    4. Select the version of the microservice engine you want to install (the latest version is recommended).

        ```shell
        helm search repo skoala-release/skoala --versions
        ```

        ```none
        [root@master ~]# helm search repo skoala-release/skoala --versions
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        skoala-release/skoala  0.14.0          v0.14.0       A Helm chart for Skoala
        ...
        ```

    5. Backup `--set` Parameter.

        Before upgrading the micro service engine, you are advised to run the following command to back up the `--set` parameter of the previous version.

        ```shell
        helm get values skoala -n skoala-system -o yaml > bak.yaml
        ```

    6. Run `helm upgrade`.

        Before upgrading, it is recommended that you override the `global.imageRegistry` field in bak.yaml as the address of the image registry currently in use.

        ```shell
        export imageRegistry={your image repo}
        ```

        ```shell
        helm upgrade skoala skoala-release/skoala \
        -n skoala-system \
        -f ./bak.yaml \
        --set global.imageRegistry=$imageRegistry
        --version 0.14.0
        ```

=== "Upgrade via chart pack"

    1. Backup `--set` Parameter.

        Before upgrading the micro service engine, you are advised to run the following command to back up the `--set` parameter of the old version.

        ```shell
        helm get values skoala -n skoala-system -o yaml > bak.yaml
        ```

    2. Run the `helm upgrade` command.

        Before upgrading, it is recommended that you override `global.imageRegistry` in bak.yaml as the address of the image registry currently in use.

        ```shell
        export imageRegistry={your image repo}
        ```

        ```shell
        helm upgrade skoala . \
        -n skoala-system \
        -f ./bak.yaml \
        --set global.imageRegistry=$imageRegistry
        ```
