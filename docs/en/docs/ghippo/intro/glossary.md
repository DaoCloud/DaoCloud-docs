# Glossary

This section lists common terms for global management.

### IAM

IAM (Identity and access management) is the abbreviation of the access control module. The administrator of this module is called IAM Admin, who has the highest authority of this module.
Users (groups) assigned to IAM Admin will have all and the highest permissions for users and access control.

For more details, see [What is IAM](../user-guide/access-control/iam.md).

### RBAC

RBAC (Role-based access control, role-based access control), the basic idea is to assign the concept of [role](../user-guide/access-control/Role.md) to users, and to associate users and permissions through roles. Realize flexible configuration.
The three elements of the RBAC model are: users, roles, and permissions. Use RBAC mechanisms to authorize IAM users to access platform resources.

### User

[User](../user-guide/access-control/User.md) is the subject of initiating operations. Each user has a unique ID and is granted different roles.
The IAM user created by default does not have any permissions. You need to add it to a group and grant a role or policy to allow the user to obtain the corresponding permissions.

Users log in to DCE with usernames and operate platform resources and services according to the granted permissions.
Therefore, users are the subject of resource ownership and have corresponding permissions for the resources they own.

Users can modify user information, set password, access key and UI language in [Personal Center](../user-guide/personal-center/SecuritySetting.md).

### Group

[group](../user-guide/access-control/Group.md) is a collection of one or more users. IAM can implement user authorization through groups.
Usually create an IAM user first, join a certain group, the user will inherit the permissions of this group. When a user joins multiple groups, the user will have the permissions of multiple groups at the same time.

### Role

[Role](../user-guide/access-control/Role.md) is a bridge connecting users and permissions. A role corresponds to a set of permissions, and different roles have different permissions. Granting a role to a user grants all the permissions included in the role. There are two roles in Global Administration:

- Predefined roles: Created by the system, users can only use and cannot modify, each sub-module has an administrator Admin role.

- Custom roles: users create, update and delete independently, and the permissions in custom roles are maintained by users themselves. At the same time, because the global management brings together multiple sub-modules, each sub-module also has a corresponding administrator role, for example:

    - IAM Admin: Manage users and access control, that is, manage users/groups and authorization

    - Workspace Admin: Permission to manage levels and workspaces, only this permission can create levels

    - Audit Admin: Manage audit logs

### Permissions

[Privilege](../user-guide/access-control/iam.md) refers to whether a user is allowed to perform a certain operation on a certain resource.
In order to lower the threshold of use, DCE adopts the RBAC model to aggregate permissions into roles. The administrator only needs to authorize the role to the user, and the user can obtain a set of permissions aggregated under the role at one time.

By default, the IAM users created by the administrator do not have any role permissions. You need to grant roles to them individually or add them to groups and grant roles to groups to enable users to obtain corresponding role permissions. This process is called authorization.
After authorization, users can operate platform resources based on the granted role permissions.

### Authorization

[Authorization](../user-guide/access-control/iam.md) refers to granting users the permissions required to complete specific tasks, and the authorization takes effect through the permissions of system roles or custom roles.
After obtaining specific permissions, users can operate on resources or services.

### Workspace

Use [Workspace](../user-guide/workspace/Workspaces.md) to coordinate global management and sub-module permission relationships, and resolve resource aggregation and mapping hierarchical relationships.
Usually a workspace corresponds to a project, and different resources can be assigned to each workspace, and different users and groups can be assigned.

### Hierarchy

See the figure above, in order to meet the branch division of various departments in the enterprise, DCE introduces the concept of [level](../user-guide/workspace/ws-folder.md), usually the level corresponds to different departments, and each level can contain One or more workspaces.

### Resource

[Resource](../user-guide/workspace/quota.md) generally refers to the resources created by each sub-module on the DCE platform, which is the specific data to complete the authorization.
Usually resources describe one or more operation objects, and each sub-module has its own resources and corresponding resource definition details, such as clusters, namesapce, gateways, etc.

The owner of the resource is the main account Super Admin. Super Admin has the authority to create/manage/delete resources in each sub-module. Ordinary users will not automatically have access to resources without authorization, and Super Admin is required to authorize.
Workspace supports authorizing users (groups) to access resources across submodules.

### Credentials

[Identity Credentials](../user-guide/access-control/idprovider.md) is the basis for identifying user identities. When logging in and using resources, identity credentials are required to pass system authentication.
Identity credentials include passwords and access keys, and you can manage the identity credentials of yourself and subordinate IAM users through IAM.

For more terms, please refer to [Cloud Native Glossary](../..//dce/terms.md) included in this site.
