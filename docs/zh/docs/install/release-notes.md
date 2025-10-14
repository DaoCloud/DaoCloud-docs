# 安装器 Release Notes

本页列出安装器的 Release Notes，便于您了解各版本的演进路径和特性变化。

*[Amamba]: DCE 5.0 应用工作台的开发代号
*[Ghippo]: DCE 5.0 全局管理的开发代号
*[insight-agent]: DCE 5.0 实现可观测性 Insight 能力的必需组件，默认安装在 insight-system 命名空间
*[Kangaroo]: DCE 5.0 镜像仓库的开发代号
*[Kpanda]: DCE 5.0 容器管理的开发代号
*[Skoala]: DCE 5.0 微服务引擎的开发代号
*[Hydra]: DCE 5.0 大模型服务平台的开发代号

## 2025-09-30

### v0.34.0

- **新增** SKIP_DEPENDENCY_RESOURCES 特性门控，避免分阶段升级场景重复导入资源问题
- **新增** 支持 Kylin V11 发行版离线部署，并优化相关离线包构建 CI
- **新增** 支持集群节点接入密码密文处理
- **新增** rp_filter sysctl 默认参数配置
- **修复** 离线场景 tailing-sidecar-operator 镜像地址问题
- **修复** kylin v11 环境安装 kind 集群 cgroup v2 兼容问题
- **修复** manifest 配置组件 nodeAffinity 参数失效问题

## 2025-08-31

### v0.33.0

- **优化** 更新前置检测 Helm 最小版本要求到 v3.14.0
- **优化** 前置依赖脚本
- **修复** RHEL8 系列发行版默认 Python 版本低导致集群部署失败问题
- **修复** Kylin v10 发行版系统部署集群 VERSION_ID 非数值类型引发报错问题
- **修复** mysql DSN URL 解析验证报错
- **修复** Hydra 中重复 mysql 查询参数问题
- **修复** Hydra 最小化部署副本数配置失效问题
- **修复** Hydra 数据库字符集问题
- **修复** Hydra 回滚 rollback-app mcamel 失败问题

## 2025-07-31

### v0.32.0

- **新增** 支持删除 kind 及 kind 集群数据
- **新增** 支持组件失败回滚
- **新增** kafka 和 zookeeper 监控指标
- **优化** mysql 安装流程
- **优化** rabbitmq 重装逻辑
- **优化** kafka ca 证书时间到 10 年
- **修复** infra、middleware 组件获取版本失败问题
- **修复** yaml文件反序列化丢数据问题
- **修复** fluentbit镜像问题
- **修复** 前置依赖脚本在 sudo 高版本情况下安装失败问题

## 2025-06-30

### v0.31.0

- **新增** 支持 k8s 证书签发有效期可配置
- **优化** 默认禁用 Ubuntu 集群环境 kernel_unattended_upgrades
- **优化** 安装器 go 1.24 及 golangci-lint v2 版本更新
- **修复** 开启节点内核调优时将默认调用 nf-conntrack 启用剧本
- **修复** 在线场景 URLs 架构固定参数问题

## 2025-05-31

### v0.30.0

- **新增** 支持 Ubuntu 24.04(noble) 系统离线安装
- **新增** cilium 离线支持
- **新增** 支持使用不同的安装模式以输出对应的 manifest.yaml 内容
- **优化** 统一组件安装函数前缀、离线包内组件 chart 存放路径
- **优化** 移除为 macOS 构建二进制包
- **优化** 更新前置依赖工具版本
- **优化** helm revision 记录文件的存取逻辑
- **优化** 安装基于 Ubuntu 的集群时先停止并禁用 unattended-upgrades 服务
- **修复** 安装 cert-manager 同时将 crd 安装完成
- **修复** 升级失败的日志提示
- **修复** kant 升级无法替换 values.yaml 中 imageRegistry 字段的问题

## 2025-04-30

### v0.29.0

- **新增** 支持在 kind 集群内安装 Cloud 模式（原 AI 模式）
- **新增** 通过 --show-feature-gates 参数展示安装器脚本内部的特殊功能开关
- **新增** 构建 cloud 模式下的离线包
- **新增** 适配火种 kind 版本 v0.27.0
- **新增** 升级 DCE 5.0 时检测待升级组件的当前版本是否低于已存在版本
- **优化** AI 模式更新为 Cloud 模式
- **优化** Cloud 模式下支持 metalLB
- **优化** istio-ingressgateway 的镜像拉取策略为 'IfNotPresent'
- **优化** 使用 dce5-installer rollback 子命令回滚时对于历史升级记录的处理
- **优化** 构建脚本中对火种离线资源的处理逻辑，移除冗余逻辑，提升后期维护性
- **修复** 安装中间件 rabbitmq 时从公网拉取镜像的问题
- **修复** chart values 里包含 '#' 字符时解析失败的问题
- **修复** 离线升级 DCE 5.0 后 mcamel-mysql 组件使用镜像错误的问题
- **修复** 升级 DCE 5.0 后覆盖之前手动修改的 metallb 组件相关的 CR L2Advertisement

## 2025-03-31

### v0.28.0

- **新增** AI 模式部署框架
- **新增** 实验性新增 rollback-app 命令，用于回滚全局管理集群组件应用
- **优化** 更新默认 k8s 版本到 v1.31.6
- **优化** 火种集群启动前对 podman systemd 配置的清理
- **优化** mysql 中间件配置检测
- **优化** 全局管理集群使用独立 resolv.conf 配置
- **优化** 配置 cni 二进制 owner 为 root， 避免权限问题
- **修复** kube-vip 组件缺失 iptables 版本离线镜像问题

## 2025-02-28

### v0.27.0

- **新增** manifest.yaml 支持设置 variables 参数，以便扩展及自定义 GProduct 组件的配置参数

## 2025-01-31

### v0.26.0

- **优化** 外接 MySQL 数据库时支持设置数据库模式（master-slave 或 mgr）

## 2024-12-31

### v0.25.0

- **优化** Manifest 组件与组件依赖

## 2024-11-30

### v0.24.0

- **修复** df 命令在不同系统输出单位不一致问题

## 2024-10-30

### v0.23.0

#### 优化

- **优化** 启用 cert-manager
- **优化** 新增前置依赖包中安装 helm-push 插件
- **优化** mysql mgr 模式下，采用 router 双副本
- **优化** 中间件统一 mysql 版本使用 8.0.37

#### 修复

- **修复** 集群状态检测方法，补充集群无法访问时的异常处理
- **修复** 安装 全局管理集群，es、redis、mysql 外置时，创建 minio 失败
- **修复** skopeo copy 在 x86 环境拉取 arm 镜像时的架构问题
- **修复** 中间件 redis 镜像 registry
- **修复** kafka metrics 采集异常

## 2024-09-30

### v0.22.0

#### 优化

- **优化** 更新默认 K8s 版本为 v1.30.4
- **优化** 支持 Rocky Linux 8
- **优化** 支持跳过验证 ospkg，需要在 clusterconfig.yaml 中 spec -> osRepos
  下定义 `skipValidateOSPackage: true`

#### 修复

- **修复** 多架构镜像融合后未清理中间镜像问题
- **修复** 部分 GProduct 组件 helm repo 缺失问题

!!! warning "已知问题"

    在线安装时 `baize` 组件（AI Lab）会报错：

    ```text
    Error: chart "baize" matching v0.9.0 not found in baize index. (try 'helm repo update'): no chart name found
    ```

## 2024-08-30

### v0.21.0

#### 优化

- **优化** 允许配置 CPU/内存 检测阈值
- **优化** 允许前置依赖使用原始地址下载
- **优化** 支持组件安装门控
- **优化** 移除 contour 安装代码
- **优化** 支持共享一个 MySQL 实例
- **优化** 升级 gproduct 时导入 files

#### 修复

- **修复** 修复由于 grep 不支持 PCRE 导致 values 解析为空的问题

## 2024-07-30

### v0.20.0

#### 优化

- **优化** 支持 Kylin v10sp3
- **优化** 支持更新火种集群内部的全局服务集群 kubeconfig
- **优化** 支持更新火种集群自身证书及 kubeconfig
- **优化** 向全局管理注册安装器版本信息
- **优化** clusterConfig.yaml 配置模版对 `elasticsearch` 添加 `insecure` 选项
- **优化** 检测系统 ipv6 启用状态并自动启用
- **优化** 优化外接 redis url 中的特殊字符校验

#### 修复

- **修复** 命令行 -s 指定脚本后 -j 参数不生效
- **修复** ps -p 偶发进程阻塞问题
- **修复** Ubuntu 22.04 内核参数依赖问题
- **修复** 磁盘检测误警告问题

## 2024-06-30

### v0.19.0

#### 优化

- **优化** 更新默认 K8s 版本为 v1.29.5
- **优化** 支持 clusterconfig.yaml 中 `kubeanConfig` 参数下配置 `ubuntu_kernel_unattended_upgrades_disabled: true` 禁用 ubuntu 内核自动更新
- **优化** 支持 addon 离线包多文件上传
- **优化** 升级依赖 charts-syncer 版本到 v0.0.23
- **优化** 隐藏任务调度器不必要的细节日志

#### 修复

- **修复** skopeo 安装目录清理问题
- **修复** import-artifact 命令多架构镜像导入失败
- **修复** 镜像检测失败被忽略问题
- **修复** OpenEuler 22.03 SP3 火种节点 Pod 不断重启问题
- **修复** 镜像列表中空行报错问题

#### 已知问题

- 基于 ARM 架构 kylinv10 操作系统下的 kind 集群为 v1.29.4 部署社区版时，会出现组件 `mcamel-common-mysql-cluster` 安装失败。

## 2024-05-30

### v0.18.0

#### 优化

- **优化** 更新默认 K8s 版本为 v1.28.9
- **优化** 支持 Ubuntu 22.04
- **优化** 支持产品组件扩展集成其命令行工具
- **优化** 增强 All-In-One 模式火种集群和全局服务集群的隔离性
- **优化** 优化 Kubean download_url 格式
- **优化** 扩展 merge_values_xxx 函数参数列表，支持获取由安装程序组装的原始 values 参数
- **优化** 添加前置依赖组件的最小可用版本检测
- **优化** 优化安装器和离线包的版本对应关系检查
- **优化** 优化 precheck 过程获取安装器版本的方法
- **优化** 升级前置依赖组件版本

#### 修复

- **修复** 修复火种集群 apiserver 端口漏洞
- **修复** 修复多架构融合失败过后重新执行报错

## 2024-04-30

### v0.17.0

#### 优化

- **优化** 支持从源站下载二进制、拉取镜像, 不经过代理加速站
- **优化** 重构 Kubean Config, 将模版拆分解耦
- **优化** 支持 docker 单容器磁盘限制
- **优化** 支持 kpanda 的 mysql 设置 mgr 模式，默认模式仍为 master-slave
- **优化** 支持 ubuntu ospkg 及 iso 的多架构
- **优化** 优化 yq 的错误提示信息显示

#### 修复

- **修复** 修复提示信息中 kubean 版本无法显示的问题
- **修复** 修复多架构镜像合并的问题
- **修复** 修复通过 dry-run 输出脚本的问题
- **修复** 修复安装过程超时，无法捕获超时步骤的问题
- **修复** 修复 insight-agent 安装问题
- **修复** 在火种启动之前，禁用火种宿主机的防火墙

## 2024-04-09

### v0.16.1

#### 修复

- **修复** 从低版本升级 gproduct 到 v0.16.0 时，由于 insight 组件脚本 bug，会导致升级失败的问题。

## 2024-03-31

### v0.16.0

#### 优化

- **优化** 支持 Rocky Linux 9.2 x86 containerd 部署
- **优化** 优化 Rocky Linux 最大用户实例数
- **优化** 简化自定义 action 在安装器侧的扩展使用
- **优化** 新增离线包手动裁剪工具脚本
- **优化** 火种数据落盘及可重载
- **优化** 允许部署集群跳过 docker 运行时安装
- **优化** 允许火种 apiserver 端口可指定配置

#### 修复

- **修复** 修复导入异构镜像时，OCI_PATH 未生效问题
- **修复** 处理 kubean 自定义 action manifest 乱序问题
- **修复** 修复火种集群时区与宿主机不一致问题

#### 已知问题

- 从低版本升级 gproduct 到 v0.16.0 时，由于 insight 组件脚本 bug，会导致升级失败，绕行方案：升级时在 mainfest.yaml 文件中对 insight 组件临时禁用即可。

## 2024-03-01

### v0.15.2

#### 修复

- **修复** 修复 CVE-2024-21626 安全漏洞，containerd 版本升级到 1.7.13，runc 版本升级到 v1.1.12

#### 注意事项

1. 安装器升级到 v0.15.2 版本后，支持的集群版本从 v1.26.0 ～ v1.29.0 更新为 v1.27.0 ～ v0.29.1。
   若是不支持的集群版本范围的生命周期管理，请参考文档[离线场景 Kubean 向下兼容版本的部署与升级操作](./best-practices/cve-20240-21626.md)
2. 可参考文档[修复 CVE-2024-21626 漏洞](./best-practices/cve-20240-21626.md)

## 2024-02-26

### v0.15.1

#### 优化

- **优化** 新增 Rocky Linux 9.2 的支持

## 2024-01-31

### v0.15.0

#### 优化

- **优化** 安装 mysql-operator 的稳定性
- **优化** 升级集群过程中停止中间件组件的 PDB
- **优化** 升级集群过程中停止 istiod 的 PDB
- **优化** 升级 gproduct 时跳过推送 iso 和 ospkg
- **优化** 更新导入 addon 包时使用安装器依赖的 chart-sycner 版本
- **优化** 升级合并 chart values 过程产生的无效日志

#### 修复

- **修复** 安装容器管理组件时提取外部数据库密码的不正确规则
- **修复** kafak/zookeeper pod 反亲和设置不生效问题
- **修复** 部分组件升级未生效问题，消除升级合并 chart values 过程中产生的所有镜像

## 2023-12-31

### v0.14.0

#### 优化

- **优化** 安装器通过调用 kubean 上游功能实现镜像多架构合并
- **优化** 仅在离线模式下启用 localArtifactSet 配置
- **优化** kubean 组件 k8s 老版本兼容支持
- **优化** 社区版移除火种节点检测
- **优化** LocalArtifactSet 仅在离线场景下使用

#### 修复

- **修复** OpenEuler22.03 环境下，火种节点 Pod 重启问题
- **修复** kubean 升级时，operator 组件版本未更新

## 2023-11-30

### v0.13.0

#### 新增

- **新增** 支持单独规划 etcd 节点部署
- **新增** 支持外接 Kafka 组件

#### 优化

- **优化** 火种机内置镜像仓库的证书有效期设置为 10 年
- **优化** 更新前置依赖软件版本

#### 修复

- **修复** 由于换行符导致 chart values 解析框架死循环问题
- **修复** 并发调度框架未正确处理 IFS（Internal Field Separator）问题

#### 已知问题

- 在火种节点中使用 podman 时必须开启 ipv6 -全局服务集群会出现 `etcd NOSPACE` 告警风险

## 2023-10-31

### v0.12.0

#### 新增

- **新增** 下载离线包断点续传功能
- **新增** 安装器在启用画眉存储组件时新增检查各个主机节点是否安装 lvm2
- **新增** 安装器内置默认 k8s 版本升级到 `1.27.5`

#### 优化

- **优化** 在社区版使用 `-z` 最小化安装时，去除了全局管理、容器管理、可观测组件的 cpu/memory 资源申请和限制
- **优化** 安装器 `-m` 参数检查，在使用 `-m` 参数但且并未指定 manifest 文件时报错并退出安装
- **优化** 升级功能的日志显示
- **优化** 新适配了 kubean 中的 containerd 相关参数
- **优化** 将 GProduct 组件重新打包上传到火种节点 ChartMuseum
- **优化** 在上传 addon 失败时的日志输出
- **优化** 适配升级 GProduct 组件时的复用 helm 安装参数
- **优化** 调整的全局服务集群每个节点 Pod 数量最大为 180
- **优化** 迁移 charts 过程中日志过多的问题

#### 修复

- **修复** 安装器基于非 root 用户安装时缓存文件的特权问题
- **修复** 在安装过程中从火种节点迁移数据到全局服务集群时的报错
- **修复** 上传 addon 可能失败的问题
- **修复** 从代码上修复可能出现的 `helm operation in progress` 问题
- **修复** Kpanda 组件支持带密码的哨兵模式的外置 redis
- **修复** 基于 docker 运行时部署全局服务集群失败的问题
- **修复** 在 LB 模式下 Ghippo 重定向问题
- **修复** MinIO 组件启动时没有 metric 指标的问题

#### 已知问题

- 在火种节点中使用 podman 时必须开启 ipv6 -全局服务集群会出现 `etcd NOSPACE` 告警风险

## 2023-8-31

### v0.11.0

#### 新增

- **新增** 更新全局服务集群的 k8s 版本到 v1.26.7 以避免旧版本安全漏洞
- **新增** 支持在 clusterConfig.yaml 设置 ansible 扩展参数
- **新增** 支持在 clusterConfig.yaml 添加证书更新配置，支持周期性更新及一次性更新
- **新增** 支持 redhat 9.2 系统离线部署
- **新增** 离线包添加 diag.sh 全局服务集群诊断脚本
- **新增** `--multi-arch` 标识，避免升级操作覆盖多架构镜像问题

#### 优化

- **优化** 安装器源码结构模块优化

#### 修复

- **修复** Redis 哨兵模式不支持哨兵实例密码
- **修复** 工作集群添加 TencentOS 3.1 系统节点失败

## 2023-7-31

### v0.10.0

#### 新增

- **新增** 支持 Oracle Linux R8-U7 操作系统
- **新增** 支持灵活暴露 kind 容器映射至宿主机的端口
- **新增** import-artifact 子命令支持根据 clusterConfig.yaml 配置文件中定义的外接服务来导入离线资源

#### 优化

- **优化** 对于使用安装器通过外接 osRepos 部署环境后，优化了在容器管理创建集群时可以选择到外接 osRepos
- **优化** 重构、抽象 clusterConfig 检测层
- **优化** 前置依赖安装脚本的错误提示
- **优化** 在最小化安装过程中 ES 健康状态为 `yellow` 时允许继续安装
- **优化** 消除 import-artifact 子命令多余的镜像集成步骤
- **优化** 离线资源外接或内建场景下默认展开 clusterConfig 模板中 fullPackagePath 属性

#### 修复

- **修复** 外接镜像服务地址检测有误
- **修复** 火种 kind 集群输出的错误格式 kubeconfig
- **修复** 解压不同版本离线包至统一目录导致 helm 参数出现多个版本 chart 的问题
- **修复** prerequisite.tgz 中错误的指令集架构信息
- **修复** import-artifact 不指定-C 导入异常
- **修复** 错误的退出指令导致安装器退出提示信息未展示的问题
- **修复** podman 底座 + kind 重启导致 kube-controller-manager 和 kube-scheduler 证书认证失败问题
- **修复** 打印内嵌 manifest 子命令的命令指示符只要指定非 `install-app` 都会返回全模式 manifest 的问题
- **修复** 打印内嵌 manifest 子命令的命令名 typo
- **修复** 已存在 amd64 资源，import-artifact 子命令再次导入 arm64 包失败

#### 已知问题

- 升级不支持通过 install-app 子命令，仅支持 create-cluster 子命令

- Redhat 8.6 操作系统火种 kind 重启后 kubelet 服务无法启动，报错：

    ```message
    failed to initialize top level QOS containers: root container [kubelet kubepods] doesn't exist
    ```

    临时解决方案是执行以下命令：

    ```sh
    podman restart [containerid] --time
    ```

- 安装基于 TencentOS 3.1 的集群时，无法正确识别包管理器，如果需要 TencentOS 3.1 请使用安装器 0.9.0 版本

## 2023-6-30

### v0.9.0

#### 新增

- **新增** `istio-ingressgateway` 支持了高可用模式，从 v0.8.x 及以前升级到 v0.9.0 时必须执行如下命令：`./offline/dce5-installer cluster-create -c clusterConfig.yaml -m manifest.yaml --upgrade infrastructure,gproduct`
- **新增** 支持在 clusterConfig.yaml 中配置暴露 火种 kind 地址及端口
- **新增** 安装器在启用画眉存储时，新增前置检查各个节点是否安装 lvm2
- **新增** 安装器内置默认 k8s 版本升级到 v1.26.5
- **新增** 支持在 clusterConfig.yaml 中指定火种 kind 的本地文件挂载路径
- **新增** 整合 ISO 镜像文件导入脚本到安装器二进制中

#### 优化

- **优化** 下载脚本
- **优化** `import-artifact` 命令逻辑和功能
- **优化** 升级过程中 clusterConfig.yaml 中 `isoPath` 和 `osPackagePath` 为非必填项
- **优化** 安装器临时文件清理机制
- **优化** 火种节点复用功能

#### 修复

- **修复** ES 组件无法在 OCP 启动的问题
- **修复** 在 TencentOS 中安装 DCE 后无法访问 UI 界面的问题
- **修复** 中间件数据库在 arm64 环境高概率新建数据库失败的问题
- **修复** 镜像上传成功检查过程中错误的 Shell 扩展

#### 已知问题

从 v0.8.x 升级到 v0.9.0 时需要执行如下命令进行检查：

- 检查 `istio-ingressgateway` 端口是 `80` 还是 `8080`

    ```bash
    kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].targetPort}'
    ```

- 检查 `istio-ingressgateway` 端口是 `443` 还是 `8443`

    ```bash
    kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].targetPort}'
    ```

输出结果为 `80` 或 `443` 时，升级命令需要增加 `infrastructure` 参数，示例：

```bash
./offline/dce5-installer cluster-create -c clusterConfig.yaml -m manifest.yaml --upgrade infrastructure,gproduct
```

输出结果非上述情况时，升级操作直接参考文档[升级 DCE 5.0 产品功能模块](upgrade.md)。

## 2023-6-15

### v0.8.1

#### 优化

- **优化** ipavo 组件升级到 v0.9.3
- **优化** Amamba 组件升级到 v0.17.4
- **优化** hwameistor-operator 组件升级到 v0.10.4
- **优化** Kangaroo 组件升级到 v0.8.2
- **优化** Insight 组件升级到 v0.17.3

#### 修复

- **修复** 外接 http 的 Harbor 仓库同步镜像失败的问题
- **修复** `clusterConfig.yaml` 配置文件缩进错误的问题
- **修复** 基于外接 yum repo 时渲染 localService 配置错误的问题
- **修复** 对接外部 jfrog charts 仓库的问题

## 2023-5-31

### v0.8.0

#### 新功能

- **新增** Other Linux 模式支持操作系统 OpenAnolis 8.8 GA
- **新增** 支持操作系统 OracleLinux R9 U1
- **新增** 增加节点状态检测
- **新增** 增加对系统包（OS PKG）的文件校验
- **新增** 支持节点非 22 端口安装集群
- **新增** 外接文件服务支持 K8s 二进制资源
- **新增** 支持外接 JFrog 镜像及 Charts 仓库
- **新增** 支持混合架构部署方案
- **新增** 支持外接 Redis 组件

#### 优化

- **优化** 部署 nacos 实例报镜像缺失
- **优化** 升级集群模块时，重复执行集群安装任务

#### 已知问题

- 离线包解压后的 `offline/sample/clusterConfig.yaml` 文件存在缩进问题，导致离线部署时会变成在线安装，离线安装前如果要使用 `offline/sample/clusterConfig.yaml` 文件的话需要手动修改缩进问题，请查看[集群配置文件](commercial/cluster-config.md)
- Addon 离线包暂不支持上传到 JFrog 外接服务
- 容器管理平台离线模式暂无法支持工作集群添加节点
- 离线场景下使用外置 osRepos 仓库时，即 clusterConfig.yaml 中定义 `osRepos.type=external`，
  部署 DCE 5.0 成功后无法在容器管理中创建工作集群，临时解决方案如下：
  全局服务集群安装完成后立即更新全局服务集群 kubean-system 命名空间的 configmap kubean-localservice，
  将 `yumRepos.external` 值中所有双引号改为单引号。如下示例，将文件内的双引号都替换为单引号：

    ```yaml
    yumRepos:
      external: [ "http://10.5.14.100:8081/centos/\$releasever/os/\$basearch","http://10.5.14.100:8081/centos-iso/\$releasever/os/\$basearch" ]
    ```

    替换为：

    ```yaml
    yumRepos:
      external:
        [
          'http://10.5.14.100:8081/centos/\$releasever/os/\$basearch',
          'http://10.5.14.100:8081/centos-iso/\$releasever/os/\$basearch',
        ]
    ```

- 版本升级时，insight-agent 存在问题，请参考 [insight 升级注意事项](../insight/quickstart/install/upgrade-note.md)

## 2023-5-30

### v0.7.1

#### 优化

- **优化** 升级监控组件版本

#### 修复

- **修复** 二进制输出社区版 manifest 有误

## 2023-4-30

### v0.7.0

#### 新功能

- **新增** 支持 Other Linux 来部署 DCE 5.0，[参考文档](os-install/otherlinux.md)
- **新增** 支持操作系统 OpenEuler 22.03
- **新增** 支持外接 osReposs，[参考集群配置文件说明](commercial/cluster-config.md)
- **新增** 支持内核参数调优，[参考集群配置文件说明](commercial/cluster-config.md)
- **新增** 支持检测外部 ChartMuseum 和 MinIO 服务是否可用

#### 优化

- **优化** 对 tar 等命令的前置校验
- **优化** 升级操作命令行参数
- **优化** 关闭了 Kibana 通过 NodePort 访问，Insight 使用 ES 的 NodePort 或 VIP 访问
- **优化** 并发日志展示，终止任务使用 SIGTERM 信号而不是 SIGKILL

#### 修复

- **修复** 在线安装时 Kcoral helm chart 无法查到问题
- **修复** 升级时 KubeConfig 无法找到问题

#### 已知问题

- 在线安装全局服务集群会失败，需在 clusterConfig.yaml 的 `kubeanConfig` 块里进行如下配置：

    ```yaml
    kubeanConfig: |-
      calico_crds_download_url: "https://proxy-qiniu-download-public.daocloud.io/DaoCloud_Enterprise/dce5/calico-crds-v3.25.1.tar.gz"
    ```

    同时通过容器管理在线创建工作集群也有相同问题，需在集群创建页面高级配置的自定义参数中添加上述配置，键为
    `calico_crds_download_url`，值为上述 calico_crds_download_url 的值

- Kubean 存在低概率无法创建 spray-job 任务，通过手动删除对应的 clusteroperations CR 资源再重新执行安装命令
- 使用外部 osRepos 部署 DCE 5.0 后，无法通过容器管理离线创建工作集群，通过手动修改全局服务集群 kubean-system
  命名空间的 configmap kubean-localservice 来解决。在 `yumRepos` 下新增如下配置，需要在 external 内填写
  clusterConfig.yaml 中配置的外部 osRepos 地址：

    ```yaml
    yumRepos:
      external: []
    ```

    完成修改后对容器管理创建集群页面的节点配置的 yum 源选择新配置

## 2023-4-11

### v0.6.1

#### 优化

- **优化** 升级了 Kpanda 至 v0.16.1
- **优化** 升级了 Skoala 至 v0.19.4

#### 已知问题

- 采用 7 节点模式安装时，es 专属节点未占成功，预计下个版本修复
- 安装器向火种节点 regsitry 导入镜像时报错

    ```console
    skopeo copy 500 Internal Error -- "NAME_UNKNOWN","message":"repository name not known to registry
    ```

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
- **优化** 火种节点 inotify 参数
- **优化** 全模式在线安装体验
- **优化** clusterConfig 结构和配置
- **优化** 社区版允许不检查 clusterConfig 格式以及参数
- **优化** 安装器执行调度器日志输出

#### 修复

- **修复** 移除了对 wget 的依赖
- **修复** 重复解压离线包后安装失败的问题
- **修复** MinIO 不可重入的问题
- **修复** 删除中间件 Redis CR 时继续遗留的 redis pvc
- **修复** Amamba 和 Amamba-jenkins 并发安装时先后顺序依赖的问题
- **修复** 安装器命令行 -j 参数解析失败问题

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

- 非最小化安装的 REHL8 上由于预装的 runc 导致安装器安装失败，临时解决方案：安装前在上述每台节点上执行
  `rpm -qa | grep runc && yum remove -y runc`
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

- **优化** 离线包不再包括操作系统的 ISO，需要单独下载，在纯离线的情况下，需要在
  clusterConfig 文件中定义 ISO 的绝对路径
- **优化** 商业版使用 Contour 作为默认的 ingress-controller
- **优化** MinIO 支持使用 VIP
- **优化** coredns 自动注入仓库 VIP 解析
- **优化** 离线包制作流程，加速打包 Docker 镜像
- **优化** 离线包的大小
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
- 纯离线环境，默认没有应用商店。请手动将火种节点的 chart-museum 接入到全局服务集群，仓库地址：`http://{火种 IP}:8081`，
  用户名 rootuser，密码 rootpass123
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
- **优化** 离线包制作流程，加速打包 Docker 镜像

#### 修复

- **修复** 公有云 Service 的问题
- **修复** 各个子模块的镜像和 Helm 的问题
- **修复** 离线包加载的缺陷修复

#### 已知问题

- 因为部分 Operator 需升级到支持 K8s 1.25，导致 DCE 5.0 向下不支持 K8s 1.20
- Kubean 默认 K8s 版本和离线包仍然限制在 1.24 版本，还未能更新到 1.25（由于 postgres-operator 暂不支持）
- Image Load 情况下，istio-ingressgateway imagePullPolicy 为 always
- ARM 版本，不能执行安装脚本的第 16 步（harbor），因为 harbor 暂时不支持 ARM。
  需要修改 manifest.yaml 文件，postgressql operator 为 fasle，执行安装命令时要添加
  `-j 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15`
- 在容器管理界面上创建新集群，无法对接 HTTPS 的仓库，需要手动修改 kubean job 的 ConfigMap 和 CR
- 永久 MinIO 的 PVC 的大小默认是 30G，会不够用（承载 kubean 二进制、ISO 以及 Harbor 镜像仓库），需要进行扩容操作
