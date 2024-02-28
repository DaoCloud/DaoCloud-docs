# Virtual service parameter configuration

This page describes the parameter configuration when creating and editing a **Virtual Service**.

## Basic configuration

| UI element | YAML field | description |
| -------- | ------------------ | ------------------ ------------------------------------------ |
| Name | metadata.name | Required. Virtual service name. <br />Format requirements: lowercase letters, numbers and dashes (-), must start with a lowercase letter and end with a lowercase letter or number, up to 63 characters. |
| Namespace | metadata.namespace | Required. The namespace to which the virtual service belongs. In the same namespace, request identity authentication cannot have the same name. |
| Application Scope |spec.gateways | Required. The scope of virtual service application includes two types:<br />- specified gateway rules (multiple can be added), which can be used to expose internal services of the mesh;<br />- valid for all sidecars (-mesh). |
| Owning service |spec.hosts | Required. The service object of the application virtual service can include three types:<br />-registration service from the Kubernetes registry;<br />-registration service from the service entry;<br />-service domain name. |

## Routing configuration

Multiple routing rules can be added, and the execution order is from top to bottom, and the routing rules ranked first take effect first.

### HTTP Routing

Multiple HTTP routing rules can be dragged and sorted, any route can be collapsed, and only the route name is displayed.

#### Basic Information

| UI Elements | YAML Fields | Description |
| -------- | --------------- | --------------------- --------------------------------------- |
| Route Name | spec.http.-name | Required. http route name. <br />Format requirements: lowercase letters, numbers and dashes (-), must start with a lowercase letter and end with a lowercase letter or number, up to 63 characters. |

#### Routing matching rules

required. The YAML field is __spec.http.-name.match__ .

To match the request through URI path, port, etc., multiple rules can be added, and the order of execution is from top to bottom, and the top matching rule is used first.

| UI Elements | YAML Fields | Description |
| ---------- | ---------------------------- | --------- -------------------------------------------------- -|
| Match URI | spec.http.-name.match.uri | Optional. There are three matching methods for matching the URI path of the request: <br /> - exact (exact): the field completely matches <br /> - prefix (prefix): matches the field prefix <br /> - regular (regex) : match based on RE2-style regular expressions |
| match port | spec.http.-name.match.port | optional. Match the requested port. |
| Match header | spec.http.-name.match.header | Required. Matching the HTTP header of the request also supports three matching methods:<br />-exact (exact): the field completely matches<br />-prefix (prefix): matches the field prefix<br />-regular ( regex): matching based on RE2-style regular expressions |

#### Routing target/redirect rule

The features of __routing target__ and __redirection__ are mutually exclusive features, and only one of them can be selected in a __HTTP routing rule__ .

!!! note

     When the user turns on the __Proxy__ switch, this item and related content will be grayed out.

**routing rules**

| UI Elements | YAML Fields | Description |
| -------- | ----------------------------------------- ------ | ------------------------------------------- ----------------- |
| route destination | spec.http.-name.route.-destination | Optional. Routing targets that have matched the request, multiple routes can be added, and the routing targets with the highest ranking will be executed first. |
| Service Name | spec.http.-name.route.-destination.host | Required. The name or IP of the route target service. |
| Version Service | spec.http.-name.route.-destination.subset | Optional. The list comes from the available __Destination Rules__ for the selected service. |
| Weight | spec.http.-name.route.weight | Optional. The distribution weight of the traffic occupied by each route in this __route target__ . The sum of weights of all __route targets__ should be 100. |
| port | spec.http.-name.route.-destination.port.number | Optional. The port of the routing target service. |

**redirect**

| UI Elements | YAML Fields | Description |
| ---------- | ---------------------------------------- | -------------------------------------------------- ---------- |
| redirect | spec.http.-name.redirect | Optional. Redirects are used to forward requests to other paths. |
| Redirect path | spec.http.-name.redirect.uri | Required. The new access address path (URI). |
| authority | spec.http.-name.redirect.authority | Optional. The authentication information part in the URI path, usually __//__ means the beginning, and __/__ means the end. |
| port | spec.http.-name.redirect.port.number | Optional. The port number of the redirection service. |
| Response Code | spec.http.-name.redirect.redirectCode | Optional. Specify the response code. When the specified error code is returned, the redirection operation will be performed. The default value is 301. |

#### Optional settings

In addition, 6 optional settings are provided, which you can enable or disable according to your actual needs.

**Rewrite**

| UI Elements | YAML Fields | Description |
| --------- | ----------------------------------- | ---- -------------------------------------------------- ------ |
| rewrite | spec.http.-name.rewrite | Optional. Off by default l can reproduce the full path, or just rewrite the http prefix. |
| Rewrite path | spec.http.-name.rewrite.uri | Required. The new access address path (URI). |
| authority | spec.http.-name.redirect.authority | Optional. The authentication information part in the URI path, usually __//__ means the beginning, and __/__ means the end. |

**time out**

| UI Elements | YAML Fields | Description |
| -------- | ----------------------- | ---------------- ----------------------------------------------- |
| timeout | spec.http.-name.timeout | Optional. Disabled by default. The timeout feature is used to define the waiting time for initiating a request to the target service. |
| Timeout | spec.http.-name.timeout | Required. The tolerable timeout period. Input format: number + unit (s, m, h, ms). |

**Retry**

| UI Elements | YAML Fields | Description |
| -------- | ---------------------------------------- | -- -------------------------------------------------- -------- |
| retries | spec.http.-name.retries | Optional. Disabled by default. The retry feature is used to define the number of attempts to re-initiate the request when the request feedback is abnormal. |
| Number of retries | spec.http.-name.retries.attempts | Optional. The number of retries for a request that returns an exception. The default retry interval is 25ms. <br />When both the retry and timeout features are enabled, the product of the number of retries, the timeout of retries, and the timeout period takes effect, whichever is the shortest, so the actual number of retries may be less than the set value. |
| retry timeout | spec.http.-name.retries.perTryTimeout | Optional. The timeout length of each retry is the same as the timeout feature setting (http.route.timeout) by default. Input format: number + unit (s, m, h, ms). |
| Retry Conditions | spec.http.-name.retries.retryOn | Optional. Preconditions for allowing retries, this item contains multiple checks:<br />- 5xx: When the upstream server returns a 5xx response code or no response (disconnect/reset/read timeout), envoy will retrytry. <br />- refused-stream: Envoy will retry when the upstream server resets the stream with error code REFUSED_STREAM. <br />- gateway-error: Only retry for 502, 503, 504 errors. <br />- retriable-status-codes: When the return code of the upstream server is the same as the response code or the x-envoy-retriable-status-codes definition in the request header, retry. <br />- reset: When the upstream server is unresponsive (disconnect/reset/read timeout), will retry. <br />- connect-failure: When the connection with the upstream server fails (connection timeout, etc.) and the request fails, it will be retried. <br />- retriable-headers: When the upstream server response code matches the definition in the retry policy or matches the x-ENVIGET-retriable-header-NAME header, a retry will be attempted. <br />- envoy-ratelimited: Retry when header x-ENVISENT-ratelimited is present. <br />- retriable-4xx: envoy will retry when the upstream server returns a 4xx response code (currently only 409). |

**Fault Injection**

| UI Elements | YAML Fields | Description |
| ------------ | ------------------------------------ -- | ----------------------------------------------- ------------- |
| Fault Injection | spec.http.-name.fault | Optional. Disabled by default. <br />The fault injection feature is used to inject faults into the target service at the application layer, and can provide two types of faults: "delay" and "termination". When using fault injection, timeout and retry features cannot be enabled. |
| Delay duration | spec.http.-name.delay.delay.fixedDelay | Required. The length of time that the request response can be delayed Input format: number + unit (s, m, h, ms). |
| Fault injection percentage | spec.http.-name.fault.delay.percentage | Optional. Fault injection ratio in all requests, default 100%. |
| Abort Response Code | spec.http.-name.fault.abort.httpStatus | Required. The http return code used to terminate the current request. |
| Fault injection percentage | spec.http.-name.fault.abort.percentage | Optional. Fault injection ratio in all requests, default 100%. |

**Proxy Virtual Service**

The YAML field is __spec.http.-name.delegate__ , which is off by default.

- The virtual service proxy feature can split the routing configuration into two virtual services, master and slave. The master virtual service completes the basic settings and matching rules, and the proxy virtual service completes the specific routing rules.

- After the proxy feature is enabled, only the route matching of the main virtual service takes effect, and the routing matching rules of the proxy virtual service do not need to be set.

- The routing rules of the proxy virtual service will be combined with the routing rules of the main virtual service.

- The proxy feature does not support nesting, and only the main virtual service can enable the proxy function.

- Proxies are not configurable when the virtual service has "route target/redirect" configured.

| UI Elements | YAML Fields | Description |
| ------------ | ----------------------------------- | - -------------------------------------------------- --------- |
| Delegate Virtual Service | spec.http.-name.delegate.name | Required. Secondary virtual service for proxy<br />Note:<br />A virtual service configured with a proxy item cannot be used as a proxy, that is, a proxy cannot be nested;<br />A virtual service configured with the spec.hosts field Not available as an agent. |
| Owning namespace | spec.http.-name.delegate.namespace | Optional. The namespace to which the secondary virtual service belongs is the same as the main virtual service by default. |

**Traffic image**

| UI element | | YAML field | Description. |
| ------------ | ---- | ------------------------------- -------------- | ----------------------------------- --------------------- |
| traffic image | n | spec.http.-name.image | Optional. Disabled by default. Used to replicate request traffic to other target services. |
| image to service | y | spec.http.-name.mirror.host | Required. The transfer target service of traffic image. |
| Traffic image percentage | n | spec.http.-name.mirror.mirrorPercentage:value | Optional. The ratio of the copied request traffic to the original request traffic, the default is 100%. |
| service version | n | spec.http.-name.mirror.subset | optional. The service version list content comes from the available "Destination Rules" for the current target service. |

### TLS Routing

- Multiple entries can be added, and the order of execution is from top to bottom, and the top routing rules take effect first

- Multiple TLS routing rules can be dragged and sorted

- Each route can be collapsed, only the route name is displayed

#### Routing matching rules

The YAML field is __spec.tls.-name.match__ .

Match requests by port (-port) and SNI (-port.sniHosts) names, and multiple rules can be added. The order of execution is from top to bottom, and the top matching rules are used first.

#### Routing target

| UI Elements | YAML Fields | Description |
| ------------ | ------------------------------------ --------- | ---------------------------------------- -------------------- |
| Add Route Target | spec.tls.-name.route | Required. Add routing target information, multiple items can be added, and the order of execution is from top to bottom |
| Service Name | spec.tls.-name.route.-destination.host | Required. The target service name, the drop-down list contains all services that enable the tls protocol under the current namespace |
| port | spec.tls.-name.route.-destination.port.number | Optional. target service port |
| Service Version | spec.tls.-name.route.-destination.subset | Optional. The service version list content comes from the available "Destination Rules" for the current target service. |
| Weight | spec.tls.-name.route.-destination.weight | Optional. The distribution weight of each "routing destination" in this "tls routing" rule. The sum of the weights of each rule should be 100. |

### TCP Routing

- Multiple entries can be added, and the order of execution is from top to bottom, and the top routing rules take effect first

- Drag and sort between multiple TCP routing rules

- Each route can be collapsed, only the route name is displayed

#### Routing matching rules

| UI Elements | YAML Fields | Description |
| ---------------- | -------------------------- | ----- -------------------------------------------------- ----- |
| Add route matching rules | spec.tcp.-name.match | Optional. To match the request by port (-port), multiple rules can be added, and the order of execution is from top to bottom, and the matching rule with the highest ranking is used first. |
| port | spec.tcp.-name.match.-port | Required. tcp port number. |

#### Routing target

| UI Elements | YAML Fields | Description |
| ------------ |------------------------------------ --------- | ---------------------------------------- -------------------- |
| Add Route Target |spec.tcp.-name.route | Required. Add routing target information, multiple items can be added, and the execution order is from top to bottom. |
| Service Name | spec.tcp.-name.route.-destination.host | Required. The target service name, the drop-down list contains all services of the tcp protocol available in the current namespace. |
| port |spec.tcp.-name.route.-destination.port.number | Optional. Target service port. |
| Service version |spec.tcp.-name.route.-destination.subset | Optional. The service version list content comes from the available "Destination Rules" for the current target service. |
| Weight |spec.tcp.-name.route.-destination.weight | Optional. The distribution weight of each "routing destination" in this "TCP routing" rule. The sum of the weights of each rule should be 100. |
