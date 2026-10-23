# Common 503 Errors in Service Mesh

This page describes common 503 error scenarios in the service mesh and their solutions.

## Occasional 503

### Using Custom Metrics Where a Few 503 Errors Appear in Log Monitoring Whenever the Configuration Changes

#### Problem Cause

The logic of the custom metrics feature is to update the configuration of `istio.stats` by generating a corresponding EnvoyFilter.
This configuration takes effect at the Envoy Listener level, that is, it takes effect through LDS synchronization. When Envoy applies a Listener-level configuration,
it needs to disconnect existing connections. The corresponding in-flight requests return 503 because the connection is reset or closed.

#### Solution

When the upstream server actively closes the connection, the 503 you see is not sent by the upstream server, but is a response returned locally by the client sidecar because the upstream connection was actively disconnected.

The default retry configuration of Istio does not include "the upstream server actively closes the connection". Among the retry conditions of EnvoyProxy,
`reset` matches the trigger condition for this case. Therefore, you need to configure a retry policy for the route of the corresponding service.
The retry policy configured under the VirtualService includes the trigger condition `reset`.

The configuration example is as follows. This configuration only takes effect for the Ratings service.

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: ratings-route
spec:
  hosts:
    - ratings.prod.svc.cluster.local
  http:
    - route:
        - destination:
            host: ratings.prod.svc.cluster.local
            subset: v1
      retries:
        attempts: 2
        retryOn: connect-failure,refused-stream,unavailable,cancelled,retriable-status-codes,reset,503
```

#### Related FAQs

**Why does the default retry mechanism of Istio not take effect?**

The conditions under which the default retry of Istio occurs are as follows. By default, it retries 2 times. This scenario is not among the retry conditions, so it does not take effect.

```yaml
"retry_policy":
  {
    "retry_on": "connect-failure,refused-stream,unavailable,cancelled,retriable-status-codes",
    "num_retries": 2,
    "retry_host_predicate":
      [{ "name": "envoy.retry_host_predicates.previous_hosts" }],
    "host_selection_retry_max_attempts": "5",
    "retriable_status_codes": [503],
  }
```

- **connect-failure**: The connection failed.
- **refused-stream**: The HTTP2 stream returns the `REFUSED_STREAM` error code.
- **unavailable**: The gRPC request returns the `unavailable` error code.
- **cancelled**: The gRPC request returns the `cancelled` error code.
- **retriable-status-codes**: The `status_code` returned by the request matches the error code defined in the `retriable_status_codes` configuration.

For the complete retry conditions of the latest version of EnvoyProxy, see the following documents.

- Existing retry condition configuration for HTTP (including HTTP2 and HTTP3):
  [Router](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/router_filter#x-envoy-retry-on)
- Retry condition configuration specific to gRPC:
  [x-envoy-retry-grpc-on](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/router_filter#config-http-filters-router-x-envoy-retry-grpc-on)

### Occasional 503 Without Regularity and Without Configuration Changes During the Process

503 appears occasionally, but it appears continuously when the traffic is intensive. It usually appears on the Inbound side of the sidecar.

#### Problem Cause

The idle connection keep-alive time of Envoy does not match that of the application. The default Envoy idle connection time is 1 hour.

- The Envoy idle connection time is too long while that of the application is relatively short:

    The application has ended the idle connection, but Envoy thinks it has not ended. If there is a new connection at this time, a 503UC will be reported.

- The Envoy idle connection time is too short while that of the application is relatively long:

    This case will not cause a 503. Envoy thinks the previous connection has been closed, so it directly creates a new connection.

#### Solution

**Solution 1: Configure idleTimeout in the DestinationRule**

The cause of this problem is that idleTimeout does not match, so configuring idleTimeout in the DestinationRule is a relatively fundamental solution.

If idleTimeout is configured, it takes effect on both the Outbound and Inbound sides, that is, the Sidecar on both the Outbound and Inbound sides
will have the idleTimeout configuration. If the client has no Sidecar, idleTimeout will also take effect and can effectively reduce 503s.

Configuration suggestion: This configuration is related to the business. If it is too short, the number of connections will be too high. It is recommended that you configure it slightly shorter than the real idleTimeout of the business application.

**Solution 2: Configure retries in the VirtualService**

Retries will re-establish the connection and can solve this problem. For details, see the solution in [Scenario 1](#using-custom-metrics-where-a-few-503-errors-appear-in-log-monitoring-whenever-the-configuration-changes).

!!! important

    This operation is a non-idempotent request, and retries carry great risks. Please proceed with caution.

### Related to Sidecar Lifecycle

#### Problem Cause

It is caused by the lifecycle of the sidecar and the business container, and often occurs when a Pod is restarted.

#### Solution

For details, see [Sidecar Lifecycle](./sidecar-lifecycle.md).

## Guaranteed 503

### Application Listens on localhost

#### Problem Cause

When an application in the cluster listens on the localhost network address, since localhost is a local address, other Pods in the cluster cannot access it normally.

#### Solution

You can solve this problem by exposing the application service externally. For details, see [How to Make an Application Listening on localhost in a Cluster Accessible by Other Pods](./localhost-by-pod.md).

### Health Check Always Fails with a 503 Error After Enabling the Sidecar

#### Problem Cause

After mTLS is enabled in the service mesh, the health check request sent by kubelet to the Pod is intercepted by the sidecar, and kubelet does not have the corresponding TLS certificate, which causes the health check to fail.

#### Solution

You can solve this problem by configuring the port so that the health check traffic bypasses the sidecar proxy.
