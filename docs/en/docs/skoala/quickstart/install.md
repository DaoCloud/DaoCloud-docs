# Install the microservice engine

If you need to install the micro-service engine, you are advised to install it in the installation package [DCE 5.0 Business Release](../../install/commercial/start-install.md). With the Commercial Release, you can install all of the DCE modules at once.

This tutorial is intended to complement scenarios that require a manual **Separate installation** microservice engine. `skoala` appears below is the internal development code of the micro-service engine, and refers to the micro-service engine.

## Use the commercial version installer

When installing the microservice engine through the commercial Release, note the version number of the commercial edition ([Latest Versions](../../download/dce5.md)). You need to perform different operations for different versions.

### Commercial version ≤ v0.3.28

By default, the microservice engine is not installed when the installation command is executed. You need to modify `mainfest.yaml` against the configuration below to allow the microservice engine to be installed.

Modify the file:

```bash
./dce5-installer install-app -m /sample/manifest.yaml
```

The revised content:

```yaml
...
components:
  skoala:
    enable: true
    helmVersion: v0.12.2
    variables:
...
```

### Commercial version ≥ v0.3.29

The microservice engine is installed by default, but it is still recommended to check the `mainfest.yaml` file to make sure that the `components/skoala/enable` value is `true` and that the version of Helm is specified.

!!! note

## Check before manual installation

The microservice engine consists of two components named in the code `skoala` and `skoala-init`. Both components must be installed when installing the microservice engine.

### Microservice engine deployment structure

<!--![]()screenshots-->

chart in the blue box on the left is the component `skoala`, which needs to be installed in the control plane cluster, namely the global cluster `kpanda-global-clsuter` of DCE 5.0. For details, please refer to [Deploy Architecture](../../install/commercial/deploy-arch.md) of DCE 5.0. After installing the `skoala` component, you can see the microservice engine module in the level 1 navigation bar of DCE 5.0. Note the following: Before installing `skoala`, install the `common-mysql` component that is used for storage resources.

chart in the blue box on the right is the `skoala-init` component that needs to be installed in the working cluster. After the `skoala-init` component is installed, various features of the microservice engine, such as creating registries, gateway instances, and so on, are available. Also note that the `skoala-init` component relies on the `insight-agent` component of the DCE 5.0 observable module to provide metrics monitoring and link tracking. If you want to use this function, install the `insight-agent` component. For details, see [Install the insight agent component ](../../insight/user-guide/quickstart/install-agent.md).

### Check whether the microservice engine is installed

Check whether the following resources exist in the `skoala-system` namespace. If no resources are available, the microservice engine is not currently installed.

```bash
~ kubectl -n skoala-system get pods
NAME                                   READY   STATUS    RESTARTS        AGE
hive-8548cd9b59-948j2                  2/2     Running   2 (3h48m ago)   3h48m
sesame-5955c878c6-jz8cd                2/2     Running   0               3h48m
ui-7c9f5b7b67-9rpzc                    2/2     Running   0               3h48m
 
~ helm -n skoala-system list
NAME        NAMESPACE       REVISION    UPDATED                                 STATUS      CHART               APP VERSION
skoala      skoala-system   3           2022-12-16 11:17:35.187799553 +0800 CST deployed    skoala-0.13.0       0.13.0
```

### Detect dependent storage components

The `common-mysql` component is required to store the configuration when installing the microservice engine, so make sure it already exists. In addition, you need to see if there is a database named `skoala` in the `common-mysql` namespace.

```bash
~ kubectl -n mcamel-system get statefulset
NAME                                          READY   AGE
mcamel-common-mysql-cluster-mysql             2/2     7d23h
```

You are advised to set the following parameters to configure database information for the micro-service engine:

- host: mcamel-common-mysql-cluster-mysql-master.mcamel-system.svc.cluster.local
- port: 3306
- database : skoala
- user: skoala
- password:

### Monitor components that detect dependencies

The microservice engine relies on the capabilities of the [ DCE 5.0 Observability](../../insight/intro/what.md) module. If you want to monitor metrics of the micro-service and trace traces, install corresponding `insight-agent` in the cluster. For details, see [](../../insight/user-guide/quickstart/install-agent.md).

<!--![]()screenshots-->

!!! note

    - If the installation before `skoala-init` without prior to install `insight-agent`, do not install `service-monitor`.
    - If you need to install the `service-monitor`, please install the `insight-agent`, and then install `skoala-init`.

## Manual installation procedure

With everything in place, you can begin the formal installation of the microservice engine. The specific process is as follows:

~~### Initializes the database table ~~

!!! note

    - This step only applies to skoala-release/skoala version v0.17.1 or later.
    - If skoala-Release /skoala version v0.17.1 or later is installed, skip this step and go to the next step. The system automatically initializes the table.

~~ If skoala database in common-mysql is empty, log in to skoala database and run the following SQL: ~~

????? note "If the initialization fails, check whether the following three tables exist in the skoala database and whether the corresponding SQL has taken effect."

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

### Configure skoala helm repo

After skoala registry is configured, skoala application chart can be viewed and obtained

```bash
~ helm repo add skoala-release https://release.daocloud.io/chartrepo/skoala
~ helm repo update
```

> The Helm needs to be installed beforehand

Key content: After the completion of Skoala-release, there are two charts that need to be paid attention to:

- Skoala is the control side service of Skoala,
    - After the installation is complete, you can see the entry of the micro-service engine on the web page
    - Contains 3 components ui, hive and sesame
    - It must be installed in the global management cluster
- Skoala-init is the Operator of all Skoala components
    - Install it only to the specified working cluster
    - Included components: skoala-agent, nacos, contour, sentinel
    - When not installed, you are prompted for missing components when you create the registry and gateway

By default, after installing skoala to kpanda-global-cluster, you will see the entry to the corresponding microservice engine in the sidebar.

### View the latest version of the skoala component

Upgrade the deployment script to deploy all components with one click.

In the global management cluster, check the latest version of Skoala, directly through the helm repo update to get the latest;

```bash
~ helm repo update skoala-release
~ helm search repo skoala-release/skoala --versions
NAME                        CHART VERSION   APP VERSION DESCRIPTION
skoala-release/skoala       0.13.0          0.13.0      The helm chart for Skoala
skoala-release/skoala       0.12.2          0.12.2      The helm chart for Skoala
skoala-release/skoala       0.12.1          0.12.1      The helm chart for Skoala
skoala-release/skoala       0.12.0          0.12.0      The helm chart for Skoala
......
```

> When skoala is deployed, it takes the most recent front-end version with it. If you want to specify the front-end ui version,
> See the front-end code repository for the corresponding version number:

In the working cluster, look at the latest version of skoala-init and update directly through helm repo to get the latest one

```bash
~ helm repo update skoala-release
~ helm search repo skoala-release/skoala-init --versions
NAME                        CHART VERSION   APP VERSION DESCRIPTION
skoala-release/skoala-init  0.13.0          0.13.0      A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init  0.12.2          0.12.2      A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init  0.12.1          0.12.1      A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init  0.12.0          0.12.0      A Helm Chart for Skoala init, it includes Skoal...
......
```

### Perform deployment (also for upgrades)

Run the command directly. Note the corresponding version number

```bash
~ helm upgrade --install skoala --create-namespace -n skoala-system --cleanup-on-fail \
    --set ui.image.tag=v0.9.0 \
    --set sweet.enable=true \
    --set hive.configMap.data.database.host=mcamel-common-mysql-cluster-mysql-master.mcamel-system.svc.cluster.local \
    --set hive.configMap.data.database.port=3306 \
    --set hive.configMap.data.database.user=root \
    --set hive.configMap.data.database.password=xxxxxxxx \
    --set hive.configMap.data.database.database=skoala \
    skoala-release/skoala \
    --version 0.13.0
```

> Customize and initialize database parameters; The database information needs to be added to the configuration
> --set sweet. enable=true \
> --set hive.configMap.data.database. host= \
> --set hive.configMap.data.database. port= \
> --set hive.configMap.data.database. user= \
> --set hive.configMap.data.database. password= \
> --set hive.configMap.data.database. database= \
>
> Customize the front-end ui version
> ui.image.tag=v0.9.0

Check whether the deployed pod is successfully started

```bash
~ kubectl -n skoala-system get pods
NAME                                   READY   STATUS    RESTARTS        AGE
hive-8548cd9b59-948j2                  2/2     Running   2 (3h48m ago)   3h48m
sesame-5955c878c6-jz8cd                2/2     Running   0               3h48m
ui-7c9f5b7b67-9rpzc                    2/2     Running   0               3h48m
```

### Install skoala-init to the working cluster

Since skoala involves a large number of components, we package these components into the same Chart, which is Skoala-init, so we should install Skoala-init in the working cluster that uses the micro-service engine

```bash
~  helm search repo skoala-release/skoala-init --versions
NAME                        CHART VERSION   APP VERSION DESCRIPTION
skoala-release/skoala-init  0.13.0          0.13.0      A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init  0.12.2          0.12.2      A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init  0.12.1          0.12.1      A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init  0.12.0          0.12.0      A Helm Chart for Skoala init, it includes Skoal...
......
```

Installation command, with the update; Verify that you need to install the Pods in the specified namespace and that all Pods have started successfully.

```bash
~ helm upgrade --install skoala-init --create-namespace -n skoala-system --cleanup-on-fail \
    skoala-release/skoala-init \
    --version 0.13.0
```

In addition to terminal installation, UI can be found in the Helm application in Kpanda cluster management Skoala-init for installation.

<!--![]()screenshots-->

Unload command

```bash
~ helm uninstall skoala-init -n skoala-system
```

Frequently asked Questions:

- How do I uninstall the microservice engine after installation?

    run the following command:

    ```bash
    ~ helm uninstall skoala -n skoala-system
    ```

- How to update the microserver engine?

    Supports offline upgrade and online upgrade. For details, see [Offline Upgrade](../quickstart/offline-upgrade.md) or [Online Upgrade](online-upgrade.md).
