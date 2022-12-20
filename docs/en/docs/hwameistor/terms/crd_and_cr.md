# CRD and CR

##CRD

`CRD` is the abbreviation of `Custom Resource Definition`, which is a built-in native resource type of `Kubernetes`. It is the definition of a custom resource (CR), which describes what a custom resource is.

CRD can register a new resource with the `Kubernetes` cluster to extend the capabilities of the `Kubernetes` cluster. With `CRD`, you can customize the abstraction of the underlying infrastructure, customize resource types according to business needs, and use the existing resources and capabilities of `Kubernetes` to define higher-level abstractions through the pattern of Lego blocks.

##CR

`CR` is the abbreviation of `Custom Resource`, it is actually an instance of `CRD`, and it is a resource description conforming to the field format definition in `CRD`.

## CRDs + Controllers

We all know that `Kubernetes` has a very powerful expansion capability, but only `CRD` is useless, and it needs the support of a controller (`Custom Controller`) to reflect the value of `CRD`, `Custom Controller` You can listen to the `CRUD` event of `CR` to implement custom business logic.

In `Kubernetes`, it can be said that `CRDs + Controllers = Everything`.

Please also refer to the official Kubernetes documentation:

- [CustomResource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)
- [CustomResourceDefinition](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/)