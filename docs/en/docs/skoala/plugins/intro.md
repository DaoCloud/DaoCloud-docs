# Plugin Center

The Plugin Center is a unified plugin management portal for cloud-native gateways and cloud-native microservices. It involves various flow control, authorization, and custom plugins. Once configured, these plugins can be used in cloud-native gateways and cloud-native microservices, eliminating the need for redundant plugin development for the same business logic requirements and providing more convenience for developers and operators.

The microservice engine supports the integration of Auth, JWT, Global Rate Limit, Wasm, and ExtProc plugins.
**Plugins need to be integrated in the Plugin Center before they can be used in cloud-native microservices or gateways**.

- JWT (JSON Web Token) is an open standard for authentication and authorization. It consists of three parts:
  header, payload, and signature. JWT can be used to transmit information between clients and servers and
  verify it using signatures. In the cloud computing and cloud-native industry,
  JWT is commonly used for authentication and authorization in microservices architecture.

- Auth (Authorization) is a plugin used for user identity verification and access authorization.
  It can be used together with JWT to authenticate requests and determine whether to allow access to
  specific resources based on user permissions. The Auth plugin ensures that only authenticated users
  can access specific APIs or services.

- Rate Limit is a plugin used to limit the request rate. In cloud computing and cloud-native environments,
  a large number of requests can put a load on the system. The Rate Limit plugin helps limit the
  request rate per user or IP address to ensure system stability and security.

- Wasm (WebAssembly) is a low-level bytecode format that enables high-performance compiled code to run
  in web browsers. In the cloud computing and cloud-native industry, Wasm can be used as a
  runtime environment for plugins, allowing developers to use a wider range of programming languages
  and tools to extend and customize cloud services. By using Wasm plugins, more efficient,
  scalable, and flexible cloud-native applications can be achieved.

- ExtProc (External Process) is a plugin used to invoke an external process. The ExtProc plugin can forward
  requests and responses to an external process, which handles the request and returns the result.
  It can perform additional processing on requests, such as modifying request headers, request bodies,
  response headers, response bodies, etc., or perform additional custom logic based on the request information.

<!--![](../images/plugin01.png)-->