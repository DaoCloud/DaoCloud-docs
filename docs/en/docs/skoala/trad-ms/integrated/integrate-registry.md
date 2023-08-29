---
hide:
  - toc
---

# Integrate Registry

If you want to monitor or trace your existing microservices without creating a new registry, then you can just integrate your registries into the Microservices module of DCE 5.0.

Supported registries: [Nacos Registry](../../../reference/basic-knowledge/registry.md#nacos-registry), [Eureka Registry](../../../reference/basic-knowledge/registry.md#eureka-registry), [Zookeeper Registry](../../../reference/basic-knowledge/registry.md#zookeeper-registry), [Kubernetes Registry](../../../reference/basic-knowledge/registry.md#kubernetes-registry), and [Mesh Registry](../../../reference/basic-knowledge/registry.md#service-mesh-registry).

However, compared with hosted registries, integrated registries can only use some basic features, such as checking basic information, monitoring information, and tracing. To experience more fantastic and surprising boasted features, it is suggested to create a [Hosted Registry](../hosted/create-registry.md).

To integrate a registry, follow these steps:

1. Click `Traditional Microservices`-->`Integrated Registry` in the left navigation bar, and then click `Integrate Registry` in the upper right corner of the page.

    ![](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/integrate01.png)

2. Complete required information and click `OK` at the bottom of the page.

    Different types of registries requires different information.

    - Kubernetes/Mesh registry: directly select a cluster or service service

        - If your expected cluster doesn't appear in the drop-down list, go to the Container Management module to [Integrate Cluster](../../../kpanda/user-guide/clusters/integrate-cluster) or [Create Cluster]( ../../../kpanda/user-guide/clusters/create-cluster.md).

        - If your expected mesh doesn't appear in the drop-down list, go to the Service Mesh module to [Create Mesh](../../../mspider/user-guide/service-mesh/README.md).

            ![Integrate Mesh/Kubernetes](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/integrate02.png)

    - Nacos/Zookeeper/Eureka registries: fill in the name and address of the registry, and click `OK` at the bottom of the page.

        Click `+ Add` to enter multiple addresses.

        ![Nacos/Zookeeper/Eureka](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/skoala/images/integrate03.png)