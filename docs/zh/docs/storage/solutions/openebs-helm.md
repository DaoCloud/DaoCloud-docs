# 通过 Helm 部署并验证 OpenEBS

本文将提供用 Helm 部署并验证 OpenEBS 云原生存储系统的操作步骤及说明。
DCE 5.0 支持众多第三方存储方案，我们针对 OpenEBS 进行了相关测试，并最终将其作为 Addon 集成了应用商店中。 以下是对 OpenEBS 的调研和测评。

有关应用商店 Addon 的图形化界面安装、部署、卸载等操作说明，将于稍后提供。

## 测试环境

本次测试使用三个虚拟机节点部署一个 Kubernetes 集群：1 个 Master + 2 个 Worker 节点，kubelet 版本为 1.23.6。

```
[root@k8s-10-6-162-31 ~]# kubectl get no
NAME              STATUS   ROLES                  AGE    VERSION
k8s-10-6-162-31   Ready    control-plane,master   114d   v1.23.6
k8s-10-6-162-32   Ready    <none>                 114d   v1.23.6
k8s-10-6-162-33   Ready    <none>                 114d   v1.23.6
```

## 添加并更新 OpenEBS repo

```
[root@k8s-10-6-162-31 ~]# helm repo add openebs https://openebs.github.io/charts
"openebs" has been added to your repositories
[root@k8s-10-6-162-31 ~]# helm repo update
Hang tight while we grab the latest from your chart repositories...
...Successfully got an update from the "longhorn" chart repository
...Successfully got an update from the "openebs" chart repository
Update Complete. ⎈Happy Helming!⎈
[root@k8s-10-6-162-31 ~]# helm repo list
NAME URL
longhorn https://charts.longhorn.io
openebs https://openebs.github.io/charts
```

## Helm 安装 OpenEBS

```
[root@k8s-10-6-162-31 ~]# helm install openebs --namespace openebs openebs/openebs --create-namespace
NAME: openebs
LAST DEPLOYED: Tue Jan 31 14:44:11 2023
NAMESPACE: openebs
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
Successfully installed OpenEBS.

Check the status by running: kubectl get pods -n openebs

The default values will install NDM and enable OpenEBS hostpath and device
storage engines along with their default StorageClasses. Use `kubectl get sc`
to see the list of installed OpenEBS StorageClasses.

**Note**: If you are upgrading from the older helm chart that was using cStor
and Jiva (non-csi) volumes, you will have to run the following command to include
the older provisioners:

helm upgrade openebs openebs/openebs \
--namespace openebs \
--set legacy.enabled=true \
--reuse-values

For other engines, you will need to perform a few more additional steps to
enable the engine, configure the engines (e.g. creating pools) and create
StorageClasses.

For example, cStor can be enabled using commands like:

helm upgrade openebs openebs/openebs \
--namespace openebs \
--set cstor.enabled=true \
--reuse-values

For more information,
- view the online documentation at https://openebs.io/docs or
- connect with an active community on Kubernetes slack #openebs channel.
```

## 查看已安装 OpenEBS 集群资源
```
[root@k8s-10-6-162-31 ~]# kubectl get po -nopenebs
NAME                                                         READY       STATUS        RESTARTS       AGE
openebs-localpv-provisioner-5646cc6748-sdh2g                  1/1        Running       6 (4m44s ago)  47m
openebs-ndm-6dffs                                             1/1        Running       0              47m
openebs-ndm-fs2jk                                             1/1        Running       0              47m
openebs-ndm-m5x6d                                             1/1        Running       0              47m
openebs-ndm-operator-65fdff8c8d-zvl8v                         1/1        Running       0              47m

[root@k8s-10-6-162-31 ~]# mkdir -p /data/openebs/local
[root@k8s-10-6-162-31 ~]# cd /data/openebs/local
[root@k8s-10-6-162-31 local]# pwd
/data/openebs/local
[root@k8s-10-6-162-31 ~]# kubectl get sc -A
NAME                     PROVISIONER             RECLAIMPOLICY    VOLUMEBINDINGMODE    ALLOWVOLUMEEXPANSION   AGE
longhorn (default)       driver.longhorn.io      Delete           Immediate            true                   48d
openebs-device           openebs.io/local        Delete           WaitForFirstConsumer false                  19h
openebs-hostpath         openebs.io/local        Delete           WaitForFirstConsumer false                  19h
```
## 创建 local-hostpath-pvc 资源
```
[root@k8s-10-6-162-31 ~]# cat local-hostpath-pvc.yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
name: local-hostpath-pvc
spec:
storageClassName: openebs-hostpath
accessModes:
- ReadWriteOnce
resources:
requests:
storage: 5G
[root@k8s-10-6-162-31 ~]#

[root@k8s-10-6-162-31 ~]# cat local-hostpath-pod.yaml
apiVersion: v1
kind: Pod
metadata:
name: hello-local-hostpath-pod
spec:
volumes:
- name: local-storage
persistentVolumeClaim:
claimName: local-hostpath-pvc
containers:
- name: hello-container
image: busybox
command:
- sh
- -c
- 'while true; do echo "`date` [`hostname`] Hello from OpenEBS Local PV." >> /data/greeting.txt; sleep $(($RANDOM % 5 + 300)); done'
volumeMounts:
- mountPath: /data
name: local-storage

[root@k8s-10-6-162-31 ~]# kubectl apply -f local-hostpath-pvc.yaml
persistentvolumeclaim/local-hostpath-pvc created
[root@k8s-10-6-162-31 ~]# kubectl get pvc
NAME STATUS VOLUME CAPACITY ACCESS MODES STORAGECLASS AGE
local-hostpath-pvc Pending openebs-hostpath 8s

[root@k8s-10-6-162-31 ~]# kubectl apply -f local-hostpath-pod.yaml
pod/hello-local-hostpath-pod created
[root@k8s-10-6-162-31 ~]#
[root@k8s-10-6-162-31 ~]# kubectl get po
NAME READY STATUS RESTARTS AGE
hello-local-hostpath-pod 0/1 Pending 0 11s
longhorn-iscsi-installation-2thd5 1/1 Running 1 48d
longhorn-iscsi-installation-ctqtg 1/1 Running 1 (47d ago) 48d
longhorn-iscsi-installation-mrm4h 1/1 Running 1 (47d ago) 48d

[root@k8s-10-6-162-31 ~]# kubectl get po
NAME READY STATUS RESTARTS AGE
hello-local-hostpath-pod 1/1 Running 0 4m56s
longhorn-iscsi-installation-2thd5 1/1 Running 1 48d
longhorn-iscsi-installation-ctqtg 1/1 Running 1 (47d ago) 48d
longhorn-iscsi-installation-mrm4h 1/1 Running 1 (47d ago) 48d
```
## 创建 workload 并验证 
```
[root@k8s-10-6-162-31 ~]# kubectl exec hello-local-hostpath-pod -- cat /data/greeting.txt
Wed Feb 1 03:50:57 UTC 2023 [hello-local-hostpath-pod] Hello from OpenEBS Local PV.

[root@k8s-10-6-162-31 ~]# kubectl exec -it hello-local-hostpath-pod -sh
error: you must specify at least one command for the container
[root@k8s-10-6-162-31 ~]# kubectl exec -it hello-local-hostpath-pod -- sh
/ # ls
bin data dev etc home proc root sys tmp usr var
/ # cd data
/data # ls
greeting.txt
/data # cat greeting.txt
Wed Feb 1 03:50:57 UTC 2023 [hello-local-hostpath-pod] Hello from OpenEBS Local PV.
Wed Feb 1 03:55:59 UTC 2023 [hello-local-hostpath-pod] Hello from OpenEBS Local PV.
Wed Feb 1 04:01:01 UTC 2023 [hello-local-hostpath-pod] Hello from OpenEBS Local PV.
Wed Feb 1 04:06:04 UTC 2023 [hello-local-hostpath-pod] Hello from OpenEBS Local PV.

[root@k8s-10-6-162-31 ~]# kubectl get -o yaml pv |grep 'path:'
path: /var/openebs/local/pvc-44db3536-2dc3-4b4d-bcd6-6d388a534fcd
[root@k8s-10-6-162-31 ~]#
[root@k8s-10-6-162-31 ~]# kubectl get pv
NAME                                       CAPACITY   ACCESS MODES    RECLAIM POLICY     STATUS    CLAIM                         STORAGECLASS      REASON    AGE
pvc-44db3536-2dc3-4b4d-bcd6-6d388a534fcd   5G         RWO             Delete             Bound     default/local-hostpath-pvc    openebs-hostpath            71m
[root@k8s-10-6-162-31 ~]# kubectl get -o yaml pv pvc-44db3536-2dc3-4b4d-bcd6-6d388a534fcd |grep 'path:'
path: /var/openebs/local/pvc-44db3536-2dc3-4b4d-bcd6-6d388a534fcd
```
## 安装 dbench 性能测试工具
```
[root@k8s-10-6-162-31 ~]# cat fio-deploy.yaml
** NOTE: For details of params to construct an fio job, refer to this link:
** https://fio.readthedocs.io/en/latest/fio_doc.html

---
apiVersion: batch/v1
kind: Job
metadata:
generateName: dbench-
spec:
template:
spec:
containers:
- name: dbench
image: openebs/perf-test:latest
imagePullPolicy: IfNotPresent
env:

** storage mount point on which testfiles are created

- name: DBENCH_MOUNTPOINT
value: /data
```
## 测试 io 性能
```
kubectl delete pod hello-local-hostpath-pod

[root@k8s-10-6-162-31 ~]# kubectl create -f fio-deploy.yaml
job.batch/dbench-rmdqr created

[root@k8s-10-6-162-31 ~]# kubectl get pod
NAME READY STATUS RESTARTS AGE
dbench-rmdqr-qbl74 1/1 Running 0 4m59s
longhorn-iscsi-installation-2thd5 1/1 Running 1 54d
longhorn-iscsi-installation-ctqtg 1/1 Running 1 (52d ago) 54d
longhorn-iscsi-installation-mrm4h 1/1 Running 1 (52d ago) 54d

[root@k8s-10-6-162-31 ~]# kubectl logs -f dbench-729cw-nqfpt
Error from server (NotFound): pods "dbench-729cw-nqfpt" not found
[root@k8s-10-6-162-31 ~]# kubectl logs -f dbench-rmdqr-qbl74
Working dir: /data

Testing Read IOPS...
read_iops: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=64
fio-3.13
Starting 1 process
read_iops: Laying out IO file (1 file / 2048MiB)

read_iops: (groupid=0, jobs=1): err= 0: pid=17: Mon Feb 6 06:27:30 2023
read: IOPS=137, BW=566KiB/s (580kB/s)(8600KiB/15193msec)
bw ( KiB/s): min= 8, max= 1752, per=100.00%, avg=570.00, stdev=518.97, samples=29
iops : min= 2, max= 438, avg=142.41, stdev=129.78, samples=29
cpu : usr=0.22%, sys=1.13%, ctx=1984, majf=0, minf=16
IO depths : 1=0.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=100.0%
submit : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
complete : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
issued rwts: total=2087,0,0,0 short=0,0,0,0 dropped=0,0,0,0
latency : target=0, window=0, percentile=100.00%, depth=64

Run status group 0 (all jobs):
READ: bw=566KiB/s (580kB/s), 566KiB/s-566KiB/s (580kB/s-580kB/s), io=8600KiB (8806kB), run=15193-15193msec

Disk stats (read/write):
dm-0: ios=2475/39, merge=0/0, ticks=1076796/25702, in_queue=1114531, util=100.00%, aggrios=2494/51, aggrmerge=0/3, aggrticks=1094965/36042, aggrin_queue=1130703, aggrutil=99.98%
sda: ios=2494/51, merge=0/3, ticks=1094965/36042, in_queue=1130703, util=99.98%


Testing Write IOPS...
write_iops: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=64
fio-3.13
Starting 1 process

write_iops: (groupid=0, jobs=1): err= 0: pid=33: Mon Feb 6 06:27:49 2023
write: IOPS=199, BW=815KiB/s (835kB/s)(13.0MiB/16358msec); 0 zone resets
bw ( KiB/s): min= 40, max= 3408, per=100.00%, avg=871.87, stdev=932.70, samples=30
iops : min= 10, max= 852, avg=217.87, stdev=233.18, samples=30
cpu : usr=0.17%, sys=1.05%, ctx=958, majf=0, minf=16
IO depths : 1=0.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=100.0%
submit : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
complete : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
issued rwts: total=0,3271,0,0 short=0,0,0,0 dropped=0,0,0,0
latency : target=0, window=0, percentile=100.00%, depth=64

Run status group 0 (all jobs):
WRITE: bw=815KiB/s (835kB/s), 815KiB/s-815KiB/s (835kB/s-835kB/s), io=13.0MiB (13.7MB), run=16358-16358msec

Disk stats (read/write):
dm-0: ios=0/4802, merge=0/0, ticks=0/1128001, in_queue=1129209, util=99.50%, aggrios=0/4826, aggrmerge=0/4, aggrticks=0/1147779, aggrin_queue=1147776, aggrutil=99.41%
sda: ios=0/4826, merge=0/4, ticks=0/1147779, in_queue=1147776, util=99.41%


Testing Read Bandwidth...
read_bw: (g=0): rw=randread, bs=(R) 128KiB-128KiB, (W) 128KiB-128KiB, (T) 128KiB-128KiB, ioengine=libaio, iodepth=64
fio-3.13
Starting 1 process

read_bw: (groupid=0, jobs=1): err= 0: pid=49: Mon Feb 6 06:28:09 2023
read: IOPS=128, BW=16.5MiB/s (17.3MB/s)(280MiB/16965msec)
bw ( KiB/s): min= 256, max=50176, per=100.00%, avg=17994.26, stdev=14173.96, samples=31
iops : min= 2, max= 392, avg=140.48, stdev=110.71, samples=31
cpu : usr=0.18%, sys=1.66%, ctx=2092, majf=0, minf=16
IO depths : 1=0.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=100.0%
submit : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
complete : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
issued rwts: total=2180,0,0,0 short=0,0,0,0 dropped=0,0,0,0
latency : target=0, window=0, percentile=100.00%, depth=64

Run status group 0 (all jobs):
READ: bw=16.5MiB/s (17.3MB/s), 16.5MiB/s-16.5MiB/s (17.3MB/s-17.3MB/s), io=280MiB (294MB), run=16965-16965msec

Disk stats (read/write):
dm-0: ios=2366/3, merge=0/0, ticks=1093765/4077, in_queue=1100333, util=99.51%, aggrios=2366/6, aggrmerge=0/0, aggrticks=1096465/8183, aggrin_queue=1104639, aggrutil=99.42%
sda: ios=2366/6, merge=0/0, ticks=1096465/8183, in_queue=1104639, util=99.42%


Testing Write Bandwidth...
write_bw: (g=0): rw=randwrite, bs=(R) 128KiB-128KiB, (W) 128KiB-128KiB, (T) 128KiB-128KiB, ioengine=libaio, iodepth=64
fio-3.13
Starting 1 process

write_bw: (groupid=0, jobs=1): err= 0: pid=65: Mon Feb 6 06:28:27 2023
write: IOPS=69, BW=9453KiB/s (9680kB/s)(145MiB/15707msec); 0 zone resets
bw ( KiB/s): min= 256, max=29952, per=100.00%, avg=10800.19, stdev=9114.78, samples=26
iops : min= 2, max= 234, avg=84.35, stdev=71.20, samples=26
cpu : usr=0.15%, sys=0.67%, ctx=555, majf=0, minf=16
IO depths : 1=0.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=100.0%
submit : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
complete : 0=0.0%, 4=99.9%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
issued rwts: total=0,1097,0,0 short=0,0,0,0 dropped=0,0,0,0
latency : target=0, window=0, percentile=100.00%, depth=64

Run status group 0 (all jobs):
WRITE: bw=9453KiB/s (9680kB/s), 9453KiB/s-9453KiB/s (9680kB/s-9680kB/s), io=145MiB (152MB), run=15707-15707msec

Disk stats (read/write):
dm-0: ios=0/1499, merge=0/0, ticks=0/1047546, in_queue=1137554, util=99.39%, aggrios=0/1502, aggrmerge=0/3, aggrticks=0/1152415, aggrin_queue=1152412, aggrutil=99.25%
sda: ios=0/1502, merge=0/3, ticks=0/1152415, in_queue=1152412, util=99.25%


Testing Read Latency...
read_latency: (g=0): rw=randread, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=4
fio-3.13
Starting 1 process

read_latency: (groupid=0, jobs=1): err= 0: pid=81: Mon Feb 6 06:28:46 2023
read: IOPS=9, BW=39.7KiB/s (40.7kB/s)(652KiB/16407msec)
slat (usec): min=25, max=224, avg=106.02, stdev=36.24
clat (usec): min=165, max=3176.6k, avg=395710.97, stdev=707730.31
lat (usec): min=227, max=3176.7k, avg=395817.82, stdev=707732.74
clat percentiles (usec):
| 1.00th=[ 229], 5.00th=[ 2147], 10.00th=[ 10683],
| 20.00th=[ 23462], 30.00th=[ 35390], 40.00th=[ 57934],
| 50.00th=[ 91751], 60.00th=[ 145753], 70.00th=[ 263193],
| 80.00th=[ 505414], 90.00th=[1652556], 95.00th=[2021655],
| 99.00th=[3170894], 99.50th=[3170894], 99.90th=[3170894],
| 99.95th=[3170894], 99.99th=[3170894]
bw ( KiB/s): min= 7, max= 216, per=100.00%, avg=63.80, stdev=57.40, samples=20
iops : min= 1, max= 54, avg=15.80, stdev=14.41, samples=20
lat (usec) : 250=1.25%, 500=0.62%, 1000=1.25%
lat (msec) : 2=1.88%, 4=2.50%, 10=2.50%, 20=7.50%, 50=19.38%
lat (msec) : 100=16.25%, 250=18.12%, 500=10.00%, 750=6.25%, 1000=1.25%
cpu : usr=0.01%, sys=0.13%, ctx=162, majf=0, minf=17
IO depths : 1=0.0%, 2=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
submit : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
complete : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
issued rwts: total=160,0,0,0 short=0,0,0,0 dropped=0,0,0,0
latency : target=0, window=0, percentile=100.00%, depth=4

Run status group 0 (all jobs):
READ: bw=39.7KiB/s (40.7kB/s), 39.7KiB/s-39.7KiB/s (40.7kB/s-40.7kB/s), io=652KiB (668kB), run=16407-16407msec

Disk stats (read/write):
dm-0: ios=195/15, merge=0/0, ticks=62870/9094, in_queue=113278, util=99.51%, aggrios=195/22, aggrmerge=0/4, aggrticks=72364/49995, aggrin_queue=122359, aggrutil=99.49%
sda: ios=195/22, merge=0/4, ticks=72364/49995, in_queue=122359, util=99.49%


Testing Write Latency...
write_latency: (g=0): rw=randwrite, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=4
fio-3.13
Starting 1 process

write_latency: (groupid=0, jobs=1): err= 0: pid=97: Mon Feb 6 06:29:04 2023
write: IOPS=30, BW=123KiB/s (126kB/s)(1868KiB/15174msec); 0 zone resets
slat (usec): min=11, max=235, avg=58.23, stdev=38.98
clat (usec): min=205, max=2619.4k, avg=136822.73, stdev=357077.08
lat (usec): min=281, max=2619.5k, avg=136881.82, stdev=357079.12
clat percentiles (usec):
| 1.00th=[ 277], 5.00th=[ 383], 10.00th=[ 537],
| 20.00th=[ 10421], 30.00th=[ 17171], 40.00th=[ 23200],
| 50.00th=[ 32375], 60.00th=[ 44303], 70.00th=[ 68682],
| 80.00th=[ 92799], 90.00th=[ 274727], 95.00th=[ 784335],
| 99.00th=[1937769], 99.50th=[2365588], 99.90th=[2634023],
| 99.95th=[2634023], 99.99th=[2634023]
bw ( KiB/s): min= 7, max= 688, per=100.00%, avg=184.90, stdev=186.47, samples=20
iops : min= 1, max= 172, avg=46.00, stdev=46.69, samples=20
lat (usec) : 250=0.43%, 500=9.05%, 750=2.59%
lat (msec) : 2=0.86%, 4=1.29%, 10=5.82%, 20=15.73%, 50=26.72%
lat (msec) : 100=19.40%, 250=7.54%, 500=5.39%, 750=0.43%, 1000=1.29%
cpu : usr=0.06%, sys=0.20%, ctx=222, majf=0, minf=17
IO depths : 1=0.0%, 2=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
submit : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
complete : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
issued rwts: total=0,464,0,0 short=0,0,0,0 dropped=0,0,0,0
latency : target=0, window=0, percentile=100.00%, depth=4

Run status group 0 (all jobs):
WRITE: bw=123KiB/s (126kB/s), 123KiB/s-123KiB/s (126kB/s-126kB/s), io=1868KiB (1913kB), run=15174-15174msec

Disk stats (read/write):
dm-0: ios=0/475, merge=0/0, ticks=0/68658, in_queue=69443, util=99.48%, aggrios=0/475, aggrmerge=0/0, aggrticks=0/69983, aggrin_queue=69983, aggrutil=99.40%
sda: ios=0/475, merge=0/0, ticks=0/69983, in_queue=69983, util=99.40%


Testing Read Sequential Speed...
read_seq: (g=0): rw=read, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=16
fio-3.13
Starting 1 thread

read_seq: (groupid=0, jobs=1): err= 0: pid=113: Mon Feb 6 06:29:28 2023
read: IOPS=17, BW=17.8MiB/s (18.7MB/s)(358MiB/20078msec)
bw ( KiB/s): min= 2043, max=81920, per=100.00%, avg=24218.28, stdev=22785.58, samples=29
iops : min= 1, max= 80, avg=23.52, stdev=22.30, samples=29
cpu : usr=0.03%, sys=0.60%, ctx=351, majf=0, minf=0
IO depths : 1=0.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=100.0%, 32=0.0%, >=64=0.0%
submit : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
complete : 0=0.0%, 4=99.7%, 8=0.0%, 16=0.3%, 32=0.0%, 64=0.0%, >=64=0.0%
issued rwts: total=343,0,0,0 short=0,0,0,0 dropped=0,0,0,0
latency : target=0, window=0, percentile=100.00%, depth=16

Run status group 0 (all jobs):
READ: bw=17.8MiB/s (18.7MB/s), 17.8MiB/s-17.8MiB/s (18.7MB/s-18.7MB/s), io=358MiB (375MB), run=20078-20078msec

Disk stats (read/write):
dm-0: ios=764/10, merge=0/0, ticks=589803/16574, in_queue=609402, util=99.61%, aggrios=764/13, aggrmerge=0/1, aggrticks=592905/15938, aggrin_queue=608802, aggrutil=99.52%
sda: ios=764/13, merge=0/1, ticks=592905/15938, in_queue=608802, util=99.52%


Testing Write Sequential Speed...
write_seq: (g=0): rw=write, bs=(R) 1024KiB-1024KiB, (W) 1024KiB-1024KiB, (T) 1024KiB-1024KiB, ioengine=libaio, iodepth=16
...
fio-3.13
Starting 4 threads
write_seq: Laying out IO file (1 file / 2798MiB)

write_seq: (groupid=0, jobs=1): err= 0: pid=129: Mon Feb 6 06:29:59 2023
write: IOPS=5, BW=6679KiB/s (6839kB/s)(187MiB/28670msec); 0 zone resets
bw ( KiB/s): min= 2043, max=67449, per=59.42%, avg=16001.91, stdev=15698.61, samples=22
iops : min= 1, max= 65, avg=15.50, stdev=15.23, samples=22
cpu : usr=0.04%, sys=0.17%, ctx=149, majf=0, minf=0
IO depths : 1=0.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=100.0%, 32=0.0%, >=64=0.0%
submit : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
complete : 0=0.0%, 4=99.4%, 8=0.0%, 16=0.6%, 32=0.0%, 64=0.0%, >=64=0.0%
issued rwts: total=0,172,0,0 short=0,0,0,0 dropped=0,0,0,0
latency : target=0, window=0, percentile=100.00%, depth=16
write_seq: (groupid=0, jobs=1): err= 0: pid=130: Mon Feb 6 06:29:59 2023
write: IOPS=6, BW=6827KiB/s (6991kB/s)(189MiB/28350msec); 0 zone resets
bw ( KiB/s): min= 2048, max=57344, per=60.09%, avg=16183.05, stdev=15552.27, samples=21
iops : min= 2, max= 56, avg=15.67, stdev=15.15, samples=21
cpu : usr=0.04%, sys=0.18%, ctx=160, majf=0, minf=0
IO depths : 1=0.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=100.0%, 32=0.0%, >=64=0.0%
submit : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
complete : 0=0.0%, 4=99.4%, 8=0.0%, 16=0.6%, 32=0.0%, 64=0.0%, >=64=0.0%
issued rwts: total=0,174,0,0 short=0,0,0,0 dropped=0,0,0,0
latency : target=0, window=0, percentile=100.00%, depth=16
write_seq: (groupid=0, jobs=1): err= 0: pid=131: Mon Feb 6 06:29:59 2023
write: IOPS=6, BW=6932KiB/s (7098kB/s)(189MiB/27921msec); 0 zone resets
bw ( KiB/s): min= 2048, max=55185, per=75.56%, avg=20347.18, stdev=14701.69, samples=17
iops : min= 2, max= 53, avg=19.71, stdev=14.20, samples=17
cpu : usr=0.03%, sys=0.19%, ctx=163, majf=0, minf=0
IO depths : 1=0.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=100.0%, 32=0.0%, >=64=0.0%
submit : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
complete : 0=0.0%, 4=99.4%, 8=0.0%, 16=0.6%, 32=0.0%, 64=0.0%, >=64=0.0%
issued rwts: total=0,174,0,0 short=0,0,0,0 dropped=0,0,0,0
latency : target=0, window=0, percentile=100.00%, depth=16
write_seq: (groupid=0, jobs=1): err= 0: pid=132: Mon Feb 6 06:29:59 2023
write: IOPS=6, BW=6767KiB/s (6929kB/s)(189MiB/28600msec); 0 zone resets
bw ( KiB/s): min= 2048, max=67584, per=60.14%, avg=16196.64, stdev=15468.10, samples=22
iops : min= 2, max= 66, avg=15.73, stdev=15.17, samples=22
cpu : usr=0.04%, sys=0.19%, ctx=162, majf=0, minf=0
IO depths : 1=0.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=100.0%, 32=0.0%, >=64=0.0%
submit : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
complete : 0=0.0%, 4=99.4%, 8=0.0%, 16=0.6%, 32=0.0%, 64=0.0%, >=64=0.0%
issued rwts: total=0,174,0,0 short=0,0,0,0 dropped=0,0,0,0
latency : target=0, window=0, percentile=100.00%, depth=16

Run status group 0 (all jobs):
WRITE: bw=26.3MiB/s (27.6MB/s), 6679KiB/s-6932KiB/s (6839kB/s-7098kB/s), io=754MiB (791MB), run=27921-28670msec

Disk stats (read/write):
dm-0: ios=0/1536, merge=0/0, ticks=0/3438611, in_queue=3460488, util=99.70%, aggrios=0/1553, aggrmerge=0/0, aggrticks=0/3505870, aggrin_queue=3506177, aggrutil=99.72%
sda: ios=0/1553, merge=0/0, ticks=0/3505870, in_queue=3506177, util=99.72%


Testing Read/Write Mixed...
rw_mix: (g=0): rw=randrw, bs=(R) 4096B-4096B, (W) 4096B-4096B, (T) 4096B-4096B, ioengine=libaio, iodepth=64
fio-3.13
Starting 1 process

rw_mix: (groupid=0, jobs=1): err= 0: pid=148: Mon Feb 6 06:30:22 2023
read: IOPS=294, BW=1185KiB/s (1214kB/s)(23.5MiB/20301msec)
bw ( KiB/s): min= 24, max=10088, per=100.00%, avg=2173.91, stdev=2974.57, samples=22
iops : min= 6, max= 2522, avg=543.41, stdev=743.66, samples=22
write: IOPS=93, BW=377KiB/s (386kB/s)(7656KiB/20301msec); 0 zone resets
bw ( KiB/s): min= 8, max= 3000, per=100.00%, avg=754.55, stdev=998.04, samples=20
iops : min= 2, max= 750, avg=188.60, stdev=249.52, samples=20
cpu : usr=0.25%, sys=1.12%, ctx=2198, majf=0, minf=16
IO depths : 1=0.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=100.0%
submit : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
complete : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.1%, >=64=0.0%
issued rwts: total=5971,1896,0,0 short=0,0,0,0 dropped=0,0,0,0
latency : target=0, window=0, percentile=100.00%, depth=64

Run status group 0 (all jobs):
READ: bw=1185KiB/s (1214kB/s), 1185KiB/s-1185KiB/s (1214kB/s-1214kB/s), io=23.5MiB (24.6MB), run=20301-20301msec
WRITE: bw=377KiB/s (386kB/s), 377KiB/s-377KiB/s (386kB/s-386kB/s), io=7656KiB (7840kB), run=20301-20301msec

Disk stats (read/write):
dm-0: ios=2926/2535, merge=0/0, ticks=676178/621959, in_queue=1332944, util=99.60%, aggrios=2926/2630, aggrmerge=0/21, aggrticks=676172/1200603, aggrin_queue=1875954, aggrutil=100.00%
sda: ios=2926/2630, merge=0/21, ticks=676172/1200603, in_queue=1875954, util=100.00%


All tests complete.

==================
= Dbench Summary =
==================
Random Read/Write IOPS: 137/199. BW: 16.5MiB/s / 9453KiB/s
Average Latency (usec) Read/Write: 395817.82/136881.82
Sequential Read/Write: 17.8MiB/s / 26.3MiB/s
Mixed Random Read/Write IOPS: 294/93
```

