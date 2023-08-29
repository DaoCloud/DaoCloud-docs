# Workspace Best Practices

A workspace is a resource grouping unit, and most resources can be bound to a certain workspace.
The workspace can realize the binding relationship between users and roles through authorization and resource binding, and apply it to all resources in the workspace at one time.

Through the workspace, you can easily manage teams and resources, and solve cross-module and cross-cluster resource authorization issues.

## Workspace features

A workspace consists of three features: authorization, resource groups, and shared resources. It mainly solves the problems of unified authorization of resources, resource grouping and resource quota.



1. Authorization: Grant users/groups different roles in the workspace, and apply the roles to the resources in the workspace.

    Best practice: When ordinary users want to use Workbench, microservice engine, service mesh, and middleware module features, or need to have permission to use container management and some resources in the service mesh, the administrator needs to grant the workspace permissions (Workspace Admin, Workspace Edit, Workspace View).
    The administrator here can be the Admin role, the Workspace Admin role of the workspace, or the Folder Admin role above the workspace.
    See [Relationship between Folder and Workspace](ws-folder.md).

2. Resource group: Resource group and shared resource are two resource management modes of the workspace.

    Resource groups support four resource types: Cluster, Cluster-Namespace (cross-cluster), Mesh, and Mesh-Namespace.
    A resource can only be bound to one resource group. After a resource is bound to a resource group, the owner of the workspace will have all the management rights of the resource, which is equivalent to the owner of the resource, so it is not limited by the resource quota.

    Best practice: The workspace can grant different role permissions to department members through the "authorization" function, and the workspace can apply the authorization relationship between people and roles to all resources in the workspace at one time. Therefore, the operation and maintenance personnel only need to bind resources to resource groups, and add different roles in the department to different resource groups to ensure that resource permissions are assigned correctly.

    | Department | Role | Cluster | Cross-cluster Cluster-Namespace | Mesh | Mesh-Namespace |
    | ------------ | --------------- | ------------ | ------- ----------------- | ------- | -------------- |
    | Department Admin | Workspace Admin | &check; | &check; | &check; | &check; |
    | Department Core Members | Workspace Edit | &check; | &cross; | &check; | &cross; |
    | Other Members | Workspace View | &check; | &cross; | &cross; | &cross; |

3. Shared resources: The shared resource feature is mainly for cluster resources.

    A cluster can be shared by multiple workspaces (referring to the shared resource feature in the workspace); a workspace can also use the resources of multiple clusters at the same time.
    However, resource sharing does not mean that the sharer (workspace) can use the shared resource (cluster) without restriction, so the resource quota that the sharer (workspace) can use is usually limited.

    At the same time, unlike resource groups, workspace members are only users of shared resources and can use resources in the cluster under resource quotas. For example, go to Workbench to create a namespace, deploy applications, etc., but do not have the management authority of the cluster. After the restriction, the total resource quota of the namespace created/bound under this workspace cannot exceed the resources set by the cluster in this workspace Use cap.

    Best practice: The operation and maintenance department has a high-availability cluster 01, and wants to allocate it to department A (workspace A) and department B (workspace B), where department A allocates 50 CPU cores, and department B allocates CPU 100 cores .
    Then you can borrow the concept of shared resources, share cluster 01 with department A and department B respectively, and limit the CPU usage quota of department A to 50, and the CPU usage quota of department B to 100.
    Then the administrator of department A (workspace A Admin) can create and use a namespace in Workbench, and the sum of the namespace quotas cannot exceed 50 cores, and the administrator of department B (workspace B Admin) can create a namespace in Workbench And use namespaces, where the sum of namespace credits cannot exceed 100 cores.
    The namespaces created by the administrators of department A and department B will be automatically bound to the department, and other members of the department will have the roles of Namesapce Admin, Namesapce Edit, and Namesapce View corresponding to the namespace (the department here refers to Workspace, workspace can also be mapped to other concepts such as organization, supplier, etc.). The whole process is as follows:

    | Department | Role | Cluster | Resource Quota |
    | ------------ | ------------------------------------ ------------------- | ------------ | ---------- |
    | Department Administrator A | Workspace Admin | CPU 50 cores | CPU 50 cores |
    | Department Administrator B | Workspace Admin | CPU 100 cores | CPU 100 cores |
    | Other Members of the Department | Namesapce Admin<br />Namesapce Edit<br />Namesapce View | Assign as Needed | Assign as Needed |

## The effect of the workspace on the DCE module

1. Module name: [Workbench](../../../amamba/intro/index.md), [Microservice Engine](../../../skoala/intro/index.md), [Service Mesh](../../../mspider/intro/index.md), [Middleware](../../../middleware/index.md)

    The premise of entering the above modules is to have the permission of a certain workspace, so you must have the Admin role or have certain role permissions of a certain workspace before using the module features.

    - The roles of the workspace are automatically applied to the resources contained in the workspace. For example, if you have the Workspace Admin role of workspace A, then you are the Admin role for all resources in this workspace;
    - If you are a Workspace Edit, you are the Edit role for all resources in the workspace;
    - If you are Workspace View, you are View role for all resources in the workspace.

    In addition, the resources you create in these modules will also be automatically bound to the corresponding workspace without any additional operations.

2. Module name: [Container Management](../../../kpanda/intro/index.md), [Service Mesh](../../../mspider/intro/index.md)

    Due to the particularity of functional modules, resources created in the container management module will not be automatically bound to a certain workspace.

    If you need to perform unified authorization management on people and resources through workspaces, you can manually bind the required resources to a certain workspace, so as to apply the roles of users in this workspace to resources (resources here can be cross- clustered).

    In addition, there is a slight difference between container management and service mesh in terms of resource binding entry. The workspace provides the binding entry of Cluster and Cluster-Namespace resources in container management, but has not opened the Mesh and Mesh-Namespace for service mesh. Bindings for Namespace resources.

    For Mesh and Mesh-Namespace resources, you can manually bind them in the resource list of the service mesh.

## Use Cases of Workspace

- Mapping to concepts such as different departments, projects, organizations, etc. At the same time, the roles of Workspace Admin, Workspace Edit, and Workspace View in the workspace can be mapped to different roles in departments, projects, and organizations
- Add resources for different purposes to different workspaces for separate management and use
- Set up completely independent administrators for different workspaces to realize user and authority management within the scope of the workspace
- Share resources to different workspaces, and limit the upper limit of resources that can be used by workspaces
