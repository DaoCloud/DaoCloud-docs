---
hide:
  - toc
---

# Container Insight

Container monitoring is the process of monitoring workloads in cluster management. In the list, you can view basic information and status of workloads. On the workload details page, you can see the number of active alerts and the trend of resource consumption such as CPU and memory.

## Prerequisites

- The cluster has Insight Agent installed, and all container groups are in the `Running` state.

- To install Insight Agent, please refer to: [Installing insight-agent online](../../../insight/quickstart/install/install-agent.md) or [Offline upgrade of insight-agent](../../../insight/quickstart/install/offline-install.md).

## Steps

Follow these steps to view service monitoring metrics:

1. Go to the `Observability` product module.

2. Select `Infrastructure` > `Containers` from the left navigation pane.

3. Switch between tabs at the top to view data for different types of workloads.


4. Click the target workload name to view the details.

    1. Incidents: Displays the total number of active alerts for the workload.
    2. Resource Consumption: Shows the CPU, memory, and network usage of the workload.
    3. Monitoring Metrics: Provides the trends of CPU, memory, network, and disk usage for the workload over the past hour.


### Metric Explanations

| Metric Name | Description |
| -- | -- |
| CPU Usage | The sum of CPU usage for all container groups under the workload.|
| CPU Requests | The sum of CPU requests for all container groups under the workload.|
| CPU Limits | The sum of CPU limits for all container groups under the workload.|
| Memory Usage | The sum of memory usage for all container groups under the workload.|
| Memory Requests | The sum of memory requests for all container groups under the workload.|
| Memory Limits | The sum of memory limits for all container groups under the workload.|
| Disk Read/Write Rate | The total number of continuous disk reads and writes per second within the specified time range, representing a performance measure of the number of read and write operations per second on the disk.|
| Network Send/Receive Rate | The incoming and outgoing rates of network traffic, aggregated by workload, within the specified time range.|
