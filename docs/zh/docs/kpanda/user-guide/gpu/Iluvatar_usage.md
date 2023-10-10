# 使用天数（Iluvatar）GPU

DCE 5.0 支持通过 UI 图形界面和 YAML 声明方式使用天数虚拟 GPU。

## 前提条件

- 已经[部署 DCE 5.0](../../../install/index.md) 容器管理平台，且平台运行正常。
- 容器管理模块[已接入 Kubernetes 集群](../clusters/integrate-cluster.md)或者[已创建 Kubernetes 集群](../clusters/create-cluster.md)，且能够访问集群的 UI 界面。
- 当前集群已安装天数（Iluvatar）GPU 驱动。
- 当前集群内 GPU 卡未进行任何虚拟化操作或被其它应用占用。

## UI 界面配置步骤

1. 确认集群是否已检测 GPU 卡。点击对应`集群` -> `集群设置` -> `Addon 插件`，查看是否已自动启用并自动检测对应 GPU 类型。
    目前集群会自动启用 `GPU`，并且设置 `GPU` 类型为 `Iluvatar`。

    ![集群设置](./images/cluster-setting-iluvatar-gpu.jpg)

2. 部署工作负载，点击对应`集群` -> `工作负载`，通过镜像方式部署工作负载，选择类型（Iluvatar）之后，需要配置应用使用的 GPU 资源：

    - **物理卡数量（iluvatar.ai/vcuda-core）**：表示当前 Pod 需要挂载几张物理卡，
      输入值必须为整数且**小于等于**宿主机上的卡数量。
    - **显存使用数量（iluvatar.ai/vcuda-memory）**：表示每张卡占用的 GPU 显存，
      值单位为 MB，最小值为 1，最大值为整卡的显存值。

    ![负载使用](./images/workload_iluvatargpu_userguide.jpg)

    > 如果上述值配置的有问题则会出现调度失败，资源分配不了的情况。

## YAML 配置说明

创建工作负载申请 GPU 资源，在资源申请和限制配置中增加
`iluvatar.ai/vcuda-core: 1`、`iluvatar.ai/vcuda-memory: 200` 参数配置应用使用物理卡的资源。

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
