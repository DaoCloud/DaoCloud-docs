# Group

A group is a collection of users. By joining a group, a user can inherit the role permissions of the group. Authorize users in batches through groups to better manage users and their permissions.

## Use cases

When a user's permission changes, it only needs to be moved to the corresponding group without affecting other users.

When the permissions of a group change, you only need to modify the role permissions of the group to apply to all users in the group.

## Create group

Prerequisite: Admin or IAM Owner.

1. Enters __Access Control__ , selects __Groups__ , enters the list of groups, and clicks __Create a group__ on the upper right.

    ![group button](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/group00.png)

2. Fill in the group information on the __Create group__ page.

    ![fill](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/group01.png)

3. Click __OK__ , the group is created successfully, and you will return to the group list page. The first line in the list is the newly created group.

## Add permissions to a group

Prerequisite: The group already exists.

1. Enters __Access Control__ , selects __Groups__ , enters the list of groups, and clicks __┇__ -> __Add permissions__ .

    ![add permissions](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/group02.png)

2. On the __Add permissions__ page, check the required role permissions (multiple choices are allowed).

    ![button](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/group03.png)

3. Click __OK__ to add permissions to the group. Automatically return to the group list, click a group to view the permissions granted to the group.

    ![view](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/group04.png)

## Add users to a group

1. Enters __Access Control__ , selects __Groups__ to display the group list, and on the right side of a group, click __┇__ -> __Add Members__ .

    ![members](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/group05.png)

2. On the __Add Group Members__ page, click the user to be added (multiple choices are allowed). If there is no user available, click __Create a new user__ , first go to create a user, and then return to this page and click the refresh icon to display the newly created user.

    ![new user](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/group06.png)

3. Click __OK__ to finish adding users to the group.

!!! note

    Users in the group will inherit the permissions of the group; users who join the group can be viewed in the group details.

## Delete group

Note: Deleting a group will not delete the users in the group, but the users in the group will no longer be able to inherit the permissions of the group

1. The administrator enters __Access Control__ , selects __group__ to enter the group list, and on the right side of a group, click __┇__ -> __Delete__ .

    ![delete](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/deletegroup01.png)

2. Click __Delete__ to delete the group.

    ![confirm](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/deletegroup02.png)

3. Return to the group list, and the screen will prompt that the deletion is successful.

    ![success](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/deletegroup03.png)

!!! note

    Deleting a group will not delete the users in the group, but the users in the group will no longer be able to inherit the permissions from the group.
