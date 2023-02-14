# 多云编排 Release Notes

本页列出多云编排的 Release Notes，便于您了解各版本的演进路径和特性变化。

## v0.5

发布日期：2022-12-25

## API

- **新增** 添加 cronjob 的增删改查等相关接口
- **新增** 添加 job 的增删改查等相关接口
- **新增** 新增单集群应用一键迁移多集群应用，自动升级依赖资源
- **修复** 修复在移除 member 集群的过程中，不能对 member 集群的资源进行一键升级

## Infrastructure

- **新增** 给 ListPropagationPolicies 和 ListInstanceOverridePolicies 接口增加 job 和 cronjob 类型
- **新增** ETCD 高可用
- **新增** 部署策略新增 priority 字段
- **新增** 差异化策略新支持 imageOverride, CommandOverrider ArgsOverrider LabelsOverrider AnnotationsOverrider
- **新增** 如果部署策略已经被工作负载使用和关联，部署策略不支持删除

## External

- **新增** 多云工作负载，新增支持 Job、CronJob
- **新增** 差异化策略支持表单化创建、更新
- **新增** 部署策略支持表单化创建、更新
- **新增** 工作集群支持显示驱逐状态
- **修复** 一个未关联任何角色的用户可以查看所有的实例信息
- **修复** 调度算法为 Duplicated 时，工作负载实例总数统计错误
- **修复** 调度算法为 Duplicated 时，工作负载实例总数统计错误
- **修复** 实例删除时，ghippo 中的数据没有删除
- **修复** 实例删除时，工作集群的 labels 没有被移除
- **修复** 移除集群时，可以在单集群应用多云化界面中看到正在移除的集群，并能添加正在移除的集群应

## v0.4

发布日期：2022-11-25

- **新增** prometheus 指标 metrics、opentelemetry 链路 trace
- **新增** 创建工作负载指定地域后显示对应集群列表
- **新增** 创建工作负载指定标签后显示对应集群列表
- **新增** failover 故障转移产品化
- **修复** estimator 没有适配离线安装
- **修复** 实例详情页面无状态负载显示异常的问题

## v0.3

发布日期：2022-10-21

- **新增** 多云编排开启权限校验
- **新增** 多云编排 list instance 接口，根据权限展示数据
- **新增** 多云编排根据用户权限查询 cluster 资源概览信息
- **新增** 多云编排查询所有 member 集群的 labels
- **新增** 多云编排单机集群应用一键转换为多集群应用
- **新增** 多云编排查询 member 集群的 namespace 和 deployment 资源
- **新增** 多云资源创建的提示语
- **修复** 多云编排修复实例下所有 PropagationPolicy 资源的排序不生效的问题
- **修复** 多云编排修复移除 member 集群的问题
- **优化** 多云编排优化 karmada PropagationPolicy 和 OverridePolicy 的 protobuf 数据结构
- **修复** 若干 bug 修复

## v0.2

发布日期：2022-9-25

- **新增** 对调度时间查询接口
- **新增** 多云服务 ConfigMap 管理接口
- **新增** 批量创建多个资源和 policy 资源
- **新增** Service 增加工作负载的标签
- **新增** 获取所有命名空间下 Service 的接口
- **新增** 注入 istio sidecar
- **新增** 接入集群时，部署 karmada estimator
- **新增** 多云 secret 接口
- **新增** 新增 instance 的 cpu 和 memery 的资源数据收集
- **新增** 新增 instance 的 event 查询 API

## v0.1

发布日期：2022-8-21

- **新增** 新增 cloudshell 的 API 通过 cloudshell 可以管理 karmada 集群
- **新增** 对多云命名空间的管理接口
- **新增** 多云 service 管理接口
- **新增** 多云工作负载详情相关接口
- **新增** 支持设置集群的污点与容忍
- **新增** 下载 karmada 实例 kubeconfig 接口
- **新增** 提供 instance 的 update API 支持修改 instance 别名和 label
- **优化** 优化 instance 的 API 并收集 karmada 实例的资源统计情况
