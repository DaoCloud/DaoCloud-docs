---
hide:
  - toc
---

# 多云编排 Release Notes

本页列出多云编排的 Release Notes，便于您了解各版本的演进路径和特性变化。

## v0.3

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

- **新增** 新增 cloudshell 的 API 通过 cloudshell 可以管理 karmada 集群
- **新增** 对多云命名空间的管理接口
- **新增** 多云 service 管理接口
- **新增** 多云工作负载详情相关接口
- **新增** 支持设置集群的污点与容忍
- **新增** 下载 karmada 实例 kubeconfig 接口
- **新增** 提供 instance 的 update API 支持修改 instance 别名和 label
- **优化** 优化 instance 的 API 并收集 karmada 实例的资源统计情况
