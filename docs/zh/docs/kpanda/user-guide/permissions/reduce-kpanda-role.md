# 减少容器管理内置权限点

*[Kpanda]: 容器管理的开发代号

从容器管理 v0.50.0 开始，您可以减少 Namespace 内置角色（NS Admin、NS Editor、NS Viewer）的权限。
本文以禁止 NS Viewer 查看 Pod 日志为例，说明如何减少内置角色的权限点。

## 前提条件

- 容器管理版本为 v0.50.0 或更高版本。
- 已[接入 Kubernetes 集群](../clusters/integrate-cluster.md)或
  [创建 Kubernetes 集群](../clusters/create-cluster.md)。
- 具备 Global Cluster 的管理员权限，并且能够使用 `kubectl` 操作该集群。

!!! note

    - 只需在 Global Cluster 创建权限缩减规则。Kpanda 控制器会将计算后的内置角色权限同步到所有子集群，
      同步过程可能需要一段时间。
    - 权限缩减仅支持 Namespace 内置角色 `role-template-ns-admin`、`role-template-ns-edit` 和
      `role-template-ns-view`，不支持 Cluster 级内置角色。
    - 只能使用带有指定 Label 的 ClusterRole 缩减权限，不能使用 Role。不要直接修改内置 ClusterRole，
      否则 Kpanda 控制器会覆盖您的修改。

## 内置角色与 Label 的对应关系

为目标角色创建权限缩减 ClusterRole 时，将对应 Label 的值设置为 `"delete"`：

| 内置角色 | ClusterRole | Label |
| --- | --- | --- |
| NS Admin | `role-template-ns-admin` | `rbac.kpanda.io/role-template-ns-admin: "delete"` |
| NS Editor | `role-template-ns-edit` | `rbac.kpanda.io/role-template-ns-edit: "delete"` |
| NS Viewer | `role-template-ns-view` | `rbac.kpanda.io/role-template-ns-view: "delete"` |

Kpanda 会先合并内置权限和通过 `merge` 或 `true` 追加的权限，再减去所有 `delete` 规则中声明的权限：

```text
最终权限 =（内置权限 ∪ 追加权限）- 缩减权限
```

## 操作步骤

以下步骤从 NS Viewer 中移除读取 Pod 日志的权限，同时保留查看 Pod 状态和其他资源的权限。

1. 在 Global Cluster 中创建以下 ClusterRole：

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

    1. 名称可以自定义，但必须符合 Kubernetes 资源命名规范且不能与已有资源重名。
    2. 如果要缩减其他 Namespace 内置角色的权限，请替换为该角色对应的 Label，值保持为 `"delete"`。

1. 应用 YAML 文件，并等待 Kpanda 控制器完成同步：

    ```sh
    kubectl apply -f delete-ns-view-pod-log-read.yaml
    ```

1. 查看 NS Viewer 对应的内置 ClusterRole，确认 `pods/log` 不再包含
   `get`、`list` 和 `watch` 权限：

    ```sh
    kubectl get clusterrole role-template-ns-view -o yaml
    ```

    同步完成后，已授予 NS Viewer 的用户将无法再查看 Pod 日志。

## 恢复权限

删除权限缩减 ClusterRole 后，Kpanda 会自动重新计算内置角色，并恢复相应权限：

```sh
kubectl delete clusterrole delete-ns-view-pod-log-read
```

等待同步完成后，运行以下命令确认权限已恢复：

```sh
kubectl get clusterrole role-template-ns-view -o yaml
```

## 使用限制

- `delete` 规则不支持 `resourceNames` 和 `nonResourceURLs`。
- 不支持从通配符 `apiGroups: ["*"]` 或 `resources: ["*"]` 中仅删除某个具体值。如需删除通配符覆盖的全部值，
  请在 `delete` 规则中也使用 `"*"`。
- 不支持 `*/subresource` 形式的资源通配符，例如 `*/scale`。
- 如果原权限的 `verbs` 为 `"*"`，可以删除 `get`、`list`、`watch`、`create`、`update`、`patch`、
  `delete` 和 `deletecollection` 等 Kubernetes 标准操作。对于自定义操作，请先确认 Kpanda 是否支持展开该操作。
- 无效的 `delete` 配置不会生效，对应角色将保留内置默认权限。请检查 Kpanda 控制器日志并修正配置。
