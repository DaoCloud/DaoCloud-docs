---
MTPE: ModetaNiu
DATE: 2024-09-19
---

# Offline Upgrade

Multicloud Management supports offline upgrades. You need to load the images from the installation package and 
then execute the respective commands for upgrading.

!!! info

    The term "kairship" appearing in the following commands or scripts is the internal development codename for the Multicloud Management module.

## Load Images from the Downloaded Installation Package

You can load the images in one of the following two ways, but it is recommended to use chart-syncer to 
synchronize the images to the container registry when an container registry is available in the environment. 
This method is more efficient and convenient.

#### Method 1: Synchronize Images Using chart-syncer

Using chart-syncer, you can upload the charts and their dependent image packages from the downloaded installation 
package to the container registry and helm repository used by the installer to deploy DCE.

First, find a node that can connect to the container registry and helm repository (e.g., the spark node) 
and create the __load-image.yaml__ configuration file on the node with the appropriate configuration information 
for the container registry and helm repository.

1. Create __load-image.yaml__ 

    !!! note  

        All parameters in this YAML file are required.

    === "Helm repo added"

        If the current environment already has a chart repo installed, chart-syncer supports exporting the chart as a tgz file.
    
        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: kairship # The path where the .tar.gz package is located after using chart-syncer
        target:
          containerRegistry: 10.16.10.111 # Container registry address
          containerRepository: release.daocloud.io/kairship # Container registry path
          repo:
            kind: HARBOR # Helm Chart repository type
            url: http://10.16.10.111/chartrepo/release.daocloud.io # Helm repository address
            auth:
              username: "admin" # Container registry username
              password: "Harbor12345" # Container registry password
          containers:
            auth:
              username: "admin" # Helm repository username
              password: "Harbor12345" # Helm repository password
        ```

    === "Helm repo not added"

        If no helm repo is added on the current node, chart-syncer supports exporting the chart as a tgz file and storing it in the specified path.
    
        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: kairship # The path where the .tar.gz package is located after using chart-syncer
        target:
          containerRegistry: 10.16.10.111 # Container registry URL
          containerRepository: release.daocloud.io/kairship # Container registry path
          repo:
            kind: LOCAL
            path: ./local-repo # Local chart path
          containers:
            auth:
              username: "admin" # Container registry username
              password: "Harbor12345" # Container registry password
        ```

1. Run the command to synchronize the images.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

#### Method 2: Load Images Using Docker or containerd

Unpack and load the image files.

1. Unpack the tar archive.

    ```shell
    tar xvf kairship.bundle.tar
    ```

    After successful unpacking, you will have three files:

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
        ctr -n k8s.io image import images.tar
        ```

!!! note

    Each node needs to perform the Docker or containerd image loading operation.
    After loading is complete, it is necessary to tag the images to match the registry and repository as they were during installation.

## Upgrading

There are two ways to upgrade. You can choose the corresponding upgrade method based on the prerequisites:

=== "Upgrade via helm repo"

    1. Check if the Multicloud Management Helm repository exists.
    
        ```shell
        helm repo list | grep kairship
        ```
    
        If the result is empty or shows the following prompt, proceed to the next step; otherwise, skip the next step.
    
        ```none
        Error: no repositories to show
        ```
    
    1. Add the Multicloud Management Helm repository.
    
        ```shell
        helm repo add kairship http://{harbor url}/chartrepo/{project}
        ```
    
    1. Update the Multicloud Management Helm repository.
    
        ```shell
        helm repo update kairship
        ```
    
    1. Select the version of Multicloud Management you want to install (it is recommended to install the latest version).
    
        ```shell
        helm search repo kairship/kairship --versions
        ```
    
        The output will be similar to:
        
        ```none
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        kairship/kairship  0.20.0          v0.20.0       A Helm chart for kairship
        ...
        ```
    
    1. Back up the `--set` parameters.
    
        Before upgrading the Multicloud Management version, it is recommended to run the following command to back up the `--set` parameters of the old version.
    
        ```shell
        helm get values kairship -n kairship-system -o yaml > bak.yaml
        ```
    
    1. Update kairship CRDs
    
        ```shell
        helm pull kairship/kairship --version 0.21.0 && tar -zxf kairship-0.21.0.tgz
        kubectl apply -f kairship/crds
        ```
    
    1. Run `helm upgrade` .
    
        Before upgrading, it is recommended to update the `global.imageRegistry` field in bak.yaml to the container registry address you are currently using.
    
        ```shell
        export imageRegistry={your_image_registry}
        ```
    
        ```shell
        helm upgrade kairship kairship/kairship \
          -n kairship-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.21.0
        ```

=== "Upgrade via chart package"

    1. Back up the `--set` parameters.
    
        Before upgrading the Multicloud Management version, it is recommended to run the following command to back up the `--set` parameters of the old version.
    
        ```shell
        helm get values kairship -n kairship-system -o yaml > bak.yaml
        ```
    
    1. Update kairship CRDs
    
        ```shell
        kubectl apply -f ./crds
        ```
    
    1. Run `helm upgrade` .
    
        Before upgrading, it is recommended to update the `global.imageRegistry` field in bak.yaml to the container registry address you are currently using.
    
        ```shell
        export imageRegistry={your_image_registry}
        ```
    
        ```shell
        helm upgrade kairship . \
          -n kairship-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
        ```
