# import repository

This page shows how to import repositories.

## prerequisites

- Need to create a workspace and a user, the user needs to join the workspace and give `workspace edit` role.
  Refer to [Creating a workspace](../../../ghippo/user-guide/workspace/workspace.md), [Users and roles](../../../ghippo/user-guide/access-control/user.md).
- Prepare a Git repository.

## import repository

If the code warehouse where the manifest file of the continuous deployment application is located is not public, you need to import the warehouse to the application workbench in advance. App Workbench currently supports two import methods: `Import repository using HTTPS` and `Import repository using SSH`.

### Import repository using HTTPS

1. On `App Workbench` -> `GitOps` -> `Repository` page, click the `Import Repository` button and select `Use HTTPS`.

    <!--![]()screenshots-->

2. On the `Import warehouse using HTTPS` page, configure the relevant parameters and click `OK`.

    <!--![]()screenshots-->

### Import repository using SSH

1. On `App Workbench` -> `GitOps` -> `Repository` page, click the `Import Repository` button and select `Use SSH`.

    <!--![]()screenshots-->

2. On the `Import warehouse using SSH` page, configure the relevant parameters and click `OK`.

    <!--![]()screenshots-->

## delete repository

If you no longer use a code repository, you can delete it by following the steps below.

1. Select a warehouse on the warehouse list page, click `︙`, and click `Delete` in the pop-up menu.

    <!--![]()screenshots-->

2. Click `OK` in the secondary confirmation pop-up window.

    <!--![]()screenshots-->