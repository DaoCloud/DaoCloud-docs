# 日志配置

本文说明 Ingress Nginx 全局设置中用于配置日志的选项，例如日志输出路径，输出格式，日志等级等。

|配置项|描述|默认配置|
| ---- |---- | --- |
|`access-log-path` |用于设置访问日志的输出位置。建议将日志输出到 `stdout`，以便在容器平台上进行方便的日志收集。|默认为 `/var/log/nginx/access.log`，其是 `/dev/stdout` 的符号链接。|
|`error-log-path`| 用于设置错误日志的输出位置。建议将日志输出到 `stderr`，以便在容器平台上进行方便的日志收集。|默认为 `/var/log/nginx/error.log`，其是 `/dev/stderr` 的符号链接。|
|`disable-access-log` |关闭访问日志输出。|N/A|
|`http-access-log-path` 和 `stream-access-log-path` |分别控制 http 和 stream 的日志。|默认为：""，若无指定，则使用 `access-log-path` 。|
|`enable-access-log-for-default-backend`|启用默认后端的日志访问。|默认值为 `false`。|
|`error-log-level` |错误日志等级，支持设置为 `debug`, `info`, `notice`, `warn`, `error`, `crit`, `alert`, `emerg`。这些日志级别是按照严重程度的增加顺序排列的，例如级别 `crit` 将导致 `crit`, `alert` 和 `emerg` 消息被记录下来。|默认为 `notice`。|
|`log-format-escape-none` |设置是否完全禁止变量中的字符转义参数（`true`）或由 `log-format-escape-json` 控制（`false`） 设置 nginx 日志格式。|N/A|
|`log-format-escape-json` |在输出格式为 JSON 的场景，对渲染的值进行转义。|默认为 `false`。|
|`log-format-stream` |设置 nginx stream 日志输出格式。|N/A|
|`skip-access-log-urls` |过滤掉出现在 NGINX 访问日志中的 URL 列表。最佳实践是过滤 `/health`。这种健康检查 URL 很有用，因为它们会使阅读日志变得复杂。|默认为空。|
|`enable-syslog` |启用 syslog 功能访问日志和错误日志。<ul><li>`syslog-host` 设置 syslog 服务器的地址，该地址可以被指定为域名或 IP 地址。</li> <li> `syslog-port` 设置 syslog 服务器的端口。默认：`514`。</li> </ul>| 默认为 `false`。|
|`log-format-upstream` |设置 nginx 日志格式，可使用的字段可以参考 [Embedded Variables](https://nginx.org/en/docs/http/ngx_http_upstream_module.html#variables)。以下是一个设置为 json 输出的例子。

```yaml
log-format-upstream: '{"time": "$time_iso8601", "remote_addr": "$proxy_protocol_addr", "x_forwarded_for": "$proxy_add_x_forwarded_for", "request_id": "$req_id",
  "remote_user": "$remote_user", "bytes_sent": $bytes_sent, "request_time": $request_time, "status": $status, "vhost": "$host", "request_proto": "$server_protocol",
  "path": "$uri", "request_query": "$args", "request_length": $request_length, "duration": $request_time,"method": "$request_method", "http_referrer": "$http_referer",
  "http_user_agent": "$http_user_agent" }'
```
