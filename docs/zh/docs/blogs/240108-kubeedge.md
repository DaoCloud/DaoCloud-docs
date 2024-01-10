# KubeEdge v1.15.0 发布

> 作者：[WillardHu](https://github.com/WillardHu) 和 [JiaweiGithub](https://github.com/JiaweiGithub)

KubeEdge 是 DCE 5.0 [云边协同](../kant/intro/index.md)的核心组件，DaoCloud
持续积极跟随、推进、规划 KubeEdge 的各项特性。

## 版本变更

KubeEdge v1.15.0 主要新增了 Windows 边缘节点支持、基于物模型的设备管理、DMI 数据面支持等功能，具体细节如下：

### 支持 Windows 边缘节点

随着边缘计算应用场景的不断拓展，涉及到的设备类型也越来越多，其中包括很多基于 Windows 操作系统的传感器、摄像头和工控设备等，
因此新版本的 KubeEdge 支持在 Windows 上运行边缘节点，覆盖更多的使用场景。

在 v1.15.0 版本中，KubeEdge 支持边缘节点运行在 Windows Server 2019，并且支持 Windows 容器运行在边缘节点上，
将 KubeEdge 的使用场景成功拓展到 Windows 生态。Windows 版本的 EdgeCore 配置新增了 windowsPriorityClass 字段，
默认为 NORMAL_PRIORITY_CLASS。用户可以在 Windows 边缘主机上下载 Windows 版本的 EdgeCore 安装包，
解压后执行如下命令即可完成 Windows 边缘节点的注册与接入，用户可以通过在云端执行 kubectl get nodes 确认边缘节点的状态，并管理边缘 Windows 应用。

```sh
edgecore.exe --defaultconfig > edgecore.yaml
edgecore.exe --config edgecore.yaml
```

### 基于物模型的新版本设备管理 API v1beta1 发布

v1.15.0 版本中，基于物模型的设备管理 API，包括 Device Model 与 Device Instance，从 v1alpha2 升级到了
v1beta1，新增了边缘设备数据处理相关等的配置，北向设备 API 结合南向的 DMI 接口，实现设备数据处理，API 的主要更新包括：

- Device Model 中按物模型标准新增了设备属性描述、设备属性类型、设备属性取值范围、设备属性单位等字段。
- Device Instance 中内置的协议配置全部移除，包括 Modbus、Opc-UA、Bluetooth 等。用户可以通过可扩展的
  Protocol 配置来设置自己的协议，以实现任何协议的设备接入。Modbus、Opc-UA、Bluetooth 等内置协议的 Mapper
  不会从 mappers-go 仓库移除，并且会更新到对应的最新版本，且一直维护。
- 在 Device Instance 的设备属性中增加了数据处理的相关配置，包括设备上报频率、收集数据频率、属性是否上报云端、推送到边缘数据库等字段，
  数据的处理将在 Mapper 中进行。

### 承载 DMI 数据面的 Mapper 自定义开发框架 Mapper-Framework 发布

v1.15.0 版本中，对 DMI 数据面部分提供了支持，主要承载在南向的 Mapper 开发框架 Mapper-Framework 中。
Mapper-Framework 提供了全新的 Mapper 自动生成框架，框架中集成了 DMI 设备数据管理（数据面）能力，
允许设备在边缘端或云端处理数据，提升了设备数据管理的灵活性。Mapper-Framework 能够自动生成用户的 Mapper 工程，
简化用户设计实现 Mapper 的复杂度，提升 Mapper 的开发效率。

- DMI 设备数据面管理能力支持

    v1.15.0 版本 DMI 提供了数据面能力的支持，增强边缘端处理设备数据的能力。
    设备数据在边缘端可以按配置直接被推送至用户数据库或者用户应用，也可以通过云边通道上报至云端，用户也可以通过 API
    主动拉取设备数据。设备数据管理方式更加多样化，解决了 Mapper 频繁向云端上报设备数据，易造成云边通信阻塞的问题，
    能够减轻云边通信的数据量，降低云边通信阻塞的风险。DMI 数据面系统架构如下图所示：

    ![系统架构](./images/edge01.png)

- Mapper 自动生成框架 Mapper-Framework

    v1.15.0 版本提出全新的 Mapper 自动生成框架 Mapper-Framework。框架中已经集成 Mapper 向云端注册、云端向 Mapper 下发
    Device Model 与 Device Instance 配置信息、设备数据传输上报等功能，大大简化用户设计实现 Mapper 的开发工作，便于用户体验
    KubeEdge 边缘计算平台带来的云原生设备管理体验。

### 支持边缘节点运行 Kubernetes 静态 Pod

新版本的 KubeEdge 支持了 Kubernetes 原生静态 Pod 能力，与 Kubernetes 中操作方式一致，用户可以在边缘主机的指定目录中，
以 JSON 或者 YAML 的形式写入 Pod 的 Manifests 文件，Edged 会监控这个目录下的文件来创建/删除边缘静态 Pod，并在集群中创建镜像 Pod。

静态 Pod 默认目录是 /etc/kubeedge/manifests，您也可以通过修改 EdgeCore 配置的 staticPodPath 字段来指定目录。

### 升级 Kubernetes 依赖到 v1.26

新版本将依赖的 Kubernetes 版本升级到 v1.26.7，您可以在云和边缘使用新版本的特性。

v1.15.0 更多详细信息： https://bbs.huaweicloud.com/blogs/413613

## DaoCloud 在 KubeEdge 社区做出的贡献

DaoCloud 秉承社区繁荣共建的理念，持续鼓励贡献上游，回馈社区。

### 参与的功能

- keadm 兼容 cloudcore、edgecore 历史版本 ci（[PR #5289](https://github.com/kubeedge/kubeedge/pull/5289)）、
  keadm 兼容 k8s 版本 ci（[PR #5006](https://github.com/kubeedge/kubeedge/pull/5006)）
- 新增 Device CRD Admission 校验([PR #5290](https://github.com/kubeedge/kubeedge/pull/5290))、
  开发基于物模型的新版本设备管理 API 新版本 v1beta1+编写 proposal（[PR #4983](https://github.com/kubeedge/kubeedge/pull/4983)）、
  新增 Mapper-Framework 仓库([mapper-framework](https://github.com/kubeedge/mapper-framework))、
  Mapper-Framework Config 模块重构（[PR #5219](https://github.com/kubeedge/kubeedge/pull/5219)）、
  Mapper-Framework 新增 lint check（[PR #5292](https://github.com/kubeedge/kubeedge/pull/5292)）、
  Mapper-Framework 设备初始化模块优化（[PR #5247](https://github.com/kubeedge/kubeedge/pull/5247)）
- admission 安装包支持([PR #5034](https://github.com/kubeedge/kubeedge/pull/5034)) 、
  云端 cloudcore 的升级（[PR #5229](https://github.com/kubeedge/kubeedge/pull/5229)）、
  mqtt 使用 DaemonSet 维护（[PR #5235](https://github.com/kubeedge/kubeedge/pull/5235)）
- 批量工作负载(EdgeApplication)提供更多差异化配置字段（[PR #5262](https://github.com/kubeedge/kubeedge/pull/5262)）

### 修复 bug

- 删除节点接入时拉取 pause 镜像（[PR #5312](https://github.com/kubeedge/kubeedge/pull/5312)）、
  历史版本中节点升级失败问题（[PR #5085](https://github.com/kubeedge/kubeedge/pull/5085) ）
- sedna helm 安装包 bug([PR #420](https://github.com/kubeedge/sedna/pull/420))
- 优化 rule admission 校验（[PR #5225](https://github.com/kubeedge/kubeedge/pull/5225)）
- 修复 device model 下发和删除时的同步问题([PR #5065](https://github.com/kubeedge/kubeedge/pull/5065))
- 修复 Mapper-Framework 下 pkg 包目录和相关应用([PR #5070](https://github.com/kubeedge/kubeedge/pull/5070))
- 修复 mutex 互斥锁 unlock 时机的问题（[PR #5279](https://github.com/kubeedge/kubeedge/pull/5279)）

### 社区席位

- top level 的 kubeedge reviewer [@WillardHu](https://github.com/WillardHu)
- sig release chairs + technical leads [@zhiyingfang2022](https://github.com/zhiyingfang2022)
- sig network chairs(审批中) + technical leads [@JiaweiGithub](https://github.com/JiaweiGithub)
- sig device chairs + technical leads [@cl2017](https://github.com/cl2017)

### 其它事项

- 协助社区完成 2023 年下半年规划（[PR #172](https://github.com/kubeedge/community/pull/172)）
- 将 DaoCloud 添加到 KubeEdge 合作伙伴（[PR #491](https://github.com/kubeedge/website/pull/491)）
- 在社区分享了消息路由支持修改([PR #5129](https://github.com/kubeedge/kubeedge/issues/5129))、
  消息路由支持断点续传([PR #4995](https://github.com/kubeedge/kubeedge/issues/4995))、
  消息路由云边通信阻塞问题优化([PR #5332](https://github.com/kubeedge/kubeedge/issues/5332))等功能技术方案。
- 在 SIG-AI 担任 sedna 10-11 月份轮值主持人
- 主持 SIG-DeviceIOT 社区例会
- 指导完成开源之夏项目《基于 KubeEdge 设备管理接口 DMI 的边缘设备多节点迁移方案》
- 参与 EdgeMesh CNI 功能设计
- Q4 DaoCloud 边缘团队总计给 KubeEdge 社区提交 PR [22 个](https://kubeedge.devstats.cncf.io/d/56/company-commits-table?orgId=1&from=now-90d&to=now&var-repogroups=kubeedge&var-companies=DaoCloud%20Network%20Technology%20Co.%20Ltd.)

![贡献](./images/edge02.png)
