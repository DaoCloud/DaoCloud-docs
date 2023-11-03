# Deploy Longhorn via App Store

This page will provide the operation steps and instructions for deploying the Longhorn cloud native storage system in the DCE 5.0 app store with the Addon graphical interface.

## Format conversion of Longhorn helm charts

### Add repo

```
[root@k8s-10-6-162-31 ~]# helm search repo longhorn
NAME CHART VERSION APP VERSION DESCRIPTION
longhorn/longhorn 1.3.2 v1.3.2 Longhorn is a distributed block storage system ...
```

### Pull and unzip Longhorn helm charts

```
[root@k8s-10-6-162-31 ~]# helm pull longhorn/longhorn
[root@k8s-10-6-162-31 ~]# ls
anaconda-ks.cfg calico.yaml helm-v3.10.1-linux-amd64.tar.gz linux-amd64 longhorn-1.3.2.tgz rook rook-ceph-image rook-ceph-image.zip

[root@k8s-10-6-162-31 ~]# tar xvfz longhorn-1.3.2.tgz
longhorn/Chart.yaml
longhorn/values.yaml
longhorn/templates/NOTES.txt
longhorn/templates/_helpers.tpl
longhorn/templates/clusterrole.yaml
longhorn/templates/clusterrolebinding.yaml
longhorn/templates/crds.yaml
longhorn/templates/daemonset-sa.yaml
longhorn/templates/default-setting.yaml
longhorn/templates/deployment-driver.yaml
longhorn/templates/deployment-ui.yaml
longhorn/templates/deployment-webhook.yaml
longhorn/templates/ingress.yaml
longhorn/templates/postupgrade-job.yaml
longhorn/templates/psp.yaml
longhorn/templates/registry-secret.yaml
longhorn/templates/serviceaccount.yaml
longhorn/templates/services.yaml
longhorn/templates/storageclass.yaml
longhorn/templates/tls-secrets.yaml
longhorn/templates/uninstall-job.yaml
longhorn/.helmignore
longhorn/README.md
longhorn/app-readme.md
longhorn/questions.yaml

[root@k8s-10-6-162-31 ~]# cd longhorn
[root@k8s-10-6-162-31 longhorn]# ls
app-readme.md Chart.yaml questions.yaml README.md templates values.yaml
```

### Replace Longhorn values.yaml with json

```
[root@k8s-10-6-162-31 ~]# helm plugin install https://github.com/karuppiah7890/helm-schema-gen.git
karuppiah7890/helm-schema-gen info checking GitHub for tag '0.0.4'
karuppiah7890/helm-schema-gen info found version: 0.0.4 for 0.0.4/Linux/x86_64
karuppiah7890/helm-schema-gen info installed ./bin/helm-schema-gen
Installed plugin: schema-gen
[root@k8s-10-6-162-31 longhorn]# helm schema-gen values.yaml > values.schema.json
[root@k8s-10-6-162-31 longhorn]# ls
app-readme.md Chart.yaml questions.yaml README.md templates values.schema.json values.yaml
```

### Pack and zip charts with json files

```
[root@k8s-10-6-162-31 longhorn]# cd ..
[root@k8s-10-6-162-31 ~]# ls
anaconda-ks.cfg helm-v3.10.1-linux-amd64.tar.gz longhorn rook rook-ceph-image.zip
calico.yaml linux-amd64 longhorn-1.3.2.tgz rook-ceph-image values.schema.json
[root@k8s-10-6-162-31 ~]# tar zcvf longhorn-v1.3.2.tgz longhorn
longhorn/
longhorn/Chart.yaml
longhorn/values.yaml
longhorn/templates/
longhorn/templates/NOTES.txt
longhorn/templates/_helpers.tpl
longhorn/templates/clusterrole.yaml
longhorn/templates/clusterrolebinding.yaml
longhorn/templates/crds.yaml
longhorn/templates/daemonset-sa.yaml
longhorn/templates/default-setting.yaml
longhorn/templates/deployment-driver.yaml
longhorn/templates/deployment-ui.yaml
longhorn/templates/deployment-webhook.yaml
longhorn/templates/ingress.yaml
longhorn/templates/postupgrade-job.yaml
longhorn/templates/psp.yaml
longhorn/templates/registry-secret.yaml
longhorn/templates/serviceaccount.yaml
longhorn/templates/services.yaml
longhorn/templates/storageclass.yaml
longhorn/templates/tls-secrets.yaml
longhorn/templates/uninstall-job.yaml
longhorn/.helmignore
longhorn/README.md
longhorn/app-readme.md
longhorn/questions.yaml
longhorn/values.schema.json
[root@k8s-10-6-162-31 ~]# ls
anaconda-ks.cfg helm-v3.10.1-linux-amd64.tar.gz longhorn longhorn-v1.3.2.tgz rook-ceph-image values.schema.json
calico.yaml linux-amd64 longhorn-1.3.2.tgz rook rook-ceph-image.zip
```

## Upload the chart package to DCE 5.0 registry






## Install Longhorn via DCE 5.0 App Store



```
[root@k8s-10-6-162-31 ~]# kubectl get po -n longhorn-system
NAME READY STATUS RESTARTS AGE
csi-attacher-7bf4b7f996-7g2h6 1/1 Running 0 3h13m
csi-attacher-7bf4b7f996-d996x 1/1 Running 1 (108m ago) 3h13m
csi-attacher-7bf4b7f996-nxwcw 1/1 Running 0 3h13m
csi-provisioner-869bdc4b79-4xgbs 1/1 Running 1 (108m ago) 3h13m
csi-provisioner-869bdc4b79-8bjb5 1/1 Running 0 3h13m
csi-provisioner-869bdc4b79-zmqkp 1/1 Running 0 3h13m
csi-resizer-6d8cf5f99f-lfvhq 1/1 Running 1 (108m ago) 3h13m
csi-resizer-6d8cf5f99f-lzkd4 1/1 Running 0 3h13m
csi-resizer-6d8cf5f99f-zcd6g 1/1 Running 0 3h13m
csi-snapshotter-588457fcdf-crddw 1/1 Running 1 (108m ago) 3h13m
csi-snapshotter-588457fcdf-qnghk 1/1 Running 0 3h13m
csi-snapshotter-588457fcdf-xbl4q 1/1 Running 0 3h13m
engine-image-ei-a5371358-qtbzf 1/1 Running 0 3h14m
engine-image-ei-a5371358-sgrkv 1/1 Running 0 3h14m
engine-image-ei-a5371358-t8gd6 1/1 Running 0 3h14m
helm-operation-install-longhorn-deploy-jf5rm-hdx82 0/1 Completed 0 3h20m
instance-manager-e-2894727b 1/1 Running 0 3h14m
instance-manager-e-c285811f 1/1 Running 0 3h14m
instance-manager-e-c33ef405 1/1 Running 0 3h14m
instance-manager-r-5eed6e09 1/1 Running 0 3h14m
instance-manager-r-7aea1541 1/1 Running 0 3h14m
instance-manager-r-832995c5 1/1 Running 0 3h14m
longhorn-admission-webhook-84dbdf4b-7k9pf 1/1 Running 0 3h20m
longhorn-admission-webhook-84dbdf4b-w9xjz 1/1 Running 0 3h20m
longhorn-conversion-webhook-77f447c97b-fj52b 1/1 Running 0 3h20m
longhorn-conversion-webhook-77f447c97b-fxqck 1/1 Running 0 3h20m
longhorn-csi-plugin-mvwwd 2/2 Running 0 3h13m
longhorn-csi-plugin-nj6pg 2/2 Running 0 3h13m
longhorn-csi-plugin-t8smg 2/2 Running 0 3h13m
longhorn-driver-deployer-7cd5cfcd64-lsjnm 1/1 Running 0 3h20m
longhorn-manager-lwrxj 1/1 Running 0 3h20m
longhorn-manager-x7vgm 1/1 Running 0 3h20m
longhorn-manager-xsn8k 1/1 Running 1 (3h14m ago) 3h20m
longhorn-ui-68bc57db67-46brf 1/1 Running 0 3h20m
```

Modify the Longhorn front-end service port:





Get access to the Longhorn UI:

![longhorn ui](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/longhorn-1.png)

![longhorn ui](https://docs.daocloud.io/daocloud-docs-images/docs/storage/images/longhorn-2.png)

So far, the Longhorn storage system has been successfully deployed in the DCE 5.0 app store!
