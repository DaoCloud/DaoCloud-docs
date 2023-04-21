---
hide:
  - toc
---

# Access from external applications to services in the mesh

This page explains how external applications can be configured to access services within the mesh.

precondition:

- The service `bookinfo.com` runs under the `default` namespace of the mesh `global-service`

- Mesh provides `ingressgateway` gateway instance

Configuration goal: realize the external exposure of the internal service `bookinfo.com`.

1. Through the URI matching method, realize the access routing of the specified page of the service `bookinfo.com` by external applications.

    

2. Click `Traffic Governance` -> `Gateway Rules` -> `Create` to create a gateway rule for the istio gateway, and expose the service and port to the outside.

    

    The YAML example after configuration is as follows:

    ```yaml
    apiVersion: networking.istio.io/v1beta1
    kind: Gateway
    metadata:
      name: bookinfo-gateway
    spec:
      selector:
        istio: ingressgateway # use the default controller
      servers:
      - port:
          number: 80
          name: http
          protocol: HTTP
        hosts:
        -bookinfo.com
    ```

3. Click `OK` to return to the list of gateway rules, and you can see the prompt of successful creation.

4. Click `Traffic Governance` -> `Virtual Service` -> `Create` to create routing rules to route to specified pages based on the URI in the request.

    

    The YAML example after configuration is as follows:

    ```yaml
    apiVersion: networking.istio.io/v1beta1
    kind: VirtualService
    metadata:
      name: bookinfo
    spec:
      hosts:
      -bookinfo.com
      gateways:
      -bookinfo-gateway
      http:
      - match:
          - uri:
              exact: /productpage
          - uri:
              exact: /login
          - uri:
              exact: /logout
          - uri:
              prefix: /api/v1/products
        route:
        -destination:
            host: productpage
            port:
              number: 9080
    ```

5. Click `OK` to return to the virtual service list, and you can see the prompt that the creation is successful.

!!! info

    For a more intuitive operation demonstration, please refer to [Video Tutorial](../../../videos/mspider.md).