#IngressClass

IngressClass represents the class of Ingress and is referenced by Ingress spec.
The `ingressclass.kubernetes.io/is-default-class` annotation can be used to mark an IngressClass as the default class.
When an IngressClass resource has this annotation set to true , new Ingress resources without a specified class will be assigned this default class.

## Scenes

* In the same cluster, there are internal Ingress and external Ingress requirements
* In the same cluster and the same tenant, different teams use different Ingress instances
* In the same cluster, different applications have requirements for the ratio of Ingress instance resources
    * For example, some services require exclusive use of 4C 4G data plane gateway resources

## use

### Ingress specifies the ingressClassName example

When an Ingress needs to specify an ingressClassName instance, it needs to be specified through `ingressClassName`.
The annotation `kubernetes.io/ingress.class` is deprecated.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: dao-2048
spec:
  ingressClassName: contour # specify the ingress class name
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

### Default IngressClass

Each cluster can have a default IngressClass. When there is a default IngressClass, the `ingressClassName` field can not be specified when creating an Ingress.

## QA

### How can different tenants use different Ingress load traffic without specifying ingressClassName?

By specifying `--watch-namespace`, different instances watch different namespaces.
ingress-nginx can be installed through helm by specifying `controller.scope.enabled=true` and `--set controller.scope.namespace=$NAMESPACE`,
For more information, please refer to [scope](https://kubernetes.github.io/ingress-nginx/deploy/#scope).