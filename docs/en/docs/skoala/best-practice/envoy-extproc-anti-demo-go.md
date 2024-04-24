---
MTPE: windsonsea
Date: 2024-04-24
---

# Cloud Native Custom Plugin Demo: envoy-extproc-anti-replay-demo-go

[Envoy-extproc-anti-replay-demo-go](https://github.com/projectsesame/envoy-extproc-anti-replay-demo-go)
is an example of how to use the
[ext_proc](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/ext_proc_filter)
feature provided by Envoy in Go language, implemented based on
[envoy-extproc-sdk-go](https://github.com/wrossmorrow/envoy-extproc-sdk-go).

## Features

Its main function is to verify the sign, timestamp, and nonce of the request submitted by Downstream
before routing it to Upstream. If any of the verifications fail, it will directly respond with 401 to
prevent replay attacks.

## Prerequisites

- Install Envoy (Version >= v1.29)
- Install Go (Version >= v1.21), can be skipped if only running
- Upstream service that supports HTTP Method: POST (referred to as Upstream),
  assuming it supports the following routes:
  
    - `/*`
    - `/no-extproc`

## Compilation

Go to the root directory of the project (this step can be skipped if only running).

```bash
go build . -o extproc
```

## Execution

- Envoy:

    ```bash
    envoy -c ./envoy.yaml # This file is located in the root directory of the project.
    ```

- Caching:

    - Bare Metal:

        ```bash
        ./extproc anti-replay --log-stream --log-phases timespan "900"
        ```

    - Kubernetes:

        ```bash
        kubectl apply -f ./deployment.yaml # This file is located in the root directory of the project.
        ```

- Curl

    ```bash
    curl --request POST \
        --url http://127.0.0.1:8080/ \
        --data '{
        "key": "value",
        "key2": "",
        "sign": "659876b30987883efdf178e69f062896",
        "nonce": "6062",
        "timestamp": "1712480920"
        }'
    ```

!!! note "Parameters"

    - log-stream: Whether to output logs about the request/response stream.
    - log-phases: Whether to output logs for each processing phase.
    - update-extproc-header: Whether to add the name of this plugin to the response header.
    - update-duration-header: Add the total processing time to the response header when the stream ends.

    **All of the above parameters default to false.**

    - timespan 900: The time span (in seconds) of the request.

## Notes

1. The first 4 command-line arguments in this example are global configuration parameters,
   which are supported by all plugins implemented based on
   [envoy-extproc-sdk-go](https://github.com/wrossmorrow/envoy-extproc-sdk-go) by default.
   The **timespan 900** is a specific parameter for the plugin (envoy-extproc-anti-replay-demo-go)
   and is parsed and used by this plugin.

2. In this example, MD5 is used as the "signature" algorithm for demonstration purposes only.
   Please use algorithms like SHA256WithRSA in production.

3. The following 3 fields are **required** for each request:

    - **sign**: Calculated as `MD5(k1=v1&k2=v2...kN=vN)`, the original string is
      sorted in ascending order of keys and ignores key-value pairs with empty values.

        ```text
        eg: sign = MD5("key=value&nonce=6062&timestamp=1712480920") = 659876b30987883efdf178e69f062896
        ```

    - **nonce**: The same nonce can only be used once within the time span.
    - **timestamp**: The current time in seconds.

4. The **request_body_mode** in the processing_mode configuration must be configured as
   the option in the red box in the **following image**:

    ![Add custom attributes](../images/envoy-extproc-anti-replay-demo-go.png)
