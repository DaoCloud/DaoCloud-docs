# GPU Monitoring Metrics

This page lists some commonly used GPU monitoring metrics.

## Cluster Dimension

| Name | Description | Metric | Table Style |
| --- | --- | --- | --- |
| Total GPU | The total number of GPU cards in the cluster, including MIG instances that are counted as individual physical cards | __count(DCGM_FI_DEV_COUNT{cluster="$cluster",node=~"${node}"})__ | Numeric |
| GPU Avg Utilization | The average utilization of all GPU cards in the cluster | __avg(max_over_time(DCGM_FI_DEV_GPU_UTIL{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}[29s]))__ | Numeric |
| GPU Avg Utilization (Only MIG Enabled) | The average utilization of all GPU cards in the cluster when MIG feature is enabled | __avg(max_over_time(DCGM_FI_DEV_GPU_UTIL{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}[29s]))__ | Numeric |
| GPU Avg Memory Utilization | The average memory utilization of all GPU cards in the cluster | __sum(max_over_time(DCGM_FI_DEV_FB_USED{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}[29s])) / sum(max_over_time(DCGM_FI_DEV_FB_USED{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"} + DCGM_FI_DEV_FB_FREE{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"} [29s])) * 100__ | Numeric |
| GPU Power Usage | The power usage of all GPU cards in the cluster | __DCGM_FI_DEV_POWER_USAGE{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}__ | Bar Chart |
| GPU Temperature | The temperature of all GPU cards in the cluster | __DCGM_FI_DEV_GPU_TEMP{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}__ | Bar Chart |
| GPU Utilization Details | Utilization details of all GPU cards in the cluster within 24 hours (including max, avg, current) | __DCGM_FI_DEV_GPU_UTIL{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}__ | Line Chart |
| GPU Utilization Details (Only MIG Enabled) | Utilization details of all GPU cards in the cluster within 24 hours when MIG feature is enabled (including max, avg, current) | __DCGM_FI_PROF_GR_ENGINE_ACTIVE{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"} * 100__ | Line Chart |
| GPU Memory Used Details | Memory usage details of all GPU cards in the cluster within 24 hours (including min, max, avg, current) | __DCGM_FI_DEV_FB_USED{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}__ | Line Chart |
| GPU Memory Copy Utilization | The memory copy utilization of all GPU cards in the cluster | __DCGM_FI_DEV_MEM_COPY_UTIL{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}__ | Line Chart |

## Node Dimension

| Name | Description | Metric | Table Style |
| --- | --- | --- | --- |
| Total GPU | The total number of GPU cards on a specific node in the cluster, including MIG instances that are counted as individual physical cards | __count(DCGM_FI_DEV_COUNT{cluster="$cluster",node=~"${node}"})__ | Numeric |
| GPU Mode | The mode of GPU cards on a specific node, including Whole GPU mode, MIG mode, vGPU mode | __topk(1,DCGM_FI_DEV_MIG_MODE{cluster="$cluster",node=~"$node"})__ | Text |
| GPU Avg Utilization | The average utilization of all GPU cards on a specific node in the cluster | __avg(max_over_time(DCGM_FI_DEV_GPU_UTIL{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}[29s]))__ | Numeric |
| GPU Avg Utilization (Only MIG Enabled) | The average utilization of all GPU cards on a specific node in the cluster when MIG feature is enabled | __avg(max_over_time(DCGM_FI_PROF_GR_ENGINE_ACTIVE{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}[29s] * 100))__ | Numeric |
| GPU Avg Memory Utilization | The average memory utilization of all GPU cards on a specific node in the cluster | __sum(max_over_time(DCGM_FI_DEV_FB_USED{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}[29s])) / sum(max_over_time(DCGM_FI_DEV_FB_USED{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"} + DCGM_FI_DEV_FB_FREE{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"} [29s])) * 100__ | Numeric |
| GPU Driver Version | The version information of GPU card drivers on a specific node | __DCGM_FI_DEV_MIG_MODE{cluster="$cluster",node=~"$node",gpu=~"$gpu"} {{modelName}}__ | Text |
| GPU Specifications | The specifications of GPU cards on a specific node | __DCGM_FI_DEV_MIG_MODE{cluster="$cluster",node=~"$node",gpu=~"$gpu"}__ | Table |
| GPU Utilization Details | Utilization details of all GPU cards on a specific node in the cluster within 24 hours (including max, avg, current) | __DCGM_FI_DEV_GPU_UTIL{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}__ | Line Chart |
| GPU Utilization Details (Only MIG Enabled) | Utilization details of all GPU cards on a specific node in the cluster within 24 hours when MIG feature is enabled (including max, avg, current) | __DCGM_FI_PROF_GR_ENGINE_ACTIVE{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"} * 100__ | Line Chart |
| GPU Memory Used Details | Memory usage details of all GPU cards on a specific node in the cluster within 24 hours (including min, max, avg, current) | __DCGM_FI_DEV_FB_USED{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}__ | Line Chart |

## Workload Dimension

| Dimension | Name | Description | Metric | Chart Style |
| --- | --- | --- | --- | --- |
| Application Overview | Pod GPU Utilization | The ratio of GPU cards currently used by the Pod | __DCGM_FI_DEV_GPU_UTIL{cluster="$cluster",exported_namespace="$namespace",exported_pod="$pod"}__ | Line chart |
| Application Overview | Pod GPU Utilization (Only MIG Enabled) | The ratio of GPU cards currently used by the Pod when MIG feature is enabled | __DCGM_FI_PROF_GR_ENGINE_ACTIVE{cluster="$cluster",exported_namespace="$namespace",exported_pod="$pod"} * 100__ | Line chart |
| Application Overview | Pod GPU Utilization (vGPU) | The ratio of GPU cards currently used by the Pod when vGPU feature is enabled | __vGPUCorePercentage{cluster="$cluster",exported_namespace="$namespace",podname="$pod"}__ | Line chart |
| Application Overview | Pod GPU Memory Utilization | The ratio of GPU memory currently used by the Pod | __DCGM_FI_DEV_FB_USED{cluster="$cluster",exported_namespace="$namespace",exported_pod="$pod"}__ | Line chart |
| Application Overview | Pod GPU Memory Utilization (vGPU) | The ratio of GPU memory currently used by the Pod in vGPU mode | __vGPUMemoryPercentage{cluster="$cluster",exported_namespace="$namespace",podname="$pod"}__ | Line chart |
| Application Overview | Pod Memory Usage | The memory usage of GPU cards currently used by the Pod | __DCGM_FI_DEV_FB_USED{cluster="$cluster",exported_namespace="$namespace",exported_pod="$pod"}__ | Line chart |
| Application Overview | Pod Memory Usage (vGPU) | The memory usage of GPU cards currently used by the Pod in vGPU mode | __sum(GPUDeviceMemoryLimit{cluster="$cluster"}) * vGPUMemoryPercentage{cluster="$cluster",exported_namespace="$namespace",podname="$pod"}__ | Line chart |
| Application Overview | Pod GPU Memory Copy Utilization | The ratio of GPU memory copy currently used by the Pod | __DCGM_FI_DEV_MEM_COPY_UTIL{cluster="$cluster",exported_namespace="$namespace",exported_pod="$pod"}__ | Line chart |
| Application Overview | Pod Decode Utilization | The ratio of GPU decode engine currently used by the Pod | __DCGM_FI_DEV_DEC_UTIL{cluster="$cluster",exported_namespace="$namespace",exported_pod="$pod"}__ | - |
| Application Overview | Pod Encode Utilization | The ratio of GPU encode engine currently used by the Pod | __DCGM_FI_DEV_ENC_UTIL{cluster="$cluster",exported_namespace="$namespace",exported_pod="$pod"}__ | - |
| GPU Card - Compute & Memory | GPU Utilization Details | Usage details (max, avg, current) of GPU cards associated with the Pod in the last 24 hours | __DCGM_FI_DEV_GPU_UTIL{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"}__ | Line chart |
| GPU Card - Compute & Memory | GPU Utilization Details (Only MIG Enabled) | Usage details (max, avg, current) of GPU cards associated with the Pod when MIG feature is enabled in the last 24 hours | __DCGM_FI_PROF_GR_ENGINE_ACTIVE{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 100__ | Line chart |
| GPU Card - Compute & Memory | GPU Memory Used Details | Memory usage details (min, max, avg, current) of GPU cards associated with the Pod in the last 24 hours | __DCGM_FI_DEV_FB_USED{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"}__ | Time-based line chart |
| GPU Card - Compute & Memory | GPU Memory Copy Utilization | Memory copy utilization of GPU cards associated with the Pod | __DCGM_FI_DEV_MEM_COPY_UTIL{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"}__ | Line chart |
| GPU Card - Engine Overview | GPU Graphics Engine Active | The ratio of time the Graphics or Compute engine is active within a monitoring period | __DCGM_FI_PROF_GR_ENGINE_ACTIVE{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 100__ | Line chart |
| GPU Card - Engine Overview | GPU DRAM Active | Memory bandwidth utilization | __DCGM_FI_PROF_DRAM_ACTIVE{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 100__ | Line chart |
| GPU Card - Engine Overview | GPU Tensor Core Engine Active | The ratio of time the Tensor Core pipeline is active within a monitoring period | __DCGM_FI_PROF_PIPE_TENSOR_ACTIVE{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 100__ | Line chart |
| GPU Card - Engine Overview | GPU FP16 Engine Active | The ratio of time the FP16 pipeline is active within a monitoring period | __DCGM_FI_PROF_PIPE_FP16_ACTIVE{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 100__ | Line chart |
| GPU Card - Engine Overview | GPU FP32 Engine Active | The ratio of time the FP32 pipeline is active within a monitoring period | __DCGM_FI_PROF_PIPE_FP32_ACTIVE{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 100__ | Line chart |
| GPU Card - Engine Overview | GPU FP64 Engine Active | The ratio of time the FP64 pipeline is active within a monitoring period | __DCGM_FI_PROF_PIPE_FP64_ACTIVE{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 100__ | Line chart |
| GPU Card - Engine Overview | GPU Decode Utilization | The ratio of GPU decode engine utilization | __DCGM_FI_DEV_DEC_UTIL{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"}__ | Line chart |
| GPU Card - Engine Overview | GPU Encode Utilization | The ratio of GPU encode engine utilization | __DCGM_FI_DEV_ENC_UTIL{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"}__ | Line chart |
| GPU Card - Temperature & Power | GPU Temperature | Temperature of all GPU cards in the cluster | __DCGM_FI_DEV_GPU_TEMP{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"}__ | Bar chart |
| GPU Card - Temperature & Power | GPU Power Usage | Power usage of all GPU cards in the cluster | __DCGM_FI_DEV_POWER_USAGE{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"}__ | Bar chart |
| GPU Card - Temperature & Power | GPU Total Energy Consumption | Total energy consumption of GPU cards | __sum(DCGM_FI_DEV_POWER_USAGE{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"})__ | Line chart |
| GPU Card - Temperature & Power | GPU Memory Clock | Memory clock frequency | __DCGM_FI_DEV_MEM_CLOCK{cluster="$cluster",UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 1000 * 1000__ | Line chart |
| GPU Card - Temperature & Power | GPU APP SM Clock | Application SM clock frequency | __DCGM_FI_DEV_APP_SM_CLOCK{cluster="$cluster",UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 1000 * 1000__ | Line chart |
| GPU Card - Temperature & Power Consumption | GPU Card Application Memory Frequency | GPU APP Memory Clock | Application Memory Frequency | __DCGM_FI_DEV_APP_MEM_CLOCK{cluster="$cluster",UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 1000 * 1000__ | Line Chart |
| GPU Card - Temperature & Power Consumption | GPU Card Video Engine Frequency | GPU Video Clock | Video Engine Frequency | __DCGM_FI_DEV_VIDEO_CLOCK{cluster="$cluster",UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 1000 * 1000__ | Line Chart |
| GPU Card - Temperature & Power Consumption | GPU Card Throttling Reasons | GPU-Clock Throttle Reasons | Throttling Reasons | __DCGM_FI_DEV_CLOCK_THROTTLE_REASONS{cluster="$cluster",UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} __ | Text |
| GPU Card - Other Details | PCIe Transfer Rate | PCIE TX BYTES | Data transfer rate of the node GPU card via PCIe bus. | __rate(DCGM_FI_PROF_PCIE_RX_BYTES{cluster="$cluster",UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"}[1m])__ | Line Chart |
| GPU Card - Other Details | PCIe Receive Rate | PCIE RX BYTES | Data receive rate of the node GPU card via PCIe bus. | __rate(DCGM_FI_PROF_PCIE_TX_BYTES{cluster="$cluster",UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"}[1m])__ | Line Chart |
