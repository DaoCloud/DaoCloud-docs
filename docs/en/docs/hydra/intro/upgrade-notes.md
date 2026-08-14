# Upgrade Notes

This page describes important considerations when upgrading Hydra to a new version.

## Upgrading from v0.16.0 (or Earlier) to v0.17.1

Starting from v0.17.1, hydra decouples model metadata from MaaS-related data that was previously stored
together in the `model` table. A new `maas_model` table is introduced to store MaaS information.
The MaaS fields in the `model` table will be gradually deprecated after the migration is complete.
To prevent model metadata loss during the upgrade, complete the following data table migration before upgrading.

!!! warning

    The decoupling of Model and MaaS is still in progress. In the future, information in the `maas_model`
    table may be recorded directly in Knoway-related resources, and this table may eventually be removed.
    If there is no specific need to upgrade to v0.17.1, it is recommended to postpone the upgrade
    until the decoupling work is complete.

!!! note

    Perform the following operations on the Global cluster.

1. Check the database currently connected to hydra.

    ```bash
    APP_NS=hydra-system
    kubectl -n "$APP_NS" get cm hydra -o jsonpath='{.data.config\.yaml}' | sed -n '/^db_config:/,/^[^ ]/p'
    ```

    Pay particular attention to the host, port, database name, username, and password.
    The output should look similar to:

    ```yaml
    db_config:
      dbType: mysql
      dsn: hydra:hydraPwd@tcp(mcamel-common-mysql-cluster-mysql-master.mcamel-system.svc.cluster.local:3306)/hydra?charset=utf8mb4&parseTime=true&loc=Local
      autoMigrate: true
      debug: false
    ```

1. Prepare the environment variables based on the database connection parameters,
   and prepare the migration file `create_maas_model.sql`.

    ```bash
    APP_NS=hydra-system
    DB_NS=mcamel-system
    DB_POD=mcamel-common-mysql-cluster-mysql-0
    DB_HOST=mcamel-common-mysql-cluster-mysql-master.mcamel-system.svc.cluster.local
    DB_PORT=3306
    DB_NAME=hydra
    DB_USER=hydra
    # Prepare the migration file in the corresponding directory.
    SQL_FILE=/home/create_maas_model.sql
    ```

    !!! note

        Modify the variables above according to the actual connection information
        in the ConfigMap from the previous step. Do not use the example values directly.

1. Copy the SQL file to the MySQL Pod.

    ```bash
    kubectl -n "$DB_NS" cp "$SQL_FILE" "$DB_POD:/tmp/$(basename "$SQL_FILE")" -c mysql
    ```

1. Enter the MySQL Pod.

    ```bash
    kubectl -n "$DB_NS" exec -it "$DB_POD" -- bash
    ```

    After entering the Pod, reset the same environment variables used in Step 2
    before proceeding with the following commands.

1. (Optional) Back up the `model` table. If the current account has the required permissions, run:

    ```bash
    mysqldump -h "$DB_HOST" -P "$DB_PORT" -u "$DB_USER" -p "$DB_NAME" model > /tmp/hydra-model-maas-backup.sql
    ```

    You will be prompted to enter the hydra database password. This command backs up only the `model` table.

1. Perform the migration.

    ```bash
    mysql -h "$DB_HOST" -P "$DB_PORT" -u "$DB_USER" -p "$DB_NAME" < "/tmp/$(basename "$SQL_FILE")"
    ```

    You will likewise be prompted to enter the password. Use the password corresponding
    to the DSN in the hydra ConfigMap. Enter the password manually; do not include it in the command line.

1. Verify the migration results.

    ```bash
    mysql -h "$DB_HOST" -P "$DB_PORT" -u "$DB_USER" -p "$DB_NAME"
    ```

    After entering MySQL, run:

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

    `actual_count` should match `expected_count`, and `workspace_visibility_scope` should be `ALL`.

## Upgrading from v0.14.1 (or earlier) to v0.15.0

Starting from Hydra v0.15.0, Higress is integrated into the Knoway gateway to provide AI security
and token quota capabilities. When upgrading, note the following:

1. Higress is disabled by default. Enable it in the hydra-agent Helm values:

    ```yaml
     knoway:
       higress:
         enabled: true
    ```

2. In v0.15.0, the Hydra version installed in the global management cluster is bound to the hydra-agent version
   in worker clusters. When you upgrade either component, upgrade both together. Otherwise, usage reporting and
   billing may be affected.

3. After Higress is enabled, required Wasm plugin CRs are built into the product. Apply the CRDs in each worker
   cluster where hydra-agent is installed before upgrading; otherwise hydra-agent installation may fail:

    ```bash
    helm repo add hydra https://release.daocloud.io/chartrepo/hydra
    helm repo update hydra
    helm pull hydra/hydra-agent --version v0.15.0 --untar
    kubectl apply -f hydra-agent/crds/
    ```

4. After Higress is enabled, you can configure [Security Policy Management](../oam/security-policy.md)
   in the Admin Console and query policy trigger records in [Security Audit Logs](../oam/security-audit-logs.md).

## Upgrading from v0.12.1 (or earlier) to v0.13.1

Starting from v0.13.1, hydra-agent no longer includes the dataset component by default. It must be installed
separately via the addon repository. To ensure that existing dataset CRs are not lost after the upgrade,
follow the steps below.

!!! note

    The following upgrade steps must be executed on each sub-cluster.

1. Check the currently installed hydra-agent and all datasets

    ```bash
    cloudshell-worker-ct8cbvdtb6:~# helm ls -n hydra-system | grep agent
    hydra-agent     hydra-system    1               2026-03-16 10:02:15.663202599 +0000 UTC deployed        hydra-agent-v0.12.3             v0.12.3           

    cloudshell-worker-ct8cbvdtb6:~# kubectl get datasets.dataset.baizeai.io -A
    NAMESPACE      NAME           TYPE          URI                            PHASE
    hydra-system   qwen3-0-6b-1   MODEL_SCOPE   modelscope://Qwen/Qwen3-0.6B   PROCESSING
    ```

1. Run the following command to modify the CRD (you can also edit the CRD YAML in the UI to add annotations)

    Use Helm’s `resource-policy=keep` to ensure this resource is skipped during upgrade.
    Also update the dataset CRD release-related fields to avoid errors when installing dataset separately later.

    ```bash
    cloudshell-worker-ct8cbvdtb6:~# kubectl annotate crd datasets.dataset.baizeai.io  \
    meta.helm.sh/release-name=dataset \
    meta.helm.sh/release-namespace=dataset-system \
    helm.sh/resource-policy=keep \
    --overwrite
    customresourcedefinition.apiextensions.k8s.io/datasets.dataset.baizeai.io annotated
    ```

1. Run the following command to modify the CRs

    !!! note

        It is recommended to use the CLI to update all resources at once; otherwise,
        each CR must be modified individually.

    ```bash
    cloudshell-worker-ct8cbvdtb6:~# kubectl annotate datasets.dataset.baizeai.io -A --all helm.sh/resource-policy=keep
    dataset.dataset.baizeai.io/qwen3-0-6b-1 annotated
    ```

1. Start the upgrade

    !!! note

        hydra-agent removes the dataset component from v0.12.1 to v0.13.1.

    Go to the **Helm Apps** -> **Helm Apps** page in the workload cluster,
    find the **hydra-agent** plugin, and upgrade it.

1. Verify dataset

    ```bash
    cloudshell-worker-ct8cbvdtb6:~# kubectl get datasets.dataset.baizeai.io -A
    NAMESPACE      NAME           TYPE          URI                            PHASE
    hydra-system   qwen3-0-6b-1   MODEL_SCOPE   modelscope://Qwen/Qwen3-0.6B   PROCESSING
    ```

1. Install the dataset Helm app

    Go to the **Helm Apps** -> **Helm Templates** page in the workload cluster,
    find the **dataset** plugin, and install it.

1. Remove the `keep` annotations

    ```bash
    cloudshell-worker-l2vhhlz6f4:~# kubectl annotate crd datasets.dataset.baizeai.io helm.sh/resource-policy-
    customresourcedefinition.apiextensions.k8s.io/datasets.dataset.baizeai.io annotated

    cloudshell-worker-l2vhhlz6f4:~# kubectl annotate datasets.dataset.baizeai.io -A --all helm.sh/resource-policy-
    dataset.dataset.baizeai.io/qwen3-0-6b-1 annotated
    ```

1. Update dataset

    To ensure the old CRD definition is consistent with the latest dataset version, update the dataset plugin.

    !!! note

        No parameter changes are required; simply perform the update.
