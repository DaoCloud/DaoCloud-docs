---
hide:
  - toc
---

# GPU 监控指标

本页列出一些常用的 GPU 监控指标。

## 集群维度

| 指标名称 | 英文  | 描述  | 指标  | 表格样式 |
| --- | --- | --- | --- | --- |
| GPU 卡数 | Total GPU | 集群下所有的 GPU 卡数量，切分的 MIG 实例也将会被统计成的单张的物理卡 | `count(DCGM_FI_DEV_COUNT{cluster="$cluster",node=~"${node}"})` | 数值  |
| GPU 平均使用率（整卡） | GPU Avg Utilization | 集群下所有 GPU 卡的平均使用率 | `avg(max_over_time(DCGM_FI_DEV_GPU_UTIL{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}[29s]))` | 数值  |
| GPU 平均使用率（MIG） | GPU Avg Utilization  <br>（Only MIG Enably） | 当启用 MIG 特性后，集群下所有 GPU 卡的平均使用率 | `avg(max_over_time(DCGM_FI_DEV_GPU_UTIL{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}[29s]))` | 数值  |
| GPU 卡平均显存使用率 | GPU Avg Memory Utilization | 集群下所有 GPU 卡的平均显存使用率 | `sum(max_over_time(DCGM_FI_DEV_FB_USED{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}[29s])) / sum(max_over_time(DCGM_FI_DEV_FB_USED{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"} + DCGM_FI_DEV_FB_FREE{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"} [29s])) * 100` | 数值  |
| GPU 卡功率 | GPU Power Usage | 集群下所有 GPU 卡的功率 | `DCGM_FI_DEV_POWER_USAGE{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}` | 柱状图|
| GPU 卡温度 | GPU Temperature | 集群下所有 GPU 卡的温度 | `DCGM_FI_DEV_GPU_TEMP{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}` | 柱状图 |
| GPU 使用率细节（整卡） | GPU Utilization Details | 24 小时内，集群下所有 GPU 卡的使用率细节（包含 max、avg、current） | `DCGM_FI_DEV_GPU_UTIL{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}` | 折线图 |
| GPU使用率细节（mig） | GPU Utilization Details（Only MIG Enably） | 24 小时内，当启用 MIG 特性后，集群下所有 GPU 卡的使用率细节。  <br>（包含 max、avg、current） | `DCGM_FI_PROF_GR_ENGINE_ACTIVE{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"} * 100` | 折线图 |
| GPU 显存使用量 | GPU Memory Used Details | 24 小时内，集群下所有 GPU 卡的显存使用量细节  <br>（包含min  <br>、max、avg、current） | `DCGM_FI_DEV_FB_USED{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}` | 折线图 |
| GPU 显存复制使用率 | GPU Memory Copy Utilization | 集群下所有 GPU 卡的显存复制使用率 | `DCGM_FI_DEV_MEM_COPY_UTIL{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}` | 折线图 |

## 节点维度

| 指标名称 | 英文  | 描述  | 指标  | 表格样式 |
| --- | --- | --- | --- | --- |
| GPU 卡数 | Total GPU | 节点上所有的 GPU 卡数量，切分的 MIG 实例也将会被统计成的单张的物理卡 | `count(DCGM_FI_DEV_COUNT{cluster="$cluster",node=~"${node}"})` | 数值  |
| GPU 模式 | GPU Mode | 节点上 GPU 卡的模式使用模式，包含 整卡模式、MIG 模式、vGPU 模式 | `topk(1,DCGM_FI_DEV_MIG_MODE{cluster="$cluster",node=~"$node"})` | 文本  |
| GPU 平均使用率（整卡） | GPU Avg Utilization | 节点上所有 GPU 卡的平均使用率 | `avg(max_over_time(DCGM_FI_DEV_GPU_UTIL{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}[29s]))` | 数值  |
| GPU 平均使用率（MIG） | GPU Avg Utilization  <br>（Only MIG Enably） | 当启用 MIG 特性后，节点上所有 GPU 卡的平均使用率 | `avg(max_over_time(DCGM_FI_PROF_GR_ENGINE_ACTIVE{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}[29s] * 100))` | 数值  |
| GPU 卡平均显存使用率 | GPU Avg Memory Utilization | 节点上所有 GPU 卡的平均显存使用率 | `sum(max_over_time(DCGM_FI_DEV_FB_USED{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}[29s])) / sum(max_over_time(DCGM_FI_DEV_FB_USED{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"} + DCGM_FI_DEV_FB_FREE{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"} [29s])) * 100` | 数值  |
| GPU 驱动版本 | GPU Driver Version | 节点上 GPU 卡驱动的版本信息 | `DCGM_FI_DEV_MIG_MODE{cluster="$cluster",node=~"$node",gpu=~"$gpu"} {{modelName}}` | 文本  |
| GPU 卡型号/规格 | GPU Specifications | 节点上 GPU 卡规格信息 | `DCGM_FI_DEV_MIG_MODE{cluster="$cluster",node=~"$node",gpu=~"$gpu"}` | 表格  |
| GPU 使用率细节（整卡） | GPU Utilization Details | 24 小时内，节点上所有 GPU 卡的使用率细节（包含 max、avg、current） | `DCGM_FI_DEV_GPU_UTIL{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}` | 折线图 |
| GPU 使用率细节（MIG） | GPU Utilization Details（Only MIG Enably） | 24 小时内，当启用 MIG 特性后，节点上所有 GPU 卡的使用率细节。  <br>（包含 max、avg、current） | `DCGM_FI_PROF_GR_ENGINE_ACTIVE{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"} * 100` | 折线图 |
| GPU 显存使用量 | GPU Memory Used Details | 24 小时内，节点上所有 GPU 卡的显存使用量细节  <br>（包含min  <br>、max、avg、current） | `DCGM_FI_DEV_FB_USED{cluster="$cluster",node=~"${node}", gpu=~"${gpu}"}` | 折线图 |

## 工作负载维度

| 维度  | 指标名称 | 英文  | 描述  | 指标  | 表格样式 |
| --- | --- | --- | --- | --- | --- |
| 应用概览 | Pod GPU 使用率（整卡） | Pod GPU Utilization | 当前 Pod 所使用到的 GPU 卡的比率 | `DCGM_FI_DEV_GPU_UTIL{cluster="$cluster",exported_namespace="$namespace",exported_pod="$pod"}` | 折线图 |
| 应用概览 | Pod GPU 使用率（MIG） | Pod GPU Utilization  <br>（Only MIG Enably） | 当启用 MIG 特性后，当前 Pod 所使用到的 GPU 卡的比率 | `DCGM_FI_PROF_GR_ENGINE_ACTIVE{cluster="$cluster",exported_namespace="$namespace",exported_pod="$pod"} * 100` | 折线图 |
| 应用概览 | Pod GPU 使用率（vGPU） | Pod GPU Utilization  <br>（vGPU） | 当启用 vGPU 特性后，当前 Pod 所使用到的 GPU 卡的比率 | `vGPUCorePercentage{cluster="$cluster",exported_namespace="$namespace",podname="$pod"}` | 折线图 |
| 应用概览 | Pod GPU 显存使用率 | Pod GPU Memory Utilization | 当前 Pod 所使用到的 GPU 卡的显存比率 | `DCGM_FI_DEV_FB_USED{cluster="$cluster",exported_namespace="$namespace",exported_pod="$pod"}` | 折线图 |
| 应用概览 | Pod GPU 显存使用率（vGPU） | Pod GPU Memory Utilization（vGPU） | 当前 Pod 所使用到的 GPU 卡的显存比率(vGPU 模式) | `vGPUMemoryPercentage{cluster="$cluster",exported_namespace="$namespace",podname="$pod"}` | 折线图 |
| 应用概览 | Pod 显存使用量 | Pod 显存使用量 | 当前 Pod 所使用到的 GPU 卡的显存量 | `DCGM_FI_DEV_FB_USED{cluster="$cluster",exported_namespace="$namespace",exported_pod="$pod"}` | 折线图 |
| 应用概览 | Pod 显存使用量（vGPU） | Pod 显存使用量  <br>（vGPU） | 当前 Pod 所使用到的 GPU 卡的显存比率(vGPU 模式) | `sum(GPUDeviceMemoryLimit{cluster="$cluster"}) * vGPUMemoryPercentage{cluster="$cluster",exported_namespace="$namespace",podname="$pod"}` | 折线图 |
| 应用概览 | Pod GPU 显存复制使用率 | Pod GPU Memory Copy Utilization | 当前 Pod 所使用到的 GPU 卡的显存显存复制比率 | `DCGM_FI_DEV_MEM_COPY_UTIL{cluster="$cluster",exported_namespace="$namespace",exported_pod="$pod"}` | 折线  |
| 应用概览 | Pod 解码使用率 | Pod Decode Utilization | 当前 Pod 所使用到的 GPU 卡解码引擎比率 | `DCGM_FI_DEV_DEC_UTIL{cluster="$cluster",exported_namespace="$namespace",exported_pod="$pod"}` | -   |
| 应用概览 | Pod 编码使用率 | Pod Encode Utilization | 当前 Pod 所使用到的 GPU 卡编码引擎比率 | `DCGM_FI_DEV_ENC_UTIL{cluster="$cluster",exported_namespace="$namespace",exported_pod="$pod"}` | -   |
| GPU 卡-算力&显存 | GPU 使用率细节（整卡） | GPU Utilization Details | 24 小时内，Pod 关联的 GPU 卡的使用率细节（包含 max、avg、current） | `DCGM_FI_DEV_GPU_UTIL{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"}` | 折线图 |
| GPU 卡-算力&显存 | GPU使用率细节（MIG） | GPU Utilization Details（Only MIG Enably） | 24 小时内，当启用 MIG 特性后，Pod 关联的 GPU 卡的使用率细节。  <br>（包含 max、avg、current） | `DCGM_FI_PROF_GR_ENGINE_ACTIVE{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 100` | 折线图 |
| GPU 卡-算力&显存 | GPU 显存使用量 | GPU Memory Used Details | 24 小时内，Pod 关联的 GPU 卡的显存使用量细节  <br>（包含min  <br>、max、avg、current） | `DCGM_FI_DEV_FB_USED{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"}` | 时间维度折线图 |
| GPU 卡-算力&显存 | GPU 显存复制使用率 | GPU Memory Copy Utilization | Pod 关联的 GPU 卡的显存复制使用率 | `DCGM_FI_DEV_MEM_COPY_UTIL{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"}` | 折线图 |
| GPU 卡-引擎概览 | GPU 图形引擎活动百分比 | GPU Graphics Engine Active | 表示在一个监控周期内，Graphics 或 Compute 引擎处于 Active 的时间占总的时间的比例。 | `DCGM_FI_PROF_GR_ENGINE_ACTIVE{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 100` | 折线图 |
| GPU 卡-引擎概览 | GPU DRAM 活动百分比 | GPU DRAM Active | 表示内存带宽利用率（Memory BW Utilization） | `DCGM_FI_PROF_DRAM_ACTIVE{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 100` | 折线图 |
| GPU 卡-引擎概览 | Tensor 核心引擎使用率 | GPU Tensor Core Engine Active | 表示在一个监控周期内，Tensor Core管道（Pipe）处于Active时间占总时间的比例。 | `DCGM_FI_PROF_PIPE_TENSOR_ACTIVE{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 100` | 折线图 |
| GPU 卡-引擎概览 | FP16 引擎使用率 | GPU FP16 Engine Active | 表示在一个监控周期内，FP16 管道处于 Active 的时间占总的时间的比例。 | `DCGM_FI_PROF_PIPE_FP16_ACTIVE{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 100` | 折线图 |
| GPU 卡-引擎概览 | FP32 引擎使用率 | GPU FP32 Engine Active | 表示在一个监控周期内，FP32 管道处于 Active 的时间占总的时间的比例。 | `DCGM_FI_PROF_PIPE_FP32_ACTIVE{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 100` | 折线图 |
| GPU 卡-引擎概览 | FP32 引擎使用率 | GPU FP64 Engine Active | 表示在一个监控周期内，FP64 管道处于 Active 的时间占总的时间的比例。 | `DCGM_FI_PROF_PIPE_FP64_ACTIVE{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 100` | 折线图 |
| GPU 卡-引擎概览 | GPU 解码使用率 | GPU Decode Utilization | GPU 卡解码引擎比率 | `DCGM_FI_DEV_DEC_UTIL{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"}` | 折线图 |
| GPU 卡-引擎概览 | GPU 编码使用率 | GPU Encode Utilization | GPU 卡编码引擎比率 | `DCGM_FI_DEV_ENC_UTIL{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"}` | 折线图 |
| GPU 卡-温度&功耗 | GPU 卡温度 | GPU Temperature | 集群下所有 GPU 卡的温度 | `DCGM_FI_DEV_GPU_TEMP{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"}` | 柱状图 |
| GPU 卡-温度&功耗 | GPU 卡功率 | GPU Power Usage | 集群下所有 GPU 卡的功率 | `DCGM_FI_DEV_POWER_USAGE{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"}` | 柱状图 |
| GPU 卡-温度&功耗 | GPU 卡-总耗能 | GPU Total Energy Consumption | GPU 卡总共消耗的能量 | `sum(DCGM_FI_DEV_POWER_USAGE{cluster="$cluster", UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"})` | 折线图 |
| GPU 卡-温度&功耗 | GPU 卡内存频率 | GPU Memory Clock | 内存频率 | `DCGM_FI_DEV_MEM_CLOCK{cluster="$cluster",UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 1000 * 1000` | 折线图 |
| GPU 卡-温度&功耗 | GPU 卡应用SM 时钟频率 | GPU APP SM Clock | 应用的SM 时钟频率 | `DCGM_FI_DEV_APP_SM_CLOCK{cluster="$cluster",UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 1000 * 1000` | 折线图 |
| GPU 卡-温度&功耗 | GPU 卡应用内存频率 | GPU APP Memory Clock | 应用内存频率 | `DCGM_FI_DEV_APP_MEM_CLOCK{cluster="$cluster",UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 1000 * 1000` | 折线图 |
| GPU 卡-温度&功耗 | GPU 卡视频引擎频率 | GPU Video Clock | 视频引擎频率。 | `DCGM_FI_DEV_VIDEO_CLOCK{cluster="$cluster",UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} * 1000 * 1000` | 折线图 |
| GPU 卡-温度&功耗 | GPU 卡降频原因 | GPU-Clock Throttle Reasons | 降频原因 | `DCGM_FI_DEV_CLOCK_THROTTLE_REASONS{cluster="$cluster",UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"} ` | 文本  |
| GPU 卡-Other details | PCLe 传输速率 | PCIE TX BYTES | 节点 GPU 卡通过 PCIe 总线传输的数据速率。 | `rate(DCGM_FI_PROF_PCIE_RX_BYTES{cluster="$cluster",UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"}[1m])` | 折线图 |
| GPU 卡-Other details | PCLe 接收速率 | PCIE RX BYTES | 节点 GPU 卡通过 PCIe 总线接收的数据速率。 | `rate(DCGM_FI_PROF_PCIE_TX_BYTES{cluster="$cluster",UUID="${gpu}",GPU_I_ID=~"${gpu_i_id}"}[1m])` | 折线图 |
