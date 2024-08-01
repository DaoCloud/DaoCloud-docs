---
hide:
  - toc
---

# Creating/Deleting Workspaces

A workspace is a resource category that represents a hierarchical relationship of resources.
A workspace can contain resources such as clusters, namespaces, and registries. Typically,
each workspace corresponds to a project and different resources can be allocated, and
different users and user groups can be assigned to each workspace.

Follow the steps below to create a workspace:

1. Log in to DCE 5.0 with a user account having the admin/folder admin role.
   Click __Global Management__ -> __Workspace and Folder__ at the bottom of the left navigation bar.

    ![Global Management](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/ws01.png)

3. Click the __Create Workspace__ button in the top right corner.

    ![Create Workspace](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/ws02.png)

4. Fill in the workspace name, folder assignment, and other information, then click __OK__ to complete creating the workspace.

    ![Confirm](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/ws03.png)

!!! tip

    After successful creation, the workspace name will be displayed in the left tree structure, represented by different icons for folders and workspaces.

    ![Folders and Workspaces](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/ws04.png)

!!! note

    To edit or delete a specific workspace or folder, select it and click __...__ on the right side.

    - If resource groups and shared resources have resources under the workspace, the workspace cannot be deleted. All resources need to be unbound before deletion of the workspace.

    - If Microservices Engine has Integrated Registry under the workspace, the workspace cannot be deleted. Integrated Registry needs to be removed before deletion of the workspace.

    - If Container Registry has Registry Space or Integrated Registry under the workspace, the workspace cannot be deleted. Registry Space needs to be removed, and Integrated Registry needs to be deleted before deletion of the workspace.
