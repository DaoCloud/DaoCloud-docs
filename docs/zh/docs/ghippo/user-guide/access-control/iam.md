# 什么是用户与访问控制

IAM（Identity and Access Management，用户与访问控制）是全局管理的一个重要模块，您可以通过用户与访问控制模块创建、管理和销毁用户（用户组），并使用系统角色和自定义角色控制其他用户使用 DCE 平台的权限。

![IAM 定义](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/iam.png)

## 优势

- 简洁流畅

    企业内部的结构和角色可能非常复杂，项目、工作小组及授权的管理都在不断地变化。用户与访问控制采用清晰整洁的页面，打通用户、用户组、角色之间的授权关系，以最短链路实现对用户（用户组）的授权。

- 适当的角色

    用户与访问控制为每个子模块预定义了一个管理员角色，无需用户维护，您可以直接将平台预定义的系统角色授权给用户，实现平台的模块化管理（细粒度权限请参阅[权限管理](role.md)。

- 企业级访问控制

    当您希望本企业员工可以使用企业内部的认证系统登录 DCE 平台，而不需要在 DCE 平台创建对应的用户，您可以使用用户与访问控制的身份提供商功能，建立您所在企业与 DCE 的信任关系，通过联合认证使员工使用企业已有账号直接登录 DCE 平台，实现单点登录。

## 使用流程

有关访问控制的常规流程为：

```mermaid
graph TD
    login[登录] --> user[创建用户]
    user --> auth[为用户授权]
    auth --> group[创建用户组]
    group --> role[创建自定义角色]
    role --> id[创建身份提供商]

 classDef plain fill:#ddd,stroke:#fff,stroke-width:4px,color:#000;
 classDef k8s fill:#326ce5,stroke:#fff,stroke-width:4px,color:#fff;
 classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;
 
 class login,user,auth,group,role,id cluster;

click login "https://docs.daocloud.io/ghippo/install/login.html"
click user "https://docs.daocloud.io/ghippo/user-guide/access-control/user.html"
click auth "https://docs.daocloud.io/ghippo/user-guide/access-control/role.html"
click group "https://docs.daocloud.io/ghippo/user-guide/access-control/group.html"
click role "https://docs.daocloud.io/ghippo/user-guide/access-control/custom-role.html"
click id "https://docs.daocloud.io/ghippo/user-guide/access-control/idprovider.html"
```
