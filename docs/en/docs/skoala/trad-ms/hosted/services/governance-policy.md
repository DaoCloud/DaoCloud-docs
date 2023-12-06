# Rule introduction

The micro-service engine supports east-west traffic governance via a service mesh or Sentinel.

## Sentinel governance rules

- [flow-control.md](flow-control.md)

    The principle of the flow control rule is to monitor the QPS metric of application or service traffic. When the metric reaches the threshold, the traffic is controlled according to the preset rule, preventing application crashes due to excessive traffic processing in a short period of time. After the flow control rule is used, the system can gradually process the accumulated requests in the following idle period. When the metric falls below the threshold again, normal traffic request control is resumed.

- Fusing Rules

    In a distributed system, each service usually needs to call other internal or external services in order to run properly. If the called service is not stable, the cascading effect will lead to the response time of the caller, resulting in thread accumulation and even service unavailability. To avoid this situation, the circuit breaker should be used to cut off unstable call traces according to preset rules, or degrade downstream services to protect the overall availability of the system.

- Hot Rules

    Hotspot refers to frequently accessed data. When setting a hotspot rule, you need to set hotspot parameters (target parameters for traffic statistics). Then, the system collects statistics on the request volume of the hotspot parameter. When the request volume reaches a certain threshold, the resource containing the hotspot parameter is restricted. Hotspot rules apply to statistics on frequently accessed resources. When a certain threshold is reached, the access to the resource is restricted.

- System rules

    System rules refer to the automatic selection of flow control rules to control the request traffic from the overall dimension based on Sentinel"s integrated system capacity, CPU usage, average response time, inbound QPS and other data. Different from other rules, system rules take effect only on the inbound traffic at the application level. Other rules usually control the resource dimension.

- Authorization rules

    Authorization rules allow traffic governance based on the source of requests. For example, only requests initiated by callers in the whitelist are allowed, but requests initiated by callers in the blacklist are not allowed.

[Flow Control](flow-control.md){ .md-button .md-button--primary }

## Mesh governance rules

Traffic governance provides users with three resource configurations: virtual service, target rule, and gateway rule. By configuring corresponding rules, you can implement multiple traffic governance features, such as routing, redirection, circuit breaker, and traffic diversion. Users can create and edit governance policies through wizards or YAML.

- Virtual services are used to customize routing rules for request traffic and perform data flow diversion, redirection, and timeout return.
- The target rules pay more attention to the governance of traffic itself, and provide more powerful features such as load balancing, connection survival search, and circuit breaker for the requested traffic.
- Gateway rules provide ways for Istio gateways to expose services on the gateway.

See [Traffic Governance](../../../../mspider/user-guide/traffic-governance/README.md) for detailed descriptions of these three governance rules.

[Virtual Service](../../../../mspider/user-guide/traffic-governance/virtual-service.md){ .md-button .md-button--primary }[Destination Rules](../../../../mspider/user-guide/traffic-governance/destination-rules.md) { .md-button .md-button--primary }[Gateways](../../../../mspider/user-guide/traffic-governance/gateway-rules.md) { .md-button .md-button--primary }
