# Service topology

On the service topology page, you can view the previous calls and dependencies of services that access trace data. Understand the call relationship between services through the visualized topology, and view the calls and performance status of services within a specified time.

## Service Topology

The connection between the nodes of the topology graph represents the calling relationship between the two services within the query time range.
Follow the steps below to view service monitoring metrics:

1. Go to `Observability` product module,
2. In the left navigation bar, select `Scene Monitoring -> Service Topology`.
3. In the topology map, you can perform the following operations as required:

- Click on the node to view the traffic metrics of the service.
- When the mouse hovers over the connection, you can view the traffic metrics requested between services.
- In the `Display Settings` module, it is possible to configure the display elements in the topology map.

     

## Node health status

The node health status is determined according to the error rate and request delay of all current service traffic. The judgment logic is as follows:

| Status | Rules |
| ---- | ---------------------------------------- |
| Healthy | The error rate is equal to 0% and the request latency is less than 100ms |
| Warning | Error Rate (0, 5%] or Request Latency (100ms, 200ms] |
| Exception | Error Rate (5%, 100%] or Request Latency (200ms, +Infinity)|
