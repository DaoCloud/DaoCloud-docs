# 权限扫描

为了使用[权限扫描](index.md)功能，需要先创建扫描策略，执行该策略之后会自动生成扫描报告以供查看。

## 创建扫描策略

1. 在容器管理模块的首页左侧导航栏点击`安全管理`。

    ![安全管理](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/user-guide/images/security01.png)

2. 在左侧导航栏点击`权限扫描`，点击`扫描策略`页签，在右侧点击`创建扫描策略`。

    ![安全管理](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/user-guide/images/security11.png)

3. 参考下列说明填写配置，最后点击`确定`即可。

    - 集群：选择需要扫描哪个集群。可选的集群列表来自[容器管理](../../intro/index.md)模块中接入或创建的集群。如果没有想选的集群，可以去容器管理模块中[接入](../clusters/integrate-cluster.md)或[创建](../clusters/create-cluster.md)集群。
    - 扫描类型：

        - 立即扫描：在扫描策略创建好之后立即执行一次扫描，后续不可以自动/手动再次执行扫描。
        - 定时扫描：通过设置扫描周期，自动按时重复执行扫描。

    - 扫描报告保留数量：设置最多保留多少扫描报告。超过指定的保留数量时，从最早的报告开始删除。

        ![安全管理](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/user-guide/images/security12.png)

## 更新/删除扫描策略

创建扫描策略之后，可以根据需要更新或删除扫描策略。

在`扫描策略`页签下，点击配置右侧的 `ⵗ` 操作按钮：

- 对于周期性的扫描策略：

    - 选择`立即执行`意味着，在周期计划之外立即再扫描一次集群
    - 选择`禁用`会中断扫描计划，直到点击`启用`才可以继续根据周期计划执行该扫描策略。
    - 选择`编辑`可以更新配置，支持更新扫描配置、类型、扫描周期、报告保留数量，不可更改配置名称和需要扫描的目标集群。
    - 选择`删除`可以删除该配置

- 对于一次性的扫描策略：仅支持`删除`操作。

    ![创建扫描配置](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/user-guide/images/security13.png)

## 查看扫描报告

1. 在`安全管理`->`权限扫描`->`扫描报告`页签下，点击报告名称

    > 在报告右侧点击`删除`可以手动删除报告。

    ![创建扫描配置](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/user-guide/images/security14.png)

2. 查看扫描报告内容，包括：

    - 扫描的目标集群
    - 使用的扫描策略
    - 扫描项总数、警告数、错误数
    - 在周期性扫描策略生成的扫描报告中，还可以查看扫描频率
    - 扫描开始的时间
    - 检查详情，例如被检查的资源、资源类型、扫描结果、错误类型、错误详情

        ![创建扫描配置](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/user-guide/images/security15.png)