# 安装微服务引擎

如需安装微服务引擎，推荐通过 [DCE 5.0 商业版](../../install/commercial/start-install.md) 的安装包进行安装。通过商业版可以一次性同时安装  DCE 的所有模块。

本教程旨在补充需要手工 **单独安装** 微服务引擎的场景。下文出现的 `skoala` 是微服务引擎的内部开发代号，代指微服务引擎。

## 使用商业版安装包安装

通过商业版安装微服务引擎时，需要注意商业版的版本号（[点击查看最新版本](../../download/dce5.md)）。需要针对不同版本执行不同操作。

### 商业版 ≤ v0.3.28

执行安装命令时，默认不会安装微服务引擎。需要对照下面的配置修改 `mainfest.yaml` 以允许安装微服务引擎。

修改文件：

```bash
./dce5-installer install-app -m /sample/manifest.yaml
```

修改后的内容：

```yaml
...
components:
  skoala:
    enable: true
    helmVersion: v0.12.2
    variables:
...
```

### 商业版 ≥ v0.3.29

默认会安装微服务引擎，但仍旧建议检查 `mainfest.yaml` 文件进行确认 `components/skoala/enable` 的值是否为 `true`，以及是否指定了 Helm 的版本。

!!! note

    商业版中默认安装的是经过测试的最新版本。如无特殊情况，不建议修改默认的 Helm 版本。

## 手动安装前检测

微服务引擎由两个组件构成，在代码中分别命名为 `skoala` 和 `skoala-init`。安装微服务引擎时需要同时安装这两个组件。

### 微服务引擎部署结构

![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/install-step.png)

左侧蓝色框内的 chart 即 `skoala` 组件，需要安装在控制面集群，即 DCE 5.0 的全局集群 `kpanda-global-clsuter`，详情可参考 DCE 5.0 的[部署架构](../../install/commercial/deploy-arch.md)。安装 `skoala` 组件之后即可以在 DCE 5.0 的一级导航栏中看到微服务引擎模块。另外需要注意：安装 `skoala` 之前需要安装好其依赖的 `common-mysql` 组件用于存储资源。

右侧蓝色框内的 chart 即 `skoala-init` 组件，需要安装在工作集群。安装 `skoala-init` 组件之后即可以使用微服务引擎的各项功能，例如创建注册中心、网关实例等。另外需要注意，`skoala-init` 组件依赖  DCE 5.0 可观测模块的 `insight-agent` 组件提供指标监控和链路追踪等功能。如您需要使用该项功能，则需要事先安装好 `insight-agent` 组件，具体步骤可参考[安装组件 insight-agent](../../insight/user-guide/quickstart/install-agent.md)。

### 检测微服务引擎是否已安装

查看 `skoala-system` 命名空间中是否有以下对应的资源。如果没有任何资源，说明目前尚未安装微服务引擎。

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

### 检测依赖的存储组件

安装微服务引擎时需要用到 `common-mysql` 组件来存储配置，所以要确保该组件已经存在。此外，还需要查看 `common-mysql` 命名空间中是否有名为 `skoala` 的数据库。

```bash
~ kubectl -n mcamel-system get statefulset
NAME                                          READY   AGE
mcamel-common-mysql-cluster-mysql             2/2     7d23h
```

建议使用如下参数为微服务引擎配置数据库信息：

- host: mcamel-common-mysql-cluster-mysql-master.mcamel-system.svc.cluster.local
- port: 3306
- database : skoala
- user: skoala
- password:

### 检测依赖的监控组件

微服务引擎依赖 [DCE 5.0 可观测性](../../insight/intro/what.md)模块的能力。如您需要监控微服务的各项指标、追踪链路，则需要在集群中安装对应的 `insight-agent`，具体说明可参考[](../../insight/user-guide/quickstart/install-agent.md)。

![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/cluster-list.png)

!!! note

    - 如果安装 `skoala-init` 之前没有事先安装 `insight-agent`，则不会安装 `service-monitor`。
    - 如果需要安装 `service-monitor`，请先安装 `insight-agent`，然后再安装 `skoala-init`。

## 手动安装过程

一切就绪之后，就可以开始正式安装微服务引擎了。具体的流程如下：

~~### 初始化数据库表~~

!!! note

    - 此步骤仅适用于安装 skoala-release/skoala 版本 v0.17.1 以下的版本。
    - 如果安装 skoala-release/skoala 版本 v0.17.1 及更高版本，直接跳过此步骤执行下一步。系统会自动完成表格初始化，无需手动进行。

~~如果在 common-mysql 内的 skoala 数据库为空，请登录到 skoala 数据库后，执行以下 SQL：~~

??? note "如果初始化失败，请检查 skoala 数据库内是否有下方 3 张数据表以及对应的 SQL 是否全部生效。"

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

### 配置 skoala helm repo

配置好 skoala 仓库，即可查看和获取到 skoala 的应用 chart

```bash
~ helm repo add skoala-release https://release.daocloud.io/chartrepo/skoala
~ helm repo update
```

> 需要事先安装 Helm

重点内容：增加完成后 Skoala-release 之后，常用需要关注的有 2 个 Chart：

- Skoala 是 Skoala 的控制端的服务，
    - 安装完成后，可以网页看到微服务引擎的入口
    - 包含 3 个组件 ui、hive、sesame
    - 需要安装在全局管理集群
- Skoala-init 是 Skoala 所有的组件 Operator
    - 仅安装到指定工作集群即可
    - 包含组件有：skoala-agent, nacos, contour, sentinel
    - 未安装时，创建注册中心和网关时会提示缺少组件

默认情况下，安装完成 skoala 到 kpanda-global-cluster(全局管理集群)，就可以在侧边栏看到对应的微服务引擎的入口了。

### 查看 skoala 组件最新版本

升级部署脚本，一键部署全部组件。

在全局管理集群，查看 Skoala 的最新版本，直接通过 helm repo 来更新获取最新的；

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

> 在部署 skoala 时，会携带当时最新的前端版本，如果想要指定前端 ui 的版本，
> 可以去看前端代码仓库获取对应的版本号：

在工作集群，查看 skoala-init 的最新版本，直接通过 helm repo 来更新获取最新的

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

### 执行部署（同样适用于升级）

直接执行命令即可，注意对应的版本号

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

> 自定义并初始化数据库参数；需要将数据库信息做配置添加进去
> --set sweet.enable=true \
> --set hive.configMap.data.database.host= \
> --set hive.configMap.data.database.port= \
> --set hive.configMap.data.database.user= \
> --set hive.configMap.data.database.password= \
> --set hive.configMap.data.database.database= \
>
> 自定义前端 ui 版本
> ui.image.tag=v0.9.0

查看部署的 pod 是否启动成功

```bash
~ kubectl -n skoala-system get pods
NAME                                   READY   STATUS    RESTARTS        AGE
hive-8548cd9b59-948j2                  2/2     Running   2 (3h48m ago)   3h48m
sesame-5955c878c6-jz8cd                2/2     Running   0               3h48m
ui-7c9f5b7b67-9rpzc                    2/2     Running   0               3h48m
```

### 安装 skoala-init 到工作集群

由于 Skoala 涉及的组件较多，我们将这些组件打包到同一个 Chart 内，也就是 skoala-init，所以我们应该在用到微服务引擎的工作集群安装好 skoala-init

```bash
~  helm search repo skoala-release/skoala-init --versions
NAME                        CHART VERSION   APP VERSION DESCRIPTION
skoala-release/skoala-init  0.13.0          0.13.0      A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init  0.12.2          0.12.2      A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init  0.12.1          0.12.1      A Helm Chart for Skoala init, it includes Skoal...
skoala-release/skoala-init  0.12.0          0.12.0      A Helm Chart for Skoala init, it includes Skoal...
......
```

安装命令，同更新; 确认需要安装到指定的命名空间，确认看到全部 Pod 启动成功。

```bash
~ helm upgrade --install skoala-init --create-namespace -n skoala-system --cleanup-on-fail \
    skoala-release/skoala-init \
    --version 0.13.0
```

除了通过终端安装，UI 的方式 可以在 Kpanda 集群管理中 Helm 应用内找到 Skoala-init 进行安装。

![image](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/images/skoala-init.png)

卸载命令

```bash
~ helm uninstall skoala-init -n skoala-system
```

常见问题：

- 安装之后如何卸载微服务引擎？

    执行如下命令即可：

    ```bash
    ~ helm uninstall skoala -n skoala-system
    ```

- 后续如何更新微服务器引擎？

    支持离线升级和在线升级两种方式，具体可参考[离线升级](../quickstart/offline-upgrade.md)或[在线升级](online-upgrade.md)
