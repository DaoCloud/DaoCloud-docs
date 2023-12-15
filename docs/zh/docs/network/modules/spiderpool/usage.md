---
hide:
  - toc
---

# 工作负载使用 IP 池

本章节主要介绍结合 Spiderpool 及 Multus CR 管理，为工作负载 Pod 配置多网卡，并通过 Spiderpool 进行 Underlay 网络的 IP 的分配和固定。主要介绍内容如下：

1. Pod 设置多容器网卡
2. 工作负载使用 IP 池
3. 工作负载使用固定 IP 池
4. 工作负载使用自动创建固定 IP 池
5. 工作负载使用默认 IP 池

## 前提条件

1. [SpiderPool 已成功部署](../../modules/spiderpool/install.md)。
2. 如使用手动选择 IP 池，请提前完成[创建 IP 子网和 IP 池](../../modules/spiderpool/createpool.md)。如使用自动创建固定 IP 池，请提前完成[创建 IP 池](../../modules/spiderpool/createpool.md)。
3. 如果使用默认 IP 池，请提前完成[创建 IP 子网和 IP 池](../../modules/spiderpool/createpool.md)。并在容器网络 Multus CNI 配置中，配置好带有默认 IP 池的网卡。
4. 对应使用的[Multus CR 已创建](../../config/multus-cr.md)。

## 界面操作

1. 登录平台 UI，在左侧导航栏点击`容器管理`->`集群列表`，找到对应集群。然后，在左侧导航栏选择`无状态负载`，点击`镜像创建`。

    ![镜像创建](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/useippool01.png)

2. 在`创建无状态负载`页面，完成`基本信息`、`容器配置`、`服务配置`页面的信息输入。然后，进入`高级配置`，点击配置`容器网卡`。

    ![容器网卡](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/useippool02.png)

3. 进入`容器网卡配置`页面，完成以下参数的配置：

    - `网卡信息`: 若创建的应用容器需要使用多张网卡（如一张东西向通信，一张南北向通信），可以添加多网卡。
        - eth0（默认网卡）：默认为 Overlay CNI，可选 Calico/Cilium/Macvlan CR，设置前请确认[Multus CR 已创建](../../config/multus-cr.md)。当 eth0（默认网卡）设置为 Underlay CNI，如 Macvlan 时，net1，net2 等新增网卡只能选择 Underlay CNI。
        
        - net1: 可选择 Underlay CNI 配置，如 Macvlan/SR-IOV ，本文示例为 Macvlan。
        
    - `IP 池配置`：Underlay CNI IP 分配的规则。
    - `创建固定 IP 池`： 开启后，只需要为新增的容器网卡（net1、net2、net3）选择对应子网，工作负载在部署时会自动创建固定 IP 池，部署后容器网卡仅能使用此 IP 池中的地址。
        
    - `弹性 IP`: 开启后，IP 池中的 IP 数量会根据设置的弹性 IP 数量变动。最大可用 IP 数等于 Pod 副本数 + 弹性 IP 数量。Pod 扩容时IP 池也随之进行扩容。
        
    - `自定义路由`：当应用创建有特殊路由需求时，可添加自定义路由。
        
    - `网卡 IP 池`：选择对应网卡待使用的子网或对应 IP 池。
        
    - `使用默认 IP 池`：开启后，会为新增的容器网卡（eth0、net1、net2）全部选择好默认的 IP 池。

    工作负载使用 IP 池有如下两种方式，两种方式的使用场景及流程差异可参考：[IP 池的使用说明](ippoolusage.md)

    **手动选择已有的 IP 池**

    手动选择 IP 池需要提前创建 IP 池，可选择 IP 池范围为： [已关联所选择 的Multus CNI 配置的 IPPool](createpool.md) ，可以是：`共享 IP 池`，添加了当前`应用亲和性的 IP 池`，添加了当前`命名空间亲和性的 IP 池`。

    ![手动选择](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/useippool03.png)

    **自动创建固定 IP 池**

    仅需要选择对应的子网，即可自动创建固定 IP 池。

    ![自动创建](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/useippool04.png)

    **使用默认 IP 池**

    提前创建好 IP 池，并在 Multus CNI 配置中，选择带有默认 IP 池的网卡，即可使用默认 IP 池功能。
    ![默认IP池](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/useippool05.png)
    
1. 创建完工作负载后，可点击对应工作负载 `test01` 查看工作负载 Pod 使用的 IP。

    ![工作负载 IP](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/useippool06.png)

    ![工作负载 IP](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/network/images/useippool07.png)

## YAML 使用

1. 使用 Pod 注解 `ipam.spidernet.io/ippool` 选择从 IP 池 `testingippool` 分配 IP，创建以下 Deployment：

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: workload01
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: workload01
      template:
        metadata:
          annotations:
            ipam.spidernet.io/ippool: |-
              {
                "ipv4": ["testingippool"]
              }
          labels:
            app: workload01
        spec:
          containers:
          - name: workload01
            image: busybox
            imagePullPolicy: IfNotPresent
            command: ["/bin/sh", "-c", "trap : TERM INT; sleep infinity & wait"]
    ```

2. 由 Deployment `workload01` 所控制的 Pod 均从 IP 池 `testingippool` 分配 IP 地址且成功运行。

    ```bash
    kubectl get se
    NAME                                      INTERFACE   IPV4POOL               IPV4              IPV6POOL   IPV6   NODE            CREATETION TIME
    workload01-6967dcd8df-8b6zp   eth0        standard-ipv4-ippool   172.18.41.47/24                     spider-worker   7s
    standard-ippool-deploy-6967dcd8df-cvq79   eth0        standard-ipv4-ippool   172.18.41.50/24                     spider-worker   7s
    standard-ippool-deploy-6967dcd8df-s58x9   eth0        standard-ipv4-ippool   172.18.41.41/24                     spider-worker   7s
    ```
