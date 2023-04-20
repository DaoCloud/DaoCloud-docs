# import repository

This page shows how to import repositories.

## Prerequisites

- Need to create a workspace and a user, the user needs to join the workspace and give `workspace edit` role.
  Refer to [Creating Workspaces](../../../ghippo/user-guide/02Workspace/Workspaces.md), [Users and Roles](../../../ghippo/04UserGuide/01UserandAccess/User. md).
- Prepare a Git repository.

## Import repository

If the codebase where the manifest file of the continuous deployment application is located is not public, you need to import the registry to the application workbench in advance. Application Workbench currently supports two import methods: `Import repository using HTTPS` and `Import repository using SSH`.

### Import repository using HTTPS

1. On `Application Workbench` -> `GitOps` -> `Repository` page, click the `Import Repository` button and select `Use HTTPS`.

    

2. On the `Import registry using HTTPS` page, configure the relevant parameters and click `OK`.

    

### Import repository using SSH

1. On `Application Workbench` -> `GitOps` -> `Repository` page, click the `Import Repository` button and select `Use SSH`.

    

2. On the `Import registry using SSH` page, configure the relevant parameters and click `OK`.

    

## Delete repository

If you no longer use a code repository, you can delete it by following the steps below.

1. Select a registry on the registry list page, click `︙`, and click `Delete` in the pop-up menu.

    

2. Click `OK` in the secondary confirmation pop-up window.

    