---
hide:
  - toc
---

# Access registry

The registry supports access to [Nacos registry](../../../reference/basic-knowledge/registry.md#nacos-registry), [Eureka registry](../../.. /reference/basic-knowledge/registry.md#eureka-registry), [Zookeeper registry](../../../reference/basic-knowledge/registry.md#zookeeper-registry), [Kubernetes Registry](../../../reference/basic-knowledge/registry.md#kubernetes-registry), [Mesh Registry](../../../reference/basic-knowledge/ registry.md#service-mesh-registry).

Compared with the hosting registration center, the access registration center only supports some basic operations, such as viewing basic information, monitoring information, etc. To experience more advanced and comprehensive management operations, you need to create a [Managed Registry](../managed/registry-lcm/create-registry.md).

The steps to access the registration center are as follows:

1. Click `Microservice Management Center`-->`Access Registration Center` in the left navigation bar, and then click `Access Registration Center` in the upper right corner of the page.

    

2. Fill in the configuration information and click `OK` at the bottom of the page.

    Accessing different types of registries requires filling in different configuration information.

    - Kubernetes/Mesh registration center: directly select the cluster or mesh service you want to access.

        - If you can't find the Kubernetes cluster you want to add, you can go to the container management module [Access Cluster](../../../kpanda/07UserGuide/Clusters/JoinACluster.md) or [Create Cluster](.. /../../kpanda/07UserGuide/Clusters/CreateCluster.md).

        - If you can't find the mesh service you want to add, you can go to the mesh service module [Create Mesh](../../../mspider/user-guide/servicemesh/README.md).

            

    - Nacos/Zookeeper/Eureka registration center: fill in the name and address of the registration center, and click `Access Test`.

        If the address bar turns gray, it means that the access test is successful. For a distributed high-availability registry, you can also click `+ Add` to enter multiple addresses.

        