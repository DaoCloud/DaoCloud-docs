---
hide:
  - toc
---

# 删除微服务网关

微服务网关支持多租户实例的高可用架构，兼容多种模式微服务的统一网关接入能力。本页介绍如何删除微服务网关实例。

删除网关同样也有两种方式。为保证服务不受影响，删除网关之前需要释放到网关中全部路由的 API。

!!! danger

    网关删除后不可恢复，请谨慎操作。

- 在`微服务网关列表`页选择需要移除的网关实例，在实例右侧点击 `⋯` 并选择`删除`。

    ![移除网关](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/gateway/imgs/delete.png)

- 点击网关名称进入进入概览页面后，在右上角 `⋯` 并选择`删除`。

    ![移除网关](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/gateway/imgs/delete-gateway.png)
