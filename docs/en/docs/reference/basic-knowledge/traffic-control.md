# traffic management

Service mesh traffic routing rules allow you to easily control traffic and API calls between services.
A service mesh simplifies configuration of service-level properties such as circuit breakers, timeouts, and retries, and makes it easy to set up important tasks.
It also provides out-of-the-box failover features that help increase the robustness of applications in the event of failures of dependent services or networks.

The service mesh traffic management model is derived from the Envoy proxy deployed with the service.
All traffic (data plane traffic) sent and received by services within the mesh is proxied through Envoy, which makes controlling traffic within the mesh extremely simple without requiring any changes to the services.

In order to direct traffic in the mesh, the service mesh needs to know where all the endpoints are and which service they belong to.
To locate the service registry (service registry), the service mesh connects to a service discovery system.
For example, if you have a service mesh installed on a Kubernetes cluster, it will automatically detect the services and endpoints in that cluster.

Using this service registry, Envoy proxies can direct traffic to relevant services.
In most microservice-based applications, each service workload has multiple instances to handle traffic, called a load-balancing pool.
By default, the Envoy proxy distributes traffic in the service's load balancing pool based on the round-robin scheduling model, and sends requests to each member in the pool in order. Once all service instances have received a request, they return to the first pool member.

The basic service discovery and load balancing capabilities of a service mesh give you a usable service mesh, but it can do a lot more than that.
In many cases, you may wish to have finer-grained control over the traffic profile of your mesh.
As part of A/B testing, you might want to direct a certain percentage of traffic to a new version of a service, or apply a different load balancing strategy to a specific subset of service instances.
You may also want to apply special rules for traffic to and from your mesh, or add your mesh's external dependencies to a service registry.
This can be done, and even more, by adding traffic configurations to the service mesh using the service mesh's traffic management API.

Like other service mesh configurations, these APIs are declared using Kubernetes Custom Resource Definitions (CRDs), which you can configure using YAML.

## Traffic governance strategy

- Limiting

    Rate Limit is the abbreviation of Rate Limit, which means that only specified traffic is allowed to enter the system, and traffic exceeding the threshold will be denied service, queued or waited, downgraded, etc.
    Current limiting is to ensure the stability of the machine and the overall business and avoid system avalanche.

- downgrade

    When the pressure on the server increases sharply, according to the actual business situation and traffic, the non-core and non-critical services are strategically not or simplified, so as to release part of the server resources to ensure the normal operation or efficient operation of core services.
    When the overall load of the entire microservice architecture exceeds the preset upper limit or the upcoming traffic is expected to exceed the set threshold, downgrade processing can be performed.

- fuse

    The concept of fusing comes from the Circuit Breaker in electronic engineering.
    In the Internet system, when the downstream service responds slowly or fails due to excessive access pressure, exceeding the set threshold, the upstream service will temporarily cut off the call to the downstream service, thereby protecting the overall availability of the system.
    This measure of sacrificing the part and preserving the whole is called fusing.