# Virtual Machine Monitoring

The virtual machine's monitoring is based on the Grafana Dashboard open-sourced by Kubevirt, which generates monitoring dashboards for each virtual machine.

Monitoring information of the virtual machine can provide better insights into the resource consumption of the virtual machine, such as CPU, memory, storage, and network resource usage. This information can help optimize and plan resources, improving overall resource utilization efficiency.

## Prerequisites

Before viewing the virtual machine monitoring information, the following prerequisites need to be met:

- The Insight-agent component needs to be installed in the same cluster where the virtual machine is located.

## Virtual Machine Monitoring

Navigate to the detailed information of the virtual machine and click on `Overview` to view the monitoring content of the virtual machine. Please note that without the Insight-agent component installed, monitoring information cannot be obtained. Below are the detailed information:

- Total CPU, CPU usage, total memory, memory usage.

    <!-- Add image later -->

- CPU usage rate: the percentage of CPU resources currently used by the virtual machine; Memory usage rate: the percentage of memory resources currently used by the virtual machine out of the total available memory.

    <!-- Add image later -->

- Network traffic: the amount of network data sent and received by the virtual machine during a specific time period; Network packet loss rate: the proportion of lost data packets during data transmission out of the total sent data packets.

    <!-- Add image later -->

- Network error rate: the rate of errors that occur during network transmission; Disk throughput: the speed and capacity at which the virtual machine system reads and writes to the disk within a certain time period.

    <!-- Add image later -->

- IOPS: the number of input/output operations the virtual machine system performs in one second. Disk latency: the time delay experienced by the virtual machine system when performing disk read and write operations.

    <!-- Add image later -->
