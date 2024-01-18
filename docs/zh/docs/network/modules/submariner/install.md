---
hide:
- toc
---

# 安装 Submariner

本页介绍如何安装 Submariner。

## 前置条件

- 至少准备两个集群，可将 submariner-k8s-broker 部署在其中一个集群中，也可以单独部署在其他集群，submariner-operator 部署在每个 join 的子集群中。子集群和 submariner-k8s-broke 部署的集群之间应能够正常通讯
- 不同子集群的子网最好不要重叠, 否则需要启用 Globalnet 功能, 而 Globalnet 功能有一定的限制
- 支持的 CNI 列表为:
    * OpenShift-SDN
    * Weave
    * Flannel
    * Canal
    * Calico(存在兼容性问题，需要手动规避，参考[使用说明](usage.md))
    * OVN(要求 OVN NorthBound DB 的版本 > 6.1.0+)
- Kube-proxy 的模式必须为 `IPtables`，`IPvs` 模式目前尚不支持
- 集群内部需要允许 `Vxlan` 的流量，集群外部需要放通 udp/4500 端口

> Submariner 现在处于比较早期的阶段, 出现 Bug 比较常见。

## 安装步骤

!!! note

    `submariner-k8s-broker` 可以部署在一个单独的集群，也可以部署在 Join 的子集群中。本文以 `submariner-k8s-broker` 部署在一个单独的集群为例，展示安装过程。

请确认您的集群已成功接入`容器管理`平台，然后执行以下步骤首先安装 `submariner-k8s-broker`:

1. 在左侧导航栏点击 `容器管理` —> `集群列表`, 然后找到准备安装 `submariner-k8s-broker` 的集群名称。

2. 在左侧导航栏中选择 `Helm 应用` -> `Helm 模板`，找到并点击 `submariner-k8s-broker`。

    ![helm](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/submariner-k8s-broker-helm-repo.png)

3. 在版本选择中选择希望安装的版本，点击安装。

4. 推荐安装到 `submariner-k8s-broker` 命名空间下：

    ![broker-ns](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/submariner-k8s-broker-ns.png)

5. 下图所示配置无需更改，保持默认参数即可：

    ![config](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/submariner-k8s-broker-config.png)

6. 在 Broker 集群成功安装 `submariner-k8s-broker`：

    ![broker](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/submariner-k8s-broker-install.png)

7. 切换到其中子集群：master01，安装 `submariner-operator`：

    ![operator](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/submariner-operator-helm-repo.png)

8. 在版本选择中选择希望安装的版本，点击安装。

9. 推荐安装到 `submariner-operator` 命名空间下，开启就绪等待：

    ![operator-ns](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/submariner-operator-ns.png)

10. 配置 `submariner-operator` 连接 Broker 集群的配置:

    ![operator-broker](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/submariner-operator-broker.png)

    上面的参数说明:

    * `Broker` —> `brokerK8sApiServer`：Broker 集群 API-Server 的地址，可以通过以下方式获取：

        ```shell
        # 在安装 submariner-k8s-broker 的集群上
        [root@broker ~]# kubectl -n default get endpoints kubernetes  -o jsonpath="{.subsets[0].addresses[0].ip}:{.subsets[0].ports[?(@.name=='https')].port}"
        10.6.172.22:6443
        ```

    * `Broker` —> `brokerK8sCA`：访问 Broker 集群 API-Server 的客户端证书，可以通过以下方式获取：

        ```shell
        # 在安装 submariner-k8s-broker 的集群上
        [root@broker ~]# kubectl -n submariner-k8s-broker get secrets  -o jsonpath="{.items[?(@.metadata.annotations['kubernetes\.io/service-account\.name']=='submariner-k8s-broker-client')].data['ca\.crt']}"
        LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUMvakNDQWVhZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREFWTVJNd0VRWURWUVFERXdwcmRXSmwKY201bGRHVnpNQjRYRFRJek1ESXlNakV3TkRjek5Wb1hEVE16TURJeE9URXdORGN6TlZvd0ZURVRNQkVHQTFVRQpBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUJBTVFLCmRVUHZoeDNOcFRXeGU0STZNV1I1VFU0VThJeVhBeWF6ZXJRRnhZK3l5Q3F1NnhFOUUwTDRSbUdxS0pyTFRSVWYKQi85YmowcWRaNFRJd2FTTmN3cGVqanYxYllTaVVKV0NsT0dXbTdLWUd4UnhCMEZFbVlCaGovT29HWGJhaEw5eQpqR1A1VjFsYTMxYlhONllSY0duR3hXMCt0QmE0RndhMGlUV3owd2R5dFE4cVpuMXdLUC9QMjNKZ0o1N1pwN3hOCmlLOHV6OENGRjZmTnkyNVJYeEV2cGRQdzEwcnJDM0Npem1mcjNaZHl0cGVFdk44U2V6STByMVNtVHBxSTM4UlEKZzVKdTFvV1NRcENEZjBPV1N5WUxxRno1NmU5dStPc0tyVXFzQkVsUkdKNWhvUGppVW9VN3I2N3lmSGl4TmdTcgpEM1I4aklSQzZITE5OTHE5UG8wQ0F3RUFBYU5aTUZjd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWRFd0VCCi93UUZNQU1CQWY4d0hRWURWUjBPQkJZRUZDclJxaGJRNnV1aWFlOVJJd3RsdGd0bHhaRzhNQlVHQTFVZEVRUU8KTUF5Q0NtdDFZbVZ5Ym1WMFpYTXdEUVlKS29aSWh2Y05BUUVMQlFBRGdnRUJBSU5QUmtZMEpKSk5jNjFlVUpSOQo2bm9LTFl0cUN6VUxqRDVOZ3BmSy9GK0NvNk45Y0k5c0c1V1FVQ3ZMUVc5MUlFRlhFencvSEswUFBJTy8zVFpICjVQS05TUjR5d2hwSmtyeFRveDEvWWRqK2RWNzNGUnFKTFVuQkw1T3U4SWlKR2RNR0VKc040dnd5amk5TGt3WGMKcC9aUUVieWhLdmRvRWdOaDlhUzMrQzRJSVFnNmVqZTgvYVh6NTVaL2RoN2NZQUhCZWFQYmVwWU1kNklwc3VhTwo5Smx3TmJaSWczNHIzL3hQYjhCNUJOSkp2MXI3eE1YblFlaXc1MFNWaGdpR0JXMFdOdFo4NDVGREY2NHFzVFBsCjhLSjZOQkdjRUVuTHpDSXNhVUwxUHk4bk90K3NWWFNlUlhXV2VlWm84R0krWGpXQjZWL3FscnllSmp6Yy9hUU4KYWdBPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg==
        ```

    * `Broker` —> `brokerK8sApiServerToken`：访问 Broker 集群 API-Server 的 Token，可以通过以下方式获取：

        ```shell
        # 在安装 submariner-k8s-broker 的集群上
        [root@broker ~]# kubectl -n submariner-k8s-broker get secrets -o jsonpath="{.items[?(@.metadata.annotations['kubernetes\.io/service-account\.name']=='submariner-k8s-broker-client')].data.token}" | base64 --decode
        eyJhbGciOiJSUzI1NiIsImtpZCI6Ik1kUWpXalIwUVV0RmtTcjJXdElvMW1WWHdZbU5Md2pRN0tFeVZSbUpINTgifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJzdWJtYXJpbmVyLWs4cy1icm9rZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlY3JldC5uYW1lIjoic3VibWFyaW5lci1rOHMtYnJva2VyLWNsaWVudC10b2tlbiIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50Lm5hbWUiOiJzdWJtYXJpbmVyLWs4cy1icm9rZXItY2xpZW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQudWlkIjoiYzM0MzQ0MTItOTEyNi00NmFjLTk5ODUtZDgwYWI3MDAxOTdkIiwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OnN1Ym1hcmluZXItazhzLWJyb2tlcjpzdWJtYXJpbmVyLWs4cy1icm9rZXItY2xpZW50In0.quC7a3hTctbgaRKHmzAvlP16EspwtTzWzirgj0o2d9XYfVe6bPX29Wg4XHh3ZzetaMYmvj_toukQJcQ6bO1CG7xv4mOFFkLF2ECrQNPGKYa5A2LHgQCFiWteWjU7wcisW3lugMTC6a5OrbK4optvVjseLwqI-BClm8nsgjGocBTrv1qqDp-4aiPkLtgcZRV2bsgE3yLsyc7Mhuncs7gDmI2NuBXoYRGfXtAjd6XIbnXd5Tp5sAV_k92xruNqKDpzQZI32K6I7It1WNQvtGOTYHa9sks0gxgUmQu8Z9Pikke5LCFOMNcBbjwlCCxzg6jKWJH87ReMtenRqcfG2jNeTQ
        ```

        > 注意需要执行 decode

    * `Broker` —> `brokerK8sRemoteNamespace`： submariner-k8s-broker 组件的命名空间，默认为 submariner-k8s-broker(参考步骤 4)。
    * `Broker` —> `enableGloablnet`：是否启用 Globalnet 功能。如果子集群间子网重叠，可以启用。

11. 配置 `submariner-operator`：

    ![operator-install1](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/submariner-operator-install1.png)

    以上配置说明:

    * `IPsec Configuration` —> `ceIPSecPSK`：建立 IPsec 隧道时所需要的预共享密钥。如果对安全性有较高要求，可以使用下面的方式获取：

        ```shell
        [root@broker ~]# LC_CTYPE=C tr -dc 'a-zA-Z0-9' < /dev/urandom | fold -w 64 | head -n 1
        ZSMhkWz6EfO7zacMLCeYoKruYIm6iq1roNQKS8rKW8cQGJiYwDaYQNrzbbdP2azl
        ```

    * `Submariner` —> `clusterId`：用于标识该子集群，填写规范需要满足 DNS-1123 Label。
    * `Submariner` —> `clusterCidr`：子集群 Pod 的 CIDR。

        ![operator-install2](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/submariner-opearator-install2.png)

    * `Submariner` —> `serviceCidr`：子集群 Service 的 CIDR。
    * `Submariner` —> `globalCidr`：开启 globalnet 功能。

        > 注意: 如果不使用  globalnet 功能, 请不要配置该字段。

    * `Image Configuration` —> `cableDriver`：隧道模式，支持 `libreswan`(默认)、`wireguard`、`vxlan`。
    * `Image Configuration` —> `natEnabled`：是否打开网关节点之间的 NAT 功能。如果不同子集群的网关节点需要跨公网才能通讯, 则开启。

12. 在子集群 master01 安装完成：

    ![opearator-install-3](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/submariner-opearator-install-3.png)

13. 安装完成后，需要手动设置子集群 master01 其中某个节点为网关节点，需要添加标签 "submariner.io/gateway: true"：

    ![gateway](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/submariner-operator-gateway-label.png)

14. 查看组件是否正常 running：

    ```shell
    root@controller-node-1:~# kubectl  get po -n submariner-operator
    NAME                                                     READY   STATUS      RESTARTS       AGE
    helm-operation-upgrade-submariner-operator-q79sp-9bkzl   0/1     Completed   0              31h
    submariner-gateway-jpclp                                 1/1     Running     18 (30m ago)   31h
    submariner-lighthouse-agent-589676874b-dn75z             1/1     Running     0              31h
    submariner-lighthouse-coredns-5d675b4897-tm752           1/1     Running     0              32h
    submariner-lighthouse-coredns-5d675b4897-wxr8z           1/1     Running     0              32h
    submariner-metrics-proxy-2ptmn                           2/2     Running     0              31h
    submariner-operator-75ccdf484-6862g                      1/1     Running     0              32h
    submariner-routeagent-kh4hp                              1/1     Running     0              31h
    ```

15. 子集群 master01 join 完成，按照同样方式在另一个子集群安装 submariner。

## 注意事项

- 安装完之后需要至少给一个节点打上标签："submariner.io/gateway: true"。只有该标签存在, Gateway 组件才会被安装。
- 如果集群 CNI 为 Calico, 需要做一些额外的操作，来解决与 Calico 的兼容性问题，请参考[使用说明](usage.md)。
