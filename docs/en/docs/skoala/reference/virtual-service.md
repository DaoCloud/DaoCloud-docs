# Virtual Services

Here we introduce virtual services in the context of a service mesh.

Virtual Services and Destination Rules are key components of the traffic routing capabilities in a service mesh. Virtual Services allow you to configure how requests are routed to services within the service mesh, based on the basic connectivity and service discovery capabilities provided by the service mesh and platform. Each virtual service consists of a set of routing rules that are evaluated in order, and the service mesh matches each given request to the actual destination address specified by the virtual service. Your mesh can have multiple virtual services or none, depending on your use case.

## Why use Virtual Services?

Virtual Services play a crucial role in enhancing the flexibility and effectiveness of traffic management in a service mesh by decoupling the target addresses of client requests from the actual destination workloads that handle the requests. Virtual Services also provide rich ways to specify different routing rules for traffic sent to these workloads.

Why is this useful? Without virtual services, Envoy would distribute requests among all service instances using a round-robin load balancing strategy. You can improve this behavior by having knowledge about your workloads. For example, some workloads may represent different versions of a service. This can be useful for A/B testing, where you may want to configure traffic percentage routing based on different service versions or direct traffic from internal users to specific sets of instances.

With virtual services, you can specify traffic behavior for one or multiple hostnames. Using routing rules within virtual services, you can instruct Envoy on how to route traffic for the virtual service to the appropriate destination. The destination addresses can be different versions of the same service or completely different services.

Virtual services enable you to:

- Handle multiple application services through a single virtual service.

    If your mesh is using Kubernetes, you can configure a virtual service to handle all services within a specific namespace. Mapping a single virtual service to multiple "real" services can be particularly useful when transitioning from a monolithic application to a composite application system built with microservices, without requiring clients to adapt to the transition. Your routing rules can specify actions like "route requests to `microservice A` for URIs under these `monolith.com`" and so on. You can see how it works in an example below.

- Integrate with and configure traffic rules for inbound and outbound traffic using [gateways](gateway.md).

    In some cases, you may also need to configure destination rules to leverage these features, as they specify service subsets. Specifying service subsets and other specific target strategies in a separate object allows for more concise reuse of these rules between virtual services.

### Example of a Virtual Service

The following virtual service routes requests to different versions of a service based on whether they come from specific users.

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

#### `hosts` Field

The `hosts` field is used to list the hosts of the virtual service, which are the target specified by the user or the target set by the routing rules. These are the addresses that clients use to send requests to the service.

```yaml
hosts:
- reviews
```

The virtual service hostname can be an IP address, a DNS name, or a platform-dependent short name (such as the short name of a Kubernetes service) that implicitly or explicitly points to a fully qualified domain name (FQDN). You can also use a wildcard (`*`) prefix to create a set of routing rules that match all services. The `hosts` field of a virtual service doesn't necessarily have to be part of the service mesh service registry; it is just a virtual target address. This allows you to model virtual hosts that are not routed within the mesh.

#### Routing Rules

The `http` field contains the routing rules of the virtual service, which describe the matching conditions and routing behavior. They direct traffic for protocols like HTTP/1.1, HTTP2, and gRPC to the targets specified in the `hosts` field (you can also set routing rules for TCP and non-terminated TLS traffic using the `tcp` and `tls` sections). A routing rule specifies the destination address for a given request, with zero or more matching conditions depending on your use case.

##### Matching Conditions

The first routing rule in the example has one condition, indicated by the `match` field. In this case, you want this route to apply to all requests from the user "jason," so you use the `headers`, `end-user`, and `exact` fields to select the appropriate requests.

```yaml
- match:
   - headers:
       end-user:
         exact: jason
```

##### Destination

The `destination` field in the `route` section specifies the actual destination address for the traffic that matches this condition. Unlike the `hosts` field of the virtual service, the `host` in the destination must be a valid target address registered in the service mesh service registry; otherwise, Envoy doesn't know where to send the request. It can be a service within the service mesh with a proxy or a non-mesh service added through a service entry. In this example running in a Kubernetes environment, the host name is a Kubernetes service name:

```yaml
route:
- destination:
    host: reviews
    subset: v2
```

Note that in this example and other examples on this page, for simplicity, we use the short name of Kubernetes to set the host for the destination. When evaluating this rule, the service mesh adds a domain suffix based on the namespace of the virtual service, which contains the fully qualified name of the host to be resolved. Using the short name in our example also means you can copy and try them in any namespace you like.

Using such short names is only possible when the target host and the virtual service are in the same Kubernetes namespace. Because using the short names in Kubernetes can lead to configuration errors, we recommend specifying fully qualified host names in a production environment.

The destination section also specifies the subset of the Kubernetes service where the requests that match this rule will be routed. In this example, the subset name is v2. You can see how to define service subsets in the Destination Rules section.

#### Routing Rule Priority

Routing rules are evaluated in the order they are defined in the virtual service, with the first rule having the highest priority. In this example, traffic that doesn't match the first routing rule is directed to a default destination specified in the second rule. Therefore, the second rule doesn't have any match conditions and directly routes traffic to the v3 subset.

```yaml
- route:
  - destination:
      host: reviews
      subset: v3
```

We recommend providing a default "catch-all" or weighted rule (as shown in the example) as the last rule for each virtual service to ensure that traffic flowing through the virtual service can match at least one routing rule.

### More on Routing Rules

As seen above, routing rules are powerful tools for routing specific subsets of traffic to designated destination addresses. You can set matching conditions on traffic ports, header fields, URIs, and more. For example, this virtual service directs users to send requests to two separate services, "ratings" and "reviews," as if they were part of a larger virtual service, `http://bookinfo.com/`. The virtual service rules match traffic based on the request's URI and route it to the appropriate service.

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

Some matching conditions can use exact values, such as prefixes or regular expressions.

You can use AND to add multiple matching conditions to the same `match` block, or use OR to add multiple `match` blocks to the same rule. There can be multiple routing rules for any given virtual service. This allows you to make the routing conditions in a single virtual service as complex or as simple as you desire.

Routing rules can also perform actions on the traffic, such as:

- Adding or removing headers
- Rewriting URLs
- Setting retry policies for requests to the destination address
