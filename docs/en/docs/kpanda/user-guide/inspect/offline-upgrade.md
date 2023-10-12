# Offline Upgrade of Cluster Inspection Module

This page explains how to install or upgrade the cluster inspection module after [downloading it from the Download Center](../../../download/modules/kcollie.md).

!!! info

    The term `kocllie` mentioned in the following commands or scripts is the internal development codename for the cluster inspection module.

## Loading Images from the Downloaded Package

You can load the images in one of the following two ways. If there is an image repository in your environment, it is recommended to choose chart-syncer to synchronize the images to the image repository as it is more efficient and convenient.

#### Option 1: Synchronize Images with chart-syncer

Using chart-syncer, you can upload the charts from the downloaded package along with their dependent image packages to the image repository and Helm repository used by the installer.

First, locate a node (such as a spark node) that can connect to both the image repository and the Helm repository. On this node, create a `load-image.yaml` configuration file and fill in the necessary information about the image repository and the Helm repository.

1. Create `load-image.yaml` file.

    !!! note

        All parameters in this YAML file are mandatory.

    === "Helm repo already added"

        If a chart repo is already installed in the current environment, chart-syncer also supports exporting the chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: kocllie # Path where the `load-image.yaml` file is executed on the node.
        target:
          containerRegistry: 10.16.10.111 # Image repository address
          containerRepository: release.daocloud.io/kocllie # Image repository path
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
          intermediateBundlesPath: kocllie # Path where the `load-image.yaml` file is executed on the node.
        target:
          containerRegistry: 10.16.10.111 # Image repository URL
          containerRepository: release.daocloud.io/kocllie # Image repository path
          repo:
            kind: LOCAL
            path: ./local-repo # Local path to the chart
          containers:
            auth:
              username: "admin" # Image repository username
              password: "Harbor12345" # Image repository password
        ```

2. Run the command to synchronize the images.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

#### Option 2: Load Images using Docker or containerd

Unzip and load the image files.

1. Unzip the tar package.

    ```shell
    tar xvf kocllie.bundle.tar
    ```

    After successful extraction, you will have three files:

    - hints.yaml
    - images.tar
    - original-chart

2. Load the images from the tar file into Docker or containerd.

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr image import images.tar
        ```

!!! note

    Each node needs to perform Docker or containerd image loading operation.
    After the loading is complete, tag the images to match the registry and repository used during installation.

## Upgrade

There are two upgrade methods. You can choose the corresponding upgrade approach based on the prerequisite operations:

=== "Upgrade via helm repo"

    1. Check if the cluster inspection Helm repository exists.

        ```shell
        helm repo list | grep kocllie
        ```

        If the result is empty or shows the following prompt, proceed to the next step; otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    2. Add the cluster inspection Helm repository.

        ```shell
        heml repo add kocllie http://{harbor url}/chartrepo/{project}
        ```

    3. Update the cluster inspection Helm repository.

        ```shell
        helm repo update kocllie
        ```

    4. Select the version of cluster inspection module you want to install (it is recommended to install the latest version).

        ```shell
        helm search repo kocllie/kocllie --versions
        ```

        ```none
        [root@master ~]# helm search repo kocllie/kocllie --versions
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        kocllie/kocllie  0.20.0          v0.20.0       A Helm chart for kocllie
        ...
        ```

    5. Backup `--set` parameters.

        Before upgrading the cluster inspection module, it is recommended to execute the following command to backup the `--set` parameters of the previous version.

        ```shell
        helm get values kocllie -n kocllie-system -o yaml > bak.yaml
        ```

    6. Update kocllie crds.

        ```shell
        helm pull kocllie/kocllie --version 0.6.0 && tar -zxf kocllie-0.6.0.tgz
        kubectl apply -f kocllie/crds
        ```

    7. Execute `helm upgrade`.

        Before the upgrade, it is recommended to modify the `global.imageRegistry` field in the `bak.yaml` file to the current image repository address being used.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade kocllie kocllie/kocllie \
          -n kocllie-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.6.0
        ```

=== "Upgrade via chart package"

    1. Backup `--set` parameters.

        Before upgrading the cluster inspection module, it is recommended to execute the following command to backup the `--set` parameters of the previous version.

        ```shell
        helm get values kocllie -n kocllie-system -o yaml > bak.yaml
        ```

    2. Update kocllie crds.

        ```shell
        kubectl apply -f ./crds
        ```

    3. Execute `helm upgrade`.

        Before the upgrade, it is recommended to modify the `global.imageRegistry` field in the `bak.yaml` file to the current image repository address being used.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade kocllie . \
          -n kocllie-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
        ```
