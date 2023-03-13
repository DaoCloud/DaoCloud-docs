# 安装器 Release Notes

本页列出安装器的 Release Notes，便于您了解各版本的演进路径和特性变化。

## 2022-2-28

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
