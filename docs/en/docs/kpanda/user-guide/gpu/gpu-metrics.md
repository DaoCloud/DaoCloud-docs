# GPU Metrics

This page lists some commonly used GPU metrics.

## Cluster Level

| Metric Name | Description |
| ----------- | ----------- |
| Number of GPUs | Total number of GPUs in the cluster |
| Average GPU Utilization | Average compute utilization of all GPUs in the cluster |
| Average GPU Memory Utilization | Average memory utilization of all GPUs in the cluster |
| GPU Power | Power consumption of all GPUs in the cluster |
| GPU Temperature | Temperature of all GPUs in the cluster |
| GPU Utilization Details | 24-hour usage details of all GPUs in the cluster (includes max, avg, current) |
| GPU Memory Usage Details | 24-hour memory usage details of all GPUs in the cluster (includes min, max, avg, current) |
| GPU Memory Bandwidth Utilization | For example, an Nvidia V100 GPU has a maximum memory bandwidth of 900 GB/sec. If the current memory bandwidth is 450 GB/sec, the utilization is 50% |

## Node Level

| Metric Name | Description |
| ----------- | ----------- |
| GPU Mode | Usage mode of GPUs on the node, including full-card mode, MIG mode, vGPU mode |
| Number of Physical GPUs | Total number of physical GPUs on the node |
| Number of Virtual GPUs | Number of vGPU devices created on the node |
| Number of MIG Instances | Number of MIG instances created on the node |
| GPU Memory Allocation Rate | Memory allocation rate of all GPUs on the node |
| Average GPU Utilization | Average compute utilization of all GPUs on the node |
| Average GPU Memory Utilization | Average memory utilization of all GPUs on the node |
| GPU Driver Version | Driver version information of GPUs on the node |
| GPU Utilization Details | 24-hour usage details of each GPU on the node (includes max, avg, current) |
| GPU Memory Usage Details | 24-hour memory usage details of each GPU on the node (includes min, max, avg, current) |

## Pod Level

| Category | Metric Name | Description |
| -------- | ----------- | ----------- |
| Application Overview GPU - Compute & Memory | Pod GPU Utilization | Compute utilization of the GPUs used by the current Pod |
| | Pod GPU Memory Utilization | Memory utilization of the GPUs used by the current Pod |
| | Pod GPU Memory Usage | Memory usage of the GPUs used by the current Pod |
| | Memory Allocation | Memory allocation of the GPUs used by the current Pod |
| | Pod GPU Memory Copy Ratio | Memory copy ratio of the GPUs used by the current Pod |
| GPU - Engine Overview | GPU Graphics Engine Activity Percentage | Percentage of time the Graphics or Compute engine is active during a monitoring cycle |
| | GPU Memory Bandwidth Utilization | Memory bandwidth utilization (Memory BW Utilization) indicates the fraction of cycles during which data is sent to or received from the device memory. This value represents the average over the interval, not an instantaneous value. A higher value indicates higher utilization of device memory.<br>A value of 1 (100%) indicates that a DRAM instruction is executed every cycle during the interval (in practice, a peak of about 0.8 (80%) is the maximum achievable).<br>A value of 0.2 (20%) indicates that 20% of the cycles during the interval are spent reading from or writing to device memory. |
| | Tensor Core Utilization | Percentage of time the Tensor Core pipeline is active during a monitoring cycle |
| | FP16 Engine Utilization | Percentage of time the FP16 pipeline is active during a monitoring cycle |
| | FP32 Engine Utilization | Percentage of time the FP32 pipeline is active during a monitoring cycle |
| | FP64 Engine Utilization | Percentage of time the FP64 pipeline is active during a monitoring cycle |
| | GPU Decode Utilization | Decode engine utilization of the GPU |
| | GPU Encode Utilization | Encode engine utilization of the GPU |
| GPU - Temperature & Power | GPU Temperature | Temperature of all GPUs in the cluster |
| | GPU Power | Power consumption of all GPUs in the cluster |
| | GPU Total Power Consumption | Total power consumption of the GPUs |
| GPU - Clock | GPU Memory Clock | Memory clock frequency |
| | GPU Application SM Clock | Application SM clock frequency |
| | GPU Application Memory Clock | Application memory clock frequency |
| | GPU Video Engine Clock | Video engine clock frequency |
| | GPU Throttle Reasons | Reasons for GPU throttling |
| GPU - Other Details | PCIe Transfer Rate | Data transfer rate of the GPU through the PCIe bus |
| | PCIe Receive Rate | Data receive rate of the GPU through the PCIe bus |
