# Using Ascend GPU in the Application

This section explains how to use Ascend GPU on the DCE 5.0 platform.

## Prerequisites

- The Ascend GPU driver has been installed on the current cluster.
- The GPU cards in the current cluster have not undergone any virtualization operations or been occupied by other applications.

## Configuration through the User Interface

1. Confirm whether the cluster has detected the GPU cards. Click `Cluster` -> `Cluster Settings` -> `Addon Plugins` and check if the corresponding GPU type has been automatically enabled and detected.
   Currently, the cluster will automatically enable `GPU`, and set the GPU type as `Ascend`.

   

2. Deploy the workload by clicking on `Cluster` -> `Workloads`. Deploy the workload using an image, and after selecting the type (Ascend), configure the number of physical cards that the application will use:

   **Number of Physical Cards (huawei.com/Ascend910)**: Indicates the number of physical cards that the current Pod needs to mount. The input value must be an integer and **less than or equal to** the number of cards on the host machine.
   
   

   > If there are issues with the above configuration, scheduling failures and resource allocation problems may occur.

## YAML Configuration

To apply for GPU resources in the workload, add the `huawei.com/Ascend910` parameter in the resource request and limit configuration to specify the physical card resources used by the application.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: full-Ascend-gpu-demo
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      app: full-Ascend-gpu-demo
  template:
    metadata:
      labels:
        app: full-Ascend-gpu-demo
    spec:
      containers:
      - image: nginx:perl
        name: container-0
        resources:
            limits:
              cpu: 250m
              huawei.com/Ascend910: '1'
              memory: 512Mi
            requests:
              cpu: 250m
              memory: 512Mi
      imagePullSecrets:
      - name: default-secret
```
