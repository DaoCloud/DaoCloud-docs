# Service Topology Element Explanations

The service topology provided by Observability allows you to quickly identify the request relationships between services and determine the health status of services based on different colors. The health status is determined based on the request latency and error rate of the service's overall traffic. This article explains the elements in the service topology.

## Node Status Explanation

The node health status is determined based on the error rate and request latency of the service's overall traffic, following these rules:

| Color | Status | Rules |
| ----- | ------ | ----- |
| Gray  | Healthy | Error rate equals 0% and request latency is less than 100ms |
| Orange | Warning | Error rate (0, 5%] or request latency (100ms, 200ms] |
| Red | Abnormal | Error rate (5%, 100%] or request latency (200ms, +Infinity) |

## Connection Status Explanation

| Color | Status | Rules |
| ----- | ------ | ----- |
| Green | Healthy | Error rate equals 0% and request latency is less than 100ms |
| Orange | Warning | Error rate (0, 5%] or request latency (100ms, 200ms] |
| Red | Abnormal | Error rate (5%, 100%] or request latency (200ms, +Infinity) |
