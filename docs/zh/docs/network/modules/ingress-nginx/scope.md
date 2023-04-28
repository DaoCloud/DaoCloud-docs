# Ingress 使用范围（Scope）

IngressClass Scope 用于指定 Ingress 实例的使用范围为集群级、命名空间级和工作空间级。

**适用场景**

* 同一个集群中，共享同一个 Ingress 实例，可设置`平台级 Ingress 实例`。
* 单一命名空间独享一个 Ingress 实例实现负载隔离，可设置命名空间级 Ingress 实例。
* 工作空间独享一个 Ingress 实例实现负载隔离，可设置`租户级 Ingress 实例`，工作空间中对应当前集群下的命名空间，其中 Pod 都可以接收到由该负载均衡分发的请求。

> 如果在同一个集群内，同一命名空间内有不同应用需要使用不同 Ingress 实例的需求，请参考 [IngressClass](ingressclass.md)。

## 平台级 Ingress 实例

创建 Ingress 实例时，如果启用 `Ingress Scope`，创建后的 IngressClass 资源在以下两种情况下， Ingress 实例的使用范围都为`集群级`：

1. 仅设置了 `parameters` 但是未设置 ` .spec.parameters.scope` 
2. 设置了 ` .spec.parameters.scope` 为 `cluster`

```yaml
#示例
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: external-lb-1
spec:
  controller: example.com/ingress-controller
  parameters:
    scope: Cluster # 指定 Ingress 实例范围为 Cluster
    apiGroup: k8s.example.net
    kind: ClusterIngressParameter #指定 Ingress 实例 Kind 为 ClusterIngressParameter
    name: external-config-1
```

## 命名空间级 Ingress 实例

当创建 Ingress 实例时，如果启用 `Ingress Scope`，IngressClass 设置了 `.spec.parameters`，并且设置 `.spec.parameters.scope` 为 `Namespace`，那么 Ingress 实例的 Ingress Class 指向为`命名空间级`，需要指定待使用的命名空间。

命名空间级的 Ingress 实例，相当于管理员将 Ingress 的使用权限下发给到某个命名空间，可以实现资源隔离。

```yaml
#示例
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: external-lb-2
spec:
  controller: example.com/ingress-controller
  parameters:
    scope: Namespace # 指定 Ingress 实例范围为 Namespace
    apiGroup: k8s.example.com
    kind: IngressParameter # 指定 Ingress 实例 Kind 为 IngressParameter
    namespace: default # 指定待使用的 Namespace
    name: external-config
```

## 租户级 Ingress 实例

当创建 Ingress 实例时，如果启用 `Ingress Scope`，IngressClass 设置了 `.spec.parameters`，并且设置 `.spec.parameters.scope` 为 `namespaceSelector`，并输入的 Label 为 `workspace.ghippo.io/id: '1235'`(其中 `12345` 为指定的工作空间 workspace  ID)，那么 Ingress 实例的 Ingress Class 指向为`租户级`，适用范围为`workspace01`中所有在当前集群的命名空间。

租户级的 Ingress 实例，相当于管理员将 Ingress 的使用权限下发给到某个工作空间，从而实现租户资源隔离。

```yaml
#示例
apiVersion: networking.k8s.io/v1
kind: IngressClass
metadata:
  name: external-lb-2
spec:
  controller: example.com/ingress-controller
  parameters:
    scope: Namespace # 指定 Ingress 实例范围为 Namespace
    apiGroup: k8s.example.com
    kind: IngressParameter # 指定 Ingress 实例 Kind 为 IngressParameter
    namespaceSelector: workspace.ghippo.io/id: '1235' # 指定待使用的工作空间 ID
    name: external-config
```



## 如何部署平台/命名空间级 Ingress 实例?

可以通过指定 `--watch-namespace` 的方式，不同的实例 watch 不同的命名空间。
若[ingress-nginx 实例通过 Helm 安装](install.md)，需通过指定 `controller.scope.enabled=true` 和 `--set controller.scope.namespace=$NAMESPACE` 开启并设置平台/命名空间级 Ingress。

1. `平台级 Ingress 实例`：创建 Ingress 实例时， `scope` 关闭，则创建的 Ingress 实例为 `平台级`。
2. `命名空间 Ingress 实例`：创建 Ingresss 实例时，`scope`关闭，并在 `namespace`中指定对应的命名空间，则创建的 Ingress 为 `命名空间级 `。

如下示例，创建的 Ingress-nginx 为 Default 独享：

![scope01](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/scope01.jpg)

对应的 `value.yaml` 中的配置信息：

![scope02](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/scope02.jpg)

## 如何部署租户级 Ingress 实例？

部署负载均衡器时，指定给某个工作空间使用后，此工作空间中对应当前集群下的命名空间，其中 Pod 都可以接收到由该负载均衡分发的请求。

部署 Ingress-Ngnix 时 指定 在 `Namespace Selector` 中输入 `kubernetes.io/metadata.name :workspace01`,创建后的 Ingress 实例为 工作空间 `workspace01` 独享。

![工作空间Ingress](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/workspaceingress.jpg)

对应的 `value.yaml` 中的配置信息：

![workspaceingress02](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/workspaceingress02.jpg)

Ingress 实例部署后，可在对应的命名空间中[创建 Ingress 规则](../../../kpanda/user-guide/services-routes/create-ingress.md)，并选择对应实例的 Ingress Class 进行使用。

更多信息可以参考 [scope](https://kubernetes.github.io/ingress-nginx/deploy/#scope)。
