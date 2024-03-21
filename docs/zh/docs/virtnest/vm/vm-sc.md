# 创建虚拟机 - 存储

本文将介绍如何在创建虚拟机时，配置存储信息。

存储和虚拟机的功能息息相关，主要是通过使用 Kubernetes 的持久卷和存储类，提供了灵活且可扩展的虚拟机存储能力。
比如虚拟机镜像存储在 PVC 里，支持和其他数据一起克隆、快照等

## 部署不同的存储

在使用虚拟机存储功能之前，需要根据需要部署不同的存储：

1. 参考[部署 hwameistor](https://hwameistor.io/cn/docs/category/installation)，
   或者在容器管理模块的 Helm 模板中安装 hwameistor-operator。
2. 参考[部署 rook-ceph](https://rook.io/docs/rook/latest-release/Getting-Started/quickstart/)
3. 部署 localpath，使用命令 `kubectl apply -f` 创建以下 YAML：

??? note "点击查看完整 YAML"

    ```yaml
    ---
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
    - apiGroups: [""]
      resources: ["nodes", "persistentvolumeclaims", "configmaps"]
      verbs: ["get", "list", "watch"]
    - apiGroups: [""]
      resources: ["endpoints", "persistentvolumes", "pods"]
      verbs: ["*"]
    - apiGroups: [""]
      resources: ["events"]
      verbs: ["create", "patch"]
    - apiGroups: ["storage.k8s.io"]
      resources: ["storageclasses"]
      verbs: ["get", "list", "watch"]

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
            image: rancher/local-path-provisioner:v0.0.22
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
          "nodePathMap": [
            {
              "node": "DEFAULT_PATH_FOR_NON_LISTED_NODES",
              "paths": ["/opt/local-path-provisioner"]
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
            image: busybox
            imagePullPolicy: IfNotPresent
    ```

## 虚拟机存储

1. 系统盘：系统默认创建一个 VirtIO 类型的 rootfs 系统盘，用于存放操作系统和数据。

2. 数据盘：数据盘是虚拟机中用于存储用户数据、应用程序数据或其他非操作系统相关文件的存储设备。与系统盘相比，数据盘是非必选的，可以根据需要动态添加或移除。数据盘的容量也可以根据需求进行灵活配置。

    默认使用块存储。如果需要使用克隆和快照功能，请确保您的存储池已经创建了对应的 VolumeSnapshotClass， 可以参考以下示例。如果需要使用实时迁移功能，请确保您的存储支持并选择了 ReadWriteMany 的访问模式 。

    大多数情况下，存储在安装过程中不会自动创建这样的 VolumeSnapshotClass，因此您需要手动创建 VolumeSnapshotClass。
    以下是一个 HwameiStor 创建 VolumeSnapshotClass 的示例：

    ```yaml
    kind: VolumeSnapshotClass
    apiVersion: snapshot.storage.k8s.io/v1
    metadata:
      name: hwameistor-storage-lvm-snapshot
      annotations:
        snapshot.storage.kubernetes.io/is-default-class: "true"
    parameters:
      snapsize: "1073741824"
    driver: lvm.hwameistor.io
    deletionPolicy: Delete
    ```

    - 执行以下命令检查 VolumeSnapshotClass 是否创建成功。

        ```sh
        kubectl get VolumeSnapshotClass
        ```

    - 查看已创建的 Snapshotclass，并且确认 Provisioner 属性同存储池中的 Driver 属性一致。
