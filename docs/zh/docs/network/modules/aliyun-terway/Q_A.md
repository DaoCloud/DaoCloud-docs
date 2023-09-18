# 总结

## 与 Spiderpool + IPVlan 的比较

四种模式与 Spiderpool + IPVlan 的异同点:

|  网络模式    |  是否支持自建集群  | Pod 的 IP 是否为 Underlay IP | 双栈支持 | 固定 Pod IP |  Pod Qos | Network Policy | LoadBalancer 服务支持 | Pod 多网卡 | 成本 |  其他 |
|----------- | -------  | -------------------------|---------|------------|---------|----------------|---------------------|------------|-------|  ----- |
| Terway VPC | 支持 |  ❌  |  ✅  |   ❌  |   ✅  |  ✅  | ✅ | ❌ | 最低，对 ECS 规格无要求，对弹性网卡和辅助IP的数量不作要求 | 需要依赖 [CCM](https://github.com/AliyunContainerService/alicloud-controller-manager) 组件发布 VPC 路由  |
| Terway ENI | 支持 |  ✅  |  ✅  |   ❌  |   ✅  |  ✅  | 不支持设置externalTrafficPolicy 为Local | ❌ | 最高，可部署 Pod 数量取决于 ECS 实例的弹性网卡数量 | 性能最好, 成本最高  |
| Terway ENIIP | 不支持, 只 ACK 集群支持 |  ✅  |  ✅  |   ❌  |   ✅  |  ✅  | ✅ | ❌ | 较低，可部署 Pod 数量 = (ECS 实例的弹性网卡数量 - 1) * 每个 ENI 支持的辅助 IP 数量 | 支持 veth 和 IPVlan 模式，IPVlan 模式内核版本大于4.2  |
| Terway ENIIP-Trunking | 不支持, 只 ACK 集群支持 |  ✅  |  ✅  |   ✅  |   ✅  |  ✅  | ✅ | ❌ | 较低，可部署 Pod 数量 = (ECS 实例的弹性网卡数量 - 1) * 每个 ENI 支持的辅助 IP 数量 | 正在公测中  |
| Spiderpool + IPVlan | 支持 |  ✅  |  ✅  |   ✅  |   ✅  |  ✅  | ✅ | ✅ | 较低，可部署 Pod 数量 = (ECS 实例的弹性网卡数量 - 1) * 每个 ENI 支持的辅助 IP 数量 | 需要将 Spiderpool IP池与ENI的辅助IP对应  |

## Q & A

* 如何查看 ECS 不同实例规格支持的 ENI 数量及 ENI 上支持的辅助 IP 数量？

> 不同规格支持数量不同，可参考 [实例规格族](https://help.aliyun.com/zh/ecs/user-guide/overview-of-instance-families?spm=a2c4g.11186623.4.1.67827940QQYeXI&scm=20140722.H_25378._.ID_25378-OR_rec-V_1) 获取详细信息。

* ENIIP 模式下，Pod 的部署密度如何？

> 可部署Pod数量 = ( ECS 实例 ENI 数量 - 1 ) * 每个 ENI 支持的最大辅助 IP 数量。

* Pod 独占 ENI 网卡时，有哪些通信问题？

> 此模式下，Pod 拥有最佳性能。但对于设置 externalTrafficPolicy 为 Local 的 LoadBalancer/NodePort Service，会存在因来回路径不一致，导致无法访问的问题。

* 阿里云自建集群是否支持运行 Calico 和 Cilium 作为 CNI 插件？

> 阿里云原生支持 Flannel CNI 插件，除此之外也支持 Calico 和 Cilium 运行。
>> 对于 Calico:
> - 只支持隧道模式(vxlan or ipip)，不支持路由模式。隧道模式下 Pod 之间的通信不依赖 CCM 组件，但 LoadBalancer Service 依赖 CCM 实现。
>> 对于 Cilium:
> - 只支持 tunnel 模式，不支持 native 模式，Pod 通信不依赖 CCM 组件，但 LoadBalancer Service 依赖 CCM 实现。