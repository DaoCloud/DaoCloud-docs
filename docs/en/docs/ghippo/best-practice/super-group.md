# Governance Architecture for Large Enterprises

With the continuous expansion of the business and the continuous growth of the company, subsidiaries and branches are established one after another. Some subsidiaries even establish further subsidiaries. The original large departments are gradually subdivided into multiple small departments, resulting in an increasing number of hierarchical levels in the organizational structure. This change in the organizational structure also has an impact on the IT governance architecture.

## Best Practices

The specific steps are as follows:

### 1. Enable Isolation Mode between Folders/Workspaces

Use a user with Admin permissions to enter the global cluster of **Container Management**.

In the **Configuration** section, search for ghippo-apiserver-config and click the Edit YAML button in the right operation column to enter the YAML editing page.

In the YAML, change the value of the userIsolationMode field to Folder and click **OK**.

After modifying, restart the ghippo-apiserver. You can go to the stateless load balancing list, search for ghippo-apiserver, and restart it.

### 2. Plan the Enterprise Architecture According to the Actual Situation

In a multi-level organizational structure, it is recommended to use the second-level folder as the isolation unit to isolate users/user groups/resources between "subsidiaries". After isolation, users/user groups/resources between "subsidiaries" are not visible to each other.

### 3. Create Users/Integrate User Systems

The platform administrator Admin should centrally [create users](../user-guide/access-control/user.md) on the platform or integrate users into DCE 5.0 through identity providers such as LDAP/OIDC/OAuth2.0.

### 4. Create Folder Roles

In the isolation mode between Folders/Workspaces, the platform administrator Admin needs to invite users to various subsidiaries through **Authorization** before the "Subsidiary Administrators (Folder Admins)" can manage these users, such as secondary authorization or editing permissions. It is recommended to simplify the management work of the platform administrator Admin and create a role with no actual permissions to assist the platform administrator Admin in inviting users to subsidiaries through "Authorization". The actual permissions of subsidiary users are delegated to the subsidiary administrators (Folder Admins) for management.

!!! note

    The resource binding permission points are not effective when used alone, so it meets the above requirements of inviting users to subsidiaries through "Authorization" and then delegating the actual permissions of subsidiary users to the subsidiary administrators (Folder Admins) for management.

### 5. Grant Users Authorization

The platform administrator invites users to various subsidiaries through "Authorization" according to the actual situation and appoints subsidiary administrators.

Grant the "minirole" to subsidiary ordinary users and grant the "Folder admin" to subsidiary administrators.

### 6. Subsidiary Administrators Manage Users/User Groups on Their Own

After logging in to the platform, the subsidiary administrator (Folder Admin) can only see the "Subsidiary 2" to which they belong and can adjust the architecture by creating folders and workspaces. They can assign other permissions to users in Subsidiary 2 by adding authorization/editing permissions.

When adding authorization, the subsidiary administrator (Folder Admin) can only see the users invited by the platform administrator through "Authorization" and cannot see all the users on the platform, thus realizing the user isolation between Folders/Workspaces. The same applies to user groups. (The platform administrator can see and authorize all users and user groups on the platform.)

!!! note

    The main difference between a large enterprise and a large/medium/small enterprise is whether users/user groups can see each other between Folders and Workspaces. In a large enterprise, users/user groups between subsidiaries are not visible to each other + permissions are isolated; in a large/medium/small enterprise, users in different departments can see each other + permissions are isolated.
