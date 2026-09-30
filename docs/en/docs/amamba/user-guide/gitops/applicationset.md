# Use ApplicationSet

ArgoCD supports using [ApplicationSet](https://argo-cd.readthedocs.io/en/stable/user-guide/application-set/)
to flexibly generate multiple GitOps applications, for example in multi-cluster application scenarios.
In the Workbench, this is supported through `AppOfApplicationSet`.
This article will guide you on how to enable the ApplicationSet feature in the Workbench.

!!! note

    This article assumes that the namespace where your ArgoCD is installed and the Helm Release name are both argocd. This will affect the subsequent search and modification operations. If your namespace and Release name are different, please replace them accordingly.

## AppOfApplicationSet Mode

`AppOfApplicationSet` is an operation mode of GitOps. It deploys multi-cluster applications through
**Application** -> **Generate ApplicationSet** -> **Generate multiple Applications**:

![applicationset](../../images/gitops-application-set.png)

Therefore, essentially it still creates GitOps Applications. The premise is that your GitOps repository
(assume the repository name is app-set-repo) needs to contain the following definition file of an ApplicationSet.

```yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet # the resource type is ApplicationSet
metadata:
  name: guestbook # note that you should not define namespace, otherwise it cannot be created properly
spec:
  generators:
    - list:
        elements: # custom elements, a map structure that can be added arbitrarily and will be replaced in the form of go template
          - cluster: "cluster1"
            namespace: "ns1"
            path: "dev"
          - cluster: "cluster2"
            namespace: "ns2"
            path: "staging"
  template: # essentially renders an ArgoCD Application resource
    metadata:
      name: "{{cluster}}-2048" # the elements defined in generators above can be used in template
    spec:
      project: "2" # represents the ID of the workspace
      source:
        repoURL: https://demo-repo.git # the repository address for actually creating the Application. The path in elements above should correspond to the repository of this URL
        targetRevision: HEAD
        path: "{{path}}"
      destination:
        name: "{{cluster}}"
        namespace: "{{namespace}}"
```

!!! note

    Note that the cluster and namespace in the Application need to be bound in the **Global Management** module in advance.
    Fill in the project, cluster, and namespace fields according to your permissions, otherwise the creation will fail.

Afterwards, you need to create a GitOps Application in the GitOps module of the Workbench, where the
repository address is the address corresponding to app-set-repo, so that multiple Applications can be
generated. For how to create a GitOps application, refer to [Create a GitOps Application](create-argo-cd.md).

Follow the steps below to enable the ApplicationSet feature.

## Enable ApplicationSet

### Workbench version >= v0.35.0

After the Workbench is upgraded to v0.35.0, we provide a feature switch to enable/disable the
`AppOfApplicationSet` feature with one click.

1. Go to __Container Management__ -> __Clusters__ -> __kpanda-global-cluster__ -> __ConfigMaps and Secrets__ -> __ConfigMaps__

2. Select the namespace where amamba is installed (the default is `amamba-system`), and select `amamba-config` to update.

3. Add or modify the following configuration item:

    ```yaml
    argocd.appAnyNamespace.enable: true # set it to false to disable
    ```
    > Note that you are adding a key-value pair
    
    ![](../../images/app-in-any-ns-config.png)

4. Click Save, go to Workbench -> GitOps module, and create a GitOps application through AppOfApplicationSet.

### Workbench version < v0.35.0

#### Enable the Configuration

1. Configure the RBAC of the ApplicationSet Controller

    ApplicationSet relies on the reconciliation of the ApplicationSet Controller to control multiple
    Applications. You need to configure the corresponding RBAC role in the cluster (it is not created
    by default and needs to be created manually). There are two cases:

    - If ArgoCD is already installed

        By default, ArgoCD installed through helm does not create the ClusterRole and ClusterRoleBinding
        of the ApplicationSet Controller, so you need to create them manually. It is recommended to do so
        by updating the Helm application.

        Go to **Container Management** -> **Clusters** -> **kpanda-global-cluster** -> **Helm Applications**,
        search for `argocd` (the Helm application name when you installed ArgoCD), click **Update** on the
        right, and enable it by updating the following YAML:

        ```yaml
        argo-cd:
          applicationSet:
            allowAnyNamespace: true  # set it to true
        
          configs:
            params:
              application.namespaces: gitops-* # set it to gitops-*  
        ```

    - If ArgoCD is not installed

        When installing, it is consistent with the configuration YAML above, and it is implemented by
        setting the helm value.

        Please make sure to wait for the ArgoCD update to complete before performing the following operations.

2. Modify the ConfigMap configurations related to ArgoCD

    Go to **Container Management** -> **Clusters** -> **kpanda-global-cluster** -> **ConfigMaps and Secrets** -> **ConfigMaps**.
    You need to modify the following two ConfigMaps. Because content needs to be added, please select **Edit YAML** to modify:

    - argocd-cm

        Add the following configuration to the data field of the YAML:

        ```yaml
        kind: ConfigMap
        apiVersion: v1
        metadata:
          name: argocd-cm
        data:
          application.resourceTrackingMethod: "annotation+label" # add this line
        ```

    - argocd-cmd-params-cm

        Add or modify the following configuration in the data field of the YAML:

        ```yaml
        kind: ConfigMap
        apiVersion: v1
        metadata:
          name: argocd-cmd-params-cm
        data:
          # add the following two lines
          applicationsetcontroller.namespaces: "gitops-*"
          applicationsetcontroller.allowed.scm.providers: "true"
        ```

After completing the above changes, you need to restart the ArgoCD and Workbench related components.

#### Restart Services

**Restart ArgoCD components:**

Go to **Container Management** -> **Clusters** -> **kpanda-global-cluster** -> **Workloads** -> **Deployments**,
select the namespace `argocd` (the namespace where you installed ArgoCD), search for
`argocd-applicationset-controller`, and click **Status** in **┇** on the right to restart it. At the same
time, in **StatefulSets**, find and restart `argocd-application-controller`.

**Restart Workbench components:**

Go to **Container Management** -> **Clusters** -> **kpanda-global-cluster** -> **Workloads** -> **Deployments**,
select the namespace `amamba-system`, and restart the two Deployments `amamba-apiserver` and `amamba-syncer` respectively.

After the above components are restarted, go to the Workbench and select `AppOfApplicationSet` to create a GitOps application.
