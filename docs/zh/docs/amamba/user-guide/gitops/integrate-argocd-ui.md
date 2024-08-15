# 开启 ArgoCD UI

为了方便用户直接在应用工作台中利用 ArgoCD 的原生 UI 查看 ArgoCD 的应用详情，
DCE 5.0 应用工作台提供了开启 ArgoCD UI 的功能。本文档将指导您如何开启 ArgoCD UI。

> 注意，在 UI 中仅有只读权限，如果有其他操作需求，请通过工作台进行操作。

## 具体配置

开启 ArgoCD 的 UI 功能需要修改的配置项较多，并且配置项之间是相互影响的，请严格按照下面的步骤进行配置。

### 修改 ArgoCD 配置

下述配置均在 `kpanda-global-cluster` 集群中，并假设您的 ArgoCD 安装在 `argocd` 这个命名空间中。

前往 __容器管理__ ->  __集群列表__ ->  __kpanda-global-cluster__ ->  __自定义资源__ ->  根据资源分组及版本搜索（ 即`apiVersion`字段。以 `Gateway`为例，搜索 `networking.istio.io`）-> __进入自定义资源详情__ -> 选择对应命名空间及版本 -> 右侧点击 Yaml 创建 ，
创建以下三个资源（`Gateway`、`VirtualService`、`GProductProxy`）。

1. 创建 Gateway

    ```yaml
    apiVersion: networking.istio.io/v1alpha3
    kind: Gateway
    metadata:
      name: argocd-gateway
      namespace: argocd # 注意命名空间
    spec:
      selector:
        istio: ingressgateway
      servers:
        - hosts:
            - "*"
          port:
            name: http
            number: 80
            protocol: HTTP
          tls:
            httpsRedirect: false
        - hosts:
            - "*"
          port:
            name: https
            number: 443
            protocol: HTTPS
          tls:
            cipherSuites:
              - ECDHE-ECDSA-AES128-GCM-SHA256
              - ECDHE-RSA-AES128-GCM-SHA256
              - ECDHE-ECDSA-AES128-SHA
              - AES128-GCM-SHA256
              - AES128-SHA
              - ECDHE-ECDSA-AES256-GCM-SHA384
              - ECDHE-RSA-AES256-GCM-SHA384
              - ECDHE-ECDSA-AES256-SHA
              - AES256-GCM-SHA384
              - AES256-SHA
            credentialName: argocd-secret
            maxProtocolVersion: TLSV1_3
            minProtocolVersion: TLSV1_2
            mode: SIMPLE
    ```

2. 创建 VirtualService

    ```yaml
    apiVersion: networking.istio.io/v1alpha3
    kind: VirtualService
    metadata:
      name: argocd-virtualservice
      namespace: argocd # 注意命名空间
    spec:
      gateways:
        - argocd-gateway
      hosts:
        - "*"
      http:
        - match:
            - uri:
                prefix: /argocd
          route:
            - destination:
                host: argocd-server
                port:
                  number: 80
    ```

3. 创建 GProductProxy

    ```yaml
    apiVersion: ghippo.io/v1alpha1
    kind: GProductProxy
    metadata:
      name: argocd
    spec:
      gproduct: amamba
      proxies:
        - authnCheck: false
          destination:
            host: amamba-argocd-server.argocd.svc.cluster.local
            port: 80
          match:
            uri:
              prefix: /argocd/applications/argocd
        - authnCheck: false
          destination:
            host: amamba-argocd-server.argocd.svc.cluster.local # 如果命名空间不是argocd，需要更改svc的名称
            port: 80
          match:
            uri:
              prefix: /argocd
    ```

host中的 `amamba-argocd-server.argocd.svc.cluster.local` 需要根据您的 ArgoCD 的服务名称和命名空间进行修改。具体可以通过 __容器管理__ ->  __集群列表__ ->  __kpanda-global-cluster__ -> __容器网络__ ，根据ArgoCD 安装的命名空间，搜索关键词 `argocd-server`来确定。 

4. 修改 ArgoCD 的相关配置

    前往 __容器管理__ ->  __集群列表__ ->  __kpanda-global-cluster__ ->  __工作负载__ ->  __无状态负载__ ，
    命名空间选择您安装的 ArgoCD 的命名空间，如 argocd。找到 `argocd-server`，点击右侧的 __重启__ 按钮。

    修改 `argocd-cmd-params-cm`

    ```yaml
    kind: ConfigMap
    metadata:
      name: argocd-cmd-params-cm
      namespace: argocd
    data:
      server.basehref: /argocd # 添加这三行
      server.insecure: "true"
      server.rootpath: /argocd
    ```

    修改 `argocd-rbac-cm`

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: argocd-rbac-cm
      namespace: argocd
    data:
      policy.csv: |-
        g, amamba, role:admin
        g, amamba-view, role:readonly   # 添加这一行
    ```

    修改 `argocd-cm`

    ```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: argocd-cm
      namespace: argocd
    data:
      accounts.amamba: apiKey
      accounts.amamba-view: apiKey # 添加这一行
    ```

5. 更改完上述选项后，需要重启 `argocd-server` 这个 Deployment。

    前往 __容器管理__ ->  __集群列表__ ->  __kpanda-global-cluster__ ->  __工作负载__ ->  __无状态负载__ ，
   命名空间选择您安装的 ArgoCD 的命名空间，如 argocd。 找到 `argocd-server`，点击右侧的 __重启__ 按钮。

### 修改 Amamba 配置项

经过上述步骤后，还需要更改 Aamamba 的配置项才能使 ArgoCD UI 生效。

前往 __容器管理__ ->  __集群列表__ ->  __kpanda-global-cluster__ ->  __配置与密钥__ ->  __配置项__ ，
命名空间选择 `amamba-system`，修改 `amamba-config` 这个 ConfigMap，修改以下配置项：

```yaml
generic:
argocd:
  host: amamba-argocd-server.argocd.svc.cluster.local:443  # 将端口改为443
  enableUI: true         # 添加这个选项
```
其中 host (**端口保持443**) 需要与上述 【创建 GProductProxy】 步骤中说明的一致。

更改完上述选项后，前往 __容器管理__ ->  __集群列表__ ->  __kpanda-global-cluster__ ->  __工作负载__ ->  __无状态负载__ ，
命名空间选择 `amamba-system`，分别重启 `amamba-apiserver` 和 `amamba-syncer` 这两个 Deployment。
