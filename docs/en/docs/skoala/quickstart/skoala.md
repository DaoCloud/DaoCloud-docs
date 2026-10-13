# Microservice Engine Management Components

This tutorial is intended to supplement the scenario of manually installing the Microservice Engine
module **separately online**. The term `skoala` used in the following text is the internal development
code name for the Microservice Engine.

Deployment Structure of Microservice Engine Management Components

The chart inside the blue box represents the `skoala` component, which needs to be installed in
the control plane cluster, namely the [global service cluster](../../kpanda/user-guide/clusters/cluster-role.md#global-service-cluster) `kpanda-global-cluster` of DCE.
For details, refer to the [deployment architecture](../../install/commercial/deploy-arch.md) of DCE.
After installing the `skoala` component, you can see the Microservice Engine module in the primary navigation bar of DCE.
Also, please note that before installing `skoala`, you need to install the required `common-mysql` component for resource storage.

## Online Install

If you need to install the Microservice Engine, it is recommended to use the installation package of
[DCE Enterprise Package](../../install/commercial/start-install.md) for installation. The
Enterprise Package allows you to install all modules of DCE at once.

!!! note

    This document provides instructions for online installation. If you have deployed the offline
    Enterprise Package, it is recommended to refer to
    [Offline Upgrade of Microservice Engine](#offline-upgrade) for offline installation or upgrade of the Microservice Engine.

### Install Enterprise Package

When installing the Microservice Engine management components using the Enterprise Package, pay attention
to the version number of the Enterprise Package ([click here to view the latest version](../../download/index.md)).
Different operations need to be performed for different versions.

When the version number of the Enterprise Package is **≥ v0.3.29**, the Microservice Engine management
components will be installed by default. However, it is still recommended to check the `manifest.yaml`
file to confirm that the value of `components/skoala/enable` is set to `true` and that the Helm version
is specified.

> The Enterprise Package installs the latest tested version by default. Unless there are special
> circumstances, it is not recommended to modify the default Helm version.

??? note "If Enterprise Package ≤ v0.3.28, click here for the corresponding instructions"

    This note only applies to Enterprise Package ≤ v0.3.28. In most cases, your version will be higher
    than this version.

    By default, the Microservice Engine is not installed when executing the installation command.
    You need to modify the `manifest.yaml` file as shown below to allow the installation of the
    Microservice Engine.

    Modified file:

    ```bash
    ./dce5-installer install-app -m /sample/manifest.yaml
    ```

    Modified content:

    ```yaml
    ...
    components:
      skoala:
        enable: true
        helmVersion: v0.12.2 # Replace with the latest version number
        variables:
    ...
    ```

### Check if the Microservice Engine is Installed

Check if the following resources exist in the `skoala-system` namespace.
If there are no resources, it means that the Microservice Engine is not currently installed.

```bash
$ kubectl -n skoala-system get pods
NAME                                   READY   STATUS    RESTARTS        AGE
hive-8548cd9b59-948j2                  2/2     Running   0               3h48m
sesame-5955c878c6-jz8cd                2/2     Running   0               3h48m
skoala-ui-75b8f8c776-nbw9d             2/2     Running   0               3h48m

$ helm -n skoala-system list
NAME        NAMESPACE       REVISION    UPDATED                                 STATUS      CHART               APP VERSION
skoala     	skoala-system	2       	2023-11-03 10:23:22.373053803 +0800 CST	deployed    skoala-0.28.1       0.28.1
```

### Check the Dependent Storage Component

When installing the Microservice Engine, the `common-mysql` component is required for storing configurations.
Therefore, make sure that this component exists. Additionally, check if there is a database named `skoala`
in the `common-mysql` namespace.

```bash
$ kubectl -n mcamel-system get statefulset
NAME                                          READY   AGE
mcamel-common-mysql-cluster-mysql             2/2     7d23h
```

It is recommended to use the following parameters to configure the database information
for the Microservice Engine:

- Host: mcamel-common-mysql-cluster-mysql-master.mcamel-system.svc.cluster.local
- Port: 3306
- Database: skoala
- User: skoala
- Password:

!!! note

    If `common-mysql` is not installed, you can use a custom database.
    Fill in the above parameters according to your actual situation.

### Check the Dependent Monitoring Component

The Microservice Engine relies on the capabilities of the
[DCE Insight](../../insight/intro/index.md) module. If you need to
monitor various metrics and trace the service calls of your microservices,
you need to install the corresponding `insight-agent` in your cluster.
For detailed instructions, refer to [Installing the insight-agent](../../insight/quickstart/install/install-agent.md).

### Manual Installation Process

Once everything is ready, you can proceed with the formal installation of the
Microservice Engine management components. The specific steps are as follows:

!!! note

    - If you are installing a version of `skoala-release/skoala` below v0.17.1, you need to manually initialize the database tables.
    - If you are installing `skoala-release/skoala` v0.17.1 or above, the database tables will be automatically initialized by the system and manual intervention is not required.

??? note "If the initialization fails, check if the following 3 data tables exist in the `skoala` database and if the corresponding SQL statements are all effective."

    ```sql
    mysql> desc api;
    +------------------+-----------------+------+-----+-------------------+-----------------------------------------------+
    | Field            | Type            | Null | Key | Default           | Extra                                         |
    +------------------+-----------------+------+-----+-------------------+-----------------------------------------------+
    | id               | bigint unsigned | NO   | PRI | NULL              | auto_increment                                |
    | is_hosted        | tinyint         | YES  |     | 0                 |                                               |
    | registry         | varchar(50)     | NO   | MUL | NULL              |                                               |
    | service_name     | varchar(200)    | NO   |     | NULL              |                                               |
    | nacos_namespace  | varchar(200)    | NO   |     | NULL              |                                               |
    | nacos_group_name | varchar(200)    | NO   |     | NULL              |                                               |
    | data_type        | varchar(100)    | NO   |     | NULL              |                                               |
    | detail           | mediumtext      | NO   |     | NULL              |                                               |
    | deleted_at       | timestamp       | YES  |     | NULL              |                                               |
    | created_at       | timestamp       | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
    | updated_at       | timestamp       | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
    +------------------+-----------------+------+-----+-------------------+-----------------------------------------------+

    mysql> desc book;
    +-------------+------------------+------+-----+-------------------+-----------------------------------------------+
    | Field       | Type             | Null | Key | Default           | Extra                                         |
    +-------------+------------------+------+-----+-------------------+-----------------------------------------------+
    | id          | bigint unsigned  | NO   | PRI | NULL              | auto_increment                                |
    | uid         | varchar(32)      | YES  | UNI | NULL              |                                               |
    | name        | varchar(50)      | NO   | UNI | NULL              |                                               |
    | author      | varchar(32)      | NO   |     | NULL              |                                               |
    | status      | int              | YES  |     | 1                 |                                               |
    | isPublished | tinyint unsigned | NO   |     | 1                 |                                               |
    | publishedAt | timestamp        | YES  |     | NULL              |                                               |
    | deleted_at  | timestamp        | YES  |     | NULL              |                                               |
    | createdAt   | timestamp        | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
    | updatedAt   | timestamp        | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
    +-------------+------------------+------+-----+-------------------+-----------------------------------------------+
    10 rows in set (0.00 sec)

    mysql> desc registry;
    +--------------+-----------------+------+-----+-------------------+-----------------------------------------------+
    | Field        | Type            | Null | Key | Default           | Extra                                         |
    +--------------+-----------------+------+-----+-------------------+-----------------------------------------------+
    | id           | bigint unsigned | NO   | PRI | NULL              | auto_increment                                |
    | uid          | varchar(32)     | YES  | UNI | NULL              |                                               |
    | workspace_id | varchar(50)     | NO   |     | default           |                                               |
    | ext_id       | varchar(50)     | YES  |     | NULL              |                                               |
    | name         | varchar(50)     | NO   | MUL | NULL              |                                               |
    | type         | varchar(50)     | NO   |     | NULL              |                                               |
    | addresses    | varchar(1000)   | NO   |     | NULL              |                                               |
    | namespaces   | varchar(2000)   | NO   |     | NULL              |                                               |
    | is_hosted    | tinyint         | NO   |     | 0                 |                                               |
    | deleted_at   | timestamp       | YES  |     | NULL              |                                               |
    | created_at   | timestamp       | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED                             |
    | updated_at   | timestamp       | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED on update CURRENT_TIMESTAMP |
    +--------------+-----------------+------+-----+-------------------+-----------------------------------------------+
    12 rows in set (0.00 sec)
    ```

### Configure Skoala Helm Repository

To configure the Skoala repository, you can view and obtain Skoala's application chart by following these steps:

```bash
helm repo add skoala-release https://release.daocloud.io/chartrepo/skoala
helm repo update
```

Note: Helm needs to be installed beforehand.

`Skoala` is the control-side service of the Microservice Engine:

- Once installed, you can see the entry point for the Microservice Engine on the DCE platform.
- It includes three components: skoala-ui, hive, and sesame.
- It needs to be installed in the global service cluster.

By default, after installing Skoala in the kpanda-global-cluster (global service cluster), you will be able to see the corresponding entry point for the Microservice Engine in the sidebar.

### Check the Latest Version of the Microservice Engine Management Components

To check the latest version of Skoala in the global service cluster,
you can use the helm command to retrieve version information directly:

```bash
$ helm repo update skoala-release
$ helm search repo skoala-release/skoala --versions
NAME                        CHART VERSION   APP VERSION DESCRIPTION
skoala-release/skoala       0.28.1       	0.28.1     	The helm chart for Skoala
skoala-release/skoala       0.28.0       	0.28.0     	The helm chart for Skoala
skoala-release/skoala       0.27.2       	0.27.2     	The helm chart for Skoala
skoala-release/skoala       0.27.1       	0.27.1     	The helm chart for Skoala
......
```

### Perform Deployment (Also Applicable for Upgrades)

Run the following command, making sure to replace the version number accordingly:

```bash
$ helm upgrade --install skoala --create-namespace -n skoala-system --cleanup-on-fail \
    --set hive.configMap.database[0].driver="mysql" \
    --set hive.configMap.database[0].dsn="skoala:xxx@tcp(mcamel-common-mysql-cluster-mysql-master.mcamel-system.svc.cluster.local:3306)/skoala?charset=utf8&parseTime=true&loc=Local&timeout=10s" \
    skoala-release/skoala \
    --version 0.28.1  # make sure to use the latest version
```

Check if the Pods have started successfully:

```bash
$ kubectl -n skoala-system get pods
NAME                                   READY   STATUS    RESTARTS        AGE
hive-8548cd9b59-948j2                  2/2     Running   0               3h48m
sesame-5955c878c6-jz8cd                2/2     Running   0               3h48m
skoala-ui-7c9f5b7b67-9rpzc             2/2     Running   0               3h48m
```

## Online Upgrade

Before starting the upgrade process, it's helpful to understand the deployment architecture
of the Microservice Engine.

The Microservice Engine consists of two components:

- The `skoala` component is installed in the control plane cluster and is responsible for
  loading the Microservice Engine modules in the DCE primary navigation bar.
- The `skoala-init` component is installed in the workspace cluster and provides core
  functionalities of the Microservice Engine, such as creating registry instances and gateway instances.

!!! note

    - When upgrading the Microservice Engine, both of these components need to be upgraded simultaneously to avoid version incompatibility.
    - For information on version updates of the Microservice Engine, refer to the [release notes](../intro/release-notes.md).

Since the `skoala` component is installed in the control plane cluster,
the following steps need to be performed in the control plane cluster.

1. Run the following command to back up the existing data:

    ```bash
    helm -n skoala-system get values skoala > skoala.yaml
    ```

2. Add the Helm repository for the Microservice Engine:

    ```bash
    helm repo add skoala https://release.daocloud.io/chartrepo/skoala
    ```

3. Update the Helm repository for the Microservice Engine:

    ```bash
    helm repo update
    ```

4. Run the `helm upgrade` command:

    ```bash
    helm --kubeconfig /tmp/deploy-kube-config upgrade --install --create-namespace -n skoala-system skoala skoala/skoala --version=0.28.1 --set hive.image.tag=v0.28.1 --set sesame.image.tag=v0.28.1 --set ui.image.tag=v0.19.0 -f skoala.yaml
    ```

    > You need to adjust the values of the `version`, `hive.image.tag`, `sesame.image.tag`,
    > and `ui.image.tag` parameters to the version of the Microservice Engine you want to upgrade to.

## Offline Upgrade

DCE modules are loosely coupled and support independent installation and upgrade of each module.
This document is applicable to offline upgrades performed after installing the Microservice Engine.

### Download the Offline Package

Download and extract the [Microservice Engine module](../../download/modules/skoala.md) offline package.

```shell
tar -vxf skoala_x.y.z_amd64.tar
```

After extraction, you will get four compressed packages:

- skoala-x.y.z.tgz
- skoala-init-x.y.z.tgz
- skoala_x.y.z.bundle.tar
- skoala-init_x.y.z.bundle.tar

### Synchronize Images

After downloading the images to your local nodes, you need to synchronize the latest version of
the images to your container registry using [charts-syncer](https://github.com/bitnami-labs/charts-syncer)
or a container runtime. It is recommended to use charts-syncer to synchronize images, as this method is
more efficient and convenient.

#### Synchronize Images with charts-syncer

1. Create a `load-image.yaml` file with the following content as the configuration file for charts-syncer.

    All parameters in the `load-image.yaml` file are required. You need a private container registry
    and modify the configurations according to the instructions below.
    For detailed explanations of the charts-syncer configuration file, refer to its
    [official documentation](https://github.com/bitnami-labs/charts-syncer).

    === "HARBOR chart repo installed"

        If a HARBOR chart repo is already installed in the current environment, charts-syncer also
        supports exporting the chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: skoala-offline # (1)
        target:
          containerPrefixRegistry: 10.16.10.111 # (2)
          repo:
            kind: HARBOR # (3)
            url: http://10.16.10.111/chartrepo/release.daocloud.io # (4)
            auth:
              username: "admin" # (5)
              password: "Harbor12345" # (6)
          containers:
            auth:
              username: "admin" # (5)
              password: "Harbor12345" # (6)
        ```

        1. The relative path to the execution of the charts-syncer command, not the relative path between this YAML file and the offline package
        2. Change it to the URL of your container registry
        3. It can also be any other supported Helm Chart repository type
        4. Change it to the chart repo project URL
        5. Your container registry username
        6. Your container registry password

    === "CHARTMUSEUM chart repo installed"

        If a CHARTMUSEUM chart repo is already installed in the current environment, charts-syncer
        also supports exporting the chart as a tgz file.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: skoala-offline # (1)
        target:
          containerPrefixRegistry: 10.16.10.111 # (2)
          repo:
            kind: CHARTMUSEUM # (3)
            url: http://10.16.10.111 # (4)
            auth:
              username: "rootuser" # (5)
              password: "rootpass123" # (6) 
          containers:
            auth:
              username: "rootuser" # (7)
              password: "rootpass123" # (6)
        ```

        1. The relative path to the execution of the charts-syncer command, not the relative path between this YAML file and the offline package
        2. Change it to the URL of your container registry
        3. It can also be any other supported Helm Chart repository type
        4. Change it to the chart repo URL
        5. Your container registry username. If chartmuseum does not enable login verification, you do not need to fill in auth
        6. Your container registry password
        7. Your container registry username

    === "No chart repo installed"

        If no chart repo is installed in the current environment, charts-syncer also supports
        exporting the chart as a `tgz` file and storing it in a specified path.

        ```yaml title="load-image.yaml"
        source:
          intermediateBundlesPath: skoala-offline # (1)
        target:
          containerRegistry: 10.16.23.145 # (2)
          containerRepository: release.daocloud.io/skoala # (3)
          repo:
            kind: LOCAL
            path: ./local-repo # (4)
          containers:
            auth:
              username: "admin" # (5)
              password: "Harbor12345" # (6)
        ```

        1. The relative path to the execution of the charts-syncer command, not the relative path between this YAML file and the offline package
        2. Change it to the URL of your container registry
        3. Change it to your container registry
        4. Local path of the chart
        5. Your container registry username
        6. Your container registry password

2. Put `skoala_x.y.z.bundle.tar` and `skoala-init_x.y.z.bundle.tar` in the skoala-offline folder.

3. Run the command to synchronize the images.

    ```shell
    charts-syncer sync --config load-image.yaml --insecure true
    ```

#### Synchronize Images with Docker or containerd

1. Extract the `tar` archive.

    ```shell
    tar -vxf skoala_x.y.z.bundle.tar
    ```

    After successful extraction, you will get 3 files:

    - hints.yaml
    - images.tar
    - original-chart

2. Load the images from the local directory to Docker or containerd.

    === "Docker"

        ```shell
        docker load -i images.tar
        ```

    === "containerd"

        ```shell
        ctr -n k8s.io image import images.tar
        ```

!!! note

    - You need to load the images via Docker or containerd on each node.
    - After loading, remember to tag the images to match the Registry and Repository used during installation.

### Start the Upgrade

After the images are synchronized, you can start upgrading the Microservice Engine.

=== "Upgrade via `helm repo`"

    1. Check whether the Microservice Engine Helm repository exists.

        ```shell
        helm repo list | grep skoala
        ```

        If the returned result is empty or shows the following prompt, proceed to the next step; otherwise, skip the next step.

        ```none
        Error: no repositories to show
        ```

    2. Add the Helm repository of the Microservice Engine.

        ```shell
        helm repo add skoala-release http://{harbor url}/chartrepo/{project}
        ```

    3. Update the Helm repository of the Microservice Engine.

        ```shell
        helm repo update skoala-release # (1)
        ```

        1. If the Helm version is too low, the update will fail. If it fails, try executing `helm repo update`.

    4. Choose the Microservice Engine version you want to install (it is recommended to install the latest version).

        ```shell
        helm search repo skoala-release/skoala --versions
        ```

        ```text
        NAME                   CHART VERSION  APP VERSION  DESCRIPTION
        skoala-release/skoala  0.28.1          v0.28.1       A Helm chart for Skoala
        ...
        ```

    5. Back up the `--set` parameters.

        Before upgrading the Microservice Engine version, it is recommended to run the following command to back up the `--set` parameters of the old version.

        ```shell
        helm get values skoala -n skoala-system -o yaml > bak.yaml
        ```

    6. Run `helm upgrade`.

        Before upgrading, it is recommended to overwrite the `global.imageRegistry` field in bak.yaml with the container registry address you are currently using.

        ```shell
        export imageRegistry={your container registry}
        ```

        ```shell
        helm upgrade skoala skoala-release/skoala \
        -n skoala-system \
        -f ./bak.yaml \
        --set global.imageRegistry=$imageRegistry \
        --version 0.28.1
        ```

=== "Upgrade via Chart Package"

    1. Prepare the `original-chart` (obtained by extracting `skoala_x.y.z.bundle.tar`).

    2. Back up the `--set` parameters.

        Before upgrading the Microservice Engine version, it is recommended to run the following command to back up the `--set` parameters of the old version.

        ```shell
        helm get values skoala -n skoala-system -o yaml > bak.yaml
        ```

    3. Run `helm upgrade`.

        Before upgrading, it is recommended to overwrite the `global.imageRegistry` field in bak.yaml with the container registry address you are currently using.

        ```shell
        export imageRegistry={your container registry}
        ```

        ```shell
        helm upgrade skoala original-chart \
        -n skoala-system \
        -f ./bak.yaml \
        --set global.imageRegistry=$imageRegistry
        ```

## Uninstall Microservice Engine Management Components

```bash
helm uninstall skoala -n skoala-system
```
