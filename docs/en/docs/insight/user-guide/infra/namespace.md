---
hide:
  - toc
---

# Namespace Monitoring

With namespaces as the dimension, you can quickly query resource consumption and trends within a namespace.

## Prerequisites

- Insight Agent is [installed](../../quickstart/install/install-agent.md) in the cluster and the applications are in the __Running__ state.

## Steps

1. Go to the __Insight__ product module.

2. Select __Infrastructure__ > __Namespaces__ from the left navigation pane. On this page, you can view the following information:

    1. **Switch Namespace**: Switch between clusters or namespaces at the top.
    2. **Resource Overview**: Provides statistics on the number of normal and total workloads within the selected namespace.
    3. **Incidents**: Displays the number of alerts generated within the selected namespace.
    4. **Events**: Shows the number of Warning level events within the selected namespace in the past 24 hours.
    5. **Resource Consumption**: Provides the sum of CPU and memory usage for container groups within the selected namespace, along with the CPU and memory quota information.


### Metric Explanations

| Metric Name | Description |
| -- | -- |
| CPU Usage | The sum of CPU usage for container groups within the selected namespace. |
| Memory Usage | The sum of memory usage for container groups within the selected namespace. |
| Container Group CPU Usage | The CPU usage for each container group within the selected namespace. |
| Container Group Memory Usage | The memory usage for each container group within the selected namespace. |
