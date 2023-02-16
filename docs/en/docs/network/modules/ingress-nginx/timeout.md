---
MTPE: Jeanine-tw
Revised: Jeanine-tw
Pics: N/A
Date: 2023-02-08
---

# Configure timeout

This page describes the global timeout configuration for Ingress Nginx and the timeout configuration available for specific Ingress resources.

## Configure the global timeout

The global timeout for Ingress Nginx can be configured using the following configuration options .

|option's name|description|default|
|---- |---- | --- |--|
|`proxy-connect-timeout`| Set the timeout for establishing a connection with a proxied server. |The default is `5s`, but it cannot usually exceed  `75s` |
|`proxy-read-timeout`| Set the timeout for reading a response from the proxied server. This timeout is only set between two consecutive read operations, not for the entire transmission of the response. |`60s`|
|`proxy-send-timeout`| Set the timeout for transmitting a request to the proxied server.  This timeout is only set between two consecutive write operations, not for the entire transmission of the request. |`60s`|
|`proxy-stream-next-upstream-timeout`| Limit the time allowed to pass the connection to the next server. |The default is `600s`,  and `0s` will disable this limit. |
|`proxy-stream-timeout`|Set the timeout between two consecutive read or write operations on a client or proxy server connection. If no data is transferred within this time, the connection will be closed.|`600s`|
|`upstream-keepalive-timeout`|Set a timeout during which a keep-alive client connection will stay open. | `60`|
|`worker-shutdown-timeout`|Set a graceful shutdown timeout. |`240s`|
|`proxy-protocol-header-timeout`| Set the timeout for receiving proxy protocol headers. The default of 5 seconds prevents TLS direct handlers from waiting indefinitely for a broken connection. |`5s`|
|`ssl-session-timeout`| Sets the valid time for session parameters in the SSL session cache. The session expiration time is relative to the creation time. Each session cache will take up about 0.25MB. |`10m`|
|`client-body-timeout`|Set the timeout for reading a client request body. |`60s`|
|`client-header-timeout`|Defines the timeout for reading a client request header. |`60s`|

## Configure custom timeout

The following are custom timeout configurations, and associated parameter configurations, such as the number of retries, etc:

|option's name|description|
| ---- |---- |
|`nginx.ingress.kubernetes.io/proxy-connect-timeout`| Set the timeout for establishing a connection with a proxied server. |
|`nginx.ingress.kubernetes.io/proxy-send-timeout`| Set the timeout for transmitting a request to the proxied server. |
| `nginx.ingress.kubernetes.io/proxy-read-timeout` | Set the timeout for reading a response from the proxied server. |
|`nginx.ingress.kubernetes.io/proxy-next-upstream`|Set retry policies or retry conditions with multiple combinations separated by spaces, such as `http_500 http_502`, which supports the following policies: <ul> <li>`error`: fail to establish a connection and return directly</li><li>`timeout`: the connection times out and returns directly</li><li>`invalid_response`: invalid return status code and return directly</li ><li>`http_xxx`: xxx can be replaced by a status code. For example, if it is set to `http_500`, it means that the next workload is selected when the upstream returns 500. The supported status codes include: `500`, `502`, `503`, `504`, `403`, `404`, `429`</li><li>`off`: disable the retry mechanism, regardless of Any error returns directly</li></ul>|
|`nginx.ingress.kubernetes.io/proxy-next-upstream-tries`| The number of retries available if the retry condition is met. |
|`nginx.ingress.kubernetes.io/proxy-request-buffering`| Enable request buffering. Set to `on` to enable request buffering, `off` to disable a request buffering. If enabled, full request data is received before being forwarded to the backend workload, otherwise requests may be forwarded when partial request data is received. HTTP/1.1 Chunked encoded requests are not limited by this parameter and will always be buffered. If disabled, the next workload will not be selected for retry when a sending error occurs during sending. |
