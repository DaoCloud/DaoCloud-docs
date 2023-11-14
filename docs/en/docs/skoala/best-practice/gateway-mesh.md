# Integrating Gateway with Service Mesh

This article describes how to integrate the DCE 5.0 cloud-native gateway with a service mesh, allowing access to services within the service mesh through the gateway. This integration enables the use of all traffic management capabilities of the service mesh, such as virtual services and destination rules.

## Current Situation

Currently, the DCE 5.0 cloud-native gateway uses Contour as the control plane and does not synchronize policies with Istio. When accessing services within the service mesh through the cloud-native gateway, the gateway API directly connects to the services within the mesh. However, without synchronizing Istio's policies, the capabilities of the service mesh, such as virtual services and destination rules, cannot be applied, resulting in a lack of mesh capabilities.

## Integration Approach

The approach is to allow the cloud-native gateway to access services within the mesh through Istio's sidecar, thereby applying Istio's rules.

## Steps

1. When [creating the cloud-native gateway](../gateway/index.md), enable sidecar injection.


2. Set the annotation `traffic.sidecar.istio.io/includeInboundPorts: ""` for the pods.

    This prevents Istio from processing inbound traffic, reducing performance overhead.

3. Add the `--base-id 10` parameter to the Envoy startup parameters to allow two Envoy instances within the same namespace, preventing conflicts.

    ![Parameter Example](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw-mesh01.png)

4. When [adding an API](../gateway/api/index.md) under the gateway, set the `Host` request header.

    This allows the gateway to access services in other clusters through the sidecar in a multi-cluster scenario, enabling cross-cluster load balancing.

    ![Parameter Example](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw-mesh02.png)

5. Configure the resources for the gateway sidecar in the service mesh module, ensuring that it is not lower than the default resource configuration of the cloud-native gateway (1 core, 1 GB).

## Demonstration

After completing the above configurations, access services through the gateway domain. Each request should be directed to a different service in different clusters, indicating that the gateway can access services across clusters.

![Parameter Example](https://docs.daocloud.io/daocloud-docs-images/docs/zh/docs/skoala/images/br-gw-mesh03.png)
