# Offline Upgrade Backup and Restore Module

This page explains how to install or upgrade the backup and restore module after
[downloading it from the Download Center](../../../download/modules/kcoral.md).

!!! info

    The term 'kcoral' used in the following commands or scripts is the internal development code name for the backup and restore module.

## Load Images from Downloaded Package

You can load the images using one of the following two methods. When the container registry exists in the environment, it is recommended to use chart-syncer to synchronize the images to the container registry, as it is more efficient and convenient.

### Method 1: Use chart-syncer to Synchronize Images

Using chart-syncer, you can upload the charts and their dependent image packages from the downloaded package to the container registry and Helm repository used by the installer.

First, find a node that can connect to the container registry and Helm repository (such as the Spark node), and create a __load-image.yaml__ configuration file on the node, filling in the configuration information for the container registry and Helm repository.

1. Create __load-image.yaml__ file

    !!! note  

        All parameters in this YAML file are required.

    === "Helm repo already added"

        If the current environment has already installed the chart repo, chart-syncer also supports exporting the chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: kcoral # (1)!
        target:
          containerRegistry: 10.16.10.111 # (2)!
          containerRepository: release.daocloud.io/kcoral # (3)!
          repo:
            kind: HARBOR # (4)!
            url: http://10.16.10.111/chartrepo/release.daocloud.io # (5)!
            auth:
              username: "admin" # (6)!
              password: "Harbor12345" # (7)!
          containers:
            auth:
              username: "admin" # (8)!
              password: "Harbor12345" # (9)!
        ```

        1. The path where the .tar.gz package is located after using chart-syncer
        2. Container registry address
        3. Container registry path
        4. Helm Chart repository type
        5. Helm repository address
        6. Container registry username
        7. Container registry password
        8. Helm repository username
        9. Helm repository password

    === "Helm repo not added"

        If the current node does not have a helm repo added, chart-syncer also supports exporting the chart as a tgz file and storing it in the specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: kcoral # (1)!
        target:
          containerRegistry: 10.16.10.111 # (2)!
          containerRepository: release.daocloud.io/kcoral # (3)!
          repo:
            kind: LOCAL
            path: ./local-repo # (4)!
          containers:
            auth:
              username: "admin" # (5)!
              password: "Harbor12345" # (6)!
        ```

        1. The path where the .tar.gz package is located after using chart-syncer
        2. Container registry URL
        3. Container registry path
        4. Local path to the chart
        5. Container registry username
        6. Container registry password

1. Run the command to synchronize the images.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### Method 2: Load Images using Docker or containerd

Unpack and load the image files.

1. Extract the tar package.

    ```shell
    tar xvf kcoral.bundle.tar
    ```

    After successful extraction, you will get three files:

    - kcoral.bundle.tar

2. Load the images into Docker or containerd from the local directory.

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
    After loading is complete, tag the images to ensure consistency with the Registry and Repository used during installation.

## Upgrade

There are two upgrade methods. You can choose the appropriate upgrade method based on the preconditions:

=== "Upgrade via Helm Repo"

    1. Check if the backup and restore Helm repository exists.

        ```shell
        helm repo list | grep kcoral
        ```

        If the result is empty or shows the following prompt, proceed to the next step. Otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    1. Add the backup and restore Helm repository.

        ```shell
        helm repo add kcoral http://{harbor url}/chartrepo/{project}
        ```

    1. Update the backup and restore Helm repository.

        ```shell
        helm repo update kcoral
        ```

    1. Select the backup and restore version you want to install (it is recommended to install the latest version version).

        ```shell
        helm search repo kcoral/kcoral --versions
        ```

        ```none
        [root@master ~]# helm search repo kcoral/kcoral --versions
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        kcoral/kcoral  0.20.0          v0.20.0       A Helm chart for kcoral
        ...
        ```

    1. Back up the `--set` parameters.

        Before upgrading the backup and restore version, it is recommended to run the following command to back up the `--set` parameters of the old version.

        ```shell
        helm get values kcoral -n kcoral-system -o yaml > bak.yaml
        ```

    1. Run `helm upgrade` .

        Before upgrading, it is recommended to replace the __global.imageRegistry__ field in the __bak.yaml__ file with the container registry address you are currently using.

        ```shell
        export imageRegistry={your container registry}
        ```

        ```shell
        helm upgrade kcoral kcoral/kcoral \
          -n kcoral-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.5.0
        ```

=== "Upgrade via Chart Package"

    1. Back up the `--set` parameters.

        Before upgrading the backup and restore version, it is recommended to run the following command to back up the `--set` parameters of the old version.

        ```shell
        helm get values kcoral -n k pan da-system -o yaml > bak.yaml
        ```

    1. Run `helm upgrade` .

        Before upgrading, it is recommended to replace the __global.imageRegistry__ in the __bak.yaml__ file with the container registry address you are currently using.

        ```shell
        export imageRegistry={your container registry}
        ```

        ```shell
        helm upgrade kcoral . \
          -n kcoral-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
        ```
