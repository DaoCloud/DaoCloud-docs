# Offline Upgrade Middleware - MinIO Module

This page explains how to install or upgrade the Middleware - MinIO module after downloading it from the [Download Center](../../../download/index.md).

!!! info

    The term __mcamel__ appearing in the following commands or scripts refers to the internal development code name of the middleware module.

## Load Images from Installation Package

You can load images in one of the following two ways. It is recommended to use chart-syncer to synchronize images to an image repository when there is an image repository available in the environment, as it is more efficient and convenient.

### Synchronize Images to Image Repository using chart-syncer

1. Create __load-image.yaml__ .

    !!! note

        All parameters in this YAML file are required. You need a private image repository and modify the relevant configuration.

    === "Chart Repo Installed"

        If the current environment has a chart repo installed, chart-syncer also supports exporting the chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mcamel-offline # Relative path to the charts-syncer command execution, not relative to this YAML file and the offline package
        target:
          containerRegistry: 10.16.10.111 # Replace with your image repository URL
          containerRepository: release.daocloud.io/mcamel # Replace with your image repository
          repo:
            kind: HARBOR # It can be any other supported Helm Chart repository type
            url: http://10.16.10.111/chartrepo/release.daocloud.io # Replace with chart repo URL
            auth:
              username: "admin" # Your image repository username
              password: "Harbor12345" # Your image repository password
          containers:
            auth:
              username: "admin" # Your image repository username
              password: "Harbor12345" # Your image repository password
        ```

    === "Chart Repo Not Installed"

        If the current environment does not have a chart repo installed, chart-syncer also supports exporting the chart as a tgz file and storing it in the specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: mcamel-offline # Relative path to the charts-syncer command execution, not relative to this YAML file and the offline package
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

1. Run the command to synchronize images.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### Load directly using Docker or containerd

Unpack and load the image files.

1. Unpack the tar archive.

    ```shell
    tar -xvf mcamel-minio_0.8.1_amd64.tar
    cd mcamel-minio_0.8.1_amd64
    tar -xvf mcamel-minio_0.8.1.bundle.tar
    ```

    After successful extraction, you will get three files:

    - hints.yaml
    - images.tar
    - original-chart

1. Load the images from the local directory into Docker or containerd.

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

There are two ways to upgrade. Choose the corresponding upgrade method based on the preconditions:

=== "Upgrade via helm repo"

    1. Check if the helm repo exists.

        ```shell
        helm repo list | grep minio
        ```

        If the result is empty or shows the following prompt, proceed to the next step. Otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    1. Add the helm repo.

        ```shell
        helm repo add mcamel-minio http://{harbor url}/chartrepo/{project}
        ```

    1. Update the helm repo.

        ```shell
        helm repo update mcamel/mcamel-minio # If helm version is too low and the update fails, try running helm update repo
        ```

    1. Select the version you want to install (we recommend installing the latest version).

        ```shell
        helm search repo mcamel/mcamel-minio --versions
        ```

        ```none
        [root@master ~]# helm search repo mcamel/mcamel-minio --versions
        NAME                            CHART VERSION   APP VERSION     DESCRIPTION               
        mcamel/mcamel-minio     0.8.1           0.8.1           A Helm chart for Kubernetes
        ...
        ```

    1. Back up the `--set` parameters.

        Before upgrading the version, we recommend executing the following command to back up the `--set` parameters of the previous version.

        ```shell
        helm get values mcamel-minio -n mcamel-system -o yaml > mcamel-minio.yaml
        ```

    1. Run `helm upgrade` .

        Before upgrading, it is recommended to update the  `global.imageRegistry` field in mcamel-minio.yaml to the address of the image repository currently in use.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade mcamel-minio mcamel/mcamel-minio \
          -n mcamel-system \
          -f ./mcamel-minio.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.8.1
        ```

=== "Upgrade via chart package"

    1. Back up the `--set` parameters.

        Before upgrading the version, we recommend executing the following command to back up the `--set` parameters of the previous version.

        ```shell
        helm get values mcamel-minio -n mcamel-system -o yaml > mcamel-minio.yaml
        ```

    1. Run `helm upgrade` .

        Before upgrading, it is recommended to update the __bak.yaml__ file's  `global.imageRegistry` field to the address of the image repository currently in use.

        ```shell
        export imageRegistry={your image repository}
        ```

        ```shell
        helm upgrade mcamel-minio . \
          -n mcamel-system \
          -f ./mcamel-minio.yaml \
          --set global.imageRegistry=${imageRegistry} \
          --set console_image.registry=${imageRegistry} \ 
          --set operator_image.registry=${imageRegistry}
        ```
