# 容器管理权限说明

容器管理权限基于全局权限管理以及 Kubernetes RBAC 权限管理打造的多维度权限管理体系。
支持集群级、命名空间级的权限控制，帮助用户便捷灵活地对租户下的 IAM 用户、用户组（用户的集合）设定不同的操作权限。

## 集群权限

集群权限基于 Kubernetes RBAC 的 ClusterRolebinding 授权，集群权限设置可让用户/用户组具备集群相关权限。
目前的默认集群角色为 __Cluster Admin__ （不具备集群的创建、删除权限）。

### __Cluster Admin__

__Cluster Admin__ 具有以下权限：

- 可管理、编辑、查看对应集群

- 管理、编辑、查看 命名空间下的所有工作负载及集群内所有资源

- 可授权用户为集群内角色 (Cluster Admin、NS Admin、NS Editor、NS Viewer)

该集群角色的 YAML 示例如下：

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  annotations:
    kpanda.io/creator: system
  creationTimestamp: "2022-06-16T09:42:49Z"
  labels:
    iam.kpanda.io/role-template: "true"
  name: role-template-cluster-admin
  resourceVersion: "15168"
  uid: f8f86d42-d5ef-47aa-b284-097615795076
rules:
- apiGroups:
  - '*'
  resources:
  - '*'
  verbs:
  - '*'
- nonResourceURLs:
  - '*'
  verbs:
  - '*'
```

## 命名空间权限

命名空间权限是基于 Kubernetes RBAC 能力的授权，可以实现不同的用户/用户组对命名空间下的资源具有不同的操作权限(包括 Kubernetes API 权限)，详情可参考：[Kubernetes RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)。目前容器管理的默认角色为：NS Admin、NS Editor、NS Viewer。

### __NS Admin__

__NS Admin__ 具有以下权限：

- 可查看对应命名空间
- 管理、编辑、查看 命名空间下的所有工作负载，及自定义资源
- 可授权用户为对应命名空间角色 (NS Editor、NS Viewer)

该集群角色的 YAML 示例如下：

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  annotations:
    kpanda.io/creator: system
  creationTimestamp: "2022-06-16T09:42:49Z"
  labels:
    iam.kpanda.io/role-template: "true"
  name: role-template-ns-admin
  resourceVersion: "15173"
  uid: 69f64c7e-70e7-4c7c-a3e0-053f507f2bc3
rules:
- apiGroups:
  - '*'
  resources:
  - '*'
  verbs:
  - '*'
- nonResourceURLs:
  - '*'
  verbs:
  - '*'    
```

### __NS Editor__

__NS Editor__ 具有以下权限：

- 可查看对应有权限的命名空间
- 管理、编辑、查看 命名空间下的所有工作负载

??? note "点击查看集群角色的 YAML 示例"

    ```yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      annotations:
        kpanda.io/creator: system
      creationTimestamp: "2022-06-16T09:42:50Z"
      labels:
        iam.kpanda.io/role-template: "true"
      name: role-template-ns-edit
      resourceVersion: "15175"
      uid: ca9e690e-96c0-4978-8915-6e4c00c748fe
    rules:
    - apiGroups:
      - ""
      resources:
      - configmaps
      - endpoints
      - persistentvolumeclaims
      - persistentvolumeclaims/status
      - pods
      - replicationcontrollers
      - replicationcontrollers/scale
      - serviceaccounts
      - services
      - services/status
      verbs:
      - '*'
    - apiGroups:
      - ""
      resources:
      - bindings
      - events
      - limitranges
      - namespaces/status
      - pods/log
      - pods/status
      - replicationcontrollers/status
      - resourcequotas
      - resourcequotas/status
      verbs:
      - '*'
    - apiGroups:
      - ""
      resources:
      - namespaces
      verbs:
      - '*'
    - apiGroups:
      - apps
      resources:
      - controllerrevisions
      - daemonsets
      - daemonsets/status
      - deployments
      - deployments/scale
      - deployments/status
      - replicasets
      - replicasets/scale
      - replicasets/status
      - statefulsets
      - statefulsets/scale
      - statefulsets/status
      verbs:
      - '*'
    - apiGroups:
      - autoscaling
      resources:
      - horizontalpodautoscalers
      - horizontalpodautoscalers/status
      verbs:
      - '*'
    - apiGroups:
      - batch
      resources:
      - cronjobs
      - cronjobs/status
      - jobs
      - jobs/status
      verbs:
      - '*'
    - apiGroups:
      - extensions
      resources:
      - daemonsets
      - daemonsets/status
      - deployments
      - deployments/scale
      - deployments/status
      - ingresses
      - ingresses/status
      - networkpolicies
      - replicasets
      - replicasets/scale
      - replicasets/status
      - replicationcontrollers/scale
      verbs:
      - '*'
    - apiGroups:
      - policy
      resources:
      - poddisruptionbudgets
      - poddisruptionbudgets/status
      verbs:
      - '*'
    - apiGroups:
      - networking.k8s.io
      resources:
      - ingresses
      - ingresses/status
      - networkpolicies
      verbs:
      - '*'      
    ```

### __NS Viewer__

__NS Viewer__ 具有以下权限：

- 可查看对应命名空间
- 可查看对应命名空间下的所有工作负载，及自定义资源

??? note "点击查看集群角色的 YAML 示例"

    ```yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      annotations:
        kpanda.io/creator: system
      creationTimestamp: "2022-06-16T09:42:50Z"
      labels:
        iam.kpanda.io/role-template: "true"
      name: role-template-ns-view
      resourceVersion: "15183"
      uid: 853888fd-6ee8-42ac-b91e-63923918baf8
    rules:
    - apiGroups:
      - ""
      resources:
      - configmaps
      - endpoints
      - persistentvolumeclaims
      - persistentvolumeclaims/status
      - pods
      - replicationcontrollers
      - replicationcontrollers/scale
      - serviceaccounts
      - services
      - services/status
      verbs:
      - get
      - list
      - watch
    - apiGroups:
      - ""
      resources:
      - bindings
      - events
      - limitranges
      - namespaces/status
      - pods/log
      - pods/status
      - replicationcontrollers/status
      - resourcequotas
      - resourcequotas/status
      verbs:
      - get
      - list
      - watch
    - apiGroups:
      - ""
      resources:
      - namespaces
      verbs:
      - get
      - list
      - watch
    - apiGroups:
      - apps
      resources:
      - controllerrevisions
      - daemonsets
      - daemonsets/status
      - deployments
      - deployments/scale
      - deployments/status
      - replicasets
      - replicasets/scale
      - replicasets/status
      - statefulsets
      - statefulsets/scale
      - statefulsets/status
      verbs:
      - get
      - list
      - watch
    - apiGroups:
      - autoscaling
      resources:
      - horizontalpodautoscalers
      - horizontalpodautoscalers/status
      verbs:
      - get
      - list
      - watch
    - apiGroups:
      - batch
      resources:
      - cronjobs
      - cronjobs/status
      - jobs
      - jobs/status
      verbs:
      - get
      - list
      - watch
    - apiGroups:
      - extensions
      resources:
      - daemonsets
      - daemonsets/status
      - deployments
      - deployments/scale
      - deployments/status
      - ingresses
      - ingresses/status
      - networkpolicies
      - replicasets
      - replicasets/scale
      - replicasets/status
      - replicationcontrollers/scale
      verbs:
      - get
      - list
      - watch
    - apiGroups:
      - policy
      resources:
      - poddisruptionbudgets
      - poddisruptionbudgets/status
      verbs:
      - get
      - list
      - watch
    - apiGroups:
      - networking.k8s.io
      resources:
      - ingresses
      - ingresses/status
      - networkpolicies
      verbs:
      - get
      - list
      - watch 
    ```

## 权限 FAQ

1. 全局权限和容器管理权限管理的关系？

    答：全局权限仅授权为粗粒度权限，可管理所有集群的创建、编辑、删除；而对于细粒度的权限，如单个集群的管理权限，单个命名空间的管理、编辑、删除权限，需要基于 Kubernetes RBAC 的容器管理权限进行实现。
    一般权限的用户仅需要在容器管理中进行授权即可。

2. 目前仅支持四个默认角色，后台自定义角色的 __RoleBinding__ 以及 __ClusterRoleBinding__ （Kubernetes 细粒度的 RBAC）是否也能生效？

    答：目前自定义权限暂时无法通过图形界面进行管理，但是通过 kubectl 创建的权限规则同样能生效。
