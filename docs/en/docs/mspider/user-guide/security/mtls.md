# Service Mesh Identity and Authentication

Identity is a fundamental concept of any security infrastructure.
When communication between workloads begins, both communicating parties must exchange credentials containing identity information for mutual authentication.
On the client side, check the server's identity against the [security naming](#_5) information to see if it is an authorized runner for the workload.
On the server side, the server can determine what information the client can access based on the authorization policy,
Audit who accesses what when, bill customers based on the workload they use,
And deny access to workloads to any customers who fail to pay their bills.

The DCE 5.0 service mesh identity model uses the classic `service identity` (service identity) to determine the identity of a request source.
This model has great flexibility and granularity, and service identities can be used to identify human users, individual workloads, or groups of workloads.
On platforms without service identities, service meshes can use other identities that group service instances, such as service names.

The following list shows the service identities available on different platforms:

- Kubernetes: Kubernetes service account
- GKE/GCE: GCP service account
- Local (non-Kubernetes): user account, custom service account, service name,
   A service mesh service account or a GCP service account. A custom service account references an existing service account,
   Like the identity managed by the customer's identity directory.

## Identity and certificate management

Service mesh PKI (Public Key Infrastructure) uses X.509 certificates to provide strong identities for each workload.
`istio-agent` runs with every Envoy agent, with `istiod`
Work together to automate key and certificate rotation at scale. The figure below shows the operation flow of this mechanism.

![workflow](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/id-prov.svg)

The service mesh provides keys and certificates through the following process:

1. `istiod` provides a gRPC service to accept [Certificate Signing Requests](https://en.wikipedia.org/wiki/Certificate_signing_request) (CSRs).
1. `istio-agent` creates a private key and a CSR at startup, then sends the CSR and its credentials to `istiod` for signing.
1. The `istiod` CA verifies the credentials carried in the CSR, and upon successful verification, signs the CSR to generate a certificate.
1. When the workload starts, Envoy uses the [Secret Discovery Service (SDS)](https://www.envoyproxy.io/docs/envoy/latest/configuration/security/secret#secret-discovery-service-sds) API Send certificate and key requests to `istio-agent` inside the same container.
1. `istio-agent` sends the certificate and key received from `istiod` to Envoy via the Envoy SDS API.
1. `istio-agent` monitors workload certificate expiration time. The above process is repeated periodically for certificate and key rotation.

## authentication

Service mesh provides two types of authentication:

- `Peer Authentication`: Used for service-to-service authentication to authenticate the client establishing the connection.
   Service Mesh provides [Mutual TLS](https://en.wikipedia.org/wiki/Mutual_authentication)
   As a full-stack solution for transport authentication, it can be enabled without changing the service code. This solution:
     - Provide each service with a strong identity representing its role for interoperability across clusters and clouds.
     - Securing service-to-service communication.
     - Provides a key management system to automate the generation, distribution, and rotation of keys and certificates.
- `request-authentication`: For end-user authentication, to verify credentials attached to a request.
   The service mesh enables request-level authentication using JSON Web Token (JWT) validation,
   And use a custom authentication implementation or any of OpenID Connect's authentication implementations (such as those listed below) to simplify the developer experience.
     - [ORY Hydra](https://www.ory.sh/)
     - [Keycloak](https://www.keycloak.org/)
     - [Auth0](https://auth0.com/)
     - [Firebase Auth](https://firebase.google.com/docs/auth/)
     - [Google Auth](https://developers.google.com/identity/protocols/OpenIDConnect)

In all cases, the service mesh stores authentication policies in the `Istio config store` via a custom Kubernetes API.
Istiod keeps each agent up to date,
And provide the key when appropriate. In addition, the authentication mechanism of the service mesh supports permissive mode,
to help you understand how policy changes will affect your security posture before they are enforced.

### mTLS authentication

The full name of mTLS is Mutual Transport Layer Security, that is, two-way transport layer security authentication.
mTLS allows communicating parties to mutually authenticate during the initial connection of the SSL/TLS handshake.

DCE 5.0 service mesh through client and server
[PEP](https://www.jerichosystems.com/technology/glossaryterms/policy_enforcement_point.html)(Policy Enforcement Policy)
To establish a service-to-service communication channel, the PEP is implemented as [Envoy Proxy](https://www.envoyproxy.io/).
When one workload sends a request to another workload using mTLS authentication,
The request is handled as follows:

1. The service mesh reroutes outbound traffic from the client to Envoy, the client's local sidecar.
1. The client Envoy and the server Envoy start a mutual TLS handshake. During the handshake,
    Client Envoy also does a [safe naming](#_5) check,
    to verify that the service account shown in the server certificate is authorized to run the target service.
1. The client Envoy and the server Envoy establish a two-way TLS connection,
    The service mesh forwards traffic from client-side Envoys to server-side Envoys.
1. Server-side Envoy authorization request. If authorized, it forwards traffic to the backend service over a local TCP connection.

The service mesh configures the client and server with `TLSv1_2` as the minimum TLS version with the following cipher suites:

- `ECDHE-ECDSA-AES256-GCM-SHA384`
- `ECDHE-RSA-AES256-GCM-SHA384`
- `ECDHE-ECDSA-AES128-GCM-SHA256`
- `ECDHE-RSA-AES128-GCM-SHA256`
- `AES256-GCM-SHA384`
- `AES128-GCM-SHA256`

#### Permissive Mode

Service Mesh Mutual TLS has a permissive mode,
Allows the service to accept both plain text traffic and mutual TLS traffic. This feature greatly improves the experience of getting started with mutual TLS.

When the operation and maintenance personnel want to migrate services to the service mesh with mutual TLS enabled,
Communication between many non-service mesh clients and non-service mesh servers can be problematic.
Usually, the operation and maintenance personnel cannot install the service mesh sidecar for all clients at the same time,
Not even permission to do so on some clients. Even with a service mesh sidecar installed on the server side,
Operators also cannot enable mutual TLS without disrupting existing connections.

When permissive mode is enabled, the service can accept both plain text and mutual TLS traffic.
This mode provides great flexibility for getting started. Service mesh sidecar installed in server
Instantly accept mutual TLS traffic without interrupting existing plaintext traffic. therefore,
Operators can step by step install and configure the client service mesh sidecar to send mutual TLS traffic.
Once the client side is configured, operators can configure the server side to TLS-only mode.

#### Safe Naming

The server identity (Server identity) is encoded in the certificate,
But the service name (service name) is retrieved through service discovery or DNS.
Secure naming information maps server identities to service names. Identity `A` to service name `B`
A mapping of means "Authorization `A` to run service `B`". control plane monitoring `apiserver`,
Generate secure naming maps and securely distribute them to PEPs.
The following example illustrates why secure naming is critical for authentication.

Assume that the legitimate server running the service `datastore` uses only the `infra-team` identity.
A malicious user has the certificate and key of the `test-team` identity.
Malicious users intend to impersonate legitimate services to inspect data sent from clients.
A malicious user deploys a fake server using the certificate and key of the `test-team` identity.
Suppose a malicious user successfully hijacks (via DNS spoofing, BGP/route hijacking, ARP spoofing, etc.)
`datastore` traffic and redirect it to a fake server.

When a client calls the `datastore` service, it extracts the `test-team` identity from the server's certificate,
And check if `test-team` is allowed to run `datastore` with security naming information.
The client detected that `test-team` is not allowed to run the `datastore` service, authentication failed.

Note that secure naming does not protect against DNS spoofing for non-HTTP/HTTPS traffic,
For example, an attacker hijacks DNS and modifies the destination IP address. This is because TCP traffic does not contain hostname information,
Envoy can only rely on the destination IP address for routing, so it is possible for Envoy to route traffic to a hijacked
on the service where the IP address resides. This DNS spoofing can happen even before the client Envoy receives the traffic.

### Authentication Architecture

You can use the `Peer Authentication` and `Request Authentication` policies to specify authentication requirements for workloads that receive requests in the service mesh.
mesh operators use `.yaml` files to specify policies. Once deployed, policies are saved in the service mesh configuration store.
The service mesh controller monitors the configuration store.

On any policy change, the new policy is translated into the appropriate configuration, telling the PEP how to enforce the required authentication mechanisms.
The control plane can take the public key and attach it to the JWT validated configuration. As an alternative,
Istiod provides paths to keys and certificates managed by the service mesh system and installs them to application pods for mutual TLS.

The service mesh sends the configuration asynchronously to the target endpoint. The new authentication requirements take effect immediately after the agent receives the configuration.

The client service sending the request is responsible for following the necessary authentication mechanisms. For `Request Authentication`,
The application is responsible for obtaining JWT credentials and attaching them to the request. For `peer authentication`,
The service mesh automatically upgrades all traffic between the two PEPs to mutual TLS. If mutual TLS mode is disabled in the authentication policy,
then the service mesh will continue to use plain text between PEPs. To override this behavior,
Please use [Destination Rules](../traffic-governance/destination-rules.md) to explicitly disable mutual TLS mode.

![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/authz.svg)

The service mesh outputs these two authentication types, as well as other claims in the credentials (if applicable), to the next layer: [authorize](./authorize.md).

### Authentication Policy

This section provides more details on service mesh authentication strategies. As stated in [Authentication Schema](#_6),
Authentication policies are effective for requests received by the service. To specify a client authentication policy in mutual TLS,
Need to set `TLSSettings` in `DetinationRule`.

Like other service mesh configurations, authentication policies can be written in `.yaml` files. Deployment strategies use `kubectl`.
The authentication policy in the following example requires that mutual TLS must be used for transport layer authentication with workloads labeled `app:reviews`:

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

#### Policy storage

A service mesh stores mesh-wide policies in the root namespace. These strategies use an empty selector
Applied to all workloads in the mesh. Policies with namespace scope are stored in the corresponding namespace.
They apply only to workloads within their namespace. If you configure the `selector` field,
then the authentication policy applies only to workloads that match the criteria you configure.

Peer and `request-authentication` strategies are distinguished by the kind field,
They are `PeerAuthentication` and `RequestAuthentication` respectively.

#### Selector field

Peer and `request-authentication` policies use the `selector` field to specify the label of the workload to which the policy applies.
The following example shows the selector field for a policy that applies to a workload with the `app:product-page` tag:

```yaml
selector:
   matchLabels:
     app: product-page
```

If you do not provide a value for the `selector` field,
The service mesh then matches the policy to all workloads within the scope of the policy store.
Therefore, the `selector` field helps you specify the scope of the policy:

- mesh-wide policy: The policy specified for the root namespace, with or without an empty `selector` field.
- Namespace-scoped policies: policies specified for non-root namespaces, with no or with an empty `selector` field.
- Workload-specific policies: Policies defined in the general namespace with a non-empty `selector` field.

Peer and `request-authentication` policies follow the same hierarchy principles for the `selector` field,
But service meshes combine and apply these strategies in a slightly different way.

There can be only one mesh-wide `Peer Authentication` policy,
There can also only be one namespace-scoped `peer-authentication` policy per namespace.
When you configure multiple mesh-wide or namespace-wide `Peer Authentication` policies for the same mesh or namespace,
The service mesh ignores newer policies. When multiple workload-specific `Peer Authentication` policies match,
The service mesh will choose the oldest policy.

The service mesh applies the narrowest matching policy to each workload in the following order:

1. Workload-specific
1. Namespace scope
1. mesh range

The service mesh can combine all matching `request-authentication` policies,
Just like they come from a single `request-authentication` policy. therefore,
You can configure multiple mesh-wide or namespace-wide policies within a mesh or namespace.
However, it is still good practice to avoid using multiple mesh-scoped or namespace-scoped `request-authentication` strategies.

#### `Peer Authentication`

The `Peer Authentication` policy specifies the mutual TLS mode that the service mesh enforces for the target workload. The following modes are supported:

- PERMISSIVE: The workload accepts mutual TLS and plaintext traffic.
   This mode is useful during the migration of workloads that cannot use mutual TLS because they do not have sidecars.
   Once the workload has been migrated for sidecar injection, the mode should be switched to STRICT.
- STRICT: The workload receives only mutual TLS traffic.
- DISABLE: Disable mutual TLS. From a security perspective, don't use this mode unless you provide your own security solution.
- UNSET: Inherit the schema of the parent scope. The mesh-wide `Peer Authentication` policy in UNSET mode uses `PERMISSIVE` mode by default.

The following `peer authentication` policy requires mutual TLS for all workloads in namespace `foo`:

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

For workload-specific `peer authentication` policies, different mutual TLS modes can be specified for different ports.
You can only configure mutual TLS for port ranges on ports declared by the workload.
The following example disables mutual TLS on port 80 for the `app:example-app` workload,
And use the mutual TLS settings of the namespace-wide `Peer Authentication` policy for all other ports:

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

The `Peer Authentication` strategy above will only work if there is a Service defined like this,
Bind requests to the `example-service` service to `example-app`
Port `80` for workloads

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

#### `Request Authentication`

The `Request Authentication` policy specifies the values required to authenticate a JSON Web Token (JWT). These values include:

- the position of the token in the request
- the issuer of the request
- Public JSON Web Key Set (JWKS)

The service mesh checks the provided token (if provided) against the rules in the `Request Authentication` policy,
And reject requests with invalid tokens. When requests come without a token, they will be accepted by default.
To deny requests without a token, provide an authorization rule that specifies restrictions on specific actions (for example, paths or actions).

Multiple JWTs can be specified in `request-authentication` policies if they use unique locations.
When multiple policies match a workload, the service mesh combines all the rules,
It is as if the rules were specified as a single policy. This behavior is useful when developing workloads that accept different JWT providers.
However, requests with multiple valid JWTs are not supported because the output body for such requests is undefined.

#### Principal

When using the `peer-auth` policy and mutual TLS, the service mesh extracts the identity from `peer-auth` into `source.principal`.
Likewise, when you use the `request authentication` strategy, the service mesh will assign the identity in the JWT to `request.auth.principal`.
Use these principals to set authorization policies and as output from telemetry.

### Update authentication policy

You can change the authentication policy at any time, and the service mesh pushes the new policy to workloads in near real time.
However, a service mesh cannot guarantee that all workloads will receive the new policy at the same time.
The following suggestions can help avoid disruption when updating authentication policies:

- When changing the mode of the `Peer Authentication` policy from `DISABLE` to `STRICT`,
   Please use `PERMISSIVE` mode for transitions and vice versa. When all workloads have successfully switched to the desired mode,
   You can apply the strategy to the final pattern. You can use service mesh telemetry to verify that the workload switched over successfully.
- When migrating the `request-authentication` policy from one JWT to another,
   Add rules for new JWTs to this policy without removing old rules. so,
   The workload will accept both types of JWT, when all traffic is switched to the new JWT,
   You can delete old rules. However, each JWT must use a different location.

Next step: Set up [Peer Authentication](./peer.md) and [Request Authentication](./request.md)
