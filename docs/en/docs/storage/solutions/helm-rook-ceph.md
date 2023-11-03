# Deploy Rook-Ceph via Helm

This page will provide the steps and instructions for deploying the Rook-Ceph cloud native storage system with Helm.

## Install by Helm

```console
[root@k8s-10-6-162-31 ~]# wget https://get.helm.sh/helm-v3.10.1-linux-amd64.tar.gz

[root@k8s-10-6-162-31 ~]# tar xvfz helm-v3.10.1-linux-amd64.tar.gz
linux-amd64/
linux-amd64/helm
linux-amd64/LICENSE
linux-amd64/README.md
[root@k8s-10-6-162-31 ~]#
[root@k8s-10-6-162-31 ~]#
[root@k8s-10-6-162-31 ~]# ls
anaconda-ks.cfg calico.yaml helm-v3.10.1-linux-amd64.tar.gz linux-amd64 rook rook-ceph-image rook-ceph-image.zip
[root@k8s-10-6-162-31 ~]# cd linux-amd64
[root@k8s-10-6-162-31 linux-amd64]# ls
helm LICENSE README.md
[root@k8s-10-6-162-31 linux-amd64]# mv helm /usr/bin
[root@k8s-10-6-162-31 linux-amd64]#
[root@k8s-10-6-162-31 linux-amd64]# cd /root
[root@k8s-10-6-162-31 ~]# helm
The Kubernetes package manager

Common actions for Helm:

- helm search: search for charts
- helm pull: download a chart to your local directory to view
- helm install: upload the chart to Kubernetes
- helm list: list releases of charts
```

## Add rook repo

```console
helm repo add rook-release https://charts.rook.io/release

[root@k8s-10-6-162-31 ~]# helm repo list
NAME                          URL
rook-release              https://charts.rook.io/release
stable                    http://mirror.azure.cn/kubernetes/charts/
aliyun                    https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts


[root@k8s-10-6-162-31 ~]# helm search repo rook-ceph
NAME                                    CHART VERSION              APP VERSION         DESCRIPTION
rook-release/rook-ceph                    v1.10.5                   v1.10.5            File, Block, and Object Storage Services for yo...
rook-release/rook-ceph-cluster            v1.10.5                   v1.10.5            Manages a single Ceph cluster namespace for Rook
```

## Install rook operator via Helm 

```console
pwd[root@k8s-10-6-162-31 ~]# helm install --namespace rook-ceph rook-ceph rook-release/rook-ceph --create-namespace --set image.repository=rook/ceph --set csi.cephcsi.image=quay.io/cephcsi/cephcsi:v3.7.2 --set csi.registrar.image=registry.k8s.io/sig-storage/csi-node-driver-registrar:v2.5.1 --set csi.provisioner.image=registry.k8s.io/sig-storage/csi-provisioner:v3.3.0 --set csi.snapshotter.image=registry.k8s.io/sig-storage/csi-snapshotter:v6.1.0 --set csi.attacher.image=registry.k8s.io/sig-storage/csi-attacher:v4.0.0 --set csi.resizer.image=registry.k8s.io/sig-storage/csi-resizer:v1.6.0

[root@k8s-10-6-162-31 ~]# helm ls -A
NAME             NAMESPACE     REVISION     UPDATED                                        STATUS           CHART                     APP VERSION
rook-ceph        rook-ceph        1         2022-11-07  13:58:04.376723834 +0800 CST       deployed         rook-ceph-v1.10.5         v1.10.5

[root@k8s-10-6-162-31 ~]# kubectl get po -n rook-ceps
NAMESPACE         NAME                                        READY                    STATUS                       RESTARTS               AGE
rook-ceph         rook-ceph-operator-964d7fbbd-j2krp          1/1                      Running                       0                     39m
```

## Install rook-ceph cluster and ceph tools via helm

```console
[root@k8s-10-6-162-31 ~]# helm install --namespace rook-ceph rook-ceph-cluster rook-release/rook-ceph-cluster --set operatorNamespace=rook-ceph --set cephClusterSpec.storage.deviceFilter="^sd." --set cephClusterSpec.cephVersion.image=quay.io/ceph/ceph:v17.2.3
NAME: rook-ceph-cluster
LAST DEPLOYED: Mon Nov 7 14:49:28 2022
NAMESPACE: rook-ceph
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
The Ceph Cluster has been installed. Check its status by running:
kubectl --namespace rook-ceph get cephcluster

Visit https://rook.io/docs/rook/latest/CRDs/ceph-cluster-crd/ for more information about the Ceph CRD.

Important Notes:
- You can only deploy a single cluster per namespace
- If you wish to delete this cluster and start fresh, you will also have to wipe the OSD disks using `sfdisk`

[root@k8s-10-6-162-31 examples]# helm ls -A
NAME                    NAMESPACE          REVISION          UPDATED                                      STATUS          CHART                      APP VERSION
rook-ceph               rook-ceph            1               2022-11-07 13:58:04.376723834 +0800 CST      deployed        rook-ceph-v1.10.5          v1.10.5
rook-ceph-cluster       rook-ceph            1               2022-11-07 14:49:28.709538725 +0800 CST      deployed        rook-ceph-cluster-v1.10.5  v1.10.5

[root@k8s-10-6-162-31 ceph]# kubectl create -f toolbox.yaml
deployment.apps/rook-ceph-tools created

[root@k8s-10-6-162-31 examples]# kubectl get po -n rook-ceph
NAME                                                               READY              STATUS               RESTARTS             AGE
csi-cephfsplugin-6jxvj                                             2/2                Running              0                    90m
csi-cephfsplugin-h68jt                                             2/2                Running              0                    90m
csi-cephfsplugin-provisioner-785d976fcf-p96s9                      5/5                Running              0                    30m
csi-cephfsplugin-provisioner-785d976fcf-w7j7p                      5/5                Running              0                    90m
csi-cephfsplugin-rzq9d                                             2/2                Running              0                    90m
csi-rbdplugin-7jcgf                                                2/2                Running              0                    90m
csi-rbdplugin-7z4v8                                                2/2                Running              0                    90m
csi-rbdplugin-8l6c9                                                2/2                Running              0                    90m
csi-rbdplugin-provisioner-dc499c7dd-62d2p                          5/5                Running              2                    90m
csi-rbdplugin-provisioner-dc499c7dd-kv6c5                          5/5                Running              0                    30m
rook-ceph-crashcollector-k8s-10-6-162-31-67678cc9f9-8ctkb          1/1                Running              0                    46m
rook-ceph-crashcollector-k8s-10-6-162-32-8655c84654-9mj22          1/1                Running              0                    18m
rook-ceph-crashcollector-k8s-10-6-162-33-5dbcc6965c-8dk89          1/1                Running              0                    46m
rook-ceph-mds-ceph-filesystem-a-b8fdd6876-s8s94                    2/2                Running              0                    30m
rook-ceph-mds-ceph-filesystem-b-fd667b865-49vx2                    2/2                Running              0                    32m
rook-ceph-mgr-a-5dbd5b49d5-2thts                                   3/3                Running              0                    46m
rook-ceph-mgr-b-6bbc5966c8-gt2fg                                   3/3                Running              0                    30m
rook-ceph-mon-a-56d4476dfd-hjr6b                                   2/2                Running              1                    (47m ago) 89m
rook-ceph-mon-b-5978cc6657-zd2tb                                   2/2                Running              0                    86m
rook-ceph-mon-c-5d94c6c9cc-9s6p9                                   2/2                Running              0                    63m
rook-ceph-operator-964d7fbbd-d6s6w                                 1/1                Running              0                    30m
rook-ceph-osd-0-79467bcb49-qtf6g                                   2/2                Running              0                    30m
rook-ceph-osd-1-64c5945d78-72z4q                                   2/2                Running              0                    30m
rook-ceph-osd-2-f68b5bcb7-59nwb                                    2/2                Running              0                    30m
rook-ceph-osd-3-99c576b7-j7prn                                     2/2                Running              0                    30m
rook-ceph-osd-4-579d5f966f-cqw5f                                   2/2                Running              0                    30m
rook-ceph-osd-5-655d7bfbd7-kztj2                                   2/2                Running              0                    30m
rook-ceph-osd-prepare-k8s-10-6-162-31-tzz2f                        0/1                Completed            0                    23m
rook-ceph-osd-prepare-k8s-10-6-162-32-7blmc                        0/1                Completed            0                    22m
rook-ceph-osd-prepare-k8s-10-6-162-33-pjjmd                        0/1                Completed            0                    22m
rook-ceph-rgw-ceph-objectstore-a-6d8b954f7d-jx9zx                  2/2                Running              0                    18m
rook-ceph-tools-7c8ddb978b-2mf52                                   1/1                Running              0                    40m
```

## Ceph tool verification

```console
[root@k8s-10-6-162-31 ~]# kubectl exec -it rook-ceph-tools-7c8ddb978b-2mf52 -n rook-ceph -- bash
bash-4.4$

bash-4.4$ ceph -s
cluster:
id: fcba483d-2c38-48cd-9137-fb93be678383
health: HEALTH_WARN
1 MDSs report slow metadata IOs
Reduced data availability: 6 pgs inactive

services:
mon: 3 daemons, quorum a,b,c (age 16m)
mgr: a(active, since 115s), standbys: b
mds: 1/1 daemons up, 1 standby
osd: 6 osds: 0 up, 6 in (since 96s)

data:
volumes: 1/1 healthy
pools: 6 pools, 6 pgs
objects: 0 objects, 0 B
usage: 0 B used, 0 B / 0 B avail
pgs: 100.000% pgs unknown
6 unknown
```

So far, rook-ceph has been installed with Helm deployment.
