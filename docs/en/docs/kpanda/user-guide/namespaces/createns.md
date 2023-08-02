# Namespaces

Namespaces are an abstraction used in Kubernetes for resource isolation. A cluster can contain multiple namespaces with different names, and the resources in each namespace are isolated from each other. For a detailed introduction to namespaces, refer to [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

This page will introduce the related operations of the namespace.

## create namespace

Supports easy creation of namespaces through forms, and quick creation of namespaces by writing or importing YAML files.

!!! note

    - Before creating a namespace, you need to [Integrate a Kubernetes cluster](../clusters/integrate-cluster.md) or [Create a Kubernetes cluster](../clusters/create-cluster.md) in the container management module.
    - The default namespace `default` is usually automatically generated after cluster initialization. But for production clusters, for ease of management, it is recommended to create other namespaces instead of using the `default` namespace directly.

### Form Creation

1. On the `Cluster List` page, click the name of the target cluster.

    

2. Click `Namespace` in the left navigation bar, and then click the `Create` button on the right side of the page.

    

3. Fill in the name of the namespace, configure the workspace and labels (optional settings), and click `OK`.

    !!! info

        - After a namespace is bound to a workspace, resources in the namespace will be shared with the bound workspace. For a detailed description of the workspace, please refer to [Workspace and Folder](../../../ghippo/user-guide/workspace/workspace.md).

        - After the namespace is created, it is still possible to bind/unbind the workspace.

    

4. Click `OK` to complete the creation of the namespace. On the right side of the namespace list, click `⋮`, and you can select update, bind/unbind workspace, quota management, delete and other operations from the pop-up menu.

    

### YAML creation

1. On the `Cluster List` page, click the name of the target cluster.

    

2. Click `Namespace` in the left navigation bar, and then click the `YAML Create` button on the right side of the page.

    

3. Input or paste the prepared YAML content, or directly import an existing YAML file locally.

    > After entering the YAML content, click `Download` to save the YAML file locally.

    

4. Finally, click `OK` in the lower right corner of the pop-up box.