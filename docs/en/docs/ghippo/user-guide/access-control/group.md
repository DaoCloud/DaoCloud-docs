# Group

A group is a collection of users. By joining a group, a user can inherit the role permissions of the group. Authorize users in batches through groups to better manage users and their permissions.

## Use cases

When a user's permission changes, it only needs to be moved to the corresponding group without affecting other users.

When the permissions of a group change, you only need to modify the role permissions of the group to apply to all users in the group.

## Create group

Prerequisite: Super Admin or IAM Admin.

1. Enters `Access Control`, selects `Groups`, enters the list of groups, and clicks `Create a group` on the upper right.

    ![group button](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/group00.png)

2. Fill in the group information on the `Create group` page.

    ![fill](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/group01.png)

3. Click `OK`, the group is created successfully, and you will return to the group list page. The first line in the list is the newly created group.

## Add permissions to a group

Prerequisite: The group already exists.

1. Enters `Access Control`, selects `Groups`, enters the list of groups, and clicks `⋮` -> `Add permissions`.

    ![add permissions](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/group02.png)

2. On the `Add permissions` page, check the required role permissions (multiple choices are allowed).

    ![button](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/group03.png)

3. Click `OK` to add permissions to the group. Automatically return to the group list, click a group to view the permissions granted to the group.

    ![view](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/group04.png)

## Add users to a group

1. Enters `Access Control`, selects `Groups` to display the group list, and on the right side of a group, click `⋮` -> `Add Members`.

    ![members](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/group05.png)

2. On the `Add Group Members` page, click the user to be added (multiple choices are allowed). If there is no user available, click `Create a new user`, first go to create a user, and then return to this page and click the refresh icon to display the newly created user.

    ![new user](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/group06.png)

3. Click `OK` to finish adding users to the group.

!!! note

    Users in the group will inherit the permissions of the group; users who join the group can be viewed in the group details.

## Delete group

Note: Deleting a group will not delete the users in the group, but the users in the group will no longer be able to inherit the permissions of the group

1. The administrator enters `Access Control`, selects `group` to enter the group list, and on the right side of a group, click `⋮` -> `Delete`.

    ![delete](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/deletegroup01.png)

2. Click `Delete` to delete the group.

    ![confirm](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/deletegroup02.png)

3. Return to the group list, and the screen will prompt that the deletion is successful.

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/deletegroup03.png)

!!! note

    Deleting a group will not delete the users in the group, but the users in the group will no longer be able to inherit the permissions from the group.
