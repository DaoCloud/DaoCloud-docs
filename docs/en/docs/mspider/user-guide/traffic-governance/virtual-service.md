# Virtual Service

In the Virtual Service, you can use various matching methods such as port, host, header, etc., to route and distribute requests from different regions and users to specific service versions, divided by weight.

Virtual Service provides routing support for three protocols: HTTP, TCP, and TLS.

## Virtual Service List

The Virtual Service list displays the Virtual Service CRD information under the mesh. Users can view it by namespace or filter the CRDs based on scope and rule labels. The rule labels include:

- HTTP routing
- TCP routing
- TLS routing
- Rewrite
- Redirect
- Retry
- Timeout
- Fault injection
- Proxy service
- Traffic mirroring

For the configuration of these label fields, refer to the [Istio Virtual Service Configuration Parameters](https://istio.io/latest/docs/reference/config/networking/virtual-service/).

Virtual Service provides two creation methods: graphical wizard creation and YAML creation.

## Graphical Wizard Creation Steps

The specific steps for creating using the graphical wizard are as follows (refer to [Virtual Service Parameters Configuration](./vsparams.md)):

1. Click __Traffic Management__ in the left navigation bar, then click __Virtual Service__ , and click the __Create__ button in the upper right corner.

    ![Create](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/user-guide/images/virtualserv01.png)

2. In the __Create Virtual Service__ page, confirm and select the namespace, service,
   and application scope where the virtual service will be created, then click __Next__ .

    ![Create Virtual Service](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/user-guide/images/virtualserv02.png)

3. Configure the HTTP routes, TLS routes, and TCP routes as prompted on the screen, then click __OK__ .

    ![Routing Configuration](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/user-guide/images/virtualserv03.png)

4. Return to the Virtual Service list, and there will be a prompt indicating successful creation. On the right side of the Virtual Service list, click the __⋮__ in the "Actions" column to perform more operations from the pop-up menu.

    ![More Actions](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/user-guide/images/virtualserv04.png)

## YAML Creation

The operation for creating using YAML is relatively simple. You can click the __Create by YAML__ button
to enter the creation page and directly write YAML. Alternatively, users can use the provided templates
on the page to simplify the editing process. The editing window provides basic syntax checking functionality
to assist users in writing. Here is an example YAML:

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  annotations:
    ckube.daocloud.io/cluster: dywtest3
    ckube.daocloud.io/indexes: '{"activePolices":"HTTP_ROUTE,RETRIES,","cluster":"dywtest3","createdAt":"2023-08-07T09:27:48Z","gateway":"nginx-gw/nginx-gwrule","gateways":"[\"nginx-gw/nginx-gwrule\"]","hosts":"[\"www.nginx.app.com\"]","is_deleted":"false","labels":"","name":"nginx-vs","namespace":"nginx-gw"}'
  creationTimestamp: "2023-08-07T09:27:48Z"
  generation: 10
  managedFields:
    - apiVersion: networking.istio.io/v1beta1
      fieldsType: FieldsV1
      fieldsV1:
        f:metadata:
          f:annotations:
            .: {}
            f:ckube.daocloud.io/cluster: {}
            f:ckube.daocloud.io/indexes: {}
        f:spec:
          .: {}
          f:gateways: {}
          f:hosts: {}
          f:http: {}
      manager: cacheproxy
      operation: Update
      time: "2023-08-09T03:06:31Z"
  name: nginx-vs
  namespace: nginx-gw
  resourceVersion: "477662"
  uid: 446e8dcf-3c26-47ec-8754-997c21e4df17
spec:
  gateways:
    - nginx-gw/nginx-gwrule
  hosts:
    - www.nginx.app.com
  http:
    - match:
        - uri:
            prefix: /
      name: nginx-http
      retries:
        attempts: 2
        perTryTimeout: 5s
        retryOn: 5xx
      route:
        - destination:
            host: nginx.nginx-test.svc.cluster.local
            port:
              number: 80
status: {}
```

## Concepts

- Hosts

    The target hosts for traffic. They can come from service registration information, service entries, or user-defined service domain names. They can be DNS names with wildcard prefixes or IP addresses.
    Depending on the platform, short names may be used instead of FQDN. In this case, the conversion from a short name to an FQDN is handled by the underlying platform.

    A hostname can only be defined in one VirtualService. The same VirtualService can control the traffic properties for multiple HTTP and TCP ports.

    It is important to note that when using the short name of a service
    (e.g., using "reviews" instead of __reviews.default.svc.cluster.local__ ),
    the service mesh will handle this name based on the namespace of the rule,
    not the namespace where the service resides. Suppose a rule in the __default__ namespace
    includes a host reference to __reviews__ . It will be treated as __reviews.default.svc.cluster.local__ ,
    regardless of the namespace where the reviews service resides.

    To avoid potential misconfigurations, it is recommended to use FQDN for service references.
    The hosts field is valid for both HTTP and TCP services.
    Services in the mesh, which are registered in the service registry, must be referenced using their registered names; only services defined by Gateways can be referenced using IP addresses.

    Example:

    ```yaml
    spec:
      hosts:
      - ratings.prod.svc.cluster.local
    ```

- Gateways

    By binding VirtualServices to gateway rules with the same host, these hosts can be exposed outside the mesh.

    The mesh uses the reserved keyword "mesh" to refer to all Sidecars in the mesh.
    When this field is omitted, the default value ("mesh") will be used, which applies to all Sidecars in the mesh.
    If the gateways field is set with gateway rules (can have multiple), it will only apply to the declared gateway rules.
    If you want to apply the rules to both gateway rules and all services, you need to explicitly include "mesh" in the gateways list.

    Example:

    ```yaml
    gateways:
    - bookinfo-gateway
    - mesh
    ```

- HTTP

    An ordered list of rules that contain all the routing configurations for HTTP protocol.
    It applies to service ports with names prefixed with __http-__ , __http2-__ , __grpc-__ , or protocols
    as HTTP, HTTP2, GRPC, and terminating TLS,
    as well as ServiceEntry using HTTP, HTTP2, and GRPC protocols. Traffic will be handled by the first rule that matches.

    Explanation of main fields in HTTP:

    - Match

        The conditions that must be satisfied for a rule to be activated. All conditions within a single match block have AND semantics, while the match blocks have OR semantics.
        If any match block succeeds, the rule is considered a match.

    - Route

        HTTP rules can either redirect or forward (default) traffic.

    - Redirect

        HTTP rules can either redirect or forward (default) traffic.
        If traffic is specified to go through an option in the rule, routing/redirecting will be ignored.
        Redirect primitives can be used to send HTTP 301 redirects to other URIs or authorities.

    - Rewrite

        Rewrite the HTTP URI and Authority header. Rewriting cannot be used together with redirect primitives.

    - Fault

        Fault injection policies for client-side HTTP communication.
        Enabling fault injection policies on the client side will disable timeouts or retries.

    - Mirror/MirrorPercent

        Mirror HTTP traffic to another destination, with the ability to set the mirroring percentage.

    - TCP

        An ordered list of routes for passthrough TCP traffic.
        TCP routing applies to all ports except for HTTP and TLS. Incoming traffic will be handled by the first rule that matches.

    - TLS

        An ordered list corresponding to passthrough TLS and HTTPS traffic. The routing process usually relies on the SNI in the ClientHello message.
        TLS routing typically applies to platform service ports with prefixes like https- or tls-, or HTTPS, TLS protocol ports passed through a Gateway, and ServiceEntry ports using HTTPS or TLS protocols.
        Note: HTTPS or TLS traffic on ports without an associated VirtualService will be treated as passthrough TCP traffic.

    The TCP protocol and its subfields are relatively simple, only containing "match" and "route" parts, which are similar to HTTP and will not be repeated here.

## Reference

- [What is __VirtualService__ ?](https://istio.io/latest/docs/concepts/traffic-management/#virtual-services)
- [ __VirtualService__ Configuration](https://istio.io/latest/docs/concepts/traffic-management/#virtual-service-example)
