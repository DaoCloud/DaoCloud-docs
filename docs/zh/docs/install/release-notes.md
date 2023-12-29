# 安装器 Release Notes

本页列出安装器的 Release Notes，便于您了解各版本的演进路径和特性变化。

## 2023-12-31

### v0.14.0

#### 优化

- __优化__ 安装器通过调用 kubean 上游功能实现镜像多架构合并
- __优化__ 仅在离线模式下启用 localArtifactSet 配置
- __优化__ kubean 组件 k8s 老版本兼容支持
- __优化__ 社区版移除火种节点检测
- __优化__ LocalArtifactSet 仅在离线场景下使用

#### 修复

- __修复__ OpenEuler22.03 环境下，火种节点 Pod 重启问题
- __修复__ kubean 升级时，operator 组件版本未更新

## 2023-11-30

### v0.13.0

#### 新增

- __新增__ 支持单独规划 etcd 节点部署
- __新增__ 支持外接 Kafka 组件

#### 优化

- __优化__ 火种机内置镜像仓库的证书有效期设置为 10 年
- __优化__ 更新前置依赖软件版本

#### 修复

- __修复__ 修复由于换行符导致 chart values 解析框架死循环问题
- __修复__ 修复并发调度框架未正确处理 IFS（Internal Field Separator）问题

#### 已知问题

- 在火种节点中使用 podman 时必须开启 ipv6
- Global 集群会出现 `etcd NOSPACE` 告警风险

## 2023-10-31

### v0.12.0

#### 新增

- __新增__ 新增下载离线包断点续传功能
- __新增__ 安装器在启用画眉存储组件时新增检查各个主机节点是否安装 lvm2
- __新增__ 安装器内置默认 k8s 版本升级到 `1.27.5`

#### 优化

- __优化__ 在社区版使用 `-z` 最小化安装时，去除了全局管理、容器管理、可观测组件的 cpu/memory 资源申请和限制
- __优化__ 优化安装器 `-m` 参数检查，在使用 `-m` 参数但且并未指定 manifest 文件时报错并退出安装
- __优化__ 优化升级功能的日志显示
- __优化__ 新适配了 kubean 中的 containerd 相关参数
- __优化__ 将 GProduct 组件重新打包上传到火种节点 ChartMuseum
- __优化__ 优化在上传 addon 失败时的日志输出
- __优化__ 适配升级 GProduct 组件时的复用 helm 安装参数
- __优化__ 调整的 Global 集群每个节点 Pod 数量最大为 180
- __优化__ 优化迁移charts过程中日志过多的问题

#### 修复

- __修复__ 修复安装器基于非 root 用户安装时缓存文件的特权问题
- __修复__ 修复在安装过程中从火种节点迁移数据到 Global 集群时的报错
- __修复__ 修复上传 addon 可能失败的问题
- __修复__ 从代码上修复可能出现的 `helm operation in progress` 问题
- __修复__ 修复 Kpanda 组件支持带密码的哨兵模式的外置 redis
- __修复__ 修复基于 docker 运行时部署 Global 集群失败的问题
- __修复__ 修复在 LB 模式下 Ghippo 重定向问题
- __修复__ 修复 MinIo 组件启动时没有 metric 指标的问题

#### 已知问题

- 在火种节点中使用 podman 时必须开启 ipv6
- Global 集群会出现 `etcd NOSPACE` 告警风险

## 2023-8-31

### v0.11.0

#### 新增

- __新增__ 更新 Global 集群的 k8s 版本到 v1.26.7 以避免旧版本安全漏洞
- __新增__ 支持在 clusterConfig.yaml 设置 ansible 扩展参数
- __新增__ 支持在 clusterConfig.yaml 添加证书更新配置，支持周期性更新及一次性更新
- __新增__ 支持 redhat 9.2 系统离线部署
- __新增__ 离线包添加 diag.sh Global 集群诊断脚本
- __新增__ 新增 `--multi-arch` 标识，避免升级操作覆盖多架构镜像问题

#### 优化

- __优化__ 安装器源码结构模块优化

#### 修复

- __修复__ 修复 redis 哨兵模式不支持哨兵实例密码
- __修复__ 修复工作集群添加 TencentOS 3.1 系统节点失败

## 2023-7-31

### v0.10.0

#### 新增

- __新增__ 支持 Oracle Linux R8-U7 操作系统
- __新增__ 支持灵活暴露 kind 容器映射至宿主机的端口
- __新增__ import-artifact 子命令支持根据 clusterConfig.yaml 配置文件中定义的外接服务来导入离线资源

#### 优化

- __优化__ 对于使用安装器通过外接 os repo 部署环境后，优化了在容器管理创建集群时可以选择到外接 os repo
- __优化__ 重构、抽象 clusterConfig 检测层
- __优化__ 优化前置依赖安装脚本的错误提示
- __优化__ 在最小化安装过程中 ES 健康状态为 `yellow` 时允许继续安装
- __优化__ 消除 import-artifact 子命令多余的镜像集成步骤
- __优化__ 离线资源外接或内建场景下默认展开 clusterConfig 模板中 fullPackagePath 属性

#### 修复

- __修复__ 修复外接镜像服务地址检测有误
- __修复__ 修复火种 kind 集群输出的错误格式 kubeconfig
- __修复__ 修复解压不同版本离线包至统一目录导致 helm 参数出现多个版本 chart 的问题
- __修复__ 修复 prerequisite.tgz 中错误的指令集架构信息
- __修复__ 修复 import-artifact 不指定-C 导入异常
- __修复__ 修复错误的退出指令导致安装器退出提示信息未展示的问题
- __修复__ 修复 podman 底座 + kind 重启导致 kube-controller-manager 和 kube-scheduler 证书认证失败问题
- __修复__ 修复打印内嵌 manifest 子命令的命令指示符只要指定非 `install-app` 都会返回全模式 manifest 的问题
- __修复__ 修复打印内嵌 manifest 子命令的命令名 typo
- __修复__ 修复已存在 amd64 资源，import-artifact 子命令再次导入 arm64 包失败

#### 已知问题

- 升级不支持通过 install-app 子命令，仅支持 create-cluster 子命令

- Redhat 8.6 操作系统火种 kind 重启后 kubelet 服务无法启动，报错：`failed to initialize top level QOS containers: root container [kubelet kubepods] doesn't exist`，临时解决方案：执行命令`podman restart [containerid] --time`

- 安装基于 TencentOS 3.1 的集群时，无法正确识别包管理器，如果需要 TencentOS 3.1 请使用安装器 0.9.0 版本

## 2023-6-30

### v0.9.0

#### 新增

- __新增__ `istio-ingressgateway` 支持了高可用模式，从 v0.8.x 及以前升级到 v0.9.0 时必须执行如下命令：`./offline/dce5-installer cluster-create -c clusterConfig.yaml -m manifest.yaml --upgrade infrastructure,gproduct`
- __新增__ 支持在 clusterConfig.yaml 中配置暴露 火种 kind 地址及端口
- __新增__ 安装器在启用画眉存储时，新增前置检查各个节点是否安装 lvm2
- __新增__ 安装器内置默认 k8s 版本升级到 v1.26.5
- __新增__ 支持在 clusterConfig.yaml 中指定火种 kind 的本地文件挂载路径
- __新增__ 整合 ISO 镜像文件导入脚本到安装器二进制中

#### 优化

- __优化__ 优化下载脚本
- __优化__ 优化 `import-artifact` 命令逻辑和功能
- __优化__ 优化升级过程中 clusterConfig.yaml 中 `isoPath` 和 `osPackagePath` 为非必填项
- __优化__ 优化安装器临时文件清理机制
- __优化__ 优化火种节点复用功能

#### 修复

- __修复__ 修复 ES 组件无法在 OCP 启动的问题
- __修复__ 修复在 TencentOS 中安装 DCE 后无法访问 UI 界面的问题
- __修复__ 修复中间件数据库在 arm64 环境高概率新建数据库失败的问题
- __修复__ 修复镜像上传成功检查过程中错误的 shell 扩展

#### 已知问题

- 从 v0.8.x 升级到 v0.9.0 时需要执行如下命令进行检查：

    - 检查 `istio-ingressgateway` 端口是 `80` 还是 `8080`

        ```bash
        kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].targetPort}'
        ```

    - 检查 `istio-ingressgateway` 端口是 `443` 还是 `8443`

        ```bash
        kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].targetPort}'
        ```
  
    输出结果为 `80` 或 `443` 时，升级命令需要增加 `infrastructure` 参数，示例：`./offline/dce5-installer cluster-create -c clusterConfig.yaml -m manifest.yaml --upgrade infrastructure,gproduct`

    输出结果非上述情况时，升级操作直接参考文档[升级 DCE 5.0 产品功能模块](upgrade.md)

## 2023-6-15

### v0.8.1

#### 优化

- __优化__ ipavo 组件升级到 v0.9.3
- __优化__ amamba 组件升级到 v0.17.4
- __优化__ hwameistor-operator 组件升级到 v0.10.4
- __优化__ kangaroo 组件升级到 v0.8.2
- __优化__ insight 组件升级到 v0.17.3

#### 修复

- __修复__ 修复外接 http 的 Harbor 仓库同步镜像失败的问题
- __修复__ 修复 `clusterConfig.yaml` 配置文件缩进错误的问题
- __修复__ 修复基于外接 yum repo 时渲染 localService 配置错误的问题
- __修复__ 修复对接外部 jfrog charts 仓库的问题

## 2023-5-31

### v0.8.0

#### 新功能

- __新增__ Other Linux 模式支持操作系统 OpenAnolis 8.8 GA
- __新增__ 支持操作系统 OracleLinux R9 U1
- __新增__ 增加节点状态检测
- __新增__ 增加对系统包(OS PKGs)的文件校验
- __新增__ 支持节点非 22 端口安装集群
- __新增__ 外接文件服务支持 k8s 二进制资源
- __新增__ 支持外接 JFrog 镜像及 charts 仓库
- __新增__ 支持混合架构部署方案
- __新增__ 支持外接 Redis 组件

#### 优化

- __优化__ 部署 nacos 实例报镜像缺失
- __优化__ 升级集群模块时，重复执行集群安装任务

#### 已知问题

- 离线包解压后的 `offline/sample/clusterConfig.yaml` 文件存在缩进问题，导致离线部署时会变成在线安装，离线安装前如果要使用 `offline/sample/clusterConfig.yaml` 文件的话需要手动修改缩进问题，请查看[集群配置文件](commercial/cluster-config.md)
- Addon 离线包暂不支持上传到 JFrog 外接服务
- 容器管理平台离线模式暂无法支持工作集群添加节点
- 离线场景下使用外置 OS Repo 仓库时，即 clusterConfig.yaml 中定义 `osRepos.type=external`，
  部署 DCE 5.0 成功后无法在容器管理中创建工作集群，临时解决方案如下：
  global 集群安装完成后立即更新 global 集群 kubean-system 命名空间的 configmap kubean-localservice，
  将 `yumRepos.external` 值中所有双引号改为单引号。如下示例，将文件内的双引号都替换为单引号：

    ```yaml
    yumRepos:
      external: [ "http://10.5.14.100:8081/centos/\$releasever/os/\$basearch","http://10.5.14.100:8081/centos-iso/\$releasever/os/\$basearch" ]
    ```

    替换为：

    ```yaml
    yumRepos:
      external: [ 'http://10.5.14.100:8081/centos/\$releasever/os/\$basearch','http://10.5.14.100:8081/centos-iso/\$releasever/os/\$basearch' ]
    ```

- 版本升级时，insight-agent 存在问题，请参考 [insight 升级注意事项](../insight/quickstart/install/upgrade-note.md)

## 2023-5-30

### v0.7.1

#### 优化

- __优化__ 升级了监控组件版本

#### 修复

- __修复__ 二进制输出社区版 manifest 有误

## 2023-4-30

### v0.7.0

#### 新功能

- __新增__ 支持 Other Linux 来部署 DCE 5.0，[参考文档](os-install/otherlinux.md)
- __新增__ 支持了操作系统 OpenEuler 22.03
- __新增__ 支持外接 OS Repos，[参考集群配置文件说明](commercial/cluster-config.md)
- __新增__ 支持了内核参数调优，[参考集群配置文件说明](commercial/cluster-config.md)
- __新增__ 支持检测外部 ChartMuseum 和 MinIo 服务是否可用

#### 优化

- __优化__ 优化了对 tar 等命令的前置校验
- __优化__ 优化了升级操作命令行参数
- __优化__ 关闭了 Kibana 通过 NodePort 访问，Insight 使用 ES 的 NodePort 或 VIP 访问
- __优化__ 优化了并发日志展示，终止任务使用 SIGTERM 信号而不是 SIGKILL

#### 修复

- __修复__ 修复在线安装时 Kcoral helm chart 无法查到问题
- __修复__ 修复升级时 KubeConfig 无法找到问题

#### 已知问题

- 在线安装 global 集群会失败，需在 clusterConfig.yaml 的 `kubeanConfig` 块里进行如下配置：

    ```yaml
    kubeanConfig: |- 
      calico_crds_download_url: "https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/calico-crds-v3.25.1.tar.gz"
    ```

    同时通过容器管理在线创建工作集群也有相同问题，需在集群创建页面高级配置的自定义参数中添加上述配置，键为 `calico_crds_download_url`，值为上述 calico_crds_download_url 的值

- Kubean 存在低概率无法创建 spray-job 任务，通过手动删除对应的 clusteroperations CR 资源再重新执行安装命令
- 使用外部 OS Repo 部署 DCE 5.0后，无法通过容器管理离线创建工作集群，通过手动修改 global 集群 kubean-system
  命名空间的 configmap kubean-localservice 来解决。在 `yumRepos` 下新增如下配置，需要在 external 内填写
  clusterConfig.yaml 中配置的外部 OS Repo 地址：

    ```yaml
    yumRepos:
      external: []
    ```

    完成修改后对容器管理创建集群页面的节点配置的 yum 源选择新配置

## 2023-4-11

### v0.6.1

#### 优化

- __优化__ 升级了 Kpanda 至 v0.16.1
- __优化__ 升级了 Skoala 至 v0.19.4

#### 已知问题

- 采用 7 节点模式安装时，es 专属节点未占成功，预计下个版本修复
- 安装器向火种节点 regsitry 导入镜像时报错 `skopeo copy 500 Internal Error -- "NAME_UNKNOWN","message":"repository name not known to registry`

## 2023-4-06

### v0.6.0

#### 新功能

- __新增__ 支持一键升级 Gproduct 组件
- __新增__ 适配了操作系统：UOS V20 1020a / Ubuntu 20.04
- __新增__ 支持 OCP (OpenShift Container Platform)安装 DCE 5.0
- __新增__ CLI 支持生成 clusterConfig 模板
- __新增__ all in one 模式默认启动最小化安装模式
- __新增__ Gproduct 组件中新增了 Kcollie 组件
- __新增__ 支持社区版将镜像同步到外部仓库

#### 优化

- __优化__ 解耦生成离线包的代码和安装流程所需的代码
- __优化__ 优化火种节点 inotify 参数
- __优化__ 优化全模式在线安装体验
- __优化__ 优化 clusterConfig 结构和配置
- __优化__ 社区版允许不检查 clusterConfig 格式以及参数
- __优化__ 优化安装器执行调度器日志输出

#### 修复

- __修复__ 移除了对 wget 的依赖
- __修复__ 修复重复解压离线包后安装失败的问题
- __修复__ 修复 MinIo 不可重入的问题
- __修复__ 修复删除中间件 Redis CR 时继续遗留的 redis pvc
- __修复__ 修复 Amamba 和 Amamba-jenkins 并发安装时先后顺序依赖的问题
- __修复__ 修复安装器命令行-j参数解析失败问题

## 2023-2-28

### v0.5.0

#### 新功能

- __新增__ 离线包分离 osPackage，需要在集群配置文件中定义 `osPackagePath`
- __新增__ 支持 addon 离线化，需要在集群配置文件中定义 `addonOfflinePackagePath`
- __新增__ 离线安装支持操作系统 REHL 8.4、REHL 7.9

#### 优化

- __优化__ 升级了前置依赖工具的版本

#### 修复

- __修复__ 安装器命令行 `-j` 参数效验检测问题
- __修复__ 前置依赖工具安装路径问题
- __修复__ 主机清单密码纯数字无效问题
- __修复__ 运行时为 Docker 时，无法拉取内建仓库镜像问题

#### 已知问题

- 非最小化安装的 REHL8 上由于预装的 runc 导致安装器安装失败，临时解决方案：安装前在上述每台节点上执行 `rpm -qa | grep runc && yum remove -y runc`
- 非最小化安装的 REHL8 上有非法的内核参数设置，临时解决方案；安装前在上述每台节点上执行
  `eval $(grep -i 'vm.maxmapcount' /etc/sysctl.conf -r /etc/sysctl.d | xargs -L1 | awk -F ':' '{printf("sed -i -r \"s/(%s)/#\\1/\" %s; ", $2, $1)}') && sysctl --system`
- helm 并发安装存在潜在风险，失败后无法继续执行安装

## 2022-12-30

### v0.4.0

#### 新功能

- __新增__ clusterConfig 的语法从 v1alpha1 升级为 v1alpha2，语法有不兼容变更，可以查看文档
- __新增__ 不再在全局服务集群上安装永久 Harbor 和永久 MinIO
- __新增__ 火种节点需要永久存在，用户安装 minio、chart museum、registry
- __新增__ 商业版新增安装 contour 作为 默认的 ingress-controller
- __新增__ 商业版新增安装 cert-manager
- __新增__ 支持私钥模式的集群部署
- __新增__ 支持外置镜像仓库进行部署

#### 优化

- __优化__ 离线包不再包括操作系统的 ISO，需要单独下载，在纯离线的情况下，需要在 clusterConfig 文件中定义 ISO 的绝对路径
- __优化__ 商业版使用 Contour 作为默认的 ingress-controller
- __优化__ MinIO 支持使用 VIP
- __优化__ coredns 自动注入仓库 VIP 解析
- __优化__ 优化离线包制作流程，加速打包 Docker 镜像
- __优化__ 优化了离线包的大小
- __优化__ 基础设施支持 1.25：升级 redis-operator、eck-operator、hwameiStor
- __优化__ 升级到 keycloakx
- __优化__ Istio 版本升级至 v1.16.1

#### 修复

- __修复__ [HwameiStor 的 operator 会随机错误清理集群中的 Job](https://github.com/hwameistor/hwameistor/issues/588)
- __优化__ mysql 增强半同步，解决频繁主从切换的数据不一致
- __优化__ 解决 mysql 磁盘被 clusterPedia 写爆
- __优化__ coredns 自动注入仓库 VIP 解析
- __优化__ 公有云上 svc 的修复
- __优化__ 修复各种子模块的镜像和 helm 问题

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

- __新增__ ARM64 支持：构建 ARM64 离线包
- __新增__ 支持麒麟 kylin v10 sp2 离线包
- __新增__ 基础设施支持 1.25：升级 redis-operator、eck-operator、hwameiStor 等组件
- __新增__ 支持私钥模式的集群部署
- __新增__ 工作负载基于自定义指标弹性伸缩，更加贴近用户实际业务弹性扩缩容需求

#### 优化

- __优化__ 永久 harbor 使用 operator 创建，开启 HTTPS，并使用 Postgressql operator
- __优化__ 商业版使用 Contour 作为默认的 ingress-controller
- __优化__ MinIO 支持使用 VIP
- __优化__ coredns 自动注入仓库 VIP 解析
- __优化__ 优化离线包制作流程，加速打包 Docker 镜像

#### 修复

- __修复__ 修复了公有云 Service 的问题
- __修复__ 修复了各个子模块的镜像和 Helm 的问题
- __修复__ 修复了离线包加载的缺陷修复

#### 已知问题

- 因为部分 Operator 需升级到支持 K8s 1.25，导致 DCE 5.0 向下不支持 K8s 1.20
- Kubean 默认 K8s 版本和离线包仍然限制在 1.24 版本，还未能更新到 1.25（由于 postgres-operator 暂不支持）
- Image Load 情况下，istio-ingressgateway imagePullPolicy 为 always
- ARM 版本，不能执行安装脚本的第 16 步（harbor），因为 harbor 暂时不支持 ARM。
  需要修改 mainfest.yaml 文件，postgressql operator 为 fasle，执行安装命令时要添加
  `-j 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15`
- 在容器管理界面上创建新集群，无法对接 HTTPS 的仓库，需要手动修改 kubean job 的 ConfigMap 和 CR
- 永久 MinIO 的 PVC 的大小默认是 30G，会不够用（承载 kubean 二进制、ISO 以及 Harbor 镜像仓库），需要进行扩容操作
