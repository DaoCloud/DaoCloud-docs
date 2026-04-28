# Edge Cluster Deployment and Management Practice

For resource-constrained edge or IoT scenarios, Kubernetes cannot well meet resource requirements. Therefore, a lightweight Kubernetes solution is needed that can not only implement container management and orchestration capabilities but also reserve more resource space for business applications. This article introduces the deployment and full lifecycle management practice of edge cluster k3s.

## Node Planning

**Architecture**

- x86_64
- armhf
- arm64/aarch64

**Operating System**

- Can work on most modern Linux systems

**CPU/Memory**

- Single-node K3s cluster

    |             | Min CPU | Recommended CPU | Min Memory | Recommended Memory |
    | :---------- | :------- | -------- | -------- | -------- |
    | K3s cluster | 1 core   | 2 cores  | 1.5 GB   | 2 GB     |

- Multi-node K3s cluster

    |            | Min CPU | Recommended CPU | Min Memory | Recommended Memory |
    | :--------- | :------- | -------- | -------- | -------- |
    | K3s server | 1 core   | 2 cores  | 1 GB     | 1.5 GB   |
