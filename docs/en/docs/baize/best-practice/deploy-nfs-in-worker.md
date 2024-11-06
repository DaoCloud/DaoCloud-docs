# Deploy NFS for Preloading Dataset

A **Network File System (NFS)** allows remote hosts to mount file systems over a network and
interact with those file systems as though they are mounted locally. This enables
system administrators to consolidate resources onto centralized servers on the network.

**Dataset** is a core feature provided by DCE 5.0 AI Lab.
By abstracting the dependency on data throughout the entire lifecycle of MLOps
into datasets, users can manage various types of data in datasets so that
training tasks can directly use the data in the dataset.

When remote data is not within the worker cluster, datasets provide the capability
to automatically preheat data, supporting data preloading from sources such as
`Git`, `S3`, and `HTTP` to the local cluster.

A storage service supporting the `ReadWriteMany` mode is needed for preloading
remote data for the `dataset`, and it is recommended to deploy NFS within the cluster.

This article mainly introduces how to quickly deploy an NFS service and add it as a
`StorageClass` for the cluster.

## Preparation

* NFS by default uses the node's storage as a data caching point,
  so it is necessary to ensure that the disk itself has enough disk space.
* The installation method uses `Helm` and `Kubectl`, please make sure they are already installed.

## Deployment Steps

Several components need to be installed:

* NFS Server
* csi-driver-nfs
* StorageClass

### Initialize Namespace

All system components will be installed in the `nfs` namespace,
so it is necessary to create this namespace first.

```bash
kubectl create namespace nfs
```

### Install NFS Server

Here is a simple YAML deployment file that can be used directly.

!!! note

    Be sure to check the `image:` and modify it to a domestic mirror based on the location of the cluster.

```yaml title="nfs-server.yaml"
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
            path: /nfsdata  # (1)!
            type: DirectoryOrCreate
```

1. Modify this to specify another path to store NFS shared data

Save the above YAML as `nfs-server.yaml`, then run the following commands for deployment:

```bash
kubectl -n nfs apply -f nfs-server.yaml

# Check the deployment result
kubectl -n nfs get pod,svc
```

### Install csi-driver-nfs

Installing `csi-driver-nfs` requires the use of `Helm`, please ensure it is installed beforehand.

```bash
# Add Helm repository
helm repo add csi-driver-nfs https://mirror.ghproxy.com/https://raw.githubusercontent.com/kubernetes-csi/csi-driver-nfs/master/charts
helm repo update csi-driver-nfs

# Deploy csi-driver-nfs
# The parameters here mainly optimize the image address to accelerate downloads in China
helm upgrade --install csi-driver-nfs csi-driver-nfs/csi-driver-nfs \
    --set image.nfs.repository=k8s.m.daocloud.io/sig-storage/nfsplugin \
    --set image.csiProvisioner.repository=k8s.m.daocloud.io/sig-storage/csi-provisioner \
    --set image.livenessProbe.repository=k8s.m.daocloud.io/sig-storage/livenessprobe \
    --set image.nodeDriverRegistrar.repository=k8s.m.daocloud.io/sig-storage/csi-node-driver-registrar \
    --namespace nfs \
    --version v4.5.0
```

!!! warning

    Not all images of `csi-nfs-controller` support `helm` parameters, so the `image` field of the `deployment` needs to be manually modified.
    Change `image: registry.k8s.io` to `image: k8s.dockerproxy.com` to accelerate downloads in China.

### Create StorageClass

Save the following YAML as `nfs-sc.yaml`:

```yaml title="nfs-sc.yaml"
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

then run the following command:

```bash
kubectl apply -f nfs-sc.yaml
```

## Test

Create a dataset and set the dataset's **associated storage class** and
`preloading method` to `NFS` to preheat remote data into the cluster.

After the dataset is successfully created, you can see that the dataset's status is `preloading`,
and you can start using it after the preloading is completed.

## FAQs

### Missing Necessary NFS Client Software `/sbin/mount`

```bash
bad option; for several filesystems (e.g. nfs, cifs) you might need a /sbin/mount.<type> helper program.
```

On the nodes running Kubernetes, ensure that the NFS client is installed:

=== "Ubuntu/Debian"

    Run the following commands to install the NFS client:

    ```bash
    sudo apt-get update
    sudo apt-get install nfs-common
    ```

=== "CentOS/RHEL"

    Run the following command to install the NFS client:

    ```bash
    sudo yum install nfs-utils
    ```

Check the NFS server configuration to ensure that the NFS server is running
and configured correctly. You can try mounting manually to test:

```bash
sudo mkdir -p /mnt/test
sudo mount -t nfs <nfs-server>:/nfsdata /mnt/test
```
