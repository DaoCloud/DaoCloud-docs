---
MTPE: windsonsea
Date: 2024-10-15
---

# Custom Service Mesh Component Resources

This page describes how to customize the resources of the [Control Plane Components](../../intro/comp-archi-ui/cp-component.md) of a mesh configured
through [Container Management](../../../kpanda/user-guide/workloads/create-deployment.md).

## Prerequisites

The cluster has been managed by the service mesh, and the mesh components have been installed normally;
The login account has the __admin__ or __editor__ permission of the namespace istio-system in the global service cluster and the working cluster;

## Customization Operations

Take __istiod__ on the working cluster under a hosted mesh as an example. The specific operations are as follows:

1. Under Service Mesh, check that the access cluster of the hosted mesh nicole-dsm-mesh is nicole-dsm-c2, as shown in the figure below.

    ![Access cluster](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/mesh-config/images/meshrcfg01.png)

2. Click the cluster name to jump to the cluster page in the __Container Management__ module, and click to enter the __Workload__ -> __Stateless Load__ page to find __istiod__ ;

    ![Find istiod](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/mesh-config/images/meshrcfg02.png)

3. Click the workload name to enter the __Container Configuration__ -> __Basic Information__ tab page;

    ![View quota](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/mesh-config/images/meshrcfg03.png)

4. Click the Edit button to modify the CPU and memory quotas, and click __Next__ , __OK__ .

    ![Modify quota](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/mesh-config/images/meshrcfg04.png)

5. View the Pod resource information under the workload, and you can see that it has changed.

    ![Confirm quota](https://docs.daocloud.io/daocloud-docs-images/docs/mspider/user-guide/mesh-config/images/meshrcfg05.png)
