# 日志配置

本文说明 Ingress Nginx 全局设置中用于配置日志的选项，例如日志输出路径，输出格式，日志等级等。

<table>
<tr>
<td>配置项</td> <td>描述</td> <td>默认配置</td>
</tr>
<tr>
<td><code>access-log-path</code></td> <td>用于设置访问日志的输出位置。建议将日志输出到 <code>stdout</code>，以便在容器平台上进行方便的日志收集。</td> <td>默认为 <code>/var/log/nginx/access.log</code>，其是 <code>/dev/stdout</code> 的符号链接。</td>
</tr>
<tr>
<td><code>error-log-path</code></td> <td>用于设置错误日志的输出位置。建议将日志输出到 <code>stderr</code>，以便在容器平台上进行方便的日志收集。</td> <td>默认为 <code>/var/log/nginx/error.log</code>，其是 <code>/dev/stderr</code> 的符号链接。</td>
</tr>
<tr>
<td><code>disable-access-log</code></td> <td>关闭访问日志输出。</td> <td> N/A </td>
</tr>
<tr>
<td><code>http-access-log-path</code> 和 <code>stream-access-log-path</code></td> <td>分别控制 http 和 stream 的日志</td> <td>默认为：""。如无指定，则使用 <code>access-log-path</code> 的值。</td>
</tr>
<tr>
<td><code>enable-access-log-for-default-backend</code> </td> <td>启用默认后端的日志访问</td> <td>默认值为 <code>false</code>。</td>
</tr>
<tr>
<td><code>error-log-level</code></td> <td>错误日志等级，支持设置为 <code>debug</code>, <code>info</code>, <code>notice</code>, <code>warn</code>, <code>error</code>, <code>crit</code>, <code>alert</code>, <code>emerg</code>。这些日志等级是按照严重程度的增加顺序排列的，例如级别 <code>crit</code> 将导致 <code>crit</code>, <code>alert</code> 和 <code>emerg</code> 消息被记录下来。</td> <td>默认为 <code>notice</code>。</td>
</tr>
<tr>
<td><code>log-format-escape-none</code></td> <td>设置是否完全禁止变量中的字符转义参数（<code>true</code>）或由 <code>log-format-escape-json</code> 控制（<code>false</code>） 设置 nginx 日志格式。</td> <td>N/A</td>
</tr>
<tr>
<td><code>log-format-escape-json</code></td> <td>在输出格式为 JSON 的场景，对渲染的值进行转义。</td> <td>默认为 <code>false</code>。</td>
</tr>
<tr>
<td> <code>log-format-upstream</code> </td><td>设置 nginx 日志格式，可使用的字段可以参考 [Embedded Variables](https://nginx.org/en/docs/http/ngx_http_upstream_module.html#variables)。以下是一个设置为 json 输出的例子：

```yaml
log-format-upstream: '{"time": "$time_iso8601", "remote_addr": "$proxy_protocol_addr", "x_forwarded_for": "$proxy_add_x_forwarded_for", "request_id": "$req_id",
  "remote_user": "$remote_user", "bytes_sent": $bytes_sent, "request_time": $request_time, "status": $status, "vhost": "$host", "request_proto": "$server_protocol",
  "path": "$uri", "request_query": "$args", "request_length": $request_length, "duration": $request_time,"method": "$request_method", "http_referrer": "$http_referer",
  "http_user_agent": "$http_user_agent" }'
```

</td><td>N/A</td>
</tr>
<tr>
<td><code>log-format-stream</code></td><td>设置 nginx stream 日志输出格式。</td><td>N/A</td>
</tr>
<tr>
<td><code>skip-access-log-urls</code></td><td>过滤掉出现在 NGINX 访问日志中的 URL 列表。最佳实践是过滤 <code>/health</code> 这种健康检查 URL 很有用，因为它们会使阅读日志变得复杂。</td><td>默认为空。</td>
</tr>
<tr>
<td><code>enable-syslog</code> </td><td>启用 syslog 功能访问日志和错误日志。    <ul><li><code>syslog-host</code> 设置 syslog 服务器的地址，该地址可以被指定为域名或 IP 地址。</li><li><code>syslog-port</code> 设置 syslog 服务器的端口。默认：<code>514</code>。</li></ul></td><td>默认为 <code>false</code>。</td>
</tr>
<table>
