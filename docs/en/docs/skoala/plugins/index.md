---
hide:
  - toc
---

# Plugin Center

The Plugin Center is a unified plugin management portal for cloud-native gateways and cloud-native microservices. It involves various flow control, authorization, and custom plugins. Once configured, these plugins can be used in cloud-native gateways and cloud-native microservices, eliminating the need for redundant plugin development for the same business logic requirements and providing more convenience for developers and operators.

The microservice engine supports the integration of Auth, JWT, Global Rate Limit, Wasm, and ExtProc plugins.
**Plugins need to be integrated in the Plugin Center before they can be used in cloud-native microservices or gateways**.

<div class="grid cards" markdown>

- :simple-jsonwebtokens:{ .lg .middle } __JWT__

    ---

    JWT (JSON Web Token) is an open standard for authentication and authorization. It consists of three parts:
    header, payload, and signature. JWT can be used to transmit information between clients and servers and
    verify it using signatures. In the cloud computing and cloud-native industry,
    JWT is commonly used for authentication and authorization in microservices architecture.

- :material-shield-lock:{ .lg .middle } __Auth__

    ---

    Auth (Authorization) is a plugin used for user identity verification and access authorization.
    It can be used together with JWT to authenticate requests and determine whether to allow access to
    specific resources based on user permissions. The Auth plugin ensures that only authenticated users
    can access specific APIs or services.

- :material-speedometer:{ .lg .middle } __Global Rate Limit__

    ---

    Rate Limit is a plugin used to limit the request rate. In cloud computing and cloud-native environments,
    a large number of requests can put a load on the system. The Rate Limit plugin helps limit the
    request rate per user or IP address to ensure system stability and security.

- :material-chip:{ .lg .middle } __Wasm__

    ---

    Wasm (WebAssembly) is a low-level bytecode format that enables high-performance compiled code to run
    in web browsers. In the cloud computing and cloud-native industry, Wasm can be used as a
    runtime environment for plugins, allowing developers to use a wider range of programming languages
    and tools to extend and customize cloud services. By using Wasm plugins, more efficient,
    scalable, and flexible cloud-native applications can be achieved.

- :material-cog:{ .lg .middle } __ExtProc__

    ---

    ExtProc (External Process) is a plugin used to invoke an external process. The ExtProc plugin can forward
    requests and responses to an external process, which handles the request and returns the result.
    It can perform additional processing on requests, such as modifying request headers, request bodies,
    response headers, and response bodies, or perform additional custom logic based on the request information.

</div>

<!--![](../images/plugin01.png)-->

## Plugin Applications

<div class="grid cards" markdown>

- :material-lan:{ .lg .middle } __Using JWT Plugin for Microservices__

    ---

    Create a hosted mesh in the service mesh, import the demo application, and enable the JWT plugin in cloud-native microservices.

    [:octicons-arrow-right-24: Get started](jwt-ms.md)

- :material-gate:{ .lg .middle } __Using JWT Plugin for Gateway__

    ---

    Create a gateway, domains, and APIs, and enable JWT authentication in the security policy of a domain or API.

    [:octicons-arrow-right-24: Get started](jwt.md)

- :material-shield-key:{ .lg .middle } __Gateway Access to Authentication Server__

    ---

    Deploy the authentication server, integrate it with the cloud-native gateway, and enable authentication for domains and APIs.

    [:octicons-arrow-right-24: Get started](auth-server.md)

- :material-key:{ .lg .middle } __Integrate AK/SK Authentication__

    ---

    Demonstrate how to integrate AK/SK authentication based on the authentication server, including deployment and request verification.

    [:octicons-arrow-right-24: Get started](ak-sk-demo.md)

- :material-certificate:{ .lg .middle } __Integrate OIDC Authentication__

    ---

    Integrate third-party authentication services based on the OIDC protocol for single sign-on and access control.

    [:octicons-arrow-right-24: Get started](OIDC-auth.md)

- :material-timer:{ .lg .middle } __Gateway Access to Rate Limit Server__

    ---

    Deploy the global rate limit server, integrate it with the cloud-native gateway, and configure rate limit policies for domains and APIs.

    [:octicons-arrow-right-24: Get started](global-ratelimit.md)

</div>

## Custom Plugin Examples

The following examples are implemented in Go based on Envoy's `ext_proc` capability and can serve as references for custom plugin development:

<div class="grid cards" markdown>

- :material-flash:{ .lg .middle } __caching__

    ---

    Cache responses to GET requests in a non-persistent store and serve subsequent requests directly from the cache.

    [:octicons-arrow-right-24: View example](envoy-extproc-caching-demo-go.md)

- :material-shield-lock:{ .lg .middle } __anti (anti-replay)__

    ---

    Verify the sign, timestamp, and nonce before routing requests to the upstream, and respond with 401 if any check fails.

    [:octicons-arrow-right-24: View example](envoy-extproc-anti-demo-go.md)

- :material-certificate:{ .lg .middle } __crc32-check__

    ---

    Perform a CRC check on the request body before routing it to the upstream, and respond with 403 if the check fails.

    [:octicons-arrow-right-24: View example](envoy-extproc-crc32-check-demo-go.md)

- :material-cog:{ .lg .middle } __method-conv__

    ---

    Convert GET/POST requests initiated by the downstream into POST/GET requests before sending them to the upstream.

    [:octicons-arrow-right-24: View example](envoy-extproc-method-conv-demo-go.md)

- :material-puzzle:{ .lg .middle } __payload-limit__

    ---

    Check the request body size before routing it to the upstream, and respond with 413 if it exceeds the allowed maximum.

    [:octicons-arrow-right-24: View example](envoy-extproc-payloadlimit-demo-go.md)

</div>
