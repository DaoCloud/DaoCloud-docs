# Offline Upgrade - Mongodb Module

This page explains how to install or upgrade the Mongodb module of the middleware after downloading it from the [Download Center](../../../download/index.md).

!!! info

    The term "mcamel" mentioned in the following commands or scripts is the internal development code name for the middleware module.

## Load Images from Installation Package

You can load the images using one of the following two methods. It is recommended to use chart-syncer to synchronize images to the image repository when a repository already exists in the environment, as it is more efficient and convenient.

### Synchronize Images to Image Repository using chart-syncer

1. Create `load-image.yaml`.

    !!! note

        All parameters in this YAML file are required. You need a private image repository and modify the relevant configurations.

    === "Installed chart repo"

        If there is already an installed chart repo in the current environment, chart-syncer can also export the chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mcamel-offline # path relative to the location where the charts-syncer command is executed, not relative to this YAML file and the offline package.
        target:
          containerRegistry: 10.16.10.111 # Replace with your image repository URL
          containerRepository: release.daocloud.io/mcamel # Replace with your image repository
          repo:
            kind: HARBOR # Can also be any other supported Helm Chart repository type
            url: http://10.16.10.111/chartrepo/release.daocloud.io # Replace with the chart repo URL
            auth:
              username: "admin" # Your image repository username
              password: "Harbor12345" # Your image repository password
          containers:
            auth:
              username: "admin" # Your image repository username
              password: "Harbor12345" # Your image repository password
        ```

    === "Uninstalled chart repo"

        If there is no installed chart repo in the current environment, chart-syncer can still export the chart as a tgz file and store it in the specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mcamel-offline # path relative to the location where the charts-syncer command is executed, not relative to this YAML file and the offline package.
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

1. Run the image synchronization command.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### Load Directly from Docker or containerd

Extract and load the image files.

1. Extract the tar archive.

    ```shell
    tar -xvf mcamel-mongodb_0.3.1_amd64.tar
    cd mcamel-mongodb_0.3.1_amd64
    tar -xvf mcamel-mongodb_0.3.1.bundle.tar
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

    Docker or containerd image loading operation should be performed on each node.
    After loading is complete, tag the images to keep the registry and repository consistent with the installation.

## Upgrade

There are two ways to upgrade. You can choose the corresponding upgrade method based on the pre-operation:

=== "Upgrade via helm repo"

    1. Check if the helm repository exists.

        ```shell
        helm repo list | grep mongodb
        ```

        If the result is empty or shows the following prompt, proceed to the next step. Otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    1. Add the helm repository.

        ```shell
        helm repo add mcamel-mongodb http://{harbor url}/chartrepo/{project}
        ```

    1. Update the helm repository.

        ```shell
        helm repo update mcamel/mcamel-mongodb # If the helm version is too low, this may fail. In that case, try executing `helm update repo` instead.
        ```

    1. Choose the version you want to install (it is recommended to install the latest version).

        ```shell
        helm search repo mcamel/mcamel-mongodb --versions
        ```

        ```none
        [root@master ~]# helm search repo mcamel/mcamel-mongodb --versions
        NAME                            CHART VERSION   APP VERSION     DESCRIPTION               
        mcamel/mcamel-mongodb     0.3.1           0.3.1           A Helm chart for Kubernetes
        ...
        ```

    1. Backup the `--set` parameters.

        Before upgrading to a new version, it is recommended to backup the `--set` parameters of the old version by executing the following command:

        ```shell
        helm get values mcamel-mongodb -n mcamel-system -o yaml > mcamel-mongodb.yaml
        ```

    1. Run `helm upgrade`.

        Before upgrading, it is recommended to replace the `global.imageRegistry` field in `mcamel-mongodb.yaml` with the image repository address you are currently using.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade mcamel-mongodb mcamel/mcamel-mongodb \
          -n mcamel-system \
          -f ./mcamel-mongodb.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.3.1
        ```

=== "Upgrade via chart package"

    1. Backup the `--set` parameters.

        Before upgrading to a new version, it is recommended to backup the `--set` parameters of the old version by executing the following command:

        ```shell
        helm get values mcamel-mongodb -n mcamel-system -o yaml > mcamel-mongodb.yaml
        ```

    1. Run `helm upgrade`.

        Before upgrading, it is recommended to replace the `global.imageRegistry` field in `mcamel-mongodb.yaml` with the image repository address you are currently using.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade mcamel-mongodb . \
          -n mcamel-system \
          -f ./mcamel-mongodb.yaml \
          --set global.imageRegistry=${imageRegistry} \
          --set console_image.registry=${imageRegistry} \ 
          --set operator_image.registry=${imageRegistry}
        ```
