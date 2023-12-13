---
hide:
  - toc
---

# Blog Posts

This page summarizes blogs and public account articles related to DCE 5.0 and cloud native
technology, sorted by date by default.

## 2023

- [20231213 | Kubernetes 1.29 Released with an Ambious Mandala Theme](./231213-k8s-1.29.md)

    On December 13, 2023, Pacific Time, Kubernetes 1.29 with the theme "Mandala" is officially released.

- [20231205 | Does Kubernetes Really Perform Better on Bare Metal vs. VMs?](./231205-vm-bm-compare.md)

    Many people presume that a Kubernetes cluster deployed on bare metal performs better than one deployed on
    virtual machines, but until now there hasn’t been any proof of that assumption.

- [20231115 | Removals, Deprecations, and Major Changes in Kubernetes 1.29](./231115-k8s-1.29-changes.md)

    As with every release, Kubernetes v1.29 will introduce feature deprecations and removals.
    Our continued ability to produce high-quality releases is a testament to our robust development
    cycle and healthy community. The following are some deprecations and removals coming
    in the Kubernetes 1.29 release.

- [20231008 | A Look Back for Kubernetes Contributor Summits in Shanghai, China](./20231008-kcs.md)

    On September 26, 2023, the first day of KubeCon + CloudNativeCon + Open Source Summit China 2023,
    nearly 50 community contributors gathered in Shanghai for the Kubernetes Contributor Summit.

- [20230815 | Kubernetes 1.28 is Released](./230815-k8s1.28.md)

    Announcing the release of Kubernetes v1.28 Planternetes, the second release of 2023!

- [20230808 | Unlocking the Power of Kubernetes with K8SGPT](./230808-k8sgpt.md)

    [K8sGPT](https://k8sgpt.ai/) is an incredible tool that gives Kubernetes SREs superpowers.
    It provides a simple and efficient way to scan your Kubernetes clusters and diagnose issues in plain English.

- [20230612 | AIGC Sharp Tools: Exploring Ray's Cloud-Native Journey - Ray Core Part II](./230615-ray.md)

    This article provides a detailed explanation of Ray's capabilities and parameters, as well as practical application operations.

- [20230612 | The Exploration of Ray Core in Cloud-Native Computing for AIGC - Ray Core](./230612-ray.md)

    This article introduces how Ray Core, a distributed computing framework, works as the foundation of Ray.

- [20230609 | Istio 1.18 Released: Officially Announcing Ambient Mode](./230609-istio118.md)

    The 1.18 release is the second release of Istio in 2023 and the first to support Ambient mode.

    This release introduces many new features and changes, including but not limited to Istio in Ambient mode, enhanced Kubernetes Gateway API,
    health check support for unregistered VMs, added support for metric expiration, and improved `istioctl analyze`.

- [20230605 | Cloud Native Federation Middleware - FedState Officially Open Sourced](./230605-fedstate.md)

    In the cloud native scenario, there has been great development of stateful services. In a multi-cloud/federation environment, how to design and implement the scheduling, deployment, and automated operation and maintenance of stateful services based on multiple clusters, multiple data centers, and hybrid cloud scenarios? The newly open-sourced FedState project is trying to solve such situation problems.

- [2023061| API Server Tracing feature upgraded to beta](./230601-api-server-tracing.md)

    In Kubernetes, the API Server is the core component responsible for managing and scheduling all cluster resources. It receives and processes requests from various clients
    and converts them into underlying resource operations. Therefore, the stability and observability of the API Server are crucial to the overall health of Kubernetes.

- [20230518| Having fun with seccomp profiles on the edge](./230518-seccom.md)

    The Security Profiles Operator (SPO) is a feature-rich
    operator for Kubernetes to make managing seccomp, SELinux and
    AppArmor profiles easier than ever. Recording those profiles from scratch is one
    of the key features of this operator, which usually involves the integration
    into large CI/CD systems. Being able to test the recording capabilities of the
    operator in edge cases is one of the recent development efforts of the SPO and
    makes it excitingly easy to play around with seccomp profiles.

- [20230509 | Kubernetes Installation Tutorial (KLTS Version)](./230509-k8s-install.md)

    Using the DaoCloud-maintained [KLTS (Kubernetes Long Term Support)](https://klts.io/docs/intro/) as an example,
    this article briefly introduces the preparation work and installation steps for installing Kubernetes.

- [20230508 | Cilium Accelerates Sockets with eBPF](./230508-cilium.md)

    With the continuous development of cloud native technology, more and more applications are deployed on the cloud. Some of these applications have very strict real-time requirements, which requires us to improve their performance to achieve faster service speeds.
    To achieve faster service speeds, a scenario is that when two applications that call each other are deployed on the same node, each request and response must pass through the socket layer, TCP/IP protocol stack, data link layer, and physical layer. 
    If requests and responses bypass the TCP/IP protocol stack and directly redirect data packets to the peer socket at the socket layer, it will greatly reduce the time consumed for sending data packets and increase the speed of the service.
    Based on this idea, eBPF technology maps and stores socket information, and uses helper functions to achieve the ability to redirect data packets to the peer socket layer. Cilium is based on this ability of eBPF to achieve socket acceleration effects.

- [20230428 | Kubernetes 1.27: Speed Up Pod Startup](./230428-pod-startup.md)

    How to speed up Pod startup on nodes in a large cluster? This is a problem that cluster administrators often face in enterprises.
    This article focuses on methods to speed up Pod startup on the kubelet side. This method does not involve the time period for controller-manager to create Pods through kube-apiserver, 
    nor does it include the scheduling time of Pods or the time to run Webhooks on them.

- [20230427 | Cloud-Native Monitoring - Basics of VictoriaMetrics](./230427-victoriametrics.md)

    When it comes to cloud native monitoring solutions, the first thing that comes to mind is basically a mature solution set of Prometheus+AlertManager+Grafana. 
    As a monitoring core, Prometheus has powerful features such as strong data modeling, efficient operation, rich monitoring capabilities, powerful query language PromQL, simplicity, and easy management. However, Prometheus is currently not perfect in terms of high availability. For this reason, many alternative and enhanced solutions have emerged in the open source community, and VictoriaMetrics is one of the more outstanding ones. It is a fast, cost-effective, and scalable monitoring solution and time-series database.

- [20230418 | Detailed Explanation of Karmada Failover](./230418-karmada-failover.md)

    In the era of multicloud, how to achieve cross-data center, cross-AZ, and cross-cluster high availability of applications has become a new topic we are exploring.
    In a single cluster, if the cluster fails, all applications in the cluster will not be accessible. Is there a way to help us automatically migrate applications to a new cluster when the cluster fails to ensure continuous external access to the application?

- [20230417 | CNCF Platform Engineering White Paper](230417-cncf-platform-wp.md)

    In 2022, the concept of "platform engineering" is very popular and also on Gartner's hype cycle curve. There are also comments that "DevOps is dead, platform engineering is the future". Developers are unwilling to deal with infrastructure, but enterprise development also needs its own infrastructure. "Platform engineering" unifies these two contradictory points, or "platform engineering" is the next stop of DevOps.

- [20230412 | The feature that has increased the most in the past two years! Kubernetes 1.27 officially released](230412-k8s-1.27.md)

    Kubernetes 1.27 has officially been released. This version is the first version of 2023 and has been released four months after the previous version. In this new version, the release team tracked 60 enhancements, which is much more than previous versions.

- [20230411 | Spiderpool: A new choice for Calico fixed application IP](230411-spiderpool.md)

    Spiderpool is a Kubernetes IPAM plugin project designed primarily for the IP address management needs of underlay networks. It can be used by any CNI project compatible with third-party IPAM plugins.

- [20230405 | Step-by-Step Installation of DCE Community](230405-step-by-step-dce5.md)

    This article completes the installation of DCE Community from 0 to 1 in a cluster of three nodes, including details of K8s clusters, dependencies, networks, storage, and more.

- [20230317 | Edge Native Application Guidelines White Paper](230317-edge-app-wp.md)

    The IoT Edge Working Group has been exploring the definition of edge-native, as well as the similarities and differences between "cloud-native" and "edge-native", and has released the "Edge Native Application Guidelines White Paper".

- [20230315 | Installing DCE Community on Linux](230315-install-on-linux.md)

    Describes how to use Docker and kind to install DCE Community online on a single Linux machine. This is an extremely simple installation method that is easy to learn and experience, and has better performance than the macOS standalone version.

- [20230315 | Installing DCE Community on macOS](230315-install-on-macos.md)

    Create a single-node kind cluster using a macOS laptop and then install DCE Community online. Suitable for beginners to experience and learn, but not suitable for production environments.

- [20230301 | Introduction to the open-source project KWOK](230301-kwok.md)

    What kind of open-source project would be used by Apple, IBM, Tencent, and Huawei within five months of its release? KWOK stands for Kubernetes WithOut Kubelet, which means Kubernetes without Kubelet. It helps you build a cluster consisting of thousands of nodes in seconds and simulates thousands of real nodes with minimal resources.

- [20230214 | How many open source projects are included in DCE Community?](230214-open-projects.md)

    Often, customers, community members, contributors, and sales, delivery, and project teams within the company ask, "Which open-source projects does DCE really involve?" This article details the open-source projects included in the DCE Community.

- [20230214 | "DaoCloud Dao Ke" and Kubernetes](230214-daocloud_k8s.md)

    Describes how "DaoCloud Dao Ke" leverages Kubernetes to create a new generation of enterprise-level cloud native application cloud platforms - DaoCloud Enterprise 5.0, and how to give back to the open-source community and practice cloud native beliefs.

- [20230201 | 2023 Cloud-Native Predictions](230201-forecast.md)

    Based on CNCF's Cloud-Native Report, this article talks about the development of various technologies and trends in the cloud native field in 2023.

- [20230201 | DCE 5.0 Struggle Quotations Collection](230201-peter.md)

    In 2022, in Shanghai, ravaged by the epidemic, lockdowns, controls, and home stays, programmers ran between the cracks of the virus 🦠. That year was the time when DCE 5.0 struggled, and it was also a difficult year for every Chinese person.

## 2022

- [20221209 | K8s 1.26 officially released](221209-k8s-1.26.md)

    Kubernetes has officially released version v1.26, titled "Electrifying". As the last version of 2022, it adds many new features and significantly improves stability. This article introduces the updates in version 1.26

- [20221130 | Karmada Resource Interpreter](https://mp.weixin.qq.com/s/DLDmWRmhM_gMVg1qGnj_fA)

    Karmada is increasingly being used by enterprises in multicloud and hybrid cloud cases. In the actual application process, users often encounter use cases where various resources are distributed to member clusters through PropagationPolicy. This requires that the distributed resource types not only include common Kubernetes native or well-known extension resources but also support distribution of custom user-defined resources. Therefore, Karmada introduces a built-in interpreter to parse common Kubernetes native or well-known extension resources, as well as a custom interpreter to interpret the structure of custom resources, and has recently proposed a configurable interpreter scheme. For both custom resources and common Kubernetes native resources, more flexible and configurable custom methods can be provided to extract specific information about resources such as replica numbers and status.

- [20221125 | KubeCon 2022 North America Station | Highlights Review](https://mp.weixin.qq.com/s/HIxBZjCK8ofCN6C5KRY25w)

    The top cloud native conference, 2022 KubeCon North America Station, which ended in November 2022, brought together more than 300 exciting speeches from cloud native technology experts, product or solution providers, and users from around the world. The themes covered include Kubernetes, GitOps, observability, eBPF, networking, service mesh, and security, among others. This article carefully selects several hot topic speeches from this conference for a brief introduction, to feel the cloud native trends behind each speech and discussion.

- [20221123 | On the Digital Native Road of Auto Enterprises | Review of the Forum](https://mp.weixin.qq.com/s/1leu7b8KQw9pcqma8A_cuw)

    On November 18th, the "Native Road Forum | Cloud-Native Digital Ecosystem Private Sharing Meeting for Auto Enterprises" hosted by DaoCloud was successfully held. Starting from specific cases of auto enterprises, this event mainly shared the application and practice of cloud native in the automotive industry. Let's review the wonderful content of this event together.

- [20221115 | SpiderPool - Cloud-Native Container Network IPAM Plugin](https://mp.weixin.qq.com/s/r6YiuUBGD2KmmMOxl26X6A)

    SpiderPool comes from the experience accumulation of container network landing practice and is an open-source native container network IPAM plugin (github: https://github.com/spidernet-io/spiderpool) developed by DaoCloud. It is mainly used with Underlay CNI to achieve fine-grained management and distribution of IP for container cloud platforms.

- [20221110 | Originating from Passion, Insisting on Beginning with the Original Intention - Happy 8th Birthday to DaoCloud!](https://mp.weixin.qq.com/s/4cYUXtZFc3tIjzphVRCSLg)

    Time flies, and years pass by. Since its establishment in November 2014, DaoCloud has gone through eight years of unremitting efforts by DaoClouders. On the afternoon of November 8th, all the crew members of DaoCloud held a birthday party for DaoCloud. Let's take a look at the grand occasion of DaoCloud eighth birthday party together!

- [20221105 | DaoCloud is a Senior Certified Service Provider for K8s](221116-kcsp.md)

    As early as 2017, DaoCloud successfully passed Kubernetes certification, becoming the earliest service provider in China to enter and be recognized by CNCF. It is also the earliest vendor in China to obtain Kubernetes Training Partner (KTP) certification. Currently, K8s versions that have been officially certified by CNCF include: v1.25, v1.24, v1.23, v1.20, v1.18, v1.15, v1.13, v1.9, and v1.7.

- [20221105 | Financial Digital Transformation from a Native Thinking Perspective](https://mp.weixin.qq.com/s/9BggFRr0aoEzzmemXplRWg)

    On November 5th to 6th, 2022, the 5th International Forum on Financial Technology was successfully held in Chengdu, jointly organized by Southwest University of Finance and Economics, Chengdu Local Financial Supervision and Administration Bureau, and Wenchuan District People's Government of Chengdu. On the afternoon of November 5th, DaoCloud founder and CEO, cloud native computing foundation ambassador Chen Qiyuan, gave a keynote speech on the theme of "Digital Economy Empowers Financial Technology Innovation." Thisspeech mainly discusses the importance of cloud native technology in the financial industry's digital transformation. Chen Qiyuan points out that when promoting digital transformation, companies should not only focus on technology but also pay attention to native thinking, which means understanding the needs of the business and users, and providing personalized solutions based on cloud native technology. The speech also introduces several successful cases of cloud native technology application in the financial industry, such as real-time risk control, intelligent investment advisory, and intelligent customer service.

- [20221103 | DaoCloud Empowers Digital Transformation of Small and Medium-sized Enterprises and Smart Agriculture](https://mp.weixin.qq.com/s/G2nT3DIvWUaCk0aNZmAs1A)

    On November 2nd, 2022, the "Smart Agriculture and Cross-border E-commerce Summit Forum" was held in Chengdu. At the forum, DaoCloud founder and CEO, cloud native computing foundation ambassador Chen Qiyuan gave a speech on "DaoCloud Empowers Digital Transformation of Small and Medium-sized Enterprises and Smart Agriculture." In this speech, Chen Qiyuan shared his insights on digital transformation and introduced how DaoCloud can help small and medium-sized enterprises and smart agriculture through cloud native technology solutions. He emphasized that the key to digital transformation lies in "people-oriented", and only by focusing on the user experience can technology bring real value.

- [20221025 | Openyurt Goes to Europe! Openyurt Community Organizes Meetup in Germany](https://mp.weixin.qq.com/s/EBL-r8LZfGJydEi28N8jYw)

    Openyurt, an open-source project for running Kubernetes workloads on edge nodes, organized a meetup in Frankfurt, Germany, on October 18th. This event brought together experts from the Openyurt community and Kubernetes users from various industries to share their experiences in the field of edge computing. The main topics discussed at the event include Openyurt's latest developments, edge computing architecture design, and practical cases of edge computing deployment.

- [20221022 | KubeCon 2022 North America Station | DaoCloud Shares Cloud-Native Best Practices with Global Developers](https://mp.weixin.qq.com/s/5Uoq9uuITZJFhJjyRcJX0A)

    On October 20th, 2022, KubeCon North America Station officially kicked off in Los Angeles, California. As a cloud native technology service provider with many years of experience, DaoCloud was invited to participate in this grand event and shared its insights on cloud native best practices with global developers. In this article, we will summarize DaoCloud's speeches and interactions during the event, including how to choose the right container container registry, how to optimize Kubernetes cluster performance, and how to implement GitOps-based continuous delivery.

- [20221021 | DaoCloud Launches Container Registry Service Based on Alibaba Cloud Object Storage Service (OSS)](https://mp.weixin.qq.com/s/C89eKlFw8nH7QJzPxT4v1g)

    On October 20th, 2022, DaoCloud officially released its container container registry service based on Alibaba Cloud Object Storage Service (OSS). This service provides users with secure and reliable storage and management of container images, helping them reduce the cost of image storage and improve image access efficiency. Moreover, by using Alibaba Cloud OSS as the underlying storage engine, DaoCloud can provide users with more diversified storage options, such as cold storage and disaster recovery.

- [20221026 | Introduction to Container Management Capability of DCE 5.0](221026-kpanda.md)

    This article explains the capabilities provided by the container management module of DCE 5.0.

- [20221018 | Introduction to Resource Management Capability of DCE 5.0](221018-resource.md)

    This article explains the capabilities provided by the global management module of DCE 5.0.

- [20220925 | Introduction to Workbench Capability of DCE 5.0](220925-amamba.md)

    This article explains the capabilities provided by the Workbench module of DCE 5.0.

- [20220914 | Merbridge Selected in eBPF Panorama](https://mp.weixin.qq.com/s/Ia9Oi3pKuLcrFJwazmpEjg)

    In April 2022, Merbridge was successfully selected for CNCF Cloud Native Landscape and recommended as a cloud native service mesh accelerator.

- [20220909 | Experience Using Clusterpedia](https://mp.weixin.qq.com/s/GAcBIshuaOXUrDgzIguWHg)

    With the increasing scale of business applications running on Kubernetes platforms, the number of clusters is also increasing, and internal resource management and retrieval are becoming more and more complex. In the era of multiple clusters, we can use Cluster-api to create and manage clusters in batches, and use Karmada/Clusternet to deploy applications. However, there seems to be a lack of functionality. How can we view resources in multiple clusters in a unified way?

- [20220908 | Huawei and DaoCloud Launch Cloud-Edge Collaborative Superconverged All-in-One Machine for Metaverse](https://mp.weixin.qq.com/s/r8vfFofBy7v1VcUMInp_Iw)

    On September 2, 2022, at the World Artificial Intelligence Conference, Huawei and Shanghai DaoCloud Network Technology jointly launched a "cloud-edge collaborative superconverged all-in-one machine" for innovative businesses in the metaverse, bringing cloud native capabilities to the edge to provide real-time virtual digital world experiences and achieve true cloud-edge integration in the metaverse.

- [20220905 | How to Build a Storage Foundation and Create a Cloud-Native Application Base? | Discussion on Native](https://mp.weixin.qq.com/s/vrBAjdCkI2BKxG7SsSX2Uw)

    The cloud native transformation of applications greatly improves their core capabilities such as availability, stability, scalability, and performance, while also profoundly changing all aspects of applications. As the cornerstone of application running, storage is inevitably affected. In the context of the cloud native era, what challenges has it brought to storage, and how can we respond to them? In the eleventh issue of Discussion on Native, DaoCloud and Huawei will share their cloud native storage solutions.

- [20220810 | Cluster API Retrieval Has Never Been So Easy](https://mp.weixin.qq.com/s/8F20pchW6WhbEdlU56qFsg)

    Clusterpedia is a CNCF sandbox project for cross-cluster complex resource retrieval. It can synchronize resources with multiple clusters and provide more powerful search features based on Kubernetes OpenAPI compatibility to help you quickly, easily, and effectively obtain any multicluster resources.

- [20220808 | Introduction to Multicloud Management Capability of DCE 5.0](220808-kairship.md)

    This article explains the capabilities provided by the Multicloud Management module of DCE 5.0.

- [20220708 | Introduction to Service Mesh Capability of DCE 5.0](220708-mspider.md)

    This article explains the capabilities provided by the service mesh module of DCE 5.0.

- [20220622 | Clusterpedia Officially Enters CNCF Sandbox as the First multicloud Retrieval Open Source Project](https://mp.weixin.qq.com/s/K2jG64msI4j-mWqPF0qkKg)

    On June 15, 2022, the Cloud Native Computing Foundation (CNCF) announced that Clusterpedia had officially joined the CNCF sandbox project. Clusterpedia is an open-source project launched by DaoCloud at the end of 2021. It is a tool that can perform complex resource retrieval across multiple clusters with kubectl, and it is currently the only project in CNCF that focuses on multicloud information retrieval and is widely used.

- [20220611 | CloudTTY: Next-generation Cloud native Open Source Cloud Shell](https://mp.weixin.qq.com/s/sFjZmvumQNbP6gnlnpglWQ)

    CloudTTY is a cloud native open-source project based on Kubernetes, which solves a series of functional requirements under "web command line" permission control on the cluster.

- [20220609 | Hot Cloud native Technology Sharing at KubeCon EU | Highlights Review](https://mp.weixin.qq.com/s/2ukrV3M6dGdwzRPnigovkw)

    At the recently concluded flagship cloud native conference KubeCon + CloudNativeCon Europe 2022, global cloud native technology experts, product or solution providers, and users exchanged and discussed extensively on cloud native technology. This article shares some of the popular cloud native open-source projects at the conference from three aspects: external integration, self-evolution, and internal related functional features, so let's dive into the cloud native world together.

- [20220606 | Merbridge CNI Mode](https://mp.weixin.qq.com/s/3t2FshkQpVHQ44zbBIQDRQ)

    The emergence of Merbridge CNI mode aims to better adapt to the features of service mesh. When there was no CNI mode before, Merbridge could do relatively little. The biggest problem was that it couldn't adapt to the Sidecar Annotation injected by Istio, which made Merbridge unable to exclude traffic from certain ports or IP ranges. At the same time, because Merbridge only processed connection requests within the Pod before, it meant that if it was external traffic sent to the Pod, Merbridge would not be able to handle it.

- [20220606 | DCE 5.0 Development Background](221008-dce-bg.md)

    Describes the background of the birth of DaoCloud Enterprise 5.0, the new generation of cloud native operating system.

- [20220530 | Cloud-Native Layout Speeds up, What is the Market Prospect? Take a Look at This Guide](https://mp.weixin.qq.com/s/S6CUDwCDZh-I4e5D1SZa4A)

    This article uses an infographic to illustrate the fast-developing cloud native and cloud computing trends currently.

- [20220520 | Into Observability | Discussion on Native](https://mp.weixin.qq.com/s/f0oZV5nWfc42b-b0cLkh2g)

    Since 2018, observability has been introduced into the IT field, and the CNCF-Landscape organization created a subgroup for observability. Since then, observability has gradually replaced traditional system monitoring and shifted from passive monitoring to active observation of various data related to application associations, becoming one of the hottest topics in the cloud native field.

[^1]: CNCF: Cloud Native Computing Foundation, affiliated with the Linux Foundation, was established in December 2015 as a non-profit organization dedicated to cultivating and maintaining a vendor-neutral open-source ecosystem to promote cloud native technology and popularize cloud native applications.
[^2]: Cloud native landscape: Maintained by CNCF since December 2016, it summarizes mature and widely used products and solutions in the community, classifies them, and provides references for enterprises to build a cloud native system. It has extensive influence in the development and operation and maintenance fields of the cloud ecosystem.
