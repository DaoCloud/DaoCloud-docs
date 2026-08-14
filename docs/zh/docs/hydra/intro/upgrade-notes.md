# 升级注意事项

本页说明将 Hydra 升级到新版本时需要注意的相关事项。

## 从 v0.16.0（或更低版本）升级到 v0.17.1

Hydra 从 v0.17.1 开始，将原先混在 `model` 表中的模型元数据与 MaaS 相关数据解耦：
新增 `maas_model` 表存储 MaaS 信息，`model` 表中的 MaaS 字段在迁移完成后将逐步废弃。
为避免升级过程中模型元数据丢失，升级前请先完成下述数据表迁移。

!!! warning

    Model 与 MaaS 的解耦仍在进行中，后续可能将 `maas_model` 表信息直接记录到 Knoway 相关资源中，
    该表未来可能会被移除。如果没有升级到 v0.17.1 的特别需要，建议暂缓升级，待解耦工作完成后再升级。

!!! note

    以下操作在 Global 集群执行。

1. 查看 Hydra 当前连接的数据库

    ```bash
    APP_NS=hydra-system
    kubectl -n "$APP_NS" get cm hydra -o jsonpath='{.data.config\.yaml}' | sed -n '/^db_config:/,/^[^ ]/p'
    ```

    请重点确认 host、port、数据库名、用户名和密码。输出类似于：

    ```yaml
    db_config:
      dbType: mysql
      dsn: hydra:hydraPwd@tcp(mcamel-common-mysql-cluster-mysql-master.mcamel-system.svc.cluster.local:3306)/hydra?charset=utf8mb4&parseTime=true&loc=Local
      autoMigrate: true
      debug: false
    ```

1. 根据数据库连接参数准备环境变量，并准备迁移文件 `create_maas_model.sql`

    ```bash
    APP_NS=hydra-system
    DB_NS=mcamel-system
    DB_POD=mcamel-common-mysql-cluster-mysql-0
    DB_HOST=mcamel-common-mysql-cluster-mysql-master.mcamel-system.svc.cluster.local
    DB_PORT=3306
    DB_NAME=hydra
    DB_USER=hydra
    # 将迁移文件准备到对应目录
    SQL_FILE=/home/create_maas_model.sql
    ```

    !!! note

        请按上一步 ConfigMap 中的实际连接信息修改上述变量，不要直接使用示例值。

1. 将 SQL 文件拷贝到 MySQL Pod

    ```bash
    kubectl -n "$DB_NS" cp "$SQL_FILE" "$DB_POD:/tmp/$(basename "$SQL_FILE")" -c mysql
    ```

1. 进入 MySQL Pod

    ```bash
    kubectl -n "$DB_NS" exec -it "$DB_POD" -- bash
    ```

    进入 Pod 后，请重新设置与第 2 步相同的环境变量，再执行后续命令。

1. （可选）备份 `model` 表。若当前账号有权限，可先执行：

    ```bash
    mysqldump -h "$DB_HOST" -P "$DB_PORT" -u "$DB_USER" -p "$DB_NAME" model > /tmp/hydra-model-maas-backup.sql
    ```

    执行后会提示输入 hydra 数据库密码。该命令只备份 `model` 表。

1. 执行迁移

    ```bash
    mysql -h "$DB_HOST" -P "$DB_PORT" -u "$DB_USER" -p "$DB_NAME" < "/tmp/$(basename "$SQL_FILE")"
    ```

    同样会提示输入密码。密码来自 hydra ConfigMap 中 DSN 对应的密码，请手工输入，不要写进命令行。

1. 校验迁移结果

    ```bash
    mysql -h "$DB_HOST" -P "$DB_PORT" -u "$DB_USER" -p "$DB_NAME"
    ```

    进入 MySQL 后执行：

    ```sql
    SHOW TABLES LIKE 'maas_model';

    SELECT COUNT(*) AS actual_count FROM maas_model;

    SELECT COUNT(*) AS expected_count
    FROM model
    WHERE del_flag = 0
      AND (
        public_endpoint_enabled = 1
        OR COALESCE(public_endpoint_base_url, '') <> ''
        OR COALESCE(public_access_model_name, '') <> ''
        OR COALESCE(public_endpoint_cluster, '') <> ''
      );

    SELECT model_id, workspace_visibility_scope
    FROM maas_model
    LIMIT 10;
    ```

    `actual_count` 应与 `expected_count` 一致；`workspace_visibility_scope` 应为 `ALL`。

## 从 v0.14.1（或更低版本）升级到 v0.15.0

hydra 从 v0.15.0 版本开始，在 knoway 网关中集成了 higress，以提供 AI 安全、token 限额等能力，升级时需要注意以下事项：

1. 默认 higress 是禁用的，需要在 hydra-agent 的 helm value 中配置开启：

    ```yaml
     knoway:
       higress:
         enabled: true
    ```

2. 在 v0.15.0 版本中，全局服务集群安装的 hydra 和子集群的 hydra-agent 版本是绑定的，升级全局集群的 hydra 或者子集群中的
   hydra-agent 的任意组件，都必须同步升级。否则会影响用量上报和计费功能。

3. 在启用了 higress 后，默认内置了产品必须的 wasm plugin CR，因此需要首先在安装 hydra-agent
   的集群中手动 apply CRD，否则会导致 hydra-agent 安装失败，apply 步骤如下（在对应的子集群中执行）：

    ```bash
    helm repo add hydra https://release.daocloud.io/chartrepo/hydra
    helm repo update hydra
    helm pull hydra/hydra-agent --version v0.15.0 --untar
    kubectl apply -f hydra-agent/crds/
    ```

4. 启用 Higress 后，可在运维管理中配置[安全策略管理](../oam/security-policy.md)，
   并在[安全审计日志](../oam/security-audit-logs.md)中查询策略触发记录。

## 从 v0.12.1（或更低版本）升级到 v0.13.1

Hydra-agent 从 0.13.1 版本开始不再内置 dataset 组件，需要单独通过 addon 仓库安装，
为保证以前的 dataset CR 在升级之后不会丢失，请参考下述步骤进行升级。

!!! note

    以下升级操作需要在每个子集群都执行一遍。

1. 查看目前安装的 hydra-agent 以及所有的 dataset

    ```bash
    cloudshell-worker-ct8cbvdtb6:~# helm ls -n hydra-system | grep agent
    ```
    ```
    hydra-agent     hydra-system    1               2026-03-16 10:02:15.663202599 +0000 UTC deployed        hydra-agent-v0.12.3             v0.12.3           

    cloudshell-worker-ct8cbvdtb6:~# kubectl get datasets.dataset.baizeai.io -A
    NAMESPACE      NAME           TYPE          URI                            PHASE
    hydra-system   qwen3-0-6b-1   MODEL_SCOPE   modelscope://Qwen/Qwen3-0.6B   PROCESSING
    ```

1. 执行以下命令修改 CRD，也可以在界面上编辑 CRD 的 yaml 添加 annotation 实现

    通过 Helm 的机制 resource-policy=keep 使得 helm 升级的时候跳过此资源，同时修改
    dataset 这个 CRD 的 release 相关字段，确保后续单独安装 dataset 不报错。

    ```bash
    cloudshell-worker-ct8cbvdtb6:~# kubectl annotate crd datasets.dataset.baizeai.io  \
    meta.helm.sh/release-name=dataset \
    meta.helm.sh/release-namespace=dataset-system \
    helm.sh/resource-policy=keep \
    --overwrite
    customresourcedefinition.apiextensions.k8s.io/datasets.dataset.baizeai.io annotated
    ```

1. 执行以下命令修改 CR

    !!! note

        推荐使用命令行的形式,可以一键修改，否则每个 CR 都需要改一遍。

    ```bash
    cloudshell-worker-ct8cbvdtb6:~# kubectl annotate datasets.dataset.baizeai.io -A --all helm.sh/resource-policy=keep
    dataset.dataset.baizeai.io/qwen3-0-6b-1 annotated
    ```

1. 开始升级

    !!! note

        Hydra-agent 从 v0.12.1 -> v0.13.1，移除了 dataset 组件。

    进入工作集群 的 **Helm 应用** -> **Helm 应用** 页面，找到 **hydra-agent** 插件并更新。

1. 验证 dataset

    ```bash
    cloudshell-worker-ct8cbvdtb6:~# kubectl get datasets.dataset.baizeai.io -A
    ```
    ```
    NAMESPACE      NAME           TYPE          URI                            PHASE
    hydra-system   qwen3-0-6b-1   MODEL_SCOPE   modelscope://Qwen/Qwen3-0.6B   PROCESSING
    ```

1. 安装 dataset helm 应用

    进入工作集群 的 **Helm 应用** -> **Helm 模板** 页面，找到 **dataset** 插件并安装。

1. 此时可以去掉 keep 的 annotation 了

    ```bash
    cloudshell-worker-l2vhhlz6f4:~# kubectl annotate crd datasets.dataset.baizeai.io helm.sh/resource-policy-
    customresourcedefinition.apiextensions.k8s.io/datasets.dataset.baizeai.io annotated

    cloudshell-worker-l2vhhlz6f4:~# kubectl annotate datasets.dataset.baizeai.io -A --all helm.sh/resource-policy-
    dataset.dataset.baizeai.io/qwen3-0-6b-1 annotated
    ```

1. 更新 dataset

    为了确保旧的 CRD 的定义和最新的 dataset 保持一致，需要更新 dataset 插件。

    !!! note

        不需要改任何参数，直接更新即可。
