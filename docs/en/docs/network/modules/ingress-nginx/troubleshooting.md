# ingress-nginx Troubleshooting Guide

This page summarizes common ingress-nginx issues, how to inspect them, and suggested fixes, helping you quickly locate problems such as Ingress rules not taking effect, abnormal access behavior, or configuration not being applied.

## Troubleshooting Workflow

When an Ingress access issue occurs, we recommend checking the following in order:

1. Verify that `Ingress`, `Service`, `Endpoints`, and `Pod` resources are healthy.
2. Verify that the `IngressClass` is correct and watched by the target ingress-nginx instance.
3. Verify that the ingress-nginx `Service` exposes a reachable address for external traffic.
4. Check ingress-nginx Controller logs for configuration generation, certificate loading, or Webhook errors.
5. Check whether annotations, TLS, timeout, and forwarding settings are configured as expected.

## Useful Troubleshooting Commands

```bash
# View Ingress rules
kubectl get ingress -A
kubectl describe ingress <ingress-name> -n <namespace>

# View IngressClass
kubectl get ingressclass
kubectl describe ingressclass <ingressclass-name>

# View ingress-nginx controller status
kubectl get pods -n <ingress-nginx-namespace>
kubectl get svc -n <ingress-nginx-namespace>
kubectl logs -n <ingress-nginx-namespace> deploy/<ingress-nginx-controller>

# View backend Services and Endpoints
kubectl get svc -n <namespace>
kubectl get endpoints -n <namespace> <service-name>
kubectl get pod -n <namespace> -o wide

# View generated nginx configuration
kubectl exec -n <ingress-nginx-namespace> <controller-pod> -- nginx -T
```

## Ingress Does Not Take Effect

**Symptoms:**

- After creating the Ingress, requests do not reach the expected ingress-nginx instance.
- `kubectl describe ingress` does not show status handled by the expected controller.

**Troubleshooting steps:**

1. Check whether the Ingress specifies the correct `ingressClassName`.

    ```bash
    kubectl get ingress <ingress-name> -n <namespace> -o yaml
    kubectl get ingressclass
    ```

2. If `ingressClassName` is not specified, check whether there is a default `IngressClass` in the cluster.
3. Check whether `scope` is enabled in the ingress-nginx installation parameters. If enabled, confirm that the Ingress namespace is within the watched scope.
4. Check Controller logs for messages showing that the Ingress was ignored.

    ```bash
    kubectl logs -n <ingress-nginx-namespace> deploy/<ingress-nginx-controller> | grep <ingress-name>
    ```

**Suggested fixes:**

- Explicitly set the correct `ingressClassName` for the Ingress.
- If multiple ingress-nginx instances exist in the cluster, make sure `IngressClass`, `Election ID`, and `scope` settings do not conflict.
- If you want users to create Ingress resources without explicitly setting a class name, mark the target `IngressClass` as the default class.

## Cannot Access from Outside the Cluster

**Symptoms:**

- The domain name is not resolved to the ingress-nginx address.
- Requests to the external address time out, are refused, or cannot be opened in a browser.

**Troubleshooting steps:**

1. Check the ingress-nginx `Service` type and address.

    ```bash
    kubectl get svc -n <ingress-nginx-namespace>
    ```

2. If the `Service` type is `LoadBalancer`, check whether `EXTERNAL-IP` has been assigned.
3. If the `Service` type is `NodePort`, confirm that security groups, firewalls, and upstream load balancers allow the relevant ports.
4. Check whether DNS resolves to the correct VIP or node address.
5. Test access from inside the cluster to determine whether the issue is only external or affects the full traffic path.

    ```bash
    kubectl run -it --rm test-curl --image=curlimages/curl -- sh
    curl -H "Host: <your-host>" http://<ingress-service-ip>
    ```

**Suggested fixes:**

- In `LoadBalancer` scenarios, confirm that the underlying LB component works correctly, such as MetalLB or a cloud provider load balancer.
- In `NodePort` scenarios, make sure node-side networking and L4 forwarding rules are complete.
- If DNS is correct but access still fails, focus on the network path from external traffic to the ingress-nginx `Service`.

## Requests Return 404 or Reach the Default Backend

**Symptoms:**

- Requests reach ingress-nginx but return `404 Not Found`.
- Traffic falls through to the default backend instead of the target service.

**Troubleshooting steps:**

1. Check whether the request `Host` matches the Ingress `rules.host`.
2. Check whether the request path matches `path` and `pathType`.
3. Check whether multiple Ingress resources use the same host and path, causing conflicts or overrides.
4. Inspect the generated nginx configuration to confirm that the rule was rendered.

    ```bash
    kubectl exec -n <ingress-nginx-namespace> <controller-pod> -- nginx -T | grep -n "<your-host>"
    ```

**Suggested fixes:**

- Use `curl -H "Host: <your-host>" http://<address>/<path>` to simulate a real request header.
- Prefer `Prefix` for common routing scenarios if path matching behavior is unclear.
- If multiple teams share one domain, define path conventions in advance to avoid routing conflicts.

## Requests Return 503

**Symptoms:**

- The Ingress rule exists, but requests return `503 Service Temporarily Unavailable`.

**Troubleshooting steps:**

1. Check whether the backend `Service` name and port referenced by the Ingress are correct.

    ```bash
    kubectl describe ingress <ingress-name> -n <namespace>
    kubectl get svc <service-name> -n <namespace> -o yaml
    ```

2. Check whether `Endpoints` contain available addresses.

    ```bash
    kubectl get endpoints <service-name> -n <namespace>
    ```

3. Check whether backend Pods are ready and whether `readinessProbe` keeps failing.
4. Check whether the `Service` selector matches the expected Pods.

**Suggested fixes:**

- `503` usually means the request reached ingress-nginx, but no backend endpoints are currently available.
- First fix issues such as unready backend Pods, mismatched `Service` ports, or incorrect label selectors.
- If `503` happens intermittently, combine this with [Timeout](./timeout.md) settings and application logs for further analysis.

## Annotations or Configuration Do Not Take Effect

**Symptoms:**

- Ingress annotations are configured, but timeout, CORS, upload limit, or forwarding behavior does not change.

**Troubleshooting steps:**

1. Check annotation names, spelling, and value format.
2. Make sure the annotations are supported by ingress-nginx rather than another Ingress controller.
3. Check Controller logs for annotation parsing or configuration validation errors.
4. Check the final generated nginx configuration for the expected directives.

**Suggested fixes:**

- Follow the expected annotation format for booleans, numbers, and durations.
- When both global settings and Ingress-level annotations exist, verify precedence and override behavior.
- For logging, timeout, upload limit, or CORS, refer to:
  - [Logs](./log.md)
  - [Timeout](./timeout.md)
  - [Upload Limit](./upload.md)
  - [Cross-Origin](./cors.md)

## Admission Webhook Validation Fails

**Symptoms:**

- Creating or updating an Ingress returns an error similar to:

```text
admission webhook "validate.nginx.ingress.kubernetes.io" denied the request
```

**Troubleshooting steps:**

1. Check the Ingress YAML for invalid fields, duplicated paths, or malformed annotations.
2. Check whether the admission webhook Pod, Service, and certificate Secret are healthy.

    ```bash
    kubectl get pods,svc,secret -n <ingress-nginx-namespace>
    ```

3. Check webhook-related logs.
4. Verify network connectivity from the apiserver to the webhook Service.

**Suggested fixes:**

- First correct the Ingress definition itself, such as path conflicts or invalid annotation values.
- If the issue is caused by webhook certificates or components not being ready, re-check the ingress-nginx installation status.
- After cluster upgrades, migration, or recovery, pay special attention to expired webhook certificates or incorrect mounts.

## TLS Certificates Do Not Take Effect

**Symptoms:**

- HTTPS serves the wrong certificate, the browser reports an untrusted or mismatched certificate, or the default certificate is still returned.

**Troubleshooting steps:**

1. Check whether `spec.tls.hosts` matches `rules.host` in the Ingress.
2. Check whether the TLS Secret exists in the same namespace as the Ingress.

    ```bash
    kubectl get secret <tls-secret-name> -n <namespace>
    kubectl describe ingress <ingress-name> -n <namespace>
    ```

3. Confirm that the Secret type is `kubernetes.io/tls`.
4. Check Controller logs for certificate loading failures or certificate chain errors.

**Suggested fixes:**

- The certificate Secret, host name, and Ingress namespace must match.
- If the default certificate is returned, the target host usually did not match the expected TLS rule, or the certificate was not loaded successfully.

## Ingress Latency Fluctuates

**Symptoms:**

- The service becomes slow intermittently, with obvious spikes in P95 and P99 latency.
- Users experience unstable response time rather than a continuous outage.

**Troubleshooting approach:**

First determine whether the latency fluctuation comes from ingress-nginx itself or from the backend service.

1. Compare request latency in ingress-nginx access logs with processing latency in backend application logs.
2. If latency is already high on the ingress-nginx side, first inspect ingress-nginx resources and scheduling behavior.
3. If ingress-nginx forwarding latency is normal but backend processing time increases, focus on the backend service, database, or dependent components.

**Troubleshooting steps:**

1. Check CPU and memory usage of ingress-nginx Pods and see whether they are close to resource limits.

    ```bash
    kubectl top pod -n <ingress-nginx-namespace>
    kubectl describe pod <controller-pod> -n <ingress-nginx-namespace>
    ```

2. Check whether `resources.requests` and `resources.limits` in the ingress-nginx Deployment or Helm values are reasonable, especially whether the CPU limit is too low.
3. Check whether CPU throttling exists. If the CPU limit is too low, burst traffic can trigger CFS throttling and cause latency spikes even when average CPU usage does not look high.
4. Use monitoring to inspect metrics such as:

    - Pod CPU usage
    - Pod memory usage
    - CPU CFS throttled periods
    - CPU CFS throttled seconds
    - Nginx request latency, request volume, and status code distribution

5. Compare backend Service and Pod latency with their resource metrics.

    ```bash
    kubectl top pod -n <namespace>
    kubectl get endpoints <service-name> -n <namespace>
    ```

6. If you suspect ingress-nginx itself is slowing down, log in to the node or container and use tools such as `perf`, `top`, or `pidstat` to inspect hot functions, system calls, and context switching.

**Suggested fixes:**

- If the latency fluctuation is caused by ingress-nginx itself:
  - Increase CPU `requests/limits` for ingress-nginx Pods to avoid resource starvation or CFS throttling.
  - Check whether the number of Controller replicas is sufficient and scale out if needed.
  - Check whether the node has CPU contention, high load, or noisy neighbor issues.
  - If deeper analysis is needed, use `perf` to sample nginx worker processes or related processes.

- If the backend service is the main source of latency:
  - Inspect application processing time, database access, external dependency calls, and GC behavior.
  - Check for resource bottlenecks, thread pool queueing, or connection pool exhaustion in backend Pods.

## Logging Tips

We recommend checking both of the following:

- ingress-nginx Controller logs, to inspect configuration sync, certificate loading, Webhook behavior, and route generation issues.
- Backend service logs, to confirm whether the request was forwarded and whether the backend returned an application-level error.

If you need deeper request-path analysis, you can temporarily adjust logging settings. See [Logs](./log.md).
