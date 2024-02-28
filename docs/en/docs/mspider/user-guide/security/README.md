---
hide:
   - toc
---

# Security Governance

The service mesh provides an [authorization mechanism](./authorize.md) and two authentication methods ([request identity authentication](./request.md) and [peer identity authentication](./peer.md) ),
Users can create and edit resource files in the service mesh through wizards and YAML writing.
And you can create rules for the three levels of mesh global, namespace, and workload. When the resources are successfully created, Istiod will convert them into configurations and distribute them to the sidecar agent for execution.



### Authorization mechanism

The authorization mechanism provided by the service mesh allows you to control access to services.
Using the authorization mechanism, you can define rules specifying which services are allowed to communicate with each other.
These rules can be based on various factors, such as the source and destination of the traffic, the protocol used, and the identity of the client making the request.
By using the service mesh's authorization mechanism, you can ensure that only authorized traffic is allowed to flow in your service mesh.

Here's an example of how to restrict traffic between two services using a service mesh's authorization mechanism:

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

In this example, we create an __AuthorizationPolicy__ resource that allows traffic to the my-service service from any namespace except my-namespace, but only for GET requests.
See also [How GUIs are created](./authorize.md).

### Request authentication

Request authentication is used to verify the identity of clients making requests to a service.

Here's an example of how to authenticate a client using request-level authentication:

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

In this example, we create a __RequestAuthentication__ resource that authenticates the identity of clients making requests to the my-service service.
We use a JSON Web Token (JWT) to authenticate the client, specifying the issuer and the location of the public key used to validate the token.
See also [How GUIs are created](./request.md).

### Peer Authentication

Peer authentication is used to verify the identity of the service itself. The service mesh offers several peer authentication options, including mutual TLS authentication and JSON Web Token-based authentication.

Here's an example of how to verify the identity of a service using mutual TLS authentication:

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

In this example, we create a __PeerAuthentication__ resource that requires mutual TLS authentication for the my-service service.
We use STRICT mode, which requires both client and server to present valid certificates.
See also [How GUIs are created](./peer.md).

See [Service Mesh Identity and Authentication](./mtls.md) for more instructions.
