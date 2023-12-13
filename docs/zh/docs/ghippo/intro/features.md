---
hide:
  - toc
---

# 功能总览

本页说明全局管理的各项功能特性。

1. 用户管理

    拥有用户帐号，是用户访问 DCE 平台的前提。
    [用户](../user-guide/access-control/user.md)由平台管理员 Admin 或者用户与访问控制管理员 IAM Owner 在`全局管理` -> `用户与访问控制` -> `用户`页面创建，或者通过 LDAP 对接而来。
    每位用户拥有独立的用户名和密码，通过给单个或者一组用户授予不同的权限，让不同的用户拥有不同资源的访问权限。

    ```mermaid
    graph LR

        admin([平台管理员或<br>用户与访问控制管理员]) --> |创建并管理用户|user[用户]
        user --> user1[用户 A]
        user --> user2[用户 B]
        user --> user3[用户 C]
        
    click user "https://docs.daocloud.io/ghippo/user-guide/access-control/user/"

    classDef plain fill:#ddd,stroke:#fff,stroke-width:0px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:0px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class admin plain;
    class user1,user2,user3 k8s;
    class user cluster
    ```

2. 用户组管理

    [用户组](../user-guide/access-control/group.md)是多个用户的集合。
    用户可以通过加入用户组，实现继承用户组的角色权限。通过用户组批量地给用户进行授权，可以更好地管理用户及其权限。

    ```mermaid
    graph LR

        admin([平台管理员或<br>用户与访问控制管理员])
        admin --> user[创建用户]
        admin --> group[创建用户组]
        admin --> add[将用户加入用户组]
        
    click user "https://docs.daocloud.io/ghippo/user-guide/access-control/user/"
    click group "https://docs.daocloud.io/ghippo/user-guide/access-control/group/"
    click add "https://docs.daocloud.io/ghippo/user-guide/access-control/group/#_5"

    classDef plain fill:#ddd,stroke:#fff,stroke-width:0px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:0px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class admin plain;
    class user,group,add cluster
    ```

3. 角色管理

    一个[角色](../user-guide/access-control/role.md)对应一组权限。
    权限决定了可以对资源执行的操作。向用户授予某个角色，即授予该角色所包含的所有权限。
    您可以将不同模块的管理权限划分给不同的用户，
    比如用户 A 管理[容器管理模块](../../kpanda/intro/index.md)，用户 B 管理[应用工作台模块](../../amamba/intro/index.md)，共同管理[可观测性模块](../../insight/intro/index.md)。

    ![角色](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/role.png)

4. 工作空间

    [工作空间](../user-guide/workspace/workspace.md)用于管理资源，包含层级和工作空间两部分。

    层级是资源层次结构中的节点，一个层级可以包含工作空间、其他层级或两者的组合。
    可以将层级理解为有层次结构的部门、环境、供应商等多种概念。

    工作空间可以理解为部门下的项目，管理员通过层级和工作空间映射企业中的层级关系。

    虽然一个层级可以包含多个层级或工作空间，但是给定的层级或者工作空间只能有一个父级。

    ![工作空间](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/workspace.png)

5. 审计日志

    [审计日志](../user-guide/audit/audit-log.md)完整地记录用户的各项操作行为，
    包括用户通过页面或 API 接口发起的操作以及各服务内部自触发的操作。
    支持通过事件来源、资源类型、操作状态等多个维度进行组合查询，支持审计日志导出。

6. 平台设置

    [平台设置](../user-guide/platform-setting/about.md)包括账号安全设置、
    [外观定制](../user-guide/platform-setting/appearance.md)、
    [邮件服务器](../user-guide/platform-setting/mail-server.md)等。
    当需要对账号的安全信息、平台 logo、许可证授权、邮件服务器等平台级设置进行管理时，
    可以通过`平台设置`进行操作，平台设置仅平台管理员具有管理权限。

    ```mermaid
    graph LR

        admin([平台管理员]) --> |管理|about[平台设置]
        about --> password[用户密码等安全策略]
        about --> appear[平台外观定制]
        about --> mail[邮件服务器]
        about --> license[正版授权]
        
    click about "https://docs.daocloud.io/ghippo/user-guide/platform-setting/about/"
    click password "https://docs.daocloud.io/ghippo/user-guide/password/"
    click appear "https://docs.daocloud.io/ghippo/user-guide/platform-setting/appearance/"
    click mail "https://docs.daocloud.io/ghippo/user-guide/platform-setting/mail-server/"
    click license "https://docs.daocloud.io/dce/license0/"

    classDef plain fill:#ddd,stroke:#fff,stroke-width:0px,color:#000;
    classDef k8s fill:#326ce5,stroke:#fff,stroke-width:0px,color:#fff;
    classDef cluster fill:#fff,stroke:#bbb,stroke-width:2px,color:#326ce5;
    class admin plain;
    class about,password,appear,mail,license cluster
    ```

## 功能清单

具体的功能清单如下所述。

1. 用户与访问控制
    1. [用户](../user-guide/access-control/user.md)
        - 列表展示用户名、描述、创建时间、最近一次登录时间
        - 列表支持通过用户名搜索用户
        - 列表支持给用户快捷授权
        - 列表支持将用户快捷加入用户组
        - 列表支持批量删除用户
        - 列表支持创建用户
        - 详情支持编辑用户基本信息，包括邮箱、描述、启用 / 禁用等
        - 详情支持记录用户授权信息，支持添加 / 移除权限
        - 详情支持记录用户加入用户组信息，支持用户加入新的用户组，支持将用户从老的用户组移除
        - 支持管理员帮助用户修改密码
        - 支持管理员帮助用户创建访问密钥
    2. [用户组](../user-guide/access-control/group.md)
        - 列表展示用户组名、组内用户数、描述、创建时间
        - 列表支持通过用户组名搜索
        - 列表支持给用户组快捷授权
        - 列表支持给用户组快捷添加用户
        - 列表支持批量删除用户组
        - 列表支持创建用户组
        - 详情支持编辑用户组基本信息，例如描述
        - 详情支持记录用户组授权信息，支持添加 / 移除权限
        - 详情支持记录用户组成员信息，支持给用户组添加新成员，支持将成员从用户组移除
    3. [角色](../user-guide/access-control/role.md)
        - 列表展示系统角色名称、描述
        - 详情记录角色授权信息，支持将角色授予用户 / 用户组，支持将用户 / 用户组从该角色移除
        - 支持 Folder Admin、Folder Editor、Folder Viewer 三种预定义文件夹角色
        - 支持 Workspace Admin、Workspace Editor、Workspace Viewer 三种预定义工作空间角色
    4. [身份提供商](../user-guide/access-control/idprovider.md)
        - 支持 LDAP、OIDC 两种协议对接外部用户
        - LDAP 协议支持手动 / 自动同步外部用户
        - LDAP 协议支持手动同步外部用户组
        - OIDC 协议支持手动同步外部用户
2. 工作空间与层级
    1. [文件夹](../user-guide/workspace/folders.md)
        - 支持树状结构展示文件夹和工作空间
        - 支持通过文件夹名称和工作空间名称搜索
        - 支持 5 级文件夹映射企业层级
        - 支持为文件夹添加用户 / 用户组并授权
        - 支持权限继承，子文件夹、工作空间能够继承用户 / 用户组在上级文件夹权限
        - 支持移动文件夹。映射企业中的部门变动，移动后其下的子文件夹、工作空间及其资源 / 成员均会跟随该文件夹移动，权限的继承关系重新发生变化
    2. [工作空间](../user-guide/workspace/workspace.md)
        - 支持为工作空间添加用户 / 用户组并授权
        - 支持添加资源到工作空间 - 资源组，支持 6 种资源类型
        - 支持权限继承，资源组中的资源能够继承用户 / 用户组在工作空间和上级文件夹的角色
        - 支持移动工作空间。映射企业中的项目变动，移动后其下的资源 / 成员均会跟随该工作空间移动，权限的继承关系重新发生变化（开发中）
        - 支持添加资源到工作空间 - 共享资源，将一个集群资源共享给多个工作空间使用
        - 支持针对每个共享的集群资源进行资源限额
        - 支持通过 CPU Limit、CPU Request 、内存 Limit、内存 Request、存储请求总量 Request Storage、存储卷声明 PersistentVolumeClaim 六个维度进行资源限额
3. [审计日志](../user-guide/audit/audit-log.md)
    - 列表展示事件名称、资源类型、资源名称、状态、操作人、操作时间
    - 列表支持查看审计日志详情
    - 列表支持展示最近一天或自定义时间内的审计日志
    - 列表支持通过状态、操作人、资源类型、资源名称搜索审计日志
    - 列表支持 .csv 格式导出审计日志
    - 默认采集全局管理的全部审计日志
    - 默认保存 365 天内的审计日志
    - 支持手动 / 自动两种方式清理全局管理的审计日志
    - 支持开启 / 关闭收集 K8s 的审计日志
    - 支持手动 / 自动两种方式清理 K8s 的审计日志
4. 平台设置
    1. 安全策略
        - 支持自定义密码规则
        - 支持自定义密码策略
        - 支持自定义会话超时策略，超出时长自动退出当前账号
        - 支持自定义账号锁定策略，限制时间内多次登录失败，账号将被锁定
        - 支持登录登出策略，开启后关闭浏览器的同时退出登录
    2. [邮件服务器设置](../user-guide/platform-setting/mail-server.md)：支持管理员配置邮件服务器，支持通过邮件方式找回用户密码，接收告警通知等
    3. [外观定制](../user-guide/platform-setting/appearance.md)
        - 支持自定义登录页，包括更换平台 LOGO、登录页图标、标签页图标等
        - 支持一键还原登录页外观配置
        - 支持自定义顶部导航栏，包括导航栏图标、标签页图标等
        - 支持一键还原顶部导航栏外观配置
    4. [正版授权](../../dce/license0.md)
        - 列表展示许可证名称、所属模块、许可证级别、许可证状态过期时间
        - 支持管理许可证，确保子模块在有效期内
    5. [关于平台](../user-guide/platform-setting/about.md)
        - 支持展示模块版本
        - 支持展示平台使用的开源软件
        - 支持展示技术团队风采
5. 个人中心
    1. [安全设置](../user-guide/personal-center/security-setting.md)
        - 支持用户更新登录密码
        - 支持通过邮箱找回登录密码
    2. [访问密钥](../user-guide/personal-center/accesstoken.md)：支持每个用户创建独立的 API 密钥，支持进行 API 密钥过期设置，以确保系统安全
    3. [语言设置](../user-guide/personal-center/language.md)：支持多语言，支持简体中文、英文、自动检测您的浏览器首选语言三种方式确定语言
