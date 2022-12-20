# Security governance parameter configuration

This page introduces parameter configuration related to peer identity authentication, request identity authentication, and authorization policy.

## Peer Authentication

When the wizard mode is used, the peer-to-peer identity authentication is divided into two steps: basic configuration and authentication setting, and the description of each parameter is as follows.

### basic configuration

| **UI Item** | **YAML Field** | **Description** |
| ---------------------- | -------------------------- ------------ | ------------------------------------- ----------------------- |
| Name | metadata.name | Required. Peer identity authentication name, which cannot be duplicated in the same namespace. |
| Namespace | metadata.namespace | Required. The namespace the peer authentication belongs to. Global policies are created when the grid's root namespace is selected. Only one global policy can be created, and it needs to be checked in the interface to avoid repeated creation by users. |
| workload tags | spec.selector | optional. Workload selection tags that apply peer authentication policies, multiple tags can be added without sorting. |
| Label name | spec.selector.matchLabels | Required. Consists of lowercase letters, numbers, hyphens (-), underscores (_), and decimal points (.) |
| Label value | spec.selector.matchLabels.{label name} | Required. Consists of lowercase letters, numbers, hyphens (-), underscores (_), and decimal points (.) |

## Authentication Settings

| **UI Item** | **YAML Field** | **Description** |
| ---------------------- | -------------------------- ------------ | ------------------------------------- ----------------------- |
| mTLS Mode | spec.mTLS.mode | Required. mTLS mode for setting the namespace:<br /> - PERMISSIVE: cleartext and mTLS connections<br /> - STRICT: mTLS connections only<br /> - DISABLE: cleartext connections only |
| Add mTLS mode for specified port | spec.portLevelMtls | Optional. Set mTLS rules for specified ports, multiple rules can be added without sorting. <br />- PERMISSIVE: cleartext and mTLS connections<br />- STRICT: mTLS connections only<br />- DISABLE: cleartext connections only |

## request authentication

When using the wizard wizard mode, requesting identity authentication is divided into two steps: basic configuration and authentication setting, and the description of each parameter is as follows.

## basic configuration

| **UI Item** | **YAML Field** | **Description** |
| ------------ | ------------------------------------ | -------------------------------------------------- ----------- |
| Name | metadata.name | Required. Request identity authentication name, the same name space cannot be duplicated. |
| Namespace | metadata.namespace | Required. Namespace to which the request authentication belongs. Global policies are created when the grid's root namespace is selected. Only one global policy can be created, and it needs to be checked in the interface to avoid repeated creation by users. <br />In the same namespace, the name requesting authentication cannot be repeated. |
| workload tags | spec.selector | Optional. The application requests the workload selection tag of the identity authentication policy. Multiple selection tags can be added without sorting. |
| Label name | spec.selector.matchLabels | Required. Consists of lowercase letters, numbers, hyphens (-), underscores (_), and decimal points (.) |
| Label value | spec.selector.matchLabels.{label name} | Required. Consists of lowercase letters, numbers, hyphens (-), underscores (_), and decimal points (.) |

### Authentication settings

| **UI Item** | **YAML Field** | **Description** |
| ------------- | ----------------------------------- - | ------------------------------------------------ ------------ |
| Add JWT rules | spec.jwtRules | Optional. JWT rules for user request authentication, multiple rules can be added. |
| Issuer | spec.jwtRules.issuers | Required. JSON Web Token (JWT) issuer information. |
| Audiences | spec.jwtRules.issuers.Audiences | Optional. Configure the list of accessible audiences, if empty, the service name will be accessed. |
| jwkURI | spec.jwtRules.issuers.jwkUri | Optional. The path to the JSON file of the JSON Web Key (JWK), in the format: URI. |
| jwks | spec.jwtRules.issuers.jwks | Optional. JSON Web Key Set (JWKS) file content, which can be provided with jwkURI alternatively. |

## Authorization Policy

When the wizard mode is used, the creation of the authorization policy is divided into two steps: `basic configuration` and `policy setting`, and the description of each parameter is as follows.

### basic configuration

| **Element** | **YAML Field** | **Description** |
| -------------------- | ---------------------------- ---------- | --------------------------------------- --------------------- |
| Name | metadata.name | Required. Authorized policy name. |
| Namespace | metadata.namespace | Required. The namespace to which the authorization policy belongs. When the grid root namespace is selected, a global policy will be created. Only one global policy can be created, and it needs to be checked on the interface to avoid repeated creation by users. In the same namespace, request identity authentication cannot have the same name. |
| workload tags | spec.selector | Optional. The workload selection tag of the application authorization policy, multiple selection tags can be added without sorting. |
| Label name | spec.selector.matchLabels | Optional. Consists of lowercase letters, numbers, hyphens (-), underscores (_), and decimal points (.). |
| Label value | spec.selector.matchLabels.{label name} | Optional. Consists of lowercase letters, numbers, hyphens (-), underscores (_), and decimal points (.). |

### Policy Settings

| **Element** | **YAML Field** | **Description** |
| -------------------- | ---------------------------- ---------- | --------------------------------------- --------------------- |
| policy action | spec.action | Optional. Contains:<br />- Allow (allow)<br />- Deny (deny)<br />- Audit (audit)<br />- Custom (custom)<br />When you choose custom, add` provider` entry. |
| Provider | spec.provider.name | Required. This input box is displayed only when the option of `Strategy Action` is `Custom`. |
| Request Policy | spec.rules | Optional. It includes three parts: request source, request operation, and policy conditions. Multiple items can be added and executed in order. |
| Add request source | spec.rules.-from | Optional. Request sources can be defined based on namespaces, IP segments, etc., and multiple entries can be added. For each parameter, see [Request Source Source](#Request Source-source) below. |
| Add request action | spec.rules.-to | Optional. The request operation is the operation performed on the filtered requests, such as sending to a specified port or host, and multiple operations can be added. For parameters, see [Request Operation Operation](#Request Operation-operation) below. |
| Add Policy Conditions | spec.rules.-when | Required. The policy condition is an optional setting, which can add restrictions like blacklist (values) and whitelist (notValues), and multiple policy conditions can be added. For parameters, see [Strategy Condition Condition](#Strategy Condition-condition) below. |

#### Request source Source

Source specifies the source identity of a request. Performs a logical AND operation on the fields in the request source.

For example, the following Source will match:

- principal is "admin" or "dev"
- The namespace is "prod" or "test"
- and ip is not "1.2.3.4".

```yaml
principals: ["admin", "dev"]
namespaces: ["prod", "test"]
notIpBlocks: ["1.2.3.4"]
```

| Field | Type | Description |
| ---------------------- | ---------- | --------------- ------------------------------------------------ |
| `principals` | `string[]` | Optional. A list of peer identities derived from peer certificates. The format of the peer identity is `"<TRUST_DOMAIN>/ns/<NAMESPACE>/sa/<SERVICE_ACCOUNT>"`, for example `"cluster.local/ns/default/sa/productpage"`. This field requires mTLS to be enabled and is equivalent to the `source.principal` property. If not set, all principals are allowed. |
| `notPrincipals` | `string[]` | Optional. A reverse match list of peer identities. |
| `requestPrincipals` | `string[]` | Optional. A list of requesting identities derived from the JWT. The format of the request identity is `"<ISS>/<SUB>"`, for example `"example.com/sub-1"`. This field requires request authentication to be enabled and is equivalent to the `request.auth.principal` property. If not set, all request bodies are allowed. |
| `notRequestPrincipals` | `string[]` | Optional. A reverse match list of request identities. |
| `namespaces` | `string[]` | Optional. A namespace derived from the peer certificate. This field requires mTLS to be enabled and is equivalent to the `source.namespace` property. If not set, all namespaces are allowed. |
| `notNamespaces` | `string[]` | Optional. A list of reverse matches for namespaces. |
| `ipBlocks` | `string[]` | Optional. A list of IP segments to populate based on the source address of the IP packet. Both single IP (eg "1.2.3.4") and CIDR (eg "1.2.3.0/24") are supported. This is equivalent to the `source.ip` property. If not set, all IPs are allowed. |
| `notIpBlocks` | `string[]` | Optional. A list of reverse matches for IP segments. |
| `remoteIpBlocks` | `string[]` | Optional. List of IP segments to populate based on X-Forwarded-For header or proxy protocol. To use this field, you must configure the gatewayTopology numTrustedProxies field under meshConfig when installing Istio or using annotations on the ingress gateway. Both single IP (eg "1.2.3.4") and CIDR (eg "1.2.3.0/24") are supported. This is equivalent to the `remote.ip` property. If not set, all IPs are allowed. |
| `notRemoteIpBlocks` | `string[]` | Optional. A list of reverse matches for remote IP ranges. |

#### Request Operation Operation

Operation specifies the requested operation. Performs a logical AND operation on the fields in the operation.

For example, the following operations will match:

- The host suffix is ".example.com"
- Method is "GET" or "HEAD"
- Patches are not prefixed with "/admin"

```yaml
hosts: ["*.example.com"]
methods: ["GET", "HEAD"]
notPaths: ["/admin*"]
```

| Field | Type | Description |
| ------------ | ---------- | ------------------------- -------------------------------------- |
| `hosts` | `string[]` | Optional. List of hosts specified in the HTTP request. not case sensitive. If not set, all hosts are allowed. Applies to HTTP only. |
| `notHosts` | `string[]` | Optional. A reverse match list of hosts specified in the HTTP request. not case sensitive. |
| `ports` | `string[]` | Optional. The list of ports specified in the connection. If not set, all ports are allowed. |
| `notPorts` | `string[]` | Optional. A list of reverse matches for the ports specified in the connection. |
| `methods` | `string[]` | Optional. List of methods specified in the HTTP request. For gRPC services, this will always be "POST". If not set, all methods are allowed. Applies to HTTP only. |
| `notMethods` | `string[]` | Optional. A list of reverse matches for the method specified in the HTTP request. |
| `paths` | `string[]` | Optional. A list of paths specified in the HTTP request. For gRPC services, this will be the fully qualified name in the format "/package.service/method". If not set, all paths are allowed. Applies to HTTP only. |
| `notPaths` | `string[]` | Optional. A list of reverse matches for paths. |

#### Policy Condition Condition

Condition specifies other required properties.

| Name | Description | Supported Protocols | Examples |
|------|-------------|--------------------|------- --|
| `request.headers` | `HTTP` request headers, need to be enclosed by `[]` | HTTP only | `key: request.headers[User-Agent]`<br/>`values: ["Mozilla/*" ]` |
| `source.ip` | source `IP` address, support single `IP` or `CIDR` | HTTP and TCP | `key: source.ip`<br/>`values: ["10.1.2.3"]` |
| `remote.ip` | Original client IP address determined by `X-Forwarded-For` request header or proxy protocol, single IP or CIDR supported | HTTP and TCP | `key: remote.ip`<br />` values: ["10.1.2.3", "10.2.0.0/16"]` |
| `source.namespace` | source payload instance namespace, mutual TLS needs to be enabled | HTTP and TCP | `key: source.namespace`<br/>`values: ["default"]` |
| `source.principal` | source payload identifier, mutual TLS needs to be enabled | HTTP and TCP | `key: source.principal`<br/>`values: ["cluster.local/ns/default/sa/productpage"] ` |
| `request.auth.principal` | Authenticated requests for `principal` | HTTP only | `key: request.auth.principal`<br/>`values: ["accounts.my-svc.com/104958560606"] ` |
| `request.auth.audiences` | The target principal for this authentication | HTTP only | `key: request.auth.audiences`<br/>`values: ["my-svc.com"]` |
| `request.auth.presenter` | Issuer of the certificate | HTTP only | `key: request.auth.presenter`<br/>`values: ["123456789012.my-svc.com"]` |
| `request.auth.claims` | `Claims` are derived from `JWT`. Need to be surrounded by `[]` | HTTP only | `key: request.auth.claims[iss]`<br/>`values: ["*@foo.com"]` |
| `destination.ip` | destination `IP` address, support single `IP` or `CIDR` | HTTP and TCP | `key: destination.ip`<br/>`values: ["10.1.2.3", "10.2 .0.0/16"]` |
| `destination.port` | The port on the destination `IP` address, must be in the range `[0, 65535]` | HTTP and TCP | `key: destination.port`<br/>`values: ["80" , "443"]` |
| `connection.sni` | server name indication, mutual TLS needs to be enabled | HTTP and TCP | `key: connection.sni`<br/>`values: ["www.example.com"]` |
| `experimental.envoy.filters.*` | Experimental metadata matching for filters, wrapped values `[]` as list matches | HTTP and TCP | `key: experimental.envoy.filters.network.mysql_proxy[ db.table]`<br/>`values: ["[update]"]` |

!!! note

     Backwards compatibility of `experimental.*` keys is not guaranteed, they can be removed at any time, but do so with caution.