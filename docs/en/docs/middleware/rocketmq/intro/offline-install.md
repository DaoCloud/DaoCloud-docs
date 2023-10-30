# Offline Upgrade of Middleware - RocketMQ Module

This page explains how to install or upgrade the Middleware - RocketMQ module after downloading it from the [Download Center](../../../download/index.md).

!!! info

    The term `mcamel` mentioned in the following commands or scripts is the internal development code name for the middleware module.

## Loading Images from Installation Package

You can load the images in one of the following two ways. When a mirror repository exists in the environment, it is recommended to choose the method of using `chart-syncer` to synchronize the images to the mirror repository as it is more efficient and convenient.

### Synchronize Images to Mirror Repository using chart-syncer

1. Create `load-image.yaml`.

    !!! note  

        The parameters in this YAML file are all required. You need to have a private image repository and modify the relevant configurations.

    === "Chart Repo Installed"

        If the current environment has a chart repo installed, `chart-syncer` also supports exporting the chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mcamel-offline # The relative path to execute the `charts-syncer` command, not the relative path between this YAML file and the offline package.
        target:
          containerRegistry: 10.16.10.111 # Change it to your image repository URL
          containerRepository: release.daocloud.io/mcamel # Change it to your image repository
          repo:
            kind: HARBOR # It can also be any other supported Helm Chart repository type
            url: http://10.16.10.111/chartrepo/release.daocloud.io # Change it to your chart repo URL
            auth:
              username: "admin" # Your image repository username
              password: "Harbor12345" # Your image repository password
          containers:
            auth:
              username: "admin" # Your image repository username
              password: "Harbor12345" # Your image repository password
        ```
        
    === "Chart Repo Not Installed"

        If the current environment does not have a chart repo installed, `chart-syncer` also supports exporting the chart as a tgz file and storing it in the specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mcamel-offline # The relative path to execute the `charts-syncer` command, not the relative path between this YAML file and the offline package.
        target:
          containerRegistry: 10.16.10.111 # Change it to your image repository URL
          containerRepository: release.daocloud.io/mcamel # Change it to your image repository
          repo:
            kind: LOCAL
            path: ./local-repo # Local path to the chart
          containers:
            auth:
              username: "admin" # Your image repository username
              password: "Harbor12345" # Your image repository password
        ```

1. Run the image synchronization command.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### Load Directly from Docker or containerd

Unpack and load the image files.

1. Extract the tar archive.

    ```shell
    tar -xvf mcamel-rocketmq_0.1.0_amd64.tar
    cd mcamel-rocketmq_0.1.0_amd64
    tar -xvf mcamel-rocketmq_0.1.0.bundle.tar
    ```

    After successful extraction, you will have three files:

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

    Docker or containerd image loading operation needs to be performed on each node.
    After loading is complete, you need to tag the image to keep the registry and repository consistent with the installation.

## Upgrade

There are two ways to upgrade. You can choose the corresponding upgrade method based on the pre-requisite operations:

=== "Upgrade via Helm Repo"

    1. Check if the helm repository exists.

        ```shell
        helm repo list | grep rocketmq
        ```

        If the result is empty or shows the following prompt, proceed to the next step. Otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    1. Add the helm repository.

        ```shell
        helm repo add mcamel-rocketmq http://{harbor url}/chartrepo/{project}
        ```

    1. Update the helm repository.

        ```shell
        helm repo update mcamel/mcamel-rocketmq # If the Helm version is too low, it may fail. If it fails, try executing `helm update repo`.
        ```

    1. Choose the version you want to install (it is recommended to install the latest version).

        ```shell
        helm search repo mcamel/mcamel-rocketmq --versions
        ```

        ```none
        [root@master ~]# helm search repo mcamel/mcamel-rocketmq --versions
        NAME                            CHART VERSION   APP VERSION     DESCRIPTION               
        mcamel/mcamel-rocketmq     0.1.0           0.1.0           A Helm chart for Kubernetes
        ...
        ```

    1. Backup the `--set` parameters.

        Before upgrading the version, it is recommended to execute the following command to backup the `--set` parameters of the old version.

        ```shell
        helm get values mcamel-rocketmq -n mcamel-system -o yaml > mcamel-rocketmq.yaml
        ```

    1. Run `helm upgrade`.

        Before upgrading, it is recommended to replace the `global.imageRegistry` field in `mcamel-rocketmq.yaml` with the address of the image repository you are currently using.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade mcamel-rocketmq mcamel/mcamel-rocketmq \
          -n mcamel-system \
          -f ./mcamel-rocketmq.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.1.0
        ```


=== "Upgrade via Chart Package"

    1. Backup the `--set` parameters.

        Before upgrading the version, it is recommended to execute the following command to backup the `--set` parameters of the old version.

        ```shell
        helm get values mcamel-rocketmq -n mcamel-system -o yaml > mcamel-rocketmq.yaml
        ```

    1. Run `helm upgrade`.

        Before upgrading, it is recommended to replace the `global.imageRegistry` field in `mcamel-rocketmq.yaml` with the address of the image repository you are currently using.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade mcamel-rocketmq . \
          -n mcamel-system \
          -f ./mcamel-rocketmq.yaml \
          --set global.imageRegistry=${imageRegistry} \
          --set console_image.registry=${imageRegistry} \ 
          --set operator_image.registry=${imageRegistry}
        ```
