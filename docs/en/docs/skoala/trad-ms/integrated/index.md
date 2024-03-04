---
hide:
  - toc
---

# Integrate Registry

If you want to monitor or trace your existing microservices without creating a new registry, then you can just integrate your registries into the Microservices module of DCE 5.0.

Supported registries: [Nacos Registry](../../../reference/basic-knowledge/registry.md#nacos-registry), [Eureka Registry](../../../reference/basic-knowledge/registry.md#eureka-registry), [Zookeeper Registry](../../../reference/basic-knowledge/registry.md#zookeeper-registry), [Kubernetes Registry](../../../reference/basic-knowledge/registry.md#kubernetes-registry), and [Mesh Registry](../../../reference/basic-knowledge/registry.md#service-mesh-registry).

However, compared with hosted registries, integrated registries can only use some basic features, such as checking basic information, monitoring information, and tracing. To experience more fantastic and surprising boasted features, it is suggested to create a [Hosted Registry](../hosted/index.md).

## Integrate

To integrate a registry, follow these steps:

1. Click __Traditional Microservices__ --> __Integrated Registry__  in the left navigation bar, and then click __Integrate Registry__ in the upper right corner of the page.

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/integrate01.png)

2. Complete required information and click __OK__ at the bottom of the page.

    Different types of registries requires different information.

    - Kubernetes/Mesh registry: directly select a cluster or service service

        - If your expected cluster doesn't appear in the drop-down list, go to the Container Management module to [Integrate Cluster](../../../kpanda/user-guide/clusters/integrate-cluster) or [Create Cluster]( ../../../kpanda/user-guide/clusters/create-cluster.md).

        - If your expected mesh doesn't appear in the drop-down list, go to the Service Mesh module to [Create Mesh](../../../mspider/user-guide/service-mesh/README.md).

            ![Integrate Mesh/Kubernetes](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/integrate02.png)

    - Nacos/Zookeeper/Eureka registries: fill in the name and address of the registry, and click __OK__ at the bottom of the page.

        Click __+ Add__ to enter multiple addresses.

        ![Nacos/Zookeeper/Eureka](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/integrate03.png)

## Update

Update Nacos/Zookeeper/Eureka registries with this guide.

If you want to update Kubernetes/Service Mesh registries, you can either remove it and reintegrate another one, or you can [update the Kubernetes cluster](../../../kpanda/user-guide/clusters/upgrade-cluster.md)/[update the mesh](../../../mspider/user-guide/service-mesh/README.md).

1. In the `Registry List` find registry you need to update, on the right side click __⋮__ and select __Edit__ .

    ![Edit](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/integrate-update01.png)

2. Add or remove the registry address, then click __OK__ at the bottom of the page.

    ![Edit](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/integrate-update02.png)

## Remove

1. In the `Registry List` find registry you need to remove, on the right side click __⋮__ and select __Remove__ .

    ![remove](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/integrate-remove01.png)

2. Enter the registry name to confirm that it is the exact one you want to remove, then click __Delete__ .

    ![remove](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/integrate-remove02.png)

!!! note

    Integrated registries can be `removed`, while hosted registries can be`deleted`. The difference between the two is:
    
    - Remove: The registry is removed from the DCE 5.0 Microservices module. The registry itself and data are not deleted. You can access the registry again later.
    - Delete: Deletes the registry and all the data in it. The registry cannot be used again. You need to create a new registry.
