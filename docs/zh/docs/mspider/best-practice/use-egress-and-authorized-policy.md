---
date: 2023-07-23
status: new
hide:
   - toc
---

# 使用网格完成定向服务访问限制

在业务场景中，我们需要限制只允许服务来访问某些特定的服务，这里可以组合 Istio 能力来进行统一的管理。

在 Istio 中，我们可以使用 __Egress__ 来控制服务对外访问的流量，同时也可以使用 __Service Entry__ 来控制网格外服务，结合授权策略 (Authorized Policy) 来控制服务对外访问的权限。本文将介绍如何使用 Egress 和授权策略来控制服务对外访问的流量和权限。

## 准备工作

首先，您需要确保你的网格属于正常的状态，如果您还没有安装 Istio，请参考 [创建网格](../install/install.md)。

### 网格启用仅出口流量

配置网格启用仅出口流量，请修改网格的治理信息，查看下方的截图介绍，注意修改了之后，我们的服务对集群外的访问需要配合 __Service Entry__ 来使用。

![image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/egress-and-authorized-03.png)

![image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/egress-and-authorized-04.png)

### 创建一个 Egress 网关

![image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/egress-and-authorized-01.png)

![image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/egress-and-authorized-02.png)

### 准备测试应用

可以使用任意应用进行测试，在后续步骤中，我们会通过 __kubectl exec pod__ 进入 pod 内进行网络访问测试，建议至少保证应用内有 __curl__ 命令即可。

> 这里是用了一个简单的 __bookinfo__ 来做示例，您也可以使用其他应用。

另外，需要保证应用的 __Pod__ 被成功注入了 __sidecar__ ，这个可以在网格的界面中查看对应服务的状态。

![image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/egress-and-authorized-14.png)

## 规则配置

下方规则均给出示例展示，您可以在服务网格的界面中进行创建，用 __YAML__ 的方式展示，方便于理解资源的定义。

### 创建 Service Entry

这里我们首先创建一个允许的出口访问地址，这里我们使用了 **baidu** 的地址，可以安装如图进行操作

![image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/egress-and-authorized-05.png)

![image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/egress-and-authorized-05-2.png)

### 创建 Virtual Service

![image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/egress-and-authorized-09.png)

### 创建 网关规则

注意使用 __ISTIO_MUTAL__ ，这样才可以用授权策略

![image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/egress-and-authorized-10.png)

### 创建网关规则的 DR

![image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/egress-and-authorized-06.png)

### 创建 **baidu** 的 DR

让所有流量走 HTTPS

![image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/egress-and-authorized-07.png)

## 启用授权策略

![image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/egress-and-authorized-11.png)

## 功能测试

### 从示例应用的 Pod 中访问 baidu

可以成功看到访问的结果是正常的，这是因为我们在网格中启用了出口流量，并且限制了来源使用的服务。

![image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/egress-and-authorized-12.png)

### 从其他应用的 Pod 中访问 baidu

此时因为有限定来源服务，所以对于从其他服务发起的咨询，会被拒绝。

![image](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/mspider/images/egress-and-authorized-13.png)
