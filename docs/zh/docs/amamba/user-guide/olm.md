---
hide:
  - toc
---

# OLM 应用

Operator Lifecycle Manager (OLM) 是 Kubernetes Operator 生态系统的一部分，用于管理 Operator 的安装、升级和权限控制。

- **Operator** ：扩展 Kubernetes 功能的控制器
- **ClusterServiceVersion (CSV)** ：定义 Operator 版本和元数据
- **CatalogSource** ：存储 Operator 及其相关资源的索引
- **Subscription** ：跟踪 Operator 安装和升级状态

## 创建 OLM 应用

1. 在 **概览** 页面中，点击 **OLM 应用** -> **创建应用**
1. 按照向导填写 **基本信息** 和 **资源配置** 参数
1. 返回 OLM 应用列表，等待其状态变为 **运行中**

通过集成 OLM 的结合，您可以更高效地在 Kubernetes 集群中管理应用和 Operator。
