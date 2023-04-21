# Sentinel service governance rules

The microservice engine supports managing east-west traffic through [service grid](../../../../mspider/user-guide/02TrafficGovernance/README.md) or Sentinel. This page describes the governance rules used when using Sentinel for service governance.

## flow control rules

The principle of flow control rules is to monitor the QPS indicator of application or service traffic. When the indicator reaches the threshold, the request flow is controlled according to the preset rules to prevent the application from crashing due to the inability to handle too much traffic in a short period of time. After using flow control rules, the system can gradually process accumulated requests during the next idle period, and resume normal flow request control when the indicator returns below the threshold.

- Resource name: the name of the resource, and the resource refers to the role domain of the rule.

- Source application: Sentinel can limit the flow for the caller, and the default is default, which means that it does not distinguish the source and limits all.

- Flow control mode: There are three types of flow control modes.
  
     - Direct mode: When the current resource reaches the threshold, the flow is directly limited.
     - Association mode: When the associated resource reaches the threshold, the associated resource is limited.
     - Link mode: Only record the traffic on the specified link (the traffic of the specified resource coming in from the ingress resource, if it reaches the threshold, the traffic can be limited).

- Threshold type:

     - QPS: QPS refers to the number of requests per second. When the QPS of calling this interface reaches the threshold, the flow will be limited.
     - Number of threads: Limit the flow when the number of threads calling this interface reaches the threshold.

- Threshold mode:

     - Standalone Threshold: Set the threshold only for a certain node.
     - Cluster or not: Whether to set the threshold for the entire cluster.

- Flow control effect:

     - Fast fail: When the traffic exceeds the set threshold, the request is directly rejected.

     - Warm Up: Slowly increase the passing traffic, gradually warm up the system, and prevent the idle system from being overwhelmed by a sudden influx of large amounts of traffic. Starting from the requested QPS threshold / 3, set the warm-up time, and gradually increase to the set QPS threshold after the warm-up time.

     - Waiting in queue: When the traffic exceeds the threshold, the queue passes at a uniform speed. The threshold type must be set to QPS, otherwise it is invalid. It is suitable for dealing with intermittent burst traffic, where a large number of requests flood in in a certain second, and it is idle in the next few seconds, such as a message queue.

    

## Fuse downgrade

In a distributed system, each service usually needs to call other internal or external services to run normally. If the called service is not stable enough, the cascading effect will cause the caller's own response time to become longer, resulting in thread accumulation and even causing service is not available. In order to avoid this situation, it is necessary to cut off unstable call links according to preset rules through the fuse mechanism, or downgrade downstream services to protect the overall availability of the system.

- Circuit breaker strategy:

     - Slow call ratio: When the average response time per second of the request exceeds the maximum RT, and the number of requests passed within the time window >=5, the degradation is triggered when these two conditions are met at the same time.

     - Abnormal ratio: When the number of requests within the statistical period reaches the minimum number of requests and the ratio of abnormal requests is greater than the threshold, a circuit breaker is triggered.

     - Number of exceptions: After the number of abnormal requests within the statistical period exceeds the threshold, a fuse downgrade is triggered.

- Ratio Threshold: The slow call ratio threshold percentage that triggers the circuit breaker.

- Maximum RT: The longest response time of the request, if it exceeds this time, it will be judged as a slow request, the unit is ms, and the maximum value is 4900.

- Fuse duration: Set the duration of the fusing, after the fusing duration is exceeded, the fusing will be canceled and the original service call will be restored.

- Minimum number of requests: The minimum number of requests to trigger a circuit breaker, and the circuit breaker mechanism will be activated when this number is exceeded.

    

- Statistical duration: Statistical time window, that is, to count the number of requests within a certain period of time.

## Hotspot rules

Hotspots refer to data that is accessed frequently. When setting hotspot rules, you need to configure hotspot parameters (that is, the target parameters that need to count visits), and then the system will count the requests for this hotspot parameter. When a certain threshold is reached, resources containing this hotspot parameter will be restricted from calling. The hotspot rule is suitable for counting resources that are frequently accessed, and restricts access to the resource after a certain threshold is reached.


- Parameter index: Specifies the subscript of the hotspot parameter, starting from 0. Defaults to 0 if extra arguments don't match.
- Parameter exceptions: set thresholds individually for specified parameter values, and only support basic types and string types.



## System rules

System rules refer to Sentinel's comprehensive system capacity, CPU usage, average response time, entrance QPS and other data, and automatically select flow control rules to control request traffic from the overall dimension. It should be noted that system rules only take effect on ingress traffic, that is, traffic entering the application. When setting system rules, you need to select the threshold type. Currently, five thresholds are supported:

- Load: Use the system load as a heuristic indicator for adaptive system protection. System protection will only be triggered when the system load exceeds the set heuristic value and the current number of concurrent threads in the system exceeds the estimated system capacity.

!!! note

     Load type thresholds are only valid for Linux/Unix-like machines.

- RT: When the average response time of all ingress traffic on a single machine reaches the threshold, system protection is triggered, and the unit is milliseconds.

- Number of threads: When the number of concurrent threads of all ingress traffic on a single machine reaches the threshold, system protection is triggered.

- Ingress QPS: When the QPS of all ingress traffic on a single machine reaches the threshold, system protection is triggered.

- CPU usage: When the system CPU usage exceeds the threshold, system protection will be triggered (value range 0.0-1.0).

    

## Authorization rules

- Flow control application: the caller, that is, the source of the call, such as an app-side call or a PC-side call.

- Authorization type:

     - Whitelist: Only when the request source is in the whitelist can it be released.

     - Blacklist: If the source of the request is in the blacklist, it will not pass, and the rest of the requests will be allowed.

    

## Cluster flow control

Cluster flow control can control the real-time call volume of a service calling the entire cluster, and can solve the problem of poor overall flow limiting effect due to uneven flow. Cluster flow control can accurately control the total number of calls in the entire cluster, and combined with single-machine current limiting, it can better exert the effect of traffic protection.