# Offline Upgrade of Security Management Module

This page explains how to install or upgrade the security management module after downloading it from the [Download Center](../../../download/index.md).

!!! info

    The term `dowl` appearing in the following commands or scripts is the internal development codename for the security management module.

## Loading Images from the Downloaded Package

You can load the images using one of the following two methods. It is recommended to use chart-syncer to sync the images to the image repository when an image repository exists in the environment as it is more efficient and convenient.

#### Method 1: Syncing Images Using chart-syncer

By using chart-syncer, you can upload the charts from the downloaded package along with their dependent image packages to the image repository and Helm repository used by the installer to deploy DCE.

First, find a node that can connect to both the image repository and the Helm repository (such as the spark node). On this node, create a `load-image.yaml` configuration file and fill in the necessary information like the image repository and Helm repository configurations.

1. Create `load-image.yaml`

    !!! note  

        All parameters in this YAML file are mandatory.

    === "Helm repo already added"

        If a chart repo has already been installed in the current environment, chart-syncer also supports exporting the chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: dowl # Path where the load-image.yaml file is executed on the node.
        target:
          containerRegistry: 10.16.10.111 # Image repository address
          containerRepository: release.daocloud.io/dowl # Image repository path
          repo:
            kind: HARBOR # Helm Chart repository type
            url: http://10.16.10.111/chartrepo/release.daocloud.io # Helm repository address
            auth:
              username: "admin" # Image repository username
              password: "Harbor12345" # Image repository password
          containers:
            auth:
              username: "admin" # Helm repository username
              password: "Harbor12345" # Helm repository password
        ```

    === "Helm repo not added"

        If there is no helm repo added on the current node, chart-syncer also supports exporting the chart as a tgz file and storing it in the specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: dowl # Path where the load-image.yaml file is executed on the node.
        target:
          containerRegistry: 10.16.10.111 # Image repository url
          containerRepository: release.daocloud.io/dowl # Image repository path
          repo:
            kind: LOCAL
            path: ./local-repo # Local chart path
          containers:
            auth:
              username: "admin" # Image repository username
              password: "Harbor12345" # Image repository password
        ```

2. Execute the image sync command.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

#### Method 2: Loading Images Using Docker or containerd

Uncompress and load the image files.

1. Uncompress the tar bundle.

    ```shell
    tar xvf dowl.bundle.tar
    ```

    After successful decompression, you will have three files:

    - hints.yaml
    - images.tar
    - original-chart

2. Load the images from the local directory into Docker or containerd.

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr image import images.tar
        ```

!!! note

    Each node needs to perform the Docker or containerd image loading operation,
    After loading is complete, tag the images to keep the Registry and Repository consistent with the installation.

## Upgrade

There are two methods for upgrading. Choose the corresponding upgrade method based on the pre-operation:

=== "Upgrade via helm repo"

    1. Check if the security management Helm repository exists.

        ```shell
        helm repo list | grep dowl
        ```

        If the result is empty or shows the following message, proceed to the next step; otherwise, skip to the next step.

        ```none
        Error: no repositories to show
        ```

    2. Add the security management Helm repository.

        ```shell
        helm repo add dowl http://{harbor url}/chartrepo/{project}
        ```

    3. Update the security management Helm repository.

        ```shell
        helm repo update dowl
        ```

        1. If the helm version is too low, it may cause a failure. If it fails, try executing `helm update repo`.

    4. Select the security management version you want to install (it is recommended to install the latest version).

        ```shell
        helm search repo dowl/dowl --versions
        ```

        ```none
        [root@master ~]# helm search repo dowl/dowl --versions
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        dowl/dowl  0.4.0          v0.4.0       A Helm chart for dowl
        ...
        ```

5. Backup the `--set` parameters.

    Before upgrading the security management version, it is recommended to execute the following command to backup the `--set` parameters of the old version.

    ```shell
    helm get values dowl -n dowl-system -o yaml > bak.yaml
    ```

6. Update dowl CRDs.

    ```shell
    helm pull dowl/dowl --version 0.4.0 && tar -zxf dowl-0.4.0.tgz
    kubectl apply -f dowl/crds
    ```

7. Execute `helm upgrade`.

    Before upgrading, it is recommended to replace the `global.imageRegistry` field in `bak.yaml` with the image repository address you are currently using.

    ```shell
    export imageRegistry={your_image_repository}
    ```

    ```shell
    helm upgrade dowl dowl/dowl \
      -n dowl-system \
      -f ./bak.yaml \
      --set global.imageRegistry=$imageRegistry \
      --version 0.4.0
    ```

=== "Upgrade via chart package"

    1. Backup the `--set` parameters.

        Before upgrading the security management version, it is recommended to execute the following command to backup the `--set` parameters of the old version.

        ```shell
        helm get values dowl -n dowl-system -o yaml > bak.yaml
        ```

    2. Update dowl CRDs.

        ```shell
        kubectl apply -f ./crds
        ```

    3. Execute `helm upgrade`.

        Before upgrading, it is recommended to replace the `global.imageRegistry` field in `bak.yaml` with the image repository address you are currently using.

        ```shell
        export imageRegistry={your_image_repository}
        ```

        ```shell
        helm upgrade dowl . \
          -n dowl-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
        ```
