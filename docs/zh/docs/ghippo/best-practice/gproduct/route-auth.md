---
hide:
  - toc
---

# 接入路由和登录认证

接入后统一登录和密码验证，效果如下图：

![接入效果](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/gproduct02.png)

各个 GProduct 模块的 API bear token 验证都走 Istio Gateway。

接入后的路由映射图如下：

![接入效果](https://docs.daocloud.io/daocloud-docs-images/docs/ghippo/images/gproduct03.png)

## 接入方法

以 `kpanda` 为例注册 GProductProxy CR。

```yaml
# GProductProxy CR 示例, 包含路由和登录认证

# spec.proxies: 后写的路由不能是先写的路由子集, 反之可以
# spec.proxies.match.uri.prefix: 如果是后端 api, 建议在 prefix 末尾添加 "/" 表述这段 path 结束（特殊需求可以不用加）
# spec.proxies.match.uri: 支持 prefix 和 exact 模式; Prefix 和 Exact 只能 2 选 1; Prefix 优先级大于 Exact
 
apiVersion: ghippo.io/v1alpha1
kind: GProductProxy
metadata:
  name: kpanda  # (1)
spec:
  gproduct: kpanda  # (2)
  proxies:
  - labels:
      kind: UIEntry
    match:
      uri:
        prefix: /kpanda # (3)
    rewrite:
      uri: /index.html
    destination:
      host: ghippo-anakin.ghippo-system.svc.cluster.local
      port: 80
    authnCheck: false  # (4)
  - labels:
      kind: UIAssets
    match:
      uri:
        prefix: /ui/kpanda/ # (5)
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
        prefix: /apis/kpanda.io/v1 # (6)
    destination:
      host: kpanda-service.kpanda-system.svc.cluster.local
      port: 80
    authnCheck: true
```

1. cluster 级别 CRD
2. 需要用小写指定 GProduct 名字
3. 还可支持 exact
4. 是否需要 istio-gateway 给该条路由 API 作 AuthN Token 认证, false 为跳过认证
5. UIAssets 建议末尾添加 __/__ 表示结束（不然前端可能会出现问题）
6. 后写的路由不能是先写的路由的子集, 反之可以
