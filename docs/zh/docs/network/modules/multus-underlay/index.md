# 什么是 Multus-underlay

`Multus-underlay` 基于 `Multus` 并搭配一些 Underlay 类型的 CNI 插件（如 MacVLAN 或 SR-IOV CNI 等)，可为 Pod 插入多张网卡。
此外，`Multus-underlay` 还解决了 Underlay CNI 的一些通信问题。
比如当 MacVLAN 作为 CNI 时，它无法与集群 ClusterIP 直接通信，并且它也无法直接与主机 MacVLAN Master 接口通信的（这是 Linux MacVLAN 技术的限制）。

> **Warning⚠️**
> 
>  目前 Multus-underlay 已经被标记为 deprecated 状态, 可能在未来被移除, 目前已经不再更新

## 解决的问题

- Underlay CNI 类型的 Pod 无法访问集群 ClusterIP
- Underlay CNI 类型的 Pod 无法通过健康检测

## 包含的组件

Multus-underlay 包含下面几个组件：

- Multus：调度多个 CNI 插件，按需为 Pod 插入一张或者多张网卡
- Meta-plugins：包括 Veth 和 Router 两个插件，解决 Underlay CNI 的一些通信问题
- SR-IOV CNI（可选）：可选安装 SR-IOV CNI，但需要硬件支持

### Meta-plugins

[Meta-plugins](https://github.com/spidernet-io/cni-plugins) 包含两个 Meta 插件。
分别是 `Veth` 和 `Router`，它们以 CNI-Chain 的方式被 CRI 调用。在 MacVLAN/SR-IOV 类的插件调用完成之后再调用，
通过在 Pod 的 NetNs 中设置一些规则，解决各种通信问题。

### Veth-Plugin

Veth 插件与 [ptp](https://github.com/containernetworking/plugins/tree/main/plugins/main/ptp) 有些类似，通过在 Pod NetNs 中添加一对 Veth-Peer 设备，并劫持来自主机、集群中的流量从 Veth 设备通过。
而集群南北向流量仍然从 `eth0` 通过。下面是 veth 插件搭配 MacVLAN 的 multus CRD 实例的配置示例：

```yaml
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  name: macvlan-standalone
  namespace: kube-system
spec:
  config: |-
    {
        "cniVersion": "0.3.1",
        "name": "macvlan-standalone",
        "plugins": [
            {
                "type": "macvlan",
                "master": "enp4s0f0np0",  # macvlan 主接口
                "mode": "bridge",
                "ipam": {
                    "type": "spiderpool", # ipam 使用 spiderpool
                    "log_level": "DEBUG",
                    "log_file_path": "/var/log/spidernet/spiderpool.log",
                    "log_file_max_size": 100,
                    "log_file_max_age": 30,
                    "log_file_max_count": 10
                }
            },{
                "type": "veth", # veth 以 cni-chain 的方式调用
                "service_hijack_subnet": ["172.96.0.0/18","2001:4860:fd00::/108"], # 集群 service的网段, 包括 IPv4 和 IPv6
                "overlay_hijack_subnet": ["10.240.0.0/12","fd00:10:244::/96"],  # 集群 pod 的网段集合
                "additional_hijack_subnet":[], # 可自定义的网段,访问此集合的网段的数据包将会先从 veth 设备送往主机, 再由主机进行转发。
                "rp_filter": {  
                    "set_host": true,
                    "value": 0
                },
                "migrate_route": -1, # 取值范围`-1,0,1`, 默认为 -1, 表示是否将新增网卡的默认路由移动到一个新的 route table中去。-1 表示通过网卡名自动迁移(eth0 < net1 < net2)，0 为不迁移，-1表示强制迁移。
                "log_options": {  # 日志写入文件
                  "log_level": "debug",
                  "log_file": "/var/log/meta-plugins/veth.log"
                }
            }
        ]
    }
```

### Router-Plugin

Router 插件通过在 Pod Netns 中设置一些路由规则，使来自主机、集群内的数据包从 Pod 的 eth0（默认 CNI 创建的网卡）转发，而来自于集群外的数据包从 MacVLAN/SR-IOV 创建的网卡转发。
下面是 Router 插件搭配 MacVLAN 的 Multus CRD 实例的配置示例：

```yaml
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  name: macvlan-vlan0-overlay 
  namespace: kube-system
spec:
  config: |-
    {
        "cniVersion": "0.3.1",
        "name": "macvlan-overlay",  # macvlan 主接口
        "plugins": [
            {
                "type": "macvlan",
                "master": "enp4s0f0np0", 
                "mode": "bridge",
                "ipam": {
                    "type": "spiderpool",  # ipam 使用 spiderpool
                    "log_level": "DEBUG",
                    "log_file_path": "/var/log/spidernet/spiderpool.log",
                    "log_file_max_size": 100,
                    "log_file_max_age": 30,
                    "log_file_max_count": 10
                }
            },{
                "type": "router", # router 插件 以 cni-chain 的方式调用
                "overlay_interface": "eth0",
                "migrate_route": -1,  # 取值范围`-1,0,1`, 默认为 -1, 表示是否将新增网卡的默认路由移动到一个新的 route table 中去。-1 表示通过网卡名自动迁移(eth0 < net1 < net2)，0 为不迁移，1 表示强制迁移。
                "skip_call": false,
                "service_hijack_subnet": ["172.96.0.0/18","2001:4860:fd00::/108"], # 集群 service的网段, 包括 IPv4 和 IPv6
                "overlay_hijack_subnet": ["10.240.0.0/12","fd00:10:244::/96"],  # 集群 pod 的网段集合
                "additional_hijack_subnet":[], # 可自定义的网段。访问此集合的网段的数据包将会先从 eth0 设备送往主机, 再由主机进行转发。
                "rp_filter": {
                    "set_host": true,
                    "value": 0
                },
                "log_options": {
                  "log_level": "debug",
                  "log_file": "/var/log/meta-plugins/router.log"
                }
            }
        ]
    }
```
