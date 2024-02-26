# Identity management for MinIO

The MinIO service provided by DCE 5.0 comes with a web console (Web Console). Understanding MinIO's identity management (identity management) helps to quickly understand how to manage sub-accounts safely and effectively within MinIO.

This article briefly introduces MinIO's identity management rules. For more details, please refer to [MinIO's official documentation](http://docs.minio.org.cn/minio/baremetal/index.html).

## Users

By default, MinIO uses the built-in IDentity Provider (IDP) for identity management. In addition to IDP, it also supports third-party [OIDC] (http://docs.minio.org.cn/minio/baremetal/security/openid-external-identity-management/external-authentication-with-openid-identity-provider.html #minio-external-identity-management-openid) and [LDAP](http://docs.minio.org.cn/minio/baremetal/security/ad-ldap-external-identity-management/external-authentication-with- ad-ldap-identity-provider.html#minio-external-identity-management-ad-ldap ).

A user consists of a username and password pair. In the context of MinIO, username is also called __access key__ (note that it is distinguished from the access key at the service account level later), and password is also called __secret key__ .

### root user

When starting MinIO, you can set the account password of the root user in the MinIO cluster through environment variables, which are the following two variables:

- MINIO_ROOT_USER
- MINIO_ROOT_PASSWORD

The root user has all operation permissions on all resources.

> Note: If you want to change the root user, you need to restart all nodes in the MinIO cluster.

### Normal users

There are three ways to create normal users:

- Web Console, created through the form in the UI interface
- mc, created using the CLI command line
- Operator CR, use CR for creation

#### Console Creation

1. On the MinIO instance details page of DCE 5.0, click the access address, and use the username and password on the right to log in to the console of the instance.

    <!--screenshot-->

2. After logging in to the Console console, create a user according to the figure below.

    <!--screenshot-->

#### mc create

> Need to [install the __mc__ command](https://min.io/docs/minio/linux/reference/minio-mc.html?ref=docs#install-mc) in advance and configure the connection to the MinIO instance

Create user:

> __ALIAS__ refers to the alias name of the MinIO instance

```bash
mc admin user add ALIAS ACCESSKEY SECRETKEY
```

Granted permission:

> __USERNAME__ refers to the username of the MinIO user, which is __ACCESSKEY__ 

```bash
mc admin policy set ALIAS readwrite user=USERNAME
```

#### Create operator CR

If you install MinIO through cr, you can also specify the secret of a common user through the users field:

```go
type TenantSpec struct {
    ....
    ....
    ....
    // *Optional* +
    //
    // An array of https://kubernetes.io/docs/concepts/configuration/secret/[Kubernetes opaque secrets] to use for generating MinIO users during tenant provisioning. +
    //
    // Each element in the array is an object consisting of a key-value pair __name: <string>__ , where the __<string>__ references an opaque Kubernetes secret. +
    //
    // Each referenced Kubernetes secret must include the following fields: +
    //
    // * __CONSOLE_ACCESS_KEY__ - The "Username" for the MinIO user +
    //
    // * __CONSOLE_SECRET_KEY__ - The "Password" for the MinIO user +
    //
    // The Operator creates each user with the __consoleAdmin__ policy by default. You can change the assigned policy after the Tenant starts. +
    // +optional
    Users []*corev1.LocalObjectReference __json:"users,omitempty"__ 
    ....
    ....
    ....
}
```

### Service account

The service account (Service Account) usually uses the user to log in to the console or manage MinIO through the mc command. But if the application needs to access MinIO, it usually uses a Service Account (this is a more formal name, and it is also called an access key in some contexts).

A user can create multiple Service Accounts.

> Note: MinIO console cannot be logged in through Service Account, which is the biggest difference between it and users.

#### Console Creation

<!--screenshot-->

#### mc command creation

```bash
mc [GLOBALFLAGS] admin user svcacct add \
                            [--access-key]\
                            [--secret-key]\
                            [--policy]\
                            ALIAS
                            USER
```

For details about MinIO users, please refer to [User Management](http://docs.minio.org.cn/minio/baremetal/security/minio-identity-management/user-management.html)

## group

A group, as the name implies, is a collection of multiple users. By combining groups with authorization policies, the permissions of a group of users can be managed in batches. Authorization policies can be used to assign resource permissions to groups, and users in this group will inherit the resource permissions of the group.

The permissions of MinIO users are divided into two parts: the original permissions of the user + the permissions inherited from the group. In the context of MinIO, users only have the authorizations they are explicitly granted or inherited from usergroups. If a user has not been explicitly granted (either directly granted or inherited) permissions to a resource, they cannot access that resource.

For details about MinIO groups, please refer to [Group Management](http://docs.minio.org.cn/minio/baremetal/security/minio-identity-management/group-management.html)

## Authorization Policy

MinIO uses policy-based access control (PBAC) to manage which permissions users have on which resources. Each policy limits the permissions that users and groups have by specifying some actions or conditions.

### Built-in Strategies

MinIO has four built-in policies that can be directly assigned to users or groups. When authorizing users/groups, you need to use the __mc admin policy set__ command. For details, please refer to [mc admin policy](http://docs.minio.org.cn/minio/baremetal/reference/minio-cli/minio- mc-admin/mc-admin-policy.html#mc-admin-policy-set)

- readonly: **read-only** permission to all buckets and storage objects in the MinIO replica

- readwrite: **Read and write** permissions on all buckets and storage objects in the MinIO replica

- diagnostics: **Diagnostics** permissions on the MinIO copy

- writeonly: have **write-only** permissions to all buckets and storage objects in MinIO replicas

### Policy file example

 The mode of the MinIO authorization policy file is the same as [Amazon Cloud IAM Policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html).

```
{
   "Version" : "2012-10-17",
   "Statement" : [
      {
         "Effect" : "Allow",
         "Action" : [ "s3:<ActionName>", ... ],
         "Resource" : "arn:aws:s3:::*",
         "Condition" : { ... }
      },
      {
         "Effect" : "Deny",
         "Action" : [ "s3:<ActionName>", ... ],
         "Resource" : "arn:aws:s3:::*",
         "Condition" : { ... }
      }
   ]
}
```


For a detailed description of the MinIO authorization policy, please refer to [Policy Management](http://docs.minio.org.cn/minio/baremetal/security/minio-identity-management/policy-based-access-control.html)