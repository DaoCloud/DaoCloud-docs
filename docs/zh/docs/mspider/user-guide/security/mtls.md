# 服务网格身份和认证

身份 (Identity) 是任何安全基础架构的基本概念。
在工作负载间开始通信时，通信双方必须交换包含身份信息的凭证以进行双向验证。
在客户端，根据[安全命名](#_5)信息检查服务器的标识，以查看它是否是工作负载授权的运行程序。
在服务器端，服务器可以根据授权策略确定客户端可以访问哪些信息，
审计谁在什么时间访问了什么，根据他们使用的工作负载向客户收费，
并拒绝任何未能支付账单的客户访问工作负载。

DCE 5.0 服务网格身份模型使用经典的 __service identity__ （服务身份）来确定一个请求源端的身份。
这种模型有极好的灵活性和粒度，可以用服务身份来标识人类用户、单个工作负载或一组工作负载。
在没有服务身份的平台上，服务网格可以使用其它可以对服务实例进行分组的身份，例如服务名称。

下面的列表展示了在不同平台上可以使用的服务身份：

- Kubernetes：Kubernetes 服务帐户
- GKE/GCE：GCP 服务帐户
- 本地（非 Kubernetes）：用户帐户、自定义服务帐户、服务名称、
  服务网格服务帐户或 GCP 服务帐户。自定义服务帐户引用现有服务帐户，
  就像客户的身份目录管理的身份一样。

## 身份和证书管理

服务网格 PKI (Public Key Infrastructure, 公钥基础设施) 使用 X.509 证书为每个工作负载都提供强大的身份标识。
 __istio-agent__ 与每个 Envoy 代理一起运行，与 __istiod__ 
一起协作来自动化的进行大规模密钥和证书轮换。下图显示了这个机制的运行流程。

![workflow](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/id-prov.svg)

服务网格通过以下流程提供密钥和证书：

1. __istiod__ 提供 gRPC 服务以接受[证书签名请求](https://en.wikipedia.org/wiki/Certificate_signing_request)（CSRs）。
1. __istio-agent__ 在启动时创建私钥和 CSR，然后将 CSR 及其凭据发送到 __istiod__ 进行签名。
1. __istiod__ CA 验证 CSR 中携带的凭据，成功验证后签署 CSR 以生成证书。
1. 当工作负载启动时，Envoy 通过[秘密发现服务（SDS）](https://www.envoyproxy.io/docs/envoy/latest/configuration/security/secret#secret-discovery-service-sds)API 向同容器内的 __istio-agent__ 发送证书和密钥请求。
1. __istio-agent__ 通过 Envoy SDS API 将从 __istiod__ 收到的证书和密钥发送给 Envoy。
1. __istio-agent__ 监控工作负载证书的过期时间。上述过程会定期重复进行证书和密钥轮换。

## 认证

服务网格提供两种类型的认证：

- __对等身份认证__ ：用于服务到服务的认证，以验证建立连接的客户端。
  服务网格提供[双向 TLS](https://en.wikipedia.org/wiki/Mutual_authentication)
  作为传输认证的全栈解决方案，无需更改服务代码就可以启用它。这个解决方案：
    - 为每个服务提供强大的身份，表示其角色，以实现跨集群和云的互操作性。
    - 保护服务到服务的通信。
    - 提供密钥管理系统，以自动进行密钥和证书的生成、分发和轮换。
- __请求身份认证__ ：用于终端用户认证，以验证附加到请求的凭据。
  服务网格使用 JSON Web Token（JWT）验证启用请求级认证，
  并使用自定义认证实现或任何 OpenID Connect 的认证实现（例如下面列举的）来简化的开发人员体验。
    - [ORY Hydra](https://www.ory.sh/)
    - [Keycloak](https://www.keycloak.org/)
    - [Auth0](https://auth0.com/)
    - [Firebase Auth](https://firebase.google.com/docs/auth/)
    - [Google Auth](https://developers.google.com/identity/protocols/OpenIDConnect)

在所有情况下，服务网格都通过自定义 Kubernetes API 将认证策略存储在 __Istio config store__ 。
Istiod 使每个代理保持最新状态，
并在适当时提供密钥。此外，服务网格的认证机制支持宽容模式（permissive mode），
以帮助您在强制实施前了解策略更改将如何影响您的安全状况。

### mTLS 认证

mTLS 全称为 Mutual Transport Layer Security，即双向传输层安全认证。
mTLS 允许通信双方在 SSL/TLS 握手的初始连接期间进行相互认证。

DCE 5.0 服务网格通过客户端和服务器端
[PEP](https://www.jerichosystems.com/technology/glossaryterms/policy_enforcement_point.html)(Policy Enforcement Policy)
建立服务到服务的通信通道，PEP 被实现为[Envoy 代理](https://www.envoyproxy.io/)。
当一个工作负载使用 mTLS 认证向另一个工作负载发送请求时，
该请求的处理方式如下：

1. 服务网格将出站流量从客户端重新路由到客户端的本地边车 Envoy。
1. 客户端 Envoy 与服务器端 Envoy 开始双向 TLS 握手。在握手期间，
   客户端 Envoy 还做了[安全命名](#_5)检查，
   以验证服务器证书中显示的服务帐户是否被授权运行目标服务。
1. 客户端 Envoy 和服务器端 Envoy 建立了一个双向的 TLS 连接，
   服务网格将流量从客户端 Envoy 转发到服务器端 Envoy。
1. 服务器端 Envoy 授权请求。如果获得授权，它将流量转发到通过本地 TCP 连接的后端服务。

服务网格将 __TLSv1_2__ 作为最低 TLS 版本为客户端和服务器配置了如下的加密套件：

- __ECDHE-ECDSA-AES256-GCM-SHA384__ 
- __ECDHE-RSA-AES256-GCM-SHA384__ 
- __ECDHE-ECDSA-AES128-GCM-SHA256__ 
- __ECDHE-RSA-AES128-GCM-SHA256__ 
- __AES256-GCM-SHA384__ 
- __AES128-GCM-SHA256__ 

#### 宽容模式

服务网格双向 TLS 具有一个宽容模式（permissive mode），
允许服务同时接受纯文本流量和双向 TLS 流量。这个功能极大地提升了双向 TLS 的入门体验。

在运维人员希望将服务移植到启用了双向 TLS 的 服务网格上时，
许多非 服务网格客户端与非 服务网格服务器端之间的通信会产生问题。
通常情况下，运维人员无法同时为所有客户端安装 服务网格边车，
甚至在某些客户端上没有这样做的权限。即使在服务器端上安装了 服务网格边车，
运维人员也无法在不中断现有连接的情况下启用双向 TLS。

启用宽容模式后，服务可以同时接受纯文本和双向 TLS 流量。
这个模式为入门提供了极大的灵活性。服务器中安装的服务网格边车
立即接受双向 TLS 流量而不会打断现有的纯文本流量。因此，
运维人员可以逐步安装和配置客户端 服务网格边车 发送双向 TLS 流量。
一旦客户端配置完成，运维人员便可以将服务器端配置为仅 TLS 模式。

#### 安全命名

服务器身份（Server identity）被编码在证书里，
但服务名称（service name）通过服务发现或 DNS 被检索。
安全命名信息将服务器身份映射到服务名称。身份 __A__ 到服务名称 __B__ 
的映射表示“授权 __A__ 运行服务 __B__ "。控制平面监视 __apiserver__ ，
生成安全命名映射，并将其安全地分发到 PEP。
以下示例说明了为什么安全命名对身份验证至关重要。

假设运行服务 __datastore__ 的合法服务器仅使用 __infra-team__ 身份。
恶意用户拥有 __test-team__ 身份的证书和密钥。
恶意用户打算模拟合法服务以检查从客户端发送的数据。
恶意用户使用证书和 __test-team__ 身份的密钥部署伪造服务器。
假设恶意用户成功劫持（通过 DNS 欺骗、BGP/路由劫持、ARP 欺骗等）发送到
 __datastore__ 的流量并将其重定向到伪造的服务器。

当客户端调用 __datastore__ 服务时，它从服务器的证书中提取 __test-team__ 身份，
并用安全命名信息检查 __test-team__ 是否被允许运行 __datastore__ 。
客户端检测到 __test-team__ 不允许运行 __datastore__ 服务，认证失败。

请注意，对于非 HTTP/HTTPS 流量，安全命名不能保护其免于 DNS 欺骗，
如攻击者劫持了 DNS 并修改了目的地 IP 地址。这是因为 TCP 流量不包含主机名信息，
Envoy 只能依靠目的地 IP 地址进行路由，因此 Envoy 有可能将流量路由到劫持
IP 地址所在的服务上。这种 DNS 欺骗甚至可以在客户端 Envoy 接收到流量之前发生。

### 认证架构

您可以使用 __对等身份认证__ 和 __请求身份认证__ 策略为在服务网格中接收请求的工作负载指定认证要求。
网格运维人员使用 __.yaml__ 文件来指定策略。部署后，策略将保存在 服务网格配置存储中。
服务网格控制器监视配置存储。

在任何的策略变更时，新策略都会转换为适当的配置，告知 PEP 如何执行所需的认证机制。
控制平面可以获取公钥并将其附加到 JWT 验证的配置中。作为替代方案，
Istiod 提供了 服务网格系统管理的密钥和证书的路径，并将它们安装到应用程序 Pod 用于双向 TLS。

服务网格异步发送配置到目标端点。代理收到配置后，新的认证要求会立即生效。

发送请求的客户端服务负责遵循必要的认证机制。对于 __请求身份认证__ ，
应用程序负责获取 JWT 凭证并将其附加到请求。对于 __对等身份认证__ ，
服务网格自动将两个 PEP 之间的所有流量升级为双向 TLS。如果认证策略禁用了双向 TLS 模式，
则服务网格将继续在 PEP 之间使用纯文本。要覆盖此行为，
请使用[目标规则](../traffic-governance/destination-rules.md)显式禁用双向 TLS 模式。

![](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/authz.svg)

服务网格将这两种认证类型以及凭证中的其他声明（如果适用）输出到下一层：[授权](./authorize.md)。

### 认证策略

本节中提供了更多服务网格认证策略方面的细节。正如[认证架构](#_6)中所说的，
认证策略是对服务收到的请求生效的。要在双向 TLS 中指定客户端认证策略，
需要在 __DetinationRule__ 中设置 __TLSSettings__ 。

和其他的 服务网格配置一样，可以用 __.yaml__ 文件的形式来编写认证策略。部署策略使用 __kubectl__ 。
下面例子中的认证策略要求：与带有 __app:reviews__ 标签的工作负载的传输层认证，必须使用双向 TLS：

```yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: "example-peer-policy"
  namespace: "foo"
spec:
  selector:
    matchLabels:
      app: reviews
  mtls:
    mode: STRICT
```

#### 策略存储

服务网格将网格范围的策略存储在根命名空间。这些策略使用一个空的 selector
应用到网格中的所有工作负载。具有命名空间范围的策略存储在相应的命名空间中。
它们仅适用于其命名空间内的工作负载。如果您配置了 __selector__ 字段，
则认证策略仅适用于与您配置的条件匹配的工作负载。

Peer 和 __请求身份认证__ 策略用 kind 字段区分，
分别是 __PeerAuthentication__ 和 __RequestAuthentication__ 。

#### Selector 字段

Peer 和 __请求身份认证__ 策略使用 __selector__ 字段来指定该策略适用的工作负载的标签。
以下示例显示适用于带有 __app：product-page__ 标签的工作负载的策略的 selector 字段：

```yaml
selector:
  matchLabels:
    app: product-page
```

如果您没有为 __selector__ 字段提供值，
则 服务网格会将策略与策略存储范围内的所有工作负载进行匹配。
因此， __selector__ 字段可帮助您指定策略的范围：

- 网格范围策略：为根命名空间指定的策略，不带或带有空的 __selector__ 字段。
- 命名空间范围的策略：为非root命名空间指定的策略，不带有或带有空的 __selector__ 字段。
- 特定于工作负载的策略：在常规命名空间中定义的策略，带有非空 __selector__ 字段。

Peer 和 __请求身份认证__ 策略对 __selector__ 字段遵循相同的层次结构原则，
但是 服务网格以略微不同的方式组合和应用这些策略。

只能有一个网格范围的 __对等身份认证__ 策略，
每个命名空间也只能有一个命名空间范围的 __对等身份认证__ 策略。
当您为同一网格或命名空间配置多个网格范围或命名空间范围的 __对等身份认证__ 策略时，
服务网格会忽略较新的策略。当多个特定于工作负载的 __对等身份认证__ 策略匹配时，
服务网格将选择最旧的策略。

服务网格按照以下顺序为每个工作负载应用最窄的匹配策略：

1. 特定于工作负载的
1. 命名空间范围
1. 网格范围

服务网格可以将所有匹配的 __请求身份认证__ 策略组合起来，
就像它们来自单个 __请求身份认证__ 策略一样。因此，
您可以在网格或命名空间中配置多个网格范围或命名空间范围的策略。
但是，避免使用多个网格范围或命名空间范围的 __请求身份认证__ 策略仍然是一个好的实践。

#### __对等身份认证__ 

 __对等身份认证__ 策略指定 服务网格对目标工作负载实施的双向 TLS 模式。支持以下模式：

- PERMISSIVE：工作负载接受双向 TLS 和纯文本流量。
  此模式在迁移因为没有边车 而无法使用双向 TLS 的工作负载的过程中非常有用。
  一旦工作负载完成边车 注入的迁移，应将模式切换为 STRICT。
- STRICT： 工作负载仅接收双向 TLS 流量。
- DISABLE：禁用双向 TLS。从安全角度来看，除非您提供自己的安全解决方案，否则请勿使用此模式。
- UNSET：继承父作用域的模式。UNSET 模式的网格范围 __对等身份认证__ 策略默认使用 __PERMISSIVE__ 模式。

下面的 __对等身份认证__ 策略要求命名空间 __foo__ 中的所有工作负载都使用双向 TLS：

```yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: "example-policy"
  namespace: "foo"
spec:
  mtls:
    mode: STRICT
```

对于特定于工作负载的 __对等身份认证__ 策略，可以为不同的端口指定不同的双向 TLS 模式。
您只能将端口范围的双向 TLS 配置在工作负载声明过的端口上。
以下示例为 __app:example-app__ 工作负载禁用了端口 80 上的双向 TLS，
并对所有其他端口使用命名空间范围的 __对等身份认证__ 策略的双向 TLS 设置：

```yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: "example-workload-policy"
  namespace: "foo"
spec:
  selector:
     matchLabels:
       app: example-app
  portLevelMtls:
    80:
      mode: DISABLE
```

上面的 __对等身份认证__ 策略仅在有如下 Service 定义时工作，
将流向 __example-service__ 服务的请求绑定到 __example-app__ 
工作负载的 __80__ 端口

```yaml
apiVersion: v1
kind: Service
metadata:
  name: example-service
  namespace: foo
spec:
  ports:
  - name: http
    port: 8000
    protocol: TCP
    targetPort: 80
  selector:
    app: example-app
```

#### __请求身份认证__

__请求身份认证__ 策略指定验证 JSON Web Token（JWT）所需的值。这些值包括：

- token 在请求中的位置
- 请求的 issuer
- 公共 JSON Web Key Set（JWKS）

服务网格会根据 __请求身份认证__ 策略中的规则检查提供的令牌（如果已提供），
并拒绝令牌无效的请求。当请求不带有令牌时，默认将接受这些请求。
要拒绝没有令牌的请求，请提供授权规则，该规则指定对特定操作（例如，路径或操作）的限制。

如果 __请求身份认证__ 策略使用唯一的位置，则可以在这些策略中指定多个 JWT。
当多个策略与一个工作负载匹配时，服务网格会将所有规则组合起来，
就好像这些规则被指定为单个策略一样。此行为对于开发接受来自不同 JWT 提供者的工作负载时很有用。
但是，不支持具有多个有效 JWT 的请求，因为此类请求的输出主体未被定义。

#### Principal

使用 __对等身份认证__ 策略和双向 TLS 时，服务网格将身份从 __对等身份认证__ 提取到 __source.principal__ 中。
同样，当您使用 __请求身份认证__ 策略时，服务网格会将 JWT 中的身份赋值给 __request.auth.principal__ 。
使用这些 principal 设置授权策略并作为遥测的输出。

### 更新认证策略

您可以随时更改认证策略，服务网格几乎实时将新策略推送到工作负载。
但是，服务网格无法保证所有工作负载都同时收到新政策。
以下建议有助于避免在更新认证策略时造成干扰：

- 将 __对等身份认证__ 策略的模式从 __DISABLE__ 更改为 __STRICT__ 时，
  请使用 __PERMISSIVE__ 模式来过渡，反之亦然。当所有工作负载成功切换到所需模式时，
  您可以将策略应用于最终模式。您可以使用 服务网格遥测技术来验证工作负载已成功切换。
- 将 __请求身份认证__ 策略从一个 JWT 迁移到另一个 JWT 时，
  将新 JWT 的规则添加到该策略中，而不删除旧规则。这样，
  工作负载将接受两种类型的 JWT，当所有流量都切换到新的 JWT 时，
  您可以删除旧规则。但是，每个 JWT 必须使用不同的位置。

下一步：设置[对等身份认证](./peer.md)和[请求身份认证](./request.md)
