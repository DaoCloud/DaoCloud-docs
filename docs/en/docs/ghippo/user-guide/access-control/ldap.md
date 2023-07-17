---
hide:
  - toc
---

# LDAP

The full name of LDAP in English is Lightweight Directory Access Protocol, that is, Lightweight Directory Access Protocol, which is an open and neutral industry-standard application protocol that provides access control and maintains directory information for distributed information through the IP protocol.

If your enterprise or organization has its own account system, and your enterprise user management system supports the LDAP protocol, you can use the identity provider feature based on the LDAP protocol provided by the global Organization members create usernames/passwords.
You can grant permissions to use DCE 5.0 resources to these external user identities.

In global management, the operation steps are as follows:

1. Log in to DCE 5.0 as a user with `admin` role. Click `Global Management` -> `Access Control` in the lower left corner of the left navigation bar.

    ![access control](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/ws01.png)

1. Click `Identity Provider` on the left nav bar, click `Create an Identity Provider` button.

    ![id provider](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/ldap00.png)

1. In the `LDAP` tab, fill in the following fields and click `Save` to establish a trust relationship with the identity provider and a user mapping relationship.

    ![ldap](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/ghippo/images/ldap01.png)

    | Field         | Description                                                  | Example                             |
    | ------------- | ------------------------------------------------------------ | ----------------------------------- |
    | Type          | Supports LDAP (Lightweight Directory Access Protocol) and AD (Active Directory) | LDAP                                |
    | Server        | The address and port number of the LDAP service              | 10.6.165.2:30061                    |
    | User Name     | The username used to log in                                   | cn=admin,dn=daocloud,dc=com          |
    | Password      | The password used to log in                                   | password                            |
    | Base DN       | The DN of the admin used to access the LDAP server            | dc=daocloud,dc=io                   |
    | User Filter   | LDAP objectClass for LDAP users.<br />New users will be written to LDAP with all of these object classes and will find existing LDAP user records as long as they contain all of these object classes. <br/>Automatically filled by DCE 5.0, can be edited directly if needed. | inetOrgPerson, organizationalPerson |
    | Enable TLS    | Enabling it will encrypt the connection between DCE 5.0 and LDAP | No                                  |
    | Full Name Map | Surname-sn; First name-cn                                     | Not editable                        |
    | Email Mapping | Refers to associating a user's email address with their LDAP account. It allows only users with specific email domain names to access resources such as intranet websites or file shares. | Email address, not editable          |

    **Advanced Configuration**

    | Field           | Description                                                  | Example |
    | --------------- | ------------------------------------------------------------ | ------- |
    | Automatic Sync  | Automatically synced once per hour by default, can be configured manually | Checked |
    | Data Sync Mode  | For read-only LDAP data, user information cannot be edited on the DCE 5.0 platform<br />For data written to LDAP, user information can be edited on DCE 5.0 and then synced back to LDAP | Read-only |
    | Read Timeout    | When the LDAP data is large, adjusting this value can effectively avoid interface timeouts | 600 ms  |
    | Username Attr   | Refers to the attribute used to identify users during authentication and authorization. The username attribute is unique and cannot be changed. It can be the user's email address, login name, or other property defined by the system administrator. The username attribute is used as a unique identifier for the user so that the system can identify specific users and grant them appropriate permissions. | uid     |
    | RDN Attribute   | Refers to the attribute used to create the Relative Distinguished Name (RDN). In X.500 and LDAP directory services, the RDN attribute is usually unique and is used to identify part of an object in the directory tree (Naming Context). For example, in "cn=John Doe,ou=People,dc=example,dc=com", "cn" is one of the RDN attributes. The RDN attribute defines the relative name of the object under its parent object, so it must be unique. When a new object is added to the directory, its RDN attribute must be different from other objects in the same level, otherwise it will cause naming conflicts. | uid     |
    | UUID Attribute  | Refers to the Universally Unique Identifier (UUID) attribute. A UUID is a 36-character string consisting of numbers, letters, and hyphens, used to identify objects in a computer system. UUID ensures that objects on different computers have unique identifiers at any given time. | entryUUID |

1. On the `Synchronize groups` tab, fill in the following fields to configure the mapping relationship of groups, and click `Save` again.

    | Field | Description | Example |
    | ---------------- | -------------------------------- ---------------------------- | --------------------- ------ |
    | base DN | location of the group in the LDAP tree | ou=groups,dc=example,dc=org |
    | Usergroup Object Filter | Object classes for usergroups, separated by commas if more classes are required. In a typical LDAP deployment, usually "groupOfNames", the system has been filled in automatically, if you need to change it, just edit it. * means all. | * |
    | group name | cn | Unchangeable |

!!! note

    1. After you have established a trust relationship between the enterprise user management system and DCE 5.0 through the LDAP protocol, you can synchronize the users or groups in the enterprise user management system to DCE 5.0 at one time through auto/manual synchronization.
    1. After synchronization, the administrator can authorize groups/groups in batches, and users can log in to DCE 5.0 through the account/password in the enterprise user management system.
    1. See the [LDAP Operations Demo Video](../../../videos/ghippo.md#ldap) for a hands-on tutorial.
