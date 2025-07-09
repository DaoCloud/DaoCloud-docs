# GPU Alerting Rules

This document describes how to set up GPU-related alerting rules on the DCE 5.0 platform.

## Prerequisites

* GPU devices are properly installed on the cluster nodes.
* The [gpu-operator component](../install_nvidia_driver_of_operator.md) is correctly installed in the cluster.
* If vGPU is used, the [Nvidia-vgpu component](../vgpu/vgpu_addon.md) must also be installed in the cluster, and servicemonitor enabled.
* The insight-agent component is properly installed in the cluster.

## Common GPU Metrics for Alerts

This section introduces commonly used GPU metrics for alerting, divided into two categories:

* Metrics at the GPU card level, mainly reflecting the operational status of a single GPU device.
* Metrics at the application level, mainly reflecting the Pod’s usage of the GPU.

### GPU Card Metrics

| Metric Name | Unit | Description |
| ----------- | ---- | ----------- |
| DCGM_FI_DEV_GPU_UTIL | % | GPU utilization |
| DCGM_FI_DEV_MEM_COPY_UTIL | % | Memory copy utilization |
| DCGM_FI_DEV_ENC_UTIL | % | Encoder utilization |
| DCGM_FI_DEV_DEC_UTIL | % | Decoder utilization |
| DCGM_FI_DEV_FB_FREE | MB | Amount of free GPU memory |
| DCGM_FI_DEV_FB_USED | MB | Amount of used GPU memory |
| DCGM_FI_DEV_GPU_TEMP | °C | Current GPU temperature |
| DCGM_FI_DEV_POWER_USAGE | W | Device power usage |
| DCGM_FI_DEV_XID_ERRORS | - | The last XID error code occurred within a time window. XID provides information on GPU hardware, NVIDIA software, or application error types, locations, and codes. More details on [XID info](./gpu-metrics.md#_2) |

### Application-Level Metrics

| Metric Name | Unit | Description |
| ----------- | ---- | ----------- |
| kpanda_gpu_pod_utilization | % | GPU utilization by the Pod |
| kpanda_gpu_mem_pod_usage | MB | GPU memory usage by the Pod |
| kpanda_gpu_mem_pod_utilization | % | GPU memory utilization by the Pod |

## Setting Alert Rules

Here is how to set GPU alert rules. Using GPU utilization as an example, users should choose metrics and write PromQL queries based on their actual business scenarios.

**Goal:** Trigger an alert if the GPU utilization stays above 80% continuously for 5 seconds.

1. On the observability page, click **Alerting** -> **Alert Policies** -> **Create Alert Policy**.

    ![Create Alert Rule](../../images/create-gpu-alarm.png)

2. Fill in the basic information.

    ![Fill Alert Rule](../../images/gpu-alarm-details.png)

3. Add the alert rule.

    ![Fill Alert Rule 2](../../images/gpu-alarm-details2.png)

4. Choose the notification method.

    ![Notification Method](../../images/gpu-alarm-message.png)

5. After setup, if a GPU maintains utilization above 80% for 5 seconds, you will receive an alert message like this:

    ![Alert Message](../../images/gpu-alarm-message2.png)
