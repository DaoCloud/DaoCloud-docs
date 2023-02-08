---
MTPE: Jeanine-tw
Revised: Jeanine-tw
Pics: Jeanine-tw
Date: 2023-02-08
---

# Ingress scope

The IngressClass Scope can be used to specify whether the Ingress instance is limited to the cluster level、the namespace level and the workspace level.

**Applicable scenarios**

* Cluster-level Ingress instances can be set up in the same cluster that shares the same Ingress instance.
* Namespace-level Ingress instances can be set when a namespace use an exclusive Ingress instance for load isolation.
* The workspace has an exclusive Ingress instance for load isolation, and the workspace corresponds to the namespace under the current cluster where all Pods can receive requests distributed by this load balancer.

> If there are different applications in the same namespace in the same cluster that need to use different Ingress instances, please refer to [IngressClass](ingressclass.md).

## Cluster-level Ingress instances

When creating an Ingress instance with `Ingress Scope` enabled, the IngressClass resource is created with `cluster-level` Ingress instances in the following two cases.

1. Only `parameters` is set but `.spec.parameters.scope` is not set
2. `.spec.parameters.scope` is set to `cluster`

```yaml
# Example
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: external-lb-1
spec:
  controller: example.com/ingress-controller
  parameters:
    scope: Cluster # Specify the scope of the Ingress instance as Cluster
    apiGroup: k8s.example.net
    kind: ClusterIngressParameter # Specify the Ingress instance Kind as ClusterIngressParameter
    name: external-config-1
```

## Namespace-level Ingress instances

When creating an Ingress instance, with  `Ingress Scope` enabled, and IngressClass set to `.spec.parameters`, and `.spec.parameters.scope` set to `Namespace`, then the Ingress Class of the Ingress instance is `namespace level` and the namespace to be used needs to be specified.

Namespace-level Ingress instances are equivalent to the fact that the admin delegates Ingress usage rights to a namespace, allowing for resource isolation.

```yaml
#Example
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: external-lb-2
spec:
  controller: example.com/ingress-controller
  parameters:
    scope: Namespace # Specify the scope of the Ingress instance as Namespace
    apiGroup: k8s.example.com
    kind: IngressParameter # Specifies that the Ingress instance Kind is IngressParameter
    namespace: default # Specify the namespace to be used
    name: external-config
```

## How to deploy cluster/namespace level Ingress instances?

Different instances can watch different namespaces by specifying `--watch-namespace`.
If [ingress-nginx instances are installed via Helm](install.md), you need to enable and set cluster/namespace level Ingress by specifying `-controller.scope.enabled=true` and `-set controller.scope.namespace=$NAMESPACE`.

If the namespace is enabled and specified during deployment, the Ingress instance created will be assigned to the namespace. Otherwise, it will be shared across the cluster.The example creates Ingress-nginx as a Default exclusive as shown below：

![scope01](../../images/scope01.png)

Configuration information in the corresponding `value.yaml`:

![scope02](../../images/scope02.png)

## How to deploy workspace-level Ingress instances?

When you assigning a load balancer to a workspace during load balancer deployment, the workspace corresponds to the namespace under the current cluster where all Pods can receive requests distributed by this load balancer.

When deploying Ingress-Ngnix, specify `kubernetes.io/metadata.name :workspace01` in the `Namespace Selector`, and the Ingress instance will be created exclusively for the workspace `workspace01`.

![workspaceIngress](../../images/workspaceingress.png)

The configuration information in the corresponding `value.yaml`:

![workspaceingress02](../../images/workspaceingress02.png)

After the Ingress instance is deployed, you can [create Ingress rules](../../../kpanda/07UserGuide/ServicesandRoutes/CreatingIngress.md)) in the corresponding namespace and select the Ingress Class for the corresponding instance to use.

For more information you can refer to [scope](https://kubernetes.github.io/ingress-nginx/deploy/#scope).
