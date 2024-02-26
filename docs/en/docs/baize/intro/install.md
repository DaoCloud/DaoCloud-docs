# Installation

Install the Cloud Native AI module on DCE 5.0 Community Edition or Enterprise Edition.

## Install local-path-storage

To meet the storage needs of system components, you can install a local-path-storage:

??? note "View the complete YAML code"

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

## Install Cloud Native AI Components

```yaml
# Baize is the development codename for the Cloud Native AI module
helm repo add baize https://release.daocloud.io/chartrepo/baize
helm repo update
export VERSION=v0.1.1
helm upgrade --install baize baize/baize \
    --create-namespace \
    -n baize-system \
    --set global.imageRegistry=release.daocloud.io \
    --version=${VERSION}
    
# Baize-agent, needs to be installed on each working cluster
```

## Install NFS Server

The deployment of the NFS Server is still on the same server for demonstration purposes. Therefore, permissions are open here. If used in production, please ensure proper security measures are in place:

### Server Deployment of NFS Server

```shell
yum install -y nfs-utils

sudo systemctl enable rpcbind
sudo systemctl enable nfs

sudo systemctl start rpcbind
sudo systemctl start nfs

# Create mount directory, default is 'data', can be modified
mkdir /data
vim /etc/exports
/data *(rw,sync,no_subtree_check,no_root_squash) # Add this line

# Mount test
mkdir /tmp/data && mount -t nfs 10.64.24.19:/data /tmp/data -o nolock
# If no errors, the mount was successful
```

### Install NFS-csi

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

Possible Issues:

- After installing CSI, there will be 2 workloads, one is a Deployment and the other is a DaemonSet. There may be image pulling issues, especially in China. You can use k8s.m.daocloud.io for image pulling.
- If you encounter DNS resolution issues, you can modify 2 workloads by changing the value of spec.dnsPolicy to ClusterFirstWithHostNet.

### Create CSI

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

Possible Issues:

- Configuration issue with the server address in the Storage Class (SC). If deployed within the cluster and using the service (svc) address, be mindful of DNS resolution issues. The DNS on the nodes and the core-dns inside Kubernetes are not interconnected.
