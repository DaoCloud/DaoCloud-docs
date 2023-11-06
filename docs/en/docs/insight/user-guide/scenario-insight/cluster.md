# Cluster monitoring

Cluster monitoring can view the basic information of the cluster, the resource consumption in the cluster and the change trend of resource consumption over a period of time.

## Prerequisites

The cluster has [insight-agent installed](../../quickstart/install/install-agent.md) and the application is in `running` state.

## Steps

1. Go to the `Observability` product module.

2. Select `Infrastructure > Clusters` from the left navigation pane. On this page, you can view the following information:

    1. **Cluster List**: Shows a list of clusters with the `insight-agent` installed. Click a specific cluster to view detailed information.
    2. **Resource Overview**: Provides statistics on the number of normal and total nodes and workloads across multiple clusters.
    3. **Incidents**: Displays the number of alerts generated in the current cluster.
    4. **Resource Consumption**: Shows the actual usage and total capacity of CPU, memory, and disk for the selected cluster.
    5. **Metric Explanations**: Describes the trends in CPU, memory, disk I/O, and network traffic for the selected cluster.

### Metric Explanations

| Metric Name | Description |
| -- | -- |
| CPU Usage Rate | The ratio of the actual CPU usage of all pod resources in the cluster to the total CPU capacity of all nodes.|
| CPU Allocation Rate | The ratio of the sum of CPU requests of all pods in the cluster to the total CPU capacity of all nodes.|
| Memory Usage Rate | The ratio of the actual memory usage of all pod resources in the cluster to the total memory capacity of all nodes.|
| Memory Allocation Rate | The ratio of the sum of memory requests of all pods in the cluster to the total memory capacity of all nodes.|
