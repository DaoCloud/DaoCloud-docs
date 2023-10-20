# Offline Upgrade of Cloud Native Network

The modules in DCE 5.0 are loosely coupled, allowing for independent installation and upgrading of each module. This document provides instructions for offline upgrading of the cloud native network module Spidernet.

Spidernet is a cloud native network management engine that primarily manages functionalities such as Spidernet, Multus CR, and Egress IP.

## Load images from the downloaded installation Package

You can load the images in one of the following two ways. When an image repository exists in the environment, it is recommended to use chart-syncer to synchronize the images to the image repository, as it is more efficient and convenient.

#### Method 1: synchronize images using chart-syncer

Using chart-syncer, you can upload the charts and their dependent image packages from the downloaded package to the image repository and helm repository used by the installer when deploying DCE.

First, find a node (e.g., Spark Node) that can connect to the image repository and helm repository. Create a load-image.yaml configuration file on the node and fill in the configuration information for the image repository and helm repository.

1. Create load-image.yaml

    !!! note  

        All parameters in this YAML file are required.
  
    === "Helm Repo Added"

        If the chart repo is already installed in the current environment, chart-syncer also supports exporting charts as tgz files.
  
        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: spidernet-offline # (1)
        target:
          containerRegistry: 10.16.23.145 # (2)
          containerRepository: release.daocloud.io/spidernet # (3)
          repo:
            kind: HARBOR # (4)
            url: http://10.16.23.145/chartrepo/release.daocloud.io # (5)
            auth:
            username: "admin" # (6)
            password: "Harbor12345" # (7)
          containers:
            auth:
              username: "admin" # (8)
              password: "Harbor12345" # (9)
        ```
  
        1. Path where the load-image.yaml file is executed on the node
        2. Image repository address
        3. Image repository path
        4. Helm Chart repository type
        5. Helm repository address
        6. Image repository username
        7. Image repository password
        8. Helm repository username
        9. Helm repository password 

    === "Helm Repo Not Added"

        If the helm repo is not added on the current node, chart-syncer also supports exporting charts as tgz files and storing them in the specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: spidernet-offline # (1)
        target:
          containerRegistry: 10.16.23.145 # (2)
          containerRepository: release.daocloud.io/spidernet # (3)
          repo:
            kind: LOCAL
            path: ./local-repo # (4)
          containers:
            auth:
              username: "admin" # (5)
              password: "Harbor12345" # (6)
        ```
  
        1. Path where the load-image.yaml file is executed on the node
        2. Image repository url
        3. Image repository path
        4. Local path of the chart
        5. Image repository username
        6. Image repository password

2. Run the image synchronization command.
  
    ```shell
    charts-syncer sync --config load-image.yaml
    ```
  
#### Method 2: load images using Docker or containerd

Unpack and load the image files.

1. Unpack the tar compressed file.

    ```shell
    tar xvf spidernet.bundle.tar
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
        ctr image import images.tar
        ```

!!! note

    Each node needs to perform the Docker or containerd image loading operation. After loading is complete, tag the images to keep the Registry and Repository consistent with the installation.

## Upgrade

There are two ways to upgrade. You can choose the corresponding upgrade method based on the pre-operation:

=== "Upgrade via Helm Repo"

    1. Check if the network engine's helm repository exists.

        ```shell
        helm repo list | grep spidernet
        ```

        If the result is empty or displays the following prompt, proceed to the next step; otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    2. Add the network engine's helm repository.

        ```shell
        helm repo add spidernet-release http://{harbor url}/chartrepo/{project}
        ```

    3. Update the network engine's helm repository.

        ```shell
        helm repo update spidernet-release # (1)
        ```

    4. In case of a failure during the upgrade process due to an outdated Helm version, please attempt to resolve the issue by executing the command of helm update repo. 

    5. Select the version of the network module you want to install (it is recommended to install the latest version).

        ```shell
        helm search repo spidernet-release/spidernet --versions
        ```

        ```none
        [root@master ~]# helm search repo spidernet-release/spidernet --versions
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        spidernet-release/spidernet  0.8.0          v0.8.0       A Helm chart for spidernet
        ...
        ```

    6. Backup the `--set` parameters.

        Before upgrading the network module, it is recommended to run the following command to backup the `--set` parameters of the old version.

        ```shell
        helm get values spidernet -n spidernet-system -o yaml > bak.yaml
        ```

    7. Run `helm upgrade`。

        Before upgrading, it is recommended to replace the fields `spidernet.image.registry` and `ui.image.registry` in bak.yaml with the image repository address you are currently using.

        ```shell
        export imageRegistry={your_image_repository}
        ```

        ```shell
        helm upgrade spidernet spidernet-release/spidernet \
        -n spidernet-system \
        -f ./bak.yaml \
        --set spidernet.image.registry=$imageRegistry \
        --set ui.image.registry=$imageRegistry \
        --version 0.8.0
        ```

=== "Upgrade via Chart Package"

    1. Backup the `--set` parameters.

        Before upgrading the container management module, it is recommended to run the following command to backup the `--set` parameters of the old version.

        ```shell
        helm get values spidernet -n spidernet-system -o yaml > bak.yaml
        ```

    2. Run `helm upgrade`。

        Before upgrading, it is recommended to replace the fields `spidernet.image.registry` and `ui.image.registry` in bak.yaml with the image repository address you are currently using.

        ```shell
        export imageRegistry={your_image_repository}
        ```

        ```shell
        helm upgrade spidernet . \
        -n spidernet-system \
        -f ./bak.yaml \
        --set spidernet.image.registry=$imageRegistry \
        --set ui.image.registry=$imageRegistry \
        ```
