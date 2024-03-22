# End-to-end Traffic lane

The microservice engine supports isolating relevant versions of an application (or other features) into an independent runtime environment (i.e., a lane), and then routing traffic that meets the rules of the lane to the target version (or other feature) of the application by setting lane rules.
This article introduces the concept of traffic lanes, use cases, and two modes of traffic lanes: strict and loose.

## Features

Gray release will forward a small part of online traffic to the new version of the service based on the request content or the proportion of request traffic. After the gray verification is passed, gradually increase the request traffic of the new version, which is a progressive release method.

When there are call chains between services, gray release of services often extends beyond individual services and requires environment isolation and traffic control for the entire request chain of services,
ensuring that gray traffic only goes to the gray version of services in the call chain, achieving isolation between call chains.

A lane is an isolation environment composed of different services with the same version (or other features).
By using the traffic lane feature, you only need to specify a small number of governance rules to build multiple traffic isolation environments from the gateway to the entire backend services,
effectively ensuring the smooth and secure release of multiple services and the parallel development of multiple versions of services, further promoting the rapid development of the business.

Traffic lanes are divided into strict and loose modes.

- Strict mode of traffic lanes

    In strict mode, each traffic lane contains all services in the call chain.
    This mode requires no requirements for your application, just configure the traffic lane.

- Loose mode of traffic lanes

    In loose mode, you only need to ensure the creation of a lane containing all services in the call chain: the baseline lane.
    Other lanes may not contain all services in the call chain. When a service in a lane calls another service,
    if the target service does not exist in the current lane, the request will be forwarded to the same service in the baseline lane,
    and when the request target exists in the current lane, the request will be redirected back to the current lane. When using the loose mode of traffic lanes,
    your application must include a request header that can be passed through the entire call chain (link-passing request header),
    and the value of the link-passing request header must be unique for each request.

## Comparison of Strict and Loose Modes

| **Traffic lane Mode** | **Advantages** | **Limitations** | **Use Cases** |
| ------------------------- | -------------- | --------------- | ------------- |
| Strict Mode | No requirements for applications in the lane. | Each traffic lane must include all services in the call chain. | Suitable for scenarios where the entire call chain needs to undergo gray release. When conducting gray release on the entire chain, the strict mode has lower requirements on the application itself. |
| Loose Mode | Requires the application to include a request header that can be passed through the entire call chain, and the value of the link-passing request header must be unique for each request. | Only need to ensure a baseline lane contains all services in the call chain, and requests from other lanes can fall back to the baseline lane. | When the application exhibits behavior of passing request headers through the call chain, the loose mode can achieve more flexible lane usage scenarios. For example, scenarios where only a portion of services in the call chain have been released, and a test environment is built based on these new version services. |
