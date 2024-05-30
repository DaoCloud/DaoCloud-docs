# Security Governance Parameters

This page introduces the parameters related to peer authentication, request authentication, and authorization policies.

## Peer Authentication

When using the graphical wizard mode, [peer authentication](./peer.md) is divided into basic configuration and authentication settings. The parameters are described as follows.

### Basic Configuration

| UI Item | YAML Field | Description |
| ------- | ---------- | ----------- |
| Name | metadata.name | Required. The name of peer authentication, which cannot be duplicated within the same namespace. |
| Namespace | metadata.namespace | Required. The namespace to which the peer authentication belongs. When selecting the root namespace of the mesh, a global policy will be created. Only one global policy can be created, so it needs to be checked in the interface to avoid duplicate creation by users. |
| Workload Labels | spec.selector | Optional. The labels for selecting workloads to apply the peer authentication policy. Multiple labels can be added without sorting. |
| Label Name | spec.selector.matchLabels | Required. Consists of lowercase letters, numbers, hyphens (-), underscores (_), and periods (.). |
| Label Value | spec.selector.matchLabels.{label name} | Required. Consists of lowercase letters, numbers, hyphens (-), underscores (_), and periods (.). |

### Authentication Settings - mTLS Mode

| UI Item | YAML Field | Description |
| ------- | ---------- | ----------- |
| mTLS Mode | spec.mTLS.mode | Required. Used to set the mTLS mode for the namespace:<br />- UNSET: Inherits the parent option. Otherwise, considered as PERMISSIVE.<br />- PERMISSIVE: plaintext and mTLS connections.<br />- STRICT: mTLS connections only.<br />- DISABLE: plaintext connections only. |
| Add mTLS Mode for Specified Ports | spec.portLevelMtls | Optional. Sets the mTLS mode for specified ports. Multiple rules can be added without sorting.<br />- UNSET: Inherits the parent option. Otherwise, considered as PERMISSIVE.<br />- PERMISSIVE: plaintext and mTLS connections.<br />- STRICT: mTLS connections only.<br />- DISABLE: plaintext connections only. |

## Request Authentication

When using the graphical wizard mode, [request authentication](./request.md) is divided into basic configuration and authentication settings. The parameters are described as follows.

### Basic Configuration

| UI Item | YAML Field | Description |
| ------- | ---------- | ----------- |
| Name | metadata.name | Required. The name of request authentication, which cannot be duplicated within the same namespace. |
| Namespace | metadata.namespace | Required. The namespace to which the request authentication belongs. When selecting the root namespace of the mesh, a global policy will be created. Only one global policy can be created, so it needs to be checked in the interface to avoid duplicate creation by users.<br />In the same namespace, the names of request authentication cannot be duplicated. |
| Workload Labels | spec.selector | Optional. The labels for selecting workloads to apply the request authentication policy. Multiple labels can be added without sorting. |
| Label Name | spec.selector.matchLabels | Required. Consists of lowercase letters, numbers, hyphens (-), underscores (_), and periods (.). |
| Label Value | spec.selector.matchLabels.{label name} | Required. Consists of lowercase letters, numbers, hyphens (-), underscores (_), and periods (.). |

### Authentication Settings

| UI Item | YAML Field | Description |
| ------- | ---------- | ----------- |
| Add JWT Rule | spec.jwtRules | Optional. JWT rules for user request authentication. Multiple rules can be added. |
| Issuer | spec.jwtRules.issuers | Required. Information about the JSON Web Token (JWT) issuer. |
| Audiences | spec.jwtRules.issuers.Audiences | Optional. Configures the list of accessible audiences. If empty, it will access the service name. |
| jwksUri | spec.jwtRules.issuers.jwksUri | Optional. The JSON file path for the JSON Web Key (JWK), exclusive with jwks. For example, <https://www.googleapis.com/oauth2/v1/certs> |
| jwks | spec.jwtRules.issuers.jwks | Optional. The content of the JSON Web Key Set (JWKS) file, exclusive with jwksUri. |

For more information, please refer to [OpenID Provider Metadata](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata).

## Authorization Policies

When using the graphical wizard mode, the creation of [authorization policies](./authorize.md) is divided into __basic configuration__ and __policy settings__. The parameters are described as follows.

### Basic Configuration

| UI Item | YAML Field | Description |
| ------- | ---------- | ----------- |
| Name | metadata.name | Required. The name of the authorization policy. |
| Namespace | metadata.namespace | Required. The namespace to which the authorization policy belongs. When selecting the root namespace of the mesh, a global policy will be created. Only one global policy can be created, so it needs to be checked in the interface to avoid duplicate creation by users. In the same namespace, request authentication cannot have the same name. |
| Workload Labels | spec.selector | Optional. The labels for selecting workloads to apply the authorization policy. Multiple labels can be added without sorting. |
| Label Name | spec.selector.matchLabels | Optional. Consists of lowercase letters, numbers, hyphens (-), underscores (_), and periods (.). |
| Label Value | spec.selector.matchLabels.{label name} | Optional. Consists of lowercase letters, numbers, hyphens (-), underscores (_), and periods (.). |

### Policy Settings

| UI Item | YAML Field | Description |
| ------- | ---------- | ----------- |
| Policy Action | spec.action | Optional. Includes: <br />- allow<br />- deny<br />- audit<br />- custom<br />When selecting custom, an additional __provider__ input item will be displayed. |
| Provider | spec.provider.name | Required. Only displayed when __Policy Action__ is selected as __custom__. |
| Request Policies | spec.rules | Optional. Includes request source, request operation, and policy condition. Multiple rules can be added and executed in order. |
| Add Request Source | spec.rules.-from | Optional. Defines the request source based on the namespace, IP range, etc. Multiple sources can be added. See the following section [Source](#source) for parameters. |
| Add Request Operation | spec.rules.-to | Optional. Defines the operation to be performed on the filtered requests, such as sending them to a specific port or host. Multiple operations can be added. See the following section [Operation](#operation) for parameters. |
| Add Policy Condition | spec.rules.-when | Required. Policy conditions are optional settings that can add restriction conditions like blacklists (values) or whitelists (notValues). Multiple policy conditions can be added. See the following section [Condition](#condition) for parameters. |

#### Source

You can add request sources (Source). Source specifies the identity of the request source and performs logical AND operations on the fields in the request source.

For example, if the Source is:

- Principal is "admin" or "dev"
- Namespace is "prod" or "test"
- IP is not "1.2.3.4"

The matching YAML content would be:

```yaml
principals: ["admin", "dev"]
namespaces: ["prod", "test"]
notIpBlocks: ["1.2.3.4"]
```

The specific field descriptions are as follows:

| Key Field | Type | Description |
| --------- | ---- | ----------- |
| __principals__ | __string[]__ | Optional. Peer identities derived from peer certificates. The format of peer identities is __"<TRUST_DOMAIN>/ns/<NAMESPACE>/sa/<SERVICE_ACCOUNT>"__, for example, __"cluster.local/ns/default/sa/productpage"__. This field requires mTLS to be enabled and is equivalent to the __source.principal__ property. If not set, it allows all principals. |
| __notPrincipals__ | __string[]__ | Optional. Reverse matching list for peer identities. |
| __requestPrincipals__ | __string[]__ | Optional. Request identities derived from JWT. The format of request identities is __"<ISS>/<SUB>"__, for example, __"example.com/sub-1"__. This field requires request authentication to be enabled and is equivalent to the __request.auth.principal__ property. If not set, it allows all request principals. |
| __notRequestPrincipals__ | __string[]__ | Optional. Reverse matching list for request identities. |
| __namespaces__ | __string[]__ | Optional. Namespaces derived from peer certificates. This field requires mTLS to be enabled and is equivalent to the __source.namespace__ property. If not set, it allows all namespaces. |
| __notNamespaces__ | __string[]__ | Optional. Reverse matching list for namespaces. |
| __ipBlocks__ | __string[]__ | Optional. IP ranges filled based on the source address of IP packets. Supports single IPs (e.g., "1.2.3.4") and CIDR (e.g., "1.2.3.0/24"). This is equivalent to the __source.ip__ property. If not set, it allows all IPs. |
| __notIpBlocks__ | __string[]__ | Optional. Reverse matching list for IP ranges. |
| __remoteIpBlocks__ | __string[]__ | Optional. IP ranges filled based on the X-Forwarded-For header or proxy protocol. To use this field, you must configure the numTrustedProxies field in meshConfig when installing Istio or when using annotations on the ingress gateway. Supports single IPs (e.g., "1.2.3.4") and CIDR (e.g., "1.2.3.0/24"). This is equivalent to the __remote.ip__ property. If not set, it allows all IPs. |
| __notRemoteIpBlocks__ | __string[]__ | Optional. Reverse matching list for remote IP ranges. |

#### Operation

You can add request operations (Operation). Operation specifies the operation of the request and performs logical AND operations on the fields in the operation.

For example, the following operation will match:

- Host suffix is ".example.com"
- Method is "GET" or "HEAD"
- Path does not have the prefix "/admin"

```yaml
hosts: ["*.example.com"]
methods: ["GET", "HEAD"]
notPaths: ["/admin*"]
```

| Key Field | Type | Description |
| --------- | ---- | ----------- |
| __hosts__ | __string[]__ | Optional. The list of hosts specified in the HTTP request. Case-insensitive. If not set, it allows all hosts. Only applicable to HTTP. |
| __notHosts__ | __string[]__ | Optional. Reverse matching list for hosts specified in the HTTP request. Case-insensitive. |
| __ports__ | __string[]__ | Optional. The list of ports specified in the connection. If not set, it allows all ports. |
| __notPorts__ | __string[]__ | Optional. Reverse matching list for ports specified in the connection. |
| __methods__ | __string[]__ | Optional. The list of methods specified in the HTTP request. For gRPC services, this will always be "POST". If not set, it allows all methods. Only applicable to HTTP. |
| __notMethods__ | __string[]__ | Optional. Reverse matching list for methods specified in the HTTP request. |
| __paths__ | __string[]__ | Optional. The list of paths specified in the HTTP request. For gRPC services, this will be in the format of "/package.service/method" fully qualified name. If not set, it allows all paths. Only applicable to HTTP. |
| __notPaths__ | __string[]__ | Optional. Reverse matching list for paths. |

**In actual operations, it is also important to note the addition of some common keys**

- request.headers[User-Agent]
- request.auth.claims[iss]
- experimental.envoy.filters.network.mysql_proxy[db.table]

For more information about the configuration parameters of __AuthorizationPolicy__, please refer to the documentation at <https://istio.io/latest/docs/reference/config/security/conditions/>.

#### Condition

You can also add policy conditions (Condition). Condition specifies other required attributes.

| Key Field | Description | Supported Protocols | Value Example |
| --------- | ----------- | ------------------ | ------------- |
| __request.headers__ | HTTP request headers, enclosed in __[]__ | HTTP only | __["Mozilla/*"]__ |
| __source.ip__ | Source IP address, supports single IP or CIDR | HTTP and TCP | __["10.1.2.3"]__ |
| __remote.ip__ | Original client IP address determined by the X-Forwarded-For request header or proxy protocol, supports single IP or CIDR | HTTP and TCP | __["10.1.2.3", "10.2.0.0/16"]__ |
| __source.namespace__ | Namespace of the source workload instance, requires bidirectional TLS | HTTP and TCP | __["default"]__  |
| __source.principal__ | Identity of the source workload, requires bidirectional TLS | HTTP and TCP | __["cluster.local/ns/default/sa/productpage"]__ |
| __request.auth.principal__ | Request with authenticated __principal__ | HTTP only | __["accounts.my-svc.com/104958560606"]__ |
| __request.auth.audiences__ | Target subject of this authentication information | HTTP only | __["my-svc.com"]__  |
| __request.auth.presenter__ | Issuer of the certificate | HTTP only | __["123456789012.my-svc.com"]__ |
| __request.auth.claims__ | Claims derived from JWT, enclosed in __[]__ | HTTP only | __["*@foo.com"]__ |
| __destination.ip__ | Destination IP address, supports single IP or CIDR | HTTP and TCP | __["10.1.2.3", "10.2.0.0/16"]__ |
| __destination.port__ | Port on the destination IP address, must be within the range of __[0, 65535]__ | HTTP and TCP | __["80", "443"]__ |
| __connection.sni__ | Server Name Indication, requires bidirectional TLS | HTTP and TCP | __["www.example.com"]__ |
| __experimental.envoy.filters.*__ | Experimental metadata matches for filters, with the value enclosed in __[]__ as a list match | HTTP and TCP | __["[update]"]__ |

!!! note

    The backward compatibility of __experimental.*__ keys cannot be guaranteed and they may be removed at any time, so be cautious.
