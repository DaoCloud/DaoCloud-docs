# Traffic Lane

The Traffic Lane feature is used to implement **fine-grained traffic routing control** in scenarios such as multi-version and grayscale release.
The core of this mechanism relies on the following three key elements:

- **Wasm extension module**: Injects a custom header (such as `x-mspider-lane`) into requests between services to identify the lane to which a request belongs.
- **TraceID tracing information**: Helps identify the origin of a request and provides context support for lane routing.
- **Istio routing configuration**: Implements lane-level traffic distribution based on headers through VirtualService (VS) and DestinationRule (DR).

## Scenario Example

### System Request Link

```yaml
bookinfo-gw (Istio gateway)
    ↓
productpage
    ↓
details & reviews...
```

Each hop of the service in this link has been integrated with the Istio sidecar and supports subset routing based on headers.

### Lane Planning Strategy

- Define two lanes: `green` and `yellow`
- Use the header key: `x-mspider-lane` (the lane identifier field)
- Default lane value: `green`

### Expected Routing Behavior

| Request Header Example | Expected Routing Target Subset |
| --------------- | ------------- |
| x-mspider-laneid: green | green |
| x-mspider-laneid: yellow | yellow |

- When a request arrives, Istio routes the traffic to the corresponding subset of Pods based on the lane identifier in the header.
- If the header is missing, the system can be configured with a default value or return an error, depending on the VS/DR policy.

### Header Rewrite Description

Because the upstream service may use the `x-mspider-laneid` field, while the standard field recognized internally by the system is `x-mspider-lane`,
it is recommended to add the following configuration to the VirtualService of the ingress gateway (such as `istio-cars-ingress`):

```yaml
http:
- match:
    ...
  headers:
    request:
      set:
        x-mspider-lane: "{{ request.headers['x-mspider-laneid'] }}"
```

!!! note

    The above operation maps `x-mspider-laneid` to the standard lane identifier `x-mspider-lane`. It is only needed when the upstream request header is inconsistent; if it has already been unified as `x-mspider-lane`, you can skip this step.

## Example Operation Steps

### 1. Enable the Mesh Tracing Feature

![img](./images/lane01.png)

### 2. Define the Traffic Lane Matching Header with a wasm plugin

```yaml
apiVersion: extensions.istio.io/v1alpha1
kind: WasmPlugin
metadata:
  name: bookinfo
  namespace: bookinfo
spec:
  imagePullPolicy: Always
  phase: STATS
  pluginConfig:
    cache_size: 1024
    lane_header: x-mspider-lane # Common header key recognized by the traffic lane
    traffic_lane: green # Default header value of the lane
    type: W3C
  selector:
    matchLabels:
      app: bookinfo # Common label of the workloads the lane applies to
  url: oci://release.daocloud.io/mspider/mspider-traffic-lane:v0.30.4 # Lane version
```

If you are in a private environment, remember to push the lane Wasm to the container registry in advance.

### 3. Service Check

- Port protocol configuration. **The port protocol definition must be correct**
- Whether the service is correctly bound to multi-version workloads
- Inject the sidecar
- Whether the service is running normally (in the Service List UI)

![img](./images/lane02.png)

### 4. Define the dr of the service, and configure both green and yellow subsets for each service

To confirm whether the target service is bound, you can use the service mesh UI as a reference.

![img](./images/lane03.png)

### 5. Define the vs routing rules for the north-south gateway

The gateway needs to rewrite the header.

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: bookinfo-gw
  namespace: bookinfo
spec:
  gateways:
    - bookinfo/bookinfo-gw # Gateway ingress service
  hosts:
    - '*'
  http:
    - headers: # Reset the request header to the common traffic lane header rule <x-mspider-lane: green>
        request:
          set: # Rewrite
            x-mspider-lane: green
      match: # Access the service, for example, an ingress HTTP request (postman) needs to define the header <green>
        - headers:
            x-mspider-laneid:
              exact: green
      name: green-lane
      route:
        - destination:
            host: productpage
            port:
              number: 9080
            subset: green
    - headers:
        request:
          set:
            x-mspider-lane: yellow
      match:
        - headers:
            x-mspider-laneid:
              exact: yellow
      name: yellow-lane
      route:
        - destination:
            host: productpage
            port:
              number: 9080
            subset: yellow
```

If you do not need to rewrite the header, here is an example:

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: bookinfo-gw
  namespace: bookinfo
spec:
  gateways:
    - bookinfo/bookinfo-gw # Gateway ingress service
  hosts:
    - '*'
  http:
    - match: # Access the service, for example, an ingress HTTP request (postman) needs to define the header <green>
        - headers:
            x-mspider-lane:
              exact: green
      name: green-lane
      route:
        - destination:
            host: productpage
            port:
              number: 9080
            subset: green
    - match:
        - headers:
            x-mspider-lane:
              exact: yellow
      name: yellow-lane
      route:
        - destination:
            host: productpage
            port:
              number: 9080
            subset: yellow
```

### 6. Define the VirtualService for subsequent internal services

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: details
  namespace: bookinfo
spec:
  gateways:
    - mesh # Global service
  hosts:
    - details # Internal service
  http:
    - match: # Match the common header rule of the lane
        - headers:
            x-mspider-lane:
              exact: green
      name: green
      route:
        - destination:
            host: details
            port:
              number: 9080
            subset: green
    - match:
        - headers:
            x-mspider-lane:
              exact: yellow
      name: yellow
      route:
        - destination:
            host: details
            port:
              number: 9080
            subset: yellow
```

## Common Issue Records

### Service Inaccessible Due to a Wrong VS Port

**The target port of the VS is selected incorrectly.** The services above both have an http and a grpc port. Internal calls of the services use grpc, but the http port is selected by default, which causes abnormal requests.

### no healthy upstream - Workload Matching Issue

Error 1: The label match in the DR subset is incorrect, so the Pod cannot be found.

Error 2: **The service and the workload do not correspond correctly**, so the corresponding Pod cannot be found. You can check the correspondence between the service and the workload in the Service List of the service mesh UI.

### Service Access Error Caused by Tracing Not Being Enabled

The symptom is that istio-proxy has an incoming header, but there is no traceid.
The request header `x-mspider-lane` seen in the business logs should normally be:

![img](./images/lane05.png)
