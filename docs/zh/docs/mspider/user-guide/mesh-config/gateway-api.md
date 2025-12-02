# 服务网格支持的 Gateway API

*[mspider]: DaoCloud 服务网格的内部开发代号

Gateway API 是 Kubernetes 社区推出的下一代流量管理 API，旨在替代传统的 Ingress API。
Istio 支持 Gateway API 并计划将其作为未来流量管理的默认 API。本文档将介绍如何在不同网格模式下配置和使用 Gateway API。

## 网格模式说明

DCE 5.0 服务网格支持三种网格模式：

- **托管网格:** 控制面由 mspider 统一管理
- **专有网格:** 独立的 Istio 控制面
- **外部网格:** 外部已有的 Istio 网格

## 第一步：配置网格参数

在 `globalMesh` 中配置网格参数 `global.enableGatewayAPI: true`，启用 Gateway API 支持：

```yaml
apiVersion: discovery.mspider.io/v3alpha1
kind: GlobalMesh
metadata:
  name: mspider-dedicated-mesh
  namespace: mspider-system
spec:
  hub: release.daocloud.io/mspider
  mode: DEDICATED
  ownerCluster: mspider-dedicate
  ownerConfig:
    controlPlaneParams:
      global.high_available: 'false'
      global.istio_version: 1.23.6-mspider
      global.mesh_capacity: S50P200
      global.enableGatewayAPI: 'true'  # 开启 GatewayAPI 功能
```

## 第二步：安装 Gateway API CRD

### 托管网格模式（目前暂不支持）

在托管网格模式下，mspider 会自动将 Gateway API 的 CRD 进行应用。同时，我们可以配合中描述的同步工作集群资源功能，将 Gateway API 资源同步到托管网格中。

托管网格的资源同步具有以下特点：

- 支持将工作集群的 Istio 资源（包括 Gateway API 资源）同步到虚拟集群

更多同步能力介绍参阅[同步托管网格工作集群资源 - DaoCloud Enterprise](../../best-practice/managed-mesh-to-sync.md)

### 专有网格模式

#### 开启 Ambient 模式

如果专有网格开启了 Ambient 模式，Gateway API CRD 已内置，无需手动安装。

#### 未开启 Ambient 模式

如果未开启 Ambient 模式，可以通过以下方式安装：

**方式一：参考 Istio 官方文档**

```shell
kubectl get crd gateways.gateway.networking.k8s.io &> /dev/null || \
  { kubectl kustomize "github.com/kubernetes-sigs/gateway-api/config/crd?ref=v1.3.0" | kubectl apply -f -; }
```

参考 [Istio Gateway API 文档](https://istio.io/latest/docs/tasks/traffic-management/ingress/gateway-api/) 进行安装。

**方式二：通过容器管理平台安装**

在 DCE 5.0 容器管理平台中进行安装配置。

### 外部网格模式

对于外部网格，请参考对应 Istio 版本的官方文档进行 Gateway API CRD 的安装。

## 第三步：操作和使用

您可以通过以下方式操作 Gateway API 资源：

- **容器管理平台:** 在 DCE 5.0 容器管理平台中直接操作

更多详细的操作步骤和配置示例，请查看 [Istio 资源管理文档](https://docs.daocloud.io/mspider/user-guide/mesh-config/istio-resources.html)

## Gateway API 资源类型

Gateway API 主要包含以下资源类型：

- **GatewayClass:** 定义网关的「类」，相当于网关的模板或驱动，类似于 Kubernetes 中的 StorageClass。
- **Gateway:** 定义网关配置和部署
- **HTTPRoute:** 配置 HTTP 路由规则
- **GRPCRoute:** 配置 GRPC 路由规则
- **ReferenceGrant:** 允许跨命名空间引用资源的机制。默认情况下，Gateway API 的路由和服务必须在同一个命名空间内，ReferenceGrant 可以打破这种限制。

## 总结

Gateway API 作为 Kubernetes 流量管理的未来标准，提供了更丰富和标准化的功能。通过本文档的指导，您可以在不同的网格模式下成功配置和使用 Gateway API，实现更灵活和强大的流量管理能力。
