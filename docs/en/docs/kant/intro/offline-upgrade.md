# Offline Upgrade Cloud Edge Collaboration Module

This page explains how to install or upgrade after [downloading the Cloud Edge Collaboration Module](../../download/modules/kant.md).

!!! info

    The __kant__ mentioned in the following commands or scripts is the internal development code name of the Cloud Edge Collaboration Module.

## Load Images from the Downloaded Installation Package

You can load images in one of the following two ways. When there is an image repository in the environment, it is recommended to choose the chart-syncer to synchronize the images to the image repository for more efficient and convenient installation.

### Use chart-syncer to Synchronize Images

Using chart-syncer allows you to upload the Chart and its dependent image packages from the downloaded installation package to the image repository and Helm repository used when deploying DCE with the installer.

First, find a node that can connect to the image repository and Helm repository (such as a fire node), create a load-image.yaml configuration file on the node, and fill in the configuration information such as the image repository and Helm repository.

1. Create load-image.yaml

    !!! note  

        All parameters in this YAML file are required.

    === "Helm repo already added"

        If a chart repo is already installed in the current environment, chart-syncer also supports exporting the chart to a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: kant # Path to run the load-image.yaml file on the node.
        target:
          containerRegistry: 10.16.10.111 # Image repository address
          containerRepository: release.daocloud.io/kant # Image repository path
          repo:
            kind: HARBOR # Type of Helm Chart repository
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

        If a helm repo is not added on the current node, chart-syncer also supports exporting the chart to a tgz file and storing it in a specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: kant # Path to run the load-image.yaml file on the node.
        target:
          containerRegistry: 10.16.10.111 # Image repository url
          containerRepository: release.daocloud.io/kant # Image repository path
          repo:
            kind: LOCAL
            path: ./local-repo # Local path of the chart
          containers:
            auth:
              username: "admin" # Image repository username
              password: "Harbor12345" # Image repository password
        ```

1. Run the command to synchronize images.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### Load Images Using Docker or containerd

Unpack and load the image files.

1. Unpack the tar compressed file.

    ```shell
    tar xvf kant.bundle.tar
    ```

    After successful unpacking, you will get 3 files:

    - hints.yaml
    - images.tar
    - original-chart

2. Load the images from the local to Docker or containerd.

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr -n k8s.io image import images.tar
        ```

!!! note

    Each node needs to perform the Docker or containerd image loading operation,
    After loading is complete, tag the images to keep the Registry, Repository consistent with the installation.

## Upgrade

There are two ways to upgrade. You can choose the corresponding upgrade solution based on the prerequisite operations:

=== "Upgrade via Helm Repo"

    1. Check if the Cloud Edge Collaboration Helm repository exists.

        ```shell
        helm repo list | grep kant-release
        ```

        If the result is empty or shows as below, proceed to the next step; otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    1. Add the Helm repository for Cloud Edge Collaboration.

        ```shell
        helm repo add kant-release http://{harbor url}/chartrepo/{project}
        ```

    1. Update the Helm repository for Cloud Edge Collaboration.

        ```shell
        helm repo update kant-release
        ```

    1. Choose the Cloud Edge Collaboration version you want to install (it is recommended to install the latest version).

        ```shell
        helm search repo kant-release/kant --versions
        ```

        The output will be similar to:

        ```none
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        kant-release/kant  0.5.0          v0.5.0       A Helm chart for kant
        ...
        ```

    1. Backup the `--set` parameters.

        Before upgrading the Cloud Edge Collaboration version, it is recommended to run the following command to back up the `--set` parameters of the old version.

        ```shell
        helm get values kant -n kant-system -o yaml > bak.yaml
        ```

    1. Update kant crds.

        ```shell
        helm pull kant-release/kant --version 0.5.0 && tar -zxf kant-0.5.0.tgz
        kubectl apply -f kant/crds
        ```

    1. Run `helm upgrade`.

        Before upgrading, it is recommended to modify the __global.imageRegistry__ field in bak.yaml to the current image repository address.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade kant-release kant-release/kant \
          -n kant-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.5.0
        ```

=== "Upgrade via Chart Package"

    1. Backup the `--set` parameters.

        Before upgrading the Cloud Edge Collaboration version, it is recommended to run the following command to back up the `--set` parameters of the old version.

        ```shell
        helm get values kant -n kant-system -o yaml > bak.yaml
        ```

    1. Update kant crds.

        ```shell
        kubectl apply -f ./crds
        ```

    1. Run `helm upgrade`.

        Before upgrading, it is recommended to modify the __global.imageRegistry__ field in bak.yaml to the current image repository address.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade kant-release . \
          -n kant-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
        ```
