# Optimizing Sidecar Resource Usage

In the design philosophy of Istio, the Sidecar caches information for all services in the cluster
by default. This leads to high resource consumption by the Sidecar, especially when there are
hundreds or thousands of business Pods.

```mermaid
graph LR

init[Reduce Sidecar resource consumption] -.70%.-> ns[Namespace]
init -.20%.-> vs[vs/dr/ServiceEntry]

ns --> nss[Use NS-level Sidecar]
ns --> topo[Dependency-based access topology] --> health1[With health checks]

vs --> export[Add exportTo] --> health2[With health checks]
vs --> limit[Dependency-based service level restrict]

classDef plain fill:#ddd,stroke:#fff,stroke-width:1px,color:#000;
classDef k8s fill:#326ce5,stroke:#fff,stroke-width:1px,color:#fff;
classDef cluster fill:#fff,stroke:#bbb,stroke-width:1px,color:#326ce5;

class ns,vs cluster;
class nss,topo,health1,health2,export,limit plain;
```

To alleviate the issue of resource consumption, you can implement the following configurations.

## Technical Solution

1. Namespace-Level sidecar restriction.

    ```yaml
    apiVersion: networking.istio.io/v1beta1
    kind: Sidecar
    metadata:
      name: restrict-access-sidecar
      namespace: namespace1
    spec:
      egress:
      - hosts:
        - namespace2/*
        - namespace3/*
    ```

    The above YAML restricts the services under __namespace1__ to only access services in __namespace2__ and __namespace3__ .

    To implement this, you need to add a whitelist of other namespaces that can be accessed by
    the namespace managed by the cluster.

    There are a few considerations to keep in mind with this approach:

    - Whether there is a global switch for enabling the whitelist mechanism
    - Whether modifying the whitelist will require Sidecar updates or restarts
    - Whether there are corresponding health check prompts when application access issues occur
    - Whether a method similar to NS-group (read from workspaces) can automatically
      configure bidirectional Sidecar namespace accessibility (with a global switch)

2. Adding __exportTo__ to Istio Resources

    By using Sidecar access control under the Namespace, you can still achieve namespace-level
    restrict. If you need to reduce resource consumption, you can add the corresponding
    __exportTo__ configuration to the Istio resources, declaring which namespaces can access these resources.

    This approach incurs higher configuration costs.
    If implemented, batch configuration capabilities should be considered:

    ```yaml
    apiVersion: networking.istio.io/v1alpha3
    kind: VirtualService
    metadata:
      name: my-virtual-service
      namespace: my-namespace
    spec:
      exportTo:
      - "namespace1"
      - "namespace2"
      hosts:
      - "*"
      http:
      - route:
        - destination:
          host: my-service
    ```

## Demo

- Prepare two services in different namespaces: __NS-a__ and __NS-b__ 
- Ensure that both services have Sidecars successfully injected
- Create a Sidecar resource with YAML content as follows:

    ![sidecar](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/best-practice/images/sidecar.png)

    ```yaml
    apiVersion: networking.istio.io/v1beta1
    kind: Sidecar
    metadata:
      name: restrict-access-sidecar
      namespace: default # current namespace
    spec:
      egress:
        - hosts:
          # allow current namespace request this namespace service
          - webstore-demo/*
    ```

    ![yaml](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/best-practice/images/yaml1.png)

- Access Result

    ![Access Result](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/best-practice/images/effect.png)
