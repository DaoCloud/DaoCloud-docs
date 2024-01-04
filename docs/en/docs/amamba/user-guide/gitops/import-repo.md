# import repository

This page shows how to import repositories.

## prerequisites

- Need to create a workspace and a user, the user needs to join the workspace and give __workspace edit__ role.
  Refer to [Creating a workspace](../../../ghippo/user-guide/workspace/workspace.md), [Users and roles](../../../ghippo/user-guide/access-control/user.md).
- Prepare a Git repository.

## import repository

If the code warehouse where the manifest file of the continuous deployment application is located is not public, you need to import the warehouse to Workbench in advance. Workbench currently supports two import methods: __Import repository using HTTPS__ and __Import repository using SSH__ .

### Import repository using HTTPS

1. On __Workbench__ -> __GitOps__ -> __Repository__ page, click the __Import Repository__ button and select __Use HTTPS__ .

    <!--![]()screenshots-->

2. On the __Import warehouse using HTTPS__ page, configure the relevant parameters and click __OK__ .

    <!--![]()screenshots-->

### Import repository using SSH

1. On __Workbench__ -> __GitOps__ -> __Repository__ page, click the __Import Repository__ button and select __Use SSH__ .

    <!--![]()screenshots-->

2. On the __Import warehouse using SSH__ page, configure the relevant parameters and click __OK__ .

    <!--![]()screenshots-->

## delete repository

If you no longer use a code repository, you can delete it by following the steps below.

1. Select a warehouse on the warehouse list page, click __︙__ , and click __Delete__ in the pop-up menu.

    <!--![]()screenshots-->

2. Click __OK__ in the secondary confirmation pop-up window.

    <!--![]()screenshots-->