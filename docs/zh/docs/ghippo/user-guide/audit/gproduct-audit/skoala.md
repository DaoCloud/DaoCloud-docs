---
hide:
  - toc
---

# 微服务引擎审计项汇总

| 事件名称 | 资源类型 | 备注 |
| --- | --- | --- |
| 创建网关：Create-Gateway                                     | Gateway              |      |
| 更新网关：Update-Gateway                                     | Gateway              |      |
| 集群中网关列表：ListClusterGateway-Gateway                   | Gateway              |      |
| 删除网关：Delete-Gateway                                     | Gateway              |      |
| API 上下线：UpdateAPIStatus-GatewayAPI                       | GatewayAPI           |      |
| API 调用测试：DebugGatewayAPI-GatewayAPI                     | GatewayAPI           |      |
| 创建 API：CreateGatewayAPI-GatewayAPI                        | GatewayAPI           |      |
| 导入 API 检查：ImportAPICheck-GatewayAPI                     | GatewayAPI           |      |
| 导入 API：ImportAPI-GatewayAPI                               | GatewayAPI           |      |
| 更新 API 高级策略：UpdateGatewayAPIAdvancedPolicy-GatewayAPI | GatewayAPI           |      |
| 更新 API：UpdateGatewayAPI-GatewayAPI                        | GatewayAPI           |      |
| 批量更新 API 状态：BatchOperationAPI-GatewayAPI              | GatewayAPI           |      |
| 删除 API：DeleteAPI-GatewayAPI                               | GatewayAPI           |      |
| 创建网关接入服务：CreateService-GatewayService               | GatewayService       |      |
| 更新网关服务策略：UpdateServicePolicy-GatewayService         | GatewayService       |      |
| 更新网关接入服务：UpdateService-GatewayService               | GatewayService       |      |
| 删除网关服务：DeleteService-GatewayService                   | GatewayService       |      |
| 创建流量泳道：CreateLane-Lane                                | Lane                 |      |
| 创建泳道引流规则：CreateLaneDrainageRule-Lane                | Lane                 |      |
| 更新流量泳道状态：ActionLane-Lane                            | Lane                 |      |
| 更新泳道引流规则状态：UpdateLaneDrainageRuleStatus-Lane      | Lane                 |      |
| 更新泳道引流规则：UpdateLaneDrainageRule-Lane                | Lane                 |      |
| 删除流量泳道：DeleteLane-Lane                                | Lane                 |      |
| 删除泳道引流规则：DeleteLaneDrainageRule-Lane                | Lane                 |      |
| 添加流量泳道服务：AddLaneService-Lane                        | Lane                 |      |
| 移除流量泳道服务：DeleteLaneService-Lane                     | Lane                 |      |
| 创建云原生微服务的服务治理插件：CreateServiceIstioPlugin-Mesh | Mesh                 |      |
| 创建云原生微服务的服务治理端口超时规则：CreateTimeout-Mesh   | Mesh                 |      |
| 创建云原生微服务的服务治理端口故障注入：CreateFault-Mesh     | Mesh                 |      |
| 创建云原生微服务的服务治理端口离群检测：CreateOutlierDetection-Mesh | Mesh                 |      |
| 创建云原生微服务的服务治理端口熔断规则：CreateConnectionPool-Mesh | Mesh                 |      |
| 创建云原生微服务的服务治理端口重试规则：CreateRetry-Mesh     | Mesh                 |      |
| 创建云原生微服务的服务治理端口重写规则：CreateRewrite-Mesh   | Mesh                 |      |
| 对云原生微服务的服务治理插件排序：SortServiceIstioPlugin-Mesh | Mesh                 |      |
| 更新云原生微服务的服务治理插件：UpdateServiceIstioPlugin-Mesh | Mesh                 |      |
| 更新云原生微服务的服务治理端口超时规则：UpdateTimeout-Mesh   | Mesh                 |      |
| 更新云原生微服务的服务治理端口负载均衡：UpdateLb-Mesh        | Mesh                 |      |
| 更新云原生微服务的服务治理端口故障注入：UpdateFault-Mesh     | Mesh                 |      |
| 更新云原生微服务的服务治理端口离群检测：UpdateOutlierDetection-Mesh | Mesh                 |      |
| 更新云原生微服务的服务治理端口熔断规则：UpdateConnectionPool-Mesh | Mesh                 |      |
| 更新云原生微服务的服务治理端口重试规则：UpdateRetry-Mesh     | Mesh                 |      |
| 更新云原生微服务的服务治理端口重写规则：UpdateRewrite-Mesh   | Mesh                 |      |
| 将网格服务导入到云原生微服务中：ExportService-Mesh           | Mesh                 |      |
| 删除云原生微服务的服务治理插件：DeleteServiceIstioPlugin-Mesh | Mesh                 |      |
| 删除云原生微服务的服务治理端口超时规则：DeleteTimeout-Mesh   | Mesh                 |      |
| 删除云原生微服务的服务治理端口故障注入：DeleteFault-Mesh     | Mesh                 |      |
| 删除云原生微服务的服务治理端口离群检测：DeleteOutlierDetection-Mesh | Mesh                 |      |
| 删除云原生微服务的服务治理端口熔断规则：DeleteConnectionPool-Mesh | Mesh                 |      |
| 删除云原生微服务的服务治理端口重试规则：DeleteRetry-Mesh     | Mesh                 |      |
| 删除云原生微服务的服务治理端口重写规则：DeleteRewrite-Mesh   | Mesh                 |      |
| 为云原生微服务的服务全局限流端口绑定限流规则：CreateServiceIstioPluginRLSRules-Mesh | Mesh                 |      |
| 为云原生微服务的服务全局限流端口更新限流规则：UpdateServiceIstioPluginRLSRules-Mesh | Mesh                 |      |
| 为云原生微服务的服务全局限流端口删除限流规则：DeleteServiceIstioPluginRLSRules-Mesh | Mesh                 |      |
| 移除云原生微服务的服务：RemoveService-Mesh                   | Mesh                 |      |
| 按metadata查询托管 Nacos服务的实例列表：QueryServiceInstance-Nacos | Nacos                |      |
| 创建托管 Nacos 命名空间中的配置：CreateConfig-Nacos          | Nacos                |      |
| 创建托管 Nacos 命名空间中服务的 API 信息：CreateServiceAPI-Nacos | Nacos                |      |
| 创建托管 Nacos 命名空间：CreateNamespace-Nacos               | Nacos                |      |
| 创建托管 Nacos：Create-Nacos                                 | Nacos                |      |
| 更新托管 Nacos 命名空间中的服务：UpdateService-Nacos         | Nacos                |      |
| 更新托管 Nacos 命名空间中的配置：UpdateConfig-Nacos          | Nacos                |      |
| 更新托管 Nacos 命名空间中服务的 API 信息：UpdateServiceAPI-Nacos | Nacos                |      |
| 更新托管 Nacos 命名空间中服务的实例详情：UpdateServiceInstance-Nacos | Nacos                |      |
| 更新托管 Nacos 命名空间：UpdateNamespace-Nacos               | Nacos                |      |
| 更新托管 Nacos：Update-Nacos                                 | Nacos                |      |
| 回滚托管 Nacos 命名空间中的配置：RollbackConfig-Nacos        | Nacos                |      |
| 删除托管 Nacos 命名空间中的配置：DeleteConfig-Nacos          | Nacos                |      |
| 删除托管 Nacos 命名空间中配置的灰度配置：DeleteBetaConfig-Nacos | Nacos                |      |
| 删除托管 Nacos 命名空间：DeleteNamespace-Nacos               | Nacos                |      |
| 删除托管 Nacos：Delete-Nacos                                 | Nacos                |      |
| 托管 Nacos 命名空间中的服务可观测信息：GetServiceInsight-Nacos | Nacos                |      |
| 托管 Nacos 命名空间中服务的实例可观测信息：GetServiceInstanceInsight-Nacos | Nacos                |      |
| 修改托管 Nacos 用户密码：UpdateUserPassword-Nacos            | Nacos                |      |
| 更新托管 Nacos 的插件详情：Update-Plugin                     | Plugin               |      |
| 创建接入注册中心服务的 API 文档：CreateServiceAPI-Registry   | Registry             |      |
| 创建接入注册中心：Create-Registry                            | Registry             |      |
| 更新接入注册中心服务的 API 文档：UpdateServiceAPI-Registry   | Registry             |      |
| 更新接入注册中心服务的实例：UpdateInstance-Registry          | Registry             |      |
| 更新接入注册中心：Update-Registry                            | Registry             |      |
| 接入注册中心服务的可观测数据：GetServiceInsight-Registry     | Registry             |      |
| 接入注册中心服务的实例可观测信息：GetInstanceInsight-Registry | Registry             |      |
| 接入注册中心可用性检测：Ping-Registry                        | Registry             |      |
| 移除接入注册中心：Delete-Registry                            | Registry             |      |
| 创建/更新服务中的 Sentinel Token 服务器：CreateOrUpdateTokenServer-Sentinel | Sentinel             |      |
| 创建服务中的 Sentinel 流控规则：CreateFlowRule-Sentinel      | Sentinel             |      |
| 创建服务中的 Sentinel 热点规则：CreateParamFlowRule-Sentinel | Sentinel             |      |
| 创建服务中的 Sentinel 熔断规则：CreateDegradeRule-Sentinel   | Sentinel             |      |
| 创建服务中的 Sentinel 授权规则：CreateAuthorityRule-Sentinel | Sentinel             |      |
| 创建服务中的 Sentinel 系统规则：CreateSystemRule-Sentinel    | Sentinel             |      |
| 更新服务中的 Sentinel 流控规则：UpdateFlowRule-Sentinel      | Sentinel             |      |
| 更新服务中的 Sentinel 热点规则：UpdateParamFlowRule-Sentinel | Sentinel             |      |
| 更新服务中的 Sentinel 熔断规则：UpdateDegradeRule-Sentinel   | Sentinel             |      |
| 更新服务中的 Sentinel 授权规则：UpdateAuthorityRule-Sentinel | Sentinel             |      |
| 更新服务中的 Sentinel 系统规则：UpdateSystemRule-Sentinel    | Sentinel             |      |
| 删除服务中的 Sentinel 集群流控：DeleteClusterFlow-Sentinel   | Sentinel             |      |
| 删除服务中的 Sentinel 流控规则：DeleteFlowRule-Sentinel      | Sentinel             |      |
| 删除服务中的 Sentinel 热点规则：DeleteParamFlowRule-Sentinel | Sentinel             |      |
| 删除服务中的 Sentinel 熔断规则：DeleteDegradeRule-Sentinel   | Sentinel             |      |
| 删除服务中的 Sentinel 授权规则：DeleteAuthorityRule-Sentinel | Sentinel             |      |
| 删除服务中的 Sentinel 系统规则：DeleteSystemRule-Sentinel    | Sentinel             |      |
| 移除服务实例中的 Sentinel 治理详情：DeleteInsGovern-Sentinel | Sentinel             |      |
| 创建插件：CreatePlugin-SkoalaPluginTemplate                  | SkoalaPluginTemplate |      |
| 更新插件状态：UpdatePluginStatus-SkoalaPlugin                | SkoalaPlugin         |      |
| 更新插件：UpdatePlugin-SkoalaPluginTemplate                  | SkoalaPluginTemplate |      |
| 删除插件：DeletePlugin-SkoalaPluginTemplate                  | SkoalaPluginTemplate |      |
| 创建插件模板：CreatePluginTemplate-SkoalaPluginTemplate      | SkoalaPluginTemplate |      |
| 创建插件：CreatePlugin-SkoalaPluginTemplate                  | SkoalaPluginTemplate |      |
| 更新插件模板：UpdatePluginTemplate-SkoalaPluginTemplate      | SkoalaPluginTemplate |      |
| 更新插件：UpdatePlugin-SkoalaPluginTemplate                  | SkoalaPluginTemplate |      |
| 删除插件模板：DeletePluginTemplate-SkoalaPluginTemplate      | SkoalaPluginTemplate |      |
| 删除插件：DeletePlugin-SkoalaPluginTemplate                  | SkoalaPluginTemplate |      |
| 创建域名：CreateVirtualhost-Virtualhost                      | Virtualhost          |      |
| 更新域名：UpdateVirtualhost-Virtualhost                      | Virtualhost          |      |
| 删除域名：DeleteVirtualhost-Virtualhost                      | Virtualhost          |      |