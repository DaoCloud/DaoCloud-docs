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

## 视频演示和 PDF

将 DCE 5.0 集成到客户系统（OEM OUT），参阅 [OEM OUT 文档](../oem/oem-out.md)。

<div class="responsive-video-container">
<video controls src="https://harbor-test2.cn-sh2.ufileos.com/docs/videos/oem-out.mp4" preload="metadata" poster="../../../videos/images/oem-out.png"></video>
</div>

将客户系统集成到 DCE 5.0（OEM IN），参阅 [OEM IN 文档](../oem/oem-in.md)。

<div class="responsive-video-container">
<video controls src="https://harbor-test2.cn-sh2.ufileos.com/docs/videos/oemin-istio.mp4" preload="metadata" poster="../../../videos/images/oem-in.png"></video>
</div>

[查阅和下载 GProduct PDF](./GProduct-manual.pdf){ .md-button .md-button--primary }
