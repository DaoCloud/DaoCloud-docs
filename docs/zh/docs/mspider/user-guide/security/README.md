---
hide:
  - toc
---

# 安全治理

服务网格提供了一种[授权机制](./authorize.md)和两种认证方式（[请求身份认证](./request.md)和[对等身份认证](./peer.md)），
用户可以在服务网格中通过向导和 YAML 编写两种方式创建、编辑资源文件，
并可以针对网格全局、命名空间、工作负载三个层面创建规则。当资源创建成功后，Istiod 将转换为配置分发至边车代理执行。

![安全治理](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/images/security.png)

### 授权机制

服务网格提供的授权机制允许您控制对服务的访问。
使用授权机制，您可以定义规则，指定允许哪些服务相互通信。
这些规则可以基于各种因素，例如流量的源和目的地、使用的协议以及发出请求的客户端的身份。
通过使用 服务网格的授权机制，您可以确保只有经过授权的流量允许在您的服务网格中流动。

以下是如何使用 服务网格的授权机制限制两个服务之间流量的示例：

```yaml
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: my-auth-policy
spec:
  selector:
    matchLabels:
      app: my-service
  action: ALLOW
  rules:
  - from:
    - source:
        notNamespaces: ["my-namespace"]
    to:
    - operation:
        methods: ["GET"]
```

在此示例中，我们创建了一个 __AuthorizationPolicy__ 资源，允许流量从除 my-namespace 以外的任何命名空间流向 my-service 服务，但仅限于 GET 请求。
另请参见[图形界面的创建方式](./authorize.md)。

### 请求身份验证

请求身份验证用于验证向服务发出请求的客户端的身份。

以下是如何使用请求级身份验证验证客户端身份的示例：

```yaml
apiVersion: security.istio.io/v1beta1
kind: RequestAuthentication
metadata:
  name: my-authn-policy
spec:
  selector:
    matchLabels:
      app: my-service
  jwtRules:
  - issuer: "https://my-auth-server.com"
    jwksUri: "https://my-auth-server.com/.well-known/jwks.json"
```

在此示例中，我们创建了一个 __RequestAuthentication__ 资源，用于验证向 my-service 服务发出请求的客户端的身份。
我们使用 JSON Web Token（JWT）来验证客户端，指定了发行者和用于验证令牌的公钥的位置。
另请参见[图形界面的创建方式](./request.md)。

### 对等身份验证

对等身份验证用于验证服务本身的身份。服务网格提供了几种对等身份验证选项，包括双向 TLS 身份验证和基于 JSON Web Token 的身份验证。

以下是如何使用双向 TLS 身份验证验证服务身份的示例：

```yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: my-peer-authn-policy
spec:
  selector:
    matchLabels:
      app: my-service
  mtls:
    mode: STRICT
```

在此示例中，我们创建了一个 __PeerAuthentication__ 资源，要求 my-service 服务进行双向 TLS 身份验证。
我们使用 STRICT 模式，该模式要求客户端和服务器都提供有效的证书。
另请参见[图形界面的创建方式](./peer.md)。

更多说明，请参阅[服务网格身份和认证](./mtls.md)。
