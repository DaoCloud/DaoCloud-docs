# Description of container management permissions

Container management permissions are based on a multi-dimensional permission management system created by global permission management and Kubernetes RBAC permission management.
Supports cluster-level and namespace-level permission control, helping users to conveniently and flexibly set different operation permissions for IAM users and groups (a collection of users) under a tenant.

## Cluster permissions

Cluster permissions are based on the ClusterRolebinding authorization of Kubernetes RBAC. Cluster permission settings allow users/groups to have cluster-related permissions.
The current default cluster role is __Cluster Admin__ (does not have permission to create and delete clusters).

### __Cluster Admin__ 

 __Cluster Admin__ has the following permissions:

1. Can manage, edit and view the corresponding cluster

2. Manage, edit, and view all workloads under the namespace and all resources in the cluster

3. Users can be authorized as roles in the cluster (Cluster Admin, NS Admin, NS Edit, NS View)

An example YAML for this cluster role is as follows:

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

## Namespace permissions

Namespace permissions are based on the authorization of Kubernetes RBAC capabilities, which can enable different users/groups to have different operation permissions on resources under the namespace (including Kubernetes API permissions, for details, refer to: [Kubernetes RBAC](https://kubernetes .io/docs/reference/access-authn-authz/rbac/). Currently, the default roles for container management are: NS Admin, NS Edit, NS View.

### __NS Admin__ 

 __NS Admin__ has the following permissions:

1. You can view the corresponding namespace

2. Manage, edit, and view all workloads and custom resources under the namespace

3. The user can be authorized as the corresponding namespace role (NS Edit, NS View)

An example YAML for this cluster role is as follows:

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

### __NS Edit__ 

 __NS Edit__ has the following permissions:

1. You can view the corresponding namespace with permissions

2. Manage, edit, and view all workloads under the namespace

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
      - persistent volume claims
      - persistent volume claims/status
      - pods
      -replicationcontrollers
      -replicationcontrollers/scale
      - serviceaccounts
      - services
      - services/status
      verbs:
      - '*'
    - apiGroups:
      - ""
      resources:
      -bindings
      -events
      - limit ranges
      - namespaces/status
      - pods/log
      - pods/status
      -replicationcontrollers/status
      -resourcequotas
      -resourcequotas/status
      verbs:
      - '*'
    - apiGroups:
      - ""
      resources:
      - namespaces
      verbs:
      - '*'
    - apiGroups:
      -apps
      resources:
      - controller revisions
      -daemonsets
      - daemonsets/status
      - deployments
      - deployments/scales
      - deployments/status
      -replicasets
      -replicasets/scale
      - replicasets/status
      -statefulsets
      -statefulsets/scale
      - statefulsets/status
      verbs:
      - '*'
    - apiGroups:
      - autoscaling
      resources:
      -horizontal pod autoscalers
      -horizontal pod autoscalers/status
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
      -daemonsets
      - daemonsets/status
      - deployments
      - deployments/scales
      - deployments/status
      - ingresses
      - ingresses/status
      - networkpolicies
      -replicasets
      -replicasets/scale
      - replicasets/status
      -replicationcontrollers/scale
      verbs:
      - '*'
    - apiGroups:
      - policy
      resources:
      -pod disruption budgets
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

### __NS View__ 

 __NS View__ has the following permissions:

1. You can view the corresponding namespace

2. You can view all workloads and custom resources under the corresponding namespace

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
      - persistent volume claims
      - persistent volume claims/status
      - pods
      -replicationcontrollers
      -replicationcontrollers/scale
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
      -bindings
      -events
      - limit ranges
      - namespaces/status
      - pods/log
      - pods/status
      -replicationcontrollers/status
      -resourcequotas
      -resourcequotas/status
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
      -apps
      resources:
      - controller revisions
      -daemonsets
      - daemonsets/status
      - deployments
      - deployments/scales
      - deployments/status
      -replicasets
      -replicasets/scale
      - replicasets/status
      -statefulsets
      -statefulsets/scale
      - statefulsets/status
      verbs:
      - get
      - list
      - watch
    - apiGroups:
      - autoscaling
      resources:
      -horizontal pod autoscalers
      -horizontal pod autoscalers/status
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
      -daemonsets
      - daemonsets/status
      - deployments
      - deployments/scales
      - deployments/status
      - ingresses
      - ingresses/status
      - networkpolicies
      -replicasets
      -replicasets/scale
      - replicasets/status
      -replicationcontrollers/scale
      verbs:
      - get
      - list
      - watch
    - apiGroups:
      - policy
      resources:
      -pod disruption budgets
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

    Answer: Global permissions are only authorized as coarse-grained permissions, which can manage the creation, editing, and deletion of all clusters; for fine-grained permissions, such as the management permissions of a single cluster, the management, editing, and deletion permissions of a single namespace, they need to be based on Kubernetes. RBAC's container management permissions are implemented.
    Users with general permissions only need to authorize in container management.

2. Currently, only four default roles are supported. Will __RoleBinding__ and __ClusterRoleBinding__ (Kubernetes fine-grained RBAC) of background custom roles also take effect?

    Answer: At present, custom permissions cannot be managed through the graphical interface, but permission rules created through kubectl can also take effect.