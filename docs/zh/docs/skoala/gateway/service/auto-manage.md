# 自动纳管服务

添加成功的服务会出现在服务列表页面，添加 API 时也可以选择列表中的服务作为目标后端服务。
微服务网关支持通过手动接入和自动纳管两种方式添加服务。本页介绍如何自动纳管服务。

[网关实例创建](../index.md)成功之后，服务来源<!--待补充链接-->中的服务会被自动添加到该网关实例的服务列表中，无需手动添加。

## 查看自动纳管的服务

1. 在 __微服务网关列表__ 页面点击目标网关的名称，进入网关概览页后，在左侧导航栏点击 __服务接入__ --> __服务列表__ 。

    ![服务列表](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/service/images/service-list.png)

2. 在 __服务列表__ 页面点击 __自动纳管__ 。

    ![自动发现服务](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/service/images/auto.png)

## 配置服务策略

1. 在 __服务列表__ -> __自动纳管__ 页面找到目标服务，在右侧点击 __ⵗ__ 选择 __修改策略配置__ 。

    ![策略配置](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/service/images/policy1.png)

2. 按需调整服务策略配置，在弹框右下角点击 __确定__ 。

    - HTTPS 证书验证：开启后，必须通过证书校验才能成功访问该服务。
    - 服务熔断：当最大连接数、最大处理连接数、最大并行请求数、最大并行重试数 **任何一个** 指标达到设定的阈值时，自动切断对该服务的调用，保护系统整体的可用性。当指标降到设定的阈值之后，自动恢复对该服务的调用。

    ![策略配置](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/service/images//policy2.png)

## 查看服务详情

1. 在 __服务列表__ -> __自动纳管__ 页面找到目标服务，点击服务名称。

    ![服务详情](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/service/images/service-details.png)

2. 查看服务名称、来源、关联的 API 等信息。支持安装`最近更新时间`进行排序。

    ![服务详情](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/gateway/service/images/service-details1.png)

!!! info

    对于自动纳管的服务，仅支持上述操作，不支持更新、删除服务的操作。
