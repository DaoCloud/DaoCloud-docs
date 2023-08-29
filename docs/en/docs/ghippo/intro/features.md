---
hide:
   - toc
---

# Features

This page describes the features of Global Management.

1. Users

    Having a user account is a prerequisite for users to access the DCE platform.
    [User](../user-guide/access-control/user.md) is created by Super Admin or IAM Admin in `Global Management` -> `Access Control` -> `Users` page, or connected via LDAP.
    Each user has an independent username and password. By granting different permissions to a single or a group of users, users have access to different resources.

    ```mermaid
    graph LR

        admin([Admin or<br>user and access administrator]) --> |create and manage users|user[User]
        user --> user1[User A]
        user --> user2[User B]
        user --> user3[User C]
        
    click user "https://docs.daocloud.io/en/ghippo/user-guide/access-control/user/"

    classDef plain fill:#ddd,stroke:#fff,stroke-width:0px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:0px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class admin plain;
    class user1,user2,user3 k8s;
    class user cluster
    ```

2. Groups

    [group](../user-guide/access-control/group.md) is a collection of multiple users.
    Users can inherit the role permissions of the group by joining the group. Authorize users in batches through groups to better manage users and their permissions.

    ```mermaid
    graph LR

        admin([Admin or<br>User and Access Administrator])
        admin --> user[Create user]
        admin --> group[Create group]
        admin --> add[Add user to group]
        
    click user "https://docs.daocloud.io/en/ghippo/user-guide/access-control/user/"
    click group "https://docs.daocloud.io/en/ghippo/user-guide/access-control/group/"
    click add "https://docs.daocloud.io/en/ghippo/user-guide/access-control/group/#_5"

    classDef plain fill:#ddd,stroke:#fff,stroke-width:0px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:0px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class admin plain;
    class user,group,add cluster
    ```

3. Roles

    A [role](../user-guide/access-control/role.md) corresponds to a set of permissions.
    Permissions determine the actions that can be performed on a resource. Granting a role to a user grants all the permissions included in that role.
    You can divide the management rights of different modules to different users,
    For example, user A manages the container management module, user B manages Workbench module, and jointly manages the observability module.

4. Workspaces

    [Workspaces](../user-guide/workspace/workspace.md) are used to manage resources and consist of two parts: folders and workspaces.

    Levels represent nodes in the resource hierarchy, and each level can contain workspaces, other levels, or both. The hierarchy can be understood as a variety of concepts, such as hierarchical departments, environments, or suppliers.

    Workspaces can be thought of as projects under their respective department, and administrators can map the hierarchical relationship within the enterprise using the hierarchy and workspaces.

    Although a hierarchy may contain multiple hierarchies or workspaces, a given hierarchy or workspace can only have one parent.

5. Audit Logs

    [Audit Logs](../user-guide/audit/audit-log.md) completely records users' various operations, including operations initiated by users through pages or API interfaces and self-triggered operations within each service. It enables combined queries through multiple dimensions, such as event source, resource type, and operation status, and supports audit log export.

6. Platform Settings

    [Platform Settings](../user-guide/platform-setting/about.md) include account security settings, appearance customization, and mail server settings. When it is necessary to manage platform-level settings, such as account security information, platform logos, license authorization, and mail server, Admins can operate through `Platform Settings`. Admins have exclusive management rights for platform settings.

    ```mermaid
    graph LR

        admin([Admin]) --> |management|about[Platform settings]
        about --> password[User password and other security policies]
        about --> appear[Platform appearance customization]
        about --> mail[Mail server]
        about --> license[Genuine authorization]
        
    click about "https://docs.daocloud.io/en/ghippo/user-guide/platform-setting/about/"
    click password "https://docs.daocloud.io/en/ghippo/user-guide/password/"
    click appear "https://docs.daocloud.io/en/ghippo/user-guide/platform-setting/appearance/"
    click mail "https://docs.daocloud.io/en/ghippo/user-guide/platform-setting/mail-server/"
    click license "https://docs.daocloud.io/en/dce/license0/"

    classDef plain fill:#ddd,stroke:#fff,stroke-width:0px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:0px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class admin plain;
    class about,password,appear,mail,license cluster
    ```

## List of Features

Below is a list of features available:

1. Access Control
    1. [Users](../user-guide/access-control/user.md)
        - Display username, description, creation time and last login time in the list
        - Support searching users by username
        - Quick authorization to users from the list
        - Quickly add users to groups from the list
        - Batch deletion of users
        - Create users
        - Edit basic user information such as email, description, enable/disable etc.
        - Record user authorization information
        - Record group membership information
        - Admins can help users change passwords
        - Admins can help users create access keys
    2. [Groups](../user-guide/access-control/group.md)
        - Display group name, number of users in group, description, and creation time in the list
        - Support searching by group name
        - Quick authorization to groups from the list
        - Quickly add users to groups from the list
        - Batch deletion of groups
        - Create groups
        - Edit group basic information such as description
        - Record group authorization information
        - Record group member information
    3. [Roles](../user-guide/access-control/role.md)
        - Display system role name and description in the list
        - Record role authorization information
        - Supports predefined folder roles: Folder Admin, Folder Editor, and Folder Viewer
        - Supports predefined workspace roles: Workspace Admin, Workspace Editor, and Workspace Viewer
    4. [Identity Provider](../user-guide/access-control/idprovider.md)
        - Support LDAP and OIDC connections to external users
        - LDAP protocol supports manual/automatic synchronization of external users
        - LDAP protocol supports manual synchronization of external groups
        - OIDC protocol supports manual synchronization of external users
2. Workspace and Folders
    1. [Folders](../user-guide/workspace/folders.md)
        - Display folders and workspaces in a tree structure
        - Support searching by folder name and workspace name
        - Map up to 5 levels of folders for enterprise hierarchy
        - Add users/groups to folders and authorize them
        - Inherit permissions, subfolders, and workspaces inherit the permissions of users/groups in the parent folder
        - Move folders while changing department mappings in the enterprise
    2. [Workspaces](../user-guide/workspace/workspace.md)
        - Add users to the workspace/usergroup and authorize
        - Add resources to workspace - Resource group, supports 6 resource types
        - Permissions inheritance, resources in the resource group can inherit the roles of the user/group in the workspace and parent folder
        - Mobile workspaces, after the move, resources/members under it will follow the movement of the workspace
        - Add resources to the workspace - Share resources, share a cluster resource with multiple workspaces
        - Resource quotas for each shared cluster resource
        - Resource quotas through six dimensions: CPU Limit, CPU Request, Memory Limit, Memory Request, total storage request Request Storage, and storage volume statement PersistentVolumeClaim
3. [Audit Logs](../user-guide/audit/audit-log.md)
    - Display event name, resource type, resource name, status, operator, and operation time in the list
    - View audit log details from the list
    - Display audit logs of the latest day or custom time
    - Search audit logs by status, operator, resource type, and resource name
    - Export audit logs in .csv format
    - Collect all audit logs of global management by default
    - Keep audit logs for 365 days by default
    - Manually/auto-clean audit logs for global management
    - Enable/disable the collection of K8s audit logs
    - Manually/auto-clean K8s audit logs
4. [Platform Settings](../user-guide/platform-setting/security.md)
    1. Security Policy
        - Custom password rules
        - Custom password policy
        - Custom session timeout policy
        - Custom account lock strategy
        - Login and logout strategy
    2. [Email Settings](../user-guide/platform-setting/mail-server.md)
        - Configure the mail server
        - Retrieve user passwords by email
        - Receive alert notifications, etc.
    3. [Custom Appearance](../user-guide/platform-setting/appearance.md)
        - Custom login page appearance, including platform LOGO, login page icon, tab page icon, etc.
        - One-click restore login page appearance configuration
        - Customize the top navigation bar, including navigation bar icons, tab page icons, etc.
        - One-click restoration of the appearance configuration of the top navigation bar
    4. [Licensing](../../dce/license0.md)
        - Show license name, module it belongs to, license level, and expiration time of the license status in the list
        - Manage licenses to ensure submodules are within the validity period
     5. [About](../user-guide/platform-setting/about.md)
        - Display module version
        - Support for open source software supported by the demonstration platform
        - Display technical team style
5. Personal center
    1. [Security Settings](../user-guide/personal-center/security-setting.md)
        - Update login password
        - Retrieve login password through email
    2. [Access Keys](../user-guide/personal-center/accesstoken.md)
        - Each user can create an independent API key
        - API key expiration settings to ensure system security
    3. [Language Settings](../user-guide/personal-center/language.md)
        - Supports multiple languages: Simplified Chinese, English, automatically detects browser's preferred language
