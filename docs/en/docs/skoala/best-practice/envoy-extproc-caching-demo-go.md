# Cloud Native Custom Plugin Example: envoy-extproc-caching-demo-go

[Envoy-extproc-method-conv-demo-go](https://github.com/projectsesame/envoy-extproc-method-conv-demo-go) is an example that demonstrates how to use the [ext_proc](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/ext_proc_filter) feature provided by Envoy in Go language, based on [envoy-extproc-sdk-go](https://github.com/wrossmorrow/envoy-extproc-sdk-go).

## Functionality

The main functionality is to use a non-persistent storage to cache the responses of GET requests initiated by the Downstream. The first request for a specific path will be responded by the Upstream and cached by the Caching. All subsequent requests for this path will be directly responded by the Caching without routing to the Upstream, until the Caching is restarted. This achieves the purpose of response caching.

## Prerequisites

- Install Envoy (Version >= v1.29)
- Install Go (Version >= v1.21) (Skip this step if only running)
- Target service (referred to as Upstream) that supports HTTP Method: GET and assumes that it supports the following routes:

    ```console
    /*
    /no-extproc
    ```

## Compilation

Go to the root directory of the project (Skip this step if only running).

```go
go build . -o extproc
```

## Running

Envoy:

```bash
envoy -c ./envoy.yaml # This file is located in the root directory of the project.
```

Caching:

- Bare Metal

    ```bash
    ./extproc caching --log-stream --log-phases
    ```

- Kubernetes

    ```bash
    kubectl apply -f ./deployment.yaml # This file is located in the root directory of the project.
    ```

Curl:

```bash
curl 127.0.0.1:8000/no-extproc  # Caching will not be applied to this route, each request will be responded by the Upstream
curl 127.0.0.1:8000/abc  # The first request will be responded by the Upstream and cached by the Caching. Subsequent requests for /abc will be directly responded by the Caching.
```

## Parameter Explanation

- log-stream: Whether to output logs about the request/response stream
- log-phases: Whether to output logs for each processing phase
- update-extproc-header: Whether to add the name of this plugin in the response header
- update-duration-header: Whether to add the total processing time in the response header

**The above parameters are all false by default.**

- payload-limit 32: The maximum allowed length of the request body is 32 bytes

## Notes

1. This example only supports HTTP Method: GET.

2. The configuration options in the processing_mode, including request_header_mode and response_body_mode, must be configured as the options highlighted in the red box in the **figure below**.

    ![Add Custom Attributes](../images/envoy-extproc-caching-demo-go.png)