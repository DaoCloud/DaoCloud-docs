# IngressClass

IngressClass 代表 Ingress 的类，被 Ingress 的 spec 引用。
`ingressclass.kubernetes.io/is-default-class` 注解可以用来标明一个 IngressClass 作为默认类。
当某个 IngressClass 资源将此注解设置为 true 时，没有指定 class 的新 Ingress 资源将被分配到此默认类。

## 场景

* 同一个集群中，有内部 Ingress 和外部 Ingress 需求
* 同一个集群同一个租户中，不同团队使用不同 Ingress 实例
* 同一个集群，不同应用对 Ingress 实例资源配比要求
    * 例如某些业务需要独享 4C 4G 的数据面网关资源

## 使用

### Ingress 指定 ingressClassName 示例

当 Ingress 需要指定 ingressClassName 示例时，需要通过 `ingressClassName` 指定。
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

### 默认 IngressClass

每个集群都可以有一个默认的 IngressClass。存在默认 IngressClass 时，创建 Ingress 时可以不指定 `ingressClassName` 字段。

## QA

### 不同租户如何使用不同 Ingress 负载流量而且还不用指定 ingressClassName？

可以通过指定 `--watch-namespace` 的方式，不同的实例 watch 不同的 namespace。
ingress-nginx 可以通过 helm 安装时指定 `controller.scope.enabled=true` 和 `--set controller.scope.namespace=$NAMESPACE`，
更多信息可以参考 [scope](https://kubernetes.github.io/ingress-nginx/deploy/#scope)。
