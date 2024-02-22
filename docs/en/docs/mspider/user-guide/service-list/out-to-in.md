---
hide:
  - toc
---

# Accessing Services Inside the Mesh from External Applications

This page explains how external applications can access services inside the mesh through configuration.

**Prerequisites:**

- The service __bookinfo.com__ is running in the __default__ namespace of the mesh __global-service__ .

- The mesh provides an __ingressgateway__ gateway instance.

**Objective:** Expose the internal service __bookinfo.com__ to the outside.

1. Use URI matching to route external application access to specific pages of the __bookinfo.com__ service.

    ![Access Route](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/out-to-in01.png)

2. Click __Traffic Management__ -> __Gateway__ -> __Create__ to create a gateway rule for the Istio gateway and expose the service and ports externally.

    ![Create Rule](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/out-to-in02.png)

    Here is an example YAML after completing the configuration:

    ```yaml
    apiVersion: networking.istio.io/v1beta1
    kind: Gateway
    metadata:
      name: bookinfo-gateway
    spec:
      selector:
        istio: ingressgateway # Use the default controller
      servers:
      - port:
          number: 80
          name: http
          protocol: HTTP
        hosts:
        - bookinfo.com
    ```

3. Click __OK__ to return to the gateway rule list, where you will see a successful creation message.

4. Click __Traffic Management__ -> __Virtual Service__ -> __Create__ to create a routing rule that routes based on the URI in the request to the specified pages.

    ![Create Routing Rule](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/out-to-in04.png)

    Here is an example YAML after completing the configuration:

    ```yaml
    apiVersion: networking.istio.io/v1beta1
    kind: VirtualService
    metadata:
      name: bookinfo
    spec:
      hosts:
      - bookinfo.com
      gateways:
      - bookinfo-gateway
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
        - destination:
            host: productpage
            port:
              number: 9080
    ```

5. Click __OK__ to return to the virtual service list, where you will see a successful creation message.

!!! info

    For more detailed instructions, you can refer to the [video tutorial](../../../videos/mspider.md).
