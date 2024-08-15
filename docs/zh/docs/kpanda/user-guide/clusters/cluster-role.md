# 集群角色

DaoCloud Enterprise 5.0 基于集群的不同功能定位对集群进行了角色分类，帮助用户更好地管理 IT 基础设施。

## 全局服务集群

此集群用于运行 DCE 5.0 组件，例如[容器管理](../../intro/index.md)、[全局管理](../../../ghippo/intro/index.md)、[可观测性](../../../insight/intro/index.md)、[镜像仓库](../../../kangaroo/intro/index.md)等。
一般不承载业务负载。

| 支持的功能 | 描述 |
| -------- | ---- |
| K8s 版本 | 1.22+ |
| 操作系统 | RedHat 7.6 x86/ARM, RedHat 7.9 x86, RedHat 8.4 x86/ARM, RedHat 8.6 x86；<br>Ubuntu 18.04 x86, Ubuntu 20.04 x86；<br>CentOS 7.6 x86/AMD, CentOS 7.9 x86/AMD |
| 集群全生命周期管理 | 支持 |
| K8s 资源管理 | 支持 |
| 云原生存储 | 支持 |
| 云原生网络 | Calico、Cillium、Multus 和其它 CNI |
| 策略管理 | 支持网络策略、配额策略、资源限制、灾备策略、安全策略 |

## 管理集群

此集群用于管理工作集群，一般不承载业务负载。

- [经典模式](../../../install/commercial/deploy-requirements.md)将全局服务集群和管理集群部署在不同的集群，适用于企业多数据中心、多架构的场景。
- [简约模式](../../../install/commercial/deploy-requirements.md)将管理集群和全局服务集群部署在同一个集群内。

| 支持的功能 | 描述 |
| -------- | ---- |
| K8s 版本 | 1.22+ |
| 操作系统 | RedHat 7.6 x86/ARM, RedHat 7.9 x86, RedHat 8.4 x86/ARM, RedHat 8.6 x86；<br>Ubuntu 18.04 x86, Ubuntu 20.04 x86；<br>CentOS 7.6 x86/AMD, CentOS 7.9 x86/AMD |
| 集群全生命周期管理 | 支持 |
| K8s 资源管理 | 支持 |
| 云原生存储 | 支持 |
| 云原生网络 | Calico、Cillium、Multus 和其它 CNI |
| 策略管理 | 支持网络策略、配额策略、资源限制、灾备策略、安全策略 |

## 工作集群

这是使用[容器管理](../../intro/index.md)创建的集群，主要用于承载业务负载。该集群由管理集群进行管理。

| 支持的功能 | 描述 |
| -------- | ---- |
| K8s 版本 | 支持 K8s 1.22 及以上版本 |
| 操作系统 | RedHat 7.6 x86/ARM, RedHat 7.9 x86, RedHat 8.4 x86/ARM, RedHat 8.6 x86；<br>Ubuntu 18.04 x86, Ubuntu 20.04 x86；<br>CentOS 7.6 x86/AMD, CentOS 7.9 x86/AMD |
| 集群全生命周期管理 | 支持 |
| K8s 资源管理 | 支持 |
| 云原生存储 | 支持 |
| 云原生网络 | Calico、Cillium、Multus 和其它 CNI |
| 策略管理 | 支持网络策略、配额策略、资源限制、灾备策略、安全策略 |

## 接入集群

此集群用于接入已有的标准 K8s 集群，包括但不限于本地数据中心自建集群、公有云厂商提供的集群、私有云厂商提供的集群、边缘集群、信创集群、异构集群、Daocloud 不同发行版集群。
主要用于承担业务负载。

| 支持的功能 | 描述 |
| -------- | ---- |
| K8s 版本 | 1.18+ |
| 支持友商 | Vmware Tanzu、Amazon EKS、Redhat Openshift、SUSE Rancher、阿里 ACK、华为 CCE、腾讯 TKE、标准 K8s 集群、Daocloud DCE |
| 集群全生命周期管理 | 不支持 |
| K8s 资源管理 | 支持 |
| 云原生存储 | 支持 |
| 云原生网络 | 依赖于接入集群发行版网络模式 |
| 策略管理 | 支持网络策略、配额策略、资源限制、灾备策略、安全策略 |

!!! note

    一个集群可以有多个集群角色，例如一个集群既可以是全局服务集群，也可以是管理集群或工作集群。
