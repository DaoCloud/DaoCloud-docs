# MinIO 的身份管理

DCE 5.0 提供的 MinIO 服务自带网页控制台（Web Console）。了解 MinIO 的身份管理（identity management）有助于快速了解如何在 MinIO 内安全有效地管理子账号。

本文简单介绍 MinIO 的身份管理规则，更多详细说明可参考 [MinIO 的官方文档](http://docs.minio.org.cn/minio/baremetal/index.html)。

## 用户

默认情况下，MinIO 使用内置的 IDentity Provider（IDP）来完成身份管理。除了 IDP，还支持第三方 [OIDC](http://docs.minio.org.cn/minio/baremetal/security/openid-external-identity-management/external-authentication-with-openid-identity-provider.html#minio-external-identity-management-openid) 和 [LDAP](http://docs.minio.org.cn/minio/baremetal/security/ad-ldap-external-identity-management/external-authentication-with-ad-ldap-identity-provider.html#minio-external-identity-management-ad-ldap) 的方式。

用户由一对 username 和 password 组成。在 MinIO 的语境中，username 又被称为 __access key__ （注意与后面 service account 层级的 access key 区分开来），password 又称为 __secret key__ 。

### root 用户

在启动 MinIO 时，可以通过环境变量的方式设置 MinIO 集群中 root 用户的账号密码，分别是以下两个变量：

- MINIO_ROOT_USER
- MINIO_ROOT_PASSWORD

root 用户拥有所有资源的所有操作权限。

> 注意：如果要变更 root 用户，需要重启 MinIO 集群中所有的节点。

### 普通用户

支持通过三种方式创建普通用户：

- Web Console，在 UI 界面中通过表单进行创建
- mc，使用 CLI 命令行创建
- Operator CR，使用 CR 进行创建

#### Console 创建

1. 在 DCE 5.0 的 MinIO 实例详情页面，点击访问地址，使用右侧的用户名和密码即可登录该实例的 Console 控制台。

    ![登录 Console](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/minio/images/insight03.png)

2. 登录 Console 控制台之后根据下图所示，创建用户。

    ![通过 Console 创建普通用户](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/minio/images/miniouser01.png)

#### mc 创建

> 需要事先[安装 __mc__  命令](https://min.io/docs/minio/linux/reference/minio-mc.html?ref=docs#install-mc)，并配置连接到 MinIO 实例

创建用户：

> __ALIAS__  指 MinIO 实例的别名

```bash
mc admin user add ALIAS ACCESSKEY SECRETKEY
```

授予权限：

> __USERNAME__  指 MinIO 用户的用户名，即 __ACCESSKEY__ 

```bash
mc admin policy set ALIAS readwrite user=USERNAME
```

#### operator CR 创建

如果是通过 cr 安装 MinIO，也可以通过 users 字段来指定普通用户的 secret：

```go
type TenantSpec struct {
    ....
    ....
    ....
    // *Optional* +
    //
    // An array of https://kubernetes.io/docs/concepts/configuration/secret/[Kubernetes opaque secrets] to use for generating MinIO users during tenant provisioning. +
    //
    // Each element in the array is an object consisting of a key-value pair __name: <string>__ , where the __<string>__  references an opaque Kubernetes secret. +
    //
    // Each referenced Kubernetes secret must include the following fields: +
    //
    // * __CONSOLE_ACCESS_KEY__  - The "Username" for the MinIO user +
    //
    // * __CONSOLE_SECRET_KEY__  - The "Password" for the MinIO user +
    //
    // The Operator creates each user with the __consoleAdmin__  policy by default. You can change the assigned policy after the Tenant starts. +
    // +optional
    Users []*corev1.LocalObjectReference __json:"users,omitempty"__ 
    ....
    ....
    ....
}
```

### 服务账号

服务账号 (Service Account) 通常使用用户登录 console 或者通过 mc 命令对 MinIO 进行管理操作。但如果应用程序需要访问 MinIO，则通常使用 Service Account（这是比较正式的叫法，某些上下文中也称之为 access key）。

一个用户可以创建多个 Service Account。

> 注意：无法通过 Service Account 登录 MinIO console，这也是它与用户最大的不同之处。

#### Console 创建

![通过 console 创建 service account](https://docs.daocloud.io/daocloud-docs-images/docs/middleware/minio/images/miniouser02.png)

#### mc 命令创建

```bash
mc [GLOBALFLAGS] admin user svcacct add     \
                            [--access-key]  \
                            [--secret-key]  \
                            [--policy]      \
                            ALIAS
                            USER
```

有关 MinIO 用户的详细说明，可参考 [User Management](http://docs.minio.org.cn/minio/baremetal/security/minio-identity-management/user-management.html)

## 用户组

用户组，顾名思义即多个用户形成的集合。通过用户组结合授权策略可以批量管理一组用户的权限。通过授权策略可以为用户组分配资源权限，该组中的用户会继承用户组的资源权限。

MinIO 用户的权限分为两部分：用户原本具有的权限 + 从所在用户组继承而来的权限。在 MinIO 语境中，用户仅具有其明确被授予或从用户组继承而来的授权。如果用户没有明确获得（被直接授予或继承）某一资源的权限，则无法访问该资源。

有关 MinIO 用户组的详细说明，可参考 [Group Management](http://docs.minio.org.cn/minio/baremetal/security/minio-identity-management/group-management.html)

## 授权策略

MinIO 使用基于策略的访问控制 (PBAC)来管理用户对哪些资源具有哪些权限。每条策略通过规定一些动作或条件来限制用户和用户组具有的权限。

### 内置策略

MinIO 内置了四种策略可以直接分配给用户或用户组。为用户/用户组授权时需要使用 __mc admin policy set__  命令，具体可参考 [mc admin policy](http://docs.minio.org.cn/minio/baremetal/reference/minio-cli/minio-mc-admin/mc-admin-policy.html#mc-admin-policy-set)

- readonly：对 MinIO 副本中的所有存储桶和存储对象具有 **只读** 权限

- readwrite：对 MinIO 副本中的所有存储桶和存储对象具有 **读写** 的权限

- diagnostics：对 MinIO 副本具有 **诊断** 权限

- writeonly：对 MinIO 副本中的所有存储桶和存储对象具有 **只写** 权限

### 策略文件示例

 MinIO 授权策略文件的模式和[亚马逊云 IAM Policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) 相同。

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


有关 MinIO 授权策略的详细说明，可参考 [Policy Management](http://docs.minio.org.cn/minio/baremetal/security/minio-identity-management/policy-based-access-control.html)