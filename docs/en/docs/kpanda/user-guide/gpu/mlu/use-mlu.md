# Using Cambricon GPUs

This document describes how to use Cambricon GPUs in DCE 5.0.

## Prerequisites

* DCE 5.0 container management platform has been [deployed](../../../../install/index.md) and is running properly.
* The container management module has either [connected to a Kubernetes cluster](../../clusters/integrate-cluster.md) or [created a Kubernetes cluster](../../clusters/create-cluster.md), and the UI interface of the cluster is accessible.
* The current cluster has installed the Cambricon firmware, drivers, and DevicePlugin component. For installation details, please refer to the official documentation:

    * [Driver and Firmware Installation](https://www.cambricon.com/docs/sdk_1.15.0/driver_5.10.22/user_guide/index.html)
    * [DevicePlugin Installation](https://github.com/Cambricon/cambricon-k8s-device-plugin/blob/master/device-plugin/README.md)

> **Note:** When installing the DevicePlugin, make sure to disable the `--enable-device-type` parameter; otherwise, DCE 5.0 will not be able to recognize Cambricon GPUs correctly.

## Cambricon GPU Modes

Cambricon GPUs support the following modes:

* **Full GPU mode**: Registers the entire Cambricon GPU to the cluster for use as a whole.
* **Share mode**: Allows a single Cambricon GPU to be shared among multiple Pods. The number of shareable containers can be configured using the `virtualization-num` parameter.
* **Dynamic SMLU mode**: Provides fine-grained resource allocation, allowing control over the amount of GPU memory and compute assigned to each container.
* **MIM mode**: Splits a Cambricon GPU into multiple fixed-spec virtual GPUs for use.

## Using Cambricon in DCE 5.0

Taking **Dynamic SMLU mode** as an example:

1. After correctly installing the DevicePlugin and related components, go to **Cluster** -> **Cluster Maintenance** -> **Cluster Settings** -> **Addon Plugins** to check whether the corresponding GPU type has been automatically enabled and detected.

    ![MLU Type](../images/mlu1.PNG)

2. Go to the Node Management page to verify whether the node has correctly recognized the GPU type.

    ![Node List](../images/mlu2.png)

3. Deploy workloads. Navigate to **Cluster** -> **Workloads**, and deploy workloads using an image. After selecting the type (e.g., **MLU VGPU**), configure the GPU resources required by the app:

    * **GPU Compute Power (`cambricon.com/mlu.smlu.vcore`)**: Indicates the percentage of core compute the Pod needs.
    * **GPU Memory (`cambricon.com/mlu.smlu.vmemory`)**: Indicates the amount of GPU memory the Pod needs, in MB.

    ![Using MLU](../images/mlu3.png)

## YAML Configuration Example

Sample YAML file:

```yaml
apiVersion: v1  
kind: Pod  
metadata:  
  name: pod1  
spec:  
  restartPolicy: OnFailure  
  containers:  
    - image: ubuntu:16.04  
      name: pod1-ctr  
      command: ["sleep"]  
      args: ["100000"]  
      resources:  
        limits:  
          cambricon.com/mlu: "1" # use this when device type is not enabled, else delete this line.  
          #cambricon.com/mlu: "1" #uncomment to use when device type is enabled  
          #cambricon.com/mlu.share: "1" #uncomment to use device with env-share mode  
          #cambricon.com/mlu.mim-2m.8gb: "1" #uncomment to use device with mim mode  
          #cambricon.com/mlu.smlu.vcore: "100" #uncomment to use device with smlu mode  
          #cambricon.com/mlu.smlu.vmemory: "1024" #uncomment to use device with smlu mode
```
