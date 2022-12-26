# What is user and access control

IAM (Identity and Access Management, user and access control) is an important module of global management. You can create, manage and destroy users (user groups) through the user and access control module, and use system roles and custom roles to control other users Access to the DCE Platform.

![IAM definition](../../images/iam.png)

## Advantage

- Simple and smooth

    Structures and roles within an enterprise can be complex, with the management of projects, work groups, and mandates constantly changing. User and access control uses a clear and tidy page to open up the authorization relationship between users, user groups, and roles, and realize the authorization of users (user groups) with the shortest link.

- Appropriate role

    User and access control pre-defines an administrator role for each sub-module, without user maintenance, you can directly authorize the predefined system roles of the platform to users to realize the modular management of the platform (for fine-grained permissions, please refer to [Privilege Management](../01UserandAccess/Role.md).

- Enterprise-grade access control

    When you want your company's employees to use the company's internal authentication system to log in to the DCE platform without creating corresponding users on the DCE platform, you can use the identity provider function of user and access control to establish a trust relationship between your company and DCE , Through joint authentication, employees can directly log in to the DCE platform with the existing account of the enterprise, realizing single sign-on.

## manual

1. Use the DCE platform main account (Super Admin) or a user account with administrator privileges to log in to the DCE platform.
2. Create a user, see [User](User.md).
3. Authorize users, see [Rights Management](Role.md).
4. Create a user group, see [User Group](Group.md).
5. Create a custom role, see [Custom Role](Role.md).
6. Create an identity provider, see [Identity Provider](idprovider.md).