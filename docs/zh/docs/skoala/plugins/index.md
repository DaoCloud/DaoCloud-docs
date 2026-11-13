---
hide:
  - toc
---

# 插件中心

插件中心是针对云原生网关和云原生微服务的统一插件管理门户，其中涉及多种流控，权限及自定义插件，
一次配置后即可在云原生网关和云原生微服务中进行使用，避免了相同业务逻辑需求下的插件重复开发，为开发和运维人员带来了更多便利。

微服务引擎支持接入 Auth、JWT、全局限流、Wasm、ExtProc 插件。
**只有先在插件中心接入插件，然后才能在云原生微服务或云原生网关中使用这些插件**。

<div class="grid cards" markdown>

- :simple-jsonwebtokens:{ .lg .middle } __JWT__

    ---

    JWT（JSON Web Token）是一种用于身份验证和授权的开放标准。它由三部分组成：
    头部、载荷和签名。JWT 可以在客户端和服务器之间传递信息，并使用签名进行验证。
    在云计算和云原生行业中，JWT 通常用于在微服务架构中进行身份验证和授权。

- :material-shield-lock:{ .lg .middle } __Auth__

    ---

    Auth（Authorization）是一种用于验证用户身份和授权访问的插件。
    它可以与 JWT 一起使用，对请求进行身份验证，并根据用户的权限决定是否允许访问特定资源。
    Auth 插件可以确保只有经过身份验证的用户才能访问特定的 API 或服务。

- :material-speedometer:{ .lg .middle } __全局限流__

    ---

    Rate Limit（全局限流）是一种用于限制请求速率的插件。在云计算和云原生环境中，
    由于大量的请求可能会对系统造成负载压力，Rate Limit 插件可以帮助限制每个用户或 IP 地址的请求速率，
    以确保系统的稳定性和安全性。

- :material-chip:{ .lg .middle } __Wasm__

    ---

    Wasm（WebAssembly）是一种低级别的字节码格式，可以在浏览器中运行高性能的编译代码。
    在云计算和云原生行业中，Wasm 可以用作插件的运行环境，使开发人员能够使用更多的编程语言和工具来扩展和定制云服务。
    通过使用 Wasm 插件，可以实现更高效、可扩展和灵活的云原生应用程序。

- :material-cog:{ .lg .middle } __ExtProc__

    ---

    ExtProc（External Process）是一种用于调用外部进程的插件。ExtProc 插件可以将请求和响应转发给外部进程，
    由外部进程处理请求并返回结果。可以对请求进行额外处理，例如修改请求头、请求体、响应头、响应体等，
    或者根据请求的信息进行额外的自定义逻辑处理。

</div>

![plugin list](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/plugin01.png)

## 插件应用

<div class="grid cards" markdown>

- :material-lan:{ .lg .middle } __云原生微服务使用 JWT 插件__

    ---

    在服务网格中创建托管网格，导入演示应用，并在云原生微服务中启用 JWT 插件完成验证。

    [:octicons-arrow-right-24: 开始使用](jwt-ms.md)

- :material-gate:{ .lg .middle } __云原生网关使用 JWT 插件__

    ---

    创建网关、域名和 API，在域名或 API 的安全策略中启用 JWT 认证。

    [:octicons-arrow-right-24: 开始使用](jwt.md)

- :material-shield-key:{ .lg .middle } __微服务网关接入认证服务器__

    ---

    部署认证服务器并将其接入云原生网关，在域名和 API 层面启用认证。

    [:octicons-arrow-right-24: 开始使用](auth-server.md)

- :material-key:{ .lg .middle } __接入 AK/SK 认证__

    ---

    基于认证服务器演示如何接入 AK/SK 认证，包括部署和请求验证步骤。

    [:octicons-arrow-right-24: 开始使用](ak-sk-demo.md)

- :material-certificate:{ .lg .middle } __接入 OIDC 认证__

    ---

    基于 OIDC 协议接入第三方认证服务，实现网关的单点登录与访问控制。

    [:octicons-arrow-right-24: 开始使用](OIDC-auth.md)

- :material-timer:{ .lg .middle } __微服务网关接入限流服务器__

    ---

    部署全局限流服务器并将其接入云原生网关，为域名和 API 配置限流策略。

    [:octicons-arrow-right-24: 开始使用](global-ratelimit.md)

</div>

## 自定义插件示例

以下示例均基于 Envoy 的 `ext_proc` 能力，以 Go 语言实现，可作为自定义插件开发的参考：

<div class="grid cards" markdown>

- :material-flash:{ .lg .middle } __caching__

    ---

    使用非持久化存储缓存 GET 请求的应答，命中缓存时直接返回。

    [:octicons-arrow-right-24: 查看示例](envoy-extproc-caching-demo-go.md)

- :material-shield-lock:{ .lg .middle } __anti（防重放）__

    ---

    在请求路由到 Upstream 之前审核 sign、timestamp、nonce，任一验证失败直接应答 401。

    [:octicons-arrow-right-24: 查看示例](envoy-extproc-anti-demo-go.md)

- :material-certificate:{ .lg .middle } __crc32-check__

    ---

    在请求路由到 Upstream 之前对请求体执行 CRC 校验，校验未通过直接应答 403。

    [:octicons-arrow-right-24: 查看示例](envoy-extproc-crc32-check-demo-go.md)

- :material-cog:{ .lg .middle } __method-conv__

    ---

    将 Downstream 发起的 GET/POST 请求转换为 POST/GET 请求后再发送到 Upstream。

    [:octicons-arrow-right-24: 查看示例](envoy-extproc-method-conv-demo-go.md)

- :material-puzzle:{ .lg .middle } __payloadlimit__

    ---

    在请求路由到 Upstream 之前审核请求体大小，超过最大准许值直接应答 413。

    [:octicons-arrow-right-24: 查看示例](envoy-extproc-payloadlimit-demo-go.md)

</div>
