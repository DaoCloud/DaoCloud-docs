# Upgrade Notes

This page describes important considerations when upgrading Hydra to a new version.
Choose the section that matches your current version.

## Upgrading from v0.16.0 / v0.17.1 to v0.18.0 {#upgrade-to-v0180}

Starting from Hydra v0.18.0, MaaS enablement status, cluster assignment, and Workspace visibility
are all based on the Knoway `ModelRoute` CR. The old database fields are kept temporarily
and are used only as the source for upgrade migration.

Upgrading `hydra-agent` automatically upgrades Knoway. Knoway is a subchart of the `hydra-agent` Chart,
with `knoway.enabled=true` by default, so a separate Knoway upgrade is not required.

!!! warning

    Follow this order: back up the database and `ModelRoute` objects, upgrade `hydra-agent` on every
    worker cluster (which automatically upgrades Knoway), then upgrade Hydra on the global service cluster,
    and finally verify the MaaS migration results.

    If the environment has `knoway.enabled=false`, or Knoway is managed as an independent Helm Release,
    upgrade Knoway separately before upgrading Hydra on the global service cluster.

!!! note

    When upgrading directly from v0.16.0 to v0.18.0, **do not** run `create_maas_model.sql`.
    The upgrade Job automatically reads the `model` table if the `maas_model` table does not exist.

This section applies to:

- Upgrading from v0.17.1 to v0.18.0
- Upgrading directly from v0.16.0 (without the MaaS table migration) to v0.18.0

| Source version | Migration source used automatically | Migration result |
| -------------- | ----------------------------------- | ---------------- |
| v0.17.1 | `maas_model` table | Keeps enablement status and `ALL` / `SPECIFIED` Workspace visibility |
| v0.16.0 | `model.public_endpoint_*` | Keeps enablement status; visibility is set to `ALL` |

The global Hydra upgrade first runs the `hydra-maas-migrate` Job. A failed migration blocks the upgrade,
and the new apiserver will not roll out early.

### Before You Upgrade

1. Back up the database. At a minimum, back up:

    - The `model` table
    - The `maas_model` table on v0.17.1 environments
    - The entire Hydra database when possible

    Have a DBA run the backup with controlled credentials.
    Do not put the database password in commands, scripts, or tickets.

    To inspect the database currently used by Hydra, see the steps in
    [Upgrading from v0.16.0 (or Earlier) to v0.17.1](#upgrade-to-v0171).

1. Export `ModelRoute` objects. On every worker cluster, run:

    ```bash
    kubectl get modelroutes.llm.knoway.dev -A -o yaml > <worker>-modelroutes-backup.yaml
    ```

    Replace `<worker>` with the worker cluster name so backup files are easy to tell apart.

### Upgrade hydra-agent on Worker Clusters

Upgrade **hydra-agent** on the **Helm Apps** page of each worker cluster.
Upgrade a non-critical cluster first, confirm it is healthy, and then upgrade the remaining clusters.

By default, this also upgrades:

- Knoway Controller and Gateway
- The `ModelRoute` CRD
- Other hydra-agent components

After each worker cluster upgrade, run:

```bash
kubectl -n hydra-system get pods
kubectl get crd modelroutes.llm.knoway.dev
kubectl get modelroutes.llm.knoway.dev -A
kubectl explain modelroute.spec.enabled --api-version=llm.knoway.dev/v1alpha1
kubectl explain modelroute.spec.metadata.visibilityScope --api-version=llm.knoway.dev/v1alpha1
kubectl explain modelroute.spec.metadata.visibleWorkspaces --api-version=llm.knoway.dev/v1alpha1
```

Continue only when all hydra-agent and Knoway Pods are Ready, and the three `ModelRoute` fields above exist.

!!! note

    The latest Chart no longer treats the NodePort that already belongs to the same hydra-agent Release
    as a conflict. If the upgrade still reports that the port is in use by another Service,
    it is a real conflict; change the port and retry.

### Upgrade Hydra on the Global Service Cluster

After hydra-agent has been upgraded on every worker cluster, upgrade Hydra on the
**Helm Apps** page of the global service cluster.

Watch the MaaS migration Job during the upgrade:

```bash
kubectl -n hydra-system get job,pod -l app=hydra-maas-migrate -w
```

When the Job appears, follow its logs:

```bash
kubectl -n hydra-system logs job/hydra-maas-migrate -f
```

The default Job name is `hydra-maas-migrate`. The Job is deleted automatically after it succeeds,
so save the logs while the upgrade is running.

!!! note

    The migration Job is idempotent. If it fails, fix the issue and rerun the upgrade.

### Common Failures

| Log or symptom | What to do |
| -------------- | ---------- |
| The `ModelRoute` CRD is missing `enabled` or visibility fields | Re-upgrade hydra-agent on the failing worker cluster and confirm Knoway upgraded automatically |
| Legacy MaaS data exists, but Clusterpedia cannot find `ModelRoute` | Check Clusterpedia sync, permissions, and network |
| Enabled MaaS data has no matching `ModelRoute` | Restore the corresponding CR, or disable the model on the old version after business confirmation |
| DB and CR status do not match | Migration treats the CR as the source of truth; review migration warnings against the expected behavior |
| A NodePort is used by another Service | Change the conflicting Service or hydra-agent port |
| The migration Job times out or fails | Save the logs, fix the database, Clusterpedia, or cluster connectivity, then rerun the upgrade |

!!! warning

    Do not bypass errors by dropping the `maas_model` table, skipping the migration Job, or force-deleting `ModelRoute` objects.

### After You Upgrade

- Hydra on the global service cluster, and all hydra-agent and Knoway Pods, are Ready
- The number of MaaS models matches the count before the upgrade
- MaaS list pagination (`items`, `pageSize`, and total) works as expected
- Previously enabled models remain available; previously disabled models remain disabled
- Workspace visibility from v0.17.1 is unchanged
- MaaS models migrated from v0.16.0 are visible to all Workspaces by default
- MaaS API Keys, intelligent routing, and public endpoint calls work as expected
- Migration logs contain no unhandled errors, and every warning has been reviewed

## Upgrading from v0.16.0 (or Earlier) to v0.17.1 {#upgrade-to-v0171}

Starting from v0.17.1, hydra decouples model metadata from MaaS-related data that was previously stored
together in the `model` table. A new `maas_model` table is introduced to store MaaS information.
The MaaS fields in the `model` table will be gradually deprecated after the migration is complete.
To prevent model metadata loss during the upgrade, complete the following data table migration before upgrading.

!!! warning

    If the target version is v0.18.0 or later, do not run `create_maas_model.sql` in this section.
    Follow [Upgrading from v0.16.0 / v0.17.1 to v0.18.0](#upgrade-to-v0180) instead.

    Complete this table migration only when you must upgrade to v0.17.1 first.

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
