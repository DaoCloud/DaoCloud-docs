# Offline upgrade global management module

This page explains how to install or upgrade the global management module after
[downloading it from Download Center](../../download/modules/ghippo.md).

!!! info

    The word `ghippo` appearing in the commands or scripts below is the internally developed code name for the global management module.

## Synchronize image to the container registry

First, synchronize the image to the specified container registry through chart-syncer.

1. Create load-image.yaml

    !!! note

        All parameters in this YAML file are required. You need a private container registry and modify related configurations.

    === "chart repo installed"

        If the current environment has installed the chart repo, chart-syncer also supports exporting the chart as a tgz file.

        ```yaml
        source:
        intermediateBundlesPath: ghippo-offline # relative path to charts-syncer
                                        # But not the relative path between this YAML file and the offline package
        target:
        containerRegistry: 10.16.10.111 # need to be changed to your container registry url
        containerRepository: release.daocloud.io/ghippo # need to be changed to your container registry
        repo:
          kind: HARBOR # Can also be any other supported Helm Chart repository class
          url: http://10.16.10.111/chartrepo/release.daocloud.io # need to change to chart repo url
          auth:
            username: "admin" # Your container registry username
            password: "Harbor12345" # Your container registry password
        containers:
          auth:
            username: "admin" # Your container registry username
            password: "Harbor12345" # Your container registry password
        ```

    === "chart repo not installed"

        If the chart repo is not installed in the current environment, chart-syncer also supports exporting the chart as a tgz file and storing it in the specified path.

        ```yaml
        source:
        intermediateBundlesPath: ghippo-offline # relative path to charts-syncer
                                    # But not the relative path between this YAML file and the offline package
        target:
        containerRegistry: 10.16.10.111 # need to be changed to your container registry url
        containerRepository: release.daocloud.io/ghippo # need to be changed to your container registry
        repo:
          kind: LOCAL
          path: ./local-repo # chart local path
        containers:
          auth:
          username: "admin" # Your container registry username
          password: "Harbor12345" # Your container registry password
        ```

1. Run the synchronous image command.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

## Load image file

Unzip and load the image file.

1. Unzip the tar archive.

    ```shell
    tar xvf ghippo.bundle.tar
    ```

    After successful decompression, you will get 3 files:

    - hints.yaml
    - images.tar
    - original-chart

2. Load the image locally to Docker or containerd.

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr -n k8s.io image import images.tar
        ```

!!! note

    After the loading is complete, the tag image is required to keep the Registry and Repository consistent with the installation.

## upgrade

There are two ways to upgrade. You can choose the corresponding upgrade plan according to the pre-operations:

!!! note

    When upgrading from v0.11.x (or lower) to v0.12.0 (or higher), you need to change all keycloak keys in __bak.yaml__ to keycloakx.

    Example modification of this key:

    ```yaml
    USER-SUPPLIED VALUES:
    keycloak:
        ...
    ```

    change into:

    ```yaml
    USER-SUPPLIED VALUES:
    keycloakx:
        ...
    ```

!!! note  

    When upgrading from v0.15.x (or lower) to v0.16.0 (or higher) versions,
    the database connection parameters need to be modified.

    Here is an example of modifying the database connection parameters:

    ```yaml title="bak.yaml"
    USER-SUPPLIED VALUES:
    global:
      database:
        host: 127.0.0.1
        port: 3306
        apiserver:
          dbname: ghippo
          password: passowrd
          user: ghippo
        keycloakx:
          dbname: keycloak
          password: passowrd
          user: keycloak
      auditDatabase:
        auditserver:
          dbname: audit
          password: passowrd
          user: audit
        host: 127.0.0.1
        port: 3306
    ```

    Change it to:

    ```yaml title="bak.yaml"
    USER-SUPPLIED VALUES:
    global:
      storage:
        ghippo:
        - driver: mysql
          accessType: readwrite
          dsn: {global.database.apiserver.user}:{global.database.apiserver.password}@tcp({global.database.host}:{global.database.port})/{global.database.apiserver.dbname}?charset=utf8mb4&multiStatements=true&parseTime=true
        audit:
        - driver: mysql
          accessType: readwrite
          dsn: {global.auditDatabase.auditserver.user}:{global.auditDatabase.auditserver.password}@tcp({global.auditDatabase.host}:{global.auditDatabase.port})/{global.auditDatabase.auditserver.dbname}?charset=utf8mb4&multiStatements=true&parseTime=true
        keycloak:
        - driver: mysql
          accessType: readwrite
          dsn: {global.database.keycloakx.user}:{global.database.keycloakx.password}@tcp({global.database.host}:{global.database.port})/{global.database.keycloakx.dbname}?charset=utf8mb4
    ```

=== "upgrade via helm repo"

    1. Check whether the global management helm repository exists.

        ```shell
        helm repo list | grep ghippo
        ```

        If the returned result is empty or as prompted, proceed to the next step; otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    1. Add the globally managed helm repository.

        ```shell
        helm repo add ghippo http://{harbor url}/chartrepo/{project}
        ```

    1. Update the globally managed helm repository.

        ```shell
        helm repo update ghippo # (1) 
        ```

        1. If the helm version is too low, it will fail. If it fails, please try to run helm update repo

    1. Select the version of Global Management you want to install (the latest version is recommended).

        ```shell
        helm search repo ghippo/ghippo --versions
        ```

        ```none
        [root@master ~]# helm search repo ghippo/ghippo --versions
        NAME CHART VERSION APP VERSION DESCRIPTION
        ghippo/ghippo 0.9.0 v0.9.0 A Helm chart for GHippo
        ...
        ```

    1. Back up the __--set__ parameter.

        Before upgrading the global management version, it is recommended that you run the following command to back up the __--set__ parameter of the old version.

        ```shell
        helm get values ​​ghippo -n ghippo-system -o yaml > bak.yaml
        ```

    1. Execute __helm upgrade__ .

        Before upgrading, it is recommended that you override the __global.imageRegistry__ field in bak.yaml to the address of the currently used container registry.

        ```shell
        export imageRegistry={your image registry}
        ```

        ```shell
        helm upgrade ghippo ghippo/ghippo \
        -n ghippo-system\
        -f ./bak.yaml \
        --set global.imageRegistry=$imageRegistry
        --version 0.9.0
        ```

=== "upgrade via chart package"

    1. Back up the __--set__ parameter.

        Before upgrading the global management version, it is recommended that you run the following command to back up the __--set__ parameter of the old version.

        ```shell
        helm get values ​​ghippo -n ghippo-system -o yaml > bak.yaml
        ```

    1. Update ghippo crds

        ```shell
        kubectl apply -f ./crds
        ```

    1. Execute __helm upgrade__ .

        Before upgrading, it is recommended that you overwrite __global.imageRegistry__ in bak.yaml to the address of the current container registry.

        ```shell
        export imageRegistry={your-container-registry}
        ```

        ```shell
        helm upgrade ghippo .\
        -n ghippo-system\
        -f ./bak.yaml \
        --set global.imageRegistry=$imageRegistry
        ```