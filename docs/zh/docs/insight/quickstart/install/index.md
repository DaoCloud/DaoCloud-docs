# 开始观测

DCE 5.0 平台实现了对多云多集群的纳管，并支持创建集群。在此基础上，可观测性 Insight 作为多集群统一观测方案，通过部署 insight-agent 插件实现对多集群观测数据的采集，并支持通过 DCE 5.0 可观测性产品实现对指标、日志、链路数据的查询。

 __insight-agent__ 是可观测性实现对多集群数据采集的工具，安装后无需任何修改，即可实现对指标、日志以及链路数据的自动化采集。

通过 __容器管理__ 创建的集群默认会安装 insight-agent，故在此仅针对接入的集群如何开启观测能力提供指导。

- [在线安装 insight-agent](install-agent.md)

可观测性 Insight 作为多集群的统一观测平台，其部分组件的资源消耗与创建集群的数据、接入集群的数量息息相关，在安装 insight-agent 时，需要根据集群规模对相应组件的资源进行调整。

1. 根据创建集群的规模或接入集群的规模，调整 insight-agent 中采集组件 __Prometheus__ 的 CPU 和内存，请参考: [Prometheus 资源规划](../res-plan/prometheus-res.md)

2. 由于多集群的指标数据会统一存储，则需要 DCE 5.0 平台管理员根据创建集群的规模、接入集群的规模对应调整 vmstorage 的磁盘，请参考：[vmstorage 磁盘容量规划](../res-plan/vms-res-plan.md)。

- 如何调整 vmstorage 的磁盘，请参考：[vmstorge 磁盘扩容](../res-plan/modify-vms-disk.md)。

由于 DCE 5.0 支持对多云多集群的纳管，insight-agent 目前也完成了部分验证，由于监控组件冲突问题导致在 DCE 4.0 集群和 Openshift 4.x 集群中安装 insight-agent 会出现问题，若您遇到同样问题，请参考以下文档：

- [在 DCE 4.0.x 安装 insight-agent](../other/install-agentindce.md)
- [在 Openshift 4.x 安装 insight-agent](../other/install-agent-on-ocp.md)

目前，采集组件 insight-agent 已对当前主流的 Kubernetes 版本完成了部分的功能测试，请参考：

- [kubernetes 集群兼容性测试](../../compati-test/k8s-compatibility.md)
- [Openshift 4.x 集群兼容性测试](../../compati-test/ocp-compatibility.md)
- [Rancher 集群兼容性测试](../../compati-test/rancher-compatibility.md)
