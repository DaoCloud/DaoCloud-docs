# Offline Upgrade Middleware - MySQL Module

This page explains how to install or upgrade the middleware - MySQL module after downloading it from the [Download Center](../../../download/index.md).

!!! info

    The term `mcamel` mentioned in the following commands or scripts is the internal development code name for the middleware module.

## Load Images from Installation Package

You can load the images using one of the following two methods. When an image repository exists in the environment, it is recommended to choose chart-syncer for synchronizing images to the image repository as it is more efficient and convenient.

### Synchronize Images to Image Repository using chart-syncer

1. Create `load-image.yaml`.

    !!! note

        All parameters in this YAML file are required. You need a private image repository and modify the relevant configurations.

    === "Chart Repo Installed"

        If the chart repo is already installed in the current environment, chart-syncer also supports exporting the chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mcamel-offline # Relative path to the directory where the charts-syncer command is executed, not the relative path between this YAML file and the offline package
        target:
          containerRegistry: 10.16.10.111 # Replace with your image repository URL
          containerRepository: release.daocloud.io/mcamel # Replace with your image repository
          repo:
            kind: HARBOR # It can also be any other supported Helm Chart repository type
            url: http://10.16.10.111/chartrepo/release.daocloud.io # Replace with the chart repo URL
            auth:
            username: "admin" # Your image repository username
            password: "Harbor12345" # Your image repository password
          containers:
            auth:
              username: "admin" # Your image repository username
              password: "Harbor12345" # Your image repository password
        ```

    === "Chart Repo Not Installed"

        If the chart repo is not installed in the current environment, chart-syncer also supports exporting the chart as a tgz file and storing it in the specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mcamel-offline # Relative path to the directory where the charts-syncer command is executed, not the relative path between this YAML file and the offline package
        target:
          containerRegistry: 10.16.10.111 # Replace with your image repository URL
          containerRepository: release.daocloud.io/mcamel # Replace with your image repository
          repo:
            kind: LOCAL
            path: ./local-repo # Local path to the chart
          containers:
            auth:
              username: "admin" # Your image repository username
              password: "Harbor12345" # Your image repository password
        ```

1. Run the command to synchronize the images.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### Directly Load using Docker or containerd

Unpack and load the image files.

1. Unpack the tar archive.

    ```shell
    tar -xvf mcamel-mysql_0.11.1_amd64.tar
    cd mcamel-mysql_0.11.1_amd64
    tar -xvf mcamel-mysql_0.11.1.bundle.tar
    ```

    After successful unpacking, you will get the following 3 files:

    - hints.yaml
    - images.tar
    - original-chart

2. Load the images from local to Docker or containerd.

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
    After loading is complete, the images need to be tagged to match the Registry and Repository used during installation.

## Upgrade

There are two ways to upgrade. You can choose the corresponding upgrade method based on the pre-operation:

=== "Upgrade via helm repo"

    1. Check if the helm repo exists.

        ```shell
        helm repo list | grep mysql
        ```

        If the result is empty or shows the following message, proceed to the next step; otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    1. Add a helm repo.

        ```shell
        helm repo add mcamel-mysql http://{harbor url}/chartrepo/{project}
        ```

    1. Update the helm repo.

        ```shell
        helm repo update mcamel/mcamel-mysql # If the helm version is too low, it may fail. In that case, try executing `helm update repo`.

    1. Select the version you want to install (it is recommended to install the latest version).

        ```shell
        helm search repo mcamel/mcamel-mysql --versions
        ```

        ```none
        [root@master ~]# helm search repo mcamel/mcamel-mysql --versions
        NAME                            CHART VERSION   APP VERSION     DESCRIPTION               
        mcamel/mcamel-mysql     0.11.1           0.11.1           A Helm chart for Kubernetes
        ...
        ```

    1. Backup the `--set` parameters.

        Before upgrading the version, it is recommended to execute the following command to back up the `--set` parameters of the previous version.

        ```shell
        helm get values mcamel-mysql -n mcamel-system -o yaml > mcamel-mysql.yaml
        ```

    1. Run `helm upgrade`.

        Before upgrading, it is recommended to replace the `global.imageRegistry` field in `mcamel-mysql.yaml` with the image repository address currently used.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade mcamel-mysql mcamel/mcamel-mysql \
          -n mcamel-system \
          -f ./mcamel-mysql.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.11.1
        ```


=== "Upgrade via chart package"

    1. Backup the `--set` parameters.

        Before upgrading the version, it is recommended to execute the following command to back up the `--set` parameters of the previous version.

        ```shell
        helm get values mcamel-mysql -n mcamel-system -o yaml > mcamel-mysql.yaml
        ```

    1. Run `helm upgrade`.

        Before upgrading, it is recommended to replace the `global.imageRegistry` field in `mcamel-mysql.yaml` with the image repository address currently used.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade mcamel-mysql . \
          -n mcamel-system \
          -f ./mcamel-mysql.yaml \
          --set global.imageRegistry=${imageRegistry} \
          --set console_image.registry=${imageRegistry} \ 
          --set operator_image.registry=${imageRegistry}
        ```
