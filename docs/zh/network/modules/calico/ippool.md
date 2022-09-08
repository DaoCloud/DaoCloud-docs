# `ippool`

`IPPool` 表示 Calico 期望从中给 Pod 分配 IP 的地址集合。通过 Kubespray 拉起 Calico 之后，会分别为 IPv4、IPv6 创建一个默认的地址池：
`default-ipv4-ippool` 和 `default-ipv6-ippool`。

运行命令：

```shell
calicoctl get ippools  default-ipv4-ippool -o yaml
```

输出为：

```yaml
apiVersion: crd.projectcalico.org/v1
kind: IPPool
metadata:
  annotations:
    projectcalico.org/metadata: '{"uid":"637e72f1-d4ff-433c-92c5-cafe3aef5753","creationTimestamp":"2022-05-12T14:34:03Z"}'
  creationTimestamp: "2022-05-12T14:34:03Z"
  generation: 1
  name: default-ipv4-pool
  resourceVersion: "689"
  uid: c94af437-5a37-46c8-b521-641724b86ff8
spec:
  allowedUses:
  - Workload
  - Tunnel
  blockSize: 26
  cidr: 10.244.0.0/18
  ipipMode: Never
  natOutgoing: true
  nodeSelector: all()
  vxlanMode: Always
```

## `BlockSize`

在 Calico IPAM 中，`IPPool` 被细分为 Block，这些 Block 与集群中的特定节点相关联。
集群中的每个节点可以有一个或多个与之相关的 Block。当集群中的节点或 Pod 的数量增加或减少时，Calico 会根据需要自动创建和销毁 Block。

Block 的存在使 Calico 可以有效地聚合分配给同一节点上的 Pod 地址，这将会减少路由表的大小。
默认情况下，Calico 将尝试从节点相关的 Block 分配 IP。如果有必要，将会创建一个新的 Block。
Calico 也可以从该节点不相关的块中分配地址。默认情况下，Calico 创建的块有 64 个地址的空间（/26），但这可以修改。

> Note：特别是在集群节点数量较多且 `IPPool Cidr` 不足的情况，我们更需要根据集群规模提前规划好 `IPPool` 和 `BlockSize` 的大小。
> 否则可能会出现某些节点无法分配到 `Block` 的情况。

- `BlockSize` 默认为 26，即每个 block 拥有 2^(32-26) = 64 个地址。可由 `calico node env`: `CALICO_IPV4POOL_BLOCK_SIZE` 控制 (IPv4: 20-32;IPv6:116-128)
- Calico 要求 `BlockSize` 必须大于或者等于 `IPPool` 的 CIDR 的掩码，但实际环境中应确保每个节点至少有一个 Block。
  所以 Block 的个数应该大于等于节点的个数. 即 2^(`BLOCK_SIZE-IPPool_MASK`) >= NUM(nodes)

## 指定多默认池

随着集群的扩张或pod数量的增加，默认使用的地址池可能地址不足。导致Pod可能无IP可用或者某些节点没有可分配的Block. 我们可以通过修改calico的配置文件，使其在IP地址不够的时候，可以选择其他的`IPPool`. 防止IP地址不够，导致其他非预期的问题。

### 创建新的 `IPPool` 池

运行命令：

```shell
cat << EOF | calicoctl apply -f -
```

输出为：

```yaml
apiVersion: projectcalico.org/v3
kind: IPPool
metadata:
  name: extra-ippool
spec:
  cidr: 192.168.0.0/20
  blockSize: 26
  vxlanMode: Always
  natOutgoing: true
EOF
```

其中，

- `cidr`：可由实际环境决定 IP 地址范围

- `blockSize`：默认为 26，根据实际集群规模决定。缩小 `blockSize` 意味着每个 Block 中的地址变多，但 Block 总的数量会减少。
这适用于节点数不多但每节点上 Pod 比较多的场景。增大 `blockSize` 意味着每个 Block 中的地址变少，但 Block 总的数量会增加。
这适用于节点数较多的场景。但总的来说，只要 `IPPool` 的 CIDR 足够大，不用调整 `blockSize`（保持默认即可）也基本没有问题。

- `vxlanMode`：采用`vxlan`模式用于跨子网通讯

- `natOutgoing`：跨`IPPool`通讯是否需要`snat`

## `IPPool` 细粒度控制

默认情况下，`IPPool` 是集群全局共享。也可以将 `IPPool` 指定分配给特定的节点、租户、Pod。

### 节点过滤

在 `IPPool` 中根据 `nodeSelector` 字段去匹配特定的节点，只有特定节点才可以从此 `IPPool` 中去分配 IP。

- 给节点打上 label

    ```shell
    kubectl label nodes node1 type=test
    ```

- 在 `IPPool` 中配置 `nodeSelector`

    运行命令：

    ```shell
    cat << EOF | calicoctl apply -f -
    ```

    ```yaml
    apiVersion: projectcalico.org/v3
    kind: IPPool
    metadata:
    name: extra-ippool
    spec:
    cidr: 192.168.0.0/20
    blockSize: 26
    vxlanMode: Always
    natOutgoing: true
    nodeSelector: type=="test"
    EOF
    ```

但此 `IPPool` 不会影响到该节点已经创建的 Pod，如果要更新其 Pod 从该 `IPPool` 分配地址，那么必须 `recreate pod`。
进一步了解[高级的 selector 语法](https://projectcalico.docs.tigera.io/reference/resources/ippool)。

### 租户过滤

可通过在 namespace 中打上特定的 annotation，使其下的 Pod 会从此 label 对应的 `ippool` 分配 IP。

如果要为 namespace 添加 annotation，则编辑 namespace，在 annotation 中添加如下的 key-value 对：

```shell
kubectl annotate namespace test-ns "cni.projectcalico.org/ipv4pools"='["extra-ippool"]'
```

value 为 `ippool` 的 name 列表。如果是 ipv6，那么 key 为：`cni.projectcalico.org/ipv6pools`。

> NOTE: 此操作只能保证此 namespace 下的 Pod 会从 `extra-ippools` 中分配 IP，有点优选的感觉。
> 但其他 namespace 的 Pod 仍然可以从 `extra-ippools` 分配 IP。

### Pod 过滤

与租户过滤类似：也可以通过在 Pod 的 Annotation 中指定 `ippool`，使 Pod 从该 `ippool` 中分配地址：

```shell
kubectl annotate pod  test-pod "cni.projectcalico.org/ipv4pools"='["extra-ippool"]'
```

## 改变 `BlockSize`

我们在安装 Calico 之前，就应该定义好 `blockSize`。因为安装之后，`BlockSize` 的值不能编辑。
所以最好在安装前更改 IP 池块大小，以尽量减少对 Pod 连接的中断。

最佳改变 `BlockSize` 的方式：

- 创建临时的 `ippool`

    ```yaml
    apiVersion: projectcalico.org/v3
    kind: IPPool
    metadata:
    name: temporary-pool
    spec:
    cidr: 10.0.0.0/16
    ipipMode: Always
    natOutgoing: true
    ```

    > NOTE: 注意不要跟现有的 `ippool` 子网冲突

- 将 `default-ipv4-ippool` 设置为 `disable`

    ```shell
    calicoctl patch ippool default-ipv4-ippool -p '{"spec": {"disabled": true}}'
    ```

    其中 `default-ipv4-ippool` 为我们将要修改的 ippool 的名称。

- 检查 `ippool` 的状态

    运行命令：

    ```shell
    $ calicoctl get ippool -o wide
    NAME                  CIDR             NAT    IPIPMODE   DISABLED
    default-ipv4-ippool   192.168.0.0/16   true   Always     true
    temporary-pool        10.0.0.0/16      true   Always     false
    ```

    `default-ipv4-ippool` 已 `DISABLED`，新创建的 Pod 不会从此 `ippool` 中分配地址。

- 删除先前的所有 Pod

    > NOTE: 此步骤需要删除全部存在于 `default-ipv4-ippool` 下的 Pod，所以会造成 Pod 的连通性暂时中断，请在合适的时机进行此操作。

    假设这里删除 default namespace 下的所有 Pod：

    ```shell
    kubectl delete po --all
    ```

    等待 Pod 重建完成，Pod 会使用 `temporary-pool` 的地址。

- 删除 `default-ipv4-ippool`

    ```shell
    calicoctl delete ippool default-ipv4-ippool
    ```

- 重新创建 `default-ipv4-ippool` 并修改 `cidr` 或者 `blockSize`

    运行命令：

    ```shell
    calicoctl create -f -<<EOF
    ```

    ```yaml
    apiVersion: projectcalico.org/v3
    kind: IPPool
    metadata:
    name: default-ipv4-ippool
    spec:
    blockSize: 27   # change blockSize from 26 to 27
    cidr: 192.0.0.0/16
    ipipMode: Always
    natOutgoing: true
    EOF
    ```

    > NOTE: `cidr` 和 `blockSize` 根据实际的情况修改

- DISABLE `temporary-pool`

    ```shell
    calicoctl patch ippool temporary-pool -p '{"spec": {"disabled": true}}'
    ```

- 重新创建所有 Pod

    假设这里删除 default namespace 下的所有 Pod：

    ```shell
    kubectl delete po --all
    ```

    等待 Pod 重建完成，Pod 会使用 `default-ipv4-ippool` 的地址。

- 删除 temporary-pool

## 迁移 `IPPool`

场景：原有池地址不足，需要迁移到新的 `IPPOOL` 中

> 注意！如果你按照以下这些规则，则现有的 Pod 连接将不会受到影响。
> (如果你在创建和验证新的 IP 池之前删除旧的 IP 池，则现有的 Pod 将受到影响）。当 Pod 被删除时，业务会可能中断。

- 创建新的 `ippool`

    强烈建议新 `IPPool` 是处于 Kubernetes 集群的 CIDR 中。如果从 Kubernetes 集群 CIDR 外部分配 Pod IP，则某些流量可能会不必要地应用 NAT，从而导致意外行为。

- Disable 旧 `ippool`

    ```shell
    calicoctl patch ippool default-ipv4-ippool -p '{"spec": {"disabled": true}}'  # 假设default-ipv4-ippool是旧IPPool
    ```

- 重新创建旧 IP 池下的所有 Pod

    目的是让所有 Pod 从新的 `IPPool` 中分配地址

- 验证

    新启动 Pod，观察是否从新池中分配 IP 并测试连通性

- 删除旧 `ippool`

## Q&A

1. 不同的 `IPPool` 是否支持子网重叠？

    不支持，在创建 `ippool` 时，Calico 会校验 `ippool` 的 `cidr` 是否与已存在的 `ippool` 存在子网重叠的情况。

2. `IPPool` 创建后 `BlockSize` 是否还能修改？

    不能修改。`ippool` 创建之后，已经根据 CIDR 和 `BlockSize` 就已经创建好集群所有的 `block`，手动修改 `BlockSize` 是没有效果的。
