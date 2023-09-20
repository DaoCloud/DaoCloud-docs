---
hide:
  - toc
---

# 多云路由

多云路由是对标准的 Kubernetes Ingress 多云的统一抽象，通过创建一个 Ingress 并与若干多云服务关联，即可同时分发到多个集群内。

目前提供了两种创建方式：表单创建和 YAML 创建。本文以表单创建为例，参照以下步骤操作。

1. 进入某一个多云实例后，在左侧导航栏中，点击`资源管理` -> `多云路由`，点击右上角的`创建`按钮。

    ![路由列表](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/create-ingress01.png)

2. 在`创建多云路由`页面中，配置部署位置、设置路由规则、Ingress Class、是否开启会话保持等信息后，点击`确定`。填写详情可参考[创建路由](../../kpanda/user-guide/network/create-ingress.md)

    ![创建多云路由](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/create-ingress02.png)

3. 新功能尝鲜，支持一键将子集群服务转换为多云路由，点击列表页的`立即体验`，选择指定工作集群和命名空间下的路由，点击确定后可以转换成功。

    ![一键转换](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/create-ingress03.png)

4. 点击列表右侧的 `⋮`，可以更新和删除该路由。

    ![更新和删除](https://docs.daocloud.io/daocloud-docs-images/docs/kairship/images/create-ingress04.png)

    !!! note

        如果一个路由被删除，该服务相关的信息也将消失，请谨慎操作。

## YAML 示例

此处列出一个多云路由的 YAML 示例，您稍加修改就可以使用。

```yaml
kind: Ingress
apiVersion: networking.k8s.io/v1
metadata:
  name: ingress-test
  namespace: default
  uid: 49a45f23-2e5a-4a23-9f21-77418c1b9bbb
  resourceVersion: '1979660'
  generation: 1
  creationTimestamp: '2023-04-27T00:07:43Z'
  labels:
    propagationpolicy.karmada.io/name: ingress-ingress-test-ygddx
    propagationpolicy.karmada.io/namespace: default
  annotations:
    shadow.clusterpedia.io/cluster-name: k-kairship-jxy
spec:
  rules:
    - host: testing.daocloud.io
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: test-service
                port:
                  number: 123
status:
  loadBalancer: {}
```
