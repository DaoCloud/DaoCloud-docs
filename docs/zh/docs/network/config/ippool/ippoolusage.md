# IP 池的使用说明

本页介绍在使用 Spiderpool 进行 IP 分配以及管理时，IP 池的不同使用场景。使用前请确保 [SpiderPool 已正确安装](../../modules/spiderpool/install/install.md)。

## 工作负载使用固定 IP

工作负载使用固定 IP 有 2 种使用方式：

- `手动创建固定 IP 池`，并指定待使用 IP Pool 的工作负载亲和性，创建工作负载时选择对应的固定 IP Pool。

    **适用场景**：此方式适用于 IP 强管控场景，需要提前申请开通防火墙进行 IP 放行，放行后工作负载才能使用对应的固定 IP 。操作方式可参考：[创建子网及 IP 池](../../config/ippool/createpool.md) 及[工作负载使用 IP 池](../use-ippool/usage.md)

- `自动创建固定 IP 池`，创建子网并添加待使用 IP 后，应用管理员直接基于创建后的子网自动创建固定 IP Pool，创建后的 IP Pool 仅供此应用负载独享。

    **适用场景**：此方式适用于 IP 粗粒度管理场景，可以基于较大范围 IP（如：10.6.124.10~10.6.124.200）范围进行防火墙放行，放行后工作负载可基于此 IP 段自动获取 IP 并创建对应的固定 IP 池。操作方式可参考[创建子网及 IP 池](../../config/ippool/createpool.md)及[工作负载使用 IP 池](../use-ippool/usage.md)

    ![fixedippool](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/fixedippool.jpg)

## 工作负载使用默认 IP 池

默认 IP 池是预先定义的、具有特定IP地址范围的IP资源集合。管理员需要手动设置和配置默认 IP 池，由于IP地址是预先分配的，所以这种方式更具确定性。这些 IP 地址可以为特定的工作负载或应用进行分配。

**适用场景**：此方式适用于 IP 强管控场景，如安全性要求高或需要与外部系统（如防火墙）进行配合的场景。操作方式可参考：[创建子网及 IP 池](../../config/ippool/createpool.md)及[工作负载使用 IP 池](../use-ippool/usage.md)

## IP 池的节点亲和性

**适用场景**：

当集群节点为跨子网或跨数据中心时，不同的 Node 上可用的子网不相同，例如：

- 同一数据中心内，集群接入的节点分属不同子网
- 单个集群中，节点跨越了不同的数据中心

同时工作负载创建时：

- 同一工作负载需要调度至 **跨子网** 或 **跨数据中心** 节点上，使用流程如下：

    ![nodeaffinity01](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/nodeaffinity01.jpg)

- 不同工作负载需要调度至 **不同节点** 上，并使用 **不同子网** ，如：[SR-IOV 同 Macvlan CNI 混用场景](../../plans/ethplan.md)，具体使用流程如下：

    ![nodeaffinity02](https://docs.daocloud.io/daocloud-docs-images/docs/network/images/nodeaffinity02.jpg)

## IP 池的命名空间亲和性

**适用场景**：

如果创建的 IP 池仅指定给某一个命名空间使用，该命名空间内的工作负载创建时，均可使用此 IP 池内的 IP，
并添加命名空间亲和性的 IP 池为指定命名空间内共享。操作方式可参考[创建子网及 IP 池](../../config/ippool/createpool.md)。

## FAQ

1. 问：添加了命名空间亲和性，同时添加了工作负载亲和性，或者节点亲和性，最后效果是什么样？

    答：效果为多重亲和性叠加，需要符合所有亲和性，此 IP Pool 才能被使用。

2. 问：添加了命名空间亲和性的 IP 池，是否可基于 命名空间 IP 池细分后，再分配给应用进行固定 IP 池？

    如 `ippool01` 属于子网 10.6.124.0/24，`ippool01` 中有 100 （10.6.124.10~109）个 IP，
    并添加了命名空间亲和性：`kubernetes.io/metadata.name: default`，是否可以将：

    1. 10.6.124.10~19 分配给 `default` 命名空间下的应用负载 workload01 使用并 **固定** 。
    2. 10.6.124.20~29 分配给 `default` 命名空间下的应用负载 workload02 使用并 **固定** 。
    3. ...

    答：无法做到，可以做到给某 **1 个** 应用负载使用并 **固定** ，使用方式为：在 IP Pool 上同时添加对应工作负载亲和性。
