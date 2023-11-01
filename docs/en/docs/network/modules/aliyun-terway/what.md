# Terway Network Introduction

## VPC

In the VPC mode, the IP addresses of Pods in the cluster are allocated from a global virtual subnet that is not associated with any specific VPC network. To enable cross-node communication for Pods, the VPC routing needs to be configured using the [CCM component](https://github.com/AliyunContainerService/alicloud-controller-manager).

![vpc](../../images/vpc_connection.jpeg)

- External access for Pods requires forwarding through eth0 to the host before being further routed.
- Communication between Pods on the same node does not rely on VPC networking; it leverages direct routing between the Pod and the node.
- For cross-node communication, traffic needs to be routed through the VPC network. Therefore, the CCM component needs to configure VPC routing across nodes.
- The IP addresses assigned to Pods are virtual and do not belong to the VPC IP range, similar to other CNIs like Calico.

For deployment and usage instructions, please refer to [VPC Mode Usage](usage.md#vpc-mode)

## ENI

In the ENI mode, Terway directly attaches the ENI of ECS instances to the network namespace of Pods, ensuring optimal performance for Pods. However, a limitation of this mode is that the number of deployable Pods is constrained by the available ECS instances. In this mode, the IP subnet of Pods aligns with the host's subnet.

![eni](../../images/eni_connection.jpeg)

- Pods have two network interfaces: eth0 and veth1. The default route for Pods is set to eth0, enabling external access through eth0 to the VPC network. To access Service, the routing is set on veth1. Therefore, traffic from the Pod to Services must first be forwarded through veth1 to the host, and then routed through the host's network stack to reach the destination.
- In this mode, the maximum number of deployable Pods is determined by the number of available ENIs on the ECS instance. Specifically, the number of Pods equals the number of ENIs on the ECS instance.
- With exclusive ENI per Pod in this mode, it ensures optimal performance for Pods.

For deployment and usage instructions, please refer to [ENI Mode Usage](usage.md#eni-mode)

## ENIIP

The ENI mode allows Pods to have dedicated use of an ENI, resulting in optimal performance. However, a drawback of this mode is that it has a lower Pod deployment density. ENIs support the configuration of multiple secondary IP addresses. Depending on the instance type, a ENI can be assigned 6-20 secondary IPs. The ENIIP mode leverages these secondary IP addresses and assigns them to containers, significantly enhancing the scalability and density of Pod deployments. Terway provides two network connectivity options: **veth pair** policy routing and **ipvlan**.

### Veth-pair

In the veth-pair mode, external access from Pods is forwarded through eth0 to the host, and then further routed to the VPC network. Similar to the VPC mode, the veth-pair mode establishes network connectivity between the host and Pods using a pair of veth devices. However, unlike the VPC routing method, the IP address of the Pods is derived from the secondary IP addresses of the ENI. To ensure proper routing, policy-based routing needs to be configured on the node so that traffic from the secondary IP addresses is correctly forwarded through the associated ENI:

![eniip-veth](../../images/eniip_veth.png)

- The IP addresses of the Pods belong to the same subnet as the host
- The traffic from Pods to Services is routed through the host
- Each ENI corresponds to a policy route on the host, ensuring that traffic originating from Pods is correctly forwarded through the associated ENI
- This mode relies on the Calico Felix component to implement network policies

> Currently, the deployment of ENIIP + Veth mode is not available for self-built clusters and is not recommended.

### ipvlan

In the ipvlan mode, Terway leverages the Cilium CNI chaining. It uses ipvlan as the Main  CNI to create multiple virtual subinterfaces from an interface. Terway binds the secondary IP addresses of the ENI to different ipvlan subinterfaces, enabling network connectivity. Cilium acts as the meta CNI, attaching eBPF programs to the subinterfaces for accelerated Service access and NetworkPolicy enforcement. This mode simplifies the ENIIP network structure and provides better performance compared to veth pair policy routing. Kernel version 4.2 or higher is required.

![eniip-ipvlan](../../images/terway_cilium.png)

- ipvlan operates in L2 mode
- Each ENI used by Pods has a corresponding subinterface, resolving communication issues between parent and child interfaces.
- Each Pod has a single eth0 interface, and its gateway is directed to the VPC network. This allows Pods to access external resources without passing through host forwarding.
- Cilium handles Service resolution and NetworkPolicy enforcement.
- Kernel version 4.2 or higher is necessary.

> ENIIP + ipvlan mode is not supported in self-built clusters due to communication issues

## ENI-Trunking (Public Beta)

In the above mode, the virtual switches and security groups available to Pods are at cluster level, and fixed IPs for Pods are not supported. ENI-Trunking supports declaring Pod-level network configurations via a set of CRDs and binding them to Pods via PodSelector, which allows you to:

- Configure independent virtual switches, security groups, etc. for a group of Pods
- Supports fixed IPs for StatefulSet Pods

Limitations:

- Currently in public beta, not yet GA
- Only [some machines](https://www.alibabacloud.com/help/en/ecs/user-guide/instance-families/?spm=a2c63.p38356.0.0.781a2ed2JtOesX) are supported
- Only supported in ENIIP mode, but can coexist with it

CRD:

- PodNetworking: custom resources introduced in trunk mode specify the configuration information of a network plane. A network plane can be configured with independent vSwitches, security groups, and other information. Multiple network planes can be configured within a cluster. PodNetworking matches Pods with a label selector and the matched Pods will use trunking mode.

```yaml
apiVersion: network.alibabacloud.com/v1beta1
kind: PodNetworking
metadata:
  name: test-networking
spec:
  allocationType:
    type: Elastic/Fixed # Fixed: the fixed IP policy only applies to stateful Pods. 
    releaseStrategy: TTL
    releaseAfter: "5m0s"
  selector:
    podSelector:
      matchLabels:
        foo: bar
    namespaceSelector:
      matchLabels:
        foo: bar
  vSwitchOptions:
    - vsw-aaa
  securityGroupIDs:
    - sg-aaa
```

When a CR instance is created, Terway performs state synchronization. Once the synchronization is complete, the status is set to Ready. Pods can only be used in the Ready state:

```yaml
apiVersion: network.alibabacloud.com/v1beta1
kind: PodNetworking
...
status:
  status: Ready   <---- status
  updateAt: "2023-07-19T10:45:31Z"
  vSwitches:
    - id: vsw-bp1s5grzef87ikb5zz1px
      zone: cn-hangzhou-i
    - id: vsw-bp1sx0zhxd6bw6vpt0hbl
      zone: cn-hangzhou-i
```

- PodENI: Terway uses PodENI to record the network information for each Pod. In trunk mode, each pod has a corresponding and automatically created resource with the same name that cannot be modified.

```yaml
apiVersion: network.alibabacloud.com/v1beta1
kind: PodENI
...
spec:
  allocation:
    eni:
      id: eni-bp16h6wuzpa9w2vdm5dn     <--- pod's eni id
      mac: 00:16:3e:0d:7b:c2
      zone: cn-hangzhou-i
    ipType:
      releaseAfter: 0s
      type: Elastic                    <--- podIP allocation policies
    ipv4: 192.168.51.99
status:
  instanceID: i-bp1dkga3et5atja91ixt   <--- ecs instance ID
  podLastSeen: "2021-07-19T11:23:55Z"
  status: Bind
  trunkENIID: eni-bp16h6wuzpa9utho0t2o
```

Data flow:

![eniip-trunking](../../images/eni_trunking.png)

- Each ECS node is allocated an ENI for trunking, similar to a trunk port on a traditional switch.
- All external access from Pods is forwarded through the host and then routed to the target ENI via the host's trunking ENI. Terway plugin adds or removes VLAN tags in the trunking ENI's TC hook, and packets are matched to the target ENI based on the VLAN tag.

![eni_trunking_tc](../../images/eni_trunking_tc.png)

> ENIIP-Trunking mode is not supported in self-built clusters.
