# 接入路由和 AuthN

接入后统一登录和密码验证，效果如下图：

[接入效果](../images/gproduct02.png)

各个 GProduct 模块的 API bear token 验证都走 Istio Gateway。

接入后的路由映射图如下：

[接入效果](../images/gproduct03.png)

## 接入方法

以 `kpanda` 为例注册 GProductProxy CR。

```yaml
# GProductProxy CR 示例, 包含路由和 AuthN
 
# spec.proxies: 后写的路由不能是先写的路由子集, 反之可以
# spec.proxies.match.uri.prefix: 如果是后端 api, 建议在 prefix 末尾添加 "/" 表述这段 path 结束（特殊需求可以不用加）
# spec.proxies.match.uri: 支持 prefix 和 exact 模式; Prefix 和 Exact 只能 2 选 1; Prefix 优先级大于 Exact
 
apiVersion: ghippo.io/v1alpha1
kind: GProductProxy
metadata:
  name: kpanda  # cluster 级别 CRD
spec:
  gproduct: kpanda  # 需要用小写指定 GProduct 名字
  proxies:
  - labels:
      kind: UIEntry
    match:
      uri:
        prefix: /kpanda # 还可支持 exact:   
    rewrite:
      uri: /index.html
    destination:
      host: ghippo-anakin.ghippo-system.svc.cluster.local
      port: 80
    authnCheck: false  # 是否需要 istio-gateway 给该条路由 API 作 AuthN Token 认证, false 为跳过认证
  - labels:
      kind: UIAssets
    match:
      uri:
        prefix: /ui/kpanda/ # UIAssets 建议末尾添加 "/" 表示结束（不然前端可能会出现问题）
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
        prefix: /apis/kpanda.io/v1 # 后写的路由不能是先写的路由的子集, 反之可以
    destination:
      host: kpanda-service.kpanda-system.svc.cluster.local
      port: 80
    authnCheck: true
```

!!! note

    `ghippo-controller-manager` 会把 GProductProxy 转换成 Istio CR 资源 VirtualService 和 AuthorizationPolicy。

转换后的 Istio VirtualService CR 示例：

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: kpanda-vs
  namespace: kpanda-system
spec:
  exportTo:
    - "*"  # Match all namespaces
  hosts:
    - "*"  # Allow IP access
  gateways:
    - ghippo-system/ghippo-gateway
  http:
  - match:
    - uri:
        prefix: /kpanda
    rewrite:
      uri: /index.html
    route:
    - destination:
        host: ghippo-anakin.ghippo-system.svc.cluster.local  # Parent APP UI
        port:
          number: 80
  - match:
    - uri:
        prefix: /ui/kpanda
    route:
    - destination:
        host: kpanda-ui.kpanda-system.svc.cluster.local  # GProduct UI
        port:
          number: 80
  - match:
    - uri:
        prefix: /apis/kpanda.io/v1
    route:
    - destination:
        host: kpanda-service.kpanda-system.svc.cluster.local  # GProduct Service
        port:
          number: 80  # GProduct Service port
```

转换后的 Istio AuthorizationPolicy CR 示例：

```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: kpanda-ap
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: istio-ingressgateway
  action: ALLOW
  rules:
  - to:
    - operation:
        # 列出不需要作AuthN验证就能通过的api
        paths:
        - /apis/kpanda.io/v1/swagger/*
        - /ui/kpanda*
        - /kpanda*
```
