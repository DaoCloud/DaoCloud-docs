# Glossary

This section lists common terms used in Global Management.

### IAM

IAM (Identity and Access Management) is the abbreviation for the access control module.
The administrator of this module is called the IAM Owner, who has the highest authority
of this module. Users (groups) assigned to the IAM Owner will have all and the
highest permissions for Access Control.

For more details, see [What is IAM](../user-guide/access-control/iam.md).

### RBAC

RBAC (Role-Based Access Control) assigns the concept of [role](../user-guide/access-control/role.md)
to users and associates users and permissions through roles to realize flexible configuration.
The three elements of the RBAC model are users, roles, and permissions.
Use RBAC mechanisms to authorize IAM users to access platform resources.

### User

A [user](../user-guide/access-control/user.md) is the subject of initiating operations.
Each user has a unique ID and granted different roles.
By default, the IAM user created does not have any permissions. You need to add it to
a group and grant a role or policy to allow the user to obtain corresponding permissions.

Users log in to DCE with usernames and operate platform resources and services according to the granted permissions.
Therefore, users are the subject of resource ownership and have corresponding permissions for the resources they own.

Users can modify user information, set passwords, access keys, and UI language in [Personal Center](../user-guide/personal-center/security-setting.md).

### Group

A [group](../user-guide/access-control/group.md) is a collection of one or more users.
IAM implements user authorization through groups.
Usually, you create an IAM user first, join a certain group, and the user will inherit
the permissions of this group. When a user joins multiple groups, the user will have the
permissions of multiple groups at the same time.

### Role

A [role](../user-guide/access-control/role.md) is a bridge connecting users and permissions.
A role corresponds to a set of permissions, and different roles have different permissions.
Granting a role to a user grants all the permissions included in the role.
There are two roles in Global Administration:

- Predefined roles: Created by the system, users can only use and cannot modify.
  Each submodule has an Admin role.

- Custom roles: Users create, update, and delete independently, and the permissions
  in custom roles are maintained by users themselves. At the same time, because the
  global management brings together multiple submodules, each submodule also has a
  corresponding administrator role, for example:

    - IAM Owner Manage Access Control, that is, manage users/groups and authorization

    - Workspace Admin: Permission to manage levels and workspaces, only this permission can create levels

    - Audit Admin: Manage audit logs

### Permissions

[Permissions](../user-guide/access-control/iam.md) refer to whether a user is allowed to
perform a certain operation on a specific resource. DCE adopts the RBAC model to aggregate
permissions into roles to lower the threshold of use. The administrator authorizes the role
to the user, and the user can obtain a set of permissions aggregated under the role at one time.

By default, the IAM users created by the administrator do not have any role permissions.
You need to grant roles to them individually or add them to groups and grant roles to groups
to enable users to obtain corresponding role permissions. This process is called authorization.
After authorization, users can operate platform resources based on the granted role permissions.

### Authorization

[Authorization](../user-guide/access-control/iam.md) refers to granting users the permissions
required to complete specific tasks, and the authorization takes effect through the permissions
of system roles or custom roles.
After obtaining specific permissions, users can operate on resources or services.

### Workspace

[Workspace](../user-guide/workspace/workspace.md) coordinates global management and sub-module permission relationships, resolves resource aggregation and mapping hierarchical relationships.
Usually, a workspace corresponds to a project, and different resources can be assigned to each workspace, and different users and groups can be assigned.

### Hierarchy

To meet the branch division of various departments in the enterprise, DCE introduces the concept of [level](../user-guide/workspace/ws-folder.md). Usually, the level corresponds to different departments, and each level can contain one or more workspaces.

### Resource

[Resource](../user-guide/workspace/quota.md) generally refers to the resources created by
each submodule on the DCE platform, which is the specific data to complete the authorization.
Usually, resources describe one or more operation objects, and each submodule has its resources and corresponding resource definition details, such as clusters, namespaces, gateways, etc.

The owner of the resource is the main account Super Admin. Super Admin has the authority to
create/manage/delete resources in each submodule. Ordinary users will not automatically have
access to resources without authorization, and Super Admin is required to authorize.
Workspace supports authorizing users (groups) to access resources across submodules.

### Credentials

[Identity Credentials](../user-guide/access-control/idprovider.md) are the basis for identifying user identities. When logging in and using resources, identity credentials are required to pass system authentication.
Identity credentials include passwords and access keys, and you can manage the identity credentials of yourself and subordinate IAM users through IAM.

For more terms, please refer to the [Cloud Native Glossary](../../dce/terms.md) included on this site.
