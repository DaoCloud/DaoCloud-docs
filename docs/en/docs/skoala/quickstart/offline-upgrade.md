# Offline Upgrade

Components of DCE 5.0 are loosely coupled and can be installed/upgraded independently. This guide is intended for upgrading DaoCloud Microservice Engine (DME) after installing it with the [offline mode](../../install/commercial/start-install.md).

## Synch Image

After downloading the image to your local node, you need to sync the latest image version to your container registry via [chart-syncer ](https://github.com/bitnami-labs/charts-syncer) or a container runtime. chart-syncer is more recommended for its efficiency and convenience.

### Sync with chart-syncer

1. Create `load-image.yaml` as the chart-syncer profile

    All parameters in the `load-image.yaml` file are mandatory. You need a private container registry and modify configurations as described below. See [Official Doc](https://github.com/bitnami-labs/charts-syncer) for a detailed explanation of the chart-syncer profile.

    === "chart repo installed"

        If chart repo is already install, use the following configuration to synchronize the image directly.

        ```yaml
        source:
          intermediateBundlesPath: skoala-offline # Relative path to executing chart-syncer command, **not** the relative path between
        target:
          containerRegistry: 10.16.23.145 # Change to your container registry url
          containerRepository: release.daocloud.io/skoala # Change to your container registry
          repo:
            kind: HARBOR # Can be any of the supported Helm Chart registries
            url: http://10.16.23.145/chartrepo/release.daocloud.io # Change to chart repo url
            auth:
              username: "admin" # Your container registry username
              password: "Harbor12345" # Your container registry password
          containers:
            auth:
              username: "admin" # Your container registry username
              password: "Harbor12345" # Your image vault password
        ```

    === "chart repo not installed"

        Chart-syncer also supports exporting a chart as a `tgz` file in a specified path if chart repo is not installed.

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

        1. Relative path to executing chart-syncer command, **not** the relative path between this YAML file and the offline package
        2. Change to your container registry url
        3. Change to your container registry
        4. chart local path
        5. Your container registry username
        6. Your image vault password

2. Run this command to sync the image.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### Sync with Docker/containerd

1. Decompress the `tar` package.

    ```shell
    tar xvf skoala.bundle.tar
    ```

    After the decompression, you will get 3 files:

    - hints.yaml
    - images.tar
    - original-chart

2. Load the image from local to a Docker or containerd.

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr -n k8s.io image import images.tar
        ```

!!! note
    - The image needs to be loaded via Docker or containerd to each node.
    - After the loading is complete, you should tag the image to keep version consistency.

## Start Upgrade

After the image is synced, you can start upgrading DME.

=== "Upgrade through helm repo"

    1. Check if the helm repository of DME exists. `skoala` is the internal code for DME.

        ```shell
        helm repo list | grep skoala
        ```

        If nothing is returned or the following information is displayed, proceed to the next step. Otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    2. Add DME's helm repository.

        ```shell
        helm repo add skoala-release http://{harbor url}/chartrepo/{project}
        ```

    3. Update DME'S helm repository.

        ```shell
        helm repo update skoala-release # (1)
        ```

        1. If the helm version is outdated, it will fail. If it fails, try `helm update repo` command

    4. Select the version of DME you want to install (the latest version is recommended).

        ```shell
        helm search repo skoala-release/skoala --versions
        ```

        ```none
        [root@master ~]# helm search repo skoala-release/skoala --versions
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        skoala-release/skoala  0.14.0          v0.14.0       A Helm chart for Skoala
        ...
        ```

    5. Backup `--set` parameters.

        Before upgrading DME, it is recommended to run the following command to back up the `--set` parameters of the previous version.

        ```shell
        helm get values skoala -n skoala-system -o yaml > bak.yaml
        ```

    6. Run `helm upgrade`.

        Before upgrading, it is recommended to override the `global.imageRegistry` field in `bak.yaml` as the address of the container registry currently in use.

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

=== "Upgrade via chart"

    1. Backup `--set` parameters.

        Before upgrading DME, it is recommended to run the following command to back up the `--set` parameter of the old version.

        ```shell
        helm get values skoala -n skoala-system -o yaml > bak.yaml
        ```

    2. Run the `helm upgrade` command.

        Before upgrading, it is recommended that you override `global.imageRegistry` in `bak.yaml` as the address of the container registry currently in use.

        ```shell
        export imageRegistry={your image repo}
        ```

        ```shell
        helm upgrade skoala . \
        -n skoala-system \
        -f ./bak.yaml \
        --set global.imageRegistry=$imageRegistry
        ```
