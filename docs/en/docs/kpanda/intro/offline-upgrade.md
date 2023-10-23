# Offline Upgrade of Container Management Module

This page explains how to install or upgrade the Container Management Module after [downloading it from the Download Center](../../download/modules/kpanda.md).

!!! info

    The term "kpanda" mentioned in the following commands or scripts is the internal development codename for the Container Management Module.

## Load Images from the Downloaded Package

You can load the images in one of the following two ways. When an image repository exists in the environment, it is recommended to use chart-syncer to synchronize the images to the image repository, as it is more efficient and convenient.

#### Method 1: Synchronize Images using chart-syncer

Using chart-syncer, you can upload the charts and their dependent image packages from the downloaded package to the image repository and helm repository used by the installer when deploying DCE.

First, find a node (e.g., Spark Node) that can connect to the image repository and helm repository. Create a `load-image.yaml` configuration file on the node and fill in the configuration information for the image repository and helm repository.

1. Create `load-image.yaml`

    !!! note

        All parameters in this YAML file are required.

    === "Helm Repo Added"

        If the chart repo is already installed in the current environment, chart-syncer also supports exporting charts as tgz files.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: kpanda # Path where the load-image.yaml file is executed on the node.
        target:
          containerRegistry: 10.16.10.111 # Image repository address
          containerRepository: release.daocloud.io/kpanda # Image repository path
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

    === "Helm Repo Not Added"

        If the helm repo is not added on the current node, chart-syncer also supports exporting charts as tgz files and storing them in the specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: kpanda # Path where the load-image.yaml file is executed on the node.
        target:
          containerRegistry: 10.16.10.111 # Image repository url
          containerRepository: release.daocloud.io/kpanda # Image repository path
          repo:
            kind: LOCAL
            path: ./local-repo # Local path of the chart
          containers:
            auth:
              username: "admin" # Image repository username
              password: "Harbor12345" # Image repository password
        ```

1. Run the image synchronization command.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

#### Method 2: Load Images using Docker or containerd

Unpack and load the image files.

1. Unpack the tar compressed file.

    ```shell
    tar xvf kpanda.bundle.tar
    ```

    After successful unpacking, you will get 3 files:

    - hints.yaml
    - images.tar
    - original-chart

2. Load the images from the local file to Docker or containerd.

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
    After loading is complete, tag the images to keep the Registry and Repository consistent with the installation.

## Upgrade

There are two ways to upgrade. You can choose the corresponding upgrade method based on the pre-operation:

=== "Upgrade via helm repo"

1. Check if the container management helm repository exists.

    ```shell
    helm repo list | grep kpanda
    ```

    If the result is empty or displays the following prompt, proceed to the next step; otherwise, skip the next step.

    ```none
    Error: no repositories to show
    ```

2. Add the container management helm repository.

    ```shell
    helm repo add kpanda http://{harbor url}/chartrepo/{project}
    ```

3. Update the container management helm repository.

    ```shell
    helm repo update kpanda
    ```

4. Select the version of the container management module you want to install (it is recommended to install the latest version).

    ```shell
    helm search repo kpanda/kpanda --versions
    ```

    The output will be similar to:

    ```none
    NAME                   CHART VERSION  APP VERSION  DESCRIPTION
    kpanda/kpanda  0.20.0          v0.20.0       A Helm chart for kpanda
    ...
    ```

5. Backup the `--set` parameters.

    Before upgrading the container management module, it is recommended to run the following command to backup the `--set` parameters of the old version.

    ```shell
    helm get values kpanda -n kpanda-system -o yaml > bak.yaml
    ```

6. Update the kpanda CRDs.

    ```shell
    helm pull kpanda/kpanda --version 0.21.0 && tar -zxf kpanda-0.21.0.tgz
    kubectl apply -f kpanda/crds
    ```

7. Run `helm upgrade`.

    Before upgrading, it is recommended to replace the `global.imageRegistry` field in `bak.yaml` with the image repository address you are currently using.

    ```shell
    export imageRegistry={your_image_repository}
    ```

    ```shell
    helm upgrade kpanda kpanda/kpanda \
      -n kpanda-system \
      -f ./bak.yaml \
      --set global.imageRegistry=$imageRegistry \
      --version 0.21.0
    ```

=== "Upgrade via chart package"

1. Backup the `--set` parameters.

    Before upgrading the container management module, it is recommended to run the following command to backup the `--set` parameters of the old version.

    ```shell
    helm get values kpanda -n k pan da-system -o yaml > bak.yaml
    ```

2. Update the kpanda CRDs.

    ```shell
    kubectl apply -f ./crds
    ```

3. Run `helm upgrade`.

    Before upgrading, it is recommended to replace the `global.imageRegistry` field in `bak.yaml` with the image repository address you are currently using.

    ```shell
    export imageRegistry={your_image_repository}
    ```

    ```shell
    helm upgrade kpanda . \
      -n kpanda-system \
      -f ./bak.yaml \
      --set global.imageRegistry=$imageRegistry
    ```
