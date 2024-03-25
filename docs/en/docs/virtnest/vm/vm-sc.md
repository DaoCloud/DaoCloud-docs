# Storage for Virtual Machine

This article will introduce how to configure storage when creating a virtual machine.

Storage and virtual machine functionality are closely related, mainly providing flexible and scalable virtual machine storage capabilities through the use of Kubernetes persistent volumes and storage classes.
For example, virtual machine image storage in PVC supports cloning, snapshotting, and other operations with other data.

## Deploying Different Storage

Before using virtual machine storage functionality, different storage needs to be deployed according to requirements:

1. Refer to [Deploying hwameistor](https://hwameistor.io/cn/docs/category/installation),
   or install hwameistor-operator in the Helm template of the container management module.
2. Refer to [Deploying rook-ceph](https://rook.io/docs/rook/latest-release/Getting-Started/quickstart/)
3. Deploy localpath, use the command `kubectl apply -f` to create the following YAML:

??? note "Click to view complete YAML"

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

## Virtual Machine Storage

1. System Disk: By default, a VirtIO type rootfs system disk is created for the system to store the operating system and data.

2. Data Disk: The data disk is a storage device in the virtual machine used to store user data, application data, or other files unrelated to the operating system. Compared to the system disk, the data disk is optional and can be dynamically added or removed as needed. The capacity of the data disk can also be flexibly configured according to requirements.

    Block storage is used by default. If you need to use cloning and snapshot functions, make sure that your storage pool has created the corresponding VolumeSnapshotClass, as shown in the example below. If you need to use real-time migration, make sure that your storage supports and has selected the ReadWriteMany access mode.

    In most cases, such VolumeSnapshotClass is not automatically created during the installation process, so you need to manually create VolumeSnapshotClass.
    Here is an example of creating a VolumeSnapshotClass in HwameiStor:

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

    - Execute the following command to check if the VolumeSnapshotClass has been successfully created.

        ```sh
        kubectl get VolumeSnapshotClass
        ```

    - View the created Snapshotclass and confirm that the Provisioner property is consistent with the Driver property in the storage pool.
