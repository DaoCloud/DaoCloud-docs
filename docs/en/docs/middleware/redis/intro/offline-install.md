# Offline Upgrade - Redis Module

This page explains how to install or upgrade the Redis module of the middleware after downloading it from the [Download Center](../../../download/index.md).

!!! info

    The term __mcamel__ mentioned in the following commands or scripts is the internal development codename for the middleware module.

## Load Images from Installation Package

You can load the images from the installation package using one of the following two methods. It is recommended to use the chart-syncer tool to sync images to the image repository when a repository exists in the environment as it is more efficient and convenient.

### Sync Images to Image Repository using chart-syncer

1. Create __load-image.yaml__ .

    !!! note

        All parameters in this YAML file are required. You need a private image repository and modify the relevant configurations.

    === "Installed Chart Repo"

        If a chart repo is already installed in the current environment, chart-syncer also supports exporting the chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mcamel-offline # The relative path to execute the charts-syncer command, not the relative path between this YAML file and the offline package.
        target:
          containerRegistry: 10.16.10.111 # Replace with your image repository URL
          containerRepository: release.daocloud.io/mcamel # Replace with your image repository
          repo:
            kind: HARBOR # Can be any other supported Helm Chart repository type
            url: http://10.16.10.111/chartrepo/release.daocloud.io # Replace with chart repo URL
            auth:
              username: "admin" # Your image repository username
              password: "Harbor12345" # Your image repository password
          containers:
            auth:
              username: "admin" # Your image repository username
              password: "Harbor12345" # Your image repository password
        ```

    === "Uninstalled Chart Repo"

        If a chart repo is not installed in the current environment, chart-syncer also supports exporting the chart as a tgz file and storing it in the specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mcamel-offline # The relative path to execute the charts-syncer command, not the relative path between this YAML file and the offline package.
        target:
          containerRegistry: 10.16.10.111 # Replace with your image repository URL
          containerRepository: release.daocloud.io/mcamel # Replace with your image repository
          repo:
            kind: LOCAL
            path: ./local-repo # Local path of the chart
          containers:
            auth:
              username: "admin" # Your image repository username
              password: "Harbor12345" # Your image repository password
        ```

1. Run the command to sync images.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### Directly Load Images using Docker or containerd

Extract and load the image files.

1. Extract the tar archive.

    ```shell
    tar -xvf mcamel-redis_0.11.1_amd64.tar
    cd mcamel-redis_0.11.1_amd64
    tar -xvf mcamel-redis_0.11.1.bundle.tar
    ```

    After the extraction, you will have three files:

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

    Docker or containerd image loading operation should be performed on each node.
    After loading, remember to tag the images to keep the registry and repository consistent with the installation.

## Upgrade

There are two ways to upgrade. You can choose the corresponding upgrade method based on the pre-requisites:

=== "Upgrade via helm repo"

    1. Check if the helm repository exists.

        ```shell
        helm repo list | grep redis
        ```

        If it returns empty or shows the following prompt, proceed to the next step. Otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    1. Add the helm repository.

        ```shell
        helm repo add mcamel-redis http://{harbor url}/chartrepo/{project}
        ```

    1. Update the helm repository.

        ```shell
        helm repo update mcamel/mcamel-redis # If the helm version is too low, the update may fail. In that case, try executing __helm update repo__ instead.
        ```
    
    1. Choose the version you want to install (it is recommended to install the latest version).

        ```shell
        helm search repo mcamel/mcamel-redis --versions
        ```

        ```none
        [root@master ~]# helm search repo mcamel/mcamel-redis --versions
        NAME                            CHART VERSION   APP VERSION     DESCRIPTION               
        mcamel/mcamel-redis             0.11.1           0.11.1           A Helm chart for Kubernetes
        ...
        ```

    1. Back up the `--set` parameters.

        Before upgrading the version, it is recommended to execute the following command to back up the `--set` parameters of the old version.

        ```shell
        helm get values mcamel-redis -n mcamel-system -o yaml > mcamel-redis.yaml
        ```

    1. Run `helm upgrade` .

        Before upgrading, it is suggested to replace the  `global.imageRegistry` field in __mcamel-redis.yaml__ with the image repository address you are currently using.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade mcamel-redis mcamel/mcamel-redis \
          -n mcamel-system \
          -f ./mcamel-redis.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.11.1
        ```


=== "Upgrade via chart package"

    1. Back up the `--set` parameters.

        Before upgrading the version, it is recommended to execute the following command to back up the `--set` parameters of the old version.

        ```shell
        helm get values mcamel-redis -n mcamel-system -o yaml > mcamel-redis.yaml
        ```

    1. Run `helm upgrade` .

        Before upgrading, it is suggested to replace the  `global.imageRegistry` field in __bak.yaml__ with the image repository address you are currently using.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade mcamel-redis . \
          -n mcamel-system \
          -f ./mcamel-redis.yaml \
          --set global.imageRegistry=${imageRegistry} \
          --set console_image.registry=${imageRegistry} \ 
          --set operator_image.registry=${imageRegistry}
        ```
