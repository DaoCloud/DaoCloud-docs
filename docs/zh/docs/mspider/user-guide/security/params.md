# 安全治理参数配置

本页介绍有关对等身份认证、请求身份认证、授权策略相关的参数配置。

## 对等身份认证

采用图形向导模式时，[对等身份认证](./peer.md)分为基本配置和认证设置两步，各参数说明如下。

### 基本配置

| **UI 项**    | **YAML 字段**                        | **描述**                                                                                                                               |
| ------------ | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| 名称         | metadata.name                        | 必填。对等身份认证名称，同一个命名空间下不可重名。                                                                                     |
| 命名空间     | metadata.namespace                   | 必选。对等身份认证所属的命名空间。当选择网格的根命名空间时，将创建全局策略。全局策略仅能创建一个，需在界面中做检查，避免用户重复创建。 |
| 工作负载标签 | spec.selector                        | 可选。应用对等身份认证策略的工作负载选择标签，可添加多个标签，无需排序。                                                               |
| 标签名称     | spec.selector.matchLabels            | 必填。由小写字母、数字、连字符（-）、下划线（_）及小数点（.）组成                                                                      |
| 标签值       | spec.selector.matchLabels.{标签名称} | 必填。由小写字母、数字、连字符（-）、下划线（_）及小数点（.）组成                                                                      |

### 认证设置 - mTLS 模式

| **UI 项**                | **YAML 字段**      | **描述**                                                                                                                                                                                                |
| ------------------------ | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mTLS 模式                | spec.mTLS.mode     | 必填。用于设定命名空间的 mTLS 模式：<br />- UNSET：继承父级选项。否则视为 PERMISSIVE<br />- PERMISSIVE：明文和 mTLS 连接<br />- STRICT：仅 mTLS 连接<br />- DISABLE：仅明文连接                         |
| 为指定端口添加 mTLS 模式 | spec.portLevelMtls | 可选。针对指定端口设置 mTLS 规则，可添加多条规则，无需排序。<br />- UNSET：继承父级选项。否则视为 PERMISSIVE<br />- PERMISSIVE：明文和 mTLS 连接<br />- STRICT：仅 mTLS 连接<br />- DISABLE：仅明文连接 |

## 请求身份认证

采用图形向导模式时，[请求身份认证](./request.md)分为基本配置和认证设置两步，各参数说明如下。

### 基本配置

| **UI 项**    | **YAML 字段**                        | **描述**                                                                                                                                                                                   |
| ------------ | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 名称         | metadata.name                        | 必填。请求身份认证名称，同一个命名空间下不可重名。                                                                                                                                         |
| 命名空间     | metadata.namespace                   | 必选。请求身份认证所属的命名空间。当选择网格的根命名空间时，将创建全局策略。全局策略仅能创建一个，需在界面中做检查，避免用户重复创建。<br />同一个命名空间内，请求身份认证的名称不能重复。 |
| 工作负载标签 | spec.selector                        | 可选。应用请求身份认证策略的工作负载选择标签，可添加多条选择标签，无需排序。                                                                                                               |
| 标签名称     | spec.selector.matchLabels            | 必填。由小写字母、数字、连字符（-）、下划线（_）及小数点（.）组成                                                                                                                          |
| 标签值       | spec.selector.matchLabels.{标签名称} | 必填。由小写字母、数字、连字符（-）、下划线（_）及小数点（.）组成                                                                                                                          |

### 认证设置

| **UI 项**     | **YAML 字段**                   | **描述**                                                                                                           |
| ------------- | ------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| 添加 JWT 规则 | spec.jwtRules                   | 可选。用于用户请求认证的 JWT 规则，可添加多条规则。                                                                |
| Issuer        | spec.jwtRules.issuers           | 必填。JSON Web Token (JWT) 签发人信息。                                                                            |
| Audiences     | spec.jwtRules.issuers.Audiences | 可选。配置可访问的 audiences 列表，如果为空，将访问 service name。                                                 |
| jwksUri       | spec.jwtRules.issuers.jwksUri   | 可选。JSON Web Key (JWK) 的 JSON 文件路径，与 jwks 互斥，二选一。例如 <https://www.googleapis.com/oauth2/v1/certs> |
| jwks          | spec.jwtRules.issuers.jwks      | 可选。JSON Web Key Set (JWKS) 文件内容，与 jwksUri 互斥，二选一。                                                  |

更多请参阅 [OpenID Provider Metadata](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata)。

## 授权策略

采用图形向导模式时，[授权策略](./authorize.md)的创建分为`基本配置`和`策略设置`两步，各参数说明如下。

### 基本配置

| **可配置项** | **YAML 字段**                        | **描述**                                                                                                                                                             |
| ------------ | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 名称         | metadata.name                        | 必填。授权的策略名称。                                                                                                                                               |
| 命名空间     | metadata.namespace                   | 必选。授权策略所属命名空间，当选择网格根命名空间时，将创建全局策略，全局策略仅能创建一个，需在界面做检查，避免用户重复创建。同一个命名空间内，请求身份认证不可重名。 |
| 工作负载标签 | spec.selector                        | 可选。应用授权策略的工作负载选择标签，可添加多条选择标签，无需排序。                                                                                                 |
| 标签名称     | spec.selector.matchLabels            | 可选。由小写字母、数字、连字符（-）、下划线（_）及小数点（.）组成。                                                                                                  |
| 标签值       | spec.selector.matchLabels.{标签名称} | 可选。由小写字母、数字、连字符（-）、下划线（_）及小数点（.）组成。                                                                                                  |

### 策略设置

| **可配置项** | **YAML 字段**      | **描述**                                                                                                                                                          |
| ------------ | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 策略动作     | spec.action        | 可选。包含：<br />- 允许（allow）<br />- 拒绝（deny）<br />- 审计（audit）<br />- 自定义（custom）<br />选择自定义时，增加`provider`输入项。                      |
| Provider     | spec.provider.name | 必填。仅在`策略动作`选择为`自定义`时，才显示该输入框。                                                                                                            |
| 请求策略     | spec.rules         | 可选。包含请求来源、请求操作、策略条件三部分，可添加多条，按顺序执行。                                                                                            |
| 添加请求来源 | spec.rules.-from   | 可选。请求来源可基于命名空间、IP 段等进行定义，可添加多条。各项参数参见下文 [请求来源 Source](#source)。                                                          |
| 添加请求操作 | spec.rules.-to     | 可选。请求操作是对筛选出的请求执行的操作，例如发送至指定端口或主机，可添加多个操作。各项参数参见下文[请求操作 Operation](#operation)。                            |
| 添加策略条件 | spec.rules.-when   | 必填。策略条件是一个可选设置，可以增加类似黑名单（values）、白名单的限制条件（notValues），可添加多个策略条件。各项参数参见下文[策略条件 Condition](#condition)。 |

#### 请求来源 Source

您可以增加请求来源（Source）。Source 指定一个请求的来源身份，对请求来源中的字段执行逻辑与运算。

例如，如果 Source 是：

- 主体为“admin”或“dev”
- 命名空间为“prod”或“test”
- 且 ip 不是“1.2.3.4”.

匹配的 YAML 内容为：

```yaml
principals: ["admin", "dev"]
namespaces: ["prod", "test"]
notIpBlocks: ["1.2.3.4"]
```

具体字段说明如下：

| Key 字段               | 类型       | 描述                                                                                                                                                                                                                                                                                                       |
| ---------------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `principals`           | `string[]` | 可选。从对等证书衍生的对等身份列表。对等身份的格式为 `"<TRUST_DOMAIN>/ns/<NAMESPACE>/sa/<SERVICE_ACCOUNT>"`，例如 `"cluster.local/ns/default/sa/productpage"`。此字段要求启用 mTLS，且等同于 `source.principal` 属性。如果不设置，则允许所有主体。                                                         |
| `notPrincipals`        | `string[]` | 可选。对等身份的反向匹配列表。                                                                                                                                                                                                                                                                             |
| `requestPrincipals`    | `string[]` | 可选。从 JWT 派生的请求身份列表。请求身份的格式为 `"<ISS>/<SUB>"`，例如 `"example.com/sub-1"`。此字段要求启用请求身份验证，且等同于 `request.auth.principal` 属性。如果不设置，则允许所有请求主体。                                                                                                        |
| `notRequestPrincipals` | `string[]` | 可选。请求身份的反向匹配列表。                                                                                                                                                                                                                                                                             |
| `namespaces`           | `string[]` | 可选。从对等证书衍生的命名空间。此字段要求启用 mTLS，且等同于 `source.namespace` 属性。如果不设置，则允许所有命名空间。                                                                                                                                                                                    |
| `notNamespaces`        | `string[]` | 可选。命名空间的反向匹配列表。                                                                                                                                                                                                                                                                             |
| `ipBlocks`             | `string[]` | 可选。根据 IP 数据包的来源地址进行填充的 IP 段列表。支持单个 IP（例如“1.2.3.4”）和 CIDR（例如“1.2.3.0/24”）。这等同于 `source.ip` 属性。如果不设置，则允许所有 IP。                                                                                                                                        |
| `notIpBlocks`          | `string[]` | 可选。IP 段的反向匹配列表。                                                                                                                                                                                                                                                                                |
| `remoteIpBlocks`       | `string[]` | 可选。根据 X-Forwarded-For 标头或代理协议进行填充的 IP 段列表。要使用此字段，您必须在安装 Istio 或在 ingress 网关使用注解时在 meshConfig 下配置 gatewayTopology 的 numTrustedProxies 字段。支持单个 IP（例如“1.2.3.4”）和 CIDR（例如“1.2.3.0/24”）。这等同于 `remote.ip` 属性。如果不设置，则允许所有 IP。 |
| `notRemoteIpBlocks`    | `string[]` | 可选。远程 IP 段的反向匹配列表。                                                                                                                                                                                                                                                                           |

#### 请求操作 Operation

您可以增加请求操作（Operation）。Operation 指定请求的操作，对操作中的字段执行逻辑与操作。

例如，以下操作将匹配：

- 主机后缀为“.example.com”
- 方法为“GET”或“HEAD”
- 补丁没有前缀“/admin”

```yaml
hosts: ["*.example.com"]
methods: ["GET", "HEAD"]
notPaths: ["/admin*"]
```

| Key 字段     | 类型       | 描述                                                                                                                                            |
| ------------ | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `hosts`      | `string[]` | 可选。在 HTTP 请求中指定的主机列表。不区分大小写。如果不设置，则允许所有主机。仅适用于 HTTP。                                                   |
| `notHosts`   | `string[]` | 可选。在 HTTP 请求中指定的主机反向匹配列表。不区分大小写。                                                                                      |
| `ports`      | `string[]` | 可选。连接中指定的端口列表。如果不设置，则允许所有端口。                                                                                        |
| `notPorts`   | `string[]` | 可选。连接中所指定端口的反向匹配列表。                                                                                                          |
| `methods`    | `string[]` | 可选。HTTP 请求中指定的方法列表。对于 gRPC 服务，这将始终是“POST”。如果不设置，则允许所有方法。仅适用于 HTTP。                                  |
| `notMethods` | `string[]` | 可选。HTTP 请求中所指定方法的反向匹配列表。                                                                                                     |
| `paths`      | `string[]` | 可选。HTTP 请求中指定的路径列表。对于 gRPC 服务，这将是“/package.service/method”格式的完全限定名称。如果不设置，则允许所有路径。仅适用于 HTTP。 |
| `notPaths`   | `string[]` | 可选。路径的反向匹配列表。                                                                                                                      |

**在实际的操作情况中，另外需要注意添加，一些通用的 key**

- request.headers[User-Agent]
- request.auth.claims[iss]
- experimental.envoy.filters.network.mysql_proxy[db.table]

更多关于 `AuthorizationPolicy` 的配置参数参数说明，请参考<https://istio.io/latest/docs/reference/config/security/conditions/> 的说明。

#### 策略条件 Condition

您还可以增加策略条件 (Condition)。Condition 指定其他必需的属性。

| Key 字段                       | 描述                                                                               | 支持的协议   | Value 示例                                    |
| ------------------------------ | ---------------------------------------------------------------------------------- | ------------ | --------------------------------------------- |
| `request.headers`              | `HTTP` 请求头，需要用 `[]` 括起来                                                  | HTTP only    | `["Mozilla/*"]`                               |
| `source.ip`                    | 源 `IP` 地址，支持单个 `IP` 或 `CIDR`                                              | HTTP and TCP | `["10.1.2.3"]`                                |
| `remote.ip`                    | 由 `X-Forwarded-For` 请求头或代理协议确定的原始客户端 IP 地址，支持单个 IP 或 CIDR | HTTP and TCP | `["10.1.2.3", "10.2.0.0/16"]`                 |
| `source.namespace`             | 源负载实例命名空间，需启用双向 TLS                                                 | HTTP and TCP | `["default"]`                                 |
| `source.principal`             | 源负载的标识，需启用双向 TLS                                                       | HTTP and TCP | `["cluster.local/ns/default/sa/productpage"]` |
| `request.auth.principal`       | 已认证过 `principal` 的请求                                                        | HTTP only    | `["accounts.my-svc.com/104958560606"]`        |
| `request.auth.audiences`       | 此身份验证信息的目标主体                                                           | HTTP only    | `["my-svc.com"]`                              |
| `request.auth.presenter`       | 证书的颁发者                                                                       | HTTP only    | `["123456789012.my-svc.com"]`                 |
| `request.auth.claims`          | `Claims` 来源于 `JWT`。需要用 `[]` 括起来                                          | HTTP only    | `["*@foo.com"]`                               |
| `destination.ip`               | 目标 `IP` 地址，支持单个 `IP` 或 `CIDR`                                            | HTTP and TCP | `["10.1.2.3", "10.2.0.0/16"]`                 |
| `destination.port`             | 目标 `IP` 地址上的端口，必须在 `[0，65535]` 范围内                                 | HTTP and TCP | `["80", "443"]`                               |
| `connection.sni`               | 服务器名称指示，需启用双向 TLS                                                     | HTTP and TCP | `["www.example.com"]`                         |
| `experimental.envoy.filters.*` | 用于过滤器的实验性元数据匹配，包装的值 `[]` 作为列表匹配                           | HTTP and TCP | `["[update]"]`                                |

!!! note

    无法保证 `experimental.*` 密钥向后的兼容性，可以随时将它们删除，但须谨慎操作。

