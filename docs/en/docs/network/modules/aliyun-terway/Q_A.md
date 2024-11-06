---
MPTE: WANG0608GitHub
Date: 2024-08-13
---

# Comparison with Spiderpool + IPVlan and FAQs

## Comparison with Spiderpool + IPVlan

Similarities and differences between the four models and Spiderpool + IPVlan.

| CNI Mode | Self-build Cluster | Underlay IP for pods | Dual-Stack Support | Fixed pods IP | pods QoS | Network Policy | LoadBalancer Service Support | Multiple NICs for pods | Costs | Other|
| ------- | ---- | ----- | --------- | ------ | ----- | ------- | ----- | ----- | ------- | ----- |
| Terway VPC | Support |  ❌  |  ✅  |   ❌  |   ✅  |  ✅  | ✅ | ❌ |Lowest costs. It does not have any specific requirements for ECS instance specifications and for the number of both ENI and secondary IPs. | Rely on [CCM](https://github.com/AliyunContainerService/alicloud-controller-manager) to publish VPC routes  |
| Terway ENI | Support |  ✅  |  ✅  |   ❌  |   ✅  |  ✅  | Setting externalTrafficPolicy to Local is not supported| ❌ | Highest costs. The maximum deployment of pods depends on the number of ENIs of the ECS instance. | The best performance with a higher cost  |
| Terway ENIIP | Not supported, only available for ACK clusters |  ✅  |  ✅  |   ❌  |   ✅  |  ✅  | ✅ | ❌ | Lower costs. The number of deployable pods = (Number of ENIs of ECS instance - 1) * Number of secondary IPs supported by each ENI | Supports both veth and IPVlan modes, with the latter requiring a kernel version higher than v4.2  |
| Terway ENIIP-Trunking | Not supported, only available for ACK clusters |  ✅  |  ✅  |   ✅  |   ✅  |  ✅  | ✅ | ❌ | Lower costs. The number of deployable pods = (Number of ENIs of ECS instance - 1) * Number of secondary IPs supported by each ENI | Public beta  |
| Spiderpool + IPVlan | Support |  ✅  |  ✅  |   ✅  |   ✅  |  ✅  | ✅ | ✅ | Lower costs. The number of deployable pods = (Number of ENIs of ECS instance - 1) * Number of secondary IPs supported by each ENI | Associate the Spiderpool IP pool with the ENI's secondary IPs  |
| Calico | Support |  ✅  |  ✅   |   ✅  |   ✅  |  ✅  | ✅ |  ❌  | Lowest costs. It does not have any specific requirements for ECS instance specifications and for the number of both ENI and secondary IPs. | Tunnel mode does not rely on CCM, while non-tunnel mode relies on it  |
| Cilium| Support |  ✅  |  ✅  |  ❌  |  ✅  | ✅  | ✅ |  ❌  | Lowest costs. It does not have any specific requirements for ECS instance specifications and for the number of both ENI and secondary IPs. | Tunnel mode does not rely on CCM, while non-tunnel mode relies on it |

## Q & A

1. How can I check the number of ENIs supported by different ECS instance specifications and the
   number of secondary IPs supported on ENIs?

    The number of supported ENIs varies based on different specifications. For detailed information,
    refer to the [Instance families](https://www.alibabacloud.com/help/en/ecs/user-guide/instance-families/?spm=a2c63.p38356.0.0.543f2ed20Ifi2I).

2. What is the pod deployment density in ENIIP mode?

    Number of deployable pods = (Number of ECS instances ENIs - 1) * Maximum number of secondary IPs supported per ENI.

3. What are the communication issues when pods exclusively occupy ENI network cards?

    In this mode, pods have the best performance. However, LoadBalancer/NodePort Services with
    externalTrafficPolicy set to Local may encounter access issues due to inconsistent packet paths.

4. Does Alibaba Cloud support running Calico and Cilium as CNI plugins in self-built clusters?

    Alibaba Cloud supports the Flannel CNI plugin, as well as Calico and Cilium.

    - For Calico:

        Support tunnel mode (VXLAN or IPIP) and route mode. In tunnel mode, pod-to-pod communication
        does not rely on the CCM component, but LoadBalancer Services depend on CCM implementation.
        In route mode, switching the IPAM to host-local or Spiderpool is required. For more details,
        refer to the [Run Calico on Alibaba Cloud](aliyun-calico.md).

    - For Cilium:

        Support tunnel and native modes. In tunnel mode, pod-to-pod communication does not rely on
        the CCM component, but LoadBalancer Services depend on CCM implementation. In native mode,
        switching Cilium IPAM mode to kubernetes is necessary. For more details, refer to the
        [Running Cilium on Alibaba Cloud](aliyun-cilium.md).
