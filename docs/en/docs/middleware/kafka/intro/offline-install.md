# Offline Upgrade of Middleware - Kafka Module

This page explains how to install or upgrade the middleware - kafka module after downloading it from the [Download Center](../../../download/index.md).

!!! info

    The term __mcamel__ used in the following commands or scripts is an internal development codename for the middleware module.

## Loading Images from the Installation Package

You can load the images using one of the following methods. It is recommended to use chart-syncer to sync the images to your image repository when it is available, as it is more efficient and convenient.

### Syncing Images to Image Repository using chart-syncer

1. Create __load-image.yaml__ file.

    !!! note  

        All parameters in this YAML file are required. You need to have a private image repository and modify the relevant configuration.

    === "Chart Repo Installed"

        If you already have a chart repo installed in your environment, chart-syncer also supports exporting the chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mcamel-offline # The relative path to execute the charts-syncer command, not the relative path between this YAML file and the offline package
        target:
          containerRegistry: 10.16.10.111 # Change this to your image repository URL
          containerRepository: release.daocloud.io/mcamel # Change this to your image repository
          repo:
            kind: HARBOR # It can also be any other supported Helm Chart repository type
            url: http://10.16.10.111/chartrepo/release.daocloud.io # Change this to the chart repo URL
            auth:
              username: "admin" # Your image repository username
              password: "Harbor12345" # Your image repository password
          containers:
            auth:
              username: "admin" # Your image repository username
              password: "Harbor12345" # Your image repository password
        ```

    === "Chart Repo Not Installed"

        If you don't have a chart repo installed in your environment, chart-syncer also supports exporting the chart as a tgz file and storing it in the specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mcamel-offline # The relative path to execute the charts-syncer command, not the relative path between this YAML file and the offline package
        target:
          containerRegistry: 10.16.10.111 # Change this to your image repository URL
          containerRepository: release.daocloud.io/mcamel # Change this to your image repository
          repo:
            kind: LOCAL
            path: ./local-repo # Local path to the chart
          containers:
            auth:
              username: "admin" # Your image repository username
              password: "Harbor12345" # Your image repository password
        ```

1. Run the command to sync the images.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### Directly Loading with Docker or containerd

Unpack and load the image files.

1. Extract the tar archive.

    ```shell
    tar -xvf mcamel-kafka_0.8.1_amd64.tar
    cd mcamel-kafka_0.8.1_amd64
    tar -xvf mcamel-kafka_0.8.1.bundle.tar
    ```

    After successful extraction, you will get 3 files:

    - hints.yaml
    - images.tar
    - original-chart

1. Load the images to Docker or containerd from local.

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr -n k8s.io image import images.tar
        ```

!!! note

    Docker or containerd image loading operation needs to be performed on each node.
    After loading, tag the images to match the registry and repository used during installation.

## Upgrade

There are two ways to perform the upgrade. You can choose the corresponding upgrade method based on the preconditions:

=== "Upgrade through helm repo"

    1. Check if the helm repository exists.

        ```shell
        helm repo list | grep kafka
        ```

        If the result is empty or shows the following prompt, proceed to the next step; otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    1. Add the helm repository.

        ```shell
        helm repo add mcamel-kafka http://{harbor url}/chartrepo/{project}
        ```

    1. Update the helm repository.

        ```shell
        helm repo update mcamel/mcamel-kafka # If the helm version is too low and it fails, try executing __helm update repo__ 
        ```

    1. Select the version you want to install (recommended to install the latest version).

        ```shell
        helm search repo mcamel/mcamel-kafka --versions
        ```

        ```none
        [root@master ~]# helm search repo mcamel/mcamel-kafka --versions
        NAME                            CHART VERSION   APP VERSION     DESCRIPTION               
        mcamel/mcamel-kafka     0.8.1           0.8.1           A Helm chart for Kubernetes
        ...
        ```

    1. Back up the `--set` parameters.

        Before upgrading to a new version, it is recommended to execute the following command to back up the `--set` parameters of the old version.

        ```shell
        helm get values mcamel-kafka -n mcamel-system -o yaml > mcamel-kafka.yaml
        ```

    1. Run `helm upgrade` .

        Before upgrading, it is recommended to update the  `global.imageRegistry` field in the __mcamel-kafka.yaml__ file with the current image repository address.

        ```shell
        export imageRegistry={your_image_repository}
        ```

        ```shell
        helm upgrade mcamel-kafka mcamel/mcamel-kafka \
          -n mcamel-system \
          -f ./mcamel-kafka.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.8.1
        ```

=== "Upgrade through chart package"

    1. Back up the `--set` parameters.

        Before upgrading to a new version, it is recommended to execute the following command to back up the `--set` parameters of the old version.

        ```shell
        helm get values mcamel-kafka -n mcamel-system -o yaml > mcamel-kafka.yaml
        ```

    1. Run `helm upgrade` .

        Before upgrading, it is recommended to update the __bak.yaml__ file by replacing  `global.imageRegistry` with your current image repository address.

        ```shell
        export imageRegistry={your_image_repository}
        ```

        ```shell
        helm upgrade mcamel-kafka . \
          -n mcamel-system \
          -f ./mcamel-kafka.yaml \
          --set global.imageRegistry=${imageRegistry} \
          --set console_image.registry=${imageRegistry} \ 
          --set operator_image.registry=${imageRegistry}
        ```
