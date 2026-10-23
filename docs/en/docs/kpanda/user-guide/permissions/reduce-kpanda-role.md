# Removing RBAC Rules from System Roles

*[kpanda]: A development codename for container management

Starting from container management v0.50.0, you can reduce the permissions of the built-in namespace roles (NS Admin, NS Editor, and NS Viewer).
This document uses the example of preventing NS Viewer from viewing Pod logs to explain how to reduce the permission points of built-in roles.

## Prerequisites

- Container management v0.50.0 or later.
- [Integrated Kubernetes cluster](../clusters/integrate-cluster.md) or
  [created Kubernetes cluster](../clusters/create-cluster.md).
- You have administrator permissions on the Global Cluster and can operate that cluster using `kubectl`.

!!! note

    - You only need to create the permission reduction rules in the Global Cluster. The Kpanda controller synchronizes
      the calculated built-in role permissions to all subclusters, and the synchronization may take some time.
    - Permission reduction is only supported for the built-in namespace roles `role-template-ns-admin`, `role-template-ns-edit`,
      and `role-template-ns-view`. Cluster-level built-in roles are not supported.
    - You can only reduce permissions using a ClusterRole with the specified Label, and you cannot use a Role. Do not
      directly modify the built-in ClusterRole; otherwise, the Kpanda controller will overwrite your changes.

## Correspondence Between Built-in Roles and Labels

When creating a permission reduction ClusterRole for a target role, set the value of the corresponding Label to `"delete"`:

| Built-in Role | ClusterRole | Label |
| --- | --- | --- |
| NS Admin | `role-template-ns-admin` | `rbac.kpanda.io/role-template-ns-admin: "delete"` |
| NS Editor | `role-template-ns-edit` | `rbac.kpanda.io/role-template-ns-edit: "delete"` |
| NS Viewer | `role-template-ns-view` | `rbac.kpanda.io/role-template-ns-view: "delete"` |

Kpanda first merges the built-in permissions with the permissions appended through `merge` or `true`, and then subtracts the permissions declared in all `delete` rules:

```text
Final permissions = (built-in permissions ∪ appended permissions) - reduced permissions
```

## Steps

The following steps remove the permission to read Pod logs from NS Viewer while retaining the permissions to view Pod status and other resources.

1. Create the following ClusterRole in the Global Cluster:

    ```yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: delete-ns-view-pod-log-read # (1)!
      labels:
        rbac.kpanda.io/source: "others"
        rbac.kpanda.io/role-template-ns-view: "delete" # (2)!
    rules:
      - apiGroups: [""]
        resources: ["pods/log"]
        verbs: ["get", "list", "watch"]
    ```

    1. The name can be customized, but it must comply with the Kubernetes resource naming conventions and must not duplicate an existing resource name.
    2. To reduce the permissions of another built-in namespace role, replace it with the Label corresponding to that role and keep the value as `"delete"`.

2. Apply the YAML file and wait for the Kpanda controller to complete the synchronization:

    ```sh
    kubectl apply -f delete-ns-view-pod-log-read.yaml
    ```

3. Check the built-in ClusterRole corresponding to NS Viewer and confirm that `pods/log` no longer includes
   the `get`, `list`, and `watch` permissions:

    ```sh
    kubectl get clusterrole role-template-ns-view -o yaml
    ```

    After the synchronization is complete, users who have been granted NS Viewer can no longer view Pod logs.

## Restore Permissions

After you delete the permission reduction ClusterRole, Kpanda automatically recalculates the built-in roles and restores the corresponding permissions:

```sh
kubectl delete clusterrole delete-ns-view-pod-log-read
```

After the synchronization is complete, run the following command to confirm that the permissions have been restored:

```sh
kubectl get clusterrole role-template-ns-view -o yaml
```

## Limitations

- The `delete` rule does not support `resourceNames` or `nonResourceURLs`.
- Deleting only a specific value from the wildcards `apiGroups: ["*"]` or `resources: ["*"]` is not supported. If you need to delete all the values covered by a wildcard,
  use `"*"` in the `delete` rule as well.
- Resource wildcards in the form of `*/subresource`, such as `*/scale`, are not supported.
- If the `verbs` of the original permission is `"*"`, you can delete the standard Kubernetes operations such as `get`, `list`, `watch`, `create`, `update`, `patch`,
  `delete`, and `deletecollection`. For custom operations, first confirm whether Kpanda supports expanding that operation.
- An invalid `delete` configuration does not take effect, and the corresponding role retains the built-in default permissions. Check the Kpanda controller logs and fix the configuration.
