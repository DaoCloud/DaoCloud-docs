# 安装

在需要安装 ARP Pool 的情况下, 需要启用 Helm 并就绪等待。

## 安装

- Metallb Helm Chart 存放于 addon repo 下:


![metallb_repo](../../images/metallb_helm_repo.png)

- 初始化 Metallb ARP 模式:

> 注意: 如果安装时开启 ARP 模式, 请开启 就绪等待!

> 安装 Metallb 时, 可选择初始化 Metallb ARP 模式。LoadBalancer Service默认会从这个池中分配 IP 地址, 并且通过 APR 宣告这个池中的所有 IP 地址。

> 地址池列表可以配置 IPv4 和 IPv6 的地址
> 
> 每个地址段输入格式可以为合法的 CIDR（如 192.168.1.0/24），也可以为 IP 范围（如 1.1.1.1-1.1.1.20）
> 
> 输入的每个地址段应当属于集群节点某个真实"物理"网段, 但注意不要已有的 IP 地址冲突

![metallb_ippool](../../images/metallb_ippool.png)

- 配置 Metallb L2Advertisement

    - 默认情况下, 所有节点都会作为 LoadBalancer IP的下一跳, 但可以通过 NodeSelector 限制只有某些节点作为 LoadBalancer IP 的下一跳:

    
![node_list](../../images/metallb_nodelist.png)

    如上图配置表示, 只有匹配 Label "kubernetes.io/os: linux" 的节点才会作为 LoadBalancer IP 的下一跳。

- 指定特定接口宣告 LB IP

默认情况下, Metallb 从节点所有网卡宣告 LB IPs, 我们可以配置指定网络接口宣告。

![](../../images/metallb-interface.png)


- 安装完成

    ![](../../images/metallb_installed.png)

## 注意事项

- Metallb 安装只提供初始化 ARP 模式。BGP 模式配置较为复杂且需要硬件支持,这里并不提供初始化 Metallb BGP模式。如需配置 BGP 模式, 请参考 [advanced_bgp_configuration](https://metallb.universe.tf/configuration/_advanced_bgp_configuration)
- 如果安装时未初始化 ARP 模式, 不能使用 Helm 更新的方式去重新初始化 ARP 模式, 请参考 [Metallb使用](usage.md).