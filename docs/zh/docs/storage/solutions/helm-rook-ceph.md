# 通过 Helm 部署 Rook-Ceph

本文将提供用 Helm 部署 Rook-Ceph 云原生存储系统的操作步骤及说明。

## Helm 安装

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

## 添加 rook repo

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

## Helm 安装 rook operator

```console
pwd[root@k8s-10-6-162-31 ~]# helm install --namespace rook-ceph rook-ceph rook-release/rook-ceph --create-namespace --set image.repository=rook/ceph --set csi.cephcsi.image=quay.io/cephcsi/cephcsi:v3.7.2 --set csi.registrar.image=registry.k8s.io/sig-storage/csi-node-driver-registrar:v2.5.1 --set csi.provisioner.image=registry.k8s.io/sig-storage/csi-provisioner:v3.3.0 --set csi.snapshotter.image=registry.k8s.io/sig-storage/csi-snapshotter:v6.1.0 --set csi.attacher.image=registry.k8s.io/sig-storage/csi-attacher:v4.0.0 --set csi.resizer.image=registry.k8s.io/sig-storage/csi-resizer:v1.6.0

[root@k8s-10-6-162-31 ~]# helm ls -A
NAME             NAMESPACE     REVISION     UPDATED                                        STATUS           CHART                     APP VERSION
rook-ceph        rook-ceph        1         2022-11-07  13:58:04.376723834 +0800 CST       deployed         rook-ceph-v1.10.5         v1.10.5

[root@k8s-10-6-162-31 ~]# kubectl get po -n rook-ceps
NAMESPACE         NAME                                        READY                    STATUS                       RESTARTS               AGE
rook-ceph         rook-ceph-operator-964d7fbbd-j2krp          1/1                      Running                       0                     39m
```

## Helm 安装 rook-ceph cluster 及 ceph tool

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

<details>
    <summary>点击此处查看 toolbox.yaml</summary>
    <pre><code>
apiVersion: apps/v1
kind: Deployment
metadata:
  name: rook-ceph-tools
  namespace: rook-ceph # namespace:cluster
  labels:
    app: rook-ceph-tools
spec:
  replicas: 1
  selector:
    matchLabels:
      app: rook-ceph-tools
  template:
    metadata:
      labels:
        app: rook-ceph-tools
    spec:
      dnsPolicy: ClusterFirstWithHostNet
      serviceAccountName: rook-ceph-default
      containers:
        - name: rook-ceph-tools
          image: quay.io/ceph/ceph:v18.2.2
          command:
            - /bin/bash
            - -c
            - |
              # Replicate the script from toolbox.sh inline so the ceph image
              # can be run directly, instead of requiring the rook toolbox
              CEPH_CONFIG="/etc/ceph/ceph.conf"
              MON_CONFIG="/etc/rook/mon-endpoints"
              KEYRING_FILE="/etc/ceph/keyring"

              # create a ceph config file in its default location so ceph/rados tools can be used
              # without specifying any arguments
              write_endpoints() {
                endpoints=$(cat ${MON_CONFIG})

                # filter out the mon names
                # external cluster can have numbers or hyphens in mon names, handling them in regex
                # shellcheck disable=SC2001
                mon_endpoints=$(echo "${endpoints}"| sed 's/[a-z0-9_-]\+=//g')

                DATE=$(date)
                echo "$DATE writing mon endpoints to ${CEPH_CONFIG}: ${endpoints}"
                  cat <<EOF > ${CEPH_CONFIG}
              [global]
              mon_host = ${mon_endpoints}

              [client.admin]
              keyring = ${KEYRING_FILE}
              EOF
              }

              # watch the endpoints config file and update if the mon endpoints ever change
              watch_endpoints() {
                # get the timestamp for the target of the soft link
                real_path=$(realpath ${MON_CONFIG})
                initial_time=$(stat -c %Z "${real_path}")
                while true; do
                  real_path=$(realpath ${MON_CONFIG})
                  latest_time=$(stat -c %Z "${real_path}")

                  if [[ "${latest_time}" != "${initial_time}" ]]; then
                    write_endpoints
                    initial_time=${latest_time}
                  fi

                  sleep 10
                done
              }

              # read the secret from an env var (for backward compatibility), or from the secret file
              ceph_secret=${ROOK_CEPH_SECRET}
              if [[ "$ceph_secret" == "" ]]; then
                ceph_secret=$(cat /var/lib/rook-ceph-mon/secret.keyring)
              fi

              # create the keyring file
              cat <<EOF > ${KEYRING_FILE}
              [${ROOK_CEPH_USERNAME}]
              key = ${ceph_secret}
              EOF

              # write the initial config file
              write_endpoints

              # continuously update the mon endpoints if they fail over
              watch_endpoints
          imagePullPolicy: IfNotPresent
          tty: true
          securityContext:
            runAsNonRoot: true
            runAsUser: 2016
            runAsGroup: 2016
            capabilities:
              drop: ["ALL"]
          env:
            - name: ROOK_CEPH_USERNAME
              valueFrom:
                secretKeyRef:
                  name: rook-ceph-mon
                  key: ceph-username
          volumeMounts:
            - mountPath: /etc/ceph
              name: ceph-config
            - name: mon-endpoint-volume
              mountPath: /etc/rook
            - name: ceph-admin-secret
              mountPath: /var/lib/rook-ceph-mon
              readOnly: true
      volumes:
        - name: ceph-admin-secret
          secret:
            secretName: rook-ceph-mon
            optional: false
            items:
              - key: ceph-secret
                path: secret.keyring
        - name: mon-endpoint-volume
          configMap:
            name: rook-ceph-mon-endpoints
            items:
              - key: data
                path: mon-endpoints
        - name: ceph-config
          emptyDir: {}
      tolerations:
        - key: "node.kubernetes.io/unreachable"
          operator: "Exists"
          effect: "NoExecute"
          tolerationSeconds: 5
    </code></pre>
</details>

## Ceph 工具验证

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

至此，用 Helm 部署安装 rook-ceph 完成。
