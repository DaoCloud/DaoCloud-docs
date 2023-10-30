# Offline Upgrade Middleware - RabbitMQ Module

This page explains how to install or upgrade the Middleware - RabbitMQ module after downloading it from the [Download Center](../../../download/index.md).

!!! info

    The term `mcamel` mentioned in the following commands or scripts is the internal development code name of the middleware module.

## Load Images from Installation Package

You can load the images in one of the following two ways. When an image repository exists in the environment, it is recommended to choose the chart-syncer to synchronize images to the image repository as it is more efficient and convenient.

### Synchronize Images to Image Repository Using chart-syncer

1. Create `load-image.yaml`.

    !!! note

        All parameters in this YAML file are required. You need a private image repository and modify the relevant configuration.

    === "Installed Chart Repo"

        If the current environment has installed a chart repo, chart-syncer also supports exporting the chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mcamel-offline # This is the relative path to execute the charts-syncer command, not the relative path between this YAML file and the offline package.
        target:
          containerRegistry: 10.16.10.111 # Change it to your image repository URL
          containerRepository: release.daocloud.io/mcamel # Change it to your image repository
          repo:
            kind: HARBOR # It can also be any other supported Helm Chart repository category
            url: http://10.16.10.111/chartrepo/release.daocloud.io # Change it to the chart repo URL
            auth:
            username: "admin" # Your image repository username
            password: "Harbor12345" # Your image repository password
          containers:
            auth:
              username: "admin" # Your image repository username
              password: "Harbor12345" # Your image repository password
        ```

    === "Not Installed Chart Repo"

        If the current environment has not installed a chart repo, chart-syncer also supports exporting the chart as a tgz file and storing it in the specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mcamel-offline # This is the relative path to execute the charts-syncer command, not the relative path between this YAML file and the offline package.
        target:
          containerRegistry: 10.16.10.111 # Change it to your image repository URL
          containerRepository: release.daocloud.io/mcamel # Change it to your image repository
          repo:
            kind: LOCAL
            path: ./local-repo # Local path of the chart
          containers:
            auth:
              username: "admin" # Your image repository username
              password: "Harbor12345" # Your image repository password
        ```

1. Run the command to synchronize images.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### Load Directly from Docker or containerd

Unpack and load the image files.

1. Extract the tar archive.

    ```shell
    tar -xvf mcamel-rabbitmq_0.13.1_amd64.tar
    cd mcamel-rabbitmq_0.13.1_amd64
    tar -xvf mcamel-rabbitmq_0.13.1.bundle.tar
    ```

    After successful extraction, you will have 3 files:

    - hints.yaml
    - images.tar
    - original-chart

2. Load the images from the local directory to Docker or containerd.

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr -n k8s.io image import images.tar
        ```

!!! note

    Each node needs to perform Docker or containerd image loading operations.
    After loading is complete, tag the images to keep the Registry and Repository consistent with the installation.

## Upgrade

There are two ways to upgrade. You can choose the corresponding upgrade method according to the pre-operation:

=== "Upgrade via helm repo"

    1. Check if the helm repository exists.

        ```shell
        helm repo list | grep rabbitmq
        ```

        If the result is empty or shows the following prompt, proceed to the next step; otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    1. Add the helm repository.

        ```shell
        helm repo add mcamel-rabbitmq http://{harbor url}/chartrepo/{project}
        ```

    1. Update the helm repository.

        ```shell
        helm repo update mcamel/mcamel-rabbitmq # If the helm version is too old, it may fail. In that case, try executing `helm update repo`.
        ```

    1. Choose the version you want to install (recommended to install the latest version).

        ```shell
        helm search repo mcamel/mcamel-rabbitmq --versions
        ```

        ```none
        [root@master ~]# helm search repo mcamel/mcamel-rabbitmq --versions
        NAME                            CHART VERSION   APP VERSION     DESCRIPTION               
        mcamel/mcamel-rabbitmq     0.13.1           0.13.1           A Helm chart for Kubernetes
        ...
        ```

    1. Backup the `--set` parameters.

        Before upgrading the version, it is recommended to execute the following command to back up the `--set` parameters of the old version.

        ```shell
        helm get values mcamel-rabbitmq -n mcamel-system -o yaml > mcamel-rabbitmq.yaml
        ```

    1. Run `helm upgrade`.

        Before upgrading, it is recommended to replace the `global.imageRegistry` field in mcamel-rabbitmq.yaml with the URL of the image repository you are currently using.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade mcamel-rabbitmq mcamel/mcamel-rabbitmq \
          -n mcamel-system \
          -f ./mcamel-rabbitmq.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.13.1
        ```

=== "Upgrade via chart package"

    1. Backup the `--set` parameters.

        Before upgrading the version, it is recommended to execute the following command to back up the `--set` parameters of the old version.

        ```shell
        helm get values mcamel-rabbitmq -n mcamel-system -o yaml > mcamel-rabbitmq.yaml
        ```

    1. Run `helm upgrade`.

        Before upgrading, it is recommended to replace the `global.imageRegistry` field in mcamel-rabbitmq.yaml with the URL of the image repository you are currently using.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade mcamel-rabbitmq . \
          -n mcamel-system \
          -f ./mcamel-rabbitmq.yaml \
          --set global.imageRegistry=${imageRegistry} \
          --set console_image.registry=${imageRegistry} \ 
          --set operator_image.registry=${imageRegistry}
        ```
