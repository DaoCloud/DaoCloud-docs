# Offline Upgrade of Operations Management Module

This page provides instructions on how to install or upgrade the Operations Management module
after [downloading it from the Download Center](../../../download/modules/gmagpie.md).

!!! info

    The term `gmagpie` used in the following commands or scripts refers to
    the internal development codename for the Operations Management module.

## Loading Image from the Installation Package

You can load the image using either of the following methods. It is recommended to choose
the chart-syncer method when an registry already exists in the environment,
as it is more efficient and convenient.

### Synchronize Images to Registry using chart-syncer

1. Create __load-image.yaml__ .

    !!! note

        All parameters in this YAML file are mandatory. You need a private registry
        and modify the relevant configurations accordingly.

    === "Installed chart repo"

        If you have an installed chart repo in the current environment, chart-syncer also
        supports exporting the chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: gmagpie-offline # (1)!
        target:
          containerRegistry: 10.16.10.111 # (2)!
          containerRepository: release.daocloud.io/gmagpie # (3)!
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

        1. Use the relative path to run the `charts-syncer` command, not the relative path
        2. Modify it to your registry URL.
        3. Modify it to your registry.
        4. It can also be any other supported Helm Chart repository category.
        5. Need to be changed to chart repo url
        6. Your registry username.
        7. Your registry password.
        8. Your registry username.
        9. Your registry password.

    === "Chart Repo Not Installed"

        If a chart repo is not installed in the current environment, chart-syncer also
        supports exporting the chart as a tgz file and storing it in the specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: gmagpie-offline # (1)!
        target:
          containerRegistry: 10.16.10.111 # (2)!
          containerRepository: release.daocloud.io/gmagpie # (3)!
          repo:
            kind: LOCAL
            path: ./local-repo # (4)!
          containers:
            auth:
              username: "admin" # (5)!
              password: "Harbor12345" # (6)!
        ```

        1. Use the relative path to run the `charts-syncer` command, not the relative path between this YAML file and the offline package.
        2. Modify it to your registry URL.
        3. Modify it to your registry.
        4. Local path of the chart.
        5. Your registry username.
        6. Your registry password.

1. Run the command to synchronize images.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### Loading directly with Docker or containerd

Unpack and load the image file.

1. Unpack the tar archive.

    ```shell
    tar xvf gmagpie.bundle.tar
    ```

    After a successful unpacking, you will obtain 3 files:

    - hints.yaml
    - images.tar
    - original-chart

2. Load the image from the local source into Docker or containerd.

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr -n k8s.io image import images.tar
        ```

!!! note

    Each node needs to perform the image loading operation with Docker or containerd. 
    After loading is complete, it is necessary to tag the image to keep the Registry
    and Repository consistent with the installation.

## Upgrade

There are two ways to upgrade. You can choose the corresponding upgrade method based on the preconditions:

!!! note

    When upgrading from v0.1.x (or lower) to v0.2.0 (or higher), database connection parameters need to be modified.

    Example of modifying database connection parameters:

    ```yaml title="bak.yaml"
    USER-SUPPLIED VALUES:
    global:
      database:
        host: 127.0.0.1
        port: 3306
        dbname: gmagpie
        password: passowrd
        user: gmagpie
    ```

    Modified to:

    ```yaml title="bak.yaml"
    USER-SUPPLIED VALUES:
    global:
      storage:
        gmagpie:
        - driver: mysql
          accessType: readwrite
          dsn: {global.database.apiserver.user}:{global.database.apiserver.password}@tcp({global.database.host}:{global.database.port})/{global.database.apiserver.dbname}?charset=utf8mb4&multiStatements=true&parseTime=true
    ```

=== "Upgrade via helm repo"

    1. Check if the Operations Management Helm repository exists.

        ```shell
        helm repo list | grep gmagpie
        ```

        If the result is empty or shows the following prompt, proceed to the next step;
        otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    1. Add the Operations Management Helm repository.

        ```shell
        helm repo add gmagpie http://{harbor url}/chartrepo/{project}
        ```

    1. Update the Operations Management Helm repository.

        ```shell
        helm repo update gmagpie # (1)!
        ```

        1. If the Helm version is too low, it may result in failure. If this happens,
           please try executing __helm update repo__ .

    1. Choose the version of Operations Management that you would like to install
       (it is recommended to install the latest version).

        ```shell
        helm search repo gmagpie/gmagpie --versions
        ```

        ```none
        [root@master ~]# helm search repo gmagpie/gmagpie --versions
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        gmagpie/gmagpie  0.3.0          v0.3.0       A Helm chart for GHippo
        ...
        ```

    1. Back up the `--set` parameters.

        Before upgrading the Operations Management version, it is recommended to
        run the following command to back up the `--set` parameters of the old version.

        ```shell
        helm get values gmagpie -n gmagpie-system -o yaml > bak.yaml
        ```

    1. Update Gmagpie CRD.

        ```shell
        helm pull gmagpie/gmagpie --version 0.3.0 && tar -zxf gmagpie-0.3.0.tgz
        kubectl apply -f gmagpie/crds
        ```

    1. Run `helm upgrade` .

        Before upgrading, it is recommended to replace the __global.imageRegistry__ field
        in the __bak.yaml__ file with the address of the registry you are currently using.

        ```shell
        export imageRegistry={your-registry}
        ```

        ```shell
        helm upgrade gmagpie gmagpie/gmagpie \
          -n gmagpie-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.3.0
        ```

=== "Upgrade via Chart package"

    1. Back up the `--set` parameters.

        Before upgrading the Operations Management version, it is recommended to
        run the following command to back up the `--set` parameters of the old version.

        ```shell
        helm get values gmagpie -n gmagpie-system -o yaml > bak.yaml
        ```

    2. Update the Gmagpie CRD.

        ```shell
        kubectl apply -f ./crds
        ```

    3. Run `helm upgrade` .

        It is recommended to replace the __global.imageRegistry__ field in the __bak.yaml__ file
        with the address of the registry you are currently using before performing the upgrade.

        ```shell
        export imageRegistry={your-registry}
        ```

        ```shell
        helm upgrade gmagpie . \
          -n gmagpie-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
        ```
