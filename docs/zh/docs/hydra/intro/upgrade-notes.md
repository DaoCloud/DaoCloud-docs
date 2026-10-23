# 升级注意事项

本页说明将 Hydra 升级到新版本时需要注意的相关事项。请根据当前版本选择对应章节。

## 从 v0.16.0 / v0.17.1 升级到 v0.18.3 {#upgrade-to-v0183}

Hydra 从 v0.18.3 开始，MaaS 启停状态、集群和 Workspace 可见范围统一以 Knoway `ModelRoute` CR 为准。
旧数据库字段暂时保留，仅作为升级迁移源。

升级 `hydra-agent` 会自动升级 Knoway。Knoway 是 `hydra-agent` Chart 的子 Chart，默认 `knoway.enabled=true`，无需单独升级。

!!! warning

    必须按以下顺序执行：先备份数据库和 `ModelRoute`，再升级所有工作集群的 `hydra-agent`（由其自动升级 Knoway），
    然后升级全局服务集群的 Hydra，最后检查 MaaS 迁移结果。

    如果环境配置了 `knoway.enabled=false`，或 Knoway 由独立 Helm Release 管理，必须先单独升级 Knoway，再升级全局服务集群的 Hydra。

!!! note

    从 v0.16.0 直升 v0.18.3 时，**不要**执行 `create_maas_model.sql`。
    升级 Job 会在没有 `maas_model` 表时自动读取 `model` 表。

本节适用于：

- 从 v0.17.1 升级到 v0.18.3
- 从 v0.16.0（未执行 MaaS 数据表迁移）直升到 v0.18.3

| 起始版本 | 自动使用的迁移源 | 迁移结果 |
| -------- | ---------------- | -------- |
| v0.17.1 | `maas_model` 表 | 保留启停状态及 `ALL` / `SPECIFIED` Workspace 可见范围 |
| v0.16.0 | `model.public_endpoint_*` | 保留启停状态，可见范围统一设置为 `ALL` |

全局服务集群升级会先运行 `hydra-maas-migrate` Job。迁移失败会阻断升级，新 apiserver 不会提前滚动。

### 升级前准备

1. 备份数据库。至少备份以下数据：

    - `model` 表
    - v0.17.1 环境的 `maas_model` 表
    - 条件允许时，备份整个 Hydra 数据库

    建议由 DBA 使用受控凭据执行备份。不要把数据库密码写入命令、脚本或工单。

    查看 Hydra 当前连接的数据库，可参考下文[从 v0.16.0（或更低版本）升级到 v0.17.1](#upgrade-to-v0171) 中的步骤。

1. 导出 `ModelRoute`。在每个工作集群执行：

    ```bash
    kubectl get modelroutes.llm.knoway.dev -A -o yaml > <worker>-modelroutes-backup.yaml
    ```

    将 `<worker>` 替换为工作集群名称，便于区分备份文件。

### 升级工作集群 hydra-agent

在每个工作集群的 **Helm 应用** 页面升级 **hydra-agent**。建议先升级一个非核心集群，确认正常后再升级其余集群。

默认情况下，此操作会同时自动升级：

- Knoway Controller 和 Gateway
- `ModelRoute` CRD
- hydra-agent 其他组件

每个工作集群升级后执行以下检查：

```bash
kubectl -n hydra-system get pods
kubectl get crd modelroutes.llm.knoway.dev
kubectl get modelroutes.llm.knoway.dev -A
kubectl explain modelroute.spec.enabled --api-version=llm.knoway.dev/v1alpha1
kubectl explain modelroute.spec.metadata.visibilityScope --api-version=llm.knoway.dev/v1alpha1
kubectl explain modelroute.spec.metadata.visibleWorkspaces --api-version=llm.knoway.dev/v1alpha1
```

进入下一步的条件：hydra-agent 和 Knoway Pod 全部 Ready，且上述三个 `ModelRoute` 字段均存在。

!!! note

    最新 Chart 已避免把同一 hydra-agent Release 原有的 NodePort 误判为冲突。
    如果仍提示端口被其他 Service 使用，说明存在真实冲突，需要调整端口后重试。

### 升级全局服务集群 Hydra

所有工作集群 hydra-agent 升级完成后，在全局服务集群的 **Helm 应用** 页面升级 Hydra。

升级期间观察 MaaS 迁移 Job：

```bash
kubectl -n hydra-system get job,pod -l app=hydra-maas-migrate -w
```

发现 Job 后查看日志：

```bash
kubectl -n hydra-system logs job/hydra-maas-migrate -f
```

默认 Job 名为 `hydra-maas-migrate`。Job 成功后会自动删除，建议升级期间保存日志。

!!! note

    迁移 Job 可重复执行。失败时修复问题并重新升级即可。

### 常见失败处理

| 日志或现象 | 处理方式 |
| ---------- | -------- |
| `ModelRoute` CRD 缺少 `enabled` 或可见范围字段 | 对报错的工作集群重新升级 hydra-agent，确认 Knoway 自动升级成功 |
| 存在旧 MaaS 数据，但 Clusterpedia 查不到 `ModelRoute` | 检查 Clusterpedia 同步、权限和网络 |
| 启用的 MaaS 数据没有对应 `ModelRoute` | 恢复对应 CR；或经业务确认后先在旧版本禁用该模型 |
| DB 与 CR 状态不一致 | 迁移默认以 CR 为准，按迁移告警核对业务期望 |
| NodePort 被其他 Service 占用 | 调整真实冲突的 Service 或 hydra-agent 端口 |
| 迁移 Job 超时或失败 | 保存日志，修复 DB、Clusterpedia 或集群连接后重新执行升级 |

!!! warning

    不要通过删除 `maas_model` 表、跳过迁移 Job 或强制删除 `ModelRoute` 来绕过错误。

### 升级后验收

- 全局服务集群 Hydra、所有 hydra-agent 和 Knoway Pod Ready
- MaaS 模型数量与升级前一致
- MaaS 列表分页的 items、pageSize 和总数正常
- 原启用模型仍可用，原禁用模型仍保持禁用
- v0.17.1 的 Workspace 可见范围保持不变
- v0.16.0 迁移的 MaaS 模型默认对所有 Workspace 可见
- MaaS API Key、智能路由和公共端点调用正常
- 迁移日志没有未处理的 error，warning 已逐条确认

## 从 v0.16.0（或更低版本）升级到 v0.17.1 {#upgrade-to-v0171}

Hydra 从 v0.17.1 开始，将原先混在 `model` 表中的模型元数据与 MaaS 相关数据解耦：
新增 `maas_model` 表存储 MaaS 信息，`model` 表中的 MaaS 字段在迁移完成后将逐步废弃。
为避免升级过程中模型元数据丢失，升级前请先完成下述数据表迁移。

!!! warning

    如果目标版本是 v0.18.3 或更高版本，请勿执行本节中的 `create_maas_model.sql`，
    请直接参考上文[从 v0.16.0 / v0.17.1 升级到 v0.18.3](#upgrade-to-v0183)。

    仅当必须先升级到 v0.17.1 时，才需要完成本节的数据表迁移。

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
