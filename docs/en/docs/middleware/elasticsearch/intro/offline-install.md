# Offline Upgrade of Middleware - ElasticSearch Module

This page explains how to install or upgrade the ElasticSearch module of the Middleware after downloading it from the [Download Center](../../../download/index.md).

!!! info

    The term `mcamel` used in the following commands or scripts is the internal development code name for the Middleware module.

## Loading Images from Installation Package

You can load the images using one of the following two methods. It is recommended to use chart-syncer to sync the images to your image repository when there is an image repository available, as it is more efficient and convenient.

### Syncing Images to Image Repository Using chart-syncer

1. Create `load-image.yaml` file.

    !!! note  

        All the parameters in this YAML file are mandatory. You need to have a private image repository and modify the relevant configurations.

    === "Installed chart repo"

        If you have already installed a chart repo in your environment, chart-syncer also supports exporting a chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mcamel-offline # The relative path to where the charts-syncer command will be executed, not the relative path between this YAML file and the offline package
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

    === "Uninstalled chart repo"

        If you haven't installed a chart repo in your environment, chart-syncer also supports exporting a chart as a tgz file and storing it in the specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mcamel-offline # The relative path to where the charts-syncer command will be executed, not the relative path between this YAML file and the offline package
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

2. Run the command to sync the images.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### Directly Loading with Docker or containerd

Extract and load the image files.

1. Extract the tar archive.

    ```shell
    tar -xvf mcamel-elasticsearch_0.10.1_amd64.tar
    cd mcamel-elasticsearch_0.10.1_amd64
    tar -xvf mcamel-elasticsearch_0.10.1.bundle.tar
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

    Each node needs to perform the Docker or containerd image loading operation.
    After loading is complete, tag the images to match the Registry and Repository used during installation.

## Upgrade

There are two methods to upgrade. Choose the corresponding upgrade method based on the pre-operation you performed:

=== "Upgrade through helm repo"

    1. Check if the Helm repository exists.

        ```shell
        helm repo list | grep elasticsearch
        ```

        If the result is empty or shows the following prompt, proceed to the next step; otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    1. Add the Helm repository.

        ```shell
        helm repo add mcamel-elasticsearch http://{harbor url}/chartrepo/{project}
        ```

    1. Update the Helm repository.

        ```shell
        helm repo update mcamel/mcamel-elasticsearch # If the update fails due to a low helm version, try executing `helm update repo` instead.
        ```

1. Choose the version you want to install (it is recommended to install the latest version).

    ```shell
    helm search repo mcamel/mcamel-elasticsearch --versions
    ```

    ```none
    [root@master ~]# helm search repo mcamel/mcamel-elasticsearch --versions
    NAME                            CHART VERSION   APP VERSION     DESCRIPTION               
    mcamel/mcamel-elasticsearch     0.10.1           0.10.1           A Helm chart for Kubernetes
    ...
    ```

1. Backup the `--set` parameters.

    Before upgrading to a new version, it is recommended to execute the following command to backup the `--set` parameters of the old version.

    ```shell
    helm get values mcamel-elasticsearch -n mcamel-system -o yaml > mcamel-elasticsearch.yaml
    ```

1. Run `helm upgrade`.

    Before upgrading, it is recommended to replace the `global.imageRegistry` field in `mcamel-elasticsearch.yaml` with the URL of the image repository you are currently using.

    ```shell
    export imageRegistry={your image repository}
    ```

    ```shell
    helm upgrade mcamel-elasticsearch mcamel/mcamel-elasticsearch \
      -n mcamel-system \
      -f ./mcamel-elasticsearch.yaml \
      --set global.imageRegistry=$imageRegistry \
      --version 0.10.1
    ```
    
=== "Upgrade through chart package"

    1. Backup the `--set` parameters.

        Before upgrading to a new version, it is recommended to execute the following command to backup the `--set` parameters of the old version.

        ```shell
        helm get values mcamel-elasticsearch -n mcamel-system -o yaml > mcamel-elasticsearch.yaml
        ```

    1. Run `helm upgrade`.

        Before upgrading, it is recommended to replace the `global.imageRegistry` field in `mcamel-elasticsearch.yaml` with the URL of the image repository you are currently using.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade mcamel-elasticsearch . \
          -n mcamel-system \
          -f ./mcamel-elasticsearch.yaml \
          --set global.imageRegistry=${imageRegistry} \
          --set console_image.registry=${imageRegistry} \ 
          --set operator_image.registry=${imageRegistry}
        ```
