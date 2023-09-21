# IngressClass

IngressClass 代表 Ingress 实例 的类，当创建 Ingress 规则时，可在 Ingress 的 spec 中引用。主要的适用场景如下：

**适用场景**

* 同一个集群中，有内部 Ingress 和外部 Ingress 需求
* 同一个集群同一个命名空间中，不同团队部署不同的应用，使用不同 Ingress 实例
* 同一个集群中，同一团队部署不同应用对 Ingress 实例资源配比有要求
    * 例如某些业务需要独享 4C 4G 的数据面网关资源

## 前提条件

- 已经完成 [Ingress nginx 实例部署，并设置了 IngressClassName](install.md)。
- 已获取对应的 IngressClassName。

## 使用操作

### 通过 YAML 创建 Ingress 并指定 IngressClass

通过 YAML 创建 Ingress 时，如需要指定 ingressClass 时，需要通过 `ingressClassName` 指定。
注解 `kubernetes.io/ingress.class` 已经废弃。

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: dao-2048
spec:
  ingressClassName: contour # 指定 ingress class 名称
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

### 通过界面创建 Ingress 并指定 IngressClass

如通过[图形化创建路由（Ingress ）](../../../kpanda/user-guide/network/create-ingress.md)时，可直接在界面输入对应的 `IngressClassName`。

### 默认 IngressClass

每个集群都可以有一个默认的 IngressClass。存在默认 IngressClass 时（ [创建 Ingress 实例时，开启 DefaultIngressClass](install.md) ），创建 Ingress 时可以不指定 `ingressClassName` 字段。

`ingressclass.kubernetes.io/is-default-class` 注解可以用来标明一个 IngressClass 作为默认类。一个集群最多只能设置一个。
当某个 `IngressClass` 资源将此注解设置为 `true` 时，没有指定 class 的新 Ingress 资源将被分配到此默认类。

## QA

问：不同租户如何使用不同 Ingress 负载流量而且还不用指定 ingressClassName？

答：可以通过指定 `--watch-namespace` 的方式，不同的实例 watch 不同的 namespace。
ingress-nginx 可以通过 helm 安装时指定 `controller.scope.enabled=true` 和 `--set controller.scope.namespace=$NAMESPACE`，
更多信息可以参考 [scope](https://kubernetes.github.io/ingress-nginx/deploy/#scope)。
