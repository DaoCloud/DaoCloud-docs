# 安装器 Release Notes

本页列出安装器的 Release Notes，便于您了解各版本的演进路径和特性变化。

## 2023-4-30

### v0.7.0

#### 新功能

- **新增** 支持 Other Linux 来部署 DCE 5.0，[参考文档](os-install/otherlinux.md)
- **新增** 支持了操作系统 OpenEuler 22.03
- **新增** 支持外接 OS Repos，[参考集群配置文件说明](commercial/cluster-config.md)
- **新增** 支持了内核参数调优，[参考集群配置文件说明](commercial/cluster-config.md)
- **新增** 支持检测外部 ChartMuseum 和 MinIo 服务是否可用

#### 优化

- **优化** 优化了对 tar 等命令的前置校验
- **优化** 优化了升级操作命令行参数
- **优化** 关闭了 Kibana 通过 NodePort 访问，Insight 使用 ES 的 NodePort or VIP 访问
- **优化** 优化了并发日志展示，终止任务使用 SIGTERM 信号而不是 SIGKILL

#### 修复

- **修复** 修复在线安装时 Kcoral heml chart 无法查到问题
- **修复** 修复升级时 KubeConfig 无法找到问题

#### 已知问题

- 在线安装 global 集群会失败，需在 clusterConfig.yaml 的 `kubeanConfig` 块里进行如下配置:

    ```yaml
    kubeanConfig: |- 
      calico_crds_download_url: "https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/calico-crds-v3.25.1.tar.gz"
    ```

    同时通过容器管理在线创建工作集群也有相同问题，需在集群创建页面高级配置的自定义参数中添加上述配置，键为 `calico_crds_download_url`，值为上述 calico_crds_download_url 的值

- Kubean 存在低概率无法创建 spray-job 任务，通过手动删除对应的 clusteroperations CR 资源再重新执行安装命令
- 使用外部 OS Repo 部署 DCE 5.0后，无法通过容器管理离线创建工作集群，通过手动修改 global 集群 kubean-system 命名空间的 configmap kubean-localservice 来解决。
  在 `yumRepos` 下新增如下配置,需要在 external 内填写 clusterConfig.yaml 中配置的外部OS Repo 地址:

    ```yaml
    yumRepos:
      external: []
    ```

    完成修改后对容器管理创建集群页面的节点配置的yum源选择新配置

## 2023-4-11

### v0.6.1

#### 优化

- **优化** 升级了 Kpanda 至 v0.16.1
- **优化** 升级了 Skoala 至 v0.19.4

#### 已知问题

- 采用 7 节点模式安装时，es 专属节点未占成功，预计下个版本修复
- 安装器向火种节点 regsitry 导入镜像时报错 `skopeo copy 500 Internal Error -- "NAME_UNKNOWN","message":"repository name not known to registry`

## 2023-4-06

### v0.6.0

#### 新功能

- **新增** 支持一键升级 Gproduct 组件
- **新增** 适配了操作系统：UOS V20 1020a / Ubuntu 20.04
- **新增** 支持 OCP (OpenShift Container Platform)安装 DCE 5.0
- **新增** CLI 支持生成 clusterConfig 模板
- **新增** all in one 模式默认启动最小化安装模式
- **新增** Gproduct 组件中新增了 Kcollie 组件
- **新增** 支持社区版将镜像同步到外部仓库

#### 优化

- **优化** 解耦生成离线包的代码和安装流程所需的代码
- **优化** 优化火种节点 inotify 参数
- **优化** 优化全模式在线安装体验
- **优化** 优化 clusterConfig 结构和配置
- **优化** 社区版允许不检查 clusterConfig 格式以及参数
- **优化** 优化安装器执行调度器日志输出

#### 修复

- **修复** 移除了对 wget 的依赖
- **修复** 修复重复解压离线包后安装失败的问题
- **修复** 修复 MinIo 不可重入的问题
- **修复** 修复删除中间件 Redis CR 时继续遗留的 redis pvc
- **修复** 修复 Amamba 和 Amamba-jenkins 并发安装时先后顺序依赖的问题
- **修复** 修复安装器命令行-j参数解析失败问题

## 2023-2-28

### v0.5.0

#### 新功能

- **新增** 离线包分离 osPackage，需要在集群配置文件中定义 `osPackagePath`
- **新增** 支持 addon 离线化，需要在集群配置文件中定义 `addonOfflinePackagePath`
- **新增** 离线安装支持操作系统 REHL 8.4、REHL 7.9

#### 优化

- **优化** 升级了前置依赖工具的版本

#### 修复

- **修复** 安装器命令行 `-j` 参数效验检测问题
- **修复** 前置依赖工具安装路径问题
- **修复** 主机清单密码纯数字无效问题
- **修复** 运行时为 Docker 时，无法拉取内建仓库镜像问题

#### 已知问题

- 非最小化安装的 REHL8 上由于预装的 runc 导致安装器安装失败，临时解决方案：安装前在上述每台节点上执行 `rpm -qa | grep runc && yum remove -y runc`
- 非最小化安装的 REHL8 上有非法的内核参数设置，临时解决方案；安装前在上述每台节点上执行
  `eval $(grep -i 'vm.maxmapcount' /etc/sysctl.conf -r /etc/sysctl.d | xargs -L1 | awk -F ':' '{printf("sed -i -r \"s/(%s)/#\\1/\" %s; ", $2, $1)}') && sysctl --system`
- helm 并发安装存在潜在风险，失败后无法继续执行安装

## 2022-12-30

### v0.4.0

#### 新功能

- **新增** clusterConfig 的语法从 v1alpha1 升级为 v1alpha2，语法有不兼容变更，可以查看文档
- **新增** 不再在全局服务集群上安装永久 Harbor 和永久 MinIO
- **新增** 火种节点需要永久存在，用户安装 minio、chart museum、registry
- **新增** 商业版新增安装 contour 作为 默认的 ingress-controller
- **新增** 商业版新增安装 cert-manager
- **新增** 支持私钥模式的集群部署
- **新增** 支持外置镜像仓库进行部署

#### 优化

- **优化** 离线包不再包括操作系统的 ISO，需要单独下载，在纯离线的情况下，需要在 clusterConfig 文件中定义 ISO 的绝对路径
- **优化** 商业版使用 Contour 作为默认的 ingress-controller
- **优化** MinIO 支持使用 VIP
- **优化** coredns 自动注入仓库 VIP 解析
- **优化** 优化离线包制作流程，加速打包 Docker 镜像
- **优化** 优化了离线包的大小
- **优化** 基础设施支持 1.25：升级 redis-operator、eck-operator、hwameiStor
- **优化** 升级到 keycloakx
- **优化** Istio 版本升级至 v1.16.1

#### 修复

- **修复** [HwameiStor 的 operator 会随机错误清理集群中的 Job](https://github.com/hwameistor/hwameistor/issues/588)
- **优化** mysql 增强半同步，解决频繁主从切换的数据不一致
- **优化** 解决 mysql 磁盘被 clusterPedia 写爆
- **优化** coredns 自动注入仓库 VIP 解析
- **优化** 公有云上 svc 的修复
- **优化** 修复各种子模块的镜像和 helm 问题

#### 已知问题

- 默认安装模式下暂不支持未分区的 SSD 盘，如果要支持，需要手工干涉。
- 纯离线环境，默认没有应用商店。请手动将火种节点的 chart-museum 接入到 global 集群，仓库地址：`http://{火种 IP}:8081`, 用户名 rootuser，密码 rootpass123
- metallb 社区有已知问题，在主网卡有 dadfailed 的 IPV6 回环地址，metallb 无法工作，安装之前需要确保主网卡没有 dadfailed
- insight-api-server 启动中如果机器太卡，在 Liveness 健康检查周期内，无法完成数据库的初始化（migrate）动作，导致需要手动介入
- clusterConfig 配置文件中里的 iso 路径必须是绝对路径，不支持相对路径
- kubean 默认 k8s 版本和离线包仍然限制在 k8s 1.24 版本，还未能更新到 1.25（PG 暂不支持）
- external-Registry 如果是 Harbor，暂时不会自动创建 Project，需要提前手动创建
- Docker 运行时，无法拉取 built-in 仓库，将在下个版本修复
- 禁用 IPV6 之后，podman 无法启动火种节点的 kind 集群

## 2022-11-30

### v0.3.29

#### 新功能

- **新增** ARM64 支持：构建 ARM64 离线包
- **新增** 支持麒麟 kylin v10 sp2 离线包
- **新增** 基础设施支持 1.25：升级 redis-operator、eck-operator、hwameiStor 等组件
- **新增** 支持私钥模式的集群部署
- **新增** 工作负载基于自定义指标弹性伸缩，更加贴近用户实际业务弹性扩缩容需求

#### 优化

- **优化** 永久 harbor 使用 operator 创建，开启 HTTPS，并使用 Postgressql operator
- **优化** 商业版使用 Contour 作为默认的 ingress-controller
- **优化** MinIO 支持使用 VIP
- **优化** coredns 自动注入仓库 VIP 解析
- **优化** 优化离线包制作流程，加速打包 Docker 镜像

#### 修复

- **修复** 修复了公有云 Service 的问题
- **修复** 修复了各个子模块的镜像和 Helm 的问题
- **修复** 修复了离线包加载的缺陷修复

#### 已知问题

- 因为部分 Operator 需升级到支持 K8s 1.25，导致 DCE 5.0 向下不支持 K8s 1.20
- Kubean 默认 K8s 版本和离线包仍然限制在 1.24 版本，还未能更新到 1.25（由于 postgres-operator 暂不支持）
- Image Load 情况下，istio-ingressgateway imagePullPolicy 为 always
- ARM 版本，不能执行安装脚本的第 16 步（harbor），因为 harbor 暂时不支持 ARM。
  需要修改 mainfest.yaml 文件，postgressql operator 为 fasle，执行安装命令时要添加
  `-j 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15`
- 在容器管理界面上创建新集群，无法对接 HTTPS 的仓库，需要手动修改 kubean job 的 ConfigMap 和 CR
- 永久 MinIO 的 PVC 的大小默认是 30G，会不够用（承载 kubean 二进制、ISO 以及 Harbor 镜像仓库），需要进行扩容操作
