---
MTPE: windsonsea
date: 2024-05-21
hide:
  - toc
---

# Operator

Operator is the daily management of IT resources by IT operations personnel, handling workspace tasks.

![Operator Overview](../images/oam-overview.png)

To meet the needs of different operations and maintenance (O&M) scenarios, the O&M management module is designed with the following core subpages:

- **Overview**  
  Provides a holistic view of the cluster by displaying key metrics on a large dashboard, including node resource usage, GPU utilization, GPU power consumption, and GPU device temperature. O&M personnel can quickly identify cluster bottlenecks and resource anomalies and make timely decisions.

- **Resource Flavor**  
  Used to define available compute resource objects in the cluster, including CPU, memory, and GPU resources. Through resource pools, workloads can be bound to specific node types, enabling fine-grained resource allocation and management, thereby improving scheduling efficiency and overall cluster performance.

- **Queue Management**  
  Used to manage and optimize batch workloads by scheduling tasks through a queue system. Queue management enables合理 resource allocation and balances the execution order of high-priority and low-priority tasks, improving cluster throughput and reducing resource idle time.

- **GPU Info**  
  Automatically aggregates GPU resource information across the entire platform and provides detailed visibility into GPU device status. Administrators can view per-GPU load statistics, power usage, temperature, and running tasks, supporting GPU resource monitoring and optimized scheduling.

## Common Terminology

- **GPU Allocation**  
  Statistics on the GPU allocation status of all unfinished jobs in the current cluster, and calculate the ratio between requested GPUs (Request) and total resources (Total).

- **GPU Utilization**  
  Statistics on the actual resource utilization of all running jobs in the current cluster, and calculate the ratio between the actual GPU usage and total resources.

## Extended Features and Best Practices

1. **Real-Time Monitoring and Alerts**  
   In conjunction with the Overview page, configure threshold-based alerts for GPU temperature, power, and utilization to notify O&M personnel immediately in abnormal situations, preventing hardware damage and task failures.

2. **Resource Pool Strategy Optimization**  
   Divide resource pools appropriately for different types of workloads (short jobs, long-running jobs, GPU-intensive tasks, etc.) to improve resource reuse and reduce task queueing time.

3. **Queue Scheduling Optimization**  
   Design fair or weighted scheduling strategies based on task priority, resource requirements, and historical runtime to improve task completion rates and overall cluster throughput.

4. **GPU Resource Analysis**  
   Regularly analyze GPU utilization and allocation data to identify inefficient resource usage, and adjust task assignment or migration strategies to maximize GPU utilization.

5. **O&M Reports**  
   Generate periodic reports covering resource usage trends, task completion status, and GPU efficiency to provide data-driven support for decision-making.
