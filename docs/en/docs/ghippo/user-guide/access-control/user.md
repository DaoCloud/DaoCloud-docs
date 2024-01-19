# User

A user refers to a user created by the platform administrator Admin or the access control administrator IAM Owner on the __Global Management__ -> __Access Control__ -> __Users__ page, or a user connected through LDAP / OIDC .
The username represents the account, and the user logs in to the DaoCloud Enterprise platform through the username and password.

Having a user account is a prerequisite for users to access the platform. The newly created user does not have any permissions by default. For example, you need to assign corresponding role permissions to users, such as granting administrator permissions to submodules in __User List__ or __User Details__ .
The sub-module administrator has the highest authority of the sub-module, and can create, manage, and delete all resources of the module.
If a user needs to be granted permission for a specific resource, such as the permission to use a certain resource, please see [Resource Authorization Description](#authorize-for-user).

This page introduces operations such as creating, authorizing, disabling, enabling, and deleting users.

## Create user

Prerequisite: You have the platform administrator Admin permission or the access control administrator IAM Admin permission.

1. The administrator enters __Access Control__ , selects __Users__ , enters the user list, and clicks __Create User__ on the upper right.

    ![create user](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/createuser01.png)

2. Fill in the username and login password on the __Create User__ page. If you need to create
   multiple users at one time, you can click __Create User__ to create in batches, and you can
   create up to 5 users at a time. Determine whether to set the user to reset the password
   when logging in for the first time according to your actual situation.

    ![create user](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/createuser02.png)

3. Click __OK__ , the user is successfully created and returns to the user list page.

!!! note

    The username and password set here will be used to log in to the platform.

## Authorize for User

Prerequisite: The user already exists.

1. The administrator enters __Access Control__ , selects __Users__ , enters the user list, and clicks __⋮__ -> __Authorization__ .

    ![Menu](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/user-guide/images/authorize01.png)

2. On the __Authorization__ page, check the required role permissions (multiple choices are allowed).

    ![Interface](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/user-guide/images/authorize02.png)

3. Click __OK__ to complete the authorization for the user.

!!! note

    In the user list, click a user to enter the user details page.

## Add user to group

1. The administrator enters __Access Control__ , selects __Users__ , enters the user list, and clicks __⋮__ -> __Add to Group__ .

    ![Add group menu](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/user-guide/images/joingroup01.png)

2. On the __Add to Group__ page, check the groups to be joined (multiple choices are allowed). If there is no optional group, click __Create a new group__ to create a group, and then return to this page and click the __Refresh__ button to display the newly created group.

    ![Add group interface](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/user-guide/images/joingroup02.png)

3. Click __OK__ to add the user to the group.

!!! note

    The user will inherit the permissions of the group, and you can view the groups that the user has joined in __User Details__ .

## Enable/Disable user

Once a user is deactivated, that user will no longer be able to access the Platform. Unlike deleting a user, a disabled user can be enabled again as needed. It is recommended to disable the user before deleting it to ensure that no critical service is using the key created by the user.

1. The administrator enters __Access Control__ , selects __Users__ , enters the user list, and clicks a username to enter user details.

    ![User details](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/user-guide/images/createuser03.png)

2. Click __Edit__ on the upper right, turn off the status button, and make the button gray and inactive.

    ![Edit](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/user-guide/images/enableuser01.png)

3. Click __OK__ to finish disabling the user.

## Forgot password

Premise: User mailboxes need to be set. There are two ways to set user mailboxes.

- On the user details page, the administrator clicks __Edit__ , enters the user's email address in the pop-up box, and clicks __OK__ to complete the email setting.

    ![Edit](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/user-guide/images/enableuser02.png)

- Users can also enter the __Personal Center__ and set the email address on the __Security Settings__ page.

    ![User center](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/user-guide/images/mailbox.png)

If the user forgets the password when logging in, please refer to [Reset Password](../password.md).

## Delete users

!!! warning

    After deleting a user, the user will no longer be able to access platform resources in any way, please delete carefully.
    Before deleting a user, make sure your key programs no longer use keys created by that user.
    If you are unsure, it is recommended to disable the user before deleting.
    If you delete a user and then create a new user with the same name, the new user is considered a new, separate identity that does not inherit the deleted user's roles.

1. The administrator enters __Access Control__ , selects __Users__ , enters the user list, and clicks __⋮__ -> __Delete__ .

    ![Delete user](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/user-guide/images/deleteuser01.png)

2. Click __Delete__ to finish deleting the user.

    ![Confirm deletion](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/user-guide/images/deleteuser02.png)
