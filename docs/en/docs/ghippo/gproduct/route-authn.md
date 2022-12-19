---
hide:
  - toc
---

# Access routing and login authentication

Unified login and password verification after access, the effect is as follows:

[Access Effect](../images/gproduct02.png)

The API bear token verification of each GProduct module goes through the Istio Gateway.

The routing map after access is as follows:

[Access Effect](../images/gproduct03.png)

## access method

Take `kpanda` as an example to register GProductProxy CR.

```yaml
# GProductProxy CR example, including routing and login authentication
 
# spec.proxies: The route written later cannot be a subset of the route written first, and vice versa
# spec.proxies.match.uri.prefix: If it is a backend api, it is recommended to add "/" at the end of the prefix to indicate the end of this path (special requirements can not be added)
# spec.proxies.match.uri: supports prefix and exact modes; Prefix and Exact can only choose 1 out of 2; Prefix has a higher priority than Exact
 
apiVersion: ghippo.io/v1alpha1
kind: GProductProxy
metadata:
  name: kpanda # cluster level CRD
spec:
  gproduct: kpanda # Need to specify the GProduct name in lowercase
  proxies:
  - labels:
      kind: UIEntry
    match:
      uri:
        prefix: /kpanda # can also support exact:
    rewrite:
      uri: /index.html
    destination:
      host: ghippo-anakin.ghippo-system.svc.cluster.local
      port: 80
    authnCheck: false # Whether istio-gateway is required to perform AuthN Token authentication for this routing API, false means skip authentication
  - labels:
      kind: UIAssets
    match:
      uri:
        prefix: /ui/kpanda/ # UIAssets recommend adding "/" at the end to indicate the end (otherwise there may be problems in the front end)
    destination:
      host: kpanda-ui.kpanda-system.svc.cluster.local
      port: 80
    authnCheck: false
  - match:
      uri:
        prefix: /apis/kpanda.io/v1/a
    destination:
      host: kpanda-service.kpanda-system.svc.cluster.local
      port: 80
    authnCheck: false
  - match:
      uri:
        prefix: /apis/kpanda.io/v1 # The route written later cannot be a subset of the route written first, otherwise it can
    destination:
      host: kpanda-service.kpanda-system.svc.cluster.local
      port: 80
    authnCheck: true
```