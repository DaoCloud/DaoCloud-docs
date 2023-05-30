# Virtual Services

Here we introduce virtual services in the context of a service mesh.

Virtual services and destination rules are key pieces of service mesh traffic routing functionality. Virtual services allow you to configure how requests are routed to services within the service mesh, based on the basic connectivity and service discovery capabilities provided by the service mesh and platform. Each virtual service contains a set of routing rules that the service mesh evaluates in order, matching each given request to the actual destination address specified by the virtual service. Your mesh can have multiple virtual services, or none at all, depending on your use case.

## Why Use Virtual Services?

Virtual services play a critical role in enhancing the flexibility and effectiveness of service mesh traffic management, allowing for decoupling of client-requested destination addresses from the actual workload that processes the request. Virtual services also provide rich ways to specify different routing rules for traffic sent to these workloads.

Why is this useful? Without virtual services, Envoy would distribute requests among all service instances using a round-robin load-balancing strategy. You can improve upon this behavior with knowledge of your workloads. For example, some may represent different versions. This could be useful in A/B testing, where you might want to configure traffic percentage routing based on different service versions, or direct traffic from internal users to a specific set of instances.

With virtual services, you can specify traffic behavior for one or more hostnames. Using routing rules within a virtual service tells Envoy how to send the virtual service's traffic to the appropriate destination. Routing destinations can be different versions of the same service, or completely different services.

Virtual services enable you to:

- Handle multiple application services with a single virtual service.

    With Kubernetes, if your mesh is configured to process services within a particular namespace, you can configure a virtual service to handle all the services in that namespace. Mapping a single virtual service to multiple "real" services can be particularly useful in transforming a monolithic application into a composite application system built from microservices without requiring client-side adaptation to the changes. Your routing rules can specify things like "route URIs for these `monolith.com` calls to `microservice A`," and so on. See an example of it below in the section on more about routing rules.

- Integrate with [gateways](gateway.md) and configure traffic rules to control ingress and egress traffic.

    In some cases, you'll also want to configure destination rules to use these features, as this is where subsets of services are specified. Specifying the subset of services and other specific destination policies in a single object is advantageous for more concise reuse of those rules between virtual services.

### Example Virtual Service

The following virtual service routes requests to different versions of a service based on whether the request comes from a specific user.

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: reviews
spec:
  hosts:
  - reviews
  http:
  - match:
    - headers:
        end-user:
          exact: jason
    route:
    - destination:
        host: reviews
        subset: v2
  - route:
    - destination:
        host: reviews
        subset: v3
```

#### Hosts Field

The `hosts` field lists the virtual service's hosts--that is, the targets specified by the user or set by the routing rules. These are one or more addresses used by clients to send requests to the service.

```yaml
hosts:
- reviews
```

Virtual service host names can be IP addresses, DNS names, or platform-dependent shorthand (such as Kubernetes service short names) that implicitly or explicitly point to a fully qualified domain name (FQDN). You can also use a wildcard ("*") prefix to create a set of routing rules that match all services. The `hosts` field for a virtual service doesn't actually have to be part of the service mesh service registry; it's just a virtual destination address. This lets you model virtual hosts that don't route to anything inside the mesh.

#### Routing Rules

The `http` field contains routing rules for the virtual service, describing matching conditions and routing behavior. They send traffic for HTTP/1.1, HTTP2, and gRPC among others to the targets specified by the `hosts` field (you can also use the `tcp` and `tls` sections to set routing rules for TCP and un-terminated TLS traffic). A routing rule specifies which target address to send the given request to, with zero or more matching conditions depending on your use case.

##### Matching Conditions

The first routing rule in the example has one condition, so it starts with the `match` field. In this instance, you want this route to apply to all requests from the user "jason," so you use the `headers`, `end-user`, and `exact` fields to select the appropriate requests.

```yaml
- match:
   - headers:
       end-user:
         exact: jason
```

##### Destination

The `destination` field in the `route` section specifies the actual target address for traffic that meets this condition. Unlike the `hosts` of a virtual service, the `host` of the destination must be an actual target address that exists in the service mesh service registry. Otherwise, Envoy does not know where to send the request. It can be a service mesh with a proxy or a non-mesh service added through a service entry. In this example, it runs in a Kubernetes environment, and the host name is a Kubernetes service name:

```yaml
route:
- destination:
    host: reviews
    subset: v2
```

Please note that in this example and other examples on this page, for simplicity, we use the short name of Kubernetes to set the destination host. When evaluating this rule, the service mesh adds a domain suffix based on the virtual service namespace. This virtual service contains routing rules that include the fully qualified name of the host you want to get. Using the short name in our example also means that you can copy and try them in any namespace you like.

This type of short name can only be used when the target host and virtual service are in the same Kubernetes namespace. Because using Kubernetes' short names can easily lead to configuration errors, we recommend that you specify fully qualified host names in production environments.

The destination segment also specifies a subset of the Kubernetes service to which requests that meet this rule's conditions will be routed. In this example, the subset name is v2. You can see how to define service subsets in the target rules section.

#### Routing rule priority

Routing rules are selected from top to bottom, and the first rule defined in the virtual service has the highest priority. In this example, traffic that does not meet the first routing rule flows to a default target specified in the second rule. Therefore, the second rule has no match conditions and directly routes traffic to the v3 subset.

```yaml
- route:
  - destination:
      host: reviews
      subset: v3
```

We suggest providing a default "unconditional" or weight-based rule (see below) as the last rule for each virtual service to ensure that the traffic flowing through the virtual service can at least match one routing rule.

### More on Routing Rules

As seen above, routing rules are a powerful tool for routing specific subsets of traffic to designated destination addresses.
You can set matching conditions based on traffic ports, header fields, URIs and more.
For example, this virtual service allows users to send requests to two independent services, ratings and reviews, as if they were part of a larger virtual service called `http://bookinfo.com/`.
Virtual service rules match traffic based on the requested URI and direct the traffic to the appropriate service.

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: bookinfo
spec:
  hosts:
    - bookinfo.com
  http:
  - match:
    - uri:
        prefix: /reviews
    route:
    - destination:
        host: reviews
  - match:
    - uri:
        prefix: /ratings
    route:
    - destination:
        host: ratings
...

  http:
  - match:
      sourceLabels:
        app: reviews
    route:
...
```

Some matching conditions can use exact values, such as prefix or regular expressions.

You can use "AND" to add multiple matching conditions to the same `match` block, or use "OR" to add multiple `match` blocks to the same rule.
There can also be multiple routing rules for any given virtual service. This can make routing conditions as complex or simple as desired within a single virtual service.

You can also use routing rules to perform operations on traffic, such as:

- Adding or removing headers
- Rewriting URLs
- Setting retry strategies for requests to call this destination address
