---
hide:
  - toc
---

# 第三方工作负载使用 IP 池

本本章节主要介绍结合 Spiderpool 及 Multus CR 管理，为自定义工作负载（本文采用 [OpenKruise](https://github.com/openkruise/kruise) 控制器 创建的工作负载 CloneSet） Pod 配置 IP Pool，通过 Spiderpool 进行 Underlay 网络的 IP 的分配和固定。

## 前提条件

1. [SpiderPool 已成功部署](../../modules/spiderpool/install.md)。

2. 如使用手动选择 IP 池，请提前完成[创建 IP 子网和 IP 池](../../modules/spiderpool/createpool.md)。本示例中需要使用固定 IP 池，请提前完成[创建 固定 IP 池](../../modules/spiderpool/createpool.md)。

## 操作步骤

### 使用已创建固定 IP 池

1. 部署自定义资源 `CloneSet`，并在 `Annotation` 中指定默认网络类型，VLAN ID ，子网接口，IP 池信息

    ```
    v1.multus-cni.io/default-network: kube-system/calico
    k8s.v1.cni.cncf.io/networks: kube-system/vlan6
    ipam.spidernet.io/ippools: '[{"interface":"net1","ipv4":["ippool01"]}]'
    ```

    ```
    apiVersion: apps.kruise.io/v1alpha1
    kind: CloneSet
    metadata:
      name: custom-kruise-cloneset
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: custom-kruise-cloneset
      template:
        metadata:
          annotations:
            v1.multus-cni.io/default-network: "kube-system/calico"
            k8s.v1.cni.cncf.io/networks: "kube-system/vlan6"
            ipam.spidernet.io/ippool: |-
              {
                "interface":"net1", "ipv4":["ippool01"]
              }
          labels:
            app: custom-kruise-cloneset
        spec:
          containers:
          - name: custom-kruise-cloneset
            image: busybox
            imagePullPolicy: IfNotPresent
            command: ["/bin/sh", "-c", "trap : TERM INT; sleep infinity & wait"]
    ```

    

2. 部署后，查看 CloneSet 状态

    ```
    kubectl get pods -A|grep kruise-clone
    default            custom-kruise-cloneset-jkqtx                                      1/1     Running             0                  44h
    default            custom-kruise-cloneset-v5qz7                                      1/1     Running        0                  44h
    default            custom-kruise-cloneset-xhtq6                                      1/1     Running
    0                  44h
    ```

3. 进入`容器平台`-->选择对应集群-->点击`容器网络`，然后找到对应子网-->进入子网详情， 查看 IP 使用情况：

    ​![openkruise](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/openkruise.jpg)



### 自动创建固定 IP 池

1. 如需要使用子网自动创建固定 IP 池，请在创建 自定义工作负载时，添加如下 Annotation:

    ```
    apiVersion: apps.kruise.io/v1alpha1
    kind: CloneSet
    metadata:
      name: custom-kruise-cloneset03
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: custom-kruise-cloneset03
      template:
        metadata:
          annotations:
            v1.multus-cni.io/default-network: "kube-system/calico" # 指定默认容器网卡
            k8s.v1.cni.cncf.io/networks: "kube-system/vlan6" #指定Multus CRD 实例（NetworkAttachmentDefinition）
            ipam.spidernet.io/subnet: |-   #指定使用固定 IP 池的网卡及待使用子网
              {"interface":"net1","ipv4": ["subnet124"]}
            ipam.spidernet.io/ippool-ip-number: "1" #指定弹性 IP 数量，可使用 IP 数=弹性 IP 数+Replica 数
          labels:
            app: custom-kruise-cloneset03
        spec:
          containers:
          - name: custom-kruise-cloneset03
            image: busybox
            imagePullPolicy: IfNotPresent
            command: ["/bin/sh", "-c", "trap : TERM INT; sleep infinity & wait"]
    ```

2. 部署后查看 Clonset 状态：

    ```
    kubectl get pods -A|grep kruise-clone03
    ```

3. 查看 IP Pool IP 状态：

    ```
    
    kubectl get sp -oyaml | grep kruise
          ipam.spidernet.io/application: apps.kruise.io/v1alpha1:CloneSet:default:custom-kruise-cloneset03
        name: auto-custom-kruise-cloneset03-v4-net1-f3114156804d
        allocatedIPs: '{"10.6.124.200":{"interface":"net1","pod":"default/custom-kruise-cloneset-r7xjd","podUid":"43942169-3c43-4a81-aaae-60ba1dc9d07e"},"10.6.124.201":{"interface":"net1","pod":"default/custom-kruise-cloneset-sp5t6","podUid":"4980a045-7ee9-467a-a6a3-b259411963cb"},"10.6.124.202":{"interface":"net1","pod":"default/custom-kruise-cloneset-j94tl","podUid":"72b13a85-5275-44b1-8491-323f9fff3571"}}'   
    ```
