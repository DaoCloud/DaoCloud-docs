---
hide:
  - toc
---

# GProduct 如何对接全局管理

GProduct 是 DCE 5.0 中除全局管理外的所有其他模块的统称，这些模块需要与全局管理对接后才能加入到 DCE 5.0 中。

## 对接什么

- [对接导航栏](./nav.md)

    入口统一放在左侧导航栏。

- [接入路由和 AuthN](route-auth.md)

    统一 IP 或域名，将路由入口统一走全局管理的 Istio Gateway。

- 统一登录 / 统一 AuthN 认证

    登录统一使用全局管理 (Keycloak) 登录页，API authn token 验证使用 Istio Gateway。
    GProduct 对接全局管理后不需要关注如何实现登录和认证。

[DCE 5.0 对接客户系统视频演示](../../videos/use-cases.md#dce-50_2)
