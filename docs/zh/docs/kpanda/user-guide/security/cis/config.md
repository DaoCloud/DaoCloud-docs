# 扫描配置

使用[合规性扫描](../index.md)的第一步，就是先创建扫描配置。基于扫描配置再创建扫描策略、执行扫描策略，最后查看扫描结果。

## 创建扫描配置

创建扫描配置的步骤如下：

1. 在容器管理模块的首页左侧导航栏点击 __安全管理__ 。

    ![安全管理](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/user-guide/images/security01.png)

2. 默认进入 __合规性扫描__ 页面，点击 __扫描配置__ 页签，然后在右上角点击 __创建扫描配置__ 。
  
    ![安全管理](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/user-guide/images/security02.png)

3. 填写配置名称、选择配置模板、按需勾选扫描项，最后点击 __确定__ 。

    扫描模板：目前提供了两个模板。 __kubeadm__ 模板适用于一般情况下的 Kubernetes 集群。 __daocloud__ 模板在 __kubeadm__ 模板基础上，结合 DCE 5.0 的平台设计忽略了不适用于 DCE 5.0 的扫描项。

    ![安全管理](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/user-guide/images/security03.png)

## 查看扫描配置

在扫描配置页签下，点击扫描配置的名称，可以查看该配置的类型、扫描项数量、创建时间、配置模板，以及该配置启用的具体扫描项。

![安全管理](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/user-guide/images/security04.png)

## 更新/删除扫描配置

扫描配置创建成功之后，可以根据需求更新配置或删除该配置。

在扫描配置页签下，点击配置右侧的 __┇__ 操作按钮：

- 选择 __编辑__ 可以更新配置，支持更新描述、模板和扫描项。不可更改配置名称。
- 选择 __删除__ 可以删除该配置。

    ![安全管理](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/user-guide/images/security04.png)
