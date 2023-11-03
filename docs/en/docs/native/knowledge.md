# Knowledge sharing

This page shares some technical articles related to cloud native, and we hope that everyone can make progress hand in hand.

### Troubleshooting

- [How do you solve the storage capacity problem with Prometheus?](https://mp.weixin.qq.com/s/TMApz8FxT91qBvS1fzuTVw)

    The poor scaling of standalone storage is a widely criticized problem with Prometheus. The article gives 3 clustering solutions to this problem.
    Prometheus federal cluster, remote storage solution, Prometheus own build cluster, these three solutions can solve the storage problem of Prometheus well.

- [How can nettrace quickly perform network troubleshooting in cloud native use cases?](https://mp.weixin.qq.com/s/0n7kbOhHr6m5JClTrSIysA)

    [nettrace](https://github.com/OpenCloudOS/nettrace) is an eBPF-based network toolset that integrates network message tracing (fault location), network troubleshooting, and network anomaly monitoring.
    It provides a more efficient and easy-to-use method to solve network problems in complex cases.

- [Istio Operations Practice: How to Avoid 503 UC Errors](https://mp.weixin.qq.com/s/4YIYPIszyKyWVMKXnXtHbg)

    503 UC is a common problem encountered during Istio/Envoy usage.
    The article analyzes the principle of 503 UC caused by TCP server keepalive timeout and how to circumvent it.

- [K8s CNI Cilium Network Troubleshooting Guide](https://mp.weixin.qq.com/s/jBuNPOKbL-keXmzq1gq-mQ)

    The article describes a problem the author encountered when upgrading from kubenet to cilium and the troubleshooting process. The problem was that pods on nodes in the kubenet network could not access pods on nodes in the cilium network. by grabbing packets and testing, and analyzing information about cilium, we found the problem: cilium does not manage all k8s nodes, and the remaining nodes are handled as external servers.

- [How to troubleshoot Kubernetes Service efficiently](https://blog.getambassador.io/how-to-debug-a-kubernetes-service-effectively-3d4eff0b221a)

    The article briefly describes how the service works, the various bugs that can occur when running the service, and how to resolve them. Finally, it introduces an efficient troubleshooting tool [Telepresence](https://github.com/telepresenceio/telepresence). Telepresence enables to build a remote development environment for Kubernetes, and users can still use their own local tools, such as IDEs and debuggers, and test local services against microservices in remote K8 clusters.

- [K8s: Completely solve the problem of the node's local storage being exploded](https://mp.weixin.qq.com/s/pKTA6O3bdko_eHaw5mU3gQ)

    The local storage of the K8s node stores content such as images, writable layers, logs, and emptyDir.
    Except that the container image is controlled by the system mechanism, everything else is related to the application.
    It is not reliable to completely rely on developers to limit the storage space used by applications. Therefore, K8s provides garbage collection, total log limit, emptyDir volume limit, and total temporary data limit to avoid the problem of insufficient local storage.

- [Discussion on K8s lossy release issues](https://mp.weixin.qq.com/s/jKVw0m5Ho2AtFRScnKEMKw)

    The application release process is actually a process of new Pods going online and old Pods going offline. When there is a problem with the update of traffic routing rules and the application Pods going offline, traffic loss will occur.
    In general, in order to ensure that the traffic is not damaged, it is necessary to ensure the tacit cooperation between the traffic path and the Pod's offline and offline from the gateway parameters and Pod lifecycle probes and hooks.
    The article starts with the K8s traffic path, analyzes the causes of lossy releases, and gives solutions.

- [K8s: 13 Abnormalities of Pod](https://mp.weixin.qq.com/s/cEEdH7npkSHmVHSXLbH6uQ)

    The article summarizes 13 common abnormal use cases of K8s Pod, gives the common error status of each scenario, analyzes its causes and troubleshooting ideas.

- [K8s: Everything you need to know](https://enterprisersproject.com/sites/default/files/2022-11/tep_white-paper_kubernetes-what-you-need-to-know%2Brev2.pdf)

    The e-book includes all the definitions you need to understand Kubernetes, and also includes introductions to other Kubernetes-related e-books, articles, instructional videos, and other resources, as well as 7 best practices.

- [Docker Volume causes K8s Terminating Pod problem](https://mp.weixin.qq.com/s/SMynKYP4obMSl6GQdwDlEw)

    Terminating Pod is a typical problem encountered after business containerization, with different causes.
    The article records how the NetEase Shufan-Qingzhou Kubernetes enhancement technical team conducted a step-by-step investigation, found that too many Docker Volume directories caused the Terminating Pod problem, and gave a solution.

- [Having network issues after installing Kubernetes or upgrading the host OS? This may be a problem with your iptables version](https://www.mirantis.com/blog/networking-problems-after-installing-kubernetes-1-25-or-after-upgrading-your-host-os-this-might-be-your-problem)

    After installing a new version of Kubernetes, your worker nodes can't connect to the network, and suddenly you can't ssh access or even ping them?
    This may be due to a conflict between the iptables version of kube-router 1.25 and the version you have installed.
    It boils down to the incompatibility of the rule format between iptables 1.8.8 and older versions.
    For this, there are three solutions: downgrade the iptables version to 1.8.7, clean up IPTables chain ownership (alpha), or use a lightweight Kubernetes distribution [k0s](https://github.com/k0sproject/k0s) solve.

- [Using eBPF to troubleshoot Kubernetes cluster disk I/O performance](https://mp.weixin.qq.com/s/RrTjhSJOviiINsy-DURV2A)

    The problem started when eBay engineers found that their Kafka service sometimes failed to catch up with the leader's data.
    To solve the problem, some eBPF tools are used, for example, [biopattern](https://github.com/iovisor/bcc/blob/master/tools/biopattern.py) is used to show the disk I/O pattern, [ebpf_exporter](https://github.com/cloudflare/ebpf_exporter) for data collection and visualization.

- [Kubernetes Network Troubleshooting Hardcore Guide](https://mp.weixin.qq.com/s/mp5coRHPAdx5nIfcCnPFhw)

    This page introduces the idea of network troubleshooting in a Kubernetes cluster, including Pod common network anomaly classification, troubleshooting tools, troubleshooting ideas and process models, CNI network anomaly troubleshooting steps, and case studies.

- [Summary of Redis cache exceptions and solutions](https://mp.weixin.qq.com/s/P38ETBZJO2lNlE-i7g6HhA)

    In the actual application process of Redis, there will be abnormal situations such as cache avalanche, cache breakdown and cache penetration. If these situations are ignored, it may bring disastrous consequences. This page analyzes and analyzes these cache abnormalities and corresponding solutions. Summarize.

- [K8S Internals Series: The Mystery of the Disappearance of Storage Volume metrics](https://mp.weixin.qq.com/s/Sd1TY9ml65MQYVSupmvpbw)

    This page was inspired by the fact that Grafana does not display the capacity metrics of storage volumes created with storage drivers. It shows the troubleshooting ideas and methods for this problem, and then outlines the implementation process of Kubelet for collecting storage volume metrics.

### Best Practices

- [Running StatefulSet across clusters](https://mp.weixin.qq.com/s/y1dEO8Fb3SxqQUW9WrEsHQ)

    Running StatefulSet reliably across clusters may require addressing both network and storage issues.
    The article describes one way to configure and manage stateful application services across clusters, based on an example.

- [How can we develop open source communities based on cloud native projects?](https://thenewstack.io/how-do-we-cultivate-community-within-cloud-native-projects/)

    Developing an open source community based on a cloud native project starts with knowing who will care about your project, who are the end users, stakeholders and contributors?
    What work do they do, where do they work, and what are their usage goals?
    Discovering more potential stakeholders and providing them with a path to contribute is critical to increasing the adoption of your project.

- [Dapr integration with Flomesh for cross-cluster service calling](https://mp.weixin.qq.com/s/Y-MewxHVMULKDi4_cbl6Yw)

    [Flomesh Service Mesh](https://github.com/flomesh-io/fsm) uses Pipy, a programmable agent, to provide east-west and north-south traffic management for the core.
    By breaking through the network isolation between computing environments with L7-based traffic management capabilities, a virtual flat network is created that allows applications in different computing environments to communicate with each other.
    The article describes the integration of Dapr with the Flomesh service mesh for cross-cluster service calls, enabling "true" multicluster interoperability.

- [How to mitigate container isolation vulnerabilities and monitor kernel critical paths in cloud native use cases?](https://mp.weixin.qq.com/s/qlmm2h8RpQnKOnEjlK0pMA)

    This page introduces two solutions developed by the OpenCloudOS community: CgroupFS and SLI, for mitigating container isolation vulnerabilities and monitoring kernel critical paths.
    The CgroupFS scheme provides a kernel-state container view of the VM file system (/proc, /sys), which enhances container resource view isolation.
    SLI is a container-level performance tracking mechanism that tracks and observes the competition for CPU and memory resources from the container's perspective, thus providing reliable metrics for locating and analyzing container performance problems.

- [Easy gRPC to REST transcoding based on Kubernetes and Istio](https://cloud.redhat.com/blog/grpc-to-rest-transcoding-with-openshift-and-service-mesh)

    The article describes how to make gRPC services REST compatible without extensive code changes.
    The solution uses Envoy filters to build a transcoder that allows RESTful JSON API clients to send requests over HTTP and be proxied to a gRPC service.
    The transcoder encodes the message output of the gRPC service method as JSON and sets the Content-Type header of the HTTP response to application/json.

- [Optimization of kube-state-metrics under large scale clusters](https://mp.weixin.qq.com/s/8R55Holzrf0wNVD8DLJnAg)

    In small-scale clusters, you only need to ensure kube-state-metrics is highly available for use in production environments.
    However, for large scale clusters, providing metrics through only one KSM instance is very overwhelming and requires many optimizations.
    For example, filtering unneeded metrics and tags, reducing the pressure on KSM instances by slicing, and using DaemonSet to deploy pod metrics separately.

- [Vivo Self-Developed Jenkins Resource Scheduling System Design and Practice](https://mp.weixin.qq.com/s/wEmheHwTA8m8LHr_5LVSyg)

    The article starts from the current industry implementation solutions for Jenkins high availability, analyzes the advantages and disadvantages of each solution, and introduces the Jenkins scheduler system, the Jenkins high availability solution currently used by vivo.
    The system does not use the native Jenkins deployment scheme, but adopts the full master approach, and the relationship between masters, task assignment, offline, and plugin installation are managed by the scheduling system.
    The system is currently running in a production environment.

- [Three things to do before migrating cgroup v2 for K8s](https://mp.weixin.qq.com/s/BV-y82MalhG-A--hvUFMcg)

    With the official release of Kubernetes 1.25 on cgroup v2 features (GA), kubelet container resource management capabilities have been enhanced.
    Based on the cgroup v2 concept, the article introduces the three things to do before adopting cgroup v2 in terms of Linux OS, K8s ecosystem, and application changes.

- [Alibaba Cloud Cloud Native Hands-on Guide](https://developer.aliyun.com/ebook/7879?spm=a2c6h.26392470.ebook-read.13.3e855bc8YpIdco)

    The guide covers global cloud native application insights and trends, AliCloud's latest product and technology layout in the cloud native space, AliCloud's new thinking and input on All in Serverless, and hands-on experience on cloud from companies like Transn, New Oriental, and Little Red Book.

- [service mesh Security and High Availability Deployment Best Practices](https://mp.weixin.qq.com/s/hFCshQpmF7Vr0jrpugArjA)

    Article on security and high availability best practices when deploying service meshs in a multicluster infrastructure, including: how control planes should be deployed near applications; how ingress should be deployed to promote security and agility; how to use Envoy to promote cross-cluster load balancing, and how to use certificates inside the mesh.

- [Open Source Strategy Development and Implementation for Medium and Large Technology Enterprises](https://mp.weixin.qq.com/s/9Z4zFPU0uHk6RhrpUDD-tw)

    At present, many enterprises still have some difficulties about what open source is, how to use open source, how to participate in open source, how enterprises make decisions in open source, how to conduct open source governance, and how to use open source to strengthen competitiveness.
    In this regard, the article introduces what is an enterprise open source strategy; why enterprises need an open source strategy; what an enterprise open source strategy contains, and the practical experience of developing and implementing an enterprise open source strategy.

- [Use of ServiceAccount Token in Different K8s Versions](https://mp.weixin.qq.com/s/F0V8nyo3LtATFmS7pHuxXw)

    This page describes the different ways of using ServiceAccount Token in different K8s versions.
    The article introduces the different ways to use ServiceAccount Token under different K8s versions, mainly including automatic Secret creation and Kubelet to request API via TokenRequest API.

- [Tencent's Million-Level Container Cloud Platform Practice Revealed](https://mp.weixin.qq.com/s/Gusp1ah_qIoMMOg7FhX6Vg)

    The article introduces the problems encountered in the containerized deployment of online business resources on Tencent's container cloud platform, the challenges of containerization on dynamic route synchronization and the respective solutions.
    And a new self-healing mechanism for container destruction failure is explored to solve the problem of container destruction stage stuck in the existing self-healing mechanism of K8s.

- [mTLS Best Practices for Kubernetes Zero Trust Security](https://mp.weixin.qq.com/s/QYeP6WZKG0gjJ2u6k1fXxQ)

    This page describes three best practices for implementing mutual TLS (mTLS) in Kubernetes,
    These include not using self-signed certificates, rooting Istio's trust in existing public key infrastructure (PKI), using intermediate certificates.

- [Interpretation of how to choose K8s elastic strategy from the perspective of microservice application](https://mp.weixin.qq.com/s/jfpF3WUs4YvtlJ8Q4zsuxg)

    For cluster resource elasticity, the K8s community has given two solutions, Cluster Autoscaler (CA) and Virtual Kubelet (VK).
    The article focuses on the form and characteristics of microservice applications, analyzes the use cases of CA and VK, and summarizes how to choose cluster resource elasticity for applications under the microservice architecture.

- [Introduction to the components of the GitOps software delivery pipeline](https://www.weave.works/blog/infographic-gitops-pipeline)

    The article summarizes the components needed to get started with GitOps, including container platforms, Git repositories, container registries, GitOps agents, and build servers.
    And some components that can be added when scaling up, such as container configuration automation, policy engine, service mesh, progressive delivery tools, event monitoring, etc.

- [Interpretation of Wanzi, how to build the Nginx load balancing system of the K8s container platform from 0 to 1](https://mp.weixin.qq.com/s/Q1DXAEL4ceUcUCQjHAIU5Q)

    The article introduces the practical experience of building a large-scale Kubernetes container platform Nginx load balancing system from 0 to 1,
    Including the business requirements and operation and maintenance requirements of the system, requirements for Nginx-Controller components, architecture design, experience optimization, and core considerations.

- [How to manage dependencies of cloud native applications](https://mp.weixin.qq.com/s/SipnQhbaa7WlpwORTVLCRw)

    The article introduces some best practices for cloud native application dependency management, such as using depcheck to check for unused dependencies, using dependency check scripts to detect expired dependencies,
    And leverage the automated dependency management open source tool [Mend Renovate](https://github.com/marketplace/renovate) to automatically create pull requests for all types of dependency updates.

- [K8s: Using Mutating Admission Controller to Simplify Application Environment Migration](https://blog.getambassador.io/using-mutating-admission-controllers-to-ease-kubernetes-migrations-5699c1901015)
  
    Kubernetes' Mutating Admission Webhooks are often used to enforce security practices and ensure resources follow specific policy or configuration management.
    The article introduces a new use case: simplifying the migration of applications, enabling rapid updates to the new environment's inventory while keeping the old environment up and running.

- [Alibaba cloud container attack and defense matrix & API security lifecycle, how to build a financial security cloud native platform](https://mp.weixin.qq.com/s/ZKsIn0UzrrSGWWMv8Sk4Nw)

    This page introduces the threat surface brought by the application of container platforms (container attack and defense matrix) and APIs in the financial technology field from the perspective of attackers, analyzes the threats, and gives practical suggestions for the security protection practices of container platforms and APIs throughout their lifecycle.

- [How did the world's top open source company find the top 1000 community users? ](https://mp.weixin.qq.com/s/edy6FsD1d_9fp-U60H_dug)

    The article shares how the open source projects and open source communities of 4 top open source commercial companies (HashiCorp, Confluent, Databricks, and CockroachDB) operate, how to find the top 1,000 community users and how long it took, and growth metrics, etc.

- [How to practice DevOps in a container cloud multicluster environment](https://mp.weixin.qq.com/s/MW67DhLzUWXm0xHd5LH0Tw)

    The article introduces how to implement multicluster DevOps through GitOps, recommends a multicluster GitOps workflow as a reference, and finally introduces the mainstream way to practice GitOps in continuous integration and continuous delivery.

- [Three Misunderstandings of Kubernetes HPA and Guide to Avoiding Pitfalls](https://mp.weixin.qq.com/s/3eSm0BZSrPUAZQQhG_L_5A)

    Kubernetes provides horizontal elastic expansion capability (HPA), which allows applications to expand/shrink according to real-time metrics.
    However, the actual working situation of HPA may be different from what we expected. There are some cognitive misunderstandings here. For example, HPA has a dead zone for expansion, expansion does not match the expected usage, and elastic behavior always lags behind.
    In this regard, the article summarizes some precautions to help "effectively avoid pits" when using HPA.

- [It's time to think about K8s outbound traffic security (top)](https://mp.weixin.qq.com/s/Lj3sl-Ukday9WP4U-8-vqA)[&(bottom)](https://mp. weixin.qq.com/s/NMh1XbBXeyfGuJJ8kZ6J2Q)

    We often pay attention to the capabilities of Ingress, but ignore the security control of Egress traffic. However, no matter from the perspective of security or compliance, egress traffic should be strictly controlled.
    This page analyzes the reasons for egress traffic policy control, existing challenges, and analysis of industry solutions. The solutions include six categories: based on K8s Network Policy, CNI, Service Mesh, micro-segmentation technology, and DNS interception.

- [How to ensure cloud native clustersSecurity](https://mp.weixin.qq.com/s/sv40SzD7Ic1eMeElvccs7A)

    This page is a summary of the contents of the container cluster security exchange forum.
    Contents include: classification, prevention and solutions of cloud cluster security, principles of cluster division on container cloud, cluster audit, node security guarantee, etcd cluster security, design of network strategy to ensure the security of cluster resources, network isolation issues, and security levels according to security Standardized policies or configurations for k8s clusters, etc.

- [How many nodes should the Kubernetes control plane have](https://thenewstack.io/how-many-nodes-for-your-kubernetes-control-plane/)

    The article provides a reference for sizing the Kubernetes control plane. For most use cases, 3 nodes are sufficient.
    5 nodes will provide better availability, but at a higher cost in terms of required number of nodes and hardware resource consumption.
    Additionally, monitoring and backing up etcd and control plane node configurations are best practices for troubleshooting node failures and preventing surprises.

- [Using Istio to reduce cross-zone traffic charges](https://www.tetrate.io/blog/minimizing-cross-zone-traffic-charges-with-istio/)

    Deploying a Kubernetes cluster across Availability Zones has significant reliability benefits, but requires some additional configuration to keep traffic locally.
    Istio's locally-aware routing can help reduce latency and minimize cloud provider cross-region data charges for application traffic.

- [The 2-minute test for Kubernetes pod security](https://dzone.com/articles/the-2-minute-test-for-kubernetes-pod-security)

    Run the [Kyverno CLI](https://github.com/kyverno/kyverno) from outside the cluster to audit the cluster for compliance with the latest [Kubernetes Pod Security Standard](https://kubernetes.io/docs/concepts/security/pod -security-standards/) and enforce policies for each control defined in the pod security standards. Auditing does not require anything to be installed in the cluster.

- [Practice of Proxyless Mesh in Dubbo](https://mp.weixin.qq.com/s/TH8waHN00y6q26NUDY9wzg)

    [Dubbo Proxyless Mesh](https://github.com/apache/dubbo-awesome/blob/master/proposals/D3.2-proxyless-mesh.md) directly implements xDS protocol analysis and realizes direct communication between Dubbo and Control Plane, and then realize the unified control of traffic control, service governance, observability, security, etc., and avoid the performance loss and deployment architecture complexity brought by the Sidecar mode.

- [Best Practices of K8s Security Monitoring under Zero Trust Strategy](https://mp.weixin.qq.com/s/wYUNsGaWEnQZ0BVxsQORbA)

    This page introduces how to use K8s-related security data sources and collection technologies in a distributed containerized environment to monitor K8s clusters, discover abnormal API access events, abnormal traffic, abnormal configurations, abnormal logs and other behaviors in a timely manner, and combine reasonable alert strategies to establish A more proactive security defense system.

- [Best Practices of Container Security Based on DevOps Process](https://mp.weixin.qq.com/s/y42BgaosyIQnA1uDEgqTPA)

    The article shares 14 container security practices applicable to the DevOps workflow summarized by Qingteng Cloud Security, including 6 security left-shift steps in the defense phase, safe running containers in the protection phase, abnormal behavior alerts in the detection phase, and response phase incident response and forensics.

- [How to Design a “Golden Path” for Internal Development Platforms](https://cloud.redhat.com/blog/designing-golden-paths)

    The "Golden Path" refers to a pre-architected approach to building and deploying a piece of software.
    This method is based on the precipitation of best practices, can accelerate the development efficiency of typical applications, and is a prerequisite for successfully building an internal development platform (IDP).
    The article describes what a "Golden Path" should be and a simple correlation maturity model, and shows an example of how to implement a "Golden Path".

- [Managing GPU resources in a cloud native way](https://mp.weixin.qq.com/s/W-Ntu2xdjypFgs5EPMVjkg)

    The article introduces how to manage GPU resources in a cloud native way, including unifying GPU resources and frameworks, and improving GPU utilization through qGPU sharing, which reduces the difficulty of managing GPU resources at the cluster level.

- [Microservice Full Link Grayscale New Capabilities](https://mp.weixin.qq.com/s/JL7Ru4nIiP2XuXwNiw2TtA)

    This page mainly introduces the use cases and pain points of Alibaba Cloud MSE service governance based on the full-link grayscale capability and two new capabilities: white screen at runtime and configuration grayscale.
    The white screen at runtime is used to gain insight into the traffic matching and running behavior of the whole link grayscale; the configuration grayscale refers to the grayscale capability that the ConfigMaps in the microservice application should have, so as to deal with the grayscale application’s special configuration value appeal.

- [Kubernetes Cluster Utilization Improvement Practice](https://mp.weixin.qq.com/s/IAo41AZ0aAkIxY-JzonXMQ)

    The article shares the ideas and implementation methods of improving the utilization rate of Kubernetes clusters, including two-level expansion mechanism, two-level dynamic overselling, dynamic scheduling, and dynamic eviction.

- [OpenTelemetry Integration Progress Report for NGINX Modern Application Reference Architecture (MARA)](https://mp.weixin.qq.com/s/j1dknNrFz0XqXSB2-Cwc3g)

    [MARA](https://github.com/nginxinc/kic-reference-architectures) is production-ready code that can be used to build and deploy modern applications in a Kubernetes environment.
    The article describes MARA's need for a versatile open source observability tool, then describes the trade-offs and design decisions in selecting OpenTelemetry,
    And what technologies are used to integrate OpenTelemetry with microservices applications built using Python, Java, and NGINX.

- [Istio external control plane deployment practice](https://mp.weixin.qq.com/s/TaQWryqD5AwWMJOXbejaqg)

    Through the investigation and deployment of the external Istiod deployment model, the author analyzed its architecture and the part of the deployment yaml file used by it, and summarized some problems that may be encountered during the deployment process.

- [Monitoring Cilium's key metrics](https://www.datadoghq.com/blog/cilium-metrics-and-architecture/)

    The article describes the key metrics for monitoring Cilium: health of endpoints, Kubernetes network status, effectiveness of network policies, performance of Cilium's API processing and rate limiting.

- [A cloud native security layered approach based on service mesh](https://www.tetrate.io/blog/lateral-movement-and-the-service-mesh/)

    The article focuses on how to leverage service mesh to optimize existing security tools and practices at each layer of the OSI model.
    A service mesh is well suited as the layer closest to the application, sitting on top of (and hiding) the underlying security layer, providing services with in-transit encryption, application identity, and application-level access control.

- [Observability: Sampling Scenes and Implementation Cases (Part 1)](https://mp.weixin.qq.com/s/tnYUOHJT0TOh4iYBHlP4aA)

    The article successively introduces the use cases of sampling, the position of sampling in the call chain system architecture, the main schemes (head coherent sampling, unit sampling and tail coherent sampling), sampling implementation of mainstream open source and commercial systems, landing cases, etc.

- [Observability sampling use cases and landing cases (Part 2)](https://mp.weixin.qq.com/s/nxnz37VJydNHFMaEywu9KA)

    The author shared some thoughts on the sampling design of observable systems around some landing cases.
    First analyze the necessity of full sampling and the traces suitable for full sampling, and then share the complete sampling solutions in the industry such as Ali Eagle Eye and ByteDance and the sampling case of OpenTelemetry production environment.

- [How to extend K8s Descheduler strategy](https://mp.weixin.qq.com/s/pkDxexvrzmtuLMWwzi0p_g)

    The features of the community Descheduler are far from meeting the needs of the company's internal production environment.
    The article describes extensions to the LowNodeUtilization and HighNodeUtilization strategies.
    When using Descheduler to migrate pods, it is necessary to take some measures to ensure the stability of the business. After improving the component features, it is also necessary to evaluate the effect of the service itself.

- [Kubernetes resource topology-aware scheduling optimization](https://mp.weixin.qq.com/s/CgW1zqfQBdUQo8qDtV-57Q)

    The article first introduces the business cases of Tencent Star Computing Power and the knowledge related to refined scheduling, and then conducts research on the K8s and Volcano communities, and finds that the existing solutions have limitations.
    Finally, through the pain point problem analysis, the corresponding solution is given.
    After optimization, the training speed of the original test task is increased to 3 times, and the eviction rate of CPU preemption is greatly reduced to the physical machine level.

- [How to properly configure RBAC to prevent container escape](https://mp.weixin.qq.com/s/tV3HOaE3TzJ6EbuEmYYfdA)

    The article introduces the idea of using dangerous RBAC configurations to elevate privileges in the cluster, so as to illustrate the impact of improper privilege configuration after container escape.

- [How to optimize Prometheus query performance](https://thenewstack.io/query-optimization-in-the-prometheus-world/)

    A problem that is often encountered when using Prometheus is that as the amount of collected metric data increases, query performance decreases.
    The article describes factors that affect Prometheus query performance, options provided by Prometheus to identify slow/inefficient queries, and ways to optimize query performance (such as shortening query time ranges, reducing index resolution, etc.).

- [vivo container cluster monitoring system architecture and practice](https://mp.weixin.qq.com/s/SBZO48fWcEojlDlBROdogQ)

    Based on the practical experience of vivo container cluster monitoring, This page discusses how to build the cloud native monitoring architecture, introduces the design ideas of vivo container cluster monitoring architecture from two aspects of monitoring high availability and data forwarding layer components high availability, and finally summarizes the practical Challenges encountered in the process and countermeasures.

- [Multi-Active Architecture Guide for Hybrid Cloud](https://mp.weixin.qq.com/s/NXXwjxUAGXDD3krKXyJbaQ)

    The article introduces the multi-active architecture of Jobbang Company in a hybrid cloud environment: the network between multiclouds is a state between single-cloud multi-availability zones and center-edge;
    The normal inter-application call closed-loop is within the single cloud, and only requires independent registration and discovery within the single cloud;
    Cross-cloud calls in some cases only require inter-cluster discovery;
    With full cloud deployment, north-south traffic can be prioritized for scheduling through DNS.

- [How to Harden Kubernetes in 2022?](https://elastisys.com/nsa-cisa-kubernetes-security-hardening-guide-and-beyond-for-2022/)

    The author of the article believes that the ["Kubernetes Hardening Guide"](https://media.defense.gov/2022/Aug/29/2003066362/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF issued by the US National Security Agency last year ) There is a big gap between the abstract and the main content later.
    To this end, the authors conclude the report with some additional insights related to configuration, applying arbitrary permissions, image scanning, security testing, etc.

- [Application of Chaos Engineering in Microservice Scenario](https://mp.weixin.qq.com/s/dEA3g3JnAKloW6K7cUskYQ)

    Hangzhou Mike Technology introduced Chaos Mesh, a cloud native chaos engineering testing platform, to solve the pain points encountered in the robustness testing of microservices in cloud financial use cases.

- [Baidu Cloud Native Mixed Department Large-scale Implementation Road](https://mp.weixin.qq.com/s/OgU2uRGhIy7r6WucvdrPzg)

    Hybrid technology, that is, online business and offline tasks are mixed and deployed on the same physical resources, and resource isolation, scheduling and other control methods are used to make full use of resources while ensuring service stability.
    The Baidu cloud native hybrid system is mainly divided into three parts: stand-alone management layer, scheduling layer, and operation layer.
    The stand-alone layer provides resource quality management, kernel-level QoS isolation, resource view reporting and policy enforcement, and eBPF fine-grained metric collection capabilities;
    The scheduling layer is responsible for the perception of resource dynamic source view and providing the best scheduling strategy;
    The operation layer provides features such as resource portrait, resource operation, water level setting, and hot spot management.

- [6 Best Practices for Kubernetes Security Compliance](https://mp.weixin.qq.com/s/MQh16-PQYsjaGCjwyxIk_A)

    The article describes 6 practices to follow to ensure continued compliance in a containerized environment without compromising productivity:
    Automate, secure Kubernetes itself, detect attacks in advance, focus on zero trust, and leverage Kubernetes built-in security measures to verify the security of cloud hosts.

- [How to enforce egress traffic using Istio authorization policies](https://www.tetrate.io/blog/istio-how-to-enforce-egress-traffic-using-istios-authorization-policies/)

    The article takes "sleep services in two independent namespaces in the service mesh to access external services of Google and Yahoo" as an example, and introduces how to use Istio's egress gateway to implement egress authorization policies with similar policies when implementing ingress policies.

- [Practice and exploration of solving traffic loss problem under microservice architecture](https://mp.weixin.qq.com/s/eQzy3zvvEokNXYL637LNCg)

    Although the three axes of grayscale, observable, and rollback safety production can minimize the impact on users caused by the application's own code problems during the release process, it is harmful to short-term traffic in the case of high concurrency and large traffic But still can't solve it.
    Therefore, This page focuses on how to solve the problem of traffic loss during the publishing process, and how to achieve lossless online and offline effects during the application publishing process.

- [Alibaba's Envoy Gateway Practice](https://mp.weixin.qq.com/s/t1ppAQfm0cPmqhxEARB03Q)

    The article briefly introduces the history of Alibaba's exploration of next-generation gateways: Envoy Gateway 1.0 (incubation period) is mainly used for RPC intercommunication of east-west traffic;
    2.0 (growth stage) uses Tengine + Envoy two-tier gateway to undertake north-south gateway traffic;
    3.0 (mature stage) combines traffic gateway + microservice gateway into one through Envoy, supplemented by hardware acceleration, kernel tuning and other means.

- [Alibaba Cloud released "Cloud Native Practical Case Collection"](https://developer.aliyun.com/ebook/read/7575?spm=a2c6h.26392459.ebook-detail.4.17f14848W6TyWT)

    Alibaba Cloud released the "Cloud Native Practical Case Collection", which provides some reference and reference for enterprise practice and implementation of cloud native through technology outlook, industry analysis, and interpretation of actual combat cases.

- [Alibaba Cloud Releases Enterprise Cloud Native IT Cost Governance Solution: Five Capabilities Accelerate Enterprise FinOps Process](https://mp.weixin.qq.com/s/hAHNlAi8c0OAO7zSq31J1w)

    Enterprise cloud native IT cost governance has problems such as the lifecycle mismatch between business units and billing units, the contradiction between dynamic resource delivery and static capacity planning, and the adaptation of enterprise IT cost governance models to cloud native architectures.
    As a result, Alibaba Cloud Container Service has launched an enterprise cloud native IT cost governance solution, which provides features such as enterprise IT cost management, cost visualization, and cost optimization.

- [DevOps Trends and Best Practices to Watch in 2022](https://technostacks.com/blog/devops-trends)

    This post covers the DevOps trends to watch in 2022, including microservices architecture, adoption of DevSecOps, going completely serverless, resiliency testing going mainstream, GitOps becoming the new normal, and the evolution of Chaos Engineering, among others.

- [Distributed Timed Task Scheduling Framework Practice](https://mp.weixin.qq.com/s/9gBY_QHyBrzSoMlBG83zug)

    This page introduces the demand background and pain points of the task scheduling framework, explores and practices the open source scheduling frameworks commonly used in the industry, and analyzes their respective advantages and disadvantages.

- [Split the three separate application questions: What, When, How](https://dzone.com/articles/split-the-monolith-what-when-how)

    In the design of microservice architecture, how to split the monomer is a very important thing but a headache for architects. This post presents some ideas and steps on how to prepare and run monolithic application splits.

- [K8s Security Policy Best Practices](https://mp.weixin.qq.com/s/ZDqchROixZT4enVYH6UIfw)

    The article begins with an introduction to the security risks faced by the K8s environment and the security mechanisms provided by K8s. In addition, the author summarizes the best practices for improving the K8s security situation based on the production practices of the community and his own team.

- [Prometheus Monitoring Harbor Actual Combat](https://blog.51cto.com/u_15331726/5177735)

    Harbor v2.2 and later versions support the collection and use of related metrics. This page introduces how to use Prometheus to easily capture some key metrics of Harbor instances.

### Tool recommendation

- [Kubernetes Exploration for Solving Noisy Neighbor Use Cases](https://mp.weixin.qq.com/s/g28ett0Z5LR0sHTyOljCRg)

    The noisy neighbor problem occurs when one tenant's performance degrades due to another tenant's activity.
    While Kubernetes provides a CPU manager, device plug-in manager, and topology manager to coordinate resource allocation and ensure optimal performance of critical workloads, it does not fundamentally address the problem.
    In response, Intel Resource Provisioning Technology RDT supports limiting access to shared resources for non-critical workloads by configuring the appropriate RDT classes for each of the three Kubernetes QoS levels.

- [How to Play with Application Resourcing in the FinOps Era](https://mp.weixin.qq.com/s/2ulduH_zKKcCsB64sVI0bg)

    Kubernetes schedules applications according to the resource quotas they request, so how to properly configure application resource specifications becomes the key to improving cluster utilization.
    The article shares how to properly configure application resources based on the FinOps open source project Crane, and how to promote resource optimization practices in the enterprise.

- [A new way to help Go teams use OpenTelemetry](https://gethelios.dev/blog/helping-go-teams-implement-opentelemetry-a-new-approach/)

    Implementing OTel with Go to send data to an observation platform is not simple, and Go instrumentation requires a lot of manual work.
    The Helios team has developed a [new OTel Go instrumentation method](https://app.gethelios.dev/get-started) that combines a Go AST and a proxy library that is easy to implement and maintain.
    At the same time, the approach is non-intrusive and easy to understand for end users.

- [Why is the experience of debugging applications in Kubernetes so bad?](https://mp.weixin.qq.com/s/maI6Nu6r431LtGzrgq_6rg)

    For developers, what they want is: a fast internal development loop where they can use familiar IDE tools to do local debugging; find bugs in advance to avoid entering Outer Loop prematurely; and collaboration between teams in an internal environment where they can not interfere with each other.
    To solve the above pain points, the article introduces three tools: Kubernetes local development tool [Telepresence](https://github.com/telepresenceio/telepresence), cloud native collaborative development and testing solution [KT-Connect](https://github.com/alibaba/kt-connect) and the IDE-based cloud native application development tool [Nocalhost](https://github.com/nocalhost/nocalhost).

- [Building an End-to-End Non-Intrusive Open Source Observable Solution on K8s](https://mp.weixin.qq.com/s/HUFawiyv55Hi0aEoEPl6rA)

    [Odigos](https://github.com/keyval-dev/odigos) is an open source observability control plane that allows organizations to create observability pipelines in minutes, integrating numerous third-party projects, open standards, and reducing the complexity of multiple observability software platforms and open source software solutions.
    It also allows applications to provide tracking, metrics and logs in minutes, importantly without any code changes and completely non-intrusive.
    Odigos is able to automatically detect the programming language of each application in the cluster and perform automatic detection.

- [Automating Istio CA Rotation at Scale in Production](https://mp.weixin.qq.com/s/75paqvd507_ExHHGszB_-Q)

    The article shows how to configure Istio to automatically reload its CAs, and how to configure cert-manager to automatically rotate Istio's intermediate CAs periodically before they expire to improve operational efficiency in managing CAs across multiple clusters.

- [Why do we advocate a workload-centric development model instead of an infrastructure-centric development model?](https://score.dev/blog/workload-centric-over-infrastructure-centric-development)

    Cloud native developers are often plagued by configuration inconsistencies between environments.
    [Score](https://github.com/score-spec/spec) is an open source project that provides a developer-centric, platform-independent workload specification,
    Being able to declaratively describe its runtime requirements eliminates configuration inconsistencies between local and remote environments and increases developer productivity.

- [Use Bindle to easily store and distribute cloud native applications](https://mp.weixin.qq.com/s/gGp_CneC8BzU3GKOKIfbWA)

    [Bindle](https://github.com/deislabs/bindle) is an open source package manager commonly used to store and distribute WebAssembly applications and binaries.
    Bindle can package multiple different microservices in one big application and deploy it wherever needed, or it can store applications containing dozens of different binaries.

- [Kubernetes cross-cluster traffic scheduling practice](https://mp.weixin.qq.com/s/RF--gLZtJlT0ijaPp1ZP7A)

    The article demonstrates how the Kubernetes north-south traffic management solution [FSM](https://github.com/flomesh-io/fsm) implements cross-cluster traffic scheduling and load balancing of services, as well as three different global traffic strategies Realization: Only local cluster scheduling, failover, and global load balancing.

- [ChaosBlade: A Sharp Tool for Large-Scale Kubernetes Cluster Fault Injection](https://mp.weixin.qq.com/s/gh4GVnOY_QVU2D2VeyWCeA)

    [ChaosBlade](https://github.com/chaosblade-io/chaosblade) is an experimental injection tool that follows the principles of chaos engineering and the chaos experimental model. Or provide business continuity guarantee during the process of migrating to cloud native.
    The article mainly introduces the underlying implementation principle of ChaosBlade fault injection in Kubernetes, the version optimization process, and large-scale application drill testing.

- [How OpenFeature and Feature Flag Standardization Leads to High Quality Continuous Delivery](https://www.dynatrace.com/news/blog/openfeature-and-feature-flag-standardization/)

    Feature Flag is a feature switch or feature release control, which is a technology that configures switch features without redeploying code.
    And [OpenFeature](https://github.com/open-feature) is an open standard on Feature Flag, which aims to use cloud native technology to build a powerful Feature Flag ecosystem, allowing the team to flexibly choose to meet current needs feature flag method and switch to other methods when requirements change.

- [Traffic Director: TLS Routing Using Envoy Gateway Proxy on GKE](https://cloud.google.com/blog/products/networking/tls-routing-using-envoy-gateway-proxy-on-gke)

    Traffic Director is a Google-hosted service mesh control plane for addressing the governance of microservice traffic.
    The article shares a sample architecture. On the GKE cluster, use Traffic Director to configure the Envoy gateway proxy, and use TLS routing rules to route client traffic outside the cluster to workloads deployed on the cluster.
    In addition, it demonstrates how to use the Envoy proxy as an ingress gateway to enable north-south traffic into the service mesh, and use the [Service Routing API](https://cloud.google.com/traffic-director/docs/service-routing-overview#:~:text=The%20service%20routing%20APIs%20let,two%20HTTPRoute%20resources%20configure%20routing.) to route these traffic, and finally shared some troubleshooting tips.

- [How is the Java framework of Quarkus used for serverless feature development?](https://mp.weixin.qq.com/s/oeJjQtqK8h2JSGy4wOlQ6w)

    [Quarkus](https://github.com/quarkusio/quarkus) solves the problem of large memory consumption of traditional frameworks and the expansion of container environments.
    With Quarkus, developers can build cloud native microservices and serverless features using familiar technologies.
    Articles explaining how to get started with Quarkus develops serverless features, how to optimize features and achieve continuous testing, and make portable features across serverless platforms, etc.

- [GitLab + Jenkins + Harbor Toolchain Quick Landing Guide](https://mp.weixin.qq.com/s/fA38H5up9VqZ3zEBy1eXnA)

    This page describes how to quickly deploy a DevOps toolchain (GitLab + Jenkins + Harbor) using the DevOps toolchain manager [DevStream](https://github.com/devstream-io/devstream).

- [Helm deploys highly available Harbor container registry](https://mp.weixin.qq.com/s/ev_QE9NhwiCcLHpapbAU7A)

    This page introduces how to use the Helm package management tool to deploy harbor in a kubernetes cluster and achieve high availability.

- [Microsoft Azure's Open Source Practices in Container Supply Chain Security](https://mp.weixin.qq.com/s/bXt-pPID4CyDyp0XEmDyZQ)

    This page mainly introduces Azure's open source practices in the field of container supply chain security.
    For example: [Microsoft/SBOM Tool](https://github.com/microsoft/sbom-tool) generates SBOM files, [Notary v2](https://github.com/notaryproject/notation) generates software products such as container images Sign and verify, [ORAS](https://github.com/oras-project/oras) extends OCI to enable supply chain security, [Ratify](https://github.com/deislabs/ratify) helps Kubernetes verification Application deployment security.

- [vcluster -- multi-tenant solution based on virtual cluster](https://mp.weixin.qq.com/s/831cv8ONpzcJ3FJeyQ3sxQ)

    A virtual cluster, or vcluster, is a fully functional, lightweight, and well-isolated Kubernetes cluster running on top of a regular Kubernetes cluster.
    The core idea is to provide an isolated Kubernetes control plane (such as an API Server) running on top of a "real" cluster.
    Compared with a completely independent "real" cluster, a virtual cluster does not have its own working nodes or network, and the workload is actually scheduled on the underlying host cluster.

- [5 practical tools to improve Kubernetes productivity](https://mp.weixin.qq.com/s/KAg48nzlsL2jxm0sUDo3mw)

    The article lists five powerful tools for working with Kubernetes,
    They are the terminal UI [K9s](https://github.com/derailed/k9s), the tool to clean up the Kubernetes cluster [Popeye](https://github.com/derailed/popeye), the Kubernetes cluster deployment inspection tool [Kube -bench](https://github.com/aquasecurity/kube-bench), context and namespace quick switching tool [Kubectx](https://github.com/ahmetb/kubectx), [Kubens](https:/ /github.com/ahmetb/kubectx) and [fzf](https://github.com/junegunn/fzf), log aggregator [Stern](https://github.com/stern/stern), fast from shell Check the file [Bat](https://github.com/sharkdp/bat).

- [Use Open Cluster Management (OCM) Placement to extend multicluster scheduling capabilities](https://cloud.redhat.com/blog/extending-the-multicluster-scheduling-capabilities-with-open-cluster-management-placement)

    In the K8s multicluster management project OCM, the multicluster scheduling capability is provided by the [Placement](https://github.com/open-cluster-management-io/placement) controller.
    Placement provides some default prioritizers for sorting and selecting the most suitable clusters. In some cases, the sorter needs more data to calculate the score of the cluster.
    Therefore, we need a scalable way to support scheduling based on custom scores.

- [HummerRisk, an open source cloud native security governance platform](https://mp.weixin.qq.com/s/00cER0lVP2u40GROPP_ZbA)

    [HummerRisk](https://github.com/HummerRisk/HummerRisk) is an open source cloud security governance platform that conducts comprehensive security inspections on cloud native environments in a non-intrusive manner, and solves three core problems. Cloud security compliance, middle-level K8s container cloud security and upper-level software security.

- [GitOps deployment of OCI artifacts and Helm charts with Config Sync](https://cloud.google.com/blog/products/containers-kubernetes/gitops-with-oci-artifacts-and-config-sync)

    [Config Sync](https://github.com/GoogleContainerTools/kpt-config-sync) is an open source tool that provides GitOps continuous delivery for Kubernetes clusters.
    It can store and deploy Kubernetes manifests through GitOps, package Kubernetes manifests into a container image, and use the same authentication and authorization mechanism as container images.

- [Breakthrough Kubernetes' limitation on the number of custom resources](https://mp.weixin.qq.com/s/LV83vuMZ641HzL7bKUE05g)

    The Crossplane community discovered the upper limit of CRDs that Kubernetes could handle and helped fix them.
    Reasons for the limitation include: restrictive client-side rate limiters, slow client-side caching, inefficient OpenAPI schema calculations, high cost of redundancy, etcd clients.

- [K8s DevOps Platform TAP Knative-based Cloud Native Runtime](https://mp.weixin.qq.com/s/kvUDvEVaNC3qordCtaMosw)

    The core of TAP's cloud native application runtime abstraction layer (CNR) is Knative.
    TAP provides a Runtime runtime layer, which not only supports users to use K8S Deployment and Service, but also Knative Serving, Scale From/To Zero, Eventing and Streaming, etc.

- [Using Tekton and Kyverno's Policy-Based Approach to Secure CI/CD Pipelines](https://www.cncf.io/blog/2022/09/14/protect-the-pipe-secure-ci-cd-pipelines-with-a-policy-based-approach-using-tekton-and-kyverno/)

    [Tekton](https://github.com/tektoncd/pipeline) provides a robust CI/CD framework with extensions such as Tekton Chains to secure build artifacts.
    [Kyverno](https://github.com/kyverno/kyverno) can be used to manage policies, implement namespace-based isolation, and generate secure resources for Tekton pipelines.
    Additionally, OCI artifacts such as Tekton bundles can be signed. The powerful combination of Tekton and Kyverno enables new levels of security and automation for software build and delivery systems.

- [K8S Operation and Maintenance Development and Debugging Artifact Telepresence Practice Guide](https://mp.weixin.qq.com/s/Yu5z9w26rqgVHkEYhg1t2g)

    [Telepresence](https://github.com/telepresenceio/telepresence) can be used to run a single service locally while connecting that service to a remote Kubernetes cluster.
    Telepresence provides three very important features: cluster domain name resolution, cluster traffic proxy and cluster traffic interception.

- [Use Containerlab + kind to quickly deploy Cilium BGP environment](https://mp.weixin.qq.com/s/FBkln02REVMByhdzaZhj7w)

    kind provides the ability to quickly deploy K8s, and [Containerlab](https://github.com/srl-labs/containerlab) provides the ability to quickly deploy network resources. The combination of the two can achieve second-speed deployment of cross-network K8s clusters, which can be used for rapid deployment and destruction Cilium BGP environment.

- [The next step in observability: Trace-based testing](https://thenewstack.io/trace-based-testing-the-next-step-in-observability/)

    Distributed tracing data collected by observability tools is ideal for integration testing.
    Trace-based testing can accurately specify the transaction to be tested, observe the results of system behavior, verify the dependencies between components, and actively test for potential problems.
    [Tracetest](https://github.com/kubeshop/tracetest) is a trace-based testing tool that uses data captured by Opentelemetry distributed tracing to generate powerful integration tests.

- [RunD: High-density and high-concurrency lightweight Serverless secure container runtime](https://mp.weixin.qq.com/s/fgBKqIeuGt2tLcQaYuuyfg)

    Through a full-stack host-to-guest solution, RunD solves the problems of repeated data across containers, high memory usage of each virtual machine, and high overhead of host-side cgroups, and provides support for high-density deployment and high concurrency.
    When running with RunD, it is possible to start more than 200 secure containers in a second, and it is possible to deploy more than 2500 secure containers on a node with 384GB memory.

- [Difficulties in implementing zero trust in Kubernetes and related open source solutions](https://thenewstack.io/introducing-open-source-zero-trust-to-kubernetes/)

    The complexity of Kubernetes makes standardizing the application of Zero Trust principles a challenge. By default, kubectl does not enable RBAC, and executed commands are not logged by user accounts. Accessing resources through firewalls is difficult, and supervising multiple clusters becomes cumbersome and error-prone.
    [Paralus](https://github.com/paralus/paralus) is a resource access management, threat identification and response solution designed for multicluster environments, supports custom roles, identity providers (IdP), etc., allowing administrators to create Custom rules for different permissions.

-[KIntroduction to ubernetes Gateway API and its use cases](https://www.armosec.io/blog/kubernetes-gateway-api/)

    The article describes the difference between Gateway API and Ingress and its use cases. Gateway API is an evolution of Ingress, which extends the API definition to provide some advanced features, such as HTTP and TCP routing, traffic splitting, routing across namespaces, and integrating progressive delivery tools.

- [How to conduct K8s cluster benchmarking - Kube-burner's extended support for KubeVirt CRD introduction](https://cloud.redhat.com/blog/introducing-kubevirts-crd-support-for-kube-burner-to-benchmark-kubernetes-and-openshift-creation-of-vms)

    [Kube-burner](https://github.com/cloud-bulldozer/kube-burner) is a tool for Kubernetes cluster pressure measurement by creating or deleting a large number of objects.
    kube-burner does not support third-party plugins such as KubeVirt CRD by default.
    Therefore, Openshift extends kube-burner to support KubeVirt CRD for cluster benchmarking by creating/deleting virtual machines.

- [Enhancing GitOps Security with Sops in Argo CD](https://mp.weixin.qq.com/s/GboGFpdAfF1SL150VSRn8Q)

    [Sops](https://github.com/mozilla/sops) is an encrypted file editor that supports YAML, JSON, ENV and other formats, and can be encrypted with AWS KMS, GCP KMS, age and PGP.
    Argo CD can be integrated with Sops to encrypt and decrypt private information.

- [How to use KubeClarity to detect and manage software BOM and container image and file system vulnerabilities](https://mp.weixin.qq.com/s/mw948wYKmTWt-Mxv4nxHRA)

    [KubeClarity](https://github.com/openclarity/kubeclarity) is a tool specially designed to detect and manage software bills of materials, container images and file system vulnerabilities. It can scan runtime K8s clusters and CI/CD pipelines, To enhance the security of the software supply chain.

- [How to do a canary release for Helm? ](https://mp.weixin.qq.com/s/frOOSffcCknS_YAjQChuNg)

    Helm itself does not consider gray-scale release and does not manage workloads when it is designed.
    Through [KubeVela's plug-in mechanism](https://github.com/kubevela/catalog/tree/master/addons) combined with fluxcd addon and kruise-rollout addon, Helm application can be easily completed without any changes to Helm Chart Canary releases.

- [Using Nocalhost to develop microservice applications on Rainbond](https://mp.weixin.qq.com/s/kC9P7fvMtJvKK7_TM2LbTw)

    [Nocalhost](https://github.com/nocalhost/nocalhost) is an IDE-based cloud native application development tool, and [Rainbond](https://github.com/goodrain/rainbond) is a cloud native multicloud application management tool platform.
    Nocalhost can directly develop applications in Kubernetes. Rainbond can quickly deploy microservice projects without writing Yaml. Nocalhost combines Rainbond to accelerate the efficiency of microservice development.

- [Two OCI image build tool introduction builders - melange and apko](https://blog.chainguard.dev/secure-your-software-factory-with-melange-and-apko/)

    [apk](https://github.com/alpinelinux/apk-tools) directly uses Alpine's package management tool APK to build images, no need to use Dockerfile, only need to provide a declarative YAML manifest.
    [melange](https://github.com/chainguard-dev/melange) uses a declarative YAML pipeline to build APKs.

- [Application continuous delivery practice based on Flux v2 in multicluster use cases](https://mp.weixin.qq.com/s/a9lRoa36tFl1_1-ESvXJpA)

    [Flux v2](https://github.com/fluxcd/flux2) provides a set of tools that can support the implementation of GitOps, and provides a general solution for the continuous delivery of cloud native applications.
    This page mainly starts from deploying cloud native applications with differentiated configurations in multicluster use cases, and introduces the practice of continuous app delivery based on Flux v2.

- [Use Chain-bench to Audit Your Software Supply Chain for CIS Compliance](https://blog.aquasec.com/cis-software-supply-chain-compliance)

    The Center for Internet Security (CIS) recently published [Software Supply Chain Security Guide](https://github.com/aquasecurity/chain-bench/blob/main/docs/CIS-Software-Supply-Chain-Security-Guide-v1.0.pdf), provides best practices for securing software delivery pipelines.
    As the initiator and main contributor of the guide, the Aqua team has developed the first open source tool for software supply chain auditing - [Chain-bench](https://github.com/aquasecurity/chain-bench) to audit software supply Whether the chain meets the benchmark of CIS and realizes the automation of the audit process.

- [Chainguard version of next generation Distroless images](https://blog.chainguard.dev/minimal-container-images-towards-a-more-secure-future/)

    Chainguard is building the next generation of [distroless](https://github.com/distroless) images, using a single toolchain to easily compose distroless images from existing packages and create custom packages.
    Unlike Google's Bazel and Debian-based systems, the Chainguard toolchain starts with [apk](https://github.com/alpinelinux/apk-tools) (Alpine package manager), [apko](https://github.com/chainguard-dev/apko) (used to build distroless images based on Alpine) and [melange](https://github.com/chainguard-dev/melange) (use declarative pipeline to build apk packages) as core, reducing the complexity of distroless images.

- [Enable support for LoadBalancer type service on OpenYurt edge side through MetalLB](https://openyurt.io/blog/Enable-MetalLB-in-OpenYurt/)

    In the cloud edge collaboration scenario, since the edge side does not have the cloud SLB service capability, edge Ingress or edge applications cannot expose LoadBalancer-type services for access outside the cluster.
    In this scenario, This page discusses how to implement support for LoadBalancer type service on the edge side of OpenYurt through MetalLB.

- [Implementing Hot Reloading in Kubernetes](https://loft.sh/blog/implementing-hot-reloading-in-kubernetes/?utm_medium=reader&utm_source=rss&utm_campaign=blog_implementing-hot-reloading-in-kubernetes?utm_source=thenewstack&utm_medium=website)

    If you want to test applications directly in the cluster while developing Kubernetes applications, there are quite a few steps involved.
    The article introduces the significance of hot reloading inside Kubernetes, and how to use [DevSpace](https://github.com/loft-sh/devspace) to efficiently complete hot reloading - DevSpace is responsible for automatically rebuilding and redeploying applications, Users only need to save the application files.

- [Detect and fix performance issues with Tracetest](https://kubeshop.io/blog/detect-fix-performance-issues-using-tracetest?utm_source=thenewstack&utm_medium=website)

    [Tracetest](https://github.com/kubeshop/tracetest) is an end-to-end testing tool based on OpenTelemetry Traces.
    Tracetest can find anomalies in code before users or developers encounter bugs.

- [Introduction to OPAL: Real-time Dynamic Authorization](https://www.cncf.io/blog/2022/06/27/real-time-dynamic-authorization-an-introduction-to-opal/)

    [OPAL](https://github.com/permitio/opal) is a management layer of the Open Policy Agent (OPA), which keeps the authorization layer up-to-date. OPAL detects changes in policy and policy data and pushes real-time updates to agents. As the state of the application changes, OPAL will ensure that the service is always in sync with the required authorization data and policies.

- [Nightingale - Enterprise version of Prometheus](https://mp.weixin.qq.com/s/OXmnH9KsygpB70-NmwxM1w)

    [Nightingale](https://github.com/ccfos/nightingale) is an open source cloud native monitoring and analysis system, adopting the All-In-One design, integrating data collection, visualization, monitoring and alerting, and data analysis. The cloud native ecosystem provides out-of-the-box enterprise-level monitoring, analysis and alert capabilities.
    The article mainly introduces how Nightingale correlates the three observability metrics, operation and maintenance quantification, alert noise processing, product positioning, and AIOps applications, etc.

- [Porting eBPF applications to BumbleBee - the easiest way to develop BPF CO-RE programs](https://www.solo.io/blog/porting-ebpf-applications-to-bumblebee/)

    BPF CO-RE (Compile Once - Run Everywhere) aims to solve the problem of eBPF program portability.
    The article details how to port a BPF CO-RE libbpf script to [Bumblebee](https://github.com/solo-io/bumblebee) to solve userSpace, distribution and integration challenges.

- [One-click Kubernetes observability — how to automatically generate and store OpenTelemetry traces](https://mp.weixin.qq.com/s/98tqrwgXviUIe0nRAMgzPw)

    [Tobs](https://github.com/timescale/tobs) is an observability technology stack for Kubernetes, which can deploy a complete observability technology stack in a Kubernetes cluster in minutes.
    The stack includes OpenTelemetry Operator, OpenTelemetry Collector, Promscale, and Grafana. It also deploys several other tools, such as Prometheus, to collect metrics from Kubernetes clusters and send them to Promscale.
    Tobs supports Python, Java and Node.js services auto-instrumented with OpenTelemetry trace via the OpenTelemetry Operator.

- [Categraf: Introduction to Nightingale Monitoring Default Data Collection Agent](https://mp.weixin.qq.com/s/Qt0YbhPE6WSvoZZmuCLjyw)

    Categraf is the default data collection agent of Nightingale Monitoring. It is mainly out-of-the-box and all-in-one, and supports the collection of metrics, logs, and traces.
    The article first compares the similarities and differences between categraf and telegraf, exporters, grafana-agent, datadog-agent, and then introduces the security, testing and configuration of catagraf.

- [Crane-scheduler: Scheduling based on real load](https://mp.weixin.qq.com/s/s0usEAA3pFemER97HS5G-Q)

    The native Kubernetes scheduler can only schedule based on the resource request of the resource. However, the actual resource usage of the Pod is often very different from the request/limit of the requested resource.
    Crane-scheduler is a scheduling plug-in of the cost-optimized open source project Crane, which realizes the scheduling feature based on real load, acts on the Filter and Score stages in the scheduling process, and provides a flexible scheduling policy configuration method, thereby effectively alleviating the kubernetes cluster The problem of uneven load of various resources in the network.

- [How to use Multus CNI to use Kubernetes services on secondary networks](https://cloud.redhat.com/blog/how-to-use-kubernetes-services-on-secondary-networks-with-multus-cni)

    The article describes how the OpenShift 4.10 developer preview leverages Multus CNI to use Kubernetes services on the secondary network, achieving functional parity with the Kubernetes secondary network.

- [Use vmagent instead of Prometheus to collect monitoring metrics](https://mp.weixin.qq.com/s/jGf1L-8c8id8umB72b3AsQ)

    vmagent is a component in the open source time series database VictoriaMetrics (VM), which helps us collect metrics from various sources and store them in VM or any other Prometheus-compatible storage system that supports the remote write protocol.
    vmagent can implement many features of Prometheus, but index capture is more flexible, supports pulling and pushing metrics, and uses less memory, CPU, disk I/O, and network bandwidth.

- [In-depth Interpretation: Distributed System Resilience Architecture Ballast Stone OpenChaos](https://mp.weixin.qq.com/s/x-aRajL_ThKgVpOwV5GgXA)

    [OpenChaos](https://github.com/openmessaging/openchaos) is an emerging chaos engineering tool created by the RocketMQ team for the resilience of distributed systems.
    OpenChaos sets up a dedicated detection model for the unique properties of some distributed systems, such as the delivery semantics and push efficiency of the Pub/Sub system, the precise scheduling, elastic scaling and cold start efficiency of the scheduling system, and the real-time performance of the streaming system.
    At the same time, it has built-in scalable model support to verify the resilience performance under the impact of large-scale data requests and various failures, and provide optimization suggestions for architecture evolution.

- [Kubernetes will heavily adopt Sigstore to protect the open source ecosystem](https://www.infoq.cn/article/pXTp33YPCH2LYkQw3HRv)

    Launched last year, Sigstore is a free signing service for software developers that improves the security of the software supply chain through encrypted software signing powered by transparent logging technology.
    Kubernetes 1.24 and all future releases use Sigstore to sign artifacts and verify signatures.

- [Kubernetes Node Elastic Scaling Open Source Component Amazon Karpenter Practice: Deploying GPU Inference Applications](https://mp.weixin.qq.com/s/DcP9vQGGldCFRNs9odpFJg)

    Karpenter is an open source component released by Amazon for elastic scaling of Kubernetes cluster nodes.
    This component can automatically create appropriate new nodes and join them in the cluster according to the needs of Unscheduleable Pods.
    Karpenter completely abandons the concept of node groups and uses EC2 Fleet API to directly manage nodes.
    This page takes the GPU inference scenario as an example to elaborate on the working principle, configuration process and test results of Karpenter.

- [Kruise Rollout: Enabling Progressive Delivery for All Application Loads](https://mp.weixin.qq.com/s/m-r3AQMbv2IPoAAJMhReZg)

    [Kruise Rollout](https://github.com/openkruise/rollouts) is the definition model of OpenKruise (Alibaba Cloud's open-source cloud native application automation management suite) for progressive delivery abstraction, aiming to solve traffic scheduling in the field of app delivery and Batch deployment problem.
    It can cooperate with application traffic and canary release, blue-green release, etc. of actual deployment instances, and the release process can be automated in batches and pauses based on Prometheus Metrics, compatible with various workloads, etc.

- [Prometheus long-term remote storage solution VictoriaMetrics entry practice](https://mp.weixin.qq.com/s/C3fzohygl5_tey70Qnz3og)

    VictoriaMetrics (referred to as VM) is a highly available, cost-effective and scalable open source monitoring solution and time series database, which can be used for long-term remote storage of Prometheus monitoring data.
    In addition, the main features of the VM include: external support for Prometheus-related APIs, high performance and good scalability for index data ingestion and query, and high-performance data compression methods.

- [Tools to manage Helm versions declaratively](https://helm.sh/blog/tools-to-manage-helm-declaratively/)

    This post introduces some tools in the Kubernetes ecosystem that can be used to declaratively manage Helm versions (such as the CNCF projects Flux and Argo), and compares these tools.

- [Cost Governance of Cloud Native Workloads Using Kubecost and Kyverno](https://dzone.com/articles/cost-governance-of-cloud-native-workloads-using-kubecost-and-kyverno)

    This page describes how to use the policy engine Kyverno and the cost management tool Kubecost to perform cost governance on cloud native workloads. When the cost of a certain Kubernetes workload calculated by Kubecost is higher than the assigned value, Kyverno will create a violation/failure.

- [Dubbo-go-Mesh opens a new generation of Go microservices](https://mp.weixin.qq.com/s/cSsnne_kGfUjm1lKZWLiOw)

    Dubbo-go-Mesh is a cross-ecological service framework implementation scheme of the distributed RPC framework Dubbo-go in the agentless service mesh scenario. Currently, Istio-compatible service governance capabilities are supported. It supports interface-level service discovery capabilities, is compatible with the flow control and management capabilities of the Istio ecosystem, and provides scaffolding and application templates to improve the efficiency of Go application development.

- [How to bring your own scheduler into OpenShift with the secondary scheduler](https://cloud.redhat.com/blog/how-to-bring-your-own-scheduler-into-openshift-with-the-secondary-scheduler-operator)

    Kubernetes Scheduler cannot meet the special needs of some applications for schedulers: such as common scheduling, topology-aware scheduling, load-aware scheduling, etc.
    As a result, OpenShift allows users to introduce their own customized scheduler through the [Secondary Scheduler](https://github.com/openshift/secondary-scheduler-operator) of the application market Operator Hub, and use this scheduler to run the scheduler they choose workload.
    Instead, the control plane components still use the default scheduler provided by OpenShift.

- [God's perspective of observability brought by eBPF technology: Introduction to Kindling open source project](https://mp.weixin.qq.com/s/nIqFnIbjrPsrjtxSLQp3gg)

    In the actual implementation process of distributed tracking technology, it often faces pain points such as manual probe automation coverage, difficulty in covering multilingual services, and lack of kernel observable data in APM trace.
    And Kindling's God's perspective based on eBPF technology brings a solution - the trace associated with the kernel's observable data.

- [Virtual Kubernetes Clusters: New Model Multitenancy](https://opensource.com/article/22/3/virtual-kubernetes-clusters-new-model-multitenancy)

    For a long time, the two multi-tenancy models based on namespace and cluster have many disadvantages.
    This page introduces a newer concept - virtual clusters. It combines the advantages of the two multi-tenancy approaches described above: multi-tenancy uses only one namespace, and tenants have full control within the virtual cluster.

### Product comparison

- [Kubernetes Policy Engines: OPA vs. Kyverno vs. jsPolicy](https://mp.weixin.qq.com/s/bMPraw5Q8-DZqCoJLJe2jQ)

    The article discusses the concept of a Kubernetes policy engine and compares three different Kubernetes policy engines: OPA, Kyverno, and jsPolicy.
    The conclusion is that jsPolicy is recommended for those who want a more straightforward and simple approach, or are proficient in JavaScript and TypeScript.
    If YAML is more preferred and you want to continue using Kubernetes resources directly, Kyverno is a good choice.

- [Comparison of 12 open source monitoring tools that have been open sourced in the past two decades](https://mp.weixin.qq.com/s/ByQ3skUrcf1c_DPD4dCbRg)

    The article briefly introduces and analyzes 12 typical open source monitoring tools, and points out their respective advantages and disadvantages.
    The tools mentioned include the distributed monitoring system Zabbix, the time series database VictoriaMetrics, Prometheus, the cloud native monitoring and analysis system Nightingale Monitoring, etc.

- [Discussion on the selection and application of cloud native storage tools](https://mp.weixin.qq.com/s/QoVlOe01hGWSYEKS8wfsKw)

    The article sorts out the concept of cloud native storage step by step, and briefly introduces and compares Longhorn, OpenEBS, Rook+Ceph, and finally chooses a representative Longhorn to demonstrate its installation and use.

- [Discussion on K8s CNI plug-in selection and use cases](https://mp.weixin.qq.com/s/GG7GX_E1oyZf-cmjk80OYg)

    This page introduces seven common network use cases in the container environment and the implementation of the Kubernetes CNI plug-in feature for the corresponding use cases.

- [The Way of DevOps Platform Design in the Cloud Native Era (Rancher vs KubeSphere vs Rainbond)](https://mp.weixin.qq.com/s/oxeNq4GHE85NUBIDcgixcg)

    The article focuses on the different DevOps implementations of Rancher, KubeSphere, and Rainbond, three cloud native platform-level products.
    The author believes that DevOps teams can choose the combination of Rancher + KubeSphere or Rancher + Rainbond.
    Rancher is best at docking infrastructure downwards, managing cluster security and compliance, and providing developers with an easy-to-use cloud native platform upwards is handed over to KubeSphere or Rainbond.

-[Who is stronger? Grafana Mimir and VictoriaMetrics performance test](https://mp.weixin.qq.com/s/TVJZ5k5U7bs8WEyE4rikSQ)

    The article compares the performance and resource usage of VictoriaMetrics and Grafana Mimir clusters for workloads running on the same hardware.
    In benchmarks, VictoriaMetrics exhibits higher resource efficiency and performance compared to Mimir. In terms of operation, the extension of VictoriaMetrics is more complex, and Mimir can easily implement component extensions.

- [Understand Prometheus's long-term storage mainstream solution in one article](https://mp.weixin.qq.com/s/1BF83kIF_AGVD9J2qLnlSA)

    Because Prometheus has limitations such as cross-cluster aggregation and long-term storage, the community has proposed various expansion solutions.
    The article conducts a multi-dimensional comparative analysis of five mainstream Prometheus long-term storage solutions including M3, VictoriaMetrics, Thanos, Cortex, and Grafana Mimir.

- [Technical selection of eBPF infrastructure library](https://mp.weixin.qq.com/s/4WNyNwkRW2lZ82nMOP6rMA)

    The article compares several eBPF infrastructure libraries, such as libbcc, dropbox's goebpf, Cilium's ebpf library, Calico's underlying library, falco's lib library,
    And explain why open source observability tool Kindling chose falco-libs.

- [How to choose a reliable APM system in a production environment](https://mp.weixin.qq.com/s/3dD0hIuqpXdepLVC6V7aoA)

    The article starts from the introduction of mainstream APM products (compared with Pinpoint, Jaeger, Skywalking, Tingyun, Tencent Cloud + Alibaba Cloud Arms and Datadog), and passes through several important dimensions in the production environment, such as product experience, Agent capability, alert + DB support, cloud native support capabilities, large data screens, etc., and give suggestions for APM selection solutions.

### Frontier hotspot

- [The first domestic experience of landing a community dual-stack Istio solution, the implementation code is open source](https://mp.weixin.qq.com/s/E9HZIkSbZ3BLetDL0ZhzvA)

    In the industry's widely used service mesh projects (Istio and Linkerd as examples), support for dual-stack technology is still missing.
    In order to better implement service mesh and Kubernetes in the dual-stack support to work together.
    The article focuses on the implementation scheme of Istio in dual-stack technology and the implementation scenario of this scheme in mobile cloud landing.
    However, this solution is only [an experimental branch](https://github.com/istio/istio/tree/experimental-dual-stack) and does not refine unit and integration tests.

- [Where to Go After Microservices Enter Deep Water](https://mp.weixin.qq.com/s/yBY-E-tndUJCmA4KYRfrDw)

    As microservices enter deep water, developers and architects are more concerned about microservice security, stability, cost optimization, standardization of microservice governance, and driving the gradual evolution of cloud native microservice architectures to multi-runtime microservice architectures.
    For the limitations of multi-runtime architecture, it is necessary to realize more standardized and platform-based service mesh development and operation and maintenance capabilities, standardize the definition of Sidecar and runtime, and make the operation and maintenance platform more standard and easy to use.

- [Predictions for cloud native trends in 2023](https://mp.weixin.qq.com/s/QePkownt0_Ex9RWWeGtaag)

    The article is CNCF CTO Chris Aniszczyk's predictions on the hot topics in cloud native and technology in 2023.
    These include: cloud native IDEs becoming the norm, FinOps becoming mainstream and moving left, open source SBOMs becoming ubiquitous, GitOps maturing and entering substantial peak production, OpenTelemetry maturing, Backstage developer portal continuing to improve, WebAssembly entering a steady climb, and more.

- [Exploring Tunnel-based Kubernetes Cross-Cluster Communication](https://mp.weixin.qq.com/s/uuWCr1d7V_aFdCAJCJS_XQ)

    The article describes cross-cluster access access based on ssh tunnels.
    A service in cluster A wants to access different services in cluster B, i.e., a single tunnel with multiple services is implemented by adding a proxy for the tunnel at both ends of the tunnel, and the left end of the tunnel listens to multiple ports to distinguish different services in cluster B that the service in cluster A wants to access.
    This information is communicated to the proxy on the right end of the tunnel, which forwards the information to the corresponding services in cluster B.
    This solution is currently only at the demo level.

- [Six Trends for eBPF in 2023](https://www.solo.io/blog/ebpf-trends-2023/)

    The six trends for eBPF in 2023 include
    Building high-performance HTTP monitoring with eBPF network tracing, deeper network functionality and sidecar optimization, security and malware detection, large-scale adoption of cloud platforms, adoption in the telecom space, and the emergence of more eBPF-based projects.

- [Kubernetes pain, platform engineering can solve](https://thenewstack.io/kubernetes-pains-platform-engineering-can-help/)

    The product approach needed to build platform engineering helps organizations understand areas of Kubernetes for which support is not yet available. Developer self-service allows engineers to provision and use the technologies needed to test, protect, and deploy applications on their own, without waiting for operations to provide resources or launch environments. The in-house development platform allows development and operations to focus on their respective core responsibilities and strengths, with developers focusing on writing code and operations moving upstream to more critical tasks, such as managing the network or physical hardware.

- [How does the Information technology application innovation industry bring value to the business?](https://mp.weixin.qq.com/s/uDe1wb0cVsqrz7oXjYOXXg)

    When it comes to Information technology application innovation industry, the first thought is autonomous and controllable. But to do a good job of Sentry, you need to take some energy out of burying your head in autonomous controllability and think about how to get value from Sentry. The article introduces successful cases of technology replacement at home and abroad, under what circumstances technology replacement can bring value to the business, and what can be done to make Information technology application innovation industry better for the business.

- [From PingCAP's TiDB database product to see the model of domestic technology going abroad](https://mp.weixin.qq.com/s/3y9pafdEy8rD5H2OtgPwEw)

    The article introduces the technical, compliance, and commercialization optimizations of TiDB made by PingCAP to realize technology going abroad. Technically, to achieve cost reduction and efficiency, operation and maintenance automation, multi-tenant management, and meet the needs of specific regional use cases; compliance, to consider data security and regulatory rules; commercially, to consider billing models, commercialization strategies, etc. In addition, TiDB can attract overseas customers with several factors: TiDB is open source and has an active open source community; customer data is stored on public clouds such as AWS and GCP; remote support, not relying on local technical teams, can effectively solve the problem of expensive human resources in some regions.

- [Explore K8s new feature Container Checkpointing](https://sysdig.com/blog/forensic-container-checkpointing-dfir-kubernetes/)

    The container checkpoint feature (K8s 1.25 alpha) creates a snapshot of a running container's state and saves it to disk.
    You can then use this checkpoint to start the container, restore state, or migrate the container to another machine.
    The article introduces how this feature works, Podman's checkpoint function, CRIU and forensic analysis and other use cases.

- [OCI Container and Wasm First Experience](https://mp.weixin.qq.com/s/4oFErzG65b-0FfpHQB941A)

     This page describes how to configure the OCI runtime to run Linux containers and WASI-compliant workloads.

- [Is Sidecarless the next stop for Service Mesh?](https://mp.weixin.qq.com/s/SF5uN8VHwrqji4xdME4hCg)

    Although several major open source communities such as Cilium, Linkerd, and Istio have carried out their own exploration and practice in the field of sidecarless, each has its own focus on security, stability, management costs, and resource occupation, adapting to different businesses Scenes.

- [eBPF program camera - strive to solve the most valuable and challenging problems in the field of observability in the future](https://mp.weixin.qq.com/s/FYNe1H5dmBpbKFOrIpjuzQ)
  
    Currently, observability users are easily lost in the maze of metrics. They don’t know when to view which metrics, and how to understand large-scale and fine-grained metrics.
    To solve this problem, the Kindling community chose an eBPF-based observability camera to obtain fine-grained metrics during program execution according to the eBPF granularity, helping users understand the real process of program execution and understand how fine-grained metrics affect the program implemented.

- [Is GitOps the emperor's new clothes](https://mp.weixin.qq.com/s/CpLvQM2rTI4InIN1Vk5ZKg)

    Before adopting GitOps, we need to ask ourselves "What is GitOps?" and ask ourselves "Who are we serving with these tools? What problem are we trying to solve?"
    The article questions some of the main "selling points" of GitOps (including security, version control and environment history, rollback, elegant processing, single source of truth, etc.), and introduces some of the challenges that GitOps poses.

- [Ant large-scale platform engineering practice for more than two years, what we have learned](https://mp.weixin.qq.com/s/X8AWh43qp4fb4eJSkx50hw)

    Platform engineering is the discipline of designing and building toolchains and workflows that provide self-service capabilities for software engineering organizations in the cloud native era.
    The article is based on the practice of programmable cloud native protocol stack [KusionStack](https://github.com/KusionStack) in Ant Platform engineering and automation, from platform engineering, special language, divide and conquer, modeling, automation and collaborative culture, etc. From several perspectives, the benefits and challenges in the practice of large-scale platform engineering are explained.

- [Observable and Traceable | Continuous Performance Analysis Continuous Profiling Practice Analysis](https://mp.weixin.qq.com/s/yiwq81ZHB0nSTcYSjOeyZg)

    The significance of continuous performance analysis (CP for short) to developers is that in the production process, they always know all the execution details of the code.
    On the basis of introducing the development history of CP, the article analyzes two key points of performance analysis profiling: obtaining stack data and generating flame graphs, as well as common profiling tools.

- [Design and Implementation of Next Generation Cloud Native Edge Device Management Standard DMI](https://mp.weixin.qq.com/s/T3TnKXhBefqavP4rni59Sg)

    DMI integrates device management interfaces to optimize device management capabilities in edge computing use cases;
    At the same time, a unified connection entry between EdgeCore and Mapper is defined, and EdgeCore and Mapper implement the server and client of the upstream data flow and downstream data flow respectively, and carry the specific features of DMI.

- [Using eBPF LSM to hot fix Linux kernel vulnerabilities](https://mp.weixin.qq.com/s/UJEC8nmfQbdsWdJMfju0ig)

    Linux Security Modules (LSM) is a hook-based framework for implementing security policies and mandatory access control in the Linux kernel.
    The article introduces the implementation idea of eBPF LSM (the core content is to determine the hook point), how to use unshare to map user to root, and how to solve real-world scenario problems by implementing programs in eBPF.
    Finally, the performance impact of this LSM program is compared.

- [Everything you need to know about Cilium Service Mesh](https://isovalent.com/blog/post/cilium-service-mesh/)

    Cilium officially launched Cilium Service Mesh in the latest release [v1.12](https://github.com/cilium/cilium/releases/tag/v1.12.0).
    In Cilium Service Mesh, in addition to a variety of different control planes to choose from, users also have the flexibility to choose a service mesh that runs with or without a sidecar model.

- [Pinpointing Service Mesh Critical Performance Impacts Using eBPF](https://www.tetrate.io/blog/pinpoint-service-mesh-critical-performance-impact-by-using-ebpf/)

    [SkyWalking Rover](https://github.com/apache/skywalking-rover) is the eBPF profiling feature introduced in the SkyWalking ecosystem, which can realize CPU profiling, off-CPU profiling, etc.
    The article discusses how eBPF technology can be used to improve profiling in SkyWalking and to analyze performance impact in a service mesh.

- [coolbpf technology practice, improve the efficiency of BPF program development by a hundred times](https://www.infoq.cn/article/IielSpCwjf6Owd6jMBef)

    [coolbpf](https://github.com/aliyun/coolbpf) is a one-stop BPF development and compilation platform open sourced by the Longli community, aiming to solve the problems of BPF operation and productivity improvement on different system platforms.
    The six major features of coolbpf: local compilation service, basic library encapsulation; remote compilation service; features of high version are supplemented to low version through kernel module; automatic generation of BTF; automatic feature test of each kernel version; Python, Rust, Go, C, etc. Advanced language support.

- [Thinking of the person in charge of Alibaba Cloud Container Service on cloud native and software supply chain security](https://mp.weixin.qq.com/s/jz8sBMeHTSFm8sndHakddw)

    The author of the article introduces the latest practices and tool chains for containerized software supply chain security, including SBOM support for container images, and a new generation of image signature technology - Sigstore's keyless signature Keyless Signatures mode.

- [eBPF, Sidecar and the future of the service mesh](https://buoyant.io/2022/06/07/ebpf-sidecars-and-the-future-of-the-service-mesh/)

    The Linkerd team believes that eBPF service meshes will still require sidecar proxies, at least for the foreseeable future.
    On the one hand, the limitations of eBPF mean that L7 traffic proxies still need userspace network proxies to do their job;
    On the other hand, host-based proxies are inferior in operation, maintenance, and security compared to sidecars.
    In the future, Linkerd will continue to use eBPF technology to make sidecar agents smaller and lighter.

- [Improving security of CNCF projects through fuzzing](https://mp.weixin.qq.com/s/B63juDzcifj_UOCxc8Xo_g)

    Fuzz testing is a technique for testing software by passing "random data" into the target application and seeing if the target application crashes.
    [OSS-Fuzz](https://github.com/google/oss-fuzz) is an open source project that provides continuous fuzzingProvides an automated platform. So far, a total of 18 CNCF projects have been continuously fuzzed through OSS-Fuzz.
    Click for [More details on CNCF fuzzing](https://github.com/cncf/cncf-fuzzing)

- [What is continuous profiling?](https://www.cncf.io/blog/2022/05/31/what-is-continuous-profiling/)

    Continuous profiling is a dynamic method of analyzing the complexity of a program to locate, debug, and fix performance-related problems by understanding the system's resources over a period of time.
    According to the CNCF's CTO, continuous analytics is an integral part of the observability stack.
    The article introduces related concepts, industry trends, and open source continuous performance analysis platforms.
    Click to visit Pyroscope [project address](https://github.com/pyroscope-io/pyroscope)

- [Envoy Gateway plans to provide a standardized Kubernetes ingress](https://thenewstack.io/envoy-gateway-offers-to-standardize-kubernetes-ingress/)

    The Envoy Gateway initiative makes the Envoy reverse proxy a network gateway that not only directs internal microservice traffic, but also manages external traffic entering the network.
    Its fundamental purpose is to establish a standardized and simplified API for Kubernetes.

- [Validating a request workload with WebAssembly](https://www.tetrate.io/blog/validating-a-request-payload-with-wasm/)

    This post describes how to use Wasm plugins to extend Istio - verifying the workload of a request.
    When you need to add custom functionality not supported by Envoy or Istio, you can use Wasm plugins, such as using Wasm plugins to add custom verification, authentication, logging, or manage quotas.

- [OPLG: New Generation Cloud Native Observable Best Practices](https://mp.weixin.qq.com/s/Bf6nmOymcG9bk91VxLL_Kw)

    OPLG refers to the unified display of OpenTelemetry Traces, Prometheus Metrics, and Loki Logs through Grafana Dashboards to meet most use cases of enterprise-level monitoring and analysis.
    Based on the OPLG system, a unified observable platform covering the full stack of cloud native applications can be quickly built to comprehensively monitor infrastructure, containers, middleware, applications, and end-user experience.

- [Four Essential Elements of Kubernetes Software Supply Chain Security](https://www.cncf.io/blog/2022/04/12/a-map-for-kubernetes-supply-chain-security/)

    This post introduces the four elements that a Kubernetes DevOps team needs to understand software supply chain security: Artifacts, Metadata, Attestations, and Policies (A-MAP).
    Software build systems produce artifacts and metadata, and verification of build integrity and software component security attributes requires proofs and policies.

### Security Vulnerabilities

- [Review of 2022 Kubernetes Security Vulnerabilities and What We Can Learn From Them](https://www.armosec.io/blog/kubernetes-vulnerabilities-2022/)

    The article provides a summary of the major security vulnerabilities and solutions for Kubernetes in 2022, such as the CRI-O runtime container escape vulnerability, ArgoCD authentication bypass, and more. Some measures to prevent vulnerabilities are presented: implementing security profiles, following the least privilege principle when assigning roles and permissions, continuous scanning of K8s manifest files, codebases, and clusters, regular updates of packages on clusters, using container sandboxing projects, etc.

- [Istio High Risk Vulnerability: A user with localhost access can impersonate the identity of any workload](https://github.com/istio/istio/security/advisories/GHSA-6c6p-h79f-g6p4)

    If a user has localhost access to the Istiod control plane, they can impersonate any workload identity within the service mesh.
    The affected version is 1.15.2. Currently, the patch version [1.15.3](https://github.com/istio/istio/releases/tag/1.15.3) has been released.

- [Istio high-risk vulnerability: Golang Regex library leads to DoS attack](https://github.com/istio/istio/security/advisories/GHSA-86vr-4wcv-mm9w)

    Istiod has a request processing error vulnerability that allows an attacker to crash the control plane by sending custom or oversized messages when the Kubernetes validating or mutating webhook service is exposed.
    Currently, [Istio](https://github.com/istio/istio/releases) has released patch versions 1.15.2, 1.14.5, and 1.13.9. Versions earlier than 1.14.4, 1.13.8, or 1.12.9 are affected by this.

- [CrowdStrike discovers new cryptojacking attack targeting Docker and Kubernetes infrastructure](https://www.crowdstrike.com/blog/new-kiss-a-dog-cryptojacking-campaign-targets-docker-and-kubernetes/)

    The attack uses container evasion techniques and anonymous mining pools to deliver its workload using an obfuscated domain name to conduct cryptocurrency mining activities against Docker and Kubernetes infrastructure.
    Adopting a cloud security protection platform can effectively protect the cloud environment from similar mining activities, prevent misconfiguration and control plane attacks.

- [Kube-apiserver CVE Vulnerability: Aggregated API server may cause Server Request Forgery (SSRF)](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md#cve-2022-3172-aggregated-api-server-can-cause-clients-to-be-redirected-ssrf)

    An attacker could take control of the aggregated API server, redirecting client traffic to any URL. This could cause the client to perform unexpected actions, or expose the client certificate to a third party.
    There is no mitigation for this issue. Cluster administrators should take care to secure the aggregated API Server and not allow access to mutate API Services by untrusted parties.
    Affected versions: kube-apiserver 1.25.0, 1.24.0 - 1.24.4, 1.23.0 - 1.23.10, 1.22.0 - 1.22.14. Fixed versions: 1.25.1, 1.24.5, 1.23.11, 1.22.14.

- [Aqua discovered a new type of illegal encrypted mining method that can use containers to consume network bandwidth](https://blog.aquasec.com/cryptojacking-cloud-network-bandwidth)

    Recently, Aqua Security issued an alert about a new type of mining attack. Compared with traditional mining attacks, which will cause a sharp increase in CPU consumption, new attacks use containers to consume network bandwidth, but the increase in CPU consumption is not significant.
    Therefore, security tools that rely on CPU utilization to identify attacks may miss the threat.
    Running security tools that can analyze containers both statically and dynamically is the most effective way to defend against attacks, Aqua suggests.

- [Istio Vulnerability: Sending Malformed Header to Envoy Could Cause Unknown Memory Access](https://istio.io/latest/news/security/istio-security-2022-006/)

    In the affected versions (1.14.2 and 1.13.6), malformed headers sent to Envoy in certain configurations could cause unknown behavior or crashes. The vulnerability was resolved in versions 1.12.8, 1.13.5, and 1.14.1. Additionally, Istio officially recommends against installing 1.14.2 or 1.13.6 in production environments.

- [CRI-O vulnerability: Kube API access may cause memory exhaustion on the node](https://access.redhat.com/security/cve/cve-2022-1708)

    CRI-O reads the output of ExecSync requests. If the amount of output data is large, it may exhaust the memory or disk space of the node, posing a threat to system availability. Currently, the article does not give a solution.

- [Istio control plane has a request processing vulnerability](https://istio.io/latest/news/security/istio-security-2022-004/)

    Istiod has a request processing vulnerability that could allow an attacker sending a custom or very large message to crash the control plane process.
    The risk of attack is greatest when the Kubernetes authentication or change webhook service is publicly exposed. This vulnerability is a 0day vulnerability.

### eBook

- [Excellent Case Collection of Cloud Native Architecture Containers & Microservices](https://developer.aliyun.com/ebook/7898?spm=a2c6h.20345107.ebook-index.7.195a7863AvgDpI)

    The case set is a summary of relevant customers' experience sharing and best practices in building production business systems through AliCloud cloud native products.
    There are 37 enterprise cases centered on container microservices, covering 7 industries and 10+ products such as ACK, MSE, ACR, ASK, ACK One, ASM, and observable.

- [Chinese version of white paper "Assessment of Cloud Native Maturity Matrix"](https://mp.weixin.qq.com/s/xLuAOXwCVif7KrrpZIcUow)

    The white paper summarizes a cloud native maturity matrix assessment process for enterprises undergoing cloud native transformation. Evaluate the current state of the organization from nine areas: culture, product, team, process, architecture, maintenance, delivery, configuration, and infrastructure.
    At the same time, it clarifies four classic cloud native transformation misunderstandings, and summarizes typical cloud native transformation solutions.
    Click to read [White Paper](https://pan.baidu.com/s/1qfEqtL-LCbBo9GhnZBcyyg), extraction code: kvrv

- [E-book "The Foundation of Zero Trust: Using SPIFFE to Create Universal Identity for Infrastructure"](https://mp.weixin.qq.com/s/3qwVW8AeyRvUVxYAq22XKg)

    This book introduces the SPIFFE standard for service identities, and SPIRE, the reference implementation of SPIFFE.
    Provides in-depth coverage of how to design a SPIRE deployment, how to integrate it with other systems, how to use SPIFFE identity notification authorization, how it compares to other security technologies, and more.

- [Kube-OVN v1.10 series of Chinese documents, 99.9% of the questions can be answered here](https://mp.weixin.qq.com/s/OI996gGQasWaFLy2Matghw)

    The documentation is divided into five parts: Kube-OVN Quick Start, Usage Guide, Operation and Maintenance Guide, Advanced Features, and Technical Reference.
    Click to view [documentation](https://kubeovn.github.io/docs/)

- [From construction to governance, the industry's first white paper on microservice governance technology is officially released](https://mp.weixin.qq.com/s/mG0jX66BLOHY0TWTqYO50A)

    Alibaba Cloud's cloud native microservice team recently released ["White Paper on Microservice Governance Technology"](https://developer.aliyun.com/ebook/read/7565?spm=a2c6h.26392459.ebook-detail.4.12d9775enBrpOH).
    This white paper focuses on the business domain of microservice governance, covering the whole process of microservice implementation including technical principles, business cases, solutions, and best practices.

### Other

- [How Cloud Native is Changing Telecom Standards: Top-Down vs. Bottom-Up](https://mp.weixin.qq.com/s/dH_3CAd0PS3EPYKpJA2yNQ)

    The article describes the logic of cloud native bottom-up development principles, best practices, and de facto standards, as well as top-down, committee-driven standards, such as those in the telecom industry.
    And what happens when top-down and bottom-up standards meet, and what happens when managers of protocols meet cloud native standards?

- [Is the infrastructure team ready to take over K8s deployment ops?](https://mp.weixin.qq.com/s/7Y5GfShZhFwBQkQfRUPnoA)

    Kubernetes is well suited as an Infrastructure as a Service (IaaS) that can be offered both on public clouds and on enterprise private clouds as a next-generation infrastructure that provides a reliable infrastructure for modern applications.
    As a result, the construction and operation and maintenance of Kubernetes will also be more often left to the infrastructure team.
    The article explores why an infrastructure team is suitable to take charge of the O&M of Kubernetes and whether such a shift is feasible.

- [K8s natively supported access policy management](https://mp.weixin.qq.com/s/wDlCQkHTBUQDucT9K7G2mg)

    Kubernetes 1.26 provides an alpha version of the validating admission policy update, where a common expression language (CEL) can be used to provide a declarative, in-process alternative to validating admission webhook when validating admission policies. embedding CEL expressions embedding CEL expressions into Kubernetes resources greatly reduces the complexity of the admission webhook.

- [2022 Cloud Native Technology Inventory and Outlook](https://mp.weixin.qq.com/s/yRMTS5z15-PERwlameMOIw)

    The article takes stock of the development of cloud native in 2022 from both the underlying basic technology and scenario-based application technology: the mixed part brings efficiency improvement; Serverless completes standardization based on containers; Service Mesh makes new attempts, the landing method is still being explored; the FinOps concept is rapidly developing under the major theme of cost reduction and efficiency increase Development, etc.

- [In-depth analysis of Containerd - NRI articles](https://mp.weixin.qq.com/s/2LrWqOtqIfbIzWG9fv5ANA)

    NRI is a CRI plugin in containerd that provides a container runtime-level plugin framework to manage node resources.
    NRI can be used to solve performance problems of batch computing and delay-sensitive services, and meet user requirements such as service SLA/SLO, priority, etc.
    For example, by allocating the CPU of the container to the same numa node, memory calls in numa are guaranteed.
    Of course, in addition to numa, there are also resource topology affinity such as CPU and L3 cache.

- [Kubernetes Certificate Management Series](https://mp.weixin.qq.com/s/6VC_15V0MlvN-vCN-GwRLQ)

    The article describes certificates in Kubernetes and how the Kubernetes certificate manager works in production. Then take the certificate management project cert-manager as an example to explain its architecture, components, ecological compatibility, etc.

- [Nine Trends Insights into the Container Ecosystem in 2022](https://mp.weixin.qq.com/s/WNanrbCsdWEuyWP8WvO8UQ)
  
    Datadog’s analysis of over 1.5 billion containers run by customers identified key trends in the container ecosystem:
    The use of serverless container technology in the public cloud continues to rise, multicloud usage is positively correlated with the number of containers in an organization, Kubernetes Ingress usage is on the rise, most hosts are using a Kubernetes version older than 18 months, more than 30% are running containerd of hosts use unsupported versions, NGINX, Redis, and Postgres are the most popular container images.

- [Karmada large-scale test report released, breaking through 100 clusters and 500,000 nodes](https://karmada.io/blog/2022/10/26/test-report/)

    Recently, the Karmada community has carried out large-scale testing of Karmada. According to the analysis of test results, the cluster federation with Karmada as the core can stably support 100 clusters and 500,000 nodes online at the same time, and manage more than 2 million Pods.
    In terms of  use cases, the Push mode is suitable for managing Kubernetes clusters on public clouds, while the Pull mode covers private cloud and edge-related use cases relative to the Push mode.
    In terms of performance and security, the overall performance of the Pull mode is better than that of the Push mode.

- [ToB application privatization delivery technology development history and comparison](https://mp.weixin.qq.com/s/JcDZxabHImljPCEus_inlg)

    In traditional app delivery, managing runtime environment and operating system differences is a pain point. The current cloud native app delivery uses container and kubernetes-related technologies to solve this problem, but the learning and use threshold of these technologies is too high.
    Thus, the abstracted application model becomes the next-generation solution, for example, OAM-based KubeVela app delivery and RAM-based Rainbond app delivery.

- [Survey on Backup and Recovery Solutions for Container Services of Domestic and Foreign Cloud Vendors](https://mp.weixin.qq.com/s/P71vBPiID8o1GI6pqbaO6w)

    This page investigates and analyzes the container service backup and recovery solutions of four vendors (Alibaba Cloud Container Service ACK, Tencent Cloud Container Service TKE, Huawei Cloud Backup Product CBR, Google Cloud Backup for GKE), and compares their respective advantages and disadvantages.

- [Trends behind Apache APISIX 3.0 and Kong 3.0 features in cloud native gateways](https://mp.weixin.qq.com/s/hyqqDojuzEU-LvfR5deBZw)

    The article analyzes in detail the latest versions of two API gateway projects APISIX and Kong, trying to gain insight into valuable technical trends from update details.
    Kong 3.0 began to gradually lean towards the enterprise version, focusing on the government, financial industry, and large enterprises that pay more attention to security compliance.
    All the features launched by APISIX 3.0 are open source. While ensuring performance, it is also actively expanding the surrounding ecology.

- [Kubernetes Node component index combing](https://mp.weixin.qq.com/s/nrKk7tuARnvfnH0VOF7q9Q)

    The article makes a complete review of kubelet's own metrics, kube-proxy metrics, kube-state-metrics metrics, and cadvisor metrics.

- [Upcoming changes in Kubernetes 1.25](https://kubernetes.io/blog/2022/08/04/upcoming-changes-in-kubernetes-1-25/)

    Deletions and major changes in v1.25: PodSecurityPolicy removed, core CSI migration feature upgraded to GA, GlusterFS deprecated, Kubernetes release artifact signature upgraded to Beta, cgroup v2 support upgraded to GA, IPTables chain ownership cleaned up.

- [Interpretation of memory management of Curve resource occupation](https://mp.weixin.qq.com/s/3gupHWlcRRY-lCsV9nZhDA)

    The article combines the distributed storage system [Curve](https://github.com/opencurve/curve) to illustrate the memory layout, the necessity of the memory allocator and the problems to be solved.
    And through examples to illustrate the memory management method of the memory allocator, and finally introduce the current choice of Curve memory allocator and the reason.

- [Summary of eviction strategies on the Kubernetes stand-alone side](https://mp.weixin.qq.com/s/ehECtQiXSHLpCrH5vuBX_w)

    The article summarizes the eviction process and process selection strategy for user space and kernel space.
    In user mode, Kubelet restricts node resources and pod resources through eviction.
     User space triggers the eviction process by monitoring system resources, and kernel space triggers the eviction process by allocating memory.

- [GitOps Maturity Checklist](https://www.weave.works/blog/the-16-point-checklist-for-gitops-success)

    The article introduces a [GitOps checklist](https://go.weave.works/rs/249-YDT-025/images/The%2016-point%20Checklist%20for%20GitOps%20Success.pdf), which can be used for Assess your team's GitOps maturity.
    There are 16 items in the list, including six dimensions: team culture, git management, GitOps pipeline, Kubernetes, security & policy.

- [Why does Istio use SPIRE for authentication?](https://mp.weixin.qq.com/s/043yz1etTkJ1l4Eo6DG7WA)

    The most noteworthy feature in Istio 1.14 is the new support for [SPIRE](https://github.com/spiffe/spire).
    SPIFFE unifies identity standards in heterogeneous environments. Istio uses SPIRE to provide a unique identifier for each workload. The workload in the service mesh will use the service identifier when performing peer authentication, request authentication and authorization policies to verify whether access is allowed.

- [How to ensure Pod security after deprecating Pod Security Policies](https://www.cncf.io/blog/2022/06/30/how-to-secure-kubernetes-pods-post-psps-deprecation/)

    Pod Security Policies (PSP) are deprecated and will be removed in Kubernetes 1.25 in the future.
    Pod Security Admission (PSA) will replace PSP to implement Pod security features. It defines three isolation levels for pods: privileged, baseline, and restricted. Alternatively, external admission controllers such as OPA and Kyverno can be employed.

- [CryptoMB - Speed up Istio TLS handshake](https://istio.io/latest/blog/2022/cryptomb-privatekeyprovider/)

    This page describes a new feature introduced in Envoy 1.20 and Istio 1.14: Accelerating the Istio TLS handshake via the CryptoMB Private Key Provider.
    CryptoMB is an Envoy extension that leverages Intel multi-buffer technology, enabling service meshes to offload TLS handshakes to handle more connections, lower latency, and save CPU.

- [How to think about the multi-runtime architecture of Dapr and Layotto](https://mp.weixin.qq.com/s/sKaKzlOXsLSmqBwv9uI5Cw)

    The article shares Ant's thinking after landing the multi-runtime architecture Laotto:
    The necessity of "portability" of Dapr API, the value of multi-runtime architecture, the difference with Service Mesh and Event Mesh, and the deployment form, etc.

- [Kubernetes 1.24: Avoid conflicts when assigning IP addresses to Services](https://kubernetes.io/blog/2022/05/23/service-ip-dynamic-and-static-allocation/)

    Kubernetes 1.24 allows enabling a new feature gate ``ServiceIPStaticSubrange``.
    After enabling this feature, you can use different IP allocation strategies for Services to reduce the risk of conflicts.

- [Harbor v2.5 remote replication: the signature of the artifact is always there](https://mp.weixin.qq.com/s/erH1iCbNn9yM1Bl5UlgGMg)

    Harbor v2.5 was released last week. The Cosign product signature and verification solution is an important function, which solves the problem that the signature information of products such as images cannot be copied to the target during remote replication.
    This page describes the functionality in detail.
