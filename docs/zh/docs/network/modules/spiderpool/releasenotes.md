# Spidernet Release Notes

本页列出 Spidernet 的 Release Notes，便于您了解各版本的演进路径和特性变化。

*[Spidernet]: DaoCloud 网络模块的内部开发代号
*[Spiderpool]: 一个基于 K8s 构建的 Underlay 和 RDMA 网络方案，兼容裸金属、虚拟机和公有云等运行环境，目前已入选 CNCF Sandbox
*[EgressGateway]: DaoCloud 在 GitHub 上开源的、基于 K8s 构建的出口网关方案
*[IPAM]: IP Address Management 的缩写，即 IP 地址管理
*[SR-IOV]: Single Root IO Virtualization 的缩写，一种网卡虚拟化的技术
*[RDMA]: Remote Direct Memory Access 的缩写，即远程直接内存访问，这是一个支撑 LLM 大模型和 GPT 的热门技术

## 2023-12-30

### v0.12.1

- 适配 **Spiderpool v0.9.0**
- 适配 **EgressGateway v0.4.0**

#### 新功能

- **新增** 支持使用 InfiniBand SR-IOV CNI 和 IPoIB CNI 的 InfiniBand 网卡
- **新增** 支持查询 Spiderpool 或者 EgressGateway 的集群列表接口
- **新增** 支持在 Annotation 中有接口名称以支持多个网卡
- **新增** 支持 Multus 能够配置 SR-IOV 配置的带宽
- **新增** 支持 Multus 使用自定义类型的空配置
- **新增** 支持子网在双栈中的单 IP

#### 优化

- **优化** 为 IPAM IP 池 Annotation 使用添加验证

#### 修复

- **修复** 根据命名空间查询 IP 池接口错误
- **修复** 如果 Multus 未安装，则不更新 Multus ConfigMap
- **修复** 如果 Multus 被禁用，则不会初始化 Multus CR
- **修复** coordinator 能够确保在 Pod 的 netns 中检测到网关和 IP 冲突
- **修复** 当 Kubevirt 静态 IP 功能关闭时，Spiderpool-agent 崩溃的问题
- **修复** 禁止单个没有控制器的 Pod 使用子网功能
- **修复** 从 KubeControllerManager Pod 获取 serviceCIDR

## 2023-11-30

### v0.11.1

- 适配 **Spiderpool v0.8.1**
- 适配 **EgressGateway v0.4.0**

#### 新功能

- **新增** 支持查询 Spiderpool 与 EgressGateway 安装查询接口
- **新增** 支持 Multus CR 管理 SR-IOV CNI 开启 RDMA
- **新增** 支持创建负载中自动选择 RDMA 、SR-IOV、hugepages 等网络资源参数
- **新增** 支持 EgressGateway 使用 EIP 计数功能

#### 优化

- **优化** Spiderpool SDK 依赖

#### 修复

- **修复** IP 池关联 Multus CR 实例，需要匹配命名空间问题
- **修复** 更新 Multus CR 时未更新 Annotations 问题
- **修复** EgressGateway 引起的策略重新分配错误问题

## 2023-10-30

### v0.10.1

- 适配 **Spiderpool v0.8.0**
- 适配 **EgressGateway v0.3.0**

#### 新功能

- **新增** 支持出口网关通过节点选择器选择一组节点作为 Egress 节点，并通过指定节点转发外部流量
- **新增** 支持为节点组配置 IP 池，确保有足够可用 IP 地址，供网络中的不同节点或节点组使用
- **新增** 支持在 Calico、Flannel、Weave、Spiderpool 的网络模式下，系统为命名空间或工作负载设置
  EIP，Pod 在访问外部网络时，会统一使用此 EIP 作为出口地址
- **新增** 支持设置默认的 Egress IP 作为集群或命名空间的出口地址
- **新增** 支持通过网关策略进行出网管控，支持根据目标 CIDR 过滤出口流量
- **新增** 支持查看出口网关默认 EgressIP、EgressIP 池、节点列表以及节点 IP 地址范围
- **新增** 支持网关策略使用 Pod 标签选择器或源地址，选择要使用 Egress 的 Pods，指定特定的 Pods 遵循网关策略
- **新增** 支持查看网关策略中选择的网关、EgressIP 或节点 IP、容器组等进行网络配置管控
- **新增** 支持 EgressGateway 用于低内核版本
- **新增** Multus CR 管理界面，支持创建使用不同 Multus CNI（包括 Macvlan、IPvlan、SR-IOV、自定义）类型的 CR 实例
- **新增** Spiderpool 集成了 RDMA CNI 和 RDMA 设备插件
- **新增** `sriov network operator` 的 Chart 配置信息
- **新增** 支持为 KubeVirt 虚拟机分配静态 IP 地址
- **新增** 在 SpiderAgent 的初始化容器中安装 CNI、OVS 和 RDMA

#### 优化

- **优化** OpenTelemetry 升级版本升级至 1.19.0
- **优化** Spiderpool 初始化时，如果默认的 SpiderMultusConfig 网络不为空，将自动创建
- **优化** 所有插件构建了全新的 Docker 镜像
- **优化** 改进 GetTopController 方法
- **优化** 工作负载网络配置中 Multus CR 管理对应的 CNI 类型

#### 修复

- **修复** coordinator 通过 veth0 传递的数据包中的 eth0 源 IP 问题
- **修复** SpiderMultusConfig 在 `spidermultusconfig.spec` 为空时引发的错误
- **修复** SpiderCoordinator 在自动获取 PodCIDR 类型时的问题

## 2023-08-30

### v0.9.0

适配 **Spiderpool v0.7.0**

#### 新功能

- **新增** SpiderMultusConfig 的 Annotation Webhook 校验
- **新增** 在双栈 SpiderSubnet 自动池功能下分配单栈 IP
- **新增** IPAM 核心算法优化，优先在亲和的池中分配 IP
- **新增** SpiderSubnet 自动池功能下，孤儿 IPPool 的创建
- **新增** Multus 卸载钩子移除 CNI 配置文件
- **新增** Coordinator 支持自动模式(默认)，这将自动检测 Coordinator 的工作模式，不再需要手动指定 Underlay 或 Overlay。
  相同的 Multus CNI 配置，可以同时被用作 Underlay 或 Overlay 模式。
- **新增** 通过 `spidermultusconfig` 配置 `ovs-cni`

#### 修复

- **修复** 无控制器 Pod 打上自动池 Annotation 无法启动的 Bug
- **修复** Coordinator Webhook 校验 Bug
- **修复** Coordinator 监听 Calico 资源 Bug
- **修复** CRD 错误的 VLAN 范围
- **修复** 自动池资源名字长度限制
- **修复** Coordinator 添加路由失败
- **修复** 如果 `spidercoordinator.status.phase` 未 Ready， 清理已收集的集群子网信息，并且阻止 Pod 创建
- **修复** 清理 `spidermultusconfig` 中 `SR-IOV-cni` 的 `resourceName` 字段
- **修复** 验证 `spidermultusconfig` 中自定义 CNI 配置文件是否是合法的 Json 格式
- **修复** 所有节点与 Pod 的路由都统一的被创建在主机的 `table500` 中，而不是每一个 Pod 独占一个 `table`

## 2023-07-28

### v0.8.1

适配 **Spiderpool v0.6.0**

#### 新功能

- **新增** Spiderpool CR 中新增 nodeName、multusName 字段，用于支持节点拓扑，能按需配置网络
- **新增** Spiderpool 提供了 SpiderMultusConfig CR ，简化书写 JSON 格式的 Multus CNI 配置，
  自动管理 Multus NetworkAttachmentDefinition CR
- **新增** Spiderpool 提供了 Coordinator 插件，解决 Underlay Pod 无法访问 ClusterIP、调谐 Pod
  的路由、检测 Pod 的 IP 是否冲突、Pod 的网关是否可达等。参考
  [Coordinator 文档](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/coordinator-zh_CN.md)
- **新增** IPVlan 的深度支持，适用于任何公有云环境
- **新增** 支持多个默认 IP 池，简化使用成本
- **新增** CNI 插件 `Ifacer`，用于自动创建子接口，参考
  [Ifacer 文档](https://github.com/spidernet-io/spiderpool/blob/main/docs/usage/ifacer-zh_CN.md)
- **新增**通过 Pod 注解指定默认路由网卡
- **新增**自动池的回收开关支持，可以自定义自动池是否删除
- **优化** 集群子网弹性 IP 的支持，可以很好地解决应用在滚动更新时，旧 Pod 未删除，新 Pod 没有可用 IP 的问题

## 2023-06-28

### v0.8.0

适配 **Spiderpool v0.5.0**

#### 优化

- **新增** `spidernet` 定义 Multus API
- **优化** `spidernet` e2e 稳定性
- **修复** `spidernet` `goproduct` Proxy Config
- **优化** `spidernet` 默认采用 2 副本

## 2023-05-28

### v0.7.0

适配 **Spiderpool v0.4.1**

#### 修复

- **修复** `spidernet` 子网根据 IP 排序问题。

## 2023-04-28

### v0.6.0

适配 **Spiderpool v0.4.1**

#### 修复

- **修复** 单栈时，查看工作负载出现指针错误
- **修复** 修复添加大量 IP 时 Controller 超时
- **修复** 亲和性填写可以填写中文
- **修复** 工作负载名称与命名空间不匹配
- **修复** 固定池显示问题
- **修复** 路由删除问题
- **修复** 分页数量显示问题
- **修复** 根据 Pod 获取 IP pool 问题
- **修复** 连续快速删除的缓存问题

#### 新功能

- **新增** 创建 IP pool 时，填写 VLAN ID
- **新增** 显示 IP 总量与已用数
- **新增** `e2e` 自动使用最新版 DCE 组件

## 2023-03-28

### v0.5.0

适配 **Spiderpool v0.4.0**

#### 优化

- **优化** Spidernet API，适配 **Spiderpool v0.4.0** 新版 CRD

#### 修复

- **修复** 有状态负载使用了自动 IP 池，IP 池创建成功，IP 分配成功，查询 IP 池为空问题。
- **修复** 子网管理-删除子网， 选择删除一个子网，系统提示成功，但是刷新后这个子网还在。
- **修复** 点击几次“容器网卡”，拿不到数据问题。
- **修复** `Spidernet Chart` 中的 Spidernet-UI Service Label 不正确问题。

## 2023-02-28

### v0.4.4

#### 优化

- **优化** 调整 CPU 内存 Request 值。

#### 修复

- **修复** 有状态负载使用了自动 IP 池，IP 池创建成功，IP 分配成功，查询 IP 池为空问题。
- **修复** 子网管理-删除子网，选择删除一个子网，系统提示成功，但是刷新后这个子网还在。
- **修复** 点击几次“容器网卡”，拿不到数据问题。
- **修复** `Spidernet Chart` 中的 Spidernet-UI Service Label 不正确问题。

## 2022-11-30

### v0.4.3

#### 优化

- **优化** 资源使用量，降低 CPU，内存请求量。

### v0.4.2

#### 优化

- **优化** 资源使用量，降低 CPU，内存请求量。
- **优化** 在有 IP 占用的情况下，不能删除 Subnet 或 IPPool。
- **优化** 分页问题

### v0.4.1

#### 新功能

- **新增** 基于界面进行 IP 预留，IP 解除预留等功能。
- **新增** IP 池管理，可基于界面创建、编辑、删除。
- **新增** 工作负载使用容器多网卡功能，并可选择 IP 池 并固定。
- **新增** 应用固定 IP 池可用 IP /总 IP 数量查看。

#### 优化

- **优化** 资源使用量，降低 CPU，内存请求量。
