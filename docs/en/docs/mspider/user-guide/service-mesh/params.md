# Parameter Description for Creating Mesh

## Max Retries

The service mesh embeds Envoy components, and some parameters related to Envoy can be set when [creating the mesh](./README.md).
For more details, please refer to the [Envoy documentation](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/router_filter#x-envoy-retry-on).

### HTTP

- `5xx`

    If the upstream server responds with any 5xx response code, or doesn't respond at all (connection closed/reset/read timeout), a retry will be attempted (including connect-failure and refused-stream).

- `connect-failure`

    If a request fails due to connection failure with the upstream server (such as connection timeout), a retry will be attempted (included in 5xx).

- `envoy-ratelimited`

    If the header x-envoy-ratelimited is present, Envoy will retry.

- `gateway-error`

    This policy is similar to the 5xx policy, but only retries requests that result in a 502, 503, or 504 error.

- `http3-post-connect-failure`

    If a request is sent to the upstream server via HTTP/3 and fails after connecting, a retry will be attempted.

- `refused-stream`

    If the upstream server resets the stream with the REFUSED_STREAM error code, a retry will be attempted.
    This reset type indicates that the request can be safely retried (included in 5xx).

- `reset`

    If the upstream server doesn't respond at all (connection closed/reset/read timeout), a retry will be attempted.

- `retriable-4xx`

    If the upstream server responds with a retriable 4xx response code, a retry will be attempted.
    Currently, the only response code in this category is 409.

    Note: be careful when enabling this retry type. In some cases, 409 may indicate that an optimistic locking revision needs to be updated.
    Therefore, the caller should not retry and should read and then attempt write instead. If a retry occurs in this situation, it will always fail and return another 409.

- `retriable-headers`

    If any header in the upstream server response matches a retry policy or the x-envoy-retriable-header-names header, a retry will be attempted.

- `retriable-status-codes`

    If the upstream server responds with any response code that matches a retry policy or is defined in the x-envoy-retriable-status-codes header, a retry will be attempted.

### gRPC

- `cancelled`

    If the gRPC status code in the response header is "cancelled", a retry will be attempted.

- `deadline-exceeded`

    If the gRPC status code in the response header is "deadline-exceeded", a retry will be attempted.

- `internal`

    If the gRPC status code in the response header is "internal", a retry will be attempted.

- `resource-exhausted`

    If the gRPC status code in the response header is "resource-exhausted", a retry will be attempted.

- `unavailable`

    If the gRPC status code in the response header is "unavailable", a retry will be attempted.

## Sidecar Log Level

- `critical`

    Any errors that force the service or application to shut down to prevent data loss (or further data loss).
    These are reserved for the most egregious errors and situations where data corruption or loss is guaranteed.

- `debug`

    Using `debug`, you provide diagnostic information in a verbose manner.
    It's lengthy and contains more information than you need while using the application.
    The `debug` log level is used to get information needed to diagnose, troubleshoot, or test the application. This ensures the smooth operation of the application.

- `error`

    Unlike the `critical` log level, errors don't mean your application is aborting.
    Instead, it just can't access a service or file. This `error` indicates that something important in your application has failed.
    This log level is used when serious issues cause the functionality within the application to not work effectively. Most of the time, the application will continue to run but eventually needs this issue resolved.

- `info`

    General information to be logged (service start/stop, configuration assumptions, etc.).
    This is information that you want always available but typically don't care about in normal situations. This is the out-of-the-box configuration level.

- `off`

    This log level doesn't log anything. The `off` level is used to turn off logging and is the highest possible level.
    Using this log level, nothing is recorded at all.

- `trace`

    The `trace` log level captures all detailed information about application behavior. It's primarily diagnostic and more granular than the `debug` log level.
    This log level is used for situations where you need to see what's happening in your application or in third-party libraries used. You can use the `trace` log level to query parameters in your code or interpret algorithmic steps.

- `warning`

    When unexpected application issues are detected, the `warning` log level will be used.
    This means that you aren't quite sure if the problem will happen again or still exists. At this point, you might not notice any harm to your application.
    This issue is usually a case where a specific process has stopped running. But that doesn't mean that the application has been damaged.
    In fact, the code should continue to work as usual. You should eventually investigate these warnings to prevent the problem from happening again.
