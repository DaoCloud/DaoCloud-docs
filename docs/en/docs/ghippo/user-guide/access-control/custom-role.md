# custom role

DCE 5.0 supports the creation of three scopes of custom roles:

- The permissions of **Platform Role** take effect on all relevant resources of the platform
- The permissions of **workspace role** take effect on the resources under the workspace where the user is located
- The permissions of **folder role** take effect on the folder where the user is located and the subfolders and workspace resources under it

## Create a platform role

A platform role refers to a role that can manipulate features related to a certain module of DCE 5.0 (such as container management, microservice engine, multi-cloud orchestration, service mesh, Container registry, App Workbench, and global management, etc.).

1. From the left navigation bar, click `Global Management` -> `Access Control` -> `Roles`, and click `Create Custom Role`.

     

1. Enter the name and description, select `Platform Role`, check the role permissions and click `OK`.

     

1. Return to the role list, search for the custom role you just created, and click `⋮` on the right to perform operations such as copying, editing, and deleting.

     

1. After the platform role is successfully created, you can go to [User](user.md)/[User Group](group.md) to authorize to add users and user groups for this role.

## Create a workspace role

A workspace role refers to a role that can manipulate features related to a module (such as container management, microservice engine, multi-cloud orchestration, service mesh, container registry, App Workbench, and global management) according to the workspace.

1. From the left navigation bar, click `Global Management` -> `Access Control` -> `Roles`, and click `Create Custom Role`.

     

1. Enter the name and description, select `workspace role`, check the role permissions and click `OK`.

     

1. Return to the role list, search for the custom role you just created, and click `⋮` on the right to perform operations such as copying, editing, and deleting.

     

1. After the workspace role is successfully created, you can go to [Workspace](../workspace/workspace.md) to authorize and set which workspaces this role can manage.

## Create Folder Role

The folder role refers to the ability to manipulate the relevant features of a module of DCE 5.0 (such as container management, microservice engine, multi-cloud orchestration, service mesh, container registry, App Workbench and global management, etc.) according to folders and subfolders. Role.

1. From the left navigation bar, click `Global Management` -> `Access Control` -> `Roles`, and click `Create Custom Role`.

     

1. Enter the name and description, select `Folder Role`, check the role permissions and click `OK`.

     

1. Return to the role list, search for the custom role you just created, and click `⋮` on the right to perform operations such as copying, editing, and deleting.

     

1. After the folder role is successfully created, you can go to [Folder](../workspace/folders.md) to authorize and set which folders this role can manage.
