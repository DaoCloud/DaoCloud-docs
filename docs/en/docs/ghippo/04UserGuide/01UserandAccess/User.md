# user

A user refers to a user created by the platform administrator Admin or the user and access control administrator IAM Admin on the `Global Management` -> `Users and Access Control` -> `Users` page, or a user connected through LDAP / OIDC .
The user name represents the account, and the user logs in to the DaoCloud Enterprise platform through the user name and password.

Having a user account is a prerequisite for users to access the platform. The newly created user does not have any permissions by default. For example, you need to assign corresponding role permissions to users, such as granting administrator permissions to submodules in `User List` or `User Details`.
The sub-module administrator has the highest authority of the sub-module, and can create, manage, and delete all resources of the module.
If a user needs to be granted permission for a specific resource, such as the permission to use a certain resource, please see [Resource Authorization Description] (#Authorize for User).

This page introduces operations such as creating, authorizing, disabling, enabling, and deleting users.

## Create user

Prerequisite: You have the platform administrator Admin permission or the user and access control administrator IAM Admin permission.

1. The administrator enters `Users and Access Control`, selects `Users`, enters the user list, and clicks `Create User` on the upper right.

    ![Create User Button](../../images/createuser01.png)

2. Fill in the user name and login password on the `Create User` page. If you need to create multiple users at one time, you can click `Create User` to create in batches, and you can create up to 5 users at a time. Determine whether to set the user to reset the password when logging in for the first time according to your actual situation.

    ![Set username and password](../../images/createuser02.png)

3. Click `OK`, the user is successfully created and returns to the user list page.

!!! note

    The username and password set here will be used to log in to the platform.

## Grant submodule administrator privileges to the user

Prerequisite: The user already exists.

1. The administrator enters `Users and Access Control`, selects `Users`, enters the user list, and clicks `...` -> `Authorization`.

    ![Authorize Menu](../../images/authorize01.png)

2. On the `Authorization` page, check the required role permissions (multiple choices are allowed).

    ![Authorize interface](../../images/authorize02.png)

3. Click `OK` to complete the authorization for the user.

!!! note

    In the user list, click a user to enter the user details page.

## Add user to user group

1. The administrator enters `Users and Access Control`, selects `Users`, enters the user list, and clicks `...` -> `Add User Group`.

    ![Join Group Menu](../../images/joingroup01.png)

2. On the `Join User Group` page, check the user groups to be joined (multiple choices are allowed). If there is no optional user group, click `Create User Group` to create a user group, and then return to this page and click the `Refresh` button to display the newly created user group.

    ![Join group interface](../../images/joingroup02.png)

3. Click `OK` to add the user to the user group.

!!! note

    The user will inherit the permissions of the user group, and you can view the user groups that the user has joined in `User Details`.

## enable/disable user

Once a user is deactivated, that user will no longer be able to access the Platform. Unlike deleting a user, a disabled user can be enabled again as needed. It is recommended to disable the user before deleting it to ensure that no critical service is using the key created by the user.

1. The administrator enters `Users and Access Control`, selects `Users`, enters the user list, and clicks a user name to enter user details.

    ![User Details](../../images/createuser03.png)

2. Click `Edit` on the upper right, turn off the status button, and make the button gray and inactive.

    ![edit](../../images/enableuser.png)

3. Click `OK` to finish disabling the user.

## Forgot password

Premise: User mailboxes need to be set. There are two ways to set user mailboxes.

- On the user details page, the administrator clicks `Edit`, enters the user's email address in the pop-up box, and clicks `OK` to complete the email setting.

    ![edit](../../images/enableuser.png)

- Users can also enter the `Personal Center` and set the email address on the `Security Settings` page.

    ![Personal Center](../../images/mailbox.png)

If the user forgets the password when logging in, please refer to [Reset Password](../password.md).

## Delete users

!!! warning

    After deleting a user, the user will no longer be able to access platform resources in any way, please delete carefully.
    Before deleting a user, make sure your key programs no longer use keys created by that user.
    If you are unsure, it is recommended to disable the user before deleting.
    If you delete a user and then create a new user with the same name, the new user is considered a new, separate identity that does not inherit the deleted user's roles.

1. The administrator enters `Users and Access Control`, selects `Users`, enters the user list, and clicks `...` -> `Delete`.

    ![Delete User Menu](../../images/deleteuser01.png)

2. Click `Remove` to finish deleting the user.

    ![Delete user confirmation](../../images/deleteuser02.png)