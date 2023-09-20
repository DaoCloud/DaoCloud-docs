---
MTPE: Jeanine-tw
Revised: Jeanine-tw
Pics: NA
Date: 2023-02-08
---

# IngressClass

IngressClass represents the class of the Ingress instance that can be referenced in the Ingress spec when an Ingress rule is created. The main cases are as follows.

**Use cases**

* Need both internal Ingress and external Ingress in the same cluster
* Different teams deploy different applications in the same cluster with different Ingress instances in the same namespace
* In the same cluster, the same team deploys different applications with different Ingress instance resource ratios
    * For example, some services need exclusive access to 4C 4G data plane gateway resources

## Prerequisites

- [The Ingress nginx instance has been deployed and the IngressClassName has been set](install.md).
- The corresponding IngressClassName has been obtained.

## Operations

### Create Ingress via YAML and specifying the IngressClass

If you need to specify an IngressClass when creating an Ingress via YAML, specify it via `ingressClassName`.
The annotation ``kubernetes.io/ingress.class`` is deprecated.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: dao-2048
spec:
  ingressClassName: contour # Specify the ingress class name
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: dao-2048
            port:
              number: 80
```

### Create Ingress through the interface and specify IngressClass

If [the route（Ingress) is created through the interface](../../../kpanda/user-guide/network/create-ingress.md), you can directly enter the corresponding `IngressClassName` in the interface.

### Default IngressClass

Each cluster can have a default IngressClass. When a default IngressClass exists ([enable DefaultIngressClass when creating Ingress instances](install.md)), Ingress can be created without specifying the `ingressClassName`.

The `ingressclass.kubernetes.io/is-default-class` annotation can be used to mark an IngressClass as the default class. Only one IngressClass can be set for a cluster at most.
When this annotation is set to `true` for an `IngressClass` resource, new Ingress resources without a specified class will be assigned to this default class.

## QA

Q: How can different tenants use different Ingress traffic without specifying ingressClassName?

A: Different instances can watch different namespaces by specifying `--watch-namespace`.
ingress-nginx can be installed via helm by specifying `-controller.scope.enabled=true` and `-set controller.scope.namespace=$NAMESPACE`.
More information can be found in [scope](https://kubernetes.github.io/ingress-nginx/deploy/#scope).
