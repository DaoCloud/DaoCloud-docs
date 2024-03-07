# 在工作集群部署 NFS

## 背景

数据集是智能算力中核心数据管理功能，通过将 `MLOps` 全生命周期中对于数据的依赖统一抽象为了数据集，支持用户将各类数据纳管到数据集内，以便训练任务可以直接使用数据集中的数据。

当远端数据不在工作集群内时，数据集提供了自动进行预热的能力，支持 `Git`、`S3`、`HTTP`、`NFS` 等数据提前预热到集群本地。

`数据集` 需要一个支持 `ReadWriteMany` 模式的存储服务对远端数据进行预热，推荐在集群内部署 NFS。

本文主要介绍了如何快速部署一个 NFS 服务，并将其添加为集群的`存储类`。

## 准备工作

* NFS 默认使用节点的存储作为数据缓存点，因此需要确认磁盘本身有足够的磁盘空间。
* 安装方式使用 `Helm` 与 `Kubectl`，请确保已经安装好。

## 部署过程

一共需要安装 2 个组件：

* NFS Server
* csi-driver-nfs
* StorageClass

### 初始化命名空间

所以系统组件会安装到 `nfs` 的命名空间内，因此需要先创建命名空间。

```bash
kubectl create namespace nfs
```

### 安装 NFS Server

这里是一个简单的 YAML 部署文件，可以直接使用。

> 注意检查 `image:` ，根据集群所在位置情况，可能需要修改为国内镜像。

```yaml
---
kind: Service
apiVersion: v1
metadata:
  name: nfs-server
  namespace: nfs
  labels:
    app: nfs-server
spec:
  type: ClusterIP
  selector:
    app: nfs-server
  ports:
    - name: tcp-2049
      port: 2049
      protocol: TCP
    - name: udp-111
      port: 111
      protocol: UDP
---
kind: Deployment
apiVersion: apps/v1
metadata:
  name: nfs-server
  namespace: nfs
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nfs-server
  template:
    metadata:
      name: nfs-server
      labels:
        app: nfs-server
    spec:
      nodeSelector:
        "kubernetes.io/os": linux
      containers:
        - name: nfs-server
          image: itsthenetwork/nfs-server-alpine:latest
          env:
            - name: SHARED_DIRECTORY
              value: "/exports"
          volumeMounts:
            - mountPath: /exports
              name: nfs-vol
          securityContext:
            privileged: true
          ports:
            - name: tcp-2049
              containerPort: 2049
              protocol: TCP
            - name: udp-111
              containerPort: 111
              protocol: UDP
      volumes:
        - name: nfs-vol
          hostPath:
            path: /nfsdata  # 修改此处以指定另一个路径来存储 NFS 共享数据
            type: DirectoryOrCreate
```

将上述 `YAML` 保存为 `nfs-server.yaml` ，然后执行以下命令进行部署：

```bash
kubectl -n nfs apply -f nfs-server.yaml

# 检查部署结果
kubectl -n nfs get pod,svc
```

### 安装 csi-driver-nfs

安装 `csi-driver-nfs` 需要使用 `Helm`，请注意提前安装。

```bash
# 添加 Helm 仓库
helm repo add csi-driver-nfs https://mirror.ghproxy.com/https://raw.githubusercontent.com/kubernetes-csi/csi-driver-nfs/master/charts
helm repo update csi-driver-nfs

# 部署 csi-driver-nfs
# 这里参数主要优化了镜像地址，加速国内下载
helm upgrade --install csi-driver-nfs csi-driver-nfs/csi-driver-nfs \
    --set image.nfs.repository=k8s.m.daocloud.io/sig-storage/nfsplugin \
    --set image.csiProvisioner.repository=k8s.m.daocloud.io/sig-storage/csi-provisioner \
    --set image.livenessProbe.repository=k8s.m.daocloud.io/sig-storage/livenessprobe \
    --set image.nodeDriverRegistrar.repository=k8s.m.daocloud.io/sig-storage/csi-node-driver-registrar \
    --namespace nfs \
    --version v4.5.0
```

!!! warning

    注意，`csi-nfs-controller` 的镜像并未全部支持 `helm` 参数，需要手工修改 `deployment` 的 `image` 字段
    将 `image: registry.k8s.io` 改为 `image: k8s.dockerproxy.com` 以加速国内下载。

### 创建 StorageClass

将以下 `YAML` 保存为 `nfs-sc.yaml` ，然后执行以下命令进行部署：

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: nfs-csi
provisioner: nfs.csi.k8s.io
parameters:
  server: nfs-server.nfs.svc.cluster.local
  share: /
  # csi.storage.k8s.io/provisioner-secret is only needed for providing mountOptions in DeleteVolume
  # csi.storage.k8s.io/provisioner-secret-name: "mount-options"
  # csi.storage.k8s.io/provisioner-secret-namespace: "default"
reclaimPolicy: Delete
volumeBindingMode: Immediate
mountOptions:
  - nfsvers=4.1
```

```bash
kubectl apply -f nfs-sc.yaml
```

## 测试

创建数据集，并将数据集的 **关联存储类**， `预热方式` 设置为 `NFS`，即可将远端数据预热到集群内。

数据集创建成功后，可以看到数据集的状态为 `预热中`，等待预热完成后即可使用。
