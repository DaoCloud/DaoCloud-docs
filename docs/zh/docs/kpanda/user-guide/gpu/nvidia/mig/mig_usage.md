# 使用 MIG GPU 资源

本节介绍应用如何使用 MIG GPU 资源。

## 前提条件

- 已经[部署 DCE 5.0](../../../../../install/index.md) 容器管理平台，且平台运行正常。
- 容器管理模块[已接入 Kubernetes 集群](../../../clusters/integrate-cluster.md)或者[已创建 Kubernetes 集群](../../../clusters/create-cluster.md)，且能够访问集群的 UI 界面。
- 已安装[GPU Operator](../install_nvidia_driver_of_operator.md)。
- 集群节点上具有[对应型号的 GPU 卡](../../gpu_matrix.md)

## UI 界面使用 MIG GPU

1. 确认集群是否已识别 GPU 卡类型

    进入 __集群详情__ -> __节点管理__ ，查看是否已正确识别为 MIG 模式。

    ![gpu](../../images/node-mig.png)

2. 通过镜像部署应用，可选择并使用 NVIDIA MIG 资源。

- MIG Single 模式示例（与整卡使用方式相同）：

    !!! note
    
        MIG single 策略允许用户以与 GPU 整卡相同的方式（`nvidia.com/gpu`）请求和使用GPU资源，不同的是这些资源可以是 GPU 的一部分（MIG设备），而不是整个GPU。了解更多![GPU MIG 模式设计](https://docs.google.com/document/d/1bshSIcWNYRZGfywgwRHa07C0qRyOYKxWYxClbeJM-WM/edit#heading=h.jklusl667vn2)
    
    ![usemig](../../images/usemig.png)

- MIG Mixed 模式示例：

    ![mig02](../../images/pod-mig.png)

## YAML 配置使用 MIG

**MIG Single__ 模式：**

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

1. 申请 MIG GPU 的数量

**MIG Mixed 模式：**

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

1. 通过 nvidia.com/mig-g.gb 的资源类型公开各个 MIG 设备

进入容器后可以查看只使用了一个 MIG 设备。

![mig03](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/kpanda/images/gpu_mig03.png)
