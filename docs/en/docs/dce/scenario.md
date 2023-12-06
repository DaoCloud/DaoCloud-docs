---
hide:
   - toc
---

# Use Cases

DCE 5.0 integrates numerous excellent technologies from the community, with tens of thousands of built-in dependencies. After extensive testing, they are fused together to create a new generation PaaS service platform that excels in various usage scenarios.

## DCE 5.0 Scenario Videos

We have carefully created Step-By-Step scenario videos to meet specific business requirements in various scenarios:

=== "Multi-Cloud and Hybrid Cloud"

    - [How to convert a single-cloud application into a multi-cloud application with one click?](../videos/use-cases.md#one-click-transformation-from-single-cloud-application-to-multi-cloud-application)
    - [How to deploy hybrid cloud applications in DCE 5.0?](../videos/use-cases.md#deploying-hybrid-cloud-applications-in-dce-50)

=== "Insight"

    - [How to quickly locate anomalies and troubleshoot using observability?](../videos/use-cases.md#rapid-troubleshooting-and-issue-resolution)

=== "Traffic Governance"

    - [How to connect microservices to DCE 5.0 and govern north-south traffic?](../videos/use-cases.md#traditional-microservice-governance-north-south-traffic)
    - [How to leverage service mesh to govern east-west traffic for traditional microservices?](../videos/use-cases.md#traditional-microservice-governance-east-west-traffic)

=== "OEM IN and OUT"

    - [How to integrate customer systems into DCE 5.0?](../videos/use-cases.md#integrating-customer-systems-into-dce-50-oem-in)
    - [How to integrate DCE 5.0 into customer systems?](../videos/use-cases.md#integrating-dce-50-into-customer-systems-oem-out)

=== "Networking and Communication"

    - [How to enable outbound communication with fixed IP for applications migrated to the cloud?](../videos/use-cases.md#configuring-and-using-underlay-ip)
    - [How to achieve application acceleration and cross-cluster communication?](../videos/use-cases.md#application-acceleration-and-cross-cluster-communication)

=== "CICD and GitOps"

    - [How to deliver applications quickly using CICD?](../videos/use-cases.md#application-deployment-with-cicd)
    - [How to continuously deploy cloud-native applications using GitOps?](../videos/use-cases.md#continuous-deployment-of-cloud-native-applications-with-gitops)

=== "Middleware and AI & Vector Libraries"

    - [How to deploy ChatGPT application using middleware and pgvector?](../videos/use-cases.md#deploying-chatgpt-with-middleware-and-pgvector)
    - [How to achieve cross-cluster data synchronization for Redis?](../videos/use-cases.md#redis-cross-cluster-data-synchronization)

## DCE 5.0 Use Cases

In general, DCE 5.0 can support the following use cases:

=== "Production-Grade Container Management"

Users in the operation and maintenance team need to undertake dozens to hundreds of cluster operation and maintenance tasks, and the cluster network planning needs to meet the user's traditional network supervision requirements.

Involved modules: [Container Management](../kpanda/intro/index.md), [Container Network](../network/intro/index.md), container cluster lifecycle management

Solution advantages: Provide cluster lifecycle management capabilities from deployment, upgrade, certificate change, configuration change, recycling, etc.
Reuse the network infrastructure in the current enterprise environment as much as possible, and implement the best solution for the environment: MacVLAN network solution, SR-IOV smart network card acceleration solution, [SpiderPool](../network/modules/spiderpool/index.md) Cloud native IPAM solution, [Clilum](../network/modules/cilium/index.md) eBPF network acceleration solution, Underlay and Overlay collaborative network solution.

Manage all clusters and load information through the independent open source [Clusterpedia](../community/clusterpedia.md) unified control plane, compatible with standard Kubernetes cluster access, break through the performance bottleneck of Kubernetes API, and support thousands of people to use it at the same time.

=== "Cloud Edge Collaboration"

Users design edge collaboration solutions according to the cloud, edge, and end solutions. The edge end is a general-purpose computing power platform, and the edge end has strong computing power requirements. The edge terminal supports three deployment modes: edge node and edge cluster mode, and the edge cluster superimposes the four-layer architecture mode of edge nodes.

Involved modules: [Container Management](../kpanda/intro/index.md), [Container Network](../network/intro/index.md), container cluster lifecycle management, edge nodes

Advantages of the solution: The cloud centrally manages and controls all edge nodes and cluster information. Based on the traditional cloud-edge-end three-tier model, in response to strong edge computing power requirements, an edge cluster iterative edge node solution is added to form a four-tier cloud edge collaboration solution.

=== "Dual-architecture Cloud Native"

Users have dual-architecture (x86 + ARM) needs and have specific requirements for the underlying infrastructure and operating systems, such as processors: Loongson, Haiguang, Phytium, Kunpeng, Intel; operating systems: Kirin, Tongxin UOS, OpenEuler, etc.

Involved modules: [Container Management](../kpanda/intro/index.md), [Container Network](../network/intro/index.md), container cluster lifecycle management

Solution advantages: Northbound supports domestic chips and servers, and southbound supports dual-architecture operating system and dual-architecture application ecosystem in containers.

=== "App delivery"

Users adopt cloud native technology on a large scale, and expect standardization and process-based integration with the DevOps concept to promote cloud native technology to a wider range of application project groups.

Modules involved: [Container Management](../kpanda/intro/index.md), [Workbench](../amamba/intro/index.md), [Container Network](../network/intro/index.md), container registry, Edge Cloud Collaboration, Dual-architecture Cloud

Solution advantages: support hierarchical multi-tenant system, seamlessly adapt to user organization structure planning resource allocation.
CI/CD pipeline capability automates application construction and deployment. Innovatively introduce GitOps and progressive delivery capability systems to help applications perform more detailed delivery management capabilities.

=== "Cloud Native Observables"

Users have weak ability to observe running applications, and hope to complete observation access with light-weight or no-modification access, and complete all-round application operation observation (logs, metrics, traces).

Modules involved: [Container Management](../kpanda/intro/index.md), [Observability](../insight/intro/index.md), [Container Network](../network/intro/index.md), Edge to Cloud Continuum, Dual-architecture Cloud

Advantages of the solution: unified collection of observation data, one control panel can query all cluster and load observation data, and in-depth support for microservice architecture, [service mesh](../mspider/intro/index.md), network EBPF observation ability.

=== "Converged Microservices"

The user's application architecture decides to adopt the microservice architecture or has already adopted microservices, and hopes to obtain technical support such as a full range of microservice frameworks and comprehensive operation and maintenance capabilities, or hopes to introduce service mesh technology and achieve smooth transition in the process of technology change.

Modules involved: [Container Management](../kpanda/intro/index.md), [Container Network](../network/intro/index.md), [Microservice Engine](../skoala/intro/index.md), [Service Mesh](../mspider/intro/index.md), [Observability](../insight/intro/index.md), [Workbench](../amamba/intro/index.md)

Solution advantages: seamlessly integrate the first-generation microservices represented by SpringCloud and Dubbo with the new-generation microservice technology represented by Istio service mesh, and complete the microservice management of the whole lifecycle from development, deployment, access, external, observation, operation and maintenance ability.

=== "Data Service"

The user application architecture relies on mainstream middleware capabilities, and it is hoped that middleware can be operated and maintained in a unified manner, and more professional support capabilities for middleware planning, operation and maintenance can be obtained.

Modules involved: [Container Management](../kpanda/intro/index.md), [Container Network](../network/intro/index.md), [Container Local Storage](../storage/index.md), [Cloud native middleware](../middleware/index.md), Edge to Cloud Continuum, Dual-architecture Cloud

Solution advantages: cloud native local storage capabilities designed for stateful applications, unified platform management cloud native middleware, providing middleware management capabilities for the full lifecycle of multi-tenancy, deployment, observation, backup, operation and maintenance, combined with the container platform Ability to adapt to edge and innovation use cases.

=== "App Store"

Users hope to obtain out-of-the-box cloud native application software capabilities for exclusive use cases.

Modules involved: [Container Management](../kpanda/intro/index.md), App Store

Solution advantages: Include software products from ten major fields of ecological partners, provide a complete software stack for the actual business needs of enterprises, and easily find, test, and deploy message middleware, data middleware, low-code/no code application etc.

=== "Multicloud Management"

Multicluster and multicloud deployments have become the norm among users, and they hope to complete multicloud unified release and have the ability of cross-cloud disaster recovery and backup

Involved modules: [Container Management](../kpanda/intro/index.md), [Multicloud Management](../kairship/intro/index.md), [Container Network](../network/intro/index.md), Edge to Cloud Continuum, Dual-architecture Cloud

Advantages of the solution: Innovative technology completes cross-cloud disaster recovery, high concurrency performance of cross-cloud resource retrieval, combined with container platform capabilities to adapt to edge and credit creation use cases.

[Download DCE 5.0](../download/index.md){ .md-button .md-button--primary }
[Install DCE 5.0](../install/index.md){ .md-button .md-button--primary }
[Free Trial](license0.md){ .md-button .md-button--primary }
