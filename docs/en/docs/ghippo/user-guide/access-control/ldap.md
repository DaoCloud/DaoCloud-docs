---
hide:
  - toc
---

# LDAP

The full name of LDAP in English is Lightweight Directory Access Protocol, that is, Lightweight Directory Access Protocol, which is an open and neutral industry-standard application protocol that provides access control and maintains directory information for distributed information through the IP protocol.

If your enterprise or organization has its own account system, and your enterprise user management system supports the LDAP protocol, you can use the identity provider feature based on the LDAP protocol provided by the global Organization members create usernames/passwords.
You can grant permissions to use DCE 5.0 resources to these external user identities.

In global management, the operation steps are as follows:

1. Log in to the web console as a user with `admin` role. Click `Global Management` in the upper left corner of the left navigation bar.

    

1. Navigate to `Access Control` under `Global Administration`, select `Create an Identity Provider`.

    

1. In the `LDAP` tab, fill in the following fields and click `Save` to establish a trust relationship with the identity provider and a user mapping relationship.

    

    | field | description | example value |
    | -------------- | ---------------------------------- -------------------------- | ----------------------- ------------ |
    | Server | Address and port number of the LDAP service | 10.6.165.2:30061 |
    | Username | Username for logging in LDAP service | cn=admin,dc=daocloud,dc=io|
    | password | password for logging in LDAP service | password |
    | Base DN | DN of the LDAP admin, used to access the LDAP server | dc=daocloud,dc=io |
    | User Object Filter | LDAP objectClass for LDAP users<br />Newly created users will be written to LDAP with all of these object classes, and as long as they contain all of these object classes, the current LDAP user record will be found. <br />DCE 5.0 has been automatically filled in for the user, if you need to modify it, you can edit it directly. | inetOrgPerson, organizationalPerson |
    | Auto Sync | Auto sync every ten minutes. After enabling, users can still be synchronized at any time through the manual synchronization button | Tick |
    | Whether to enable TLS | When enabled, the connection between DCE 5.0 and LDAP will be encrypted | No |
    | Full name mapping | Surname-sn; First name-cn | Unchangeable |
    | Mailbox Mapping | mail | Unchangeable |

1. On the `Synchronize groups` tab, fill in the following fields to configure the mapping relationship of groups, and click `Save` again.

    

    | field | description | example value |
    | ---------------- | -------------------------------- ---------------------------- | --------------------- ------ |
    | base DN | location of the group in the LDAP tree | ou=groups,dc=example,dc=org |
    | Usergroup Object Filter | Object classes for usergroups, separated by commas if more classes are required. In a typical LDAP deployment, usually "groupOfNames", the system has been filled in automatically, if you need to change it, just edit it. * means all. | * |
    | group name | cn | Unchangeable |

!!! note

    1. After you have established a trust relationship between the enterprise user management system and DCE 5.0 through the LDAP protocol, you can synchronize the users or groups in the enterprise user management system to DCE at one time through manual synchronization or automatic synchronization every ten minutes 5.0.
    1. After synchronization, the administrator can authorize groups/groups in batches, and users can log in to DCE 5.0 through the account/password in the enterprise user management system.
    1. See the [LDAP Operations Demo Video](../../../videos/ghippo.md#ldap) for a hands-on tutorial.