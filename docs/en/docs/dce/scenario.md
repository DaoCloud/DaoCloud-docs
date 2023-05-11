---
hide:
   - toc
---

# Applicable scenarios

DCE 5.0 integrates many of the best technologies in the community, and has tens of thousands of built-in dependencies. After massive commissioning, it has been melted into one furnace, creating a new generation of PaaS service platform, which is easy to use in various usage scenarios.

=== "Production-Grade Container Management"

Users in the operation and maintenance team need to undertake dozens to hundreds of cluster operation and maintenance tasks, and the cluster network planning needs to meet the user's traditional network supervision requirements.

Involved modules: [Container Management](../kpanda/intro/WhatisKPanda.md), [Container Network](../network/intro/what-is-net.md), container cluster lifecycle management

Solution advantages: Provide cluster lifecycle management capabilities from deployment, upgrade, certificate change, configuration change, recycling, etc.
Reuse the network infrastructure in the current enterprise environment as much as possible, and implement the best solution for the environment: MacVLAN network solution, SR-IOV smart network card acceleration solution, [SpiderPool](../network/modules/spiderpool/what.md) Cloud-native IPAM solution, [Clilum](../network/modules/cilium/what.md) eBPF network acceleration solution, Underlay and Overlay collaborative network solution.

Manage all clusters and load information through the independent open source [Clusterpedia](../community/clusterpedia.md) unified control plane, compatible with standard Kubernetes cluster access, break through the performance bottleneck of Kubernetes API, and support thousands of people to use it at the same time.

=== "Cloud Edge Collaboration"

Users design edge collaboration solutions according to the cloud, edge, and end solutions. The edge end is a general-purpose computing power platform, and the edge end has strong computing power requirements. The edge terminal supports three deployment modes: edge node and edge cluster mode, and the edge cluster superimposes the four-layer architecture mode of edge nodes.

Involved modules: [Container Management](../kpanda/intro/WhatisKPanda.md), [Container Network](../network/intro/what-is-net.md), container cluster lifecycle management, edge nodes

Advantages of the solution: The cloud centrally manages and controls all edge nodes and cluster information. Based on the traditional cloud-edge-end three-tier model, in response to strong edge computing power requirements, an edge cluster iterative edge node solution is added to form a four-tier cloud-edge collaboration solution.

=== "Xinchuang Cloud Native"

Users have Xinchuang needs and have specific requirements for the underlying infrastructure and operating systems, such as processors: Loongson, Haiguang, Phytium, Kunpeng, Intel; operating systems: Kirin, Tongxin UOS, OpenEuler, etc.

Involved modules: [Container Management](../kpanda/intro/WhatisKPanda.md), [Container Network](../network/intro/what-is-net.md), container cluster lifecycle management

Solution advantages: Northbound supports domestic chips and servers, and southbound supports Xinchuang operating system and Xinchuang application ecosystem in containers.

=== "Application Delivery"

Users adopt cloud-native technology on a large scale, and expect standardization and process-based integration with the DevOps concept to promote cloud-native technology to a wider range of application project groups.

Modules involved: [Container Management](../kpanda/intro/WhatisKPanda.md), [Application Workbench](../amamba/intro/WhatisAmamba.md), [Container Network](../network/intro/what-is-net.md), container registry, Edge Cloud Collaboration, Xinchuang Cloud

Solution advantages: support hierarchical multi-tenant system, seamlessly adapt to user organization structure planning resource allocation.
CI/CD pipeline capability automates application construction and deployment. Innovatively introduce GitOps and progressive delivery capability systems to help applications perform more detailed delivery management capabilities.

=== "Cloud Native Observables"

Users have weak ability to observe running applications, and hope to complete observation access with light-weight or no-modification access, and complete all-round application operation observation (logs, indicators, links).

Modules involved: [Container Management](../kpanda/intro/WhatisKPanda.md), [Observability](../insight/intro/what.md), [Container Network](../network/intro/what-is-net.md), Edge Cloud Synergy, Xinchuang Cloud

Advantages of the solution: unified collection of observation data, one control panel can query all cluster and load observation data, and in-depth support for microservice architecture, [service mesh](../mspider/intro/what.md), network EBPF observation ability.

=== "Converged Microservices"

The user's application architecture decides to adopt the microservice architecture or has already adopted microservices, and hopes to obtain technical support such as a full range of microservice frameworks and comprehensive operation and maintenance capabilities, or hopes to introduce service mesh technology and achieve smooth transition in the process of technology change.

Modules involved: [Container Management](../kpanda/intro/WhatisKPanda.md), [Container Network](../network/intro/what-is-net.md), [Microservice Engine](../skoala/intro/features.md), [Service Mesh](../mspider/intro/what.md), [Observability](../insight/intro/what.md), [Application Workbench](../amamba/intro/WhatisAmamba.md)

Solution advantages: seamlessly integrate the first-generation microservices represented by SpringCloud and Dubbo with the new-generation microservice technology represented by Istio service mesh, and complete the microservice management of the whole lifecycle from development, deployment, access, external, observation, operation and maintenance ability.

=== "Data Service"

The user application architecture relies on mainstream middleware capabilities, and it is hoped that middleware can be operated and maintained in a unified manner, and more professional support capabilities for middleware planning, operation and maintenance can be obtained.

Modules involved: [Container Management](../kpanda/intro/WhatisKPanda.md), [Container Network](../network/intro/what-is-net.md), [Container Local Storage](../storage/intro.md), [cloud-native middleware](../middleware/midware.md), Edge Cloud Synergy, Xinchuang Cloud

Solution advantages: cloud-native local storage capabilities designed for stateful applications, unified platform management cloud-native middleware, providing middleware management capabilities for the full lifecycle of multi-tenancy, deployment, observation, backup, operation and maintenance, combined with the container platform Ability to adapt to edge and innovation scenarios.

=== "App Store"

Users hope to obtain out-of-the-box cloud-native application software capabilities for exclusive scenarios.

Modules involved: [Container Management](../kpanda/intro/WhatisKPanda.md), App Store

Solution advantages: Include software products from ten major fields of ecological partners, provide a complete software stack for the actual business needs of enterprises, and easily find, test, and deploy message middleware, data middleware, low-code/no code application etc.

=== "Multi-Cloud Orchestration"

Multi-cluster and multi-cloud deployments have become the norm among users, and they hope to complete multi-cloud unified release and have the ability of cross-cloud disaster recovery and backup

Involved modules: [Container Management](../kpanda/intro/WhatisKPanda.md), [Multi-Cloud Orchestration](../kairship/intro/whatiskairship.md), [Container Network](../network/intro/what-is-net.md), Edge Cloud Synergy, Xinchuang Cloud

Advantages of the solution: Innovative technology completes cross-cloud disaster recovery, high concurrency performance of cross-cloud resource retrieval, combined with container platform capabilities to adapt to edge and credit creation scenarios.

[Download DCE 5.0](../download/dce5.md){ .md-button .md-button--primary }
[Install DCE 5.0](../install/intro.md){ .md-button .md-button--primary }
[Free Trial](license0.md){ .md-button .md-button--primary }
