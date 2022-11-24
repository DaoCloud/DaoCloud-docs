# Release Notes

本页列出容器管理各版本的 Release Notes，便于您了解各版本的演进路径和特性变化。

## v0.12

### API

- **新增** 新增为 metallb 提供 IP 池的接口
- **新增** 新增 metricValues 和 customMetricSummary 接口，支持自定义指标
- **新增** HPA 增删改支持跨版本兼容
- **新增** 可指定容器查看日志，包括 init container
- **新增** 检查接入的集群不能为 global 集群
- **新增** 打开容器组控制台优先 bash 进入
- **新增** CRD 列表新增根据 group 筛选
- **新增** 优化查询 helmrelease resources sql 语句
- **新增** ListClusters 接口新增原生的 labelSelector 查询参数
- **修复** 修复 clusterpedia 安装在 v1.18 证书自签导致无法启动
- **修复** 修复 insight agent 无法安装
- **修复** 修复通过集群角色筛选集群
- **修复** 修复无法获取私有仓库镜像的 tag 列表
- **修复** 修复节点列表根据角色及其他条件混合筛选
- **升级** 升级 kubean-api 到 0.3.2
- **优化** 优化 helm 安装，安装应用立刻显示应用安装中

### API 服务

**新增** 新增同步 master 分支的每次 api 变更

### 基础设施

- **升级** 升级 Clusterpedia 至最新的 client-go 版本、app 版本 0.5.1、chart 版本 1.0.0
- **优化** egress 从 watch cluster event 改为使用 controller 监听 cluster cr 变化；优化 nginx 配置渲染，每个 cluster 渲染为单独配置文件
- **优化** ingress 从 watch cluster event 改为使用 controller 监听 cluster cr 变化；优化 nginx 配置渲染，每个 cluster 渲染为单独配置文件

### 控制器

- **新增** 新增自定义指标插件安装检测
- **新增** 新增自定义指标插件安装检测
- **修复** cluster secret ref 变化误删 gproductresources cr
- **优化** 新增集群配置时保留集群配置

## v0.11

### API

- **新增** secret 列表新增根据类型筛选
- **新增** 新增为 metallb 提供 IP 池的接口
- **新增** 新增 metricValues 和 customMetricSummary 接口，支持自定义指标
- **新增** HPA 增删改支持跨版本兼容
- **新增** 可指定容器查看日志，包括 init container
- **新增** 检查接入的集群不能为 global 集群
- **新增** 打开容器组控制台优先 bash 进入
- **新增** CRD 列表新增根据 group 筛选
- **新增** 优化查询 helmrelease resources sql 语句
- **新增** ListClusters 接口新增原生的 labelSelector 查询参数
- **修复** 修复 clusterpedia 安装在 v1.18 证书自签导致无法启动
- **修复** 修复 insight agent 无法安装
- **修复** 修复通过集群角色筛选集群
- **修复** 修复无法获取私有仓库镜像的 tag 列表
- **修复** 修复节点列表根据角色及其他条件混合筛选
- **升级** 升级 kubean-api 到 0.3.2
- **优化** 优化 helm 安装，安装应用立刻显示应用安装中

### API 服务

**新增** 新增同步 master 分支的每次 api 变更

### 基础设施

- **升级** 升级 Clusterpedia 至最新的 client-go 版本、app 版本 0.5.1、chart 版本 1.0.0
- **优化** egress 从 watch cluster event 改为使用 controller 监听 cluster cr 变化；优化 nginx 配置渲染，每个 cluster 渲染为单独配置文件
- **优化** ingress 从 watch cluster event 改为使用 controller 监听 cluster cr 变化；优化 nginx 配置渲染，每个 cluster 渲染为单独配置文件

### 控制器

- **新增** 新增自定义指标插件安装检测
- **新增** 新增自定义指标插件安装检测
- **新增** 可感知 ghippo 是绑定资源还是授权
- **修复** cluster secret ref 变化误删 gproductresources cr
- **优化** 新增集群配置时保留集群配置

## v0.10

### API

- **改进** 在创建 Helm 应用时进行名称校验
- **新增** secret 列表新增根据类型筛选
- **新增** 支持显示全部的 Repo
- **新增** ListConfigMaps 和 ListSecrets 接口提供只返回 metadata 的功能
- **新增** 支持网络模式为 none
- **新增** 支持 ntp 网络参数配置
- **新增** 支持节点角色筛选
- **新增** 新增默认参数 `calico_feature_detect_override`
- **新增** 新增 cilium 参数
- **新增** 新增 helm release 历史版本及回滚功能
- **新增** 新增 NetworkPolicy 的 CRUD
- **新增** 新增 cluster 列表针对 kubernetesVersion 和 managedBy 的模糊搜索、namespace 列表针对 workspaceAlias 的模糊搜索
- **新增** 除工作负载外所有 list 接口移植 customEngine
- **新增** 创建升级集群时记录 k8s 版本号
- **新增** 新增 LimitRange 的 CRUD
- **新增** 新增 支持 cluster 的 lableSelect 的操作
- **新增** 新增 支持 node 的 cpu 和 memory 的 request 和 limit 从 k8s 获取
- **新增** 支持 clusterlcm 离线安装
- **优化** 将 apiResourcesList 移动到 cluster 的 status.APIEnablements

### 基础设施

- **改进** 修复 e2e 部署失败任然 job succeeded 的问题
- **改进** 提升 pr 识别运行 e2e 精准度
- **改进** 修复每日构建 benchmark 失败的问题
- **改进** pr 识别 e2e 过滤 md 文件
- **新增** 新增 quota 相关 e2ecase

### 控制器

- **修复** 修复 clusterlcm 新增错误节点导致集群无法卸载 bug
- **修复** 修复 kubean 版本升级管理集群标签检测失败
- **修复** 修复 1.20 以下 k8s 版本无法更新 APIResource
- **修复** 修复更新集群 kubeconfig 的 secret 不存在 bug
- **修复** 修复 apply 资源失败的 bug
- **修复** 修复获取 clusterCIDR 错误的 bug
- **修复** insight 安装的 namespace 错误的 bug

### 安装

- **新增** 安装时可指定 redis PVC 的 storageClassName
- **新增** 支持 arm 架构
