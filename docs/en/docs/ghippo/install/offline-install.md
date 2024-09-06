---
MTPE: WANG0608GitHub
Date: 2024-09-05
---

# Offline Upgrade Global Management Module

This page explains how to install or upgrade the Global Management module after
[downloading it from Download Center](../../download/modules/ghippo.md).

!!! info

    `ghippo` appearing in the commands or scripts below is the internally developed code name for the Global Management module.

## Load images from the installation package

You can load images using one of the two methods below. When an container registry is available
in the environment, it is recommended to use chart-syncer to synchronize images to the repository,
as this method is more efficient and convenient.

### Sync images with the container registry

1. Create load-image.yaml

    !!! note  

        All parameters in this YAML file are required. You need a private container registry and modify the relevant configurations.

    === "Chart repo installed"

        If the current environment has installed a chart repo, chart-syncer also supports exporting the chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: ghippo-offline # (1)!
        target:
          containerRegistry: 10.16.10.111 # (2)!
          containerRepository: release.daocloud.io/ghippo # (3)!
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

        1. Path relative to where the charts-syncer command is executed, not relative to this YAML file and the offline package
        2. Change to your container registry URL
        3. Change to your container registry
        4. Can also be any other supported Helm Chart repository type
        5. Change to the chart repo URL
        6. Your container registry username
        7. Your container registry password
        8. Your container registry username
        9. Your container registry password
   
    === "Chart repo not installed"

        If the current environment does not have a chart repo installed, chart-syncer also supports exporting the chart as a tgz file and storing it in a specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: ghippo-offline # (1)!
        target:
          containerRegistry: 10.16.10.111 # (2)!
          containerRepository: release.daocloud.io/ghippo # (3)!
          repo:
            kind: LOCAL
            path: ./local-repo # (4)!
          containers:
            auth:
              username: "admin" # (5)!
              password: "Harbor12345" # (6)!
        ```

        1. Path relative to where the charts-syncer command is executed, not relative to this YAML file and the offline package
        2. Change to your container registry URL
        3. Change to your container registry
        4. Local path of the chart
        5. Your container registry username
        6. Your container registry password

1. Run the synchronous image command.

    ```shell
    charts-syncer sync --config load-image.yaml
    ```

### Load directly with Docker or containerd

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

## Upgrade

Upgrade Notes:

=== "Upgrade from v0.11.x to ≥v0.12.0"

    When upgrading from v0.11.x (or lower versions) to v0.12.0 (or higher versions), it is necessary to change all keycloak keys in __bak.yaml__ to __keycloakx__.

    Replace the key:

    ```yaml title="bak.yaml"
    USER-SUPPLIED VALUES:
    keycloak:
        ...
    ```

    with:

    ```yaml title="bak.yaml"
    USER-SUPPLIED VALUES:
    keycloakx:
        ...
    ```

=== "Upgrade from v0.15.x to ≥v0.16.0"

    When upgrading from v0.15.x (or lower versions) to v0.16.0 (or higher versions), you need to modify the database connection parameters.

    Replace the key:

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

    with:

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

There are two upgrade methods. You can choose the proper upgrade plan based on the above operations:

=== "upgrade via helm repo"

    1. Check whether the Global Management Helm repository exists.

        ```shell
        helm repo list | grep ghippo
        ```

        If the returned result is empty or as prompted, proceed to the next step; otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    1. Add the Global Mnagement Helm repository.

        ```shell
        helm repo add ghippo http://{harbor url}/chartrepo/{project}
        ```

    1. Update the Global Mnagement Helm repository.

        ```shell
        helm repo update ghippo # (1)!
        ```

        1. If the Helm version is too low, it will fail. If it fails, please try to run Helm update repo

    1. Select the version of Global Management you want to install (the latest version is recommended).

        ```shell
        helm search repo ghippo/ghippo --versions
        ```

        ```none
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        ghippo/ghippo  0.9.0          v0.9.0       A Helm chart for GHippo
        ...
        ```

    1. Back up the `--set` parameter.

        Before upgrading the Global Management version, it is recommended that you run the following command to back up the `--set` parameter of the old version.

        ```shell
        helm get values ​​ghippo -n ghippo-system -o yaml > bak.yaml
        ```

    1. Update Ghippo CRD.

        ```shell
        helm pull ghippo/ghippo --version 0.9.0 && tar -zxf ghippo-0.9.0.tgz
        kubectl apply -f ghippo/crds
        ```

    1. Run `helm upgrade`.

        Before upgrading, it is recommended that you override the __global.imageRegistry__ field in bak.yaml to the address of the currently used container registry.

        ```shell
        export imageRegistry={your-container-registry}
        ```

        ```shell
        helm upgrade ghippo ghippo/ghippo \
          -n ghippo-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry \
          --version 0.9.0
        ```

=== "upgrade via chart package"

    1. Back up the `--set` parameter.

        Before upgrading the Global Management version, it is recommended that you run the following command to back up the `--set` parameter of the old version.

        ```shell
        helm get values ​​ghippo -n ghippo-system -o yaml > bak.yaml
        ```

    1. Update Ghippo CRD:

        ```shell
        kubectl apply -f ./crds
        ```

    1. Run `helm upgrade` .

        Before upgrading, it is recommended that you overwrite __global.imageRegistry__ in bak.yaml to the address of the current container registry.

        ```shell
        export imageRegistry={your-container-registry}
        ```

        ```shell
        helm upgrade ghippo . \
          -n ghippo-system \
          -f ./bak.yaml \
          --set global.imageRegistry=$imageRegistry
        ```
