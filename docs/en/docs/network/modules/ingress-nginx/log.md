---
MTPE: Jeanine-tw
Revised: Jeanine-tw
Pics: N/A
Date: 2023-02-20
---

# Configure log

This page describes the options used to configure log in the Ingress Nginx global settings, such as log output path, output format, logging level, and so on.

|option's name|description|default|
| ---- | ---- | --- |
|`access-log-path` | Set the output location of the access log. It is recommended to output the logs to `stdout` for easy log collection on container platforms. |Go to `/var/log/nginx/access.log` by default, which is a symlink to `/dev/stdout`. |
|`error-log-path`| Set the output location of the error log. It is recommended to output logs to `stderr` for easy log collection on container platforms. |Go to `/var/log/nginx/error.log` by default, which is a symlink to `/dev/stderr`. |
|`disable-access-log` |Disable the Access Log from the entire Ingress Controller. |N/A|
|`http-access-log-path` and `stream-access-log-path` |Control log for http and stream context respectively. |Default: "", and if not specified, `access-log-path` is used. |
|`Enable-access-log-for-default-backend`|Enable logging access to default backend.  |The default is `false`. |
|`error-log-level` | Configure the logging level of errors. Log levels are listed in the order of increasing severity, including `debug`, `info`, `notice`, `warn`, `error`, `crit`, `alert`, `emerg`.  For example level `crit` will cause `crit`, and `alert` and `emerg` messages to be logged. |The default is `notice`. |
| `log-format-escape-none` | Set if the escape parameter is disabled entirely for character escaping in variables (`true`) or controlled by log-format-escape-json (`false`) Set the nginx log format. |N/A|
|`log-format-escape-json` | Set if the escape parameter allows JSON (`true`) or default characters escaping in variables (`false`) Set the nginx log format. |The default is `false`.|
|`log-format-stream` |Set the nginx stream format.|N/A|
|`skip-access-log-urls` |Set a list of URLs that should not appear in the NGINX access log. This is useful with urls like `/health` that make "complex" reading the logs. |The default is empty|
|`enable-syslog` |Enable syslog feature for access log and error log. <ul><li>`syslog-host` is used to set the address of the syslog server, which can be specified as a domain name or IP address. </li> <li> `syslog-port` is used to set the port of the syslog server. Default: `514`.  </li> </ul>| The default is `false`。 |
|`log-format-upstream` |Set the nginx log format.The available fields can be found in [Embedded Variables](https://nginx.org/en/docs/http/ngx_http_upstream_module.html#variables). Example for json output:

```yaml
log-format-upstream: '{"time": "$time_iso8601", "remote_addr": "$proxy_protocol_addr", "x_forwarded_for": "$proxy_add_x_forwarded_for", " request_id": "$req_id",
  "remote_user": "$remote_user", "bytes_sent": $bytes_sent, "request_time": $request_time, "status": $status, "vhost": "$host", "request_proto ": "$server_protocol",
  "path":"$uri", "request_query":"$args", "request_length": $request_length, "duration": $request_time, "method":"$request_method", "http_ referrer": "$http_referer",
  "http_user_agent": "$http_user_agent" }'
```
