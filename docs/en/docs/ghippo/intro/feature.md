---
hide:
   - toc
---

# Features

This page describes the features of Global Management.

1. User Management

     Having a user account is a prerequisite for users to access the DCE platform.
     [User](../user-guide/access-control/User.md) is created by Super Admin or IAM Admin in `Global Management` -> `Users and Access Control` -> `Users` page, or connected via LDAP.
     Each user has an independent user name and password. By granting different permissions to a single or a group of users, different users have access to different resources.

     ```mermaid
     graph LR

         admin([Admin or<br>user and access administrator]) --> |create and manage users|user[User]
         user --> user1[User A]
         user --> user2[User B]
         user --> user3[User C]
        
    click user "https://docs.daocloud.io/en/ghippo/04UserGuide/01UserandAccess/User/"

    classDef plain fill:#ddd,stroke:#fff,stroke-width:0px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:0px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class admin plain;
    class user1,user2,user3 k8s;
    class user cluster
     ```

2. Group management

     [group](../user-guide/access-control/Group.md) is a collection of multiple users.
     Users can inherit the role permissions of the group by joining the group. Authorize users in batches through groups to better manage users and their permissions.

     ```mermaid
     graph LR

         admin([Admin or<br>User and Access Administrator])
         admin --> user[Create user]
         admin --> group[Create group]
         admin --> add[Add user to group]
        
    click user "https://docs.daocloud.io/en/ghippo/04UserGuide/01UserandAccess/User/"
    click group "https://docs.daocloud.io/en/ghippo/04UserGuide/01UserandAccess/Group/"
    click add "https://docs.daocloud.io/en/ghippo/04UserGuide/01UserandAccess/Group/#_5"

    classDef plain fill:#ddd,stroke:#fff,stroke-width:0px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:0px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class admin plain;
    class user,group,add cluster
     ```

3. Role Management

     A [role](../user-guide/access-control/Role.md) corresponds to a set of permissions.
     Permissions determine the actions that can be performed on a resource. Granting a role to a user grants all the permissions included in that role.
     You can divide the management rights of different modules to different users,
     For example, user A manages the container management module, user B manages the App Workbench module, and jointly manages the observability module.

     

4. Workspace

     [Workspace](../user-guide/workspace/Workspaces.md) is used to manage resources, including two parts: hierarchy and workspace.

     Levels are nodes in the resource hierarchy, and a level can contain workspaces, other levels, or a combination of both.
     Hierarchy can be understood as a variety of concepts such as hierarchical departments, environments, and suppliers.

     The workspace can be understood as the project under the department, and the administrator maps the hierarchical relationship in the enterprise through the hierarchy and the workspace.

     Although a hierarchy can contain multiple hierarchies or workspaces, a given hierarchy or workspace can only have one parent.

     

5. Audit logs

     [Audit Log](../user-guide/audit-log.md) completely records the user's various operations,
     Including operations initiated by users through pages or API interfaces and self-triggered operations within each service.
     It supports combined query through multiple dimensions such as event source, resource type, and operation status, and supports audit log export.

6. Platform Settings

     [Platform Settings](../user-guide/platform-setting/about.md) includes account security settings, appearance customization, mail server, etc.
     When it is necessary to manage platform-level settings such as account security information, platform logo, license authorization, and mail server,
     It can be operated through `Platform Settings`, and only Admin have management rights for platform settings.

     ```mermaid
     graph LR

         admin([Admin]) --> |management|about[Platform settings]
         about --> password[User password and other security policies]
         about --> appear[Platform appearance customization]
         about --> mail[Mail server]
         about --> license[Genuine authorization]
        
    click about "https://docs.daocloud.io/en/ghippo/04UserGuide/04PlatformSetting/about/"
    click password "https://docs.daocloud.io/en/ghippo/04UserGuide/password/"
    click appear "https://docs.daocloud.io/en/ghippo/04UserGuide/04PlatformSetting/Appearance/"
    click mail "https://docs.daocloud.io/en/ghippo/04UserGuide/04PlatformSetting/MailServer/"
    click license "https://docs.daocloud.io/en/dce/license0/"

    classDef plain fill:#ddd,stroke:#fff,stroke-width:0px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:0px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class admin plain;
    class about,password,appear,mail,license cluster
     ```

## List of functions

The specific function list is described below.

1. Users and Access Control
    1. [User](../user-guide/access-control/User.md)
         - List display username, description, creation time, last login time
         - List supports searching users by username
         - The list supports quick authorization to users
         - The list supports quickly adding users to groups
         - The list supports batch deletion of users
         - List support for creating users
         - Details support editing basic user information, including email, description, enable/disable, etc.
         - Detailed support for recording user authorization information, support for adding/removing permissions
         - Details support recording user joining group information, support users joining new groups, support removing users from old groups
         - Support administrators to help users change passwords
         - Support administrators to help users create access keys
    2. [group](../user-guide/access-control/Group.md)
         - List display group name, number of users in the group, description, creation time
         - The list supports searching by group name
         - The list supports quick authorization to groups
         - The list supports quickly adding users to groups
         - The list supports batch deletion of groups
         - List supports creating groups
         - Details support editing group basic information, such as description
         - Detailed support for recording group authorization information, support for adding/removing permissions
         - Detailed support for recording group member information, support for adding new members to groups, and support for removing members from groups
    3. [Role](../user-guide/access-control/Role.md)
         - List display system role name, description
         - Record role authorization information in detail, support granting roles to users/groups, and support removing users/groups from this role
         - Supports three predefined folder roles: Folder Admin, Folder Editor, and Folder Viewer
         - Supports three predefined workspace roles: Workspace Admin, Workspace Editor, and Workspace Viewer
    4. [Identity Provider](../user-guide/access-control/idprovider.md)
         - Support LDAP and OIDC to connect to external users
         - LDAP protocol supports manual/automatic synchronization of external users
         - LDAP protocol supports manual synchronization of external groups
         - OIDC protocol supports manual synchronization of external users
2. Workspace and Hierarchy
    1. [Folders](../user-guide/workspace/folders.md)
         - Support tree structure to display folders and workspaces
         - Supports searching by folder name and workspace name
         - Support 5-level folder mapping enterprise hierarchy
         - Support for adding users/groups to folders and authorizing them
         - Support permission inheritance, subfolders and workspaces can inherit the permissions of users/groups in the parent folder
         - Support moving folders. Mapping changes of departments in the enterprise, after the move, the subfolders, workspaces and their resources/members under it will follow the move of the folder, and the inheritance relationship of permissions will change again
    2. [Workspaces](../user-guide/workspace/Workspaces.md)
         - Support for adding users to the workspace/usergroup and authorize
         - Support adding resources to workspace - Resource group, supports 6 resource types
         - Support permission inheritance, the resources in the resource group can inherit the roles of the user/group in the workspace and parent folder
         - Support for mobile workspaces. Mapping project changes in the enterprise, after the move, the resources/members under it will follow the movement of the workspace, and the inheritance relationship of permissions will change again (under development)
         - Support adding resources to the workspace - Share resources, share a cluster resource to multiple workspaces
         - Support for resource quotas for each shared cluster resource
         - Supports resource quotas through six dimensions: CPU Limit, CPU Request, Memory Limit, Memory Request, total storage request Request Storage, and storage volume statement PersistentVolumeClaim
3. [Audit Log](../user-guide/audit-log.md)
     - List display event name, resource type, resource name, status, operator, operation time
     - List support to view audit log details
     - The list supports displaying the audit logs of the latest day or a custom time
     - The list supports searching audit logs by status, operator, resource type, and resource name
     - List supports exporting audit logs in .csv format
     - Collect all audit logs of global management by default
     - Audit logs are kept for 365 days by default
     - Supports manual/automatic cleaning of audit logs for global management
     - Support to enable/disable the collection of K8s audit logs
     - Support manual/automatic cleaning of K8s audit logs
4. Platform Settings
    1. Security Policy
         - Support custom password rules
         - Support custom password policy
         - Support custom session timeout policy, automatically log out of the current account when the time is exceeded
         - Support custom account lock strategy, if you fail to log in multiple times within the time limit, the account will be locked
         - Support login and logout strategy, log out while closing the browser after opening
    2. [Mail Server Settings](../user-guide/platform-setting/MailServer.md): Support administrators to configure the mail server, support retrieving user passwords by mail, receive alarm notifications, etc.
    3. [Appearance Customization](../user-guide/platform-setting/Appearance.md)
         - Support custom login page, including changing platform LOGO, login page icon, tab page icon, etc.
         - Support one-click restore login page appearance configuration
         - Support for customizing the top navigation bar, including navigation bar icons, tab page icons, etc.
         - Support for one-click restoration of the appearance configuration of the top navigation bar
    4. [Genuine License](../../dce/license0.md)
         - The list shows the license name, the module it belongs to, the license level, and the expiration time of the license status
         - Support for managing licenses to ensure submodules are within the validity period
    5. [About Platform](../user-guide/platform-setting/about.md)
         - Support display module version
         - Open source software supported by the demonstration platform
         - Support the display of technical team style
5. Personal center
    1. [Security Settings](../user-guide/personal-center/SecuritySetting.md)
         - Support users to update login password
         - Support retrieving login password through email
    2. [Access Key](../user-guide/personal-center/Password.md): Support each user to create an independent API key, and support API key expiration settings to ensure system security
    3. [Language Settings](../user-guide/personal-center/Language.md): Supports multiple languages, supports Simplified Chinese, English, and automatically detects your browser's preferred language to determine the language in three ways
