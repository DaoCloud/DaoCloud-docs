# Troubleshooting Inaccessibility of External Services

When configuring external service access for the service mesh, you may encounter a situation where a service cannot connect to an external service normally.
To help you quickly locate and solve the problem, the following are detailed troubleshooting steps.

## Background

When using a service mesh for microservice governance, the **Sidecar** container takes over all inbound and outbound traffic requests of the service.
This means that when an application needs to access external services such as in-cluster APIs and databases that are not managed by the mesh, the traffic will be processed by the Sidecar proxy.

For this reason, the service mesh provides the capability of **multiple egress traffic forwarding policies**.
See [How to Choose an Outbound Traffic Policy](../best-practice/outbound-traffic.md) to choose a suitable egress traffic policy.

If, after the configuration, a service cannot access an external service normally, you can troubleshoot according to the following steps.

## 1. Check Whether the External Service Itself Is Normal

First, confirm whether the external service is running normally.

**Verification method:**

- Without going through the service mesh, directly access the external service from other services or nodes in the cluster to confirm its availability.
- Use tools such as `curl`, `telnet`, or a database client to connect to the external service directly and see whether it responds normally.

## 2. Check Whether It Is Normal When No Sidecar Is Injected

Next, confirm whether the problem is caused by the Sidecar proxy.

- **Verification method:**
    - In the sidecar management of the mesh instance, find the corresponding workload and then temporarily disable sidecar injection.
    - Then observe whether the service without an injected Sidecar can access the external service normally.
- **Analysis:** If the service can access the external service normally when no Sidecar is injected, the problem may lie in the Sidecar proxy or the mesh configuration.

## 3. Check the Configuration of the Egress Traffic Policy

Make sure the external traffic policy is configured correctly. After a mesh instance is created, the default is registered services, which only allows access to services registered in the mesh.

If a service is not registered in the mesh or is an external service outside the cluster, you can adjust it according to the management specifications of the egress network policy.

- If you really need to use the registered services forwarding mode, you can open it in the form of a whitelist by creating a **ServiceEntry**
- You can also change it to the all services forwarding mode, so that services not registered in the mesh can also have network access later, reducing O&M costs and failures

## 4. Check the Service Port Protocol

Make sure the protocol of the service port is configured correctly, especially in the ServiceEntry and VirtualService.

- **What to check:**
    - Confirm that the port protocol (such as HTTP, TCP, TLS) is consistent with the protocol actually used by the external service.
    - For services using non-HTTP protocols, such as MySQL and Redis, the appropriate protocol type should be used.
- **Verification method:**
    - Check the ServiceEntry configuration and confirm whether the `protocol` in the `ports` field is correct.
    - Check whether you need to enable the **Pass-Through mode** to bypass the Sidecar proxy.

## 5. Check the Sidecar Logs and Monitoring

By checking the logs of the Sidecar proxy, you can obtain more fault information.

- **Verification method:**

    - Use the `kubectl logs` command to view the logs of the Sidecar container (usually `istio-proxy`):

        ```shell
        kubectl logs [pod-name] -c istio-proxy
        ```

    - Observe whether there are errors such as connection refused or timeout.

## 6. Check Network Policies and Firewalls

In some cases, a cluster network policy or a firewall may block outbound traffic.

**Verification method:**

- Check the **NetworkPolicy** configuration of Kubernetes and confirm whether outbound traffic to external services is allowed.
- Check the configuration of the cloud provider or physical firewall to make sure the relevant ports and protocols are not blocked.

## 7. Confirm the TLS and Certificate Configuration

If the external service requires TLS encryption, you need to confirm that the certificate and encryption settings are correct.

**Verification method:**

- Check whether a **DestinationRule** needs to be configured to specify the correct TLS mode.
- Confirm whether the certificate is valid and trusted.
- Configure appropriate certificate trust settings such as `TLSContext` in the Sidecar.

## Explanation of Technical Terms

- **ServiceEntry:** A configuration object in Istio used to bring external services under the control of the service mesh, allowing Istio's traffic management and policy control to be applied to external services.
- **External Traffic Policy:** Used to control the outbound traffic policy of services in the mesh to external services, and determines how services handle traffic from or to the outside.
- **Sidecar:** A proxy container that resides together with the application container, usually an Envoy proxy.
  In a service mesh, it is used to intercept and process the inbound and outbound traffic of services, implementing functions such as load balancing, service discovery, and security.
- **Deployment/Pod:** Workload objects in Kubernetes. A Deployment manages the deployment and lifecycle of a group of Pods,
  and a Pod is the smallest deployable unit in Kubernetes, containing one or more containers.

## Summary

With the above troubleshooting steps, you can systematically troubleshoot the problem that a service cannot access an external service. The key is to verify each possible cause step by step,
from the availability of the external service, the impact of the Sidecar, and the correctness of the configuration, to network policies and security settings, and finally find the root cause of the problem and solve it.
