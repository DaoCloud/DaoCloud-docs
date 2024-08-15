# Using MIG GPU Resources

This section explains how applications can use MIG GPU resources.

## Prerequisites

- DCE 5.0 container management platform is deployed and running successfully.
- The container management module is integrated with a Kubernetes cluster or a Kubernetes cluster is created, and the UI interface of the cluster can be accessed.
- NVIDIA DevicePlugin and MIG capabilities are enabled. Refer to [Offline installation of GPU Operator](../install_nvidia_driver_of_operator.md) for details.
- The nodes in the cluster have GPUs of the corresponding models.

## Using MIG GPU through the UI

1. Confirm if the cluster has recognized the GPU card type.

    Go to __Cluster Details__ -> __Nodes__ and check if it has been correctly recognized as MIG.

    

2. When deploying an application using an image, you can select and use NVIDIA MIG resources.

- Example of MIG Single Mode (used in the same way as a full GPU card):

    !!! note
    
        The MIG single policy allows users to request and use GPU resources in the same way as a full GPU card (`nvidia.com/gpu`). The difference is that these resources can be a portion of the GPU (MIG device) rather than the entire GPU. Learn more from the [GPU MIG Mode Design](https://docs.google.com/document/d/1bshSIcWNYRZGfywgwRHa07C0qRyOYKxWYxClbeJM-WM/edit#heading=h.jklusl667vn2).

- MIG Mixed Mode

## Using MIG through YAML Configuration

__MIG Single__ mode:

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
              nvidia.com/gpu: 2 # (1)!
          imagePullPolicy: Always
      restartPolicy: Always
```

1. Number of MIG GPUs to request

__MIG  Mixed__ mode:

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
              nvidia.com/mig-4g.20gb: 1 # (1)!
          imagePullPolicy: Always
      restartPolicy: Always
```

1. Expose MIG device through nvidia.com/mig-g.gb resource type

After entering the container, you can check if only one MIG device is being used:
