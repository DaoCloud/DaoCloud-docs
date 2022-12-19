# Calico network troubleshooting

This page lists general Calico network troubleshooting steps.

## Confirm whether the IP pool addresses are exhausted

Confirm whether the block of the IP pool has been allocated by the node:

- Calculate the total number of IPs

    `IPS` = 2 ^ (32 - mask)

    If the mask is 20, the total number of IPs = 2^12 = 4096

- Count how many `Block` there are

    View the `BlockSize` in the IP pool. The default is 26, so a `Block` has 2 ^ (32 - 26) = 64 addresses, and the number of Blocks = 4096 / 64 = 64.

- Check if `Block` is allocated

    In Calico, each node should have at least one block.
    Therefore, if the number of nodes is greater than 64, you may need to consider adding an IP pool or modifying the size of the original IP pool, otherwise Pods on some nodes may not be able to be accessed normally.
    Please refer to [`ippool.md`](ippool.md).

## Confirm that the tunnel interface is working properly

Take `vxlan` mode as an example:

- View `vxlan.calico` status

    ```shell
    $ ip a show vxlan.calico
    6: vxlan.calico: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1450 qdisc noqueue state UNKNOWN group default
        link/ether 66:07:01:14:06:90 brd ff:ff:ff:ff:ff:ff
        inet 10.244.0.0/32 scope global vxlan.calico
        valid_lft forever preferred_lft forever
    ```

    Note that its `state` should be `UNKNOWN`.

- Check whether the tunnel IP is normal

    Under normal circumstances, the tunnel IP address should be within the IP range of `Block` to which this node belongs. If not, there may be communication problems, most of which are usually caused by insufficient addresses.

- Check whether the routing is normal

    The route delivered by `calico` to each node is based on the block range of the node, that is, a block corresponds to a static route:

    ```shell
    $ ip r
    default via 172.18.0.1 dev eth0
    ...
    10.244.0.48/28 via 10.244.0.48 dev vxlan.calico onlink
    ...
    ```

    As above `10.244.0.48/28 via 10.244.0.48 dev vxlan.calico onlink`, there may be multiple routes like this, corresponding to the addresses of different nodes and blocks.

    Confirm whether the target Pod IP has the target address of the above static route on this node: such as `10.244.0.48/28`.
    If not present, there is a problem with routing updates.

    If it exists, check again whether the next hop of this static route: 10.244.0.48 (that is, the `vxlan` tunnel IP of the peer node) is on the same node as the Block corresponding to the target address.
    If not, it may cause communication problems. If yes, check the local neighbor table:

    ```shell
    $ ip n | grep 10.244.0.48
    10.244.0.48 dev vxlan.calico lladdr 66:46:b3:ce:05:5d PERMANENT
    ```

    Go to the corresponding node to confirm: whether the Mac of the vxlan tunnel IP of the peer node is: `66:46:b3:ce:05:5d`.
    If not, the neighbor table learning error, you can delete the `arp` cache of this section to make it learn again.

## `tcpdump` packet capture confirmation

Use `tcpdump` to capture packets in the `veth` virtual network card, tunnel network card, host network card or `Pod`, and observe at which stage the message is discarded.

## `iptables` rule view

If the route forwarding is normal, it may be filtered out by some abnormal `iptables` rules.

> TODO: Calico iptables rule combing

If the above is still not resolved: save the scene, pack the log, contact R&D.

## `calicoctl`

### Resource Operations

- get
- create
- patch
- delete
- apply
-replace

### `ipam`

- View currently allocated blocks and their usage

    ```shell
    $ calicoctl ipam show --show-blocks
    +----------+---------------------+------------+--- ---------+-------------------+
    | GROUPING | CIDR | IPS TOTAL | IPS IN USE | IPS FREE |
    +----------+---------------------+------------+--- ---------+-------------------+
    | IP Pool | 10.244.0.0/26 | 64 | 12 (19%) | 52 (81%) |
    | Block | 10.244.0.0/28 | 16 | 1 (6%) | 15 (94%) |
    | Block | 10.244.0.16/28 | 16 | 3 (19%) | 13 (81%) |
    | Block | 10.244.0.32/28 | 16 | 7 (44%) | 9 (56%) |
    | Block | 10.244.0.48/28 | 16 | 1 (6%) | 15 (94%) |
    | IP Pool | fd1a:29a5:aa4e::/48 | 1.2089e+24 | 0 (0%) | 1.2089e+24 (100%) |
    +----------+---------------------+------------+--- ---------+-------------------+
    ```

- Check if an IP is in use

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

- Release an IP

    If it is confirmed that an IP has not been allocated and Calico has not properly reclaimed the IP, it can be released manually:

    ```shell
    calicoctl ipam release --ip=10.244.0.100
    ```

    > NOTE: Be sure to confirm that no Pod is using this IP.

### node

- View node status

    ```shell
    calicoctl node status
    ```

- node status check

    ```shell
    calicoctl node diags
    ```

More command details: `calicoctl --help`