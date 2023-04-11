---
hide:
  - toc
---

# Update registry configuration

The microservice engine currently only supports updating the configuration of the Nacos/Zookeeper/Eureka registry.

1. On the `Access Registration Center List` page, select the registration center to be updated, click **`⋯`** on the right and select `Edit`.

    

2. Add or delete the registry address, then click `OK` at the bottom of the page.

    

!!! note

    To update the Kubernetes/Mesh registry:

    - You can [remove the connected registry](remove-registry.md) first, and then reconnect to other registry.
    - You can also go to the container management module [update the corresponding cluster](../../../kpanda/07UserGuide/Clusters/UpgradeCluster.md), or go to the service mesh module [update the corresponding mesh service](. ./../../mspider/03UserGuide/servicemesh/create-mesh.md).