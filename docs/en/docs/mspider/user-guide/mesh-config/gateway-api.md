# Gateway API Supported by Service Mesh

*[mspider]: Internal development codename of DaoCloud Service Mesh

Gateway API is the next-generation traffic management API introduced by the Kubernetes community, designed to replace the traditional Ingress API.
Istio supports the Gateway API and plans to make it the default API for future traffic management. This page describes how to configure and use the Gateway API in different mesh modes.

## Mesh Mode Description

DCE service mesh supports three mesh modes:

- **Hosted mesh:** The control plane is uniformly managed by mspider
- **Dedicated mesh:** An independent Istio control plane
- **External mesh:** An existing Istio mesh outside DCE

## Step 1: Configure Mesh Parameters

Configure the mesh parameter `global.enableGatewayAPI: true` in `globalMesh` to enable Gateway API support:

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
      global.enableGatewayAPI: 'true'  # Enable the Gateway API feature
```

## Step 2: Install Gateway API CRDs

### Hosted Mesh Mode (Not Supported Yet)

In hosted mesh mode, mspider automatically applies the Gateway API CRDs. At the same time, you can work with the working cluster resource synchronization feature described below to synchronize Gateway API resources to the hosted mesh.

Resource synchronization of a hosted mesh has the following characteristics:

- Supports synchronizing Istio resources (including Gateway API resources) of the working cluster to the virtual cluster

For more synchronization capabilities, refer to [Synchronize Working Cluster Resources of a Hosted Mesh - DaoCloud Enterprise](../../best-practice/managed-mesh-to-sync.md)

### Dedicated Mesh Mode

#### Ambient Mode Enabled

If Ambient mode is enabled for the dedicated mesh, the Gateway API CRDs are built in and do not need to be installed manually.

#### Ambient Mode Not Enabled

If Ambient mode is not enabled, you can install them in the following ways:

**Method 1: Refer to the official Istio documentation**

```shell
kubectl get crd gateways.gateway.networking.k8s.io &> /dev/null || \
  { kubectl kustomize "github.com/kubernetes-sigs/gateway-api/config/crd?ref=v1.3.0" | kubectl apply -f -; }
```

Refer to the [Istio Gateway API documentation](https://istio.io/latest/docs/tasks/traffic-management/ingress/gateway-api/) for installation.

**Method 2: Install through Container Management**

Install and configure it in the DCE Container Management module.

### External Mesh Mode

For an external mesh, refer to the official documentation of the corresponding Istio version to install the Gateway API CRDs.

## Step 3: Operate and Use

You can operate Gateway API resources in the following ways:

- **Container Management module:** Operate directly in the DCE Container Management module

For more detailed operation steps and configuration examples, see the [Istio Resource Management documentation](https://docs.daocloud.io/mspider/user-guide/mesh-config/istio-resources.html)

## Gateway API Resource Types

The Gateway API mainly includes the following resource types:

- **GatewayClass:** Defines the "class" of a gateway, equivalent to a template or driver for the gateway, similar to StorageClass in Kubernetes.
- **Gateway:** Defines the gateway configuration and deployment
- **HTTPRoute:** Configures HTTP routing rules
- **GRPCRoute:** Configures GRPC routing rules
- **ReferenceGrant:** A mechanism that allows resources to be referenced across namespaces. By default, routes and services of the Gateway API must be in the same namespace, and ReferenceGrant can break this restriction.

## Summary

As the future standard for Kubernetes traffic management, the Gateway API provides richer and more standardized capabilities. With the guidance of this page, you can successfully configure and use the Gateway API in different mesh modes to achieve more flexible and powerful traffic management.
