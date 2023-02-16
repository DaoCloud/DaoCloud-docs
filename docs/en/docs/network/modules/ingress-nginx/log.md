# Logging Configuration

This article explains the logging options that can be configured in the global settings of Ingress Nginx, such as log output path, log format, log level, and other options.

`access-log-path` is used to set the location of the access log. The default location is `/var/log/nginx/access.log`, which is a symbolic link to `/dev/stdout`. It is recommended to output logs to stdout for convenient log collection on container platforms.

`error-log-path` is used to set the location of the error log. The default location is `/var/log/nginx/error.log`, which is a symbolic link to `/dev/stderr`. It is recommended to output logs to stderr for convenient log collection on container platforms.

`disable-access-log` disables the output of the access log.

`http-access-log-path` and `stream-access-log-path` control the logging of HTTP and stream, respectively. The default value is `""`, which means the value of `access-log-path` is used.

`enable-access-log-for-default-backend` enables logging for the default backend. The default value is `false`.

`error-log-level` sets the level of the error log. Supported values are `debug`, `info`, `notice`, `warn`, `error`, `crit`, `alert`, `emerg`, with the default value of notice. The log levels are ordered in increasing severity, for example, level `crit` will cause `crit`, `alert`, and `emerg` messages to be logged.

`log-format-escape-none` controls whether characters in variables are escaped (`true`) or controlled by `log-format-escape-json` (`false`) when setting the Nginx log format.

`log-format-escape-json` escapes rendered values when the output format is JSON. The default value is `false`.

log-format-upstream sets the Nginx log format, and the available fields can be found in Embedded Variables. Here is an example that sets the format to JSON output:

```yaml
log-format-upstream: '{"time": "$time_iso8601", "remote_addr": "$proxy_protocol_addr", "x_forwarded_for": "$proxy_add_x_forwarded_for", "request_id": "$req_id",
  "remote_user": "$remote_user", "bytes_sent": $bytes_sent, "request_time": $request_time, "status": $status, "vhost": "$host", "request_proto": "$server_protocol",
  "path": "$uri", "request_query": "$args", "request_length": $request_length, "duration": $request_time,"method": "$request_method", "http_referrer": "$http_referer",
  "http_user_agent": "$http_user_agent" }'
```

`log-format-stream` sets the logging output format for Nginx stream.

`skip-access-log-urls` filters the list of URLs that appear in the NGINX access log. A best practice is to filter out health check URLs like `/health`, which can make reading the logs more complicated. The default is not set.

`enable-syslog` logs to syslog, with a default value of false.
* `syslog-host` sets the address of the syslog server, which can be specified as a domain name or IP address.
* `syslog-port` sets the port of the syslog server, with a default value of `514`.