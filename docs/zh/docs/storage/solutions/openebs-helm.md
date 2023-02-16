# 通过 Helm 部署并验证 OpenEBS

本文将提供用 Helm 部署并验证 OpenEBS 云原生存储系统的操作步骤及说明。DCE 5.0 支持众多第三方存储方案，我们针对 OpenEBS 进行了相关测试，并最终将其作为 Addon 集成了应用商店中。 以下是对 OpenEBS 的调研和测评。

有关应用商店 Addon 的图形化界面安装、部署、卸载等操作说明，将于稍后提供。

## 测试环境

本次测试使用三个虚拟机节点部署一个Kubernetes集群：1个 Master + 2个 Worker 节点，kubelet版本为1.23.6。
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


