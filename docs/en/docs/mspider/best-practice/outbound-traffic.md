# How to Choose an Outbound Traffic Policy

With the wide application of service mesh in microservice architectures, how to effectively manage and govern access to external services has become a key issue.
This guide introduces how to manage access from services inside the mesh to external services in an Istio environment.

!!! note

    External service: generally refers to services outside the service mesh, services in a cluster without an injected sidecar, and services outside the cluster.

## Preface

In a service mesh, the outbound traffic policy supports two forwarding modes:

- Registered services: The sidecar only forwards outbound traffic destined for registered services or services registered in a service entry (default).
- All services: The sidecar forwards all outbound traffic.

When the forwarding mode is configured as `registered services`, you can work with `Egress` to achieve fine-grained management.

## Fine-Grained Management with Egress

**Egress traffic** refers to the network traffic sent from inside the service mesh to external services. In Istio,
by configuring an **Egress policy**, you can control and manage this outbound traffic, including which services can access external resources, how they access them, and which specific external services they access.

With a fine-grained Egress traffic governance policy, O&M personnel can effectively manage the access of services inside the mesh to external services, improve security, and reduce unnecessary network overhead.

Example: [Restrict Service Access with Mesh](./use-egress-and-authorized-policy.md)

## Open All Services

In a complex network structure, services in a cluster often need to access various external services, such as third-party APIs, databases, and message queues.
If the outbound network policy is set too strictly, the cost of troubleshooting and O&M may increase.
When accessing external resources, services may need additional configuration, or access may fail when the network is restricted.

### Recommendations for the Outbound Traffic Policy

To solve the above problems, it is recommended to set the outbound traffic policy reasonably according to actual needs.

#### Allow Access to All External Services

![image](../images/outbound-traffic-01.png)

If your application has no strict access restrictions on external services, you can set the outbound traffic policy of the mesh to **Allow access to all external services**.
In this way, services with an injected **sidecar** in the mesh do not need complex configuration when they need to access external services, which reduces the complexity of O&M.

**Sidecar**: In a service mesh, a sidecar is a special proxy (usually an Envoy proxy) that runs together with the application container.
It intercepts and processes the inbound and outbound traffic of the service, implementing the observability and control capabilities of the service network.

#### Optimization for Specific Protocols

For common HTTP/HTTPS external services, allowing all services is usually sufficient. However,
for database services such as **MySQL** and **Redis** that need to maintain long connections, going through the sidecar proxy may introduce a certain performance loss.
The reason is that the sidecar proxy needs to parse and process every request, while long-connection protocols are more sensitive to latency and connection stability.

For this reason, it is recommended to enable the **Pass-Through** mode for this outbound traffic that needs long connections in the sidecar governance policy, so as to bypass the sidecar proxy directly and reduce the performance impact.

**Pass-Through mode**: In Istio, the pass-through mode allows certain traffic to be sent directly from the application to the target service
without being processed by the sidecar proxy. This reduces latency and improves performance.

![image](../images/outbound-traffic-02.png)

## Summary

By reasonably setting the outbound traffic policy of the service mesh, you can effectively meet the access requirements of services to external resources and reduce the complexity of O&M and configuration.
For environments without strict external access restrictions, allowing access to all external services is an effective way to simplify O&M.
For database services that need long connections, enabling the pass-through mode can reduce the impact of the sidecar proxy on performance.
