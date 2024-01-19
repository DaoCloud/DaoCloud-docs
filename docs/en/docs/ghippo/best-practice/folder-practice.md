---
hide:
  - toc
---

# Folder Best Practices

A folder represents an organizational unit (such as a department) and is a node in the resource hierarchy.

A folder can contain workspaces, subfolders, or a combination of both.
It provides identity management, multi-level and permission mapping capabilities, and can map the role of a user/group in a folder to its subfolders, workspaces and resources.
Therefore, with the help of folders, enterprise managers can centrally manage and control all resources.

1. Build corporate hierarchy

    First of all, according to the existing enterprise hierarchy structure, build the same folder hierarchy as the enterprise.
    DCE supports 5-level folders, which can be freely combined according to the actual situation of the enterprise, and folders and workspaces are mapped to entities such as departments, projects, and suppliers in the enterprise.

    Folders are not directly linked to resources, but indirectly achieve resource grouping through workspaces.

    

2. User identity management

    Folder provides three roles: Folder Admin, Folder Editor, and Folder Viewer.
    [View role permissions](../user-guide/access-control/role.md), you can grant different roles to users/groups in the same folder through [Authorization](../user-guide/access-control/role.md).

3. Role and permission mapping

    Enterprise Administrator: Grant the Folder Admin role on the root folder. He will have administrative authority over all departments, projects and their resources.

    Department manager: grant separate management rights to each subfolder and workspace.

    Project members: Grant management rights separately at the workspace and resource levels.