---
MTPE: windsonsea
Date: 2024-01-18
---

# Usage Notes

This page introduces how to use Submariner to enable cross-cluster communication.

!!! note

    When the CNI of the cluster is Calico, the IPTables rule inserted by Calico has a higher priority than the IPTables rule inserted by Submariner. As a result, cross-cluster communication fails. So we had to manually configure Calico's IPPool to get around this problem:

For example:

|Cluster|Pod CIDR|Service CIDR|
|---|---|---|
18 | | A | 10.244.64.0/10.244.0.0/18
18 | | B | 10.245.64.0/10.245.0.0/18

In Cluster A:

```shell
cat > clusterb-cidr.yaml <<EOF
  apiVersion: projectcalico.org/v3
  kind: IPPool
  metadata:
    name: clusterB-pod-cidr
  spec:
    cidr: 10.245.64.0/18
    natOutgoing: false
    disabled: true
EOF

cat > podwestcluster.yaml <<EOF
    apiVersion: projectcalico.org/v3
    kind: IPPool
    metadata:
      name: clusterB-service-cidr
    spec:
      cidr: 10.245.0.0/18
      natOutgoing: false
      disabled: true
EOF
```

Do the same operations in Cluster B:

```shell
cat > clusterb-cidr.yaml <<EOF
  apiVersion: projectcalico.org/v3
  kind: IPPool
  metadata:
    name: clusterA-pod-cidr
  spec:
    cidr: 10.244.64.0/18
    natOutgoing: false
    disabled: true
EOF

cat > podwestcluster.yaml <<EOF
  apiVersion: projectcalico.org/v3
  kind: IPPool
  metadata:
    name: clusterA-service-cidr
  spec:
    cidr: 10.244.0.0/18
    natOutgoing: false
    disabled: true
EOF
```

> `natOutgoing` should be set to `false`.

## Use Submariner

### Subctl

Use Subctl to export Service as well as verify and troubleshoot problems.

1. Download Subctl:

    ```shell
    root@controller:~# curl -Ls https://get.submariner.io | bash
    root@controller:~# export PATH=$PATH:~/.local/bin
    root@controller:~# echo export PATH=\$PATH:~/.local/bin >> ~/.profile
    root@controller:~# subctl version
    version: v0.13.4
    ```

1. Verify that Submariner is ready:

    ```shell
    root@controller:~# subctl show all
    Cluster "cluster.local"
    ✓ Detecting broker(s)
    ✓ No brokers found

    ✓ Showing Connections
    GATEWAY            CLUSTER   REMOTE IP    NAT  CABLE DRIVER  SUBNETS        STATUS     RTT avg.
    controller-node-1  cluster2  10.6.212.10  no   libreswan     244.1.10.0/24  connected  985.269µs

    ✓ Showing Endpoints
    CLUSTER ID                    ENDPOINT IP     PUBLIC IP       CABLE DRIVER        TYPE
    cluster1                      10.6.212.101    47.243.194.240  libreswan           local
    cluster2                      10.6.212.10     47.243.194.240  libreswan           remote

    ✓ Showing Gateways
    NODE                            HA STATUS       SUMMARY
    controller                      active          All connections (1) are established

    ✓ Showing Network details
        Discovered network details via Submariner:
            Network plugin:  calico
            Service CIDRs:   [10.233.0.0/18]
            Cluster CIDRs:   [10.233.64.0/18]
            Global CIDR:     244.0.10.0/24

    ✓ Showing versions
    COMPONENT                       REPOSITORY                                            VERSION
    submariner                      quay.m.daocloud.io/submariner                         0.14.0
    submariner-operator             quay.m.daocloud.io/submariner                         0.14.0
    service-discovery               quay.m.daocloud.io/submariner                         0.14.0
    ```

1. If cross-cluster communication fails, run the following command to troubleshoot:

    ```shell
    root@controller:~# subctl diagnose all
    Cluster "cluster.local"
    ✓ Checking Submariner support for the Kubernetes version
    ✓ Kubernetes version "v1.25.0" is supported

    ✓ Checking Submariner support for the CNI network plugin
    ✓ The detected CNI network plugin ("calico") is supported
    ✓ Trying to detect the Calico ConfigMap
    ✓ Calico CNI detected, checking if the Submariner IPPool pre-requisites are configured

    ✓ Checking gateway connections
    ✓ All connections are established

    ✓ Globalnet deployment detected - checking if globalnet CIDRs overlap
    ✓ Clusters do not have overlapping globalnet CIDRs
    ⚠ Pod "submariner-gateway-x2x48" has restarted 14 times
    ⚠ Pod "submariner-globalnet-fv7x9" has restarted 9 times

    ⚠ Starting with Kubernetes 1.23, the Pod Security admission controller expects namespaces to have security labels. Without these, you will see warnings in subctl's output. subctl should work fine, but you can avoid the warnings and ensure correct behavior by adding at least one of these labels to the namespace "submariner-operator":
      pod-security.kubernetes.io/warn=privileged
      pod-security.kubernetes.io/enforce=privileged
      pod-security.kubernetes.io/audit=privileged

    ✓ Checking Submariner support for the kube-proxy mode
    ✓ The kube-proxy mode is supported

    ⚠ Starting with Kubernetes 1.23, the Pod Security admission controller expects namespaces to have security labels. Without these, you will see warnings in subctl's output. subctl should work fine, but you can avoid the warnings and ensure correct behavior by adding at least one of these labels to the namespace "submariner-operator":
      pod-security.kubernetes.io/enforce=privileged
      pod-security.kubernetes.io/audit=privileged
      pod-security.kubernetes.io/warn=privileged

    ⢀⡱ Checking the firewall configuration to determine if the metrics port (8080) is allowed  ⚠ Starting with Kubernetes 1.23, the Pod Security admission controller expects namespaces to have security labels. Without these, you will see warnings in subctl's output. subctl should work fine, but you can avoid the warnings and ensure correct behavior by adding at least one of these labels to the namespace "submariner-operator":
      pod-security.kubernetes.io/audit=privileged
      pod-security.kubernetes.io/warn=privileged
      pod-security.kubernetes.io/enforce=privileged

    ✓ Checking the firewall configuration to determine if the metrics port (8080) is allowed
    ✓ The firewall configuration allows metrics to be retrieved from Gateway nodes

    ⚠ Starting with Kubernetes 1.23, the Pod Security admission controller expects namespaces to have security labels. Without these, you will see warnings in subctl's output. subctl should work fine, but you can avoid the warnings and ensure correct behavior by adding at least one of these labels to the namespace "submariner-operator":
      pod-security.kubernetes.io/enforce=privileged
      pod-security.kubernetes.io/audit=privileged
      pod-security.kubernetes.io/warn=privileged

    ⢀⡱ Checking the firewall configuration to determine if intra-cluster VXLAN traffic is allowed  ⚠ Starting with Kubernetes 1.23, the Pod Security admission controller expects namespaces to have security labels. Without these, you will see warnings in subctl's output. subctl should work fine, but you can avoid the warnings and ensure correct behavior by adding at least one of these labels to the namespace "submariner-operator":
      pod-security.kubernetes.io/warn=privileged
      pod-security.kubernetes.io/enforce=privileged
      pod-security.kubernetes.io/audit=privileged

    ✓ Checking Globalnet configuration
    ✓ Globalnet is properly configured and functioning

    Skipping inter-cluster firewall check as it requires two kubeconfigs. Please run "subctl diagnose firewall inter-cluster" command manually.
    ```

If the preceding methods fail, collect all information about the current environment in the following ways:

```shell
root@controller:~# subctl gather
```

### Service discovery

Service discovery across clusters:

If you want to use cross-cluster Service discovery, you need to manually export Services to other clusters, as shown in the following way:

Export this Service at ClusterA:

```shell
root@controller:~# kubectl get svc
NAME                                          TYPE           CLUSTER-IP      EXTERNAL-IP    PORT(S)        AGE
kubernetes                                    ClusterIP      10.233.0.1      <none>         443/TCP        81d                                       ClusterIP      10.233.35.64    <none>         80/TCP         58d
test                                          ClusterIP      10.233.21.143   <none>         80/TCP         79d
root@controller:~# subctl export service test
```

The above command will export a Service named `test` in the default namespace. After the export is complete, check the status:

```shell
root@controller:~# kubectl get serviceexports.multicluster.x-k8s.io
NAME   AGE
test   2d2h
root@controller:~# kubectl get serviceexports.multicluster.x-k8s.io test -o yaml
apiVersion: multicluster.x-k8s.io/v1alpha1
kind: ServiceExport
metadata:
  creationTimestamp: "2023-02-24T03:58:00Z"
  generation: 1
  name: test
  namespace: default
  resourceVersion: "20068131"
  uid: 05fa2aab-e6b1-491b-92bb-4f2561c92a1b
status:
  conditions:
  - lastTransitionTime: "2023-02-24T03:55:12Z"
    message: ""
    reason: ""
    status: "True"
    type: Valid
  - lastTransitionTime: "2023-02-24T03:55:12Z"
    message: ServiceImport was successfully synced to the broker
    reason: ""
    status: "True"
    type: Synced
```

If the export is successful, you can access the Service in ClusterB:

```shell
root@controller-node-1:~# kubectl  exec -it dao2048-5745d9b5d7-bsjjl sh
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
/ # nslookup test.default.svc.clusterset.local
Server:		10.233.0.3
Address:	10.233.0.3:53

Name:	test.default.svc.clusterset.local
Address: 10.233.21.143
```
