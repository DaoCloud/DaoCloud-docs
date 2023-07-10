# What is Multus-underlay

`Multus-underlay` is based on `Multus` and with some Underlay type CNI plug-ins (such as MacVLAN or SR-IOV CNI, etc.), it can insert multiple network cards into a Pod.
In addition, `Multus-underlay` also solves some communication problems of Underlay CNI.
For example, when MacVLAN is used as a CNI, it cannot directly communicate with the cluster ClusterIP, and it cannot directly communicate with the host MacVLAN Master interface (this is a limitation of Linux MacVLAN technology).

## solved problem

- Pods of type Underlay CNI cannot access the cluster ClusterIP
- Pods of type Underlay CNI cannot pass the health check

## Included components

Multus-underlay consists of the following components:

- Multus: schedule multiple CNI plug-ins, and insert one or more network cards for Pods as needed
- Meta-plugins: including Veth and Router two plugins to solve some communication problems of Underlay CNI
- SR-IOV CNI (optional): Optional installation of SR-IOV CNI, but requires hardware support

### Meta-plugins

[Meta-plugins](https://github.com/spidernet-io/cni-plugins) contains two Meta plugins.
They are `Veth` and `Router`, which are called by CRI in the form of CNI-Chain. Called after the MacVLAN/SR-IOV-type plug-in calls are completed,
Solve various communication problems by setting some rules in the Pod's NetNs.

### Veth-Plugin

The Veth plugin is somewhat similar to [ptp](https://github.com/containernetworking/plugins/tree/main/plugins/main/ptp), by adding a pair of Veth-Peer devices in Pod NetNs, and hijacking from the host, Traffic in the cluster passes through Veth devices.
And cluster north-south traffic still goes through `eth0`. The following is an example configuration of the veth plugin with MacVLAN's multus CRD instance:

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
                "master": "enp4s0f0np0", # macvlan master interface
                "mode": "bridge",
                "ipam": {
                    "type": "spiderpool", # ipam uses spiderpool
                    "log_level": "DEBUG",
                    "log_file_path": "/var/log/spidernet/spiderpool.log",
                    "log_file_max_size": 100,
                    "log_file_max_age": 30,
                    "log_file_max_count": 10
                }
            },{
                "type": "veth", # veth is called by cni-chain
                "service_hijack_subnet": ["172.96.0.0/18","2001:4860:fd00::/108"], # The network segment of the cluster service, including IPv4 and IPv6
                "overlay_hijack_subnet": ["10.240.0.0/12","fd00:10:244::/96"], # collection of network segments for cluster pods
                "additional_hijack_subnet":[], # Customizable network segment, the data packets accessing the network segment of this collection will be sent from the veth device to the host first, and then forwarded by the host.
                "rp_filter": {
                    "set_host": true,
                    "value": 0
                },
                "migrate_route": -1, # The value range `-1,0,1`, the default is -1, indicating whether to move the default route of the newly added network card to a new route table. -1 means automatic migration by network card name (eth0 < net1 < net2), 0 means no migration, -1 means forced migration.
                "log_options": { # log write to file
                  "log_level": "debug",
                  "log_file": "/var/log/meta-plugins/veth.log"
                }
            }
        ]
    }
```

### Router-Plugin

The Router plug-in sets some routing rules in Pod Netns, so that the data packets from the host and the cluster are forwarded from the Pod's eth0 (the network card created by the default CNI), while the data packets from outside the cluster are forwarded from the network card created by MacVLAN/SRIOV .
The following is an example configuration of a Multus CRD instance with the Router plug-in and MacVLAN:

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
        "name": "macvlan-overlay", # macvlan main interface
        "plugins": [
            {
                "type": "macvlan",
                "master": "enp4s0f0np0",
                "mode": "bridge",
                "ipam": {
                    "type": "spiderpool", # ipam uses spiderpool
                    "log_level": "DEBUG",
                    "log_file_path": "/var/log/spidernet/spiderpool.log",
                    "log_file_max_size": 100,
                    "log_file_max_age": 30,
                    "log_file_max_count": 10
                }
            },{
                "type": "router", # The router plug-in is called by cni-chain
                "overlay_interface": "eth0",
                "migrate_route": -1, # The value range `-1,0,1`, the default is -1, indicating whether to move the default route of the newly added network card to a new route table. -1 means automatic migration by network card name (eth0 < net1 < net2), 0 means no migration, -1 means forced migration.
                "skip_call": false,
                "service_hijack_subnet": ["172.96.0.0/18","2001:4860:fd00::/108"], # The network segment of the cluster service, including IPv4 and IPv6
                "overlay_hijack_subnet": ["10.240.0.0/12","fd00:10:244::/96"], # collection of network segments for cluster pods
                "additional_hijack_subnet":[], # Customizable subnet. Data packets accessing the network segment of this collection will be sent from the eth0 device to the host first, and then forwarded by the host.
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