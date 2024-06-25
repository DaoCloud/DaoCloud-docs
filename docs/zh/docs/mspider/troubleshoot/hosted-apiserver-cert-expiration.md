# 托管网格 APIServer 证书过期处理办法

## 问题现象

为了安全起见，托管网格的证书的有效期仅为一年，我们需要定期重新生成证书以确保集群服务正常。

如果在界面发现网格状态异常，且查看控制面集群的 hosted-apiserver 日志，有类似 `x509：certificate has expired or is not yet valid` ，或者收到 `MspiderHostedKubeAPICertExpiration` 的告警，表示证书已过期或即将过期，需要更换。

## 影响范围

证书过期不会影响业务正常运行，但是会影响策略下发、应用新建或重启等操作，需要及时更换。

## 修复方案

对于已经安装的网格，我们需要手动处理证书更新的过程。

首先，根据下面的 yaml，替换其中所有的 `MESH_ID` 为网格 ID（界面上的名字，如 hosted-demo）

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: MESH_ID-hosted-apiserver-certs-renew
  namespace: istio-system
spec:
  parallelism: 1
  completions: 1
  template:
    spec:     
      serviceAccountName: mspider-mcpc
      restartPolicy: Never
      volumes:
        - name: etcd-certs
          secret:
            secretName: MESH_ID-etcd-certs
        - name: kube-certs
          secret:
            secretName: MESH_ID-kube-certs
      containers:
        - name: init-certs
          image: release.daocloud.io/mspider/self-hosted-apiserver:0.0.13
          imagePullPolicy: IfNotPresent
          env:
            - name: MESH_ID
              value: MESH_ID
            - name: KUBE_CERT_SECRET
              value: MESH_ID-kube-certs
            - name: ETCD_CERT_SECRET
              value: MESH_ID-etcd-certs
            - name: KUBECONFIG_SECRET
              value: MESH_ID-apiserver-admin-kubeconfig
            - name: EXT_SANS
              value: MESH_ID-hosted-apiserver,MESH_ID-hosted-apiserver.istio-system,MESH_ID-hosted-apiserver.istio-system.svc,MESH_ID-hosted-apiserver.istio-system.svc.cluster.local
          command:
          - bash
          - -c
          volumeMounts:
            - name: etcd-certs
              mountPath: /etc/kubernetes/pki/etcd
            - name: kube-certs
              mountPath: /etc/kubernetes/pki
          args:
          - |-
            set -ex
            cd /etc/kubernetes/pki
            if [ ! -f ca.crt ]; then
              echo "ca.crt not found"
              exit 1
            fi
            d=$(mktemp -d)
            cp -Lrf /etc/kubernetes/pki/* ${d}
            cd ${d}
            # renew certs
            kubeadm  certs renew all --cert-dir ${d}
            files=$(for a in $(find . -maxdepth 1 -type f); do echo -n " --from-file $a "; done)
            cat > /tmp/secret-patch.json <<EOF
            {"data": $(kubectl create secret generic ${KUBE_CERT_SECRET} ${files} --dry-run -o jsonpath='{.data}')}
            EOF
            kubectl patch secrets ${KUBE_CERT_SECRET} --type merge --patch-file /tmp/secret-patch.json
             
            files=$(for a in $(find etcd -maxdepth 1 -type f); do echo -n " --from-file $a "; done)
            cat > /tmp/secret-patch.json <<EOF
            {"data": $(kubectl create secret generic ${ETCD_CERT_SECRET} ${files} --dry-run -o jsonpath='{.data}')}
            EOF
            kubectl patch secrets ${ETCD_CERT_SECRET} --type merge --patch-file /tmp/secret-patch.json
             
            kubeadm init phase kubeconfig admin --cert-dir ${d} --kubeconfig-dir ${d}
            cp admin.conf config
            sed -i 's#server: .*#server: https://MESH_ID-hosted-apiserver:6443#g' config
            cat > /tmp/secret-patch.json <<EOF
            {"data": $(kubectl create secret generic ${KUBECONFIG_SECRET} --from-file config --dry-run -o jsonpath='{.data}')}
            EOF
            kubectl patch secrets ${KUBECONFIG_SECRET} --type merge --patch-file /tmp/secret-patch.json
```

其次，在托管网格控制面集群（可在网格列表中查看）中，创建这个 Job，等待执行成功。
成功后需要重启 istio-system 命名空间下的 istiod, hosted-apiserver, etcd, ckube-remote 组件。

**重启这些组件不会影响业务正常服务。**

## 验证

- 界面网格状态。
- 删除创建网格相关资源能够正常工作。
