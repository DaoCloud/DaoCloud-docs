# Ingress Scope

The IngressClass Scope can be used to specify whether the Ingress instance is limited to the cluster level、the namespace level and the workspace level.

**Platform-level Load Balancing**

* Platform-level Ingress instances can be set up in the same cluster that shares the same Ingress instance.

**Namespace-level Load Balancing**

Namespace-level load balancing consists of `Namespace Ingress instances` and `Workspace Ingress instances`.

* Namespace-level Ingress instances can be set when a namespace use an exclusive Ingress instance for load isolation.
* The workspace has an exclusive Ingress instance for load isolation, which can be set up as a `workspace-level Ingress instance`. The workspace corresponds to the namespace under the current cluster where all Pods can receive requests distributed by this load balancer.

> If there are different applications in the same namespace in the same cluster that need to use different Ingress instances, please refer to [IngressClass](ingressclass.md).

## Platform-level Ingress instances

When creating an Ingress instance with `Ingress Scope` enabled, the IngressClass resource is created with `platform-level` Ingress instances in the following two cases:

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

Namespace-level Ingress instances are equivalent to the fact that the admin delegates Ingress usage rights to a namespace, allowing for resource isolation. If you set up namespace-level instances, you can select and use them in `Namespace-level Load Balancing` when you create routes.

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

## Workspace-level Ingress instances

When creating an Ingress instance, if `Ingress Scope` is enabled, IngressClass is `.spec.parameters`, and `.spec.parameters.scope` is `namespaceSelector`, and the Label is `workspace.ghippo.io/id: '12345'` (where `12345` is the ID of the specified workspace `workspace01`), then the Ingress instance's Ingress Class is at `workspace-level`, which applies to all namespaces in `workspace01` that are in the current cluster.

An Ingress instance at the namesapce level is equivalent to an admin delegating rights to use Ingress to a workspace, thus achieving tenant resource isolation.

```yaml
#Example
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata.
  name: external-lb-2
spec.
  controller: example.com/ingress-controller
  parameters.
    scope: Namespace # Specify the scope of the Ingress instance as Namespace
    apiGroup: k8s.example.com
    kind: IngressParameter # Specify the Ingress instance Kind as IngressParameter
    namespaceSelector: workspace.ghippo.io/id: '1235' # Specify the workspace ID to be used
    name: external-config
```

## How to deploy platform/workspace/namespace-level Ingress instances?

Different instances can watch different namespaces by specifying `--watch-namespace`.
If [ingress-nginx instances are installed via Helm](install.md), you need to enable and set platform/workspace/namespace level Ingress by specifying `-controller.scope.enabled=true` and `-set controller.scope.namespace=$NAMESPACE`.

1. `Platform-level Ingress Instance`: If `scope` is disabled when creating an Ingress instance, the Ingress instance created is `platform-level`.
2. `Namespace-level Ingress instances`: If you create Ingress instances with `scope` disabled and specify the corresponding namespace in `namespace`, the Ingress created is `namespace-level`.

The following example creates Ingress-nginx as a Default exclusive:

![scope01](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/scope01.png)

Configuration information in the corresponding `value.yaml`:

![scope02](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/scope02.png)

3. `Workspace-level Ingress Instance`: When deploying Ingress-Ngnix, set the `scope` to `disabled` and specify `workspace.ghippo.io/id=12345` in the `Namespace Selector` to create an Ingress Instance with an `ID`  `12345` exclusive to the workspace.
    ![WorkspaceIngress](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/workspace.png) The corresponding configuration information in `value.yaml`: ![workspaceingress02](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/network/images/workspace02.png)

After the Ingress instance is deployed, you can [create Ingress rules](../../../kpanda/user-guide/network/create-ingress.md) in the corresponding namespace and select the Ingress Class for the corresponding instance to use.

For more information you can refer to [scope](https://kubernetes.github.io/ingress-nginx/deploy/#scope).
