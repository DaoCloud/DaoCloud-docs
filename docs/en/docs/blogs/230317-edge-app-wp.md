# Edge Native Application Guidelines White Paper

Published: January 17, 2023 (first version), October 24, 2022 (draft)

Original link: [Edge Native Application Principles White Paper] (https://www.cncf.io/reports/edge-native-applications-principles-whitepaper)

## Target

The term "edge-native" has been mentioned in many places such as industry blog posts, such as
[Gartner](https://blogs.gartner.com/thomas_bittman/2020/04/17/cloud-native-isnt-edge-native/),
[Macrometa](https://www.macrometa.com/blog/edge-native-is-not-cloud-native),
[FutureCIO](https://futurecio.tech/cloud-native-versus-edge-native-know-the-difference/).
Whereas [State of the Edge](https://github.com/State-of-the-Edge/glossary/blob/master/edge-glossary.md#edge-native-application) and
[Linux Foundation](https://www.lfedge.org/wp-content/uploads/2020/07/LFedge_Whitepaper.pdf) (LF) These organizations are also discussing edge-native applications, but have not focused on edge-native application guidelines.

This white paper focuses on edge-native applications and how to define these application guidelines.

## What is an edge?

Edge computing brings data processing closer to the source, such as controlling robots in a factory. In the next five years, edge computing will become more common,
The industry is projected to grow by [38.9% from 2022 to 2030](https://www.grandviewresearch.com/industry-analysis/edge-computing-market).
Many companies are seeing the following benefits of putting computing power at the edge:

- Reduced latency
- Bandwidth management
- Enhance the security of private data
- Stable operation under unreliable network

Various definitions of edge computing exist, but this article will focus on edge computing based on the geographic location where data processing takes place.
Geographically based edges are categorized into multiple categories depending on the distance from the user. The figure below shows the
Categories defined by the [Linux Foundation Edge Whitepaper](https://www.lfedge.org/wp-content/uploads/2020/07/LFedge_Whitepaper.pdf).

![edgetype](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/edgetype.png)

There are many similarities between edge-native principles and cloud native principles, but there are also some key differences.

## Cloud Native vs Edge Native

According to the definition of [Cloud Native Foundation (CNCF)](https://github.com/cncf/foundation/blob/main/charter.md), cloud native technologies are:

> **"Cloud native technologies empower organizations to build and run scalable applications in modern dynamic environments such as public, private, and hybrid clouds. Containers, service meshes, microservices, immutable infrastructure, and declarative The API is a great example of this approach.**
>
> **These techniques enable loosely coupled systems to be resilient, manageable, and observable. Combined with powerful automation, they allow engineers to make frequent and predictable high-impact changes with minimal redundancies. "**

This broad mission still holds true for edge applications, as the [Open Edge Computing Glossary](https://github.com/State-of-the-Edge/glossary/blob/master/edge-glossary.md#edge- native-application) states that,
"Edge-native applications" refer to cloud native principles:

> **"Edge-native applications are applications built using edge computing capabilities and are not suitable for running in the central cloud. Edge-native applications refer to cloud native principles, while considering the unique characteristics of the edge, such as resource constraints, security, latency, and autonomy .Edge-native applications are built in a way that leverages cloud computing capabilities and work with upstream resources. Edge applications that don't care about centralized resource management, remote management, orchestration, CI/CD are not really "native", but more like for traditional native applications."**

As cloud native use cases involve data and events at edge locations beyond the traditional cloud, new tools and techniques are evolving to enable loosely coupled systems that are elastic, governable, and observable while managing the uniqueness of the edge.

## Similarity between edge-native and cloud native

Edge-native has many similarities to cloud native, which are described in this section.

| Attributes | Cloud Native vs. Edge Native |
| ------------------- | ----------------------------- -------------------------------------------------- -|
| Portability of applications and services | Applications and services decouple their coupling from the infrastructure. A well-written application does not need to know where it is running to support portability between platforms. |
| Observability | The platform comes with a well-documented interface and tooling options to detect issues and collect metrics. This allows developers to build systems that are resilient and efficiently managed. |
| Manageability | Provides interface and tool options to manage applications and resources at scale. The platform also has a plug-in mechanism to provide basic network connection, service and management features. |
| Support for Multiple Languages and Frameworks | Applications and services can be implemented using various popular languages and frameworks. |

## The difference between edge native and cloud native

There are similarities in the broad missions of edge-native and cloud native, but there are differences that developers should be aware of.

| Properties | Cloud Native | Edge Native |
| ------------- | ----------------------------------- ---------------------- | --------------------------- ----------- |
| Application Model | Most microservice components are stateless services that support horizontal scaling. | While service-provided edge applications are very similar, consumer edge applications may be separate monoliths; in these cases, state is associated with the application. |
| Data Model | Common is a centralized model that supports stateless components. | Caching, streaming, real-time, and distributed models are often employed. |
| Elastic | Quick startup and shutdown; typically treats underlying resources as unlimited. | Due to the limited hardware resources of edge devices, the elasticity is limited; if more resources are needed, "vertical" expansion will be performed by requesting the cloud. |
| Stability | Outsource stability to cloud providers, using redundant nodes distributed across different geographies. | Often relies on a hardened infrastructure, with a recovery architecture for stateful components; in many cases, may be less stable than on the cloud. |
| Scale | Typically limited to a small number of regions and instances | Can support large-scale regions (up to tens of thousands), support large numbers of external devices (up to hundreds of thousands) |
| Orchestration | Orchestration in large public or private clouds aims to achieve efficiency and availability by running workloads on centrally pooled hosts, scheduled in a horizontal fashion. | The edge is decentralized, and workloads are deployed in a distributed manner, usually scheduled in a designated region. |
| Governance | Although both cloud native and edge-native are manageable, the mechanisms are different; cloud native relies on centralized control and automation. | Edge-native requires a mix of remote and centralized management and zero-touch deployment (ZTP) of hardware and software. Operations personnel at the edge may not be trained, few in number, or even non-existent. The upgrade process needs to be atomic and consistent to prevent equipment from being unavailable due to failed upgrades. |
| Network | Applications can rely on high-speed networks. | The application needs to consider various network speeds (unstable, relatively poor, very good) and features. Including mobile and wireless based, integrating data and events from non-IP protocol networks. |
| Security | Infrastructure for security management. | "Zero Trust" in an untrusted and insecure environment. |
| Hardware Configuration | Rarely requiredFocus on hardware configuration, can be suitable for most applications. |Applications may have higher real-time requirements, requiring hardware platform, location, and security awareness. Developers need to understand a wider range of hardware and interfaces. |
| Interacting with External Resources | Applications rarely need to interact with local hardware resources. | Services deployed at the edge often need to interact with the local environment: cameras, sensors, actuators, users, etc. | |

## Edge Native Apps

Edge-native applications are applications and services designed for the edge. They are written with reference to similarities and differences above. Below are the core guidelines for these apps.

## Edge Native Guidelines

In order to achieve the edge-native mission mentioned earlier in this article, edge-native applications should follow the following guidelines.

| Guidelines | Description |
| --------------------------- | --------------------- ----------------------------------- |
| Hardware management capabilities | Developers need to understand a wide range of hardware platforms and interfaces, not only homogeneous hardware platforms. |
| External Device Connections | An application must know how to connect to devices in its environment and be aware of changes in functionality at runtime. For example, after initial configuration, they can respond to sensor connection/disconnection or new device connection. Features are not fixed, and the application environment needs to be considered, so the orchestrator needs to be able to coordinate application state and feature changes. |
| Variable connection awareness | Applications must adapt to unreliable or even unusable (completely isolated) network connections, using mechanisms such as asynchronous communication, queuing and caching. When the edge obtains configuration from the central site, a "pull" mechanism may need to be used to overcome scale, networking, and security issues. |
| Centralized Observability | While both edge and cloud native applications require centralized observability, edge-native applications have unique considerations. Edge-native applications may be deployed in large-scale instances, with limited operation and maintenance personnel and on-site support. Therefore, technologies such as distributed collection and centralized aggregation of data, open loop (personnel observable/operable) and closed loop (machine automation) need to be adopted. Observability includes metrics, logs, digital twins, alerts (events and alerts), and health monitoring. |
| Large-Scale Infrastructure and Platform Management | Infrastructure and platform management are very important in large-scale edge applications and need to support declarative management. In addition, there may be some special requirements, such as device access, scale-out restrictions, managing bare-metal environments, etc. At the platform level, deploying or managing Kubernetes or virtualization layers and various plugins is also an issue; the platform level needs to be kept vendor-neutral for application portability. |
| Large-Scale Application Management | The number of applications and the number of instances of those applications can be very large at the edge, requiring configuration based on declarative rules and conditions, enforced through automated services, and aggregated management views across multiple application instances. Applications may also have real-time requirements, which means that the connection between applications and infrastructure platforms (e.g. using GPUs, DPUs, FPGAs, CPU architectures, kernel optimizations, Kubernetes plugins) may be tighter than cloud applications. In other words, application orchestration may trigger underlying infrastructure and platform orchestration. |
| Cross-regional | Applications are deployed in more than one region, and there are cross-regional delays and failures. In fact, edge applications may also span public clouds and private clouds. |
| Resource Usage Optimization | Since edge computing resources are constrained, applications must continuously optimize resource usage. Adjust applications on demand, migrate and scale based on deployment location and availability intent. This means that there are different running workloads throughout the day. |
| Application portability and reusability (with limitations) | The abstraction layer attempts to provide infrastructure- and platform-independent portability through a vendor-neutral PaaS. However, due to limitations of local resources, hardware platforms, security, mobile networks, etc., configuration options need to accommodate local differences. |

### Edge Native Criterion Grouping

![edgegroup](https://docs.daocloud.io/daocloud-docs-images/docs/blogs/images/edgegroup.png)

These nine guidelines can be grouped into a smaller set of five guidelines. Hardware management, external device connectivity, variable connectivity awareness (network) can all be considered under the broader discipline of resource and hardware management.
Likewise, edge applications that are manageable at scale, can be observed centrally, and have manageable infrastructure and platforms can all be categorized as criteria for managing at scale.
Here are five principles for scaling: cross-region, resource usage optimization, portability and reusability constraints, resource and hardware management, and scale management.

## Conclusion and next steps

This document is a first edition and may be subject to revision. There will be some papers related to the sub-content of this article later.

## How to participate

The CNCF IoT Edge Working Group has regular meetings, mailing lists, and Slack. For the latest information, see the working group GitHub
[Communication section](https://github.com/cncf/tag-runtime/blob/master/wg/iot-edge.md#communication) of the page.
Readers are welcome to contribute, introduce Edge-related projects, contribute ideas for areas of work for the group, or help revise this white paper and draft follow-up documents.

## Working list of edge-native open source projects and initiatives

As part of this article, the CNCF IoT Edge working group is collecting work listings of open source projects that help application developers implement the edge-native application guidelines outlined in this article.

The list can be found in [this spreadsheet](https://docs.google.com/spreadsheets/d/1dfa3lUvLuCrzmTH1w1TLeXxU-gy6QfbsE_ZXd1h4zTI/edit#gid=0) or via a QR code.
To get edit access to add items, join the [IoT Edge Working Group Google Group](https://groups.google.com/forum/#!forum/kubernetes-wg-iot-edge).

![QR code of edge native project list](https://i.imgur.com/sToDBW9.png)

## Contributors

### author

-Amar Kapadia, Aarna Networks
-Brandon Wick, Aarna Networks
-Joel Roberts, Cisco
-Kate Goldenring, Fermyon
-Dejan Bosanac, Red Hat
- Tomoya Fujita, Sony US Lab
-Ravi Chunduru, Verizon
-Natalie Fisher, VMware
-Steven Wong, VMware

### Reviewers

- Frédéric Desbiens, Eclipse Foundation
-Prakash Ramchandran, eOTF
-Mark Abrams, SUSE

## References

The Linux Foundation Edge White Paper:
https://www.lfedge.org/wp-content/uploads/2020/07/LFedge_Whitepaper.pdf

Open Edge Computing Glossary [v2.1.0] State of the Edge:
https://github.com/State-of-the-Edge/glossary/blob/master/edge-glossary.md#edge-native-application

Cloud Native Organization (CNCF) Charter: https://github.com/cncf/foundation/blob/main/charter.md

Gartner "Cloud native is not equal to edge native":
https://blogs.gartner.com/thomas_bittman/2020/04/17/cloud-native-isnt-edge-native/

Macrometa "Edge Native Not Cloud Native":
https://www.macrometa.com/blog/edge-native-is-not-cloud-native

Future CIO "The difference between cloud native and edge native":
https://futurecio.tech/cloud-native-versus-edge-native-know-the-difference/

Edge MeterComputing Market Size, Share and Trends Analysis Report, By Component (Hardware, Software, Services, Edge Management Platform), Application, Industry Vertical, Region and Segment Forecasts, 2022 - 2030:
https://www.grandviewresearch.com/industry-analysis/edge-computing-market
