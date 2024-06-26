# 开启ArgoCDUI 

为了方便用户直接在应用工作台中利用ArgoCD的原生UI查看ArgoCD的应用详情，我们提供了开启ArgoCD UI的功能。本文档将指导您如何开启ArgoCD UI功能。

> 注意，在UI中仅有只读权限，如果有其他操作需求，请通过工作台进行操作。

## 具体配置

开启ArgoCD的UI功能需要修改的配置项较多，并且配置项之间是相互影响的，请严格按照下面的步骤进行配置。

### 修改ArgoCD 配置
下述配置均在`kpanda-global-cluster`集群中, 并假设您的ArgoCD安装在`argocd`这个命名空间中。

前往【容器管理】-> 【集群列表】-> 【kpanda-global-cluster】-> 【自定义资源】-> 【yaml创建】，创建一下三个资源(`Gateway`,`VirtualService`,`GProductProxy`)。
1. 创建Gateway

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: argocd-gateway
  namespace: argocd  # 注意命名空间
spec:
  selector:
    istio: ingressgateway
  servers:
    - hosts:
        - '*'
      port:
        name: http
        number: 80
        protocol: HTTP
      tls:
        httpsRedirect: false                    
    - hosts:
        - '*'
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

2. 创建VirtualService

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: argocd-virtualservice
  namespace: argocd       # 注意命名空间
spec:
  gateways:
    - argocd-gateway
  hosts:
    - '*'
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

3. 创建GProductProxy

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
        host: argocd-server.argocd.svc.cluster.local
        port: 80
      match:
        uri:
          prefix: /argocd/applications/argocd   
    - authnCheck: false
      destination:
        host: argocd-server.argocd.svc.cluster.local   # 如果命名空间不是argocd，需要更改svc的名称
        port: 80
      match:
        uri:
          prefix: /argocd           
```

3. 修改ArgoCD的相关配置

前往【容器管理】-> 【集群列表】-> 【kpanda-global-cluster】-> 【配置与密钥】-> 【配置项】, 命名空间选择您安装的ArgoCD的命名空间,如 argocd, 分别修改一下configmap：

修改`argocd-cmd-params-cm`
```yaml
kind: ConfigMap
metadata:
  name: argocd-cmd-params-cm
  namespace: argocd
data:
  server.basehref: /argocd     
  server.insecure: 'true'      
  server.rootpath: /argocd      
```

修改`argocd-rbac-cm`
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

修改`argocd-cm`
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-cm
  namespace: argocd
data:
  accounts.amamba: apiKey
  accounts.amamba-view: apiKey   # 添加这一行
```

更改完上述选项后，需要重启`argocd-server`这个deployment. 
前往【容器管理】-> 【集群列表】-> 【kpanda-global-cluster】-> 【工作负载】-> 【无状态负载】,命名空间选择您安装的ArgoCD的命名空间,如 argocd。 找到`argocd-server`, 点击右侧的【重启】按钮。

### 修改Amamba配置项
前往【容器管理】-> 【集群列表】-> 【kpanda-global-cluster】-> 【配置与密钥】-> 【配置项】, 命名空间选择 `amamba-system`, 修改`amamba-config`这个configmap, 修改以下配置项：

```yaml
xxxxx
generic:
  argocd:
    host: argocd-server.argocd.svc.cluster.local:443  # 将端口改为443
    enableUI: true         # 添加这个选项
```
更改完上述选项后，前往【容器管理】-> 【集群列表】-> 【kpanda-global-cluster】-> 【工作负载】-> 【无状态负载】，命名空间选择 `amamba-system`, 分别重启`amamba-apiserver`和`amamba-syncer`这两个deployment。

