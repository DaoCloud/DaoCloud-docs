# nmstate

随着混合云的出现，节点网络设置变得更加具有挑战性。不同的环境有不同的网络要求。容器网络接口（CNI）标准实现了不同的解决方案，它解决了集群中 Pod 的通讯问题, 包括为其设置 IP 和 创建路由等。

然而，在所有这些情况下，节点必须在pod被安排之前设置好网络。在一个动态的、异质的集群中设置网络，具有动态的网络需求，这本身就是一个挑战。

nmstate 这个项目旨在通过 k8s CRD 的方式配置节点上的网络, 它可以一定程度上简化网络配置。

## 限制

`nmstate` 依赖 NetworkManager , 所以不是所有的 Linux 发行版都支持, 比如 ubuntu 等。并且 NetworkManager 的版本必须 `>= 1.20` 

可通过下面的方式检查 NetworkManager 的版本:

```shell
[root@master ~]# /usr/sbin/NetworkManager --version
1.22.8-4.el8
```

## 安装

```shell
kubectl apply -f https://github.com/nmstate/kubernetes-nmstate/releases/download/v0.74.0/nmstate.io_nmstates.yaml
kubectl apply -f https://github.com/nmstate/kubernetes-nmstate/releases/download/v0.74.0/namespace.yaml
kubectl apply -f https://github.com/nmstate/kubernetes-nmstate/releases/download/v0.74.0/service_account.yaml
kubectl apply -f https://github.com/nmstate/kubernetes-nmstate/releases/download/v0.74.0/role.yaml
kubectl apply -f https://github.com/nmstate/kubernetes-nmstate/releases/download/v0.74.0/role_binding.yaml
kubectl apply -f https://github.com/nmstate/kubernetes-nmstate/releases/download/v0.74.0/operator.yaml
```

在安装完成后, 创建 CR 实例, 触发 nmstate controller 工作:

```yaml
cat <<EOF | kubectl create -f -
apiVersion: nmstate.io/v1
kind: NMState
metadata:
  name: nmstate
EOF
```

当安装完成之后, 可通过下面的方式查看是否正常工作:

```shell
[root@10-6-185-30 ~]# kubectl get nns
NAME          AGE
10-6-185-30   3d4h
10-6-185-40   3d4h
```

每一个 nns 对象都是 nmstate 搜集该节点的所有网络信息, 包括所有接口、IP 地址、路由等。

## 使用

examples:

- 为某个节点的网卡配置 IP 地址:

```shell
cat << EOF | kubectl apply -f -
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: static-ip
spec:
  nodeSelector:
    kubernetes.io/hostname: node02
  desiredState:
    interfaces:
    - name: eth1
      type: ethernet
      state: up
      ipv4:
        address:
        - ip: 10.244.0.2
          prefix-length: 24
        dhcp: false
        enabled: true
```

- `nodeSelector`: 表示此网络配置将会在哪个节点上生效
- `desiredState`: 表示期望的配置,包括网卡、IP等等

- 创建 vlan 子接口:

```shell
cat << EOF | kubectl apply -f -
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: vlan
spec:
  desiredState:
    interfaces:
    - name: eth1.102
      type: vlan
      state: up
      vlan:
        id: 102
        base-iface: eth1
      ipv4:
        dhcp: true
        enabled: true
```

这将会在集群所有节点创建一个名为 eth1.102 的 vlan 子接口

- 创建 bond 接口

```shell
cat << EOF | kubectl apply -f -
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: bond-vlan30
spec:
  nodeSelector:
    kubernetes.io/hostname: 10-6-185-30
  desiredState:
    interfaces:
    - name: bond0
      type: bond
      state: up
      ipv4:
        dhcp: false
        address:
        - ip: 172.39.0.30
          prefix-length: 16
        enabled: true
      ipv6:
        address:
        - ip: fc00:172:39::30
          prefix-length: 64
        enabled: true
      link-aggregation:
        mode: active-backup
        port:
        - ens161
        - ens256
    - name: bond0.144
      type: vlan
      state: up
      ipv4:
        address:
        - ip: 172.144.185.30
          prefix-length: 16
        dhcp: false
        enabled: true
      ipv6:
        address:
        - ip: fd00:144::172:144:185:30
          prefix-length: 64
        enabled: true
      vlan:
        base-iface: bond0
        id: 144
    - name: bond0.145
      type: vlan
      state: up
      ipv4:
        address:
        - ip: 172.145.185.30
          prefix-length: 16
        dhcp: false
        enabled: true
      ipv6:
        address:
        - ip: fd00:145::172:144:185:30
          prefix-length: 64
        enabled: true
      vlan:
        base-iface: bond0
        id: 145
```

创建这个对象之后, 它会做这几件事:

    - 基于ens161 和 ens256, 创建一个 bond0 接口, 模式为主备。并配置IP地址
    - 基于 bond0 , 分别创建 vlan 子接口: bond0.144 和 bond0.145, 并配置 IP 地址。

对象创建后, 可通过下面的方式检查是否配置完成及成功:

```shell
[root@10-6-185-30 ]# kubectl get nncp
NAME          STATUS      REASON
bond-vlan30   Available   SuccessfullyConfigured
```

这说明已经配置成功, 再检查接口:

```shell
[root@10-6-185-30 ]# ip a s bond0.144
90: bond0.144@bond0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 00:50:56:b4:e9:41 brd ff:ff:ff:ff:ff:ff
    inet 172.144.185.30/16 brd 172.144.255.255 scope global noprefixroute bond0.144
       valid_lft forever preferred_lft forever
    inet6 fd00:144::172:144:185:30/64 scope global noprefixroute
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:feb4:e941/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
```
