# import repository

This page shows how to import repositories.

## prerequisites

- Need to create a workspace and a user, the user needs to join the workspace and give `workspace edit` role.
  Refer to [Creating Workspaces](../../../ghippo/04UserGuide/02Workspace/Workspaces.md), [Users and Roles](../../../ghippo/04UserGuide/01UserandAccess/User. md).
- Prepare a Git repository.

## import repository

If the code warehouse where the manifest file of the continuous deployment application is located is not public, you need to import the warehouse to the application workbench in advance. Application Workbench currently supports two import methods: `Import repository using HTTPS` and `Import repository using SSH`.

### Import repository using HTTPS

1. On `Application Workbench` -> `GitOps` -> `Repository` page, click the `Import Repository` button and select `Use HTTPS`.

    ![import](../../images/import01.png)

2. On the `Import warehouse using HTTPS` page, configure the relevant parameters and click `OK`.

    ![import](../../images/import02.png)

### Import repository using SSH

1. On `Application Workbench` -> `GitOps` -> `Repository` page, click the `Import Repository` button and select `Use SSH`.

    ![import](../../images/import01.png)

2. On the `Import warehouse using SSH` page, configure the relevant parameters and click `OK`.

    ![import](../../images/import03.png)

## delete repository

If you no longer use a code repository, you can delete it by following the steps below.

1. Select a warehouse on the warehouse list page, click `︙`, and click `Delete` in the pop-up menu.

    ![Delete](../../images/import04.png)

2. Click `OK` in the secondary confirmation pop-up window.

    ![Delete Confirmation](../../images/import05.png)