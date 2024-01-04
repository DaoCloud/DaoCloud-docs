# Description of folder permissions

Folders have permission mapping capabilities, which can map the permissions of users/groups in this folder to subfolders, workspaces and resources under it.

If the user/group is Folder Admin role in this folder, it is still Folder Admin role when mapped to a subfolder, and Workspace Admin is mapped to the workspace under it;
If a Namespace is bound in __Workspace and Folder__ -> __Resource Group__ , the user/group is also a Namespace Admin after mapping.

!!! note

    The permission mapping capability of folders will not be applied to shared resources, because sharing is to share the use permissions of the cluster to multiple workspaces, rather than assigning management permissions to workspaces, so permission inheritance and role mapping will not be implemented.

## Use cases

Folders have hierarchical capabilities, so when folders are mapped to departments/suppliers/projects in the enterprise,

- If a user/group has administrative authority (Admin) in the first-level department, the second-level, third-level, and fourth-level departments or projects under it also have administrative authority;
- If a user/group has access rights (Editor) in the first-level department, the second-, third-, and fourth-level departments or projects under it also have access rights;
- If a user/group has read-only permission (Viewer) in the first-level department, the second-level, third-level, and fourth-level departments or projects under it also have read-only permission.

| Objects | Actions | Folder Admin | Folder Editor | Folder Viewer |
| --------------------------- | -------- | ------------ | ------------- | ------------- |
| on the folder itself | view | &check; | &check; | &check; |
| | Authorization | &check; | &cross; | &cross; |
| | Modify Alias ​​| &check; | &check; | &cross; |
| To Subfolder | Create | &check; | &cross; | &cross; |
| | View | &check; | &check; | &check; |
| | Authorization | &check; | &cross; | &cross; |
| | Modify Alias ​​| &check; | &check; | &cross; |
| workspace under it | create | &check; | &cross; | &cross; |
| | View | &check; | &check; | &check; |
| | Authorization | &check; | &cross; | &cross; |
| | Modify Alias ​​| &check; | &check; | &cross; |
| Workspace under it - Resource Group | View | &check; | &check; | &check; |
| | resource binding | &check; | &cross; | &cross; |
| | unbind | &check; | &cross; | &cross; |
| Workspaces under it - Shared Resources | View | &check; | &check; | &check; |
| | New share | &check; | &cross; | &cross; |
| | Unshare | &check; | &cross; | &cross; |
| | Resource Quota | &check; | &cross; | &cross; |