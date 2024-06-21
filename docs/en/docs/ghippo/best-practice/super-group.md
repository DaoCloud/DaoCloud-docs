---
hide:
  - toc
---

# Architecture Management of Large Enterprises

With the continuous expansion of business, the company's scale continues to grow, subsidiaries and branches are established one after another, and some subsidiaries even further establish subsidiaries. The original large departments are gradually subdivided into multiple smaller departments, leading to an increasing number of hierarchical levels in the organizational structure. This organizational structure change also affects the IT governance architecture.

The specific operational steps are as follows:

1. Enable Isolation Mode between Folder/WS

    Please refer to [Enable Isolation Mode between Folder/WS](../install/user-isolation.md).

2. Plan Enterprise Architecture according to the Actual Situation

    Under a multi-level organizational structure, it is recommended to use the second-level folder as an isolation unit to isolate users/user groups/resources between "sub-companies". After isolation, users/user groups/resources between "sub-companies" are not visible to each other.


3. Create Users/Integrate User Systems

    The main platform administrator Admin can [create users](../user-guide/access-control/user.md) on the platform or integrate users through LDAP/OIDC/OAuth2.0 and other [identity providers](../user-guide/access-control/ldap.md) to DCE 5.0.

4. Create Folder Roles

    In the isolation mode of Folder/WS, the platform administrator Admin needs to first **authorize** users to invite them to various sub-companies, so that the "sub-company administrators (Folder Admin)" can manage these users, such as secondary authorization or editing permissions. It is recommended to simplify the management work of the platform administrator Admin by creating a role without actual permissions to assist the platform administrator Admin in inviting users to sub-companies through "authorization". The actual permissions of sub-company users are delegated to the sub-company administrators (Folder Admin) to manage independently. (The following demonstrates how to create a resource-bound **role without actual permissions**, i.e., minirole)

    !!! note

        Resource-bound permissions used alone do not take effect, hence meeting the requirement of inviting users to sub-companies through "authorization" and then managed by sub-company administrators Folder Admin.


5. Authorize Users

    The platform administrator invites users to various sub-companies according to the actual situation and appoints sub-company administrators.

    ![folerauth](../images/9.png)

    Authorize sub-company regular users as "minirole" (1), and authorize sub-company administrators as Folder Admin.
    { .annotate }

    1. Refers to the **role without actual permissions** created in step 4


6. Sub-company Administrators Manage Users/User Groups Independently

    Sub-company administrator Folder Admin can only see their own "Sub-company 2" after logging into the platform, and can adjust the architecture by creating folders, creating workspaces, and assigning other permissions to users in Sub-company 2 through adding authorization/edit permissions.


    When adding authorization, sub-company administrator Folder Admin can only see users invited by the platform administrator through "authorization", and cannot see all users on the platform, thus achieving user isolation between Folder/WS, and the same applies to user groups (the platform administrator can see and authorize all users and user groups on the platform).


!!! note

    The main difference between large enterprises and small/medium-sized enterprises lies in whether users/user groups in Folder and workspaces are visible to each other. In large enterprises, users/user groups between subsidiaries are not visible + permission isolation; in small/medium-sized enterprises, users between departments are visible to each other + permission isolation.
