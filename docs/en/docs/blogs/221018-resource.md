# 5.0 Introduction to Resource Management Capabilities

As the scale of the enterprise expands, the resources under management and control must become increasingly complex: thousands of servers, machinery and equipment, electronic devices and other tangible fixed assets; daily office software, professional finance/personnel/OA/project management/development, etc. Software; management, employees, staff, etc. resources.

How to efficiently manage these resources?

![resource](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/resource01.png)

The essence of resource-based management capabilities is to establish a set of relationship structures related to the enterprise and based on the use of resources.
In DCE 5.0, it is mainly realized through the workspace and hierarchical module, which has the characteristics of global consistency, which is convenient for you to efficiently plan and manage various resources in multiple sub-modules on the platform based on this relationship structure.

There are two concepts in the Workspace and Folder module: hierarchy and workspace.
Hierarchy can be mapped to concepts such as project, environment, and supplier in the enterprise, so that you can build an enterprise hierarchical relationship that reflects resource relationships based on the business or ecological environment of the enterprise.
At the same time, the hierarchy has the ability to inherit permissions. The upper-level administrators can create and manage lower-level levels and workspaces, effectively solving the problem of one-time authorization in the hierarchical structure.
The workspace is directly associated with resources, supports multi-dimensional resources such as exclusive resource sharing and resource sharing, and cross-cluster resource management capabilities to meet the needs of rapid resource authorization and flexible resource allocation under hundreds of clusters.
At the same time, the Workspace and Folder module also supports the feature of mobile hierarchy and mobile workspace, and can respond to resource adjustments brought about by the adjustment of enterprise hierarchy at any time.

## User interaction for resource management

The resource management module is a hierarchical resource isolation and resource grouping module, which mainly solves the problems of resource unified authorization, resource grouping and resource quota.
The resource management module has two concepts: hierarchy and workspace.
In the resource management module, you can build the hierarchical relationship of enterprise business through hierarchy, and manage resources through resource groups and shared resources in the workspace, so that users (groups) of the resource management module can share resources in the workspace.

Resources are at the lowest level of the resource management module hierarchy, and resources include Cluster, Namespace, Pipeline, and Gateway.
The parent of all these lower-level resources can only be the workspace, and the workspace is a resource grouping unit as a resource container.
A workspace usually refers to a project or environment, and the resources in each workspace are logically isolated from those in other workspaces.
You can grant users (groups of users) different access rights to the same set of resources through authorization in the workspace.

Workspaces are at the first level, counting from the bottom of the hierarchy, and contain resources.
All resources except shared resources have one and only one parent. All workspaces also have one and only one parent hierarchy.

Hierarchy is a further grouping mechanism based on workspaces and has a hierarchical structure. A level can contain workspaces, other levels, or a combination of both, forming a tree-like organizational relationship.
Hierarchies allow you to map enterprise business hierarchy relationships and group workspaces by department. Hierarchy is not directly linked to resources, but indirectly implements resource grouping through workspaces.
A level has one and only one parent level, and the root level is the highest level of the hierarchy, so there is no parent level, and both the level and the workspace are attached to the root level.

At the same time, users (groups) in the hierarchy can inherit permissions from their parents through the hierarchy.
The authority of each node of the user in the hierarchical structure comes from the combined result of the authority obtained directly at the node and the authority inherited from its parent. The authority is an additive relationship and there is no mutual exclusion.

![resource](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/resource02.png)

Resources are grouped through workspaces, and there are two grouping modes in workspaces, resource groups and shared resources.
A resource can only be added to one resource group, and the resource group corresponds to the workspace one by one. After the resource is added to the resource group, the owner of the workspace will obtain the management authority of the resource, which is equivalent to the owner of the resource.
For shared resources, multiple workspaces can share one or more resources. Resource owners can choose to share their own resources with the workspace. Generally, when sharing, the resource owner will limit the amount of resources that can be used by the shared workspace.
After resources are shared, the owner of the workspace only has resource usage rights under the resource limit, and cannot manage resources or adjust the amount of resources that the workspace can use.
At the same time, shared resources also have certain requirements for the resources themselves. Only hierarchical resources can be shared, such as Cluster-Namespace. Cluster resource owners can share Cluster resources to different workspaces, and limit the workspace to this Cluster. The workspace owner can create multiple Namespaces within the resource quota, but the sum of the resource quotas of the Namespaces cannot exceed the resource quota of the Cluster in the workspace. For Kubernetes resources, the only resource type that can be shared currently is Cluster.

[Free Trial](../dce/license0.md){ .md-button .md-button--primary }

## Resource management elements

After installing DCE 5.0, the platform will automatically create a root level for the user during the initialization phase. The root level is located at the top level of the resource hierarchy of the resource management module and has no parent. Resource relationships are distributed downwards according to the root level, and up to 5 levels of hierarchy are supported.

### Hierarchy

The platform administrator creates a new hierarchy under the root hierarchy based on the existing hierarchy of the enterprise.
Hierarchy can be mapped to concepts such as enterprise projects, environments, suppliers, etc. Hierarchy has a hierarchical structure and authority inheritance, and is a node of the resource hierarchy structure of the resource management module.
A hierarchy can contain workspaces, other hierarchies, or a combination of both.
The newly created hierarchy must have a parent, and the lower hierarchy and workspace will inherit the permissions of the parent file, so the actual permissions of the user in the hierarchy or workspace are derived from the permissions inherited from the parent hierarchy and the permissions obtained at this node. and.

### Workspace

Workspace is a resource isolation unit in the resource management module, which has two modes: resource group and shared resource, and is directly associated with resources.
A workspace has one and only one parent level, and the workspace and the resources under it will inherit the permissions of the parent level.

In DCE 5.0, due to the different authorization methods of resources, resources that strongly depend on workspace authorization, such as gateways, pipelines, etc., are derived; and resources that can be selectively bound to workspaces, such as Cluster and Namespace.

Since the resources of Workbench, microservice engine, and service mesh take the workspace as the top-level concept, the resources are completely dependent on the workspace for authorization, so the resources will be automatically bound to a certain workspace, and the owner of the workspace is The owner of the resource.
Such resources do not need to be manually bound, and the resources do not need to be displayed in the resource group of the workspace. The prerequisite for users (groups) to use resources is to be granted the corresponding permissions in the workspace.
For Cluster and Namespace resources, since container management has an independent authorization module, resource owners have the right to selectively bind.
The resource is manually bound to the resource group of the workspace, which means that the workspace owner is allowed to manage and use the resource. At this time, the workspace owner is equivalent to the resource owner, and the bound resources will be displayed in the resource group of the workspace , and can be unbound at any time.
The resource is bound to the shared resource of the workspace, which means that the resource owner is allowed to use the resource within the resource limit. Currently, the only resource type that can be shared is Cluster.

### Resource Quotas

Sharing resources does not mean that the shareee can use the shared resources indefinitely. Generally, the resource owner will limit the upper limit of the resource that the workspace can use.
For example, when a Cluster is shared to a workspace, the owner of the workspace has the right to create a Namespace on the Cluster.
If the Cluster owner sets the upper limit of the resource quota of the workspace on the Cluster as Quota=100, then the sum of the Quota of the Namespace cannot exceed 100.
Similarly, when multiple Clusters are shared to the workspace, each Cluster owner can set the quota usage limit of the workspace on each Cluster.
In addition, in addition to Quota, resource owners can also limit the upper limit of resource quotas through multiple dimensions such as CPU, memory, and Secret.
(The prerequisite for the resource owner to be able to share resources: to be the owner of both the Cluster and the workspace).

### Moving Hierarchies and Workspaces

The adjustment of departmental relationship or project relationship may change the authorization relationship of resources at any time, which is born in order to be able to adapt to the situation, move the hierarchy and move the application of the workspace function.
Taking moving a hierarchy as an example, since the permissions of resources, workspaces, and hierarchies have an inheritance relationship, after moving a hierarchy, the original parent hierarchy will lose the management authority for the hierarchy and its sub-levels, workspaces, and resources in the space.
The new parent gains administrative rights to the hierarchy and its sub-hierarchies, workspaces, and resources in spaces.
There is no change to the authorization relationship of the level itself and its sublevels. Workspace is the same.

## Who Needs Resource Management

Enterprise users who need to manage K8S, microservice engine, service mesh and other resources, and the resources have a certain scale

### Solve what problem

1. There are many employees in the enterprise and there is a multi-level structure, such as multi-level suppliers, multi-level departments, etc., and resources are often concentrated in the hands of a small number of operation and maintenance personnel. Resource distribution and resource management consume a lot of manpower and material resources
2. The hierarchical structure of the enterprise is changeable, unable to flexibly respond to changes in personnel authority and resource ownership brought about by departmental adjustments
3. Project-driven enterprises need multiple authorizations for the same group of people and the same resources
4. For the same resource, it is a security risk for multiple people to have the same authority

### Applicable scene

1. Explore more convenient resource distribution and resource management methods, reduce manpower and material resource consumption, and reduce costs
2. The resource management method maps the hierarchical structure of the enterprise, decentralizes power and self-control according to the hierarchy, responds to enterprise changes more flexibly, and accesses more suppliers at the same time to expand the scope of business
3. More refined resource authority control, set management, use, read-only and other permissions for the same resource, and issue different permissions to different members to minimize security risks and further reduce accident rates

## FAQs

1. In what cases do you need to use layers?

     Answer: Hierarchy can be mapped to concepts such as enterprise projects, environments, and suppliers, with hierarchical structure and authority inheritance capabilities. It can effectively deal with the resource allocation problems of multi-level suppliers encountered by enterprises.

2. In what cases do I need to use the workspace?

     A: The resource is directly associated with the workspace, and the resource will inherit the permissions of the workspace.
     When the number of resources is large, the unified authorization of resources through the workspace can effectively reduce the workload of resource operation and maintenance.
     In addition, in DCE 5.0, the resources in Workbench, microservice engine, and service mesh depend on the workspace authorization, so the prerequisite for creating such resources is to have the corresponding permissions of the workspace.

3. What is the relationship between hierarchy, workspace and resources?

     Answer: Resources are directly associated with workspaces, and resource permissions inherit the permissions of the workspace; while the workspace must belong to a certain level, and the workspace permissions inherit the level permissions, so users with level permissions are equivalent to the users in the workspace below them. Resources have corresponding permissions, but resources are not directly bound to a hierarchy.

4. Will resources and permissions change when moving layers or workspaces?

     Answer: Resources are bound under the workspace and will move with the movement of the hierarchy or workspace.
     Because resources inherit the permissions of the workspace, and the workspace inherits the permissions of the hierarchy, the original permission inheritance relationship will be changed after moving the workspace or hierarchy. The superior of the original hierarchy or workspace loses the management authority of the hierarchy or workspace. and its superiors start to have the management authority of the level or workspace.

5. Who can create Folders?

     Answer: Admin, Workspace Owner, and upper-level Folder Admin.

6. Who can create a Workspace?

     Answer: Admin, Workspace Owner, Folder Admin.

7. Who can I ask for authorization for microservice governance, Workbench, and service mesh permissions?

     Answer: The resources under microservice governance, Workbench, and service mesh are all automatically bound to Workspace, and permissions are strongly dependent on Workspace. You need to obtain Workspace permissions and then obtain related resource permissions.
     Admin, Workspace Owner, Folder Admin, and Workspace Admin can be authorized for Workspace.

[Learn about service mesh](../ghippo/intro/index.md){ .md-button }

[Download DCE 5.0](../download/index.md){ .md-button .md-button--primary }
[Install DCE 5.0](../install/index.md){ .md-button .md-button--primary }
[Free Trial](../dce/license0.md){ .md-button .md-button--primary }
