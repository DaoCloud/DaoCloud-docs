# How to Use Iluvatar GPU in Applications

This section describes how to use Iluvatar virtual GPU on DCE 5.0.

## Prerequisites

- Deployed DCE 5.0 container management platform and it is running smoothly.
- The container management module has been integrated with a Kubernetes cluster or a Kubernetes cluster has been created, and the UI interface of the cluster can be accessed.
- The Iluvatar GPU driver has been installed on the current cluster. Refer to the [Iluvatar official documentation](https://support.iluvatar.com/#/login) for driver installation instructions, or contact the DaoCloud ecosystem team for enterprise-level support at peg-pem@daocloud.io.
- The GPU cards in the current cluster have not undergone any virtualization operations and not been occupied by other applications.

## Procedure

### Configuration via User Interface

1. Check if the GPU card in the cluster has been detected. Click `Cluster` -> `Cluster Settings` -> `Addon Plugins`, and check if the corresponding GPU type has been automatically enabled and detected.
   Currently, the cluster will automatically enable `GPU` and set the GPU type as `Iluvatar`.

   

2. Deploy a workload. Click `Cluster` -> `Workloads` and deploy a workload using the image. After selecting the type as `(Iluvatar)`, configure the GPU resources used by the application:
   
   **Physical Card Count (iluvatar.ai/vcuda-core):** Indicates the number of physical cards that the current pod needs to mount. The input value must be an integer and **less than or equal to** the number of cards on the host machine.
   
   **Memory Usage (iluvatar.ai/vcuda-memory):** Indicates the amount of GPU memory occupied by each card. The value is in MB, with a minimum value of 1 and a maximum value equal to the entire memory of the card.

   
   
   > If there are any issues with the configuration values, scheduling failures or resource allocation failures may occur.

### Configuration via YAML

To request GPU resources for a workload, add the `iluvatar.ai/vcuda-core: 1` and `iluvatar.ai/vcuda-memory: 200` to the requests and limits.
These parameters configure the application to use the physical card resources.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: full-iluvatar-gpu-demo
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      app: full-iluvatar-gpu-demo
  template:
    metadata:
      labels:
        app: full-iluvatar-gpu-demo
    spec:
      containers:
      - image: nginx:perl
        name: container-0
        resources:
            limits:
              cpu: 250m
              iluvatar.ai/vcuda-core: '1'
              iluvatar.ai/vcuda-memory: '200'
              memory: 512Mi
            requests:
                cpu: 250m
                memory: 512Mi
      imagePullSecrets:
      - name: default-secret
```
