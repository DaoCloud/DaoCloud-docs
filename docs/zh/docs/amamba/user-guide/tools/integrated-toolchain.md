# 集成工具链

DevOps 工具链是一组工具，使 DevOps 团队能够在整个产品生命周期中进行协作并解决关键的 DevOps 基础问题。

应用工作台支持两种视角的工具链集成：工作空间集成、管理员集成。其中管理员集成的实例支持分配到工作空间下，以供工作空间使用。

## 支持集成的工具链

| 工具链名称 | 描述                                                         | 认证                                                         | 备注                                                         |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| GitLab     | 集成 GitLab 仓库后，可在流水线中使用                         | Personal Access Token，获取路径：右上角头像 > Settings > Access Tokens > Create personal access token | 创建 personal access token 时必须勾选 `api `，并且是用户的个人令牌。 |
| Jira       | 通过在应用工作台中集成 Jira，从而支持对Jira->Issue的追踪。   | 用户名/密码                                                  | -                                                            |
| Jenkins    | 集成Jenkins 后，所有的工作空间均将获得流水线能力进行构建。   | 用户名/密码                                                  | 仅支持管理员集成，且全平台仅能集成一次 Jenkins               |
| SonarQube  | 集成 SonarQube 后，可以在流水线中定义代码质量扫描            | User-Token，获取路径：My Account -> Profile -> Security -> Generate Token （注意 Token 的类型选择 User-Token） | -                                                            |
| Nexus      | Nexus 是软件仓库管理工具                                     | 用户名/密码                                                  | -                                                            |
| TestLink   | TestLink 是测试用例管理工具，提供了一个协作平台，用于测试用例的创建、管理以及执行，并且支持缺陷管理的整合 | Token                                                        | -                                                            |

## 操作步骤

1. 进入 __工具链集成__ 页面，点击 __工具链集成__ 按钮。

    ![tool01](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/tool01.png)

2. 参考以下说明，配置相关参数：

    - 工具：选择一个工具链类型进行集成。
    - 集成名称：集成工具的名称，不可重复。
    - 地址：可访问工具链的地址，以 http://, https:// 开头的域名或 IP 地址。
    - 用户名和密码：可以登录工具链的用户和密码。

    ![tool02](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/tool02.png)

3. 点击 __确定__ ，集成成功返回到工具链列表页面。

    ![tool03](https://docs.daocloud.io/daocloud-docs-images/docs/amamba/images/tool03.png)