---
MTPE: windsonsea
date: 2024-05-13
---

# Container Management Permissions

Container management permissions are based on a multi-dimensional permission management system created by global permission management and Kubernetes RBAC permission management. It supports cluster-level and namespace-level permission control, helping users to conveniently and flexibly set different operation permissions for IAM users and user groups (collections of users) under a tenant.

## Cluster Permissions

Cluster permissions are authorized based on Kubernetes RBAC's ClusterRoleBinding, allowing users/user groups to have cluster-related permissions. The current default cluster role is __Cluster Admin__ (does not have the permission to create or delete clusters).

### __Cluster Admin__

__Cluster Admin__ has the following permissions:

- Can manage, edit, and view the corresponding cluster
- Manage, edit, and view all workloads and all resources within the namespace
- Can authorize users for roles within the cluster (Cluster Admin, NS Admin, NS Editor, NS Viewer)

The YAML example for this cluster role is as follows:

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

## Namespace Permissions

Namespace permissions are authorized based on Kubernetes RBAC capabilities, allowing different users/user groups to have different operation permissions on resources under a namespace (including Kubernetes API permissions). For details, refer to: [Kubernetes RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/). Currently, the default roles for container management are: NS Admin, NS Editor, NS Viewer.

### __NS Admin__ 

__NS Admin__ has the following permissions:

- Can view the corresponding namespace
- Manage, edit, and view all workloads and custom resources within the namespace
- Can authorize users for corresponding namespace roles (NS Editor, NS Viewer)

The YAML example for this cluster role is as follows:

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

__NS Editor__ has the following permissions:

- Can view corresponding namespaces where permissions are granted
- Manage, edit, and view all workloads within the namespace

??? note "Click to view the YAML example of the cluster role"

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

__NS Viewer__ has the following permissions:

- Can view the corresponding namespace
- Can view all workloads and custom resources within the corresponding namespace

??? note "Click to view the YAML example of the cluster role"

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

## Permissions FAQ

1. What is the relationship between global permissions and container management permissions?

    Answer: Global permissions only authorize coarse-grained permissions, which can manage the creation, editing, and deletion of all clusters; while for fine-grained permissions, such as the management permissions of a single cluster, the management, editing, and deletion permissions of a single namespace, they need to be implemented based on Kubernetes RBAC container management permissions. Generally, users only need to be authorized in container management.

2. Currently, only four default roles are supported. Can the __RoleBinding__ and __ClusterRoleBinding__ (Kubernetes fine-grained RBAC) for custom roles also take effect?

    Answer: Currently, custom permissions cannot be managed through the graphical interface, but the permission rules created using kubectl can still take effect.
