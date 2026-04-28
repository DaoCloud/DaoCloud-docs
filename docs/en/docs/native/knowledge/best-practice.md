# Best Practices

This page lists best practices recommended by the cloud native community for product and delivery reference.

- [Running StatefulSet Across Clusters](https://mp.weixin.qq.com/s/y1dEO8Fb3SxqQUW9WrEsHQ)

    Running StatefulSet reliably across clusters may require solving problems in two areas: network and storage.
    Based on an example, the article introduces a method for configuring and managing cross-cluster stateful application services.

- [How Do We Cultivate Community Within Cloud Native Projects?](https://thenewstack.io/how-do-we-cultivate-community-within-cloud-native-projects/)

    To cultivate an open source community based on cloud native projects, first understand who cares about your project, who are end users, stakeholders, and contributors?
    What work do they do, where do they work, and what are their goals?
    Discovering more potential stakeholders and providing contribution pathways is essential for increasing project adoption.

- [Dapr Integration with Flomesh for Cross-Cluster Service Invocation](https://mp.weixin.qq.com/s/Y-MewxHVMULKDi4_cbl6Yw)

    [Flomesh Service Mesh](https://github.com/flomesh-io/fsm) uses programmable proxy Pipy as the core to provide east-west and north-south traffic management.
    Through L7-based traffic management capabilities, it breaks network isolation between computing environments, establishing a virtual flat network enabling applications in different computing environments to communicate with each other.
    This article introduces cross-cluster service invocation through Dapr and Flomesh service mesh integration, achieving "true" multi-cluster interconnectivity.
