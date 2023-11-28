---
hide:
- toc
---

# 使用说明

本页介绍如何使用 Submariner 实现跨集群通讯。

!!! note

    当集群的 CNI 为 Calico 时，由于 Calico 插入的 IPTables 规则优先级高于 Submariner 插入的 IPTables 规则，导致跨集群通讯出现问题。
    所以我们必须手动配置 Calico 的 IPPool 来规避这个问题。

比如：

|Cluster|Pod CIDR|Service CIDR|
|---|---|---|
|A|10.244.64.0/18|10.244.0.0/18
|B|10.245.64.0/18|10.245.0.0/18

在 Cluster A：

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

在 Cluster B 执行同样操作：

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

> 应设置 natOutgoing 为 false。

## 使用

使用 Subctl 工具导出 Service，验证并排查问题。

1. 下载 Subctl

    ```shell
    root@controller:~# curl -Ls https://get.submariner.io | bash
    root@controller:~# export PATH=$PATH:~/.local/bin
    root@controller:~# echo export PATH=\$PATH:~/.local/bin >> ~/.profile
    root@controller:~# subctl version
    version: v0.13.4
    ```

1. 验证 Submariner 是否就绪：

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

1. 如果出现跨集群通讯失败，可以使用以下命令排查：

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

如果上面方式不能解决，通过以下方式收集当前环境所有信息：

```shell
root@controller:~# subctl gather
```

- 跨集群的服务发现：

    如果你想使用跨集群的服务发现，你需要手动导出 Service 到其他集群，可以参考下面的方式：

    在 ClusterA 导出这个服务：

    ```shell
    root@controller:~# kubectl get svc
    NAME                                          TYPE           CLUSTER-IP      EXTERNAL-IP    PORT(S)        AGE
    kubernetes                                    ClusterIP      10.233.0.1      <none>         443/TCP        81d                                       ClusterIP      10.233.35.64    <none>         80/TCP         58d
    test                                          ClusterIP      10.233.21.143   <none>         80/TCP         79d
    root@controller:~# subctl export service test
    ```

    上面命令将会导出 default 命令空间下一个名为 test 的 Service，导出完成之后查看状态：

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

    显示导出成功, 即可在 ClusterB 访问这个 Service：

    ```shell
    root@controller-node-1:~# kubectl  exec -it dao2048-5745d9b5d7-bsjjl sh
    kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
    / # nslookup test.default.svc.clusterset.local
    Server:		10.233.0.3
    Address:	10.233.0.3:53

    Name:	test.default.svc.clusterset.local
    Address: 10.233.21.143
    ```
