# Security Governance Parameter Configuration

This page introduces parameter configuration related to peer identity authentication, request identity authentication, and authorization policy.

## Peer Authentication

When using the graphical wizard mode, [Peer Identity Authentication](./peer.md) is divided into two steps: basic configuration and authentication setting, and the description of each parameter is as follows.

### basic configuration

| **UI Item** | **YAML Field** | **Description** |
| ---------------------- | -------------------------- ------------ | ------------------------------------- ----------------------- |
| Name | metadata.name | Required. Peer identity authentication name, which cannot be duplicated in the same namespace. |
| Namespace | metadata.namespace | Required. The namespace the peer authentication belongs to. Global policies are created when the mesh's root namespace is selected. Only one global policy can be created, and it needs to be checked in the interface to avoid repeated creation by users. |
| workload tags | spec.selector | optional. Workload selection tags that apply peer authentication policies, multiple tags can be added without sorting. |
| Label name | spec.selector.matchLabels | Required. Consists of lowercase letters, numbers, hyphens (-), underscores (_), and decimal points (.) |
| Label value | spec.selector.matchLabels.{label name} | Required. Consists of lowercase letters, numbers, hyphens (-), underscores (_), and decimal points (.) |

### Authentication Settings - mTLS Mode

| **UI Item** | **YAML Field** | **Description** |
| ---------------------- | -------------------------- ------------ | ------------------------------------- ----------------------- |
| mTLS Mode | spec.mTLS.mode | Required. mTLS mode for setting the namespace:<br /> - UNSET: Inherit parent option. Otherwise treat as PERMISSIVE<br />- PERMISSIVE: cleartext and mTLS connections<br />- STRICT: mTLS connections only<br />- DISABLE: cleartext connections only |
| Add mTLS mode for specified port | spec.portLevelMtls | Optional. Set mTLS rules for specified ports, multiple rules can be added without sorting. <br /> - UNSET: Inherit parent options. Otherwise treat as PERMISSIVE<br />- PERMISSIVE: cleartext and mTLS connections<br />- STRICT: mTLS connections only<br />- DISABLE: cleartext connections only |

## request authentication

When using the graphical wizard mode, [Request identity authentication](./request.md) is divided into two steps: basic configuration and authentication setting, and the descriptions of each parameter are as follows.

### basic configuration

| **UI Item** | **YAML Field** | **Description** |
| ------------ | ------------------------------------ | -------------------------------------------------- ----------- |
| Name | metadata.name | Required. Request identity authentication name, the same name space cannot be duplicated. |
| Namespace | metadata.namespace | Required. Namespace to which the request authentication belongs. Global policies are created when the mesh's root namespace is selected. Only one global policy can be created, and it needs to be checked in the interface to avoid repeated creation by users. <br />In the same namespace, the name requesting authentication cannot be repeated. |
| workload tags | spec.selector | optional. The application requests the workload selection tag of the identity authentication policy. Multiple selection tags can be added without sorting. |
| Label name | spec.selector.matchLabels | Required. Consists of lowercase letters, numbers, hyphens (-), underscores (_), and decimal points (.) |
| Label value | spec.selector.matchLabels.{label name} | Required. Consists of lowercase letters, numbers, hyphens (-), underscores (_), and decimal points (.) |

### Authentication settings

| **UI Item** | **YAML Field** | **Description** |
| ------------- | ----------------------------------- - | ------------------------------------------------ ------------ |
| Add JWT rules | spec.jwtRules | Optional. JWT rules for user request authentication, multiple rules can be added. |
| Issuer | spec.jwtRules.issuers | Required. JSON Web Token (JWT) issuer information. |
| Audiences | spec.jwtRules.issuers.Audiences | Optional. Configure the list of accessible audiences, if empty, the service name will be accessed. |
| jwksUri | spec.jwtRules.issuers.jwksUri | Optional. JSON Web Key (JWK) JSON file path, mutually exclusive with jwks, choose one of the two. For example https://www.googleapis.com/oauth2/v1/certs |
| jwks | spec.jwtRules.issuers.jwks | Optional. JSON Web Key Set (JWKS) file content, mutually exclusive with jwksUri, choose one of the two. |

For more information, please refer to [OpenID Provider Metadata](https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata).

## Authorization Policy

When using the graphical wizard mode, the creation of [Authorization Policy](./authorize.md) is divided into two steps: __Basic Configuration__ and __Policy Settings__ , and the description of each parameter is as follows.

### basic configuration

| **Configurable Items** | **YAML Field** | **Description** |
| -------------------- | ---------------------------- ---------- | --------------------------------------- --------------------- |
| Name | metadata.name | Required. Authorized policy name. |
| Namespace | metadata.namespace | Required. The namespace to which the authorization policy belongs. When the mesh root namespace is selected, a global policy will be created. Only one global policy can be created, and it needs to be checked on the interface to avoid repeated creation by users. In the same namespace, request identity authentication cannot have the same name. |
| workload tags | spec.selector | optional. The workload selection tag of the application authorization policy, multiple selection tags can be added without sorting. |
| Label name | spec.selector.matchLabels | Optional. Consists of lowercase letters, numbers, hyphens (-), underscores (_), and decimal points (.). |
| Label value | spec.selector.matchLabels.{label name} | Optional. Consists of lowercase letters, numbers, hyphens (-), underscores (_), and decimal points (.). |

### Policy Settings

| **Configurable Items** | **YAML Field** | **Description** |
| -------------------- | ---------------------------- ---------- | --------------------------------------- --------------------- |
| policy action | spec.action | Optional. Contains:<br />- Allow (allow)<br />- Deny (deny)<br />- Audit (audit)<br />- Custom (custom)<br />When you choose custom, add __ provider__ entry. |
| Provider | spec.provider.name | Required. This input box is displayed only when the option of __Strategy Action__ is __Custom__ . |
| Request Policy | spec.rules | Optional. It includes three parts: request source, request operation, and policy conditions. Multiple items can be added and executed in order. |
| Add request source | spec.rules.-from | Optional. Request sources can be defined based on namespaces, IP segments, etc., and multiple entries can be added. See the following [Request Source](#source) for each parameter. |
| Add request action | spec.rules.-to | Optional. The request operation is the operation performed on the filtered requests, such as sending to a specified port or host, and multiple operations can be added. See the parameters below [Request Operation Operation](#opgeneration). |
| Add Policy Conditions | spec.rules.-when | Required. The policy condition is an optional setting, which can add restrictions like blacklist (values) and whitelist (notValues), and multiple policy conditions can be added. For parameters, see [Strategy Condition Condition](#condition) below. |

#### Request source Source

You can increase the request source (Source). Source specifies the source identity of a request and performs a logical AND operation on the fields in the request source.

For example, if Source is:

- principal is "admin" or "dev"
- Namespaced as "prod" or "test"
- and ip is not "1.2.3.4".

The matching YAML content is:

```yaml
principals: ["admin", "dev"]
namespaces: ["prod", "test"]
notIpBlocks: ["1.2.3.4"]
```

The specific fields are described as follows:

| Key Field | Type | Description |
| ---------------------- | ---------- | --------------- ------------------------------------------------ |
| __principals__ | __string[]__ | Optional. A list of peer identities derived from peer certificates. The format of the peer identity is __"<TRUST_DOMAIN>/ns/<NAMESPACE>/sa/<SERVICE_ACCOUNT>"__ , for example __"cluster.local/ns/default/sa/productpage"__ . This field requires mTLS to be enabled and is equivalent to the __source.principal__ property. If not set, all principals are allowed. |
| __notPrincipals__ | __string[]__ | Optional. A reverse match list of peer identities. |
| __requestPrincipals__ | __string[]__ | Optional. A list of requesting identities derived from the JWT. The format of the request identity is __"<ISS>/<SUB>"__ , for example __"example.com/sub-1"__ . This field requires request authentication to be enabled and is equivalent to the __request.auth.principal__ property. If not set, all request bodies are allowed. |
| __notRequestPrincipals__ | __string[]__ | Optional. A reverse match list of request identities. |
| __namespaces__ | __string[]__ | Optional. A namespace derived from the peer certificate. This field requires mTLS to be enabled and is equivalent to the __source.namespace__ property. If not set, all namespaces are allowed. |
| __notNamespaces__ | __string[]__ | Optional. A list of reverse matches for namespaces. |
| __ipBlocks__ | __string[]__ | Optional. A list of IP segments to populate based on the source address of the IP packet. Both single IP (eg "1.2.3.4") and CIDR (eg "1.2.3.0/24") are supported. This is equivalent to the __source.ip__ property. If not set, all IPs are allowed. |
| __notIpBlocks__ | __string[]__ | Optional. A list of reverse matches for IP segments. |
| __remoteIpBlocks__ | __string[]__ | Optional. List of IP segments to populate based on X-Forwarded-For header or proxy protocol. To use this field, you must configure the gatewayTopology numTrustedProxies field under meshConfig when installing Istio or using annotations on the ingress gateway. Both single IP (eg "1.2.3.4") and CIDR (eg "1.2.3.0/24") are supported. This is equivalent to the __remote.ip__ property. If not set, all IPs are allowed. |
| __notRemoteIpBlocks__ | __string[]__ | Optional. A list of reverse matches for remote IP ranges. |

#### Request Operation Operation

You can increase the request operation (Operation). Operation specifies the requested operation, performing a logical AND operation on the fields in the operation.

For example, the following operations will match:

- The host suffix is ".example.com"
- Method is "GET" or "HEAD"
- Patches are not prefixed with "/admin"

```yaml
hosts: ["*.example.com"]
methods: ["GET", "HEAD"]
notPaths: ["/admin*"]
```

| Key Field | Type | Description |
| ------------ | ---------- | ------------------------- -------------------------------------- |
| __hosts__ | __string[]__ | Optional. List of hosts specified in the HTTP request. not case sensitive. If not set, all hosts are allowed. Applies to HTTP only. |
| __notHosts__ | __string[]__ | Optional. A reverse match list of hosts specified in the HTTP request. not case sensitive. |
| __ports__ | __string[]__ | Optional. The list of ports specified in the connection. If not set, all ports are allowed. |
| __notPorts__ | __string[]__ | Optional. A list of reverse matches for the ports specified in the connection. |
| __methods__ | __string[]__ | Optional. List of methods specified in the HTTP request. For gRPC services, this will always be "POST". If not set, all methods are allowed. Applies to HTTP only. |
| __notMethods__ | __string[]__ | Optional. A list of reverse matches for the method specified in the HTTP request. |
| __paths__ | __string[]__ | Optional. A list of paths specified in the HTTP request. For gRPC services, this will be the fully qualified name in the format "/package.service/method". If not set, all paths are allowed. Applies to HTTP only. |
| __notPaths__ | __string[]__ | Optional. A list of reverse matches for paths. |

**In the actual operational scenario, it is important to include additional common keys:**

- __request.headers[User-Agent]__ 
- __request.auth.claims[iss]__ 
- __experimental.envoy.filters.network.mysql_proxy[db.table]__ 

For more information on configuration parameters for __AuthorizationPolicy__ , please refer to the documentation at <https://istio.io/latest/docs/reference/config/security/conditions/>.

#### Policy Condition Condition

You can also add policy conditions (Condition). Condition specifies other required properties.

| Key Field | Description | Supported Protocols | Value Example|
|------|-------------|--------------------|------- --|
| __request.headers__ | __HTTP__ request headers, need to be surrounded by __[]__ | HTTP only | __["Mozilla/*"]__ |
| __source.ip__ | source __IP__ address, support single __IP__ or __CIDR__ | HTTP and TCP | __["10.1.2.3"]__ |
| __remote.ip__ | Original client IP address determined by __X-Forwarded-For__ request header or proxy protocol, single IP or CIDR supported | HTTP and TCP | __["10.1.2.3", "10.2.0.0 /16"]__ |
| __source.namespace__ | source workload instance namespace, need to enable mutual TLS | HTTP and TCP | __["default"]__ |
| __source.principal__ | The identity of the source payload, mutual TLS needs to be enabled | HTTP and TCP | __["cluster.local/ns/default/sa/productpage"]__ |
| __request.auth.principal__ | Authenticated requests for __principal__ | HTTP only | __["accounts.my-svc.com/104958560606"]__ |
| __request.auth.audiences__ | Target principals for this authentication | HTTP only | __["my-svc.com"]__ |
| __request.auth.presenter__ | Issuer of the certificate | HTTP only | __["123456789012.my-svc.com"]__ |
| __request.auth.claims__ | __Claims__ are derived from __JWT__ . Need to be surrounded by __[]__ | HTTP only | __["*@foo.com"]__ |
| __destination.ip__ | destination __IP__ address, support single __IP__ or __CIDR__ | HTTP and TCP | __["10.1.2.3", "10.2.0.0/16"]__ |
| __destination.port__ | The port on the destination __IP__ address, must be in the range __[0, 65535]__ | HTTP and TCP | __["80", "443"]__ |
| __connection.sni__ | server name indication, mutual TLS needs to be enabled | HTTP and TCP | __["www.example.com"]__ |
| __experimental.envoy.filters.*__ | Experimental metadata matching for filters, wrapping values __[]__ as list matches | HTTP and TCP | __["[update]"]__ |

!!! note

     Backwards compatibility of __experimental.*__ keys is not guaranteed, they can be removed at any time, but do so with caution.
