## Summary

## Comparison with Spiderpool + ipvlan

Similarities and differences between the four models and Spiderpool + ipvlan.

| Network Mode | Self-build Cluster | Underlay IP for Pods | Dual Stack Support | Fixed Pod IP | Pod QoS | Network Policy | LoadBalancer Service Support | Multiple NICs for Pods | Costs | Other|
|----------- | -------  | -------------------------|---------|------------|---------|----------------|---------------------|------------|-------|  ----- |
| Terway VPC | Support |  ❌  |  ✅  |   ❌  |   ✅  |  ✅  | ✅ | ❌ |Lowest costs. It does not have any specific requirements for ECS instance specifications, and the number of both ENI and secondary IPs. | Rely on [CCM](https://github.com/AliyunContainerService/alicloud-controller-manager) to publish VPC routes  |
| Terway ENI | Support |  ✅  |  ✅  |   ❌  |   ✅  |  ✅  | Setting externalTrafficPolicy to Local is not supported| ❌ | Highest costs. The maximum deployment of Pods depends on the number of ENIs of the ECS instance. | The best performance with a higher cost  |
| Terway ENIIP | Not supported, only available for ACK clusters |  ✅  |  ✅  |   ❌  |   ✅  |  ✅  | ✅ | ❌ | Lower costs. The number of deployable Pods = (Number of ENIs of ECS instance - 1) * Number of secondary IPs supported by each ENI | Supports both veth and ipvlan modes, with the latter requiring a kernel version higher than 4.2  |
| Terway ENIIP-Trunking | Not supported, only available for ACK clusters |  ✅  |  ✅  |   ✅  |   ✅  |  ✅  | ✅ | ❌ | Lower costs. The number of deployable Pods = (Number of ENIs of ECS instance - 1) * Number of secondary IPs supported by each ENI | Public beta  |
| Spiderpool + ipvlan | Support |  ✅  |  ✅  |   ✅  |   ✅  |  ✅  | ✅ | ✅ | Lower costs. The number of deployable Pods = (Number of ENIs of ECS instance - 1) * Number of secondary IPs supported by each ENI | Associate the Spiderpool IP pool with the ENI's secondary IPs  |
| Calico | Support |  ✅  |  ✅   |   ✅  |   ✅  |  ✅  | ✅ |  ❌  | Lowest costs. No ECS requirements, and no limitations on the number of both ENIs and secondary IPs | Tunnel mode does not rely on CCM, while non-tunnel mode relies on it  |
| Cilium| Support |  ✅  |  ✅   |    ❌  |  ✅  | ✅  | ✅ |  ❌  | Lowest costs. No ECS requirements, and no limitations on the number of both ENIs and secondary IPs | Tunnel mode does not rely on CCM, while non-tunnel mode relies on it  |

## Q & A

1. How can I check the number of ENIs supported by different ECS instance specifications and the number of secondary IPs supported on ENIs?

    The number of supported ENIs varies based on different specifications. For detailed information, refer to the [Instance families](https://www.alibabacloud.com/help/en/ecs/user-guide/instance-families/?spm=a2c63.p38356.0.0.543f2ed20Ifi2I) documentation.

2. What is the Pod deployment density in ENIIP mode?

    The maximum number of deployable Pods is calculated as (Number of ENIs on the ECS instance - 1) multiplied by the maximum number of secondary IPs supported per ENI.

3. What are the communication issues when Pods exclusively occupy ENI network cards?

    In this mode, Pods have the best performance. However, LoadBalancer/NodePort Services with externalTrafficPolicy set to Local may encounter access issues due to inconsistent packet paths.

4. Does Alibaba Cloud support running Calico and Cilium as CNI plugins in self-built clusters?

    Alibaba Cloud supports the Flannel CNI plugin, as well as Calico and Cilium.

    - For Calico:

        Support tunnel mode (vxlan or ipip) and route mode. In tunnel mode, Pod-to-Pod communication does not rely on the CCM component, but LoadBalancer Services depend on CCM implementation. In route mode, switching the IPAM to host-local or Spiderpool is required. For more details, refer to the [Run Calico on Alibaba Cloud](aliyun-calico.md) documentation.

    - For Cilium:

        Support tunnel and native modes. In tunnel mode, Pod-to-Pod communication does not rely on the CCM component, but LoadBalancer Services depend on CCM implementation. In native mode, switching Cilium's IPAM mode to "kubernetes" is necessary. For more details, refer to the [Running Cilium on Alibaba Cloud](aliyun-cilium.md) documentation.
