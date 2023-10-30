# Using MIG GPU Resources

This section explains how applications can use MIG GPU resources.

## Prerequisites

- DCE 5.0 container management platform is deployed and running successfully.
- The container management module is integrated with a Kubernetes cluster or a Kubernetes cluster is created, and the UI interface of the cluster can be accessed.
- NVIDIA DevicePlugin and MIG capabilities are enabled. Refer to [Offline installation of GPU Operator](../install_nvidia_driver_of_operator.md) for details.
- The nodes in the cluster have GPUs of the corresponding models.

## Using MIG GPU through the UI

1. Confirm if the cluster has recognized the GPU card type.

    Go to `Cluster Details` -> `Cluster Settings` -> `Addon Configuration` and check if it has been correctly recognized. The automatic recognition frequency is set to `10 minutes`.

    

2. When deploying an application using an image, you can select and use NVIDIA MIG resources.

    

## Using MIG through YAML Configuration

**`MIG Single` mode:**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mig-demo
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mig-demo
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: mig-demo
    spec:
      containers:
        - name: mig-demo1
          image: chrstnhntschl/gpu_burn
          resources:
            limits:
            nvidia.com/gpu: 2 # Number of MIG GPUs to request
          imagePullPolicy: Always
      restartPolicy: Always
```

**`MIG  Mixed` mode:**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mig-demo
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      app: mig-demo
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: mig-demo
    spec:
      containers:
        - name: mig-demo1
          image: chrstnhntschl/gpu_burn
          resources:
            limits:
            nvidia.com/mig-4g.20gb: 1 # Expose MIG device through nvidia.com/mig-g.gb resource type
          imagePullPolicy: Always
      restartPolicy: Always
```

After entering the container, you can check if only one MIG device is being used:


