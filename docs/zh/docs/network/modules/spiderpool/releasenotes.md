# Spidernet Release Notes

本页列出 Spidernet 的 Release Notes，便于您了解各版本的演进路径和特性变化。

其中包含的 Spiderpool 是 DaoCloud 自研开源的 IPAM 模块，请参考 [Spiderpool Release Notes](https://github.com/spidernet-io/spiderpool/releases)。

## 2023-08-30

### v0.9.0

适配 **Spiderpool 版本** : `v0.7.0`

#### 新功能

- **新增** SpiderMultusConfig 的 Annotation Webhook 校验
- **新增** 在双栈 SpiderSubnet自动池功能下分配单栈 IP
- **新增** IPAM 核心算法优化，优先在亲和的池中分配IP
- **新增** SpiderSubnet 自动池功能下，孤儿 IPPool 的创建
- **新增** Multus  卸载钩子移除 CNI 配置文件
- **新增** Coordinator 支持自动模式(默认)，这将自动检测 Coordinator 的工作模式，不再需要手动指定 Underlay 或 Overlay。
 相同的 multus CNI 配置，可以同时被用作 Underlay 或 Overlay 模式。
- **新增** 通过 `spidermultusconfig` 配置 `ovs-cni`

#### 修复

- **修复** 无控制器 Pod 打上自动池 Annotation 无法启动的 Bug
- **修复**  Coordinator Webhook 校验 Bug
- **修复**  Coordinator 监听 Calico 资源 Bug
- **修复**  CRD 错误的 VLAN 范围
- **修复**  自动池资源名字长度限制
- **修复**  Coordinator 添加路由失败
- **修复** 如果 `spidercoordinator.status.phase` 未 Ready, 清理已收集的集群子网信息，并且阻止 Pod 创建
- **修复** 清理 `spidermultusconfig` 中 `sriov-cni` 的 `resourceName` 字段
- **修复** 验证 `spidermultusconfig` 中自定义 CNI 配置文件是否是合法的 Json 格式
- **修复** 所有节点与 Pod 的路由都统一的被创建在主机的 `table500` 中，而不是每一个 Pod 独占一个 `table`

## 2023-07-28

### v0.8.1

适配 **Spiderpool 版本** : `v0.6.0`

#### 新功能

- **新增** Spiderpool CR 中新增 nodeName、multusName 字段，用于支持节点拓扑，能按需配置网络
- **新增** Spiderpool 提供了 SpiderMultusConfig CR ，简化书写 JSON 格式的 Multus CNI 配置，自动管理 Multus NetworkAttachmentDefinition CR
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

适配 **Spiderpool 版本** : `v0.5.0`

#### 优化

- **新增** `spidernet` 定义 Multus API
- **优化** `spidernet` e2e 稳定性
- **修复** `spidernet` `goproduct` Proxy Config
- **优化** `spidernet` 默认采用 2 副本

## 2023-05-28

### v0.7.0

适配 **Spiderpool 版本** : `v0.4.1`

#### 修复

- **修复** `spidernet` 子网根据 IP 排序问题。

## 2023-04-28

### v0.6.0

适配 **Spiderpool 版本** : `v0.4.1`

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

适配 **SpiderPool 版本** : `v0.4.0`

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

- **优化** 资源使用量，降低 CPU,内存请求量。

### v0.4.2

#### 优化

- **优化** 资源使用量，降低 CPU,内存请求量。
- **优化** 在有 IP 占用的情况下,不能删除 Subnet 或 IPPool。
- **优化** 分页问题

### v0.4.1

#### 新功能

- **新增** 基于界面进行 IP 预留，IP 解除预留等功能。

- **新增** IP 池管理，可基于界面创建、编辑、删除。

- **新增** 工作负载使用容器多网卡功能，并可选择 IP 池 并固定。

- **新增** 应用固定 IP 池可用 IP /总 IP 数量查看。

#### 优化

- **优化** 资源使用量，降低 CPU,内存请求量。
