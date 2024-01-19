# 安装

在 DCE 5.0 社区版或商业版上安装智算能力模块。

## 安装 local-path-storage

为了满足系统组件对存储的需求，可以安装一个 local-path-storage：

??? note "查看完整的 YAML 代码"

    ```yaml title="local-path-storage.yaml"
    apiVersion: v1
    kind: Namespace
    metadata:
      name: local-path-storage

    ---
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: local-path-provisioner-service-account
      namespace: local-path-storage

    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: local-path-provisioner-role
    rules:
      - apiGroups: [ "" ]
        resources: [ "nodes", "persistentvolumeclaims", "configmaps" ]
        verbs: [ "get", "list", "watch" ]
      - apiGroups: [ "" ]
        resources: [ "endpoints", "persistentvolumes", "pods" ]
        verbs: [ "*" ]
      - apiGroups: [ "" ]
        resources: [ "events" ]
        verbs: [ "create", "patch" ]
      - apiGroups: [ "storage.k8s.io" ]
        resources: [ "storageclasses" ]
        verbs: [ "get", "list", "watch" ]

    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: local-path-provisioner-bind
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: local-path-provisioner-role
    subjects:
      - kind: ServiceAccount
        name: local-path-provisioner-service-account
        namespace: local-path-storage

    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: local-path-provisioner
      namespace: local-path-storage
    spec:
      replicas: 1
      selector:
        matchLabels:
        app: local-path-provisioner
      template:
        metadata:
          labels:
            app: local-path-provisioner
        spec:
          serviceAccountName: local-path-provisioner-service-account
          containers:
            - name: local-path-provisioner
              image: docker.m.daocloud.io/rancher/local-path-provisioner:v0.0.24
              imagePullPolicy: IfNotPresent
              command:
                - local-path-provisioner
                - --debug
                - start
                - --config
                - /etc/config/config.json
              volumeMounts:
                - name: config-volume
                mountPath: /etc/config/
              env:
                - name: POD_NAMESPACE
                  valueFrom:
                    fieldRef:
                    fieldPath: metadata.namespace
          volumes:
            - name: config-volume
              configMap:
                name: local-path-config

    ---
    apiVersion: storage.k8s.io/v1
    kind: StorageClass
    metadata:
      name: local-path
    provisioner: rancher.io/local-path
    volumeBindingMode: WaitForFirstConsumer
    reclaimPolicy: Delete

    ---
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: local-path-config
      namespace: local-path-storage
    data:
      config.json: |-
        {
                "nodePathMap":[
                {
                        "node":"DEFAULT_PATH_FOR_NON_LISTED_NODES",
                        "paths":["/opt/local-path-provisioner"]
                }
                ]
        }
      setup: |-
        #!/bin/sh
        set -eu
        mkdir -m 0777 -p "$VOL_DIR"
      teardown: |-
        #!/bin/sh
        set -eu
        rm -rf "$VOL_DIR"
      helperPod.yaml: |-
        apiVersion: v1
        kind: Pod
        metadata:
        name: helper-pod
        spec:
        containers:
        - name: helper-pod
            image: docker.m.daocloud.io/busybox
            imagePullPolicy: IfNotPresent
    ```

## 安装智算能力组件

```yaml
# baize 是智算能力组件的开发代号
helm repo add baize https://release.daocloud.io/chartrepo/baize
helm repo update
export VERSION=v0.1.1
helm upgrade --install baize baize/baize \
    --create-namespace \
    -n baize-system \
    --set global.imageRegistry=release.daocloud.io \
    --version=${VERSION}
    
# baize-agent ， 需要安装在每个工作集群中
```

## 安装 NFS Server

NFS Server 的部署方式仍旧在同一台服务器上，演示环境使用，所以这里权限是放开的，如果生产使用，请做好安全处理：

### 服务器部署 nfs-server

```shell
yum install -y nfs-utils

sudo systemctl enable rpcbind
sudo systemctl enable nfs

sudo systemctl start rpcbind
sudo systemctl start nfs

# 创建挂载目录, 默认用了 data， 可以修改
mkdir /data
vim /etc/exports
/data *(rw,sync,no_subtree_check,no_root_squash) # 添加此行

# mount test
mdkir /tmp/data && mount -t nfs 10.64.24.19:/data /tmp/data -o nolock
# 不报错就是成功
```

### 安装 NFS-csi

```helm
helm repo add csi-driver-nfs https://raw.githubusercontent.com/kubernetes-csi/csi-driver-nfs/master/charts
helm upgrade --install csi-driver-nfs csi-driver-nfs/csi-driver-nfs \
    --set image.nfs.repository=k8s.m.daocloud.io/sig-storage/nfsplugin \
    --set image.csiProvisioner.repository=k8s.m.daocloud.io/sig-storage/csi-provisioner \
    --set image.livenessProbe.repository=k8s.m.daocloud.io/sig-storage/livenessprobe \
    --set image.nodeDriverRegistrar.repository=k8s.m.daocloud.io/sig-storage/csi-node-driver-registrar \
    --namespace kube-system \
    --version v4.5.0
```

可能遇到的问题：

- 安装完成 csi 后会有 2 个 workload，一个是 Deployment，一个 daemonset，会有镜像拉取的问题，特别是在国内，可以使用 k8s.m.daocloud.io
- 如果遇到了 dns 解析的问题，可以修改 2 个 workload，将 spec.dnsPolicy 的值改为 ClusterFirstWithHostNet

### 创建 CSI

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: nfs-csi
provisioner: nfs.csi.k8s.io
parameters:
  server: 172.26.97.151
  share: /data
  # csi.storage.k8s.io/provisioner-secret is only needed for providing mountOptions in DeleteVolume
  # csi.storage.k8s.io/provisioner-secret-name: "mount-options"
  # csi.storage.k8s.io/provisioner-secret-namespace: "default"
reclaimPolicy: Delete
volumeBindingMode: Immediate
mountOptions:
  - nfsvers=4.1
```

可能遇到的问题：

- 在 SC 中 server 的地址的配置问题，如果是部署在集群内，使用 svc 地址的话，注意 dns 解析的问题，
  节点上的 dns 和 k8s 内的 core-dns 是不互通的。
