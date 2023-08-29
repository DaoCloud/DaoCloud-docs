---
hide:
  - toc
---

# 创建子网及 IP 池

本页介绍在创建工作负载使用 IP 池之前，如何创建子网及 IP 池。

- 如部署 SpiderPool 组件时已创建子网及 IP 池，可直接[使用 IP 池](./usage.md)。
- 如需要创建新的子网及 IP 池可参考此文档。

## 前提条件

- [SpiderPool 已成功部署](./install.md)。
- [Multus 搭配 Macvlan / SRI-OV 已成功部署](../multus-underlay/install.md)。
- 创建子网及 IP 池前建议做好子网和 IP 规划，并充分了解 [IP 池的使用方式](ippoolusage.md)。

## 界面操作

1. 登录 DCE UI 后，在左侧导航栏点击 `容器管理` —> `集群列表`，找到对应集群。然后在左侧导航栏点击`容器网络` —> `网络配置`。

    ![网络配置](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/networkconfig01.jpg)

1. 进入`网络配置`，确认待使用子网是否已创建。

    - 如待使用子网已默认创建，可直接`创建 IP 池`。

    - 如待使用子网没有默认创建，可进入页面点击`创建子网`。

    ![创建子网](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/subnetcreate.jpg)

    参数说明：

    - `IPv4/IPv6 类型`：待创建子网的子网类型。

    - `子网`：已经规划好的子网段。如配合 Macvlan 使用，请提前同网络管理员确认对应网络接口/子接口所对应的网段。

    - `网关`：子网对应网关，请提前同网络同事确认。

    - `VLAN ID`：子网所对应的 VLAN ID。

1. 点击`下一步`进入 `IP 选择`，输入待使用的 IP 段（输入上述子网内 IP）。点击`确定`，完成子网创建。

    ![创建子网](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/subnetcreate02.jpg)

1. 点击待使用的`子网名称`，进入子网详情页面。

    ![子网详情](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/subnetlist.jpg)

1. 在子网详情页，点击`创建 IP 池`。

    !!! note

        创建 IP 池为可选步骤，可根据需要进行创建。

        - 如需要对 IP 进行严管控，可提前完成 IP 池创建。
        - 如粗粒度管控 IP 资源，可不用提前创建 IP 池。

    进入创建页面，输入如下参数：

    ![创建 IP 池](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/createippool01.jpg)

    - `网关`：`网关`默认继承`子网网关`，可修改。

    - `自定义路由`：当用户有特殊路由需求时，可基于 IP 池粒度的进行自定义。
  
    - `Multus 实例`：可以指定从哪个 IP 池为 Pods 分配 IP 地址，或者定义当 Pod 连接到特定网络时应使用哪个 IP 池。

    - `工作负载亲和性`：工作负载标签（如 `app: workload01`）。IP 池创建后，仅可被对应的工作负载选择，实现固定 IP 池效果。

    - `节点亲和性`：节点标签( 如 `node:controller-1`）。IP 池创建后，工作负载 Pod 需要调度到对应节点才能使用创建的 IP 池。

    - `命名空间亲和性`：开启后可选择对应命名空间。选择后，只有对应命名空间中的工作负载可使用创建的 IP 池。

    !!! note

        如果创建时不添加任何亲和性，创建后的 IP 池为`共享 IP 池`。

1. 点击 IP 池名称，然后点击`添加 IP` 选择 `IP 开始地址`以及加入 IP 池中的 `IP 数量`，点击`确定`，完成 IP 添加，再次点击完成 IP 池创建。

    `获取 IP 规则`：从 `IP 开始地址`依次获取输入对应数量的 IP，IP 段如不是连续的 IP，则跳过中间断档 IP，依次往后获取。

    ![添加 IP](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/createippool02.jpg)

2. 创建完成后[工作负载即可使用 IP 池](../../modules/spiderpool/usage.md)。

## YAML 创建

也可以直接通过 YAML 来创建子网和 IPPool。

### YAML 创建子网

```yaml
apiVersion: spiderpool.spidernet.io/v1
kind: SpiderSubnet
metadata:
  name: default-v4-subnet
spec:
  gateway: 172.30.120.1
  ipVersion: 4
  ips:
  - 172.30.120.126-172.30.120.127  # 已规划子网 IP，可输入IP 段
      # 如 72.30.120.126-172.30.120.127 段或单个 IP 如：172.30.120.126
  subnet: 172.30.120.0/21
  vlan: 0
```

### YAML 创建 IPPool

```yaml
apiVersion: spiderpool.spidernet.io/v1
kind: SpiderIPPool
metadata:
  name: standard-ipv4-ippool
spec:
  ipVersion: 4
  subnet: 172.30.120.0/21
  ips:
  - 172.30.120.126-172.30.120.127      # 已添加至子网内的 IP， 可输入IP 段
         # 如 172.30.120.126-172.30.120.127 段或单个 IP 如：172.30.120.126
```
