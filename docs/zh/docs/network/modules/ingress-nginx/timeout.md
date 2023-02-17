# 超时配置

本页介绍 Ingress Nginx 的全局超时配置和特定的 Ingress 资源可用的超时配置。

## 全局超时配置

可通过以下配置项进行 Ingress Nginx 的全局超时配置：

|配置项|描述|默认值|
| ---- |---- | --- |
|`proxy-connect-timeout`|设置与代理服务器建立连接的超时。|默认 `5s`，但通常不能超过 `75s` |
|`proxy-read-timeout`|设置从代理服务器读取响应的超时。该超时仅在两个连续的读取操作之间设置，而不是为整个响应的传输设置。|`60s`|
|`proxy-send-timeout`|设置向代理服务器传输请求的超时。该超时只在两个连续的写操作之间设置，而不是为整个请求的传输设置。|`60s`|
|`proxy-stream-next-upstream-timeout`|限制允许将连接传递到下一个服务器的时间。|默认为 `600s`，设置为 `0` 值则关闭此限制。|
|`proxy-stream-timeout`|设置客户端或代理服务器连接上两个连续的读或写操作之间的超时。如果在这个时间内没有传输数据，连接就会关闭|`600s`|
|`upstream-keepalive-timeout`|设置一个超时时间，在这个时间内，与上游服务器的空闲保持连接将保持开放。| `60`|
|`worker-shutdown-timeout`|设置优雅停机的超时时间。|`240s`|
|`proxy-protocol-header-timeout`|设置接收代理协议头文件的超时值。默认的 5 秒可以防止 TLS 直通处理程序无限期地等待一个中断的连接。 |`5s`|
|`ssl-session-timeout`|设置 SSL 会话缓存中的会话参数的有效时间。会话过期时间是相对于创建时间而言的。每个会话缓存会占用大约 0.25MB 空间。|`10m`|
|`client-body-timeout`|定义读取客户端请求正文的超时。|`60s`|
|`client-header-timeout`|定义读取客户端请求头的超时。|`60s`|

## 特定的资源自定义超时配置

以下是特定的资源自定义超时配置，以及相关的参数配置，例如重试次数等：

|配置项|描述|
| ---- |---- |
|`nginx.ingress.kubernetes.io/proxy-connect-timeout`| 设置代理连接超时时间。|
|`nginx.ingress.kubernetes.io/proxy-send-timeout`|设置代理发送超时时间。|
|`nginx.ingress.kubernetes.io/proxy-read-timeout` |设置代理读取超时时间。|
|`nginx.ingress.kubernetes.io/proxy-next-upstream`|配置重试策略或者重试条件，可以使用多个组合用空格分隔，例如设置为 `http_500 http_502`，支持下列策略：<ul><li>`error`：建连失败，直接返回</li><li>`timeout`：连接超时，直接返回</li><li>`invalid_response`：无效返回状态码，直接返回</li><li>`http_xxx`：xxx 可以替换为状态码，例如设置为 `http_500` 的含义是上游返回 500 时选择选择下一个工作负载。支持的状态码为：`500`、`502`、`503`、`504`、`403`、`404`、`429`</li><li>`off`：关闭重试机制，不论任何错误都直接返回</li></ul>|
|`nginx.ingress.kubernetes.io/proxy-next-upstream-tries`| 如果满足重试条件时，可用的重试次数。|
|`nginx.ingress.kubernetes.io/proxy-request-buffering`|是否启用请求缓冲功能。设置为`on` 启用请求缓冲，`off` 则禁用请求缓冲。如果启用了请求缓冲功能，则会在接收到完整的请求数据之后才将其转发到后端工作负载，否则可能会在接收到部分请求数据时就开始转发请求。HTTP/1.1 Chunked 编码的请求不受此参数限制，始终会进行缓冲。如果禁用了，发送过程中出现发送错误，就不会选择下一个工作负载重试。|
