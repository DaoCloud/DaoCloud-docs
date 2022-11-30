# Calico 网络排障

本页列出通用的 Calico 网络排障步骤。

## 确认 IP 池地址是否用完

确认 IP 池的 Block 是否被节点已经分完：

- 计算总 IP 数

    `IPS` = 2 ^ (32 - mask)

    如果掩码为 20，则总 IP 数= 2 ^ 12 = 4096

- 计算有多少个 `Block`

    查看 IP 池中 `BlockSize`。默认为 26，则一个 `Block` 拥有 2 ^ (32 - 26) = 64 个地址，Block 数= 4096 / 64 = 64。

- 确认 `Block` 是否被分完

    在 Calico 中，应确保每个节点至少拥有一个 Block。
    所以如果节点大于 64，则可能需要考虑新增 IP 池或者修改原 IP 池大小，否则可能造成无法正常访问某些节点的 Pod。
    请参考 [`ippool.md`](ippool.md)。

## 确认隧道接口是否工作正常

以 `vxlan` 模式为例:

- 查看 `vxlan.calico` 状态

    ```shell
    $ ip a show vxlan.calico
    6: vxlan.calico: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1450 qdisc noqueue state UNKNOWN group default
        link/ether 66:07:01:14:06:90 brd ff:ff:ff:ff:ff:ff
        inet 10.244.0.0/32 scope global vxlan.calico
        valid_lft forever preferred_lft forever
    ```

    注意其 `state` 应为 `UNKNOWN`。

- 查看隧道IP是否正常

    正常情况下，隧道 IP 地址应是本节点所属 `Block` 的 IP 范围内，如果不是则可能出现通信问题，大多一般是地址不够造成的。

- 查看路由是否正常

    `calico` 在每个节点下发的路由是以其节点 Block 范围为单位的，也就是一个 Block 对应一条静态路由:

    ```shell
    $ ip r
    default via 172.18.0.1 dev eth0
    ...
    10.244.0.48/28 via 10.244.0.48 dev vxlan.calico onlink
    ...
    ```

    如上 `10.244.0.48/28 via 10.244.0.48 dev vxlan.calico onlink`，类似这样的路由可能有多条，分别对应不同节点、不同 Block 的地址。

    确认目标 Pod IP 是否存在本节点如上静态路由的目标地址: 如 `10.244.0.48/28`。
    如果不存在，路由更新有问题。

    如果存在，再次检查此静态路由的下一跳：10.244.0.48（即对端节点的 `vxlan` 隧道 IP）是否和目标地址所对应的 Block 处于同个节点上。
    如果不是，可能造成通信问题。如果是，检查本端的邻居表:

    ```shell
    $ ip n | grep 10.244.0.48
    10.244.0.48 dev vxlan.calico lladdr 66:46:b3:ce:05:5d PERMANENT
    ```

    到对应节点确认: 对端节点的 `vxlan` 隧道 IP 的 Mac 是否为：`66:46:b3:ce:05:5d`。
    如果不是，则邻居表学习错误，可删除本段 `arp` 缓存，使其重新学习。

## `tcpdump` 抓包确认

通过 `tcpdump` 分别在 `veth` 虚拟网卡、隧道网卡、主机网卡或 `Pod` 内部抓包，观察报文在哪一个阶段丢弃。

## `iptables` 规则查看

如果路由转发无异常，可能被某些异常的 `iptables` 规则过滤掉了。

> TODO: calico iptables 规则梳理

如果上述仍未解决: 保存现场，打包日志，联系研发。

## `calicoctl`

### 资源操作

- get
- create
- patch
- delete
- apply
- replace

### `ipam`

- 查看目前分配的 block 及使用情况

    ```shell
    $ calicoctl ipam show --show-blocks
    +----------+---------------------+------------+------------+-------------------+
    | GROUPING |        CIDR         | IPS TOTAL  | IPS IN USE |     IPS FREE      |
    +----------+---------------------+------------+------------+-------------------+
    | IP Pool  | 10.244.0.0/26       |         64 | 12 (19%)   | 52 (81%)          |
    | Block    | 10.244.0.0/28       |         16 | 1 (6%)     | 15 (94%)          |
    | Block    | 10.244.0.16/28      |         16 | 3 (19%)    | 13 (81%)          |
    | Block    | 10.244.0.32/28      |         16 | 7 (44%)    | 9 (56%)           |
    | Block    | 10.244.0.48/28      |         16 | 1 (6%)     | 15 (94%)          |
    | IP Pool  | fd1a:29a5:aa4e::/48 | 1.2089e+24 | 0 (0%)     | 1.2089e+24 (100%) |
    +----------+---------------------+------------+------------+-------------------+
    ```

- 检查某个 IP 是否被使用

    ```shell
    $ calicoctl ipam show --ip=10.244.0.17
    IP 10.244.0.17 is in use
    Attributes:
    namespace: local-path-storage
    node: kind-control-plane
    pod: local-path-provisioner-547f784dff-jjmp6
    timestamp: 2022-05-30 16:02:17.551768878 +0000 UTC
    $ calicoctl ipam show --ip=10.244.0.100
    10.244.0.100 is not assigned
    ```

- 释放某个 IP

    如果确认某个 IP 没有被分配，Calico 没有正确地回收此 IP，可手动释放：

    ```shell
    calicoctl ipam release --ip=10.244.0.100
    ```

    > NOTE：一定要确认此 IP 并未有 Pod 在使用。

### node

- 查看 node 状态

    ```shell
    calicoctl node status
    ```

- node 状态检查

    ```shell
    calicoctl node diags
    ```

更多命令详情：`calicoctl --help`
