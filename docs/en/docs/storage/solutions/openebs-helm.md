# Deploy and verify OpenEBS via Helm

This page will provide the steps and instructions for deploying and verifying the OpenEBS cloud native storage system with Helm.
DCE 5.0 supports many third-party storage solutions. We tested OpenEBS and finally integrated it in the app store as an Addon. The following is the research and evaluation of OpenEBS.

Instructions for installing, deploying, and uninstalling the graphical interface of the App Store Addon will be provided later.

## Test environment

This test uses three virtual machine nodes to deploy a Kubernetes cluster: 1 Master + 2 Worker nodes, and the kubelet version is 1.23.6.

```
[root@k8s-10-6-162-31 ~]# kubectl get no
NAME              STATUS   ROLES                  AGE    VERSION
k8s-10-6-162-31   Ready    control-plane,master   114d   v1.23.6
k8s-10-6-162-32   Ready    <none>                 114d   v1.23.6
k8s-10-6-162-33   Ready    <none>                 114d   v1.23.6
```

## Add and update OpenEBS repo

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

## Install OpenEBS via helm

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
