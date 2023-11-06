# Node monitoring

Through node monitoring, you can get an overview of the current health status of the nodes in the selected cluster and the number of abnormalities in the corresponding pod; on the current node details page, you can view the number of alerts and the trend graph of resource consumption such as CPU, memory, and disk.

## Prerequisites

- The cluster has [insight-agent installed](../../quickstart/install/install-agent.md) and the application is in `running` state.

## Steps

1. Go to the `Insight` product module.

2. Select `Infrastructure` > `Nodes` from the left navigation pane. On this page, you can view the following information:

    1. **Cluster Switching**: Use the dropdown at the top to switch between clusters.
    2. **Node List**: Shows a list of nodes within the selected cluster. Click a specific node to view detailed information.
    3. **Incidents**: Displays the number of alerts generated in the current cluster.
    4. **Resource Consumption**: Shows the actual usage and total capacity of CPU, memory, and disk for the selected node.
    5. **Metric Explanations**: Describes the trends in CPU, memory, disk I/O, and network traffic for the selected node.


### Metric Explanations

| Metric Name | Description |
| -- | -- |
| CPU Usage Rate | The ratio of the actual CPU usage of the node to the total CPU capacity of the node.|
| Memory Usage Rate | The ratio of the actual memory usage of the node to the total memory capacity of the node.|
| Disk Read/Write Rate | The rate at which the disk is reading from or writing to data, measured in bytes per second.|
| Network Receive/Send Rate | The incoming and outgoing rates of network traffic, measured in bytes per second.|
