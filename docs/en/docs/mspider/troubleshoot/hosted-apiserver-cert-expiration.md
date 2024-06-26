# Handling Expired Certificates for Hosted Mesh APIServer

## Problem Description

For security reasons, the certificates for the hosted mesh are valid for only one year. We need to periodically regenerate these certificates to ensure that the cluster services operate normally.

If you notice an abnormal mesh status on the interface and see logs in the hosted-apiserver of the control plane cluster with messages similar to the following:

```info
x509: certificate has expired or is not yet valid
MspiderHostedKubeAPICertExpiration
```

It indicates that the certificate has expired or is about to expire and needs to be replaced.

## Impact Scope

Certificate expiration will not affect normal business operations but will impact policy issuance, application creation, or restart operations. Therefore, timely replacement is necessary.

## Solution

For an already installed mesh, we need to manually handle the certificate update process.

First, replace all instances of `MESH_ID` in the following YAML with the mesh ID (the name on the interface, such as hosted-demo).

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

Next, in the control plane cluster of the hosted mesh (which can be viewed in the mesh list),
create this Job and wait for it to execute successfully. After successful execution,
you need to restart the istiod, hosted-apiserver, etcd, and ckube-remote components in the istio-system namespace.

**Restarting these components will not affect normal business services.**

## Verification

- Check the mesh status on the interface.
- Ensure that deleting and creating mesh-related resources work properly.