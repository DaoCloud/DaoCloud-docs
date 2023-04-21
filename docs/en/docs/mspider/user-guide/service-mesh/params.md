# Parameters in creating mesh

This page explains those fields when you create a mesh.

## Max retries

### HTTP

- `5xx`

    Envoy will attempt a retry if the upstream server responds with any 5xx response code, or does not respond at all (disconnect/reset/read timeout). (Includes connect-failure and refused-stream)

    NOTE: Envoy will not retry when a request exceeds x-envoy-upstream-rq-timeout-ms (resulting in a 504 error code). Use x-envoy-upstream-rq-per-try-timeout-ms if you want to retry when individual attempts take too long. x-envoy-upstream-rq-timeout-ms is an outer time limit for a request, including any retries that take place.

- `connect-failure`

    Envoy will attempt a retry if a request is failed because of a connection failure to the upstream server (connect timeout, etc.). (Included in 5xx)

    NOTE: A connection failure/timeout is the TCP level, not the request level. This does not include upstream request timeouts specified via x-envoy-upstream-rq-timeout-ms or via route configuration or via virtual host retry policy.

- `envoy-ratelimited`

    Envoy will retry if the header x-envoy-ratelimited is present.

- `gateway-error`

    This policy is similar to the 5xx policy but will only retry requests that result in a 502, 503, or 504.

- `http3-post-connect-failure`

    Envoy will attempt a retry if a request is sent over HTTP/3 to the upstream server and failed after getting connected.

- `refused-stream`

    Envoy will attempt a retry if the upstream server resets the stream with a REFUSED_STREAM error code. This reset type indicates that a request is safe to retry. (Included in 5xx)

- `reset`

    Envoy will attempt a retry if the upstream server does not respond at all (disconnect/reset/read timeout.)

- `retriable-4xx`

    Envoy will attempt a retry if the upstream server responds with a retriable 4xx response code. Currently, the only response code in this category is 409.

    NOTE: Be careful turning on this retry type. There are certain cases where a 409 can indicate that an optimistic locking revision needs to be updated. Thus, the caller should not retry and needs to read then attempt another write. If a retry happens in this type of case it will always fail with another 409.

- `retriable-headers`

    Envoy will attempt a retry if the upstream server response includes any headers matching in either the retry policy or in the x-envoy-retriable-header-names header.

- `retriable-status-codes`

    Envoy will attempt a retry if the upstream server responds with any response code matching one defined in either the retry policy or in the x-envoy-retriable-status-codes header.

Refer to [Envoy documentation](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/router_filter#x-envoy-retry-on) for details.

### gRPC

- `cancelled`

    Envoy will attempt a retry if the gRPC status code in the response headers is “cancelled” (1)

- `deadline-exceeded`

    Envoy will attempt a retry if the gRPC status code in the response headers is “deadline-exceeded” (4)

- `internal`

    Envoy will attempt to retry if the gRPC status code in the response headers is “internal” (13)

- `resource-exhausted`

    Envoy will attempt a retry if the gRPC status code in the response headers is “resource-exhausted” (8)

- `unavailable`

    Envoy will attempt a retry if the gRPC status code in the response headers is “unavailable” (14)

## Sidecar log level

- critical

    Any error that is forcing a shutdown of the service or application to prevent data loss (or further data loss).
    You reserve these only for the most heinous errors and situations where there is guaranteed to have been data corruption or loss.

- debug

    With `debug`, you are giving diagnostic information in a detailed manner.
    It is verbose and has more information than you would need when using the application.
    `debug` logging level is used to fetch information needed to diagnose, troubleshoot,
    or test an application. This ensures a smooth running application.

- error

    Unlike the `critical` logging level, error does not mean your application is aborting.
    Instead, there is just an inability to access a service or a file. This `error` shows
    a failure of something important in your application. This log level is used when a
    severe issue is stopping functions within the application from operating efficiently.
    Most of the time, the application will continue to run, but eventually, it will need to be addressed.

- info

    Generally useful information to log (service start/stop, configuration assumptions, etc).
    Info you want to always have available but usually don't care about under normal circumstances.
    This is my out-of-the-box config level.

- off

    This log level does not log anything. This OFF level is used to turn off logging and is the greatest possible rank. With this log level, nothing gets logged at all.

- trace

    The `trace` log level captures all the details about the behavior of the application.
    It is mostly diagnostic and is more granular and finer than `debug` log level.
    This log level is used in situations where you need to see what happened in your application or
    what happened in the third-party libraries used. You can use the `trace` log level to query
    parameters in the code or interpret the algorithm’s steps.

- warning

    The `warning` log level is used when you have detected an unexpected application problem.
    This means you are not quite sure whether the problem will recur or remain. You may not
    notice any harm to your application at this point. This issue is usually a situation that
    stops specific processes from running. Yet it does not mean that the application has been
    harmed. In fact, the code should continue to work as usual. You should eventually check
    these warnings just in case the problem reoccurs.
