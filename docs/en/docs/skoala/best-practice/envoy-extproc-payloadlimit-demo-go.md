# Cloud-Native Custom Plugin Example: envoy-extproc-payloadlimit-demo-go

[Envoy-extproc-payloadlimit-demo-go](https://github.com/projectsesame/envoy-extproc-payloadlimit-demo-go)
is an example based on [envoy-extproc-sdk-go](https://github.com/wrossmorrow/envoy-extproc-sdk-go)
that demonstrates how to use Envoy's
[ext_proc](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/ext_proc_filter) feature in Go.

## Functionality

Its main functionality is to review the size of the request body submitted by the Downstream before
routing it to the Upstream. If the request body exceeds the allowed maximum size, it will directly
respond with a 413 status code to limit the request body size.

## Prerequisites

- Install Envoy (Version >= v1.29)
- Install Go (Version >= v1.21). This step can be skipped if you are only running the project.
- A target service supporting HTTP Method: POST (hereinafter referred to as Upstream),
  which is assumed to support the following routes:

    - `/*`
    - `/no-extproc`

## Compilation

Enter the project root directory (can be skipped if you are only running the project).

```bash
go build . -o extproc
```

## Running

- Envoy

    ```bash
    envoy -c ./envoy.yaml # (1)!
    ```

    1. This file is located in the project root directory.

- Caching

    - Bare Metal

        ```bash
        ./extproc payload-limit --log-stream --log-phases payload-limit 32
        ```

    - K8s

        ```bash
        kubectl apply -f ./deployment.yaml # (1)!
        ```

        1. This file is located in the project root directory.

- curl

    ```bash
    curl -XPOST 127.0.0.1:8000/no-extproc  # (1)!
    ```

    1. The payload-limit does not apply to this route; the request will be routed to Upstream regardless of the request body size.

    For example, using the command-line parameter **payload-limit 32**:

    ```bash
    curl -XPOST  -H "Content-Type: application/json" -d '{"key1":"value1", "key2":"value2"}' 127.0.0.1:8000/bar
    ```

    If the request body is smaller than 32 bytes, it will be normally routed to Upstream.
    Otherwise, Payload-limit will directly respond with status code 413.

## Parameter Explanation

- log-stream: Whether to output logs about the request/response stream.
- log-phases: Whether to output logs for each processing phase.
- update-extproc-header: Whether to add the name of this plugin in the response header.
- update-duration-header: Add the total processing time in the response header at the end of the stream.

**All the above parameters default to false.**

- payload-limit 32: The maximum allowed length for the request body is 32 bytes.

## Notes

1. The first four command-line parameters are global configuration parameters, meaning all plugins based on
   [envoy-extproc-sdk-go](https://github.com/wrossmorrow/envoy-extproc-sdk-go) will support them by default.
   The **payload-limit 32** is a specific parameter for the plugin (envoy-extproc-payloadlimit-demo-go)
   and is parsed and used by this plugin.

2. The **request_body_mode** option in the processing_mode configuration must be set
   as shown in the red box in the figure below:

    ![Add Custom Attribute](../images/payloadlimit-demo-go.png)
