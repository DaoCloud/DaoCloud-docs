# 配置 API 策略

DCE 5.0 微服务网关支持十二种 API 策略：负载均衡、路径改写、超时配置、重试机制、请求头重写、响应头重写、Websocket、本地限流、健康检查、全局限流、Cookie重写、访问黑白名单。
可以单独使用某一种策略，也可以组合使用多种策略达到最佳实践。
有关 API 策略的组合配置，参考[API 策略配置最佳实践](../../best-practice/gateway02.md)。

有两种方式可以配置 API 策略：

- 在创建 API 的过程中设置策略，参考[添加 API](index.md)。
- 在 API 创建完成后通过[更新 API 策略配置](update-api.md)进行调整。

**视频教程**：

- [API 策略的高级配置（1）](../../../videos/skoala.md#api-1)
- [API 策略的高级配置（2）](../../../videos/skoala.md#api-2)

**每一项策略的配置说明如下**:

## 负载均衡

当 API 的目标后端服务为多实例服务时，可以通过负载均衡策略控制流量分发，根据业务场景调整不同服务的实例接收到的流量。

- 随机

    默认的负载均衡策略。选择随机规则时，网关会将请求随机分发给后端服务的任意实例。在流量较小时，部分后端服务可能会负载较多。效果参考下图：

    ![负载均衡](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/lb-random.png)

- 轮询

    向后端服务的所有实例轮流分发请求，各个服务实例接收到的请求数基本相近。此规则可以在流量较小时保障流量的平均分配。效果参考下图：

    ![负载均衡](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/lb-rc.png)

- 权重

    根据 API 目标后端服务的权重分发流量，权重数值越大，优先级越高，承担的流量也相对较多。服务权重的配置入口见下图：

    ![负载均衡](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/lb-weight.png)

- Cookie

    将来源请求头中属于相同 Cookie 的流量分发到固定的后端服务实例，前提是后端服务能够根据 Cookie 做出不同的响应处理。

- 请求 Hash

    选择请求 Hash 时，可以通过一些高级策略来进负载均衡分配。当前支持的 Hash 策略为：IP、请求参数。

    ![负载均衡](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/lb.png)

## 路径改写

如果对外暴露的 API 路径与后端服务提供的路径不一致，可以改写 API 路径使其与后端服务的路径一致，确保服务的正常访问。
启用路径改写后，网关会将外部请求流量转发到重写后的路径。

注意：**需要确保重写的路径是真实存在的，并且路径正确，以 “/” 开头**

![路径改写](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/rewrite.png)

## 超时配置

设置请求响应的最大时长，如果超出所设置的最大时长，则直接请求失败。超时时长支持数值类型为 >=1 的整数值，时间单位为“秒（s）”。

超时配置默认处于关闭状态，开启后必须配置超时时长。开启超时配置有助于减少异常处理导致的阻塞问题。

![超时](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/timeout.png)

## 重试机制

微服务网关的 API 支持配置非常丰富的重试机制。启用重试机制后，网关会在请求失败时自动重新尝试访问。
达到重试超时时间之后自动触发再次重试，当重试次数达到配置的最大重试次数时停止重试。重试机制默认处于关闭状态，开启后必须配置重试次数和重试超时时长。

支持通过自定义配置选择不同的重试条件，自定义重试状态码等。

### HTTP 重试

- 5XX 响应错误：后端服务响应 HTTP status_code 大于 500 时进行重试。
- 网关错误：当响应结果为网关错误提示时，自动进行重试。
- 请求重置：当响应结果为请求重置消息时，自动进行重试。
- 连接失败：当响应结果为网络连接失败的返回时，自动进行重试。
- 拒绝流：当响应结果为后端服务将请求标记为拒绝处理时，自动进行重试。
- 指定状态码：当后端服务响应 HTTP status_code 为特定状态码时自动进行重试，支持配置特定的状态码。

### GRPC 重试

- 请求被取消：当响应结果为GRPC 请求被后端服务取消时自动进行重试。
- 响应超时： 当后端服务响应超时，自动进行重试。
- 服务内部错误：当响应结果为服务内部错误时，自动进行重试。
- 资源不足：当响应结果为资源不足时，自动进行重试。
- 服务不可用时：当响应结果为后端不可用时，自动进行重试。

![重试](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/retry.png)

## 请求头/响应头改写

支持添加、修改、删除请求头和响应头及其对应的值。

- 增加请求头/响应头：使用`设置`动作，填写新的关键字和新值。
- 修改请求头/响应头：使用`设置`动作，填写已有的关键字并赋予新值。
- 移除请求头/响应头，使用`移除`动作，只填写需要移除的关键字即可，无需填写对应的值。

![header 改写](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/header-rewrite.png)

## Websocket

WebSocket 是一种在单个 TCP 连接上进行全双工通信的协议。WebSocket 使得客户端和服务器之间的数据交换变得更加简单，允许服务端主动向客户端推送数据。在 WebSocket API 中，浏览器和服务器只需要完成一次握手，两者之间就直接可以创建持久性的连接，并进行双向数据传输。

启用 Websocket 之后支持通过 Websocket 协议访问 API 的后端服务。

![websocket](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/websocket.png)

## 本地限流

微服务网关支持丰富的限流能力，支持在 API 层级启用本地限流能力。

- 请求速率：时间窗口（秒/分/时）内允许的最大请求速率，例如每分钟最多允许 3 次请求。支持输入 >=1 的整数。
- 允许溢出速率：达到预设的请求速率时，仍旧允许额外处理一部分请求，适用于业务突增的流量高峰时段。支持输入 >=1 的整数。
- 限制返回码：默认返回码为 429，表示请求次数过多。可参考 envoy
  官方文档了解[本地限流支持的状态码](https://github.com/envoyproxy/envoy/blob/v1.23.1/api/envoy/type/v3/http_status.proto#L137)。
- Header 关键字：默认为空，可根据需求自行设置。

下图中的配置表示：每分钟最多允许请求 8 次 (3+5)，第 9 次访问时会返回 429 状态码，提示访问次数过多。
每次请求成功后返回的响应内容都会带上 `ratelimit：8` 响应头。

![本地限流](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/ratelimit.png)

!!! info

    除了在 API 层级的本地限流能力之外，还可以通过[配置域名策略](../domain/domain-policy.md)针对整个域名进行限流处理。
    当 API 与域名同时配置限流策略时，以 API 层级的限流策略为准。

## 健康检查

通过设置健康检查地址，可以有效保证当后端服务异常时，网关自动进行负载均衡调整。对不健康的后端服务进行标记，停止向该服务分发流量。当后端服务恢复并通过设定的健康检查条件后，自动恢复流量分发。

- 健康检查路径：以 “/” 开头，并且全部后端服务的所有实例都应提供相同的健康检查接口。
- 特定健康检查主机：配置主机地址后，仅对该主机进行健康检查。
- 检查时间间隔：每次健康检查的时间间隔，时间单位为“秒”，例如每隔 10 秒进行一次健康检查。
- 检查超时时间：健康检查的最大超时时长，当健康检查超过配置的时长时，直接标记健康检查失败。
- 标记健康检查次数：连续检查 N 次并且每次结果都是健康时，才将服务实例标记为健康状态；
  当服务实例被标记为健康状态后，请求流量将会自动分发到该服务实例。
- 标记不健康检查次数：连续检查 N 次并且每次结果都是不健康时，就将服务实例标记为不健康状态，
  当服务实例被标记为不健康时，停止向该实例分发请求流量。

![健康检查](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/healthcheck.png)

## Cookie 重写

参考下方说明配置 cookie 重写策略：

- 名称：必须填写当前已经存在的 cookie 名称
- 域名：重新定义 cookie 的域名
- 路径：重新定义 cookie 的路径
- Secure：`保持`指启用安全模式，`禁用`指禁用安全模式。在安全模式下，请求必须为安全连接（HTTPS），
  cookie 才会被保存下来。如果使用 HTTP 协议下，cookie 将无效
- Samesite：是否在跨域时发送 cookie

    - Strict：跨域请求严禁携带本站 cookie
    - Lax：大多数情况禁止，但是导航到目标网址的 Get 请求除外。
    - None：跨域请求允许携带本站 cookie，前提是 Secure 必须设置为`保持`，即只能在 HTTPS 协议下使用

![cookie 重写](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/cookie.png)

## 访问黑白名单

启用`访问黑白名单`后，可以仅允许白名单上的 IP 请求通过网关，拒绝其他所有来源的请求；或者拒绝黑名单上的 IP 请求通过网关，允许其他所有来源的请求。

- 网关前置代理层数：请求从客户端到网关中途需要经过几个代理端点。例如 `客户端-Nginx-网关` 的代理层数为 1，因为中间只经过 1 个 Nginx 代理端点。

    > 创建/更新网关时，可以在网关的`高级配置`部分设置代理层数，需要按照实际情况填写。

- Remote：IP 来源为 Remote 时，黑白名单是否生效取决于网关前置代理层数。当代理层数为 n 时，生效的是从网关开始向前第 n+1 个端点的 IP。
  例如 `客户端-Nginx-网关` 前置代理层数为 1，则仅对网关向前第 2 个端点的 IP 生效，即客户端的 IP。如果填写 Nginx 的 IP，黑白名单不会生效。

    ![黑白名单](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/backlist01.png)

- Peer：IP 来源为 Peer 时，无论网关前置代理层数是多少，黑白名单都仅对网关的 **直接** 对端 IP 生效。例如`客户端-...-Nginx-网关`，无论客户端和 Nginx 中间有多少个代理端点，黑白名单都仅对最后一个 Nginx 的 IP 生效。

    ![黑白名单](https://docs.daocloud.io/daocloud-docs-images/docs/skoala/ms-gateway/api/imgs/blacklist.png)
