# Install Guides

It is recommended to install DaoCloud Microservice Engine (DME) through the installation package of [DCE 5.0 Enterprise](../../install/commercial/start-install.md), because you can install all modules of DCE 5.0 once a time with that package, no need to worry about incompatibility.

This guides is designed for **manual online install of DME alone**. To be clear, `skoala` mentioned below is the internal development code of DME.

!!! note

    If you have already deployed DCE 5.0 Enterprise, it is recommended to see [Offline Upgrade Microservice Engine](offline-upgrade.md) for DME's offline install and upgrade. 

## Install with Enterprise Package

When the installer version of DCE 5.0 Enterprise **≥ v0.3.29**, DME will be installed by default. However, it is still recommended to check the `mainfest.yaml` file to confirm whether the value of `components/skoala/enable` is `true`, and whether the helm version is specified.

!!! note

    The enterprise package will install by default the latest version of DME that has passed internal tests. Unless there are special requirements, it is not recommended to modify the default Helm version.

??? note "If intaller version of DCE 5.0 Enterprise ≤ v0.3.28, click to see corresponding actions"

    This note applies only when installer version of DCE 5.0 Enterprise ≤ v0.3.28; in most cases your version will be greater than this.

    When executing the installation command, DME will not be installed by default. You need to change the `mainfest.yaml` according to the configuration below.

    Modify the file:

    ```bash
    ./dce5-installer install-app -m /sample/manifest.yaml
    ```

    Modified content:

    ```yaml
    ...
    components:
      skoala:
        enable: true
        helmVersion: v0.12.2 # replace with the latest version number
        variables:
    ...
    ```

## Manual Separate Install

DME consists of two components: `skoala` and `skoala-init`. Both are necessary for normal running of DME.

### Deployment Structure

![images](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/install01.jpg)

Chart in the blue box on the left is the component `skoala`, which needs to be installed in the control plane cluster, namely the global cluster `kpanda-global-clsuter` of DCE 5.0. For details, refer to [Deploy Architecture](../../install/commercial/deploy-arch.md) of DCE 5.0. After installing the `skoala` component, you can see DME module in the navigation bar of DCE 5.0. Note: Before installing `skoala`, install the `common-mysql` component for storage.

Chart in the blue box on the right is the `skoala-init` component that needs to be installed in a worker cluster. After `skoala-init` is installed, various features of DME are available, such as creating registries, gateway instances, and so on. Also note that `skoala-init` relies on the `insight-agent` component of the DCE 5.0 observability module to provide metrics monitoring and tracing. If you want to use observability, install the `insight-agent` component first. For details, see [Install the insight agent component](../../insight/quickstart/install/install-agent.md).

### Pre-install Check

#### If DME is already installed

Check whether the following resources exist in the `skoala-system` namespace. If no resources, it means DME is not installed yet.

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

#### If `common-mysql` is installed

The `common-mysql` component is required to store the configuration when installing DME, so make sure it already exists. In addition, you need to see if there is a database named `skoala` in the `common-mysql` namespace.

```bash
~ kubectl -n mcamel-system get statefulset
NAME                                          READY   AGE
mcamel-common-mysql-cluster-mysql             2/2     7d23h
```

It is recommended to set the database configuration as the following:

- host: mcamel-common-mysql-cluster-mysql-master.mcamel-system.svc.cluster.local
- port: 3306
- database : skoala
- user: skoala
- password:

#### If `insight-agent` is installed

DME relies on the capabilities of the [DCE 5.0 Observability](../../insight/intro/index.md) module to provide microservice monitoring. If you want to monitor metrics and trace links, you should install `insight-agent` in the cluster. For details, see [](../../insight/quickstart/install/install-agent.md).

![images](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/install02.png)

!!! note

    - If `insight-agent` is not install when you install `skoala-init`, `service-monitor` won't be installed.
    - If you need to install `service-monitor`, you should install `insight-agent` first, and then install `skoala-init`.

### Start Install

With everything in place, you can start installing DME. The specific process is as follows:

#### Initialize data table

!!! note

    If you install skoala v0.17.1 or later, skip this step. The data table will be automatically initialized.

If skoala database in common-mysql is empty, log in to skoala database and run the following SQL command:

??? note "If initialization fails, check whether the following three tables exist in the skoala database and whether the corresponding SQL has taken effect."

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

#### Configure skoala helm repo

After skoala container registry is configured, you can check and get the Helm chart of skoala.

```bash
~ helm repo add skoala-release https://release.daocloud.io/chartrepo/skoala
~ helm repo update
```

> install Helm beforehand

Note: After `skoala-release` container registry is added, there are two charts that need to be paid attention to:

- `skoala` is the control plane of DME
    - After `skoala` is installed, you can see DME in the first-level navigation bar of DCE 5.0
    - `skoala` contains 3 components: ui, hive and sesame
    - It must be installed in the global management cluster

- `skoala-init` is the operator of all components of DME
    - Install it only to a working cluster
    - Include four components: skoala-agent, nacos, contour, sentinel
    - If `skoala-init` is not installed, you are prompted for missing components when creating a registry or gateway

By default, after installing `skoala` component to the global cluster, you will see the "Microservices" option in the sidebar of DCE 5.0.

#### Check latest version of DME's components

In the global management cluster, check the latest version of `skoala` directly by this helm command.

```bash
~ helm repo update skoala-release
~ helm search repo skoala-release/skoala --versions
NAME                        CHART VERSION   APP VERSION DESCRIPTION
skoala-release/skoala       0.28.1       	0.28.1     	The helm chart for Skoala
skoala-release/skoala       0.28.0       	0.28.0     	The helm chart for Skoala
skoala-release/skoala       0.27.2       	0.27.2     	The helm chart for Skoala
skoala-release/skoala       0.27.1       	0.27.1     	The helm chart for Skoala
......
```

In the working cluster, check the latest version of `skoala-init` directly by this helm command.

```bash
~ helm repo update skoala-release
~ helm search repo skoala-release/skoala-init --versions
NAME                        CHART VERSION   APP VERSION DESCRIPTION
skoala-release/skoala-init	0.28.1       	0.28.1     	A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init	0.28.0       	0.28.0     	A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init	0.27.2       	0.27.2     	A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init	0.27.1       	0.27.1     	A Helm Chart for Skoala init, it includes Skoal...
......
```

#### Install/Upgrade `skoala` to the global cluster

Run the command directly to deploy or upgrade `skoala`. Pay attention to setting a right version.

```bash
$ helm upgrade --install skoala --create-namespace -n skoala-system --cleanup-on-fail \
    --set ui.image.tag=v0.19.0 \
    --set hive.configMap.database[0].driver="mysql" \
    --set hive.configMap.database[0].dsn="skoala:xxx@tcp(mcamel-common-mysql-cluster-mysql-master.mcamel-system.svc.cluster.local:3306)/skoala?charset=utf8&parseTime=true&loc=Local&timeout=10s" \
    skoala-release/skoala \ 
    --version 0.28.1
```

Check whether the Pod is successfully started:

```bash
~ kubectl -n skoala-system get pods
NAME                                   READY   STATUS    RESTARTS        AGE
hive-8548cd9b59-948j2                  2/2     Running   0               3h48m
sesame-5955c878c6-jz8cd                2/2     Running   0               3h48m
skoala-ui-7c9f5b7b67-9rpzc             2/2     Running   0               3h48m
```

#### Install/upgrade `skoala-init` to a working cluster

Since DME contains many components, we packaged these components into the same Chart, which is `skoala-init`. This installation command can also be used to upgrade the component.

```bash
~  helm search repo skoala-release/skoala-init --versions
NAME                        CHART VERSION   APP VERSION DESCRIPTION
skoala-release/skoala-init	0.28.1       	0.28.1     	A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init	0.28.0       	0.28.0     	A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init	0.27.2       	0.27.2     	A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init	0.27.1       	0.27.1     	A Helm Chart for Skoala init, it includes Skoal...
......
```

Use the following command to check all Pods are running as expected：

```bash
~ helm upgrade --install skoala-init --create-namespace -n skoala-system --cleanup-on-fail \
    skoala-release/skoala-init \
    --version 0.28.1
```

In addition to terminal installation, you can also install `skoala-init` by Helm chart in `Container Management` -> `Helm App`.

![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/install03.png)

## Upgrade DME

Supports offline upgrade and online upgrade. For details, see [Offline Upgrade](../quickstart/offline-upgrade.md) or [Online Upgrade](online-upgrade.md).

## Unload DME

```bash
~ helm uninstall skoala-init -n skoala-system
```

```bash
~ helm uninstall skoala -n skoala-system
```
