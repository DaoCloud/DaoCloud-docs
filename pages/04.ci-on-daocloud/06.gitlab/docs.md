---
title: '与私有的 GitLab 代码源绑定'
taxonomy:
    category:
        - docs
---

除了常见的公有代码仓库，我们还支持与企业的私有 GitLab 仓库对接，可外网访问的 GitLab 仓库和企业内部 GitLab 仓库。该功能为企业版功能，如您需要了解，请[跟我们联系](mailto:support@daocloud.io)。

#### 可外网访问的 GitLab 仓库
在这种情况下，企业的 GitLab 代码仓库是外网可访问的，用户需要指定 GitLab 地址、用户名和 Token 等信息。

![](Dashboard_gitlabtoken.png?resize=800)

#### 企业内部 GitLab 仓库
在这种情况下，企业的 GitLab 代码仓库仅提供内网访问，不需要用户开防火墙端口，GitLab 地址需要预先通过后台配置在 DaoCloud 平台上，该 GitLab 对特定组织的所有成员可见，组织成员可以绑定自己在该 GitLab 中的用户账户，如下图所示。

![](Dashboard_privategitlab.png?resize=800)

![](Dashboard_privategitlabtoken.png?resize=800)

#### GitLab 配置参数

关于对接 GitLab 的参数输入，详细解释如下：

+ 地址：请输入 GitLab 对应到外网的 IP 地址或域名，采用 http(s)://IP，或 http(s)://URL 的方式；
+ 用户名：请使用您登陆 GitLab 的用户名 （请注意，这里填写用户的显示名会导致授权失败）
+ Token：在 GitLab 内生成，具体操作如下图

![](Account_%C2%B7_Profile_Settings_%C2%B7_GitLab.png)

<!-- 
GitLab 的简单介绍

GitLab 的私有部署

GitLab 需要暴露在外网
GitLab 绑定流程的介绍和截图，这个是专业版付费功能，如果你的界面中没有开启，跟我联系，我给你开通。
GitLab 绑定需要输入 IP、用户名和密码，不必真是绑定，只要 show 出这个界面即可。

这里不展开，做一个链接到DaoCloud 私有云的交付形式
DaoCloud GitHub 公有仓库提供了大量的开发示例代码，帮助用户快速上手，鼓励用户 Fork 这些项目。最后做一个链接，到写给开发者的例子这篇文章。
-->