# Glossary

This page lists some terms common to DEC 5.0 in alphabetical order.

### A

- Abstraction

    In the context of computing, an abstraction is a representation that
    hides specifics from a consumer of [services](/service/)
    (a consumer being a computer program or human),
    making a system more generic and thus easily understood.
    A good example is your laptop's operating system (OS).
    It abstracts away all the details of how your computer works.
    You don't need to know anything about CPU, memory, and how programs are handled,
    you just operate the OS and the OS deals with the details.
    All these details are hidden behind the OS "curtain" or abstraction.

    Systems typically have multiple abstraction layers.
    This significantly simplifies development.
    When programming, developers build components compatible with a particular abstraction layer and
    don't have to worry about all underlying specifics that can be very heterogeneous.
    If it works with the abstraction layer, it works with the system — no matter what's under the hood.

- Addon

    A resource object that extends the functionality of DCE.
    You can install more additional extensions via
    [Container Management](../kpanda/03ProductBrief/WhatisKPanda.md) -> [Helm Template](../kpanda/07UserGuide/helm/README.md).

- Admission Controller

    An [Admission Controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/)
    is a piece of code that intercepts requests to the Kubernetes API server prior to persistence of the object, but after the request is authenticated and authorized.

    Admission controllers may be validating, mutating, or both. Mutating controllers may modify related objects
    to the requests they admit; validating controllers may not.

    Admission controllers limit requests to create, delete, modify objects.
    Admission controllers can also block custom verbs, such as a request connect to a Pod via an API server proxy.
    Admission controllers do not (and cannot) block requests to read (get, watch or list) objects.

- Affinity

    Affinity in DCE is a set of rules that provide the scheduler with hints on where to place pods.

    These rules are defined using DCE Label and Pod specified selectors,
    These rules can be required or preferred, depending on how strictly you want the scheduler to enforce them.

    It is actually divided into node affinity and inter-Pod affinity.

- Aggregation Layer

    The aggregation layer allows Kubernetes to be extended with additional APIs, beyond what is offered by the core Kubernetes APIs. The additional APIs can either be ready-made solutions such as a metrics server, or APIs that you develop yourself.

    The aggregation layer is different from Custom Resources, which are a way to make the kube-apiserver recognise new kinds of object.

- [Alert Rule](../insight/user-guide/05alertcenter/alertrule.md)

    In Insight, this is an alert object created based on the resource status. You can customize the conditions for triggering rules and sending notifications.

- Annotation

    [Annotation](../kpanda/07UserGuide/Nodes/labels-annotations.md) is a key-value pair that is used to attach arbitrary non-identifying metadata to objects.

    The metadata in an annotation can be small or large, structured or unstructured, and can include characters not permitted by labels. Clients such as tools and libraries can retrieve this metadata.

- API, Application Programming Interface

    An API is a way for computer programs to interact with each other. 
    Just as humans interact with a website via a web page, an API allows computer programs to interact with each other. 
    Unlike human interactions, APIs have limitations on what can and cannot be asked of them. 
    The limitation on interaction helps to create stable and functional communication between programs.

    As applications become more complex, small code changes can have drastic effects on other functionality. 
    Applications need to take a modular approach to their functionality if they can grow and maintain stability simultaneously.
    Without APIs, there is a lack of a framework for the interaction between applications. 
    Without a shared framework, it is challenging for applications to scale and integrate.

    APIs allow computer programs or applications to interact and share information in a defined and understandable manner.
    They are the building blocks for modern applications and they provide developers with a way to integrate applications together.
    Whenever you hear about microservices working together, you can infer that they interact via an API. 

- API-initiated eviction

    API-initiated eviction is the process by which you use the Eviction API to create an Eviction object that triggers graceful pod termination.

    You can request eviction by calling the Eviction API directly, or programmatically using a client of the API server, like the `kubectl drain` command. This creates an `Eviction` object, which causes the API server to terminate the Pod.

    API-initiated evictions respect your configured `PodDisruptionBudgets` and `terminationGracePeriodSeconds`.

- API Group

    API groups make it easier to extend the Kubernetes API.
    The API group is specified in a REST path and in the apiVersion field of a serialized object.

    API Groups can be enabled or disabled by changing the configuration of the API server.
    You can also disable or enable paths to specific resources.
    API groups make it easier to extend the K8s API.
    The API group is specified at the REST path and in the `apiVersion` field of the serialized object.

- API Gateway

    An API gateway is a tool that
    aggregates unique application APIs, making them all available in one place.
    It allows organizations to move key functions,
    such as authentication and authorization or limiting the number of requests between applications,
    to a centrally managed location.
    An API gateway functions as a common interface to (often external) API consumers.

    If you’re making APIs available to external consumers,
    you'll want one entry point to manage and control all access.
    Additionally, if you need to apply functionality on those interactions,
    an API gateway allows you to uniformly apply it to all traffic without requiring any app code changes.

    Providing one single access point for various APIs in an application,
    API gateways make it easier for organizations to apply cross-cutting business or security logic in a central location.
    They also allow application consumers to go to a single address for all their needs.
    An API gateway can simplify operational concerns like security and observability
    by providing a single access point for requests to all web services in a system.
    As all requests flow through the API gateway, it presents a single place to
    add functionality like metrics-gathering, rate-limiting, and authorization.

- App Container

    In contrast to the Init container, this is the container that runs part of the workload.

    Application containers are containers (or app containers) in a Pod that start after the Init container has started.

    Init containers allow you to isolate initialization details that are important to the workload as a whole, and the init container does not need to continue running once the application container starts.
    If a Pod does not have an Init container configured, all containers in that Pod are application containers.

- App Architect

    The application architect is the development leader responsible for the high-level design of the application.

    The application architect ensures that the implementation of the application allows it to interact with surrounding components in a scalable and sustainable manner.
    Surrounding components include databases, logging infrastructure, and other microservices.

- App Developer

    Developers who write applications that run on Kubernetes clusters.
    Application developers focus on a certain part of the application. There is a marked difference in the size of their working areas.

- App, Application

    The layer where various containerized services run.

- Audit log, audit log

    [Audit Log](../ghippo/04UserGuide/03AuditLog.md) provides a historical record of changes made to objects in the system.

- Authorization

    [Authorization](../ghippo/04UserGuide/01UserandAccess/iam.md) refers to granting users the permissions required to complete specific tasks, and the authorization takes effect through the permissions of system roles or custom roles.
    After obtaining specific permissions, users can operate on resources or services.

- Autoscaling

    Autoscaling is the ability of a system to scale automatically, typically, in terms of computing resources.
    With an autoscaling system, resources are automatically added when needed and can scale to meet fluctuating user demands.
    The autoscaling process varies and is configurable to scale based on different metrics, such as memory or process time.
    Managed cloud services are typically associated with autoscaling functionality
    as there are more options and implementations available than most on-premise deployments.

    Previously, infrastructure and applications were architected to consider peak system usage.
    This architecture meant that more resources were underutilized and inelastic to changing consumer demand.
    The inelasticity meant higher costs to the business and lost business from outages due to overdemand.

    By leveraging the cloud, virtualizing, and containerizing applications and their dependencies,
    organizations can build applications that scale according to user demands.
    They can monitor application demand and automatically scale them, providing an optimal user experience.
    Take the increase in viewership Netflix experiences every Friday evening.
    Autoscaling out means dynamically adding more resources: for example,
    increasing the number of servers allowing for more video streaming and scaling back once consumption has normalized.

### B, C

- Bare Metal Machine

    Bare metal refers to a physical computer, more specifically a server, that has one, and only one, operating system.
    The distinction is important in modern computing because many, if not most, servers are virtual machines.
    A physical server is typically a fairly large computer with powerful hardware built-in.
    Installing an operating system and running applications directly on that physical hardware,
    without virtualization, is referred to as running on “bare metal.”

    Pairing one operating system with one physical computer is the original pattern of computing.
    All the resources of the physical computer are available directly to the operating system and with no virtualization layer present,
    there is no artificial delay in translating operating system instructions to hardware.

    By dedicating all compute resources of a computer to a single operating system,
    you potentially provide the best possible performance to the operating system.
    If you need to run a workload that must have extremely fast access to hardware resources,
    bare metal may be the right solution.

    In the context of cloud native apps,
    we generally think of performance in terms of scaling to a large number of concurrent events,
    which can be handled by horizontal scaling (adding more machines to your resource pool).
    But some workloads may require vertical scaling (adding more power to an existing physical machine)
    and/or an extremely fast physical hardware response in which case bare metal is better suited.
    Bare metal also allows you to tune the physical hardware and possibly even hardware drivers to help accomplish your task.

- Blue Green Deployment

    Blue-green deployment is a strategy for updating running computer systems with minimal downtime.
    The operator maintains two environments, dubbed “blue” and “green”.
    One serves production traffic (the version all users are currently using), whilst the other is updated.
    Once testing has concluded on the non-active (green) environment,
    production traffic is switched over (often via the use of a load balancer.
    Note that blue-green deployment usually means switching the entire environments, comprising many services, all at once.
    Confusingly, sometimes the term is used with regard to individual services within a system.
    To avoid this ambiguity, the term “zero-downtime deployment” is preferred when referring to individual components.

    Blue-green deployments allow minimal downtime when updating software that must be changed in "lockstep" owing to a lack of backwards compatibility. 
    For example, blue-green deployment would be appropriate for an online store
    consisting of a website and a database that needs to be updated,
    but the new version of the database doesn’t work with the old version of the website, and vice versa.
    In this instance, both need to be changed at the same time.
    If this was done on the production system, customers would notice downtime.

    Blue-green deployment is an appropriate strategy for non-cloud native software that needs to be updated with minimal downtime.
    However, its use is normally a "smell" that legacy software needs to be re-engineered so that components can be updated individually.

- Canary Deployment

    Canary deployments is a deployment strategy that starts with two environments:
    one with live traffic and the other containing the updated code without live traffic.
    The traffic is gradually moved from the original version of the application to the updated version.
    It can start by moving 1% of live traffic, then 10%, 25%, and so on,
    until all traffic is running through the updated version.
    Organizations can test the new version of the software in production, get feedback,
    diagnose errors, and quickly rollback to the stable version if necessary.  

    The term “canary” refers to the "canary in a coal mine" practice
    where canary birds were taken into coal mines to keep miners safe.
    If odorless harmful gases were present, the bird would die, and the miners knew they had to evacuate quickly.
    Similarly, if something goes wrong with the updated code, live traffic is "evacuated" back to the original version.

    No matter how thorough the testing strategy, there are always some bugs discovered in production.
    Shifting 100% of traffic from one version of an app to another can lead to more impactful failures.

    Canary deployments allow organizations to see how new software behaves in real-world scenarios
    before moving significant traffic to the new version.
    This strategy enables organizations to minimize downtime and quickly rollback in case of issues with the new deployment.
    It also allows more in-depth production application testing without a significant impact on the overall user experience.

- cAdvisor

    cAdvisor (Container Advisor) 为用户提供运行中的容器资源用量和性能特征的相关信息。

    cAdvisor 是一个守护进程，负责收集、聚合、处理并输出运行中容器的信息。
    具体而言，针对每个容器，该进程记录容器的资源隔离参数、历史资源用量、完整历史资源用量和网络统计的直方图。
    这些数据可以按容器或按机器层面输出。

- Certificate

    A (digital) certificate — also often referred to as a public key certificate, or SSL certificate — 
    is a digital document used to help secure communications over the network.
    Certificates allow us to know that the particular entity we're communicating with is who they say they are.
    They also allow us to ensure that our communications are private by encrypting the data we send and receive.

    When devices communicate over a network there is no inherent guarantee that a particular device is who it says it is.
    Additionally, we can't guarantee that the traffic between any two devices won't be intercepted by a third party.
    Consequently, any communication can potentially be intercepted, compromising sensitive information like usernames and passwords.

    Modern email clients that utilize certificates can notify you if a sender's identity is correct, as will web browsers (notice the little lock in front of the address bar of your web browser).
    On the other side, certificates can be used to encrypt communication between entities on the internet.
    They provide an encryption technique that makes it nearly impossible, for someone who intercepts the communication, to actually read the data.

- cgroup, control group, 控制组

    一组具有可选资源隔离、审计和限制的 Linux 进程。

    cgroup 是一个 Linux 内核特性，对一组进程的资源使用（CPU、内存、磁盘 I/O 和网络等）进行限制、审计和隔离。

- Chaos Engineering

    Chaos Engineering or CE is the discipline of experimenting on a distributed system in production
    to build confidence in the system's capability to withstand turbulent and unexpected conditions.

    SRE and DevOps practices focus on techniques to increase product resiliency and reliability.
    A system's ability to tolerate failures while ensuring adequate service quality is
    typically a software development requirement.
    There are several aspects involved that could lead to outages of an application,
    like infrastructure, platform or other moving parts of a microservice-based application.
    High-frequency deployment of new features to the production environment can
    result in a high probability of downtime and a critical incident — with considerable consequences to the business.

    Chaos engineering is a technique to meet resilience requirements.
    It is used to achieve resilience against infrastructure, platform, and application failures.
    Chaos engineers use chaos experiments to proactively inject random failures
    to verify that an application, infrastructure, or platform can self-heal and the failure cannot noticeably impact customers.
    Chaos experiments aim to discover blind spots
    (e.g. monitoring or autoscaling techniques) and to improve the communications between teams during critical incidents.
    This approach helps increase resiliency and the team's confidence in complex systems, particularly production.

- CIDR, Classless Inter-Domain Routing

    CIDR（无类域间路由）是一种描述 IP 地址块的符号，被广泛使用于各种网络配置中。

    在 Kubernetes 的上下文中，每个节点以 CIDR 形式（含起始地址和子网掩码）获得一个 IP 地址段，
    从而能够为每个 Pod 分配一个独一无二的 IP 地址。
    虽然其概念最初源自 IPv4，CIDR 已经被扩展为涵盖 IPv6。

- Client-Server Architecture

    In a client-server architecture, the logic (or code) that makes up an application is split between two or more components:
    a client that asks for work to be done
    (e.g. the Gmail web application running in your web browser),
    and one or more servers that satisfy that request
    (e.g. the "send email" service running on Google’s computers in the cloud).
    In this example, outgoing emails that you write are sent by the client (web application running in your web browser)
    to a server (Gmail's computers, which forward your outgoing emails to their recipients).

    This contrasts with self-contained applications (such as desktop applications) that do all the work in one place.
    For example, a word processing program like Microsoft Word may be installed and run entirely on your computer.

    A client-server architecture solves a big challenge self-contained applications pose: regular updates.
    In a self-contained app, for each update, users would have to download and install the latest version.
    Imagine having to download all of Amazon’s product catalog to your own computer before being able to browse it!

    By implementing application logic in a remote server or service,
    operators can update that without needing to change the logic on the client-side.
    This means updates can be made much more frequently.
    Storing data on the server allows many clients to all see and share the same data.
    Consider the difference between using an online word processor, compared to a traditional offline word processor.
    In the former, your files exist on the server-side and
    can be shared with other users who simply download them from the server.
    In the legacy world, files needed to be copied to removable media (floppy disks!) and shared with individuals.

- Cloud Computing

    Cloud computing is a model that offers compute resources like CPU, network, and disk capabilities on-demand over the internet.
    Cloud computing gives users the ability to access and use computing power in a remote physical location.
    Cloud providers like AWS, GCP, Azure, DigitalOcean, and others all offer third parties
    the ability to rent access to compute resources in multiple geographic locations.

    Organizations traditionally faced two main problems when attempting to expand their use of computing power.
    They either acquire, support, design, and pay for facilities
    to host their physical servers and network or expand and maintain those facilities.
    Cloud computing allows organizations to outsource some portion of their computing needs to another organization.

    Cloud providers offer organizations the ability to rent compute resources on-demand and pay for usage.
    This allows for two major innovations:
    Organizations can focus on their product or service without waiting, planning, and spending resources on new physical infrastructure. They can simply scale as needed and on-demand.
    Cloud computing allows organizations to adopt as much or as little infrastructure as they need.

- Cloud Controller Manager, 云控制器管理器

    一个 Kubernetes 控制平面组件，嵌入了特定于云平台的控制逻辑。
    云控制器管理器允许您将您的集群连接到云提供商的 API 之上，
    并将与该云平台交互的组件同与您的集群交互的组件分离开来。

    通过分离 Kubernetes 和底层云基础设置之间的互操作性逻辑，
    `cloud-controller-manager` 组件使云提供商能够以不同于 Kubernetes 主项目的步调发布新特征。

- Cloud-Native Apps

    Cloud native applications are specifically designed to take advantage of innovations in cloud computing.
    These applications integrate easily with their respective cloud architectures,
    taking advantage of the cloud’s resources and scaling capabilities.
    It also refers to applications that take advantage of innovations in infrastructure driven by cloud computing.
    Cloud native applications today include apps that run in a cloud provider’s datacenter and on cloud native platforms on-premise.

    Traditionally, on-premise environments provided compute resources in a fairly bespoke way.
    Each datacenter had services that tightly coupled applications to specific environments,
    often relying heavily on manual provisioning for infrastructure, like virtual machines and services.
    This, in turn, constrained developers and their applications to that specific datacenter.
    Applications that weren't designed for the cloud couldn't take advantage of a cloud environment’s resiliency and scaling capabilities.
    For example, apps that require manual intervention to start correctly cannot scale automatically,
    nor can they be automatically restarted in the event of a failure.  

    While there is no “one size fits all” path to cloud native applications, they do have some commonalities.
    Cloud native apps are resilient, manageable, and aided by the suite of cloud services that accompany them.
    The various cloud services enable a high degree of observability,
    enabling users to detect and address issues before they escalate.
    Combined with robust automation, they allow engineers to make high-impact changes frequently and predictably with minimal toil.

- Cloud-Native Security

    Cloud native security is an approach that builds security into cloud native applications.
    It ensures that security is part of the entire application lifecycle from development to production.
    Cloud native security seeks to ensure the same standards as traditional security models
    while adapting to the particulars of cloud native environments,
    namely rapid code changes and highly ephemeral infrastructure.
    Cloud native security is highly related to the practice called DevSecOps.

    Traditional security models were built with a number of assumptions that are no longer valid.
    Cloud native apps change frequently, use a large number of open source tools and libraries,
    often run in vendor-controlled infrastructure, and are subject to rapid infrastructure changes.
    Code reviews, long quality assurance cycles, host-based vulnerability scanning,
    and last minute security reviews cannot scale with cloud native applications.

    Cloud native security introduces a new way of working that protects applications
    by migrating from traditional security models to one where security is involved in every step of the release cycle.
    Manual audits and checks are largely replaced with automated scans.
    Rapid code release pipelines are integrated with tools that scan code for vulnerabilities before they’re compiled.
    Open source libraries are pulled from trusted sources and monitored for vulnerabilities.
    Instead of slowing change a cloud native security model embraces it
    by frequently updated vulnerable components or ensuring infrastructure is regularly replaced.

- Cloud-Native Tech

    Cloud native technologies, also referred to as the cloud native stack,
    are the technologies used to build cloud native applications.
    These technologies enable organizations to build and run scalable applications in modern and dynamic environments
    such as public, private, and hybrid clouds,
    while leveraging cloud computing benefits to their fullest.
    They are designed from the ground up to exploit the capabilities of cloud computing and containers, service meshes, microservices,
    and immutable infrastructure exemplify this approach.

    The cloud native stack has many different technology categories, addressing a variety of challenges.
    If you have a look at the CNCF Cloud Native Landscape,
    you'll see how many different areas it touches upon.
    But on a high level, they address one main set of challenges:
    the downsides of traditional IT operating models.
    Challenges include difficulties creating scalable, fault-tolerant, self-healing applications,
    as well as inefficient resource utilization, among others.

    While each technology addresses a very specific problem,
    as a group, cloud native technologies enable loosely coupled systems that are resilient, manageable, and observable.
    Combined with robust automation, they allow engineers to make high-impact changes frequently and predictably with minimal toil.
    Desirable traits of cloud native systems are easier to achieve with the cloud native stack.

- Cloud Provider, 云提供商

    一个提供云计算平台的商业机构或其他组织。
    云提供商有时也称作云服务提供商（Cloud Service Provider, CSP）提供云计算平台或服务。

    很多云提供商提供托管的基础设施（也称作基础设施即服务或 IaaS）。
    针对托管的基础设施，云提供商负责服务器、存储和网络，而用户（您）
    负责管理其上运行的各层软件，例如运行一个 Kubernetes 集群。

    您也会看到 Kubernetes 被作为托管服务提供；有时也称作平台即服务或 PaaS。
    针对托管的 Kubernetes，您的云提供商负责 Kubernetes 的控制平面以及节点及其所依赖的基础设施：
    网络、存储以及其他一些诸如负载均衡器之类的元素。

- Cluster

    A cluster is a group of computers or applications that work together towards a common goal.
    In the context of cloud native computing, the term is most often applied to Kubernetes.
    A Kubernetes cluster is a set of services (or workloads) that run in their own containers, usually on different machines.
    The collection of all these containerized services, connected over a network, represent a cluster.

    Software that runs on a single computer presents a single point of failure
    — if that computer crashes, or someone accidentally unplugs the power cable,
    then some business-critical system may be taken offline.
    That's why modern software is generally built as distributed applications, grouped together as clusters.

    Clustered, distributed applications run across multiple machines, eliminating a single point of failure.
    But building distributed systems is really hard.
    In fact, it's a computer science discipline in its own right.
    The need for global systems and years of trial and error led to the development of a new kind of tech stack:
    cloud native technologies.
    These new technologies are the building blocks that make the operation and creation of distributed systems easier.

- Cluster Architect, 集群架构师

    集群架构师是指涉及一个或多个 Kubernetes 集群基础设施设计的人员。
    集群架构师通常更关心分布式系统的最佳实践，例如高可用性和安全性。

- Cluster Infrastructure, 集群基础设施

    处于基础设施层，提供并维护虚拟机、网络、安全组及其他资源。

- Cluster Operations, 集群运营

    Kubernetes 管理相关工作包括：日常管理运营和协调升级。

    集群运营工作的示例包括：

    - 部署新节点来扩容集群、执行软件升级、实施安全控制、
    - 添加或删除存储、配置集群网络、管理集群范围的可观测性和响应集群事件。

- Cluster Operator, 集群运营人员

    配置、控制、监控集群的人员。
    他们的主要职责是保证集群正常运行，可能需要进行周期性的维护和升级活动。

- CNCF, Cloud Native Computing Foundation, 云原生计算基金会

    隶属于 Linux 基金会，成立于 2015 年 12 月，是一个非营利性组织，致力于培育和维护一个厂商中立的开源生态系统来推广云原生技术，普及云原生应用。

- CNI, Container network interface, 容器网络接口

    [容器网络接口插件](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)是遵循 appc/CNI 协议的一类网络插件。

    DCE 5.0 支持的 CNI 包括但不限于：

    - Calico
    - Cilium
    - Contour
    - F5networks
    - Ingress-nginx
    - Metallb
    - Multus-underlay
    - Spiderpool

- [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/), 配置项

    [ConfigMap](../kpanda/07UserGuide/ConfigMapsandSecrets/UsedConfigMap.md) 是一种 API 对象，用来将非机密性的数据保存到键值对中。
    使用时可以用作环境变量、命令行参数或者存储卷中的配置文件。

    ConfigMap 将您的环境配置信息和容器镜像解耦，便于应用配置的修改。

- Container Environment Variables, 容器环境变量

    容器环境变量提供了 name=value 形式的、运行容器化应用所必须的一些重要信息。

    容器环境变量为运行中的容器化应用提供必要的信息，同时还提供与容器重要资源相关的其他信息，
    例如文件系统信息、容器自身的信息以及其他像服务端点（Service endpoints）这样的集群资源信息。

- Container Lifecycle Hooks, 容器生命周期钩子

    生命周期钩子暴露容器管理生命周期中的事件，允许用户在事件发生时运行代码。

    针对容器暴露了两个钩子：

    - PostStart 在容器创建之后立即执行，
    - PreStop 在容器停止之前立即阻塞并被调用。

- Container Image

    A container image is an immutable, static file containing the dependencies for the creation of a container.
    These dependencies may include a single executable binary file, system libraries,
    system tools, environment variables, and other required platform settings.
    Container images result from an application's containerization and are typically stored in container registries,
    where they can be downloaded and run as an isolated process using a Container Runtime Interface (CRI).
    A container image framework must follow the standard schema defined by the Open Container Initiative (OCI).

    Traditionally, application servers are configured per environment, and applications are deployed to them.
    Any misconfiguration between environments is problematic and often leads to downtime or failed deployments.
    An application's environment needs to be repeatable and well-defined;
    otherwise, the chance of environment-related bugs increases.
    When application environments are configured inadequately or inaccurate,
    horizontal and vertical scaling of applications becomes challenging.

    Container images bundle an application with any of its runtime dependencies, such as an application server.
    This provides consistency across all environments, including a developer's machine.
    Container images can be used to instantiate as many containers as needed, allowing for greater scalability.

- Container

    A container is a running process with resource and capability constraints managed by a computer’s operating system.
    The files available to the container process are packaged as a container image.
    Containers run adjacent to each other on the same machine,
    but typically the operating system prevents the separate container processes from interacting with each other.

    Before containers were available, separate machines were necessary to run applications.
    Each machine would require its own operating system, which takes CPU, memory, and disk space,
    all for an individual application to function.
    Additionally, the maintenance, upgrade, and startup of an operating system is another significant source of toil.

    Containers share the same operating system and its machine resources,
    spreading the operating system’s resource overhead and creating efficient use of the physical machine.
    This capability is only possible because containers are typically limited from being able to interact with each other.
    This allows many more applications to be run on the same physical machine.

    There are limitations, however.
    Since containers share the same operating system, processes can be considered less secure than alternatives.
    Containers also require limits on the shared resources.
    To guarantee resources, administrators must constrain and limit memory and CPU usage so that other applications do not perform poorly.

- containerd

    强调简单性、健壮性和可移植性的一种容器运行时。

    [containerd](https://github.com/containerd/containerd) 是一种容器行时，能在 Linux 或者 Windows 后台运行。
    containerd 能取回、存储容器镜像，执行容器实例，提供网络访问等。

- Containerization

    Containerization is the process of bundling an application and its dependencies into a container image.
    The container build process requires adherence to the [Open Container Initiative](https://opencontainers.org) (OCI) standard.
    As long as the output is a container image that adheres to this standard, which containerization tool is used doesn't matter.

    Before containers became prevalent, organizations relied on virtual machines (VMs) to
    orchestrate multiple applications on a single bare-metal machine.
    VMs are significantly larger than containers and require a hypervisor to run.
    Due to the storage, backup, and transfer of these larger VM templates, creating the VM templates is also slow.
    Additionally, VMs can suffer from configuration drift which violates the principle of immutability.

    Container images are lightweight (unlike traditional VMs) and
    the containerization process requires a file with a list of dependencies.
    This file can be version controlled and the build process automated,
    allowing an organization to focus on other priorities
    while the automated processes take care of the build.
    A container image is stored by a unique identifier
    that is tied to its exact content and configuration.
    As containers are scheduled and rescheduled,
    they are always reset to their initial state which eliminates configuration drift.

- Container as a service (CaaS)

    Containers-as-a-Service (CaaS) is a cloud service that helps manage and deploy apps
    using container-based abstraction.
    This service can be deployed on-premises or in the cloud.

    CaaS providers offer a framework or orchestration platform that
    automates key IT functions on which containers are deployed and managed.
    It helps developers build secure and scalable containerized apps.
    Because users only buy the resources they need (scheduling capabilities, load balancing, etc.),
    they save money and increase efficiency.
    Containers create consistent environments to rapidly develop and
    deliver cloud-native applications that can run anywhere.

    Without CaaS, software development teams need to deploy, manage, and monitor
    the underlying infrastructure that containers run on.

    When deploying containerized applications to a CaaS platform,
    users gain visibility into system performance through log aggregation and monitoring tools.
    CaaS also includes built-in functionality for auto scaling and orchestration management.
    It enables teams to build high visibility and high availability distributed systems.
    In addition, by allowing rapid deployments, CaaS increases team development velocity.
    While containers ensure a consistent deployment target,
    CaaS lowers engineering operating costs
    by reducing needed DevOps resources needed to manage a deployment.

- Continuous Delivery

    Continuous delivery, often abbreviated as  CD, is a set of practices
    in which code changes are automatically deployed into an acceptance environment
    (or, in the case of continuous deployment, into production).
    CD crucially includes procedures to ensure that software is adequately tested
    before deployment and provides a way to rollback changes if deemed necessary.
    Continuous integration (CI) is the first step towards continuous delivery
    (i.e., changes have to merge cleanly before being tested and deployed).

    Deploying reliable updates becomes a problem at scale.
    Ideally, we'd deploy more frequently to deliver better value to end-users.
    However, doing it manually translates into high transaction costs for every change.
    Historically, to avoid these costs, organizations have released less frequently,
    deploying more changes at once and increasing the risk that something goes wrong.

    CD strategies create a fully automated path to production
    that tests and deploys the software using various deployment strategies
    such as canary or blue-green releases.
    This allows developers to deploy code frequently,  giving them peace of mind that the new revision has been tested.
    Typically, trunk-based development is used in CD strategies as opposed to feature branching or pull requests.

- Continuous Deployment

    Continuous deployment, often abbreviated as CD, goes a step further than continuous delivery
    by deploying finished software directly to production.
    Continuous deployment (CD) goes hand in hand with continuous integration (CI),
    and is often referred to as CI/CD.
    The CI process tests if the changes to a given application are valid,
    and the CD process automatically deploys the code changes through an organization's environments from test to production.

    Releasing new software versions can be a labor-intensive and error-prone process.
    It is also often something that organizations will only want to do infrequently to avoid production incidents
    and reduce the number of time engineers need to be available outside of regular business hours.
    Traditional software deployment models leave organizations in a vicious cycle
    where the process of releasing software fails to meet organizational needs around both stability and feature velocity.

    By automating the release cycle and forcing organizations to release to production more frequently,
    CD does what CI did for development teams for operations teams.
    Specifically, it forces operations teams to automate the painful and error-prone portions of production deployments, reducing overall risk.
    It also makes organizations better at accepting and adapting to production changes, which leads to higher stability.

- Continuous Integration

    Continuous integration, often abbreviated as CI, is the practice of integrating code changes as regularly as possible.
    CI is a prerequisite for continuous delivery (CD).
    Traditionally, the CI process begins when code changes are committed to a source control system (Git, Mercurial, or Subversion)
    and ends with a tested artifact ready to be consumed by a CD system.

    Software systems are often large and complex, with numerous developers maintaining and updating them.
    Working in parallel on different parts of the system,
    these developers may make conflicting changes and inadvertently break each other’s work.
    Additionally, with multiple developers working on the same project,
    any everyday tasks such as testing and calculating code quality would need to be repeated by each developer, wasting time.

    CI software automatically checks that code changes merge cleanly whenever a developer commits a change.
    It's a near-ubiquitous practice to use the CI server to run code quality checks, tests, and even deployments.
    As such, it becomes a concrete implementation of quality control within teams.
    CI allows software teams to turn every code commit into either a concrete failure or a viable release candidate.

- Control Plane, 控制平面

    控制平面是指容器编排层，它暴露 API 和接口来定义、部署容器和管理容器的生命周期。

    这个编排层是由多个不同的组件组成，例如以下（但不限于）几种：

    - etcd
    - API 服务器
    - 调度器
    - 控制器管理器
    - 云控制器管理器

    这些组件可以作为传统的操作系统服务（守护程序）或容器运行。运行这些组件的主机也被称为 Master。

- Controller, 控制器

    控制器通过 API 服务器监控集群的公共状态，并致力于将当前状态转变为期望的状态。

    控制器（作为控制平面的一部分）通过 API 服务器监控您的集群中的公共状态。

    其中一些控制器是运行在控制平面内部的，对 Kubernetes 来说，这些控制器提供核心控制操作。
    比如部署控制器（deployment controller）、守护控制器（daemonset controller）、
    命名空间控制器（namespace controller）、持久化数据卷控制器（persistent volume controller）等
    都是运行在 kube-controller-manager 中的。

- Counter, 计数器

    计数器是一种累计型的度量指标，它是一个 **只能递增** 的数值。计数器主要用于统计类似于服务请求数、任务完成数和错误出现次数这样的数据。

- Contour, 网关控制节点

    Contour 作为微服务网关的控制面，被部署为控制节点，充当 Envoy 的后端管理服务能力。
    Contour 提供便捷的网关配置，支持动态配置更新，多集群部署能力。
    Contour 同时提供了 HTTPProxy CRD 用于增强 Kubernetes Ingress 的核心配置能力，
    Contour 以 Deployment 的方式部署，为保障生产服务稳定性，建议部署在多个副本。

- Control Plane, 控制平面

    控制平面是一组系统服务，这些服务配置网格或者网格的子网来管理工作负载实例之间的通信。
    单个网格中控制平面的所有实例共享相同的配置资源。

- [CRD](../kpanda/07UserGuide/CustomResources/create.md), CustomResourceDefinition, 自定义资源定义

    通过定制化的代码给您的 Kubernetes API 服务器增加资源对象，而无需编译完整的定制 API 服务器。

    当 Kubernetes 公开支持的 API 资源不能满足您的需要时，CRD 让您可以在自己的环境上扩展 Kubernetes API。

    自定义资源定义是默认的 Kubernetes API 扩展，服务网格使用 Kubernetes CRD API 来进行配置。

- CRI-O

    专用于 Kubernetes 的轻量级容器运行时软件工具。该工具可让您通过 Kubernetes CRI 使用 OCI 容器运行时。

    CRI-O 是 CRI 的一种实现，使得您可以使用与开放容器倡议（Open Container Initiative；OCI）
    [运行时规范](https://www.github.com/opencontainers/runtime-spec)兼容的容器。

    部署 CRI-O 允许 Kubernetes 使用任何符合 OCI 要求的运行时作为容器运行时去运行 Pod，并从远程容器仓库获取 OCI 容器镜像。

- CRI, Container Runtime Interface, 容器运行时接口

    CRI 是一组与节点上 kubelet 集成的容器运行时 API。
    kubelet 和容器运行时之间通信的主要协议。

    CRI 定义了主要 [gRPC](https://grpc.io) 协议，用于集群组件 kubelet 和容器运行时。

- CR, Container Runtime, 容器运行时

    容器运行时是负责运行容器的组件。

    Kubernetes 支持许多容器运行环境，例如 containerd、cri-o 以及
    [Kubernetes CRI](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-node/container-runtime-interface.md)
    的其他任何实现。

- [CronJob](../kpanda/07UserGuide/Workloads/CreateCronJobByImage.md), 周期调度任务

    管理定期运行的任务。

    与 **crontab** 文件中的一行命令类似，周期调度任务（CronJob）对象使用
    [cron](https://zh.wikipedia.org/wiki/Cron) 格式设置排期表。

- CSI, Container Storage Interface

    容器存储接口 （CSI）定义了存储系统暴露给容器的标准接口。

    CSI 允许存储驱动提供商为 Kubernetes 创建定制化的存储插件，
    而无需将这些插件的代码添加到 Kubernetes 代码仓库（外部插件）。
    要使用某个存储提供商的 CSI 驱动，您首先要[将它部署到您的集群上](https://kubernetes-csi.github.io/docs/deploying.html)。
    然后您才能创建使用该 CSI 驱动的 Storage Class。

### D

- [DaemonSet](../kpanda/07UserGuide/Workloads/CreateDaemonSetByImage.md), 守护进程集

    确保 Pod 的副本在集群中的一组节点上运行。

    用来部署系统守护进程，例如日志搜集和监控代理，这些进程通常必须运行在每个节点。

- Data Center

    A data center is a specialised building or facility designed specifically to house computers, most often servers.
    Data centers tend to be connected to high-speed internet lines,
    especially in the case of data centers focused on cloud computing.
    The buildings data centers are housed in also have equipment to maintain service even in the case of negative events,
    such as generators to provide power during outages,
    as well as powerful air conditioning to deal with waste heat produced by the computers.

    Instead of every business having to host their own server equipment where they are located,
    data centers allow companies and individuals to take advantage of the
    specialised knowledge and efficiencies of scale of data center providers.
    This means not having to worry about managing power supply, fire suppression technology,
    air conditioning or high speed internet connectivity, for example.

    For cloud computing, data centers are crucial.
    As resources and infrastructure can be provisioned according to the scale of demand,
    businesses can rent cloud computing resources in a data center without having to worry about forecasting
    – and potentially under-resourcing or overpaying – for computing resources.
    As data centers exist all over the world,
    this allows for provisioning resources geographically near to demand
    without having to physically ship and set up equipment.

- Database as a service

    Database-as-a-Service (DBaaS) is a service managed by a cloud operator (public or private)
    that supports applications without requiring the application team to
    perform traditional database administration functions.
    DBaaS allows app developers to leverage databases without being experts or
    hiring a database administrator (DBA) to keep the database up to date.

    Traditionally, in on-premise setups, organizations regularly have to invest in
    additional storage and processing capacity to accommodate database expansion which can be expensive.
    Additionally, developers provision and configure databases with the help of IT infrastructure teams,
    slowing deployment speed of database-driven applications down.
    Loading and executing them also takes longer.

    DBaaS allows developers to outsource all administration/administrative operations to the cloud-based service provider.
    The service provider ensures the database is running smoothly,
    including configuration management, backups, patches, upgrades, service monitoring, and more,
    with a user-friendly interface to manage it all.
    DBaaS helps organizations develop enterprise-grade applications faster while minimizing database costs.

- Data ID

    Nacos 中某个配置集的 ID。配置集是一组配置项的集合，通常表现为一个配置文件，其中包括系统各方面的配置。

- Data Plane, 数据平面

    数据平面是网格的一部分，直接控制工作负载实例之间的通信。
    服务网格的数据平面使用智能 Envoy 代理部署成边车去调节和控制服务网格中发送和接受的流量。

    提供诸如 CPU、内存、网络和存储的能力，以便容器可以运行并连接到网络。

- Debugging

    Debugging is the process or activity of finding and resolving bugs (or errors) from computer programs, software, or systems to get the desired result.
    A bug is a defect or a problem leading to incorrect or unexpected results.

    Software development is a complex activity that makes it nearly impossible to write code without introducing bugs.
    Those bugs lead to code that will likely not function as desired (undefined behavior) when executed.
    Depending on how critical an application is, bugs can have a significant negative impact — financially or even on human lives.
    Usually, application code has to go through different stages or environments where it gets tested.
    The more critical an application is, the more accurate the testing has to be.

    When bugs appear, engineers have to debug (e.g., finding and fixing) the app to decrease undesired behavior for production systems.
    Debugging is no easy task as engineers have to track down the source of the undesired behavior.
    It requires knowledge about the code itself and the execution context at runtime.
    This is where different debugging techniques and tools come in handy.
    Analysis of logs, traces, and metrics, for instance, are used for debugging directly in production.
    Developers can use interactive debugging to step through the code at runtime while analyzing the related execution context.
    Once they have identified the source of the failure, they correct the code and create a bug fix or patch.

- [Deployement](../kpanda/07UserGuide/Workloads/CreateDeploymentByImage.md), 无状态负载

    管理多副本应用的一种 API 对象，通常通过运行没有本地状态的 Pod 来完成工作。

    每个副本表现为一个 Pod，Pod 分布在集群中的节点上。
    对于确实需要本地状态的工作负载，请考虑使用 StatefulSet。

- Device Plugin, 设备插件

    一种软件扩展，可以使 Pod 访问由特定厂商初始化或者安装的设备。

    设备插件在工作节点上运行并为 Pod 提供访问资源的能力，
    例如：本地硬件这类资源需要特定于供应商的初始化或安装步骤。

    设备插件向 kubelet 公布资源，以便工作负载 Pod 访问 Pod 运行所在节点上的硬件功能特性。
    您可以将设备插件部署为 DaemonSet，或者直接在每个目标节点上安装设备插件软件。

- DevOps

    DevOps is a methodology in which teams own the entire process from application development to production operations, hence DevOps.
    It goes beyond implementing a set of technologies and requires a complete shift in culture and processes.
    DevOps calls for groups of engineers that work on small components (versus an entire feature), decreasing handoffs – a common source of errors.

    Traditionally, in complex organizations with tightly-coupled monolithic apps,
    work was generally fragmented between multiple groups.
    This led to numerous handoffs and long lead times.
    Each time a component or update was ready, it was placed in a queue for the next team.
    Because individuals only worked on one small piece of the project, this approach led to a lack of ownership.
    Their goal was to get the work to the next group, not deliver the right functionality to the customer — a
    clear misalignment of priorities.

    By the time code finally got into production, it went through so many developers,
    waiting in so many queues that it was difficult to trace the origin of the problem if the code didn’t work.
    DevOps turns this approach upside down.

    Having one team own the entire lifecycle of an application results in
    minimized handoffs, reduce risk when deploying into production, better code quality
    as teams are also responsible for how code performs in production
    and increased employee satisfaction due to more autonomy and ownership.

- Dependency topology, 依赖拓扑

    以拓扑图的方式展示服务调用之间的依赖关系。

- Destination, 目标服务

    目标服务是 envoy 代表一个源服务工作负载与之打交道的远程上游服务。
    这些上游服务可以有多个服务版本，envoy 根据路由选择对应的版本。

- Destination Rule, 目标规则

    目标规则定义了在路由发生后应用于服务的流量策略。
    这些规则指定负载均衡的配置、来自边车代理的连接池大小以及异常检测设置，从而实现从负载均衡池中检测和熔断不健康的主机。

- Diagnosis, 诊断模式

    诊断模式即对 Contour 进行功能调试，支持在 Contour 启动时附加对应的启动参数。

- Disruption, 干扰

    导致 Pod 服务停止的事件。

    干扰（Disruption）是指导致一个或者多个 Pod 服务停止的事件。
    干扰会影响依赖于受影响的 Pod 的资源，例如 Deployment。

    如果您作为一个集群操作人员，销毁了一个从属于某个应用的 Pod，Kubernetes 视之为主动干扰（Voluntary Disruption）。
    如果由于节点故障或者影响更大区域故障的断电导致 Pod 离线，Kubernetes 视之为非主动干扰（Involuntary Disruption）。

- Distributed Apps

    A distributed application is an application where the functionality is broken down into multiple smaller independent parts.
    Distributed applications are usually composed of individual microservices
    that handle different concerns within the broader application.
    In a cloud native environment, the individual components typically run as containers on a cluster.

    An application running on one single computer represents a single point of failure — if that computer fails, the application becomes unavailable.
    Distributed applications are often contrasted to monolithic applications.
    A monolithic app can be harder to scale as the various components can't be scaled independently.
    They can also become a drag on developer velocity as they grow
    because more developers need to work on a shared codebase that doesn't necessarily have well defined boundaries.

    When splitting an application into different pieces and running them in many places, the overall system can tolerate more failures.
    It also allows an application to take advantage of scaling features not available to a single application instance,
    namely the ability to scale horizontally.
    This does, however, come at a cost: increased complexity and operational overhead
    — you’re now running lots of application components instead of one app.

- Distributed System

    A distributed system is a collection of autonomous computing elements
    connected over a network that appears to users as a single coherent system.
    Generally referred to as nodes, these components can be hardware devices (e.g. computers, mobile phones) or software processes.
    Nodes are programmed to achieve a common goal and, to collaborate, they exchange messages over the network.

    Numerous modern applications today are so big they'd need supercomputers to operate.
    Think Gmail or Netflix. No single computer is powerful enough to host the entire application.
    By connecting multiple computers, compute power becomes nearly limitless.
    Without distributed computing, many applications we rely on today wouldn't be possible.

    Traditionally, systems would scale vertically.
    That's when you add more CPU or memory to an individual machine.
    Vertical scaling is time-consuming, requires downtime, and reaches its limit quickly.

    Distributed systems allow for horizontal scaling (e.g. adding more nodes to the system whenever needed).
    This can be automated allowing a system to handle a sudden increase in workload or resource consumption.

    A non-distributed system exposes itself to risks of failure because if one machine fails, the entire system fails.
    A distributed system can be designed in such a way that,
    even if some machines go down, the overall system can still keep working to produce the same result.

- Docker

    Docker 是一种可以提供操作系统级别虚拟化（也称作容器）的软件技术。

    Docker 使用了 Linux 内核中的资源隔离特性（如 cgroup 和内核命名空间）以及支持联合文件系统（如 OverlayFS 和其他），
    允许多个相互独立的“容器”一起运行在同一 Linux 实例上，从而避免启动和维护虚拟机（Virtual Machines；VM）的开销。

- Dockershim

    Dockershim 是 Kubernetes v1.23 及之前版本中的一个组件，Kubernetes 系统组件通过它与 Docker Engine 通信。

    从 Kubernetes v1.24 起，Dockershim 已从 Kubernetes 中移除。

- Downward API

    将 Pod 和容器字段值暴露给容器中运行的代码的机制。
    在不需要修改容器代码的前提下让容器拥有关于自身的信息是很有用的。
    修改代码可能使容器直接耦合到 Kubernetes。

    Kubernetes Downward API 允许容器使用它们自己或它们在 Kubernetes 集群中所处环境的信息。
    容器中的应用程序可以访问该信息，而不需要以 Kubernetes API 客户端的形式执行操作。

    有两种方法可以将 Pod 和容器字段暴露给正在运行的容器：

    - 使用环境变量
    - 使用 `downwardAPI` 卷

    这两种暴露 Pod 和容器字段的方式统称为 **Downward API**。

- Dynamic Volume Provisioning, 动态卷供应

    允许用户请求自动创建存储卷。

    动态供应让集群管理员无需再预先供应存储。相反，它通过用户请求自动地供应存储。
    动态卷供应是基于 API 对象 StorageClass 的，
    StorageClass 可以引用卷插件（Volume Plugin）提供的卷，也可以引用传递给卷插件的参数集。

### E, F

- Edge computing

    Edge computing is a distributed system approach that shifts some storage and computing capacity from the primary data center to the data source.
    The gathered data is computed locally (e.g., on a factory floor, in a store, or throughout a city) rather than sent to a centralized data center for processing and analysis.
    These local processing units or devices represent the system's edge, whereas the data center is its center.
    The output computed at the edge is then sent back to the primary data center for further processing.
    Examples of edge computing include wrists gadgets or computers that analyze traffic flow.

    Over the past decade, we've seen an increasing amount of edge devices (e.g., mobile phones, smart watches, or sensors).
    In some cases, real-time data processing is not only a nice-to-have but vital.
    Think of self-driving cars.
    Now imagine the data from the car's sensors would have to be transferred to a data center for processing before being sent back to the vehicle so it can react appropriately.
    The inherent network latency could be fatal.
    While this is an extreme example, most users wouldn't want to use a smart device unable to provide instant feedback. 

    As described above, for edge devices to be useful, they must do at least part of the processing and analyzing locally to provide near real-time feedback to users.
    This is achieved by shifting some storage and processing resources from the data center to where the data is generated: the edge device.
    Processed and unprocessed data is subsequently sent to the data center for further processing and storage.
    In short, efficiency and speed are the primary drivers of edge computing.

- EndpointSlice

    一种将网络端点与 Kubernetes 资源组合在一起的方法。

    一种将网络端点组合在一起的可扩缩、可扩展方式。
    它们将被 kube-proxy 用于在每个节点上建立网络路由。

- Endpoint, 端点

    端点负责记录与服务 Service 的选择算符相匹配的 Pod 的 IP 地址。

    端点可以手动配置到 Service 上，而不必指定选择算符标识。

    EndpointSlice 提供了一种可扩缩、可扩展的替代方案。

- Envoy

    Envoy 是在服务网格里使用的高性能代理，用于为所有服务网格里的服务调度进出的流量。

- Ephemeral Container, 临时容器

    一种可以在 Pod 中临时运行的容器类型。

    如果想要调查运行中有问题的 Pod，可以向该 Pod 添加一个临时容器并进行诊断。
    临时容器没有资源或调度保证，因此不应该使用它们来运行任何部分的工作负载本身。
    静态 Pod 不支持临时容器。

- etcd

    一致且高度可用的键值存储，用作 Kubernetes 的所有集群数据的后台数据库。

    如果您的 Kubernetes 集群使用 etcd 作为其后台数据库，请确保您针对这些数据有一份备份计划。

- Event, 事件

    对集群中某处所发生事件的报告。通常用来表述系统中某种状态变更。

    事件的保留时间有限，随着时间推进，其触发方式和消息都可能发生变化。
    事件用户不应该对带有给定原因（反映下层触发源）的时间特征有任何依赖，
    也不要寄希望于该原因所造成的事件会一直存在。

    事件应该被视为一种告知性质的、尽力而为的、补充性质的数据。

    在 Kubernetes 中，审计机制会生成一种不同类别的 Event 记录（API 组为 `audit.k8s.io`）。

- Event-Driven Architecture

    Event-driven architecture is a software architecture that promotes the creation, processing, and consumption of events.
    An event is any change to an application's state.
    For example, hailing a ride on a ride-sharing app represents an event.
    This architecture creates the structure in which events can be properly routed from their source (the app requesting a ride) to the desired receivers (the apps of available drivers nearby).

    As more data becomes real-time, finding reliable ways to ensure that events are captured and routed to the appropriate service that must process event requests gets increasingly challenging.
    Traditional methods of handling events often have no way to guarantee that messages are appropriately routed or were actually sent or received.
    As applications begin to scale, it becomes more challenging to orchestrate events.

    Event-driven architectures establish a central hub for all events (e.g., Kafka).
    You then define the event producers (source) and consumers (receiver), and the central event hub guarantees the flow of events.
    This architecture ensures that services remain decoupled and events are properly routed from the producer to the consumer.
    The producer will take the incoming event, usually by HTTP protocol, then route the event information.

- Eviction, 驱逐

    终止节点上一个或多个 Pod 的过程。

    驱逐的两种类型：

    - 节点压力驱逐
    - API 发起的驱逐

- Extensions, 扩展组件

    扩展组件（Extensions）是扩展并与 Kubernetes 深度集成以支持新型硬件的软件组件。

    许多集群管理员会使用托管的 Kubernetes 或其某种发行包，这些集群预装了扩展组件。
    因此，大多数 Kubernetes 用户将不需要安装扩展组件，需要编写新的扩展组件的用户就更少了。

- External Control Plane, 外部控制平面

    外部控制平面可以从外部管理运行在自己的集群或者其他基础设施中的网格工作负载。
    控制屏幕可以部署在一个集群中，但是不能部署在它所控制的网格的一部分集群中。
    它的目的是将控制平面与网格的数据屏幕完全分离。

- Firewall

    A firewall is a system that filters network traffic on the basis of specified rules.
    Firewalls can be hardware, software, or a combination of the two.

    By default, a network will allow anyone to enter and depart as long as they follow the network's routing rules.
    Because of this default behavior, securing a network is challenging.
    For example, in a microservices-based banking app, the services communicate with one another
    by transmitting highly sensitive financial data through their network.
    A malicious actor may infiltrate the network, intercept communication, and do damage if there was no firewall in place.

    A firewall examines network traffic using pre-defined rules.
    All traffic is filtered, and any traffic coming from untrustworthy or suspect sources is blocked
    — only traffic configured to be accepted gets in.
    Firewalls establish a barrier between secured and controlled internal trusted networks.

- Finalizer

    一个带有命名空间的键，告诉 Kubernetes 等到特定的条件被满足后，再完全删除被标记为删除的资源。

    Finalizer 是带有命名空间的键，告诉 Kubernetes 等到特定的条件被满足后，
    再完全删除被标记为删除的资源。Finalizer 提醒控制器清理被删除的对象拥有的资源。

    当您告诉 Kubernetes 删除一个指定了 Finalizer 的对象时，
    Kubernetes API 通过填充 `.metadata.deletionTimestamp` 来标记要删除的对象，
    并返回 `202` 状态码(HTTP "已接受") 使其进入只读状态。
    此时控制平面或其他组件会采取 Finalizer 所定义的行动，
    而目标对象仍然处于终止中（Terminating）的状态。
    这些行动完成后，控制器会删除目标对象相关的 Finalizer。
    当 `metadata.finalizers` 字段为空时，Kubernetes 认为删除已完成并删除对象。

    您可以使用 Finalizer 控制资源的垃圾回收。
    例如，您可以定义一个 Finalizer，在删除目标资源前清理相关资源或基础设施。

- Folder, 文件夹, 层级

    为了满足企业内各个部门的分支划分，DCE 引入了[层级](../ghippo/04UserGuide/02Workspace/folders.md)的概念，通常层级对应着不同的部门，每个层级可以包含一个或多个工作空间。

### G

- Garbage Collection, 垃圾回收

    Kubernetes 用于清理集群资源的各种机制的统称。

    Kubernetes 使用垃圾回收机制来清理资源，例如：

    - [未使用的容器和镜像](https://kubernetes.io/docs/concepts/architecture/garbage-collection/#containers-images)
    - [失败的 Pod](https://kubernetes.io//docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection)
    - [目标资源拥有的对象](https://kubernetes.io//docs/concepts/overview/working-with-objects/owners-dependents/)
    - [已完成的 Job](https://kubernetes.io//docs/concepts/workloads/controllers/ttlafterfinished/)
    - 过期或出错的资源

- Gateway node, 网关工作节点

    工作节点主要运行 Envoy 开源应用，主要提供高性能的反向代理能力，支持负载均衡、路由、缓存、自定义路由等功能。
    工作节点的数量和性能将直接影响网关的性能，建议根据需要部署足够的工作节点。

- Gateway, 网关规则

    在服务网格中，[网关规则（Gateway）](../mspider/03UserGuide/02TrafficGovernance/GatewayRules.md)定义了在网格南北向连接操作的负载均衡器，
    用于建立入站和出站的 HTTP/TCP 访问连接。它描述了需要公开的一组端口、服务域名、协议类型、负载均衡器的 SNI 配置等信息。

- Gauge, 计量器

    计量器是一个 **既可增又可减** 的度量指标值。计量器主要用于测量类似于温度、内存使用量这样的瞬时数据。

- GitOps

    GitOps is a set of best practices based on shared principles,
    applied to a workflow that depends on software agents that
    enable automation to reconcile a declared system state or configuration in a git repository.
    These software agents and practices are used to execute a cohesive workflow that
    leverages a source control system like Git as the “single source of truth” and
    extends this practice to applications, infrastructure, and operational procedures.

    Existing processes for infrastructure configuration management can face challenges
    such as configuration drift, failed deployments, relying on a system's previous state for success,
    missing documentation, or unknown development history.
    Adopting a GitOps workflow can help alleviate these issues, among several others.

    GitOps is a paradigm that can be applied to a workflow
    to help manage an application and cloud system infrastructure.
    It enables organizations several advantages
    such as better coordination, transparency, stability, and reliability of a system.
    Operating in a close loop ensures the current live state of a system matches
    against the desired target state, specified in the git repository.

- Global rate limit, 全局限流

    可选择增加网关限流组件，通过限流组件可以支持更多的流量管控能力。
    但是，限流组件也会导致一定的资源消耗和性能损失，默认情况下不启用。请根据实际情况判断是否需要启用。

- Grafana

    Grafana 是一个开源的可视化平台，提供了多样的监控数据可视化面板。

- Group

    在全局管理中，这指的是由多个用户形成的组合，即[用户组](../ghippo/04UserGuide/01UserandAccess/Group.md)。

    在微服务引擎中，这是 Nacos 中的一组配置集。

### H

- Heartbeat, 心跳

    实例启动后每隔一段时间，内置的 Nacos 客户端会主动向 Nacos 服务器发起心跳包（HeartBeat），表示实例仍存活，避免被服务端剔除。
    心跳包包含当前服务实例的名称、IP、端口、集群名称、权重等信息。

- Helm Chart, Helm 模板

    Helm Chart 是一组预先配置的 K8s 资源所构成的包，可以使用 Helm 工具对其进行管理。

    Chart 提供了一种可重现的用来创建和共享 K8s 应用的方法。
    单个 Chart 可用来部署简单的系统（例如 memcached Pod），
    也可以用来部署复杂的系统（例如：HTTP 服务器、数据库、缓存等组件的完整 Web 应用堆栈）。

- Histogram, 直方图

    直方图对观测结果（通常是请求持续时间或者响应大小这样的数据）进行采样，并在可配置的桶中对其进行统计。
    有以下几种方式来产生直方图（假设度量指标为 `<basename>`）：

    - 按桶计数，相当于 `<basename>_bucket{le="<upper inclusive bound>"}`
    - 采样值总和，相当于`<basename>_sum`
    - 采样值总数，相当于 `<basename>_count` ，也等同于把所有采样值放到一个桶里来计数 `<basename>_bucket{le="+Inf"}`

    Histogram 可以理解为柱状图，典型的应用如：请求持续时间，响应大小。可以对观测结果采样，分组及统计。

- Horizontal Pod Autoscaler, HPA, Pod 水平自动扩缩器

    Pod 水平自动扩缩器是一种 API 资源，它根据目标 CPU 利用率或自定义度量目标扩缩 Pod 副本的数量。

    HPA 通常用于 ReplicationController、Deployment 或者 ReplicaSet 上。
    HPA 不能用于不支持扩缩的对象，例如 DaemonSet。

- Horizontal Scaling

    Horizontal scaling is a technique where a system's capacity is increased by adding more nodes
    versus adding more compute resources to individual nodes (the latter being known as vertical scaling).
    Let's say, we have a system of 4GB RAM and want to increase its capacity to 16GB RAM,
    scaling it horizontally means doing so by adding 4 x 4GB RAM rather than switching to a 16GB RAM system.

    This approach enhances the performance of an application by adding new instances, or nodes,
    to better distribute the workload.
    In simple words, it aims to decrease the server's load
    rather than expanding capacity of the individual server.

    As demand for an application grows beyond the current capacity of that application instance,
    we need to find a way to scale (add capacity to) the system.
    We can either add more nodes to the system (horizontal scaling)
    or more compute resources to existing nodes (vertical scaling).

    Horizontal scaling allows applications to scale to whatever limits the underlying cluster provides.
    By adding more instances to the system, the app can process a greater number of requests.
    If a single node can handle 1,000 requests per second,
    each additional node should increase the total number of requests by around 1,000 requests per second.
    This allows the application to do more work concurrently
    without needing to increase the capacity of any node in particular.

- HostAliases, 主机别名

    主机别名是一组 IP 地址和主机名的映射，用于注入到 Pod 内的 host 文件。

    [HostAliases](https://kubernetes.io/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#hostalias-v1-core)
    是一个包含主机名和 IP 地址的可选列表，配置后将被注入到 Pod 内的 hosts 文件中。
    该选项仅适用于没有配置 hostNetwork 的 Pod。

- Hypervisor

    A hypervisor enables virtualization by taking the advantage of bare metal machine resources
    (CPU, Memory, Network, and Storage), dividing them into sub-parts,
    and allocating resources accordingly to create virtual machines (VM)
    until the underlying host reaches its performance limits.

    Traditionally, a server could only run applications of a single operating system.
    The process of acquiring software takes time. It requires infrastructure with a specific environment
    and a team of engineers to manage and monitor them.
    Servers were underutilized, considering the computing power of a server it can run multiple operating systems and more applications.
    Running applications on bare metal wasn't enough to match the needs of fluctuating traffic.

    In the context of cloud computing, the hypervisor becomes an effective tool.
    In contrast to the traditional method of creating a virtual machine, a hypervisor makes the process much simpler and faster.
    Hardware resources are logically partitioned and assigned to the VMs keeping them isolated as distinct units,
    ensuring they function independently so that issues on one don't affect the others,
    and allowing VMs to install any necessary operating system.
    A hypervisor is an abstraction over the physical hardware, it takes care of those low-level complexities of managing the VMs and monitoring them,
    making VMs loosely bound to hardware, enabling organizations to migrate their applications to the remote servers/cloud
    and autoscale their services.
    Over time, the use of this multi-tenant software has reduced computing costs.

### I

- IAM, Identity and access management, 用户与访问控制

    在全局管理中，[IAM](../ghippo/04UserGuide/01UserandAccess/iam.md) 是用户与访问控制的简称，管理员被称为 IAM Admin，拥有该模块的最高权限。
    被赋予 IAM Admin 的用户（用户组）将拥有用户与访问控制的全部且最高权限。

- Image, 镜像

    [镜像](https://kubernetes.io/docs/concepts/containers/images/)是保存的容器实例，它打包了应用运行所需的一组软件。

    镜像是软件打包的一种方式，可以将镜像存储在容器镜像仓库、拉取到本地系统并作为应用来运行。
    镜像中包含的元数据指明了运行什么可执行程序、是由谁构建的以及其他信息。

- Immutable Infrastructure

    Immutable Infrastructure refers to computer infrastructure (virtual machines, containers, network appliances)
    that cannot be changed once deployed.
    This can be enforced by an automated process that overwrites unauthorized changes or
    through a system that won't allow changes in the first place.
    Containers are a good example of immutable infrastructure
    because persistent changes to containers can only be made by
    creating a new version of the container or recreating the existing container from its image.

    By preventing or identifying unauthorized changes,
    immutable infrastructures make it easier to identify and mitigate security risks.
    Operating such a system becomes a lot more straightforward
    because administrators can make assumptions about it.
    After all, they know no one made mistakes or changes they forgot to communicate.
    Immutable infrastructure goes hand-in-hand with infrastructure as code
    where all automation needed to create infrastructure is stored in version control (e.g. Git).
    This combination of immutability and version control means that
    there is a durable audit log of every authorized change to a system.

- Infrastructure as a service

    Infrastructure as a service, or IaaS, is a cloud computing service model that offers physical or virtualized
    compute, storage, and network resources on-demand on a pay-as-you-go model.
    Cloud providers own and operate the hardware and software,
    available to consumers in public, private, or hybrid cloud deployments.

    In traditional on-premise setups, organizations often struggle with effective computing resource usage.
    Data centers have to be built for potential peak demand, even if it's only needed 1% of the time.
    During lower demand, these compute resources are idle.
    And, if the workload spikes beyond the expected demand,
    there is a shortage of computing resources to process the workload.
    This lack of scalability leads to increased costs and ineffective resource usage.

    With IaaS organizations can avoid purchasing and maintaining compute and data center space for their applications.
    An on-demand infrastructure allows them to rent compute resources as needed and
    defer large capital expenditures, or [CAPEX](https://en.wikipedia.org/wiki/Capital_expenditure),
    while giving them the flexibility to scale up or down.

    IaaS reduces the upfront costs of experimenting or trying a new application and
    provides facilities to rapidly deploy infrastructure.
    A cloud provider is an excellent option for development or test environments,
    which helps developers experiment and innovate.

- Infrastructure as code

    Infrastructure as code is the practice of storing the definition of infrastructure as one or more files.
    This replaces the traditional model where infrastructure as a service is provisioned manually,
    usually through shell scripts or other configuration tools.

    Building applications in a cloud native way requires infrastructure to be disposable and reproducible.
    It also needs to scale on-demand in an automated and repeatable way, potentially without human intervention.
    Manual provisioning cannot meet the responsiveness and scale requirements of cloud native applications.
    Manual infrastructure changes are not reproducible, quickly run into scale limits, and introduces misconfiguration errors.

    By representing the data center resources such as servers, load balancers, and subnets as code,
    it allows infrastructure teams to have a single source of truth for all configurations and
    also allows them to manage their data center in a CI/CD pipeline,
    implementing version control and deployment strategies.

- Ingress, 路由

    [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
    是对集群中服务的外部访问进行管理的 API 对象，典型的访问方式是 HTTP。

    Ingress 可以提供负载均衡、SSL 终结和基于名称的虚拟托管。

- Init Container, [Init 容器](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)

    应用容器运行前必须先运行完成的一个或多个 Init 容器。

    Init 容器像常规应用容器一样，只有一点不同：Init 容器必须在应用容器启动前运行完成。
    Init 容器的运行顺序：一个 Init 容器必须在下一个 Init 容器开始前运行完成。

- Istio

    [Istio](https://istio.io/) 是一个免费开源的服务网格，提供了一种统一的方式来集成微服务、管理流量、实施策略和汇总度量数据。

    添加 Istio 时不需要修改应用代码。它是基础设施的一层，介于服务和网络之间。
    当它和服务的 Deployment 相结合时，就构成了通常所谓的服务网格（Service Mesh）。
    Istio 的控制面抽象掉了底层的集群管理平台，这一集群管理平台可以是 Kubernetes、Mesosphere 等。

### J, K

- [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/)

    [Job](../kpanda/07UserGuide/Workloads/CreateJobByImage.md) 是需要运行完成的确定性的或批量的任务。

    创建一个或多个 Pod 对象，并确保指定数量的 Pod 成功终止。
    随着各 Pod 成功结束，Job 会跟踪记录成功完成的个数。

- Kops

    [Kops](https://kubernetes.io/docs/setup/production-environment/tools/kops/)
    是一个命令行工具，可以帮助您创建、销毁、升级和维护生产级，高可用性的 Kubernetes 集群。
    Kops 目前仅支持 AWS。对 GCE、VMware vSphere 及其他第三方 PaaS 平台的支持还处于 Alpha 阶段。

    您也可以将自己的集群作为一个构造块，使用 kubeadm 构造集群。
    `kops` 是建立在 kubeadm 之上的。

- kube-apiserver, k8s API 服务器

    [kube-apiserver](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/)
    是提供 Kubernetes API 服务的控制面组件。
    Kubernetes API 服务器验证并配置 API 对象的数据，这些对象包括 Pod、Service、replicationcontroller 等。
    API 服务器为 REST 操作提供服务，并为集群的共享状态提供前端， 所有其他组件都通过该前端进行交互。

    API 服务器是 Kubernetes 控制平面的组件，该组件负责公开了 Kubernetes API，负责处理接受请求的工作。
    API 服务器是 Kubernetes 控制平面的前端。

    Kubernetes API 服务器的主要实现是 [kube-apiserver](https://kubernetes.io//docs/reference/command-line-tools-reference/kube-apiserver/)。
    `kube-apiserver` 设计上考虑了水平扩缩，也就是说，它可通过部署多个实例来进行扩缩。
    您可以运行 `kube-apiserver` 的多个实例，并在这些实例之间平衡流量。

- kube-controller-manager

    [kube-controller-manager](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/)
    是一个守护进程，是 Master 节点上运行控制器的组件，负责运行控制器进程。

    从逻辑上讲，每个控制器都是一个单独的进程，
    但是为了降低复杂性，它们都被编译到同一个可执行文件，并在同一个进程中运行。

- kube-proxy

    [kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/)
    是集群中每个节点上运行的网络代理，是实现 Kubernetes Service 概念的组成部分。

    kube-proxy 维护节点上的一些网络规则，这些网络规则会允许从集群内部或外部的网络会话与 Pod 进行网络通信。

    如果操作系统提供了可用的数据包过滤层，则 kube-proxy 会通过它来实现网络规则。否则，kube-proxy 仅做流量转发。

- [kube-scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/)

    这是一个控制平面组件，负责监视新创建的、未指定运行节点的 Pod，选择节点让 Pod 在上面运行。

    调度决策考虑的因素包括单个 Pod 及 Pods 集合的资源需求、软硬件及策略约束、亲和性及反亲和性规范、数据位置、工作负载间的干扰及最后时限。

- [Kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/)

    用来快速安装 Kubernetes 并搭建安全稳定的集群的工具。您可以使用 Kubeadm 安装控制面和工作节点组件。

- kubectl

    [kubectl](https://kubernetes.io/docs/reference/kubectl/) 是用来和 Kubernetes 集群进行通信的命令行工具。
    您可以使用 `kubectl` 创建、检视、更新和删除 Kubernetes 对象。

- kubelet

    一个在集群中每个节点上运行的代理。它保证容器都运行在 Pod 中。

    [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/)
    接收一组通过各类机制提供给它的 PodSpecs，确保这些 PodSpecs 中描述的容器处于运行状态且健康。
    kubelet 不会管理不是由 Kubernetes 创建的容器。

- Kubernetes, K8s

    Kubernetes, often abbreviated as K8s, is an open source container orchestrator.
    It automates the lifecycle of containerized applications on modern infrastructures, functioning as a "datacenter operating system" that manages applications across a distributed system.

    Kubernetes schedules containers across nodes in a cluster, bundling several infrastructure resources such as load balancer, persistent storage, etc. to run containerized applications.

    Kubernetes enables automation and extensibility, allowing users to deploy applications declaratively (see below) in a reproducible way. 
    Kubernetes is extensible via its API, allowing experienced Kubernetes practitioners to leverage its automation capabilities according to their needs.

    Infrastructure automation and declarative configuration management have been important concepts for a long time, but they have become more pressing as cloud computing has gained popularity.
    As demand for compute resources increases and organizations need to provide more operational capabilities with fewer engineers, new technologies and working methods are required to meet that demand.

    Similar to traditional infrastructure as code tools, Kubernetes helps with automation but has the advantage of working with containers. 
    Containers are more resistant to configuration drift than virtual or physical machines.

    Additionally, Kubernetes works declaratively, which means that instead of operators instructing the machine how to do something, they describe — usually as manifest files (e.g., YAML) — what the infrastructure should look like.
    Kubernetes then takes care of the "how".
    This results in Kubernetes being extremely compatible with infrastructure as code.

    Kubernetes also self-heals.
    The cluster's actual state will always match the operator's desired state.
    If Kubernetes detects a deviation from what is described in the manifest files, a Kubernetes controller kicks in and fixes it. 
    While the infrastructure Kubernetes uses may be continually changing, Kubernetes constantly and automatically adapts to changes and ensures that it matches with the desired state.

- Kubernetes API

    [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/)
    是通过 RESTful 接口提供 Kubernetes 功能服务并负责集群状态存储的应用程序。

    Kubernetes 资源和"意向记录"都是作为 API 对象储存的，并可以通过调用 RESTful 风格的 API 进行修改。
    API 允许以声明方式管理配置。
    用户可以直接和 Kubernetes API 交互，也可以通过 `kubectl` 这样的工具进行交互。
    核心的 Kubernetes API 是很灵活的，可以扩展以支持定制资源。

### L

- Label, 标签

    用来为对象设置可标识的属性标记；这些标记对用户而言是有意义且重要的。

    标签是一些关联到 Pod 这类对象上的键值对。它们通常用来组织和选择对象子集。

- LimitRange

    提供约束来限制命名空间中每个容器或 Pod 的资源消耗。

    LimitRange 按照类型来限制命名空间中对象能够创建的数量，以及单个 容器（Containers）或 Pod 可以请求/使用的计算资源量。

- Load Balancer, 负载均衡器

    负载均衡器是一种在后端的一组服务器之间分配传入网络流量的方法。
    该解决方案可以是基于软件或硬件的。

    这有助于解决与高可用性和分布式系统相关的问题。
    在处理需要扩展到数十万用户的应用程序或服务时，通常需要将该应用程序分布在多个服务器上。
    负载均衡器是路由流量的“交通警察”。

    负载均衡器将充当网络流量和客户端的前端。
    它通常有多种方法来检查哪些服务器已启动并且处理请求的负载最低。

- [Log](https://opentelemetry.io/docs/concepts/signals/logs/), 日志

    在 Insight 中，[日志](../insight/user-guide/04dataquery/logquery.md)是集群或应用程序记录的事件列表。
    系统运行过程中变化的一种抽象数据，其内容为指定对象的操作和其操作结果按时间的有序集合。

    应用程序和系统日志可以帮助您了解集群内部发生的情况。日志对于调试问题和监视集群活动非常有用。

- Loosely coupled architecture, 松耦合架构

    松耦合架构（紧耦合架构的相反范式）是一种架构风格，其中应用程序的各个组件彼此独立构建。
    每个组件，有时称为微服务，都是为了执行特定功能而构建的，以便被任意数量的其他服务使用。
    这种模式的实现通常比紧耦合架构慢。但有许多好处，特别是随着应用程序的不断扩展。
    松耦合的应用程序允许团队独立开发功能、部署和扩展，这允许组织快速迭代各个组件。
    应用程序开发速度更快，团队结构可以围绕应用程序的能力构建，专注于他们的特定应用程序。

### M

- Managed Control Plane, 托管控制平面

    托管控制平面是一个为客户提供管理的控制平面。
    托管控制平面降低了用户部署的复杂性，并通常保证一定水平的性能和可用性。

- Managed Mesh, 托管网格

    由服务网格在所选集群创建并托管的控制平面。具备简单、低成本、高可用、无需单独运维管理 的特点。

- Managed Service, 托管服务

    托管服务是一种软件产品，其运营和管理由第三方负责。
    例如类似 Amazon RDS 的数据库即服务或类似 Datadog 的外部监控服务。

    软件的管理比较复杂，尤其是要考虑现代技术栈所包含的各种不同技术。
    而想要将管理做到面面俱到并招募能胜任此职的内部专家，要么成本过于高昂，要么会耗用工程师的宝贵时间。
    您的团队应投入精力构建新功能，而不是处理可以通过外包就能轻松解决的运营任务。

    托管服务从一开始就处于使用就绪状态，运营开销非常小。
    托管服务具备良好定义的、通常由 API 驱动的边界，
    便于各个组织将超出其核心竞争力的任务有效外包出去。

- Manifest, 清单

    一个或多个 Kubernetes API 对象的序列化规范。

    清单指定了在应用该清单时 kubernetes 将维护的对象的期望状态。每个配置文件可包含多个清单。

- Master cluster, 主集群

    主集群是具有控制平面的集群。
    一个网格可以有一个以上的主集群，以用于 HA 或需要低延迟的场景。
    主集群可以充当工作集群的控制平面。

- [Metric](https://opentelemetry.io/docs/concepts/signals/metrics/), [指标](../insight/user-guide/04dataquery/metricquery.md)

    对资源性能的数据描述或状态描述，指标由命名空间、维度、指标名称和单位组成。
    采集目标暴露的、可以完整反映监控对象运行或者业务状态的一系列标签化数据。

- Metadata, 元数据

    元数据是数据本身的描述信息，是关于数据的数据，例如服务版本、各种自定义标签等。
    元数据分为服务级别的元数据、集群的元数据及实例的元数据。

- Microservice, 微服务

    微服务是一种通过多个小型服务组合来构建单个应用的架构风格。
    在微服务引擎中，微服务指将一个完整的应用根据业务功能拆分而得到的各个小型服务。

    微服务是一种利用云原生技术进行应用开发的现代方法。
    虽然现代应用程序，如 Netflix，看起来是一个单一的应用程序，但它们实际上是一个较小的服务的集合——所有的服务都密切配合。
    例如，一个允许您访问、搜索和预览视频的单一页面很可能是由较小的服务提供的，它们各自处理其中的一个方面（如搜索、认证和在浏览器中运行预览）。
    简而言之，微服务指的是一种应用架构模式，通常与单体应用形成对比。

    微服务是对单体应用所带来的挑战的一种回应。一般来说，一个应用程序的不同部分需要分别进行扩缩。
    例如，一个在线商店将有更多的产品视图而不是结账。这意味着您需要更多的产品视图功能的运行，而不是结账。
    在一个单一的应用程序中，这些逻辑位不能被单独部署。
    如果您不能单独扩展产品功能，您将不得不复制整个应用程序和所有其他您不需要的组件：这是一种低效的资源利用。
    单机式应用程序也使开发人员容易屈服于设计陷阱。
    因为所有的代码都在一个地方，所以更容易使这些代码高耦合，更难执行关注点分离的原则。
    单机通常要求开发人员了解整个代码库，然后才能有成效。

    将功能分离成不同的微服务，使它们更容易独立部署、更新和扩展。
    通过允许不同的团队专注于更大的应用中他们自己的一小部分，也让他们更容易在不对组织的其他部分产生负面影响的情况下对他们的应用进行工作。
    虽然微服务解决了许多问题，但它们也产生了运营开销：您需要部署和跟踪的东西增加了一个数量级或更多。
    许多云原生技术旨在使微服务更容易部署和管理。

- Microservice instance, 微服务实例

    将同一个微服务部署在多个容器或虚拟机上，每个容器或虚拟机上运行的微服务副本就是一个微服务实例。
    多个微服务实例可以同时运行。

- Microservice instance group, 微服务实例分组

    将同一个微服务下的所有微服务实例按照需求进一步划分得到的分组。

- Monolithic Apps, 单体应用

    单体应用在一个简单可部署的程序中包含所有的功能。
    在制作一个应用程序时，这通常是最简单和最容易的开始。
    然而，一旦应用程序的复杂性增加，单体式就会变得难以维护。
    随着更多的开发人员在同一个代码库上工作，发生冲突性变化的可能性和开发人员之间的人际沟通的需要就会增加。

    将一个应用程序转变成微服务会增加其运营开销——有更多的东西需要测试、部署和保持运行。
    在产品生命周期的早期，推迟这种复杂性并建立一个单体应用，直到产品被确定为成功，可能是有利的。

    精心设计的单体可以坚持精益原则，因为它是启动和运行应用程序的最简单方式。
    当单体应用的商业价值被证明是成功的，它可以被分解成微服务。
    在证明有价值之前，制作一个基于微服务的应用程序可能是过早地花费了工程努力。
    如果应用程序没有产生任何价值，这些努力就会被浪费掉。

- Multitenancy, 多租户模式

    多租户模式指的是通过单次软件安装为多个租户提供服务。
    租户是一个用户、应用程序或一组用户/应用程序，租户们使用各自的数据集来操控同一个软件。
    这些租户不共享数据（除非软件的所有者明确授权），甚至可能未意识到彼此的存在。

    租户可以是小到只有一个登录 ID 的独立用户（就像单机版软件），
    也可以是大到拥有数千个登录 ID 的整个公司，其中每个登录 ID 有自己的权限但又以多种方式相互关联。
    多租户软件示例包括 Google Mail、Google Docs、Microsoft Office 365、Salesforce CRM 和 Dropbox，
    以及更多归类为具有完全或部分多租户能力的软件。

    如果没有多租户模式，每个租户都需要专门安装一次软件。
    这会增加资源利用和维护的工作量，最终会加剧软件成本。

    多租户软件为每个租户提供一个隔离（工作数据、设置、凭证列表等）的环境，同时为多个租户提供服务。
    从租户的角度来看，每个租户都有其专用的软件安装实例，尽管实际上他们是在共享同一个软件。
    具体实现的方式为：在服务器上运行一个软件，然后允许租户通过网络接口和/或 API 连接到该软件。
    使用多租户软件时，各个租户可以共享同一个安装实例，彼此毫无影响，且能以预先定义和受控的方式使用该软件。
    软件提供商由此达成的资源节省也可以转而让租户受益，显著降低每个用户的软件成本（想想基于 Web 的电子邮件或文档编辑器）。

- Mutual Transport Layer Security, mTLS, 双向传输层安全性协议

    双向 TLS (mTLS) 是一种用于对两个服务之间发送的消息进行身份验证和加密的技术。
    双向 TLS (mTLS) 是标准的传输层安全性协议 (TLS)，但不是仅验证一个连接的身份，而是验证双方。

    微服务通过网络进行通信，就像您的 WiFi 网络一样，通过该网络传输的通信可能会被黑客入侵。
    mTLS 确保没有未经授权的一方监听或冒充合法请求。

    mTLS 确保客户端和服务器之间的双向流量是安全和可信的，
    为进入网络或应用程序的用户提供了额外的安全层。
    它还验证不遵循登录过程的客户端设备连接，例如物联网 (IoT) 设备。
    mTLS 可以防止诸如路径上的攻击、欺骗攻击、凭证填充、暴力攻击等攻击。

### N

- Nacos 集群节点角色

    这是[微服务引擎](../skoala/intro/features.md)中节点在 Raft 协议中的角色。Raft 是一种实现分布式共识的协议，即如何让多个节点达成一致。

    **Leader** 是所有请求的处理者，负责接收客户端发起的操作请求，将请求写入本地日志并向其他节点同步请求日志。
    任何时候最多只能有一个 Leader。

    **Follower** 是 Leader 的跟随者，负责从 Leader 接收更新请求并将其写入本地日志，并在 Leader 通知可以提交日志时提交日志。

- Name, 名称

    客户端提供的字符串，用来指代资源 URL 中的对象，如 `/api/v1/pods/some-name`。

    某一时刻，只能有一个给定类型的对象具有给定的名称。但是，如果删除该对象，则可以创建同名的新对象。

- Namespace, 命名空间

    [命名空间](../kpanda/07UserGuide/Namespaces/createns.md)是 Kubernetes 用来支持隔离单个集群中的资源组的一种抽象。

    命名空间用来组织集群中对象，并为集群资源划分提供了一种方法。
    同一命名空间内的资源名称必须唯一，但跨命名空间时不作要求。
    基于命名空间的作用域限定仅适用于命名空间作用域的对象（例如 Deployment、Services 等），
    而不适用于集群作用域的对象（例如 StorageClass、Node、PersistentVolume 等）。
    在一些文档里命名空间也称为命名空间。

    在微服务引擎中，命名空间指的是 Nacos 命名空间，主要用于实现租户层级的配置隔离，例如隔离开发环境、测试环境、生产环境的资源配置。

- Network Policy, 网络策略

    网络策略是一种规范，规定了允许 Pod 组之间、Pod 与其他网络端点之间以怎样的方式进行通信。

    网络策略帮助您声明式地配置允许哪些 Pod 之间、哪些命名空间之间允许进行通信，
    并具体配置了哪些端口号来执行各个策略。`NetworkPolicy` 资源使用标签来选择 Pod，
    并定义了所选 Pod 可以接受什么样的流量。网络策略由网络提供商提供的并被 Kubernetes 支持的网络插件实现。
    请注意，当没有控制器实现网络资源时，创建网络资源将不会生效。

- Node, 节点

    [节点](../kpanda/07UserGuide/Nodes/AddNode.md)是一台能与其他计算机（或节点）协同工作以完成一个共同任务的计算机。
    以您的笔记本电脑、调制解调器或打印机为例。它们都通过您的 wifi 网络进行通信和协作，各自代表一个节点。
    在云计算中，节点可以是一台物理机，也可以是一台虚拟机（即 VM），甚至可以是容器。

    虽然一个应用程序可以（很多应用程序确实是）运行在一台独立的机器上，但这样做存在一些风险。也就是说，底层系统的故障将会破坏应用程序。
    为了解决这个问题，开发人员开始创建分布式应用程序，其中每个进程都在自己的节点上运行。
    因此，节点作为集群或节点组的一部分运行着应用程序或进程，而这些节点一起工作以实现共同的目标。

    节点为您提供了一个可以分配给集群的独特计算单元（内存、CPU、网络）。
    在云原生平台或应用程序中，一个节点代表一个可执行工作的单元。
    理想情况下，单个节点是不作区分的，因为任何特定类型的节点与其相同类型的节点应该是不可区分的。

- Node Pressure Eviction, 节点压力驱逐

    节点压力驱逐是 kubelet 主动使 Pod 失败以回收节点上的资源的过程。

    kubelet 监控集群节点上的 CPU、内存、磁盘空间和文件系统 inode 等资源。
    当这些资源中的一个或多个达到特定消耗水平时，
    kubelet 可以主动使节点上的一个或多个 Pod 失效，以回收资源并防止饥饿。

    节点压力驱逐不用于 [API 发起的驱逐](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/)。

- Notification, 通知

    当资源存在异常而产生告警时，可将告警信息通过邮件、钉钉、企业微信、webhook 等方式发送给指定的用户。

### O

- Object, 对象

    Kubernetes 系统中的实体，代表了集群的部分状态。Kubernetes API 用这些实体表示集群的状态。

    Kubernetes 对象通常是一个“目标记录”。
    一旦您创建了一个对象，Kubernetes 控制平面就会持续工作，确保该对象所代表的项目切实存在。
    创建一个对象相当于告知 Kubernetes 系统：您期望这部分集群负载看起来像什么；这也就是您集群的期望状态。

- Objective, 目标

    Prometheus 抓取的采集目标。采集目标暴露自身状态，或者代理暴露监控对象的运行、业务指标。

- Observability, 可观测性

    [可观测性](../insight/intro/WhatisInsight.md)指的是从所观测的系统采集信号，持续生成并发现可执行的洞察力。
    换言之，可观测性允许用户从某个系统的外部输出中洞察该系统的状态并采取（修正）措施。

    计算机系统的衡量机制为观测 CPU 时间、内存、磁盘空间等底层信号以及每秒
    API 响应次数、每秒错误率、每秒处理的事务数等高级信号和业务信号。

    系统的可观测性对其运营和开发成本有重大影响。
    可观测系统为操作人员提供了有意义的、可执行的数据，使他们能够达成有利的结果
    （即更快的事件响应、更高的开发效率）以及更少的艰辛时刻和更短的停机时间。

    请注意，更多的信息并不一定能转化为可观测性更好的系统。
    事实上，有时系统生成的大量信息会形成信息噪音，会使得鉴别有价值的健康信号变得更加困难。
    可观测性需要在合适的时间为合适的消费者（一个人或一个软件）提供合适的数据，从而做出合适的决策。

- Operator

    Operator 是打包，部署和管理 Kubernetes 应用程序的一种方法。

- Operator Pattern, Operator 模式

    一种用于管理自定义资源的专用控制器。
    [Operator 模式](https://kubernetes.io//docs/concepts/extend-kubernetes/operator/)是一种系统设计，将控制器关联到一个或多个自定义资源。

    除了使用作为 Kubernetes 自身一部分的内置控制器之外，您还可以通过将控制器添加到集群中来扩展 Kubernetes。

    如果正在运行的应用程序能够充当控制器并通过 API 访问的方式来执行任务操控那些在控制平面中定义的自定义资源，这就是一个 Operator 模式的示例。

- OverridePolicy, 差异化策略

    [差异化策略](../kairship/07policy/overridepolicy.md)是定义多云资源对象分发到不同工作集群时的差异化配置策略，
    例如在不同的工作集群中，可以使用不同的镜像，增加不同的标签等。

    OverridePolicy 作为一个独立的策略 API 能够自动处理集群相关的配置，例如：

    - 根据子集群的地域分布自动为镜像添加不同的前缀
    - 根据您的云提供商使用不同的 StorageClass

### P

- Permission, 权限

    [权限](../ghippo/04UserGuide/01UserandAccess/iam.md)指是否允许用户对某种资源执行某种操作。
    为了降低使用门槛，DCE 采用 RBAC 模型将权限聚合成一个个角色，管理员只需要将角色授权给用户，该用户就一次性得到了该角色下聚合的一组权限。

    默认情况下，管理员创建的 IAM 用户没有任何角色权限，需要对其单独授予角色或将其加入用户组并给用户组授予角色，才能使得用户获得对应的角色权限，这一过程称为授权。授权后，用户就可以基于被授予的角色权限对平台资源进行操作。

- Persistent Volume Claim, PVC, 持久卷申领

    申领在持久卷中定义的存储资源，以便可以将其挂载为容器中的卷。

    指定存储的数量，如何访问存储（只读、读写或独占）以及如何回收存储（保留、回收或删除）。
    存储本身的详细信息在 PersistentVolume 对象中。

- Persistent Volume, PV, 持久卷

    持久卷是代表集群中一块存储空间的 API 对象。它是通用的、可插拔的、并且不受单个 Pod 生命周期约束的持久化资源。

    持久卷提供了一个 API，该 API 对存储的供应方式细节进行抽象，令其与使用方式相分离。
    在提前创建存储（静态供应）的场景中，PV 可以直接使用。
    在按需提供存储（动态供应）的场景中，需要使用 PersistentVolumeClaims (PVC)。

- Platform as a service, PaaS, 平台即服务

    平台即服务（PaaS）是应用程序开发团队部署和运行其应用程序的外部平台。
    Heroku、Cloud Foundry、App Engine 是 PaaS 产品的示例。

    要利用好微服务或分布式应用程序等云原生模式，
    运维团队和开发人员需要能够免去大量运维工作，其中包括供应基础设施、处理服务发现和负载平衡以及扩展应用程序等任务。

    平台即服务（PaaS）以完全自动化的方式为应用程序开发人员提供通用基础设施工具。
    它使开发人员可以了解基础设施并减少对基础设施的担忧，并将更多的时间和精力用于编写应用程序代码。
    它还提供了一些监控和可观测性来帮助应用程序团队确保他们的应用程序是健康的。

- Pilot

    Pilot 是服务网格里的一个组件，它控制 Envoy 代理，负责服务发现、负载均衡和路由分发。

- Pod

    Pod 表示集群上正在运行的一组容器。Pod 是 Kubernetes 的原子对象，是 Kubernetes 部署的一个工作负载实例。

    通常创建 Pod 是为了运行单个主容器。
    Pod 还可以运行可选的边车（sidecar）容器，以添加诸如日志记录之类的补充特性。
    通常用 Deployment 来管理 Pod。

    Pod 中包含了一个或多个共享存储和网络的容器以及如何运行容器的规约。

- Pod Disruption Budget, PDB

    Pod Disruption Budget 是这样一种对象：它保证在主动干扰（voluntary disruptions）时，多实例应用的 Pod 不会少于一定的数量。

    PDB 无法防止非主动的干扰，但是会计入预算（budget）。

- Pod Disruption, Pod 干扰

    主动或非主动地终止节点上的 Pod 的过程。

    主动干扰是由应用程序所有者或集群管理员有意启动的。非主动干扰是无意的，
    可能由不可避免的问题触发，如节点耗尽资源或意外删除。

- Pod Lifecycle, Pod 生命周期

    关于 Pod 在其生命周期中处于哪个阶段的更高层次概述。

    [Pod 生命周期](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)是关于 Pod
    处于哪个阶段的概述。包含了下面 5 种可能的阶段：

    - Running
    - Pending
    - Succeeded
    - Failed
    - Unknown

    关于 Pod 的阶段的更高级描述请查阅
    [PodStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podstatus-v1-core) `phase` 字段。

- Pod Priority, Pod 优先级

    Pod 优先级表示一个 Pod 相对于其他 Pod 的重要性。

    [Pod 优先级](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#pod-priority)允许用户为
    Pod 设置高于或低于其他 Pod 的优先级，这对于生产集群工作负载而言是一个重要的特性。

- Pod Security Policy, Pod 安全策略

    为 Pod 的创建和更新操作启用细粒度的授权。

    Pod 安全策略是集群级别的资源，它控制着 Pod 规约中的安全性敏感的内容。
    `PodSecurityPolicy` 对象定义了一组条件以及相关字段的默认值，Pod
    运行时必须满足这些条件。Pod 安全策略控制实现上体现为一个可选的准入控制器。

    PodSecurityPolicy 已于 Kubernetes v1.21 起弃用，并在 v1.25 中删除。
    作为替代方案，请使用 [Pod 安全准入](https://kubernetes.io/docs/concepts/security/pod-security-admission/)或第三方准入插件。

- Policy as code, PaC, 策略即代码

    策略即代码是将一些策略的定义存储为一个或多个机器可读和可处理格式文件的做法。
    这取代了在传统模型中，以人类可读的形式记录在单独文档中的策略。

    构建应用和基础设施通常受到某组织所定义的许多策略的约束，
    例如禁止在源代码中存储 Secret、禁止以超级用户权限运行容器或禁止将某些数据存储在特定地理区域之外的安全策略。
    对于开发人员和审查人员来说，按照策略文档手动检查应用和基础设施既耗时费力又容易出错。
    手动检查策略无法满足云原生应用的响应要求和扩缩要求。

    通过使用策略即代码，可以自动检查系统属性和操作。
    软件开发的最佳实践也适用于构建策略即代码，例如使用 Git 及相关工作流。

- Portability, 可移植性

    可移植性是一种软件特征，一种可重用性的形式，有助于避免“锁定”到某些操作环境，
    例如云提供商、操作系统或供应商。

    传统软件通常是为特定环境（例如 AWS 或 Linux）构建的。
    而可移植软件可以在不同的操作环境中工作，无需大量返工。
    如果应用适配新环境所需的工作量在合理范围内，则该应用被认为是可移植的。
    “移植”这个词意味着修改软件并使其适应在不同的计算机系统上工作。

- Preemption, 抢占

    Kubernetes 中的抢占逻辑通过驱逐节点上的低优先级 Pod 来帮助悬决的 Pod 找到合适的节点。

    如果一个 Pod 无法调度，调度器会尝试[抢占](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#preemption)较低优先级的 Pod，以使得悬决的 Pod 有可能被调度。

- Prometheus

    Prometheus 是一套开源的监控、报警、时间序列数据库的组合。

- PromQL

    Prometheus 内置的数据查询语言，其提供对时间序列数据丰富的查询，聚合以及逻辑运算能力的支持。

- PropagationPolicy, 部署策略

    在多云编排中，[PropagationPolicy](../kairship/07policy/propagationpolicy.md) 是定义多云资源对象的分发策略，支持使用指定集群、指定标签等方式来规划将资源部署到哪些工作集群。

    PropagationPolicy 是一种独立的策略 API，可以根据分发要求来定义多集群调度方式。

    - 支持 1:n 的`策略:工作负载`，用户每次创建多云应用时无需重复指出调度的约束条件。
    - 采用默认的策略时，用户可以直接与 Kubernetes API 交互。

- Proxy, 代理

    在计算机领域，代理指的是充当远程服务中介的服务器。

    客户端与代理进行交互；代理将客户端的数据复制到实际服务器；实际服务器回复代理；代理将实际服务器的回复发送给客户端。

    [kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/)
    是集群中每个节点上运行的网络代理，实现了部分 Kubernetes Service 概念。

    您可以将 kube-proxy 作为普通的用户态代理服务运行。
    如果您的操作系统支持，则可以在混合模式下运行 kube-proxy；该模式使用较少的系统资源即可达到相同的总体效果。

### R

- RBAC, Role-Based Access Control, 基于角色的访问控制

    管理授权决策，允许管理员通过 Kubernetes API 动态配置访问策略。

    RBAC 使用[角色](../ghippo/04UserGuide/01UserandAccess/Role.md) (包含权限规则）和角色绑定（将角色中定义的权限授予一个用户组）。

- Registration center, 注册中心

    注册中心相当于微服务架构中的“通讯录”，负责记录服务和服务地址的映射关系。
    微服务引擎支持的注册中心类型有：Eureka、Zookeeper、Nacos、Mesh、Kubernetes。

- Reliability, 可靠性

    从云原生的角度来看，可靠性是指系统对故障的响应能力。
    如果我们有一个可以在基础架构更改和单个组件发生故障时继续工作的分布式系统，那么它是可靠的。
    另一方面，如果它很容易出现故障，并且需要操作人员手动干预以保持其运行，则它是不可靠的。
    云原生应用的目标是构建内在可靠的系统。

- ReplicaSet

    ReplicaSet 是下一代副本控制器。

    ReplicaSet 就像 ReplicationController 那样，确保一次运行指定数量的 Pod 副本。
    ReplicaSet 支持新的基于集合的选择器需求（在标签的用户指南中有相关描述），而副本控制器只支持基于等值的选择器需求。

- Replication Controller, 副本控制器

    一种管理多副本应用的（已弃用）的 API 对象。

    一种工作管理多副本应用的负载资源，能够确保特定个数的 Pod 实例处于运行状态。

    控制面确保所指定的个数的 Pods 处于运行状态，即使某些 Pod 会失效，
    比如被您手动删除或者因为其他错误启动过多 Pod 时。

    ReplicationController 已被弃用。请参阅 Deployment 执行类似功能。

- Resource, 资源

    资源泛指 DCE 平台上通过各个子模块创建的资源，是完成授权的具体数据。
    通常资源描述一个或多个操作对象，每个子模块拥有其各自的资源和对应的资源定义详情，如集群、Namesapce、网关等。

    资源的拥有者是主账号 Super Admin。
    Super Admin 具有在各子模块创建/管理/删除资源的权限。
    普通用户在没有授权的情况下，不会自动拥有资源的访问权限，需要 Super Admin 进行授权。
    工作空间支持跨子模块授权用户（用户组）对于资源的访问权限。

- Resource limit, 资源限制值

    限制值是实例的可用资源上限。请求值小于限制值。

- Resource Quota, 资源配额

    [资源配额](../ghippo/04UserGuide/02Workspace/quota.md)提供了限制每个命名空间的资源消耗总和的约束。

    限制了命名空间中每种对象可以创建的数量，也限制了项目中可被资源对象利用的计算资源总数。

- Resource request, 资源请求值

    请求值规定了为实例预先分配多少可用资源。

- Resource Template, 资源模板

    在[多云编排](../kairship/01product/whatiskairship.md)中采用了一种叫做联邦资源的模板，
    这是基于 K8s 原生 API 定义的一种多云资源模板，便于集成使用 K8s 生态范围内的所有云原生工具。

    通过这种资源模板可以统一管理[多云服务](../kairship/06resource/service.md)、
    [多云命名空间](../kairship/06resource/ns.md)、
    [多云配置项](../kairship/06resource/configmap.md)和[多云密钥](../kairship/06resource/secret.md)。

- Role, 角色

    [角色](../ghippo/04UserGuide/01UserandAccess/Role.md)是连接用户与权限的桥梁，
    一个角色对应一组权限，不同角色具有不同的权限。向用户授予某角色，即授予该角色所包含的所有权限。
    全局管理中有两种角色：

    - 预定义角色：由系统创建，用户只能使用不能修改，每个子模块都有一个管理员 Admin 角色。
    - 自定义角色：用户自主创建、更新和删除，自定义角色中的权限由用户自己维护。
     同时因为全局管理汇聚了多个子模块，各子模块也拥有相应的管理员角色，例如：
       - IAM Admin：管理用户与访问控制，即管理用户/用户组以及授权
       - Workspace Admin：管理层级及工作空间的权限，仅此权限可以创建层级
       - Audit Admin：管理审计日志

- Rolling update, 滚动更新

    [滚动更新](../mspider/03UserGuide/upgrade/IstioUpdate.md)指一次只更新一小部分副本、成功后再更新更多的副本、最终完成所有副本的更新。
    滚动更新的最大的好处是零停机，整个更新过程始终有副本在运行，从而保证了业务的连续性。

- Routing Rule, 路由规则

    在服务网格的[虚拟服务](../mspider/03UserGuide/02TrafficGovernance/VirtualService.md)中配置的路由规则，遵循服务网格定义了请求的路径。
    使用路由规则，可以定义将寻址到虚拟服务主机的流量路由到指定目标的工作负载。
    路由规则使您可以控制流量，以实现按百分比分配流量的分阶段等任务。

### S

- Scalability, 可扩缩性

    可扩缩性指的是一个系统能有多大的发展。这就是增加做任何系统应该做的事情的能力。
    例如，Kubernetes 集群通过增加或减少容器化应用程序的数量来进行扩缩，但这种可扩缩性取决于几个因素。
    它有多少节点，每个节点可以处理多少个容器，控制平面可以支持多少条记录和操作？

    可扩缩的系统使添加更多容量更容易。主要有两种扩缩方法。
    一方面，有水平扩缩添加更多节点来处理增加的负载。
    相比之下，在垂直扩缩中，单个节点的功能更强大，可以执行更多事务（例如，通过向单个机器添加更多内存或 CPU）。
    可扩缩的系统能够轻松更改并满足用户需求。

- Secret

    [Secret](../kpanda/07UserGuide/ConfigMapsandSecrets/create-secret.md) 用于存储敏感信息，如密码、 OAuth 令牌和 SSH 密钥。

    Secret 允许用户对如何使用敏感信息进行更多的控制，并减少信息意外暴露的风险。
    默认情况下，Secret 值被编码为 base64 字符串并以非加密的形式存储，
    但可以配置为[静态加密（Encrypt at rest）](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/#ensure-all-secrets-are-encrypted)。

    Pod 可以通过多种方式引用 Secret，例如在卷挂载中引用或作为环境变量引用。Secret 设计用于机密数据，而
    [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)
    设计用于非机密数据。

- Security Context, 安全上下文

    securityContext 字段定义 Pod 或容器的特权和访问控制设置，包括运行时 UID 和 GID。

    在一个 `securityContext` 字段中，您可以设置进程所属用户和用户组、权限相关设置。
    您也可以设置安全策略（例如 SELinux、AppArmor、seccomp）。

    `PodSpec.securityContext` 字段配置会应用到一个 Pod 中的所有的容器。

- Selector, 选择算符

    选择算符允许用户通过标签对一组资源对象进行筛选过滤。

    在查询资源列表时，选择算符可以通过标签对资源进行过滤筛选。

- Serverless

    Serverless 是一种云原生开发模型，允许开发人员构建和运行应用程序，而无需管理服务器。
    Serverless 中仍有服务器，但它们被抽象出来，远离应用程序开发。
    云提供商处理配置、维护和扩缩服务器基础架构的日常工作。
    开发人员可以简单地将他们的代码打包在容器中进行部署。
    部署后，Serverless 应用程序会响应需求并根据需要自动扩展和缩减。
    公共云提供商的 Serverless 产品通常通过事件驱动的执行模型按需计量。
    因此，当无服务器功能处于空闲状态时，它不会花费任何费用。

    在标准的基础设施即服务 (IaaS) 云计算模型下，用户预先购买容量单位，
    这意味着您需要向公共云提供商支付永远在线的服务器组件的费用来运行您的应用程序。
    用户有责任在高需求时扩缩服务器容量，并在不在需要该容量时缩减容量。
    即使在不使用应用程序时，运行应用程序所需的云基础设施也处于活动状态。

    相比之下，使用 Serverless 架构，应用程序仅在需要时启动。
    当事件触发应用程序代码运行时，公共云提供商会为该代码动态分配资源。
    当代码执行完成后，用户就停止为资源付款。
    除了成本和效率优势之外，Serverless 还使开发人员从与应用程序扩展和服务器配置相关的日常和琐碎任务中解放出来。
    借助 Serverless，管理操作系统和文件系统、安全补丁、负载平衡、容量管理、扩缩、日志记录和监控等日常任务都被交给云服务提供商。

- Service, 服务

    请注意，在 IT 中，服务有多种含义。
    在这个定义中，我们将关注更传统的定义：微服务中的服务。
    服务与微服务哪里有、是否有区别是细微的，不同的人可能有不同的看法。
    在更高层次的定义中，我们将它们视为相同。具体请参考微服务的定义。

    服务所针对的 Pod 集合（通常）由选择算符确定。
    如果有 Pod 被添加或被删除，则与选择算符匹配的 Pod 集合将发生变化。
    服务确保可以将网络流量定向到该工作负载的当前 Pod 集合。

- ServiceAccount

    为在 Pod 中运行的进程提供标识。

    当 Pod 中的进程访问集群时，API 服务器将它们作为特定的服务帐户进行身份验证，例如 `default`。
    创建 Pod 时，如果您没有指定服务账户，它将自动被赋予同一个{{< glossary_tooltip text="命名空间" term_id="namespace" >}}中的 default 服务账户。

- Service Catalog, 服务目录

    服务目录是一种扩展 API，它能让 Kubernetes 集群中运行的应用易于使用外部托管的软件服务，例如云供应商提供的数据仓库服务。

    服务目录可以检索、供应并绑定外部托管服务（Managed Services），而无需知道那些服务具体是怎样创建和托管的。

- Service Discovery, 服务发现

    服务发现是查找组成服务各个实例的过程。
    服务发现工具持续跟踪构成服务的各种节点或端点。

    云原生架构是动态的和不确定的，这意味着它们不断在变化。
    容器化的应用程序在其生命周期内可能会多次启动和停止。
    每次这种情况发生时，它都会有一个新地址，任何应用程序想要找到它，都需要一个工具来提供新的地址信息。

    服务发现持续跟踪网络中的应用程序，以便在需要时可以找到彼此。
    它提供了一个公共的地方来查找和识别不同服务。
    服务发现引擎是类似数据库的工具，用于存储当前有哪些服务以及如何找到它们。

- Service Entry, 服务条目

    在服务网格中，服务条目用于将一个无法注册到服务注册表的网格内部服务（例如：vm）或网格外部服务器添加到服务网格抽象模型中。
    添加服务条目后，Envoy 代理可以将流量发送到该服务，这个服务条目将和网格中的其他服务一样。

- Service Mesh, 服务网格

    在微服务的理念里，应用程序被分解成多个较小的服务，通过网络进行通信。
    就像您的 WIFI 网络一样，计算机网络本质上是不可靠的，可被黑客攻击的，而且往往很慢。
    服务网格通过管理服务之间的流量（即通信），并在所有服务中统一添加可靠性、可观测性和安全功能来解决这一系列新的挑战。

    在转向微服务架构后，工程师们现在要处理数百个，甚至数千个单独的服务，都需要进行通信。
    这意味着大量的流量在网络上来回传输。
    除此之外，单个应用程序可能需要对通信进行加密，以支持监管要求，为运营团队提供通用指标，或提供对流量的详细洞察，以帮助诊断问题。
    如果内置于单个应用程序中，这些功能中的每一个都会引起团队间的冲突，并减缓新功能的开发。

    服务网格在集群的所有服务中统一增加了可靠性、可观测性和安全功能，而不需要改变代码。
    在服务网格之前，这些功能必须被编码到每一个服务中，成为错误和技术债务的潜在来源。

- Service Name, 服务名称

    服务名称是服务 Service 唯一的名字，是 Service 在服务网格里的唯一标识。服务名称是唯一的，不得重复。
    一个服务有多个版本，但是服务名是与版本独立的。

- Service Operator

    Service Operator 是在服务网格里管理 Service 的代理，
    通过操纵配置状态并通过各种仪表板监视服务的运行状况来管理这些服务。

- Service Proxy, 服务代理

    服务代理拦截进出某项服务的流量，对其应用一些逻辑，然后将该流量转发给另一项服务。
    它本质上是一个“中间人”，收集有关网络流量的信息，并决定是否对其应用规则。

    为了跟踪服务与服务之间的通信（又称网络流量），并可能对其进行转换或重定向，我们需要收集数据。
    传统上，实现数据收集和网络流量管理的代码被嵌入每个应用程序中。

    服务代理允许我们将这种功能“外部化”。它不再需要生活在应用程序中。
    相反，它现在被嵌入到平台层中（您的应用程序运行的地方）。

    作为服务之间的守门员，代理提供对正在发生的通信类型的洞察力。
    根据他们的洞察力，他们决定将一个特定的请求发送到哪里，甚至完全拒绝它。

    代理人收集关键数据，管理路由（在服务之间平均分配流量，或在某些服务中断时重新路由），加密连接，并缓存内容（减少资源消耗）。

- Service Registry, 服务注册表

    服务网格维护了一个内部服务注册表 (service registry)，包含在服务网格中运行的一组服务及其相应的服务 endpoints。服务网格使用服务注册表生成 Envoy 配置。

- Self Healing, 自愈

    一个自愈系统无需任何人为干预就能从某些类型的故障中恢复。
    像 DCE 5.0 这种系统自带一个“收敛”或“控制”循环，可以主动查看系统的实际状态并将其与运营商最初期望的状态进行比较。
    如果有所差异（例如运行的应用程序实例数少于预期实例数），系统将自动采取修正措施（例如启动新的实例或 Pod）。

- Shuffle Sharding, 混排切片

    一种将请求指派给队列的技术，其隔离性好过对队列个数哈希取模的方式。

    我们通常会关心不同的请求序列间的相互隔离问题，目的是为了确保密度较高的请求序列不会湮没密度较低的序列。
    将请求放入不同队列的一种简单方法是对请求的某些特征值执行哈希函数，将结果对队列的个数取模，从而得到要使用的队列的索引。
    这一哈希函数使用请求的与其序列相对应的特征作为其输入。例如在互联网上，这一特征通常指的是由源地址、目标地址、协议、源端口和目标端口所组成的五元组。

    这种简单的基于哈希的模式有一种特性，高密度的请求序列（流）会湮没那些被哈希到同一队列的其他低密度请求序列（流）。
    为大量的序列提供较好的隔离性需要提供大量的队列，因此是有问题的。
    混排切片是一种更为灵活的机制，能够更好地将低密度序列与高密度序列隔离。
    混排切片的术语采用了对一叠扑克牌进行洗牌的类比，每个队列可类比成一张牌。
    混排切片技术首先对请求的特定于所在序列的特征执行哈希计算，生成一个长度为十几个二进制位或更长的哈希值。
    接下来，用该哈希值作为信息熵的来源，对一叠牌来混排，并对整个一手牌（队列）来洗牌。
    最后，对所有处理过的队列进行检查，选择长度最短的已检查队列作为请求的目标队列。
    在队列数量适中的时候，检查所有已处理的牌的计算量并不大，对于任一给定的低密度的请求序列而言，有相当的概率能够消除给定高密度序列的湮没效应。
    当队列数量较大时，检查所有已处理队列的操作会比较耗时，低密度请求序列消除一组高密度请求序列的湮没效应的机会也随之降低。因此，选择队列数目时要颇为谨慎。

- Site Reliability Engineering, SRE, 网站可靠性工程

    网站可靠性工程（SRE） 是一门结合运营和软件工程的学科。
    后者特别适用于基础设施和运营问题。
    这意味着，网站可靠性工程师不是构建产品功能，而是构建系统来运行应用程序。
    与 DevOps 有相似之处，但 DevOps 专注于将代码投入生产环境，
    而 SRE 是确保在生产环境中运行的代码正常工作。

    确保应用程序可靠运行需要多种功能，
    从性能监控、警报、调试到故障排除。
    没有这些，系统操作员只能对问题做出反应，而不是主动努力避免它们，因为停机只是时间问题。

    网站可靠性工程通过不断改进底层系统来最小化软件开发过程的成本、时间和工作量。
    该系统持续测量和监控基础设施和应用程序组件。
    当出现问题时，系统会提示网站可靠性工程师何时、何地以及如何修复它。
    这种方法通过自动化任务来帮助创建高度可扩展和可靠的软件系统。

- Software as a service, SaaS, 软件即服务

    软件即服务 (SaaS) 允许用户通过互联网连接或使用云服务。
    常见的例子有电邮、日历和办公工具（例如 Gmail、AWS、GitHub、Slack）。
    SaaS 以按需付费的方式提供完整的软件解决方案。
    所有运维任务和应用数据由服务提供商处理。

    传统的商业软件被安装在独立的计算机上，需要管理员维护和更新。
    例如：某组织可能在企业内部使用客户关系管理 (CRM) 软件。
    该软件需要内部 IT 部门采购、安装、确保安全、维护和定期升级，为 IT 团队增加了负担。
    与许可证、安装和潜在附加硬件相关的前期成本可能令人望而却步。
    也很难按需响应，很难随着业务增长或变化快速扩缩。

    SaaS 应用无需内部 IT 部门付出任何特别努力即可工作。
    这些应用由供应商安装、维护、升级和确保安全。
    扩缩、可用性和容量问题由服务提供商处理，采用按需付费的模式。
    对于想要使用企业级应用的各个组织而言，SaaS 是一种经济实惠的方式。

- Stateful Apps, 有状态应用

    当我们说到有状态（和无状态）应用时，状态是指应用需要存储以便其按设计运行的任何数据。
    例如，任何能记住您购物车的在线商店都是有状态应用。

    使用一个应用通常需要多个请求。
    例如，使用网上银行时，您将通过输入密码（请求 #1）来验证自己的身份，
    然后您可以将钱转给某个朋友（请求 #2），最后您需要查看转账详情（请求 #3）。
    为了保证正常运行，每一步都必须记住前面的步骤，银行需要记住每个人的账户状态。
    今天我们使用的大多数应用至少总有一部分是有状态的，
    因为这些应用会存储诸如偏好和设置之类的东西以改善用户体验。

    有几种方法可以为有状态应用存储状态。
    最简单的是将状态保存在内存中，而不是将其持久保存在任何其他地方。
    这样做的问题是，每次应用必须重启时，所有状态都会丢失。
    为了防止这种情况发生，状态被持久存储在本地（磁盘上）或数据库系统中。

- StatefulSet

    [StatefulSet](../kpanda/07UserGuide/Workloads/CreateStatefulSetByImage.md) 用来管理某 Pod 集合的部署和扩缩，并为这些 Pod 提供持久存储和持久标识符。

    与 Deployment 类似，StatefulSet 管理基于相同容器规约的一组 Pod。
    但和 Deployment 不同的是，StatefulSet 为它们的每个 Pod 维护了一个有粘性的 ID。
    这些 Pod 是基于相同的规约来创建的，但是不能相互替换：无论怎么调度，每个 Pod 都有一个永久不变的 ID。

    如果希望使用存储卷为工作负载提供持久存储，可以使用 StatefulSet 作为解决方案的一部分。
    尽管 StatefulSet 中的单个 Pod 仍可能出现故障，但持久的 Pod 标识符使得将现有卷与替换已失败 Pod 的新 Pod 相匹配变得更加容易。

- Stateless Apps, 无状态应用

    无状态应用不会在应用所在的服务器上保存任何客户端会话（状态）数据。
    每个会话都像第一次一样执行，响应不依赖于前一个会话的数据并提供使用打印服务、内容分发网络（CDN）或
    Web 服务器的功能，以处理每个短期请求。
    例如，有人在搜索引擎中搜索某个问题并按下了回车键。
    如果搜索操作由于某种原因被中断或关闭，您必须重新开始一个新的，因为您之前的请求没有保存数据。

    无状态应用解决了弹性问题，因为集群中的不同 Pod 可以独立工作，
    同时允许多个请求到达这些 Pod。
    如果应用出现故障，您只需重启应用，就能恢复到初始状态，停机时间很短或没有停机时间。
    因此，无状态应用的好处包括坚韧、弹性和高可用性。
    然而，我们今天使用的大多数应用至少总有一部分是有状态的，
    因为它们会存储诸如偏好和设置之类的东西以改善用户体验。

    归根结底，在无状态应用中集群唯一负责的是托管在其上的代码和其他静态内容。
    就是这样，不更改数据库，没有写入，删除 Pod 时也没有留下文件。
    无状态容器更易于部署，您无需担心如何将容器数据保存在持久存储卷上。
    您也不必担心备份数据。

- Static Pod, 静态 Pod

    静态 Pod 是指由特定节点上的 kubelet 守护进程直接管理的 Pod。
    API 服务器不会察觉这种 Pod。静态 Pod 不支持临时容器。

- StorageClass

    StorageClass 是管理员用来描述可用的不同存储类型的一种方法。

    StorageClass 可以映射到服务质量等级（QoS）、备份策略、或者管理员任意定义的策略。
    每个 StorageClass 对象包含的字段有 `provisioner`、`parameters` 和 `reclaimPolicy`。
    动态制备该存储类别的持久卷时需要用到这些字段值。
    通过设置 StorageClass 对象的名称，用户可以请求特定存储类别。

- sysctl

    用于获取和设置 Unix 内核参数的接口。`sysctl` 是一个半标准化的接口，用于读取或更改正在运行的 Unix 内核的属性。

    在类 Unix 系统上，`sysctl` 既是管理员用于查看和修改这些设置的工具的名称，也是该工具所调用的系统调用的名称。

    容器运行时和网络插件可能对 `sysctl` 的取值有一定的要求。

- Summary, 汇总

    类似于直方图，汇总也对观测结果进行采样。除了可以统计采样值总和和总数，它还能够按分位数统计。有以下几种方式来产生汇总（假设度量指标为 `<basename>`）：

    - 按分位数，也就是采样值小于该分位数的个数占总数的比例小于 φ，相当于 `<basename>{quantile="<φ>"}`
    - 采样值总和，相当于 `<basename>_sum`
    - 采样值总数，相当于 `<basename>_count`

### T

- Taint, 污点

    [污点](../kpanda/07UserGuide/Nodes/Taints.md)是一种核心对象，包含三个必需的属性：key、value 和 effect。污点会阻止在节点或节点组上调度 Pod。

    污点配合容忍度一起工作，以确保不会将 Pod 调度到不适合的节点上。
    同一节点上可标记一个或多个污点。节点应该仅调度那些带着能与污点相匹配容忍度的 Pod。

- Temporary microservice instance, 临时微服务实例

    不能持久化存储在 Nacos 服务端的微服务实例。
    临时微服务实例需要通过上报心跳的方式进行包活，如果一段时间内没有上报心跳，就会被 Nacos 服务端摘除。

- Threshold, 保护阈值

    阈值是一个 0 到 1 之间的浮点数。
    当健康实例数占总服务实例数的比例小于该值时，无论实例是否健康，都会将这个实例返回给客户端。
    这样可以防止流量压力把健康实例压垮并形成雪崩效应。

- Tightly Coupled Architecture, 紧耦合架构

    紧耦合架构（松耦合架构的相反范式）是一种架构风格，其中许多应用程序组件相互依赖。
    这意味着一个组件的更改可能会影响其他组件。
    它通常比松耦合架构更容易实现，但会使系统更容易受到级联故障的影响。
    它还意味着需要协调各个组件的部署，这可能会拖累开发人员的生产力。

    紧耦合应用程序架构是一种相当传统的应用程序构建方式。
    在某些特定情况下，当我们不需要与微服务开发的所有最佳实践一致时，它将变得很有用。
    这意味着更快、更简单地实现， 和单体应用很像，可以加快最初的开发周期。

- Toleration, 容忍度

    一个核心对象，由三个必需的属性组成：key、value 和 effect。
    容忍度允许将 Pod 调度到具有对应污点的节点或节点组上。

    容忍度和污点共同作用可以确保不会将 Pod 调度在不适合的节点上。
    在同一 Pod 上可以设置一个或者多个容忍度。
    容忍度表示在包含对应污点的节点或节点组上调度 Pod 是允许的（但不必要）。

- Transport Layer Security, TLS, 传输层安全性协议

    传输层安全性协议 (TLS) 是一种旨在为网络通信提供更高安全性的协议。
    它确保通过互联网发送的数据安全交付，避免可能的数据监视和/或篡改。
    该协议广泛用于消息传递、电子邮件等应用程序中。

    如果没有 TLS，网页浏览习惯、电子邮件通信、在线聊天和电话会议等敏感信息在传输过程中很容易被他人追踪和篡改。
    启用服务器和客户端应用程序对 TLS 的支持，可以确保它们之间传输的数据是加密的，并且第三方无法查看。

    TLS 使用多种编码技术，在通过网络传输数据时提供安全性。
    TLS 允许客户端应用程序和服务器（如浏览器和银行站点）之间的加密连接。
    它还允许客户端应用程序积极地识别他们正在调用的服务器，从而降低客户端与欺诈站点通信的风险。
    这可以确保第三方无法查看和监控使用 TLS 在应用程序之间传输的数据，从而保护敏感隐私的信息，例如信用卡号、密码、位置等。

- [Trace](https://opentelemetry.io/docs/concepts/signals/traces/), [链路](../insight/user-guide/04dataquery/tracequery.md)

    记录单次请求范围内的处理信息，其中包括服务调用和处理时长等数据。
    一个 Trace 有一个唯一的 Trace ID ，并由多个 Span 组成。

### U, V

- UID

    由 Kubernetes 系统生成、用来唯一标识对象的字符串。

    在 Kubernetes 集群的整个生命周期中创建的每个对象都有一个不同的 UID，它旨在区分类似实体的历史事件。

- User, 用户

    [用户](../ghippo/04UserGuide/01UserandAccess/User.md)是发起操作的主体，每个用户都有唯一的 ID，并被授予不同的角色。
    默认创建的 IAM 用户没有任何权限，需要将其加入用户组，授予角色或策略，才能让用户获得对应的权限。

    用户以用户名登录 DCE，按照被授予的权限操作平台资源和服务。
    所以用户是资源归属的主体，对其拥有的资源具有相应权限。

    用户可以在个人中心修改用户信息，设置密码、访问密钥和 UI 语言。

- User namespace, 用户命名空间

    一种为非特权用户模拟超级用户特权的 Linux 内核功能特性。

    用来模拟 root 用户的内核功能特性，用来支持“Rootless 容器”。

    用户命名空间（User Namespace）是一种 Linux 内核功能特性，允许非 root 用户
    模拟超级用户（"root"）的特权，例如用来运行容器却不必成为容器之外的超级用户。

    用户命名空间对于缓解因潜在的容器逃逸攻击而言是有效的。

    在用户命名空间语境中，命名空间是 Linux 内核的功能特性而不是 Kubernetes 意义上的命名空间概念。

- Version Control, 版本控制

    源代码管理（或版本控制）是一种跟踪和管理文档更改的行为。
    它是一个持续记录单个文件或一组文件变化的系统，以便您在以后可以回退到特定版本。

    版本控制系统致力于解决以下问题，
    备份随时间变化的文档或代码库，
    允许在多个用户存在交叉修改时解决冲突，并随时间存储更改日志。
    处理关键业务的应用程序代码通常复杂且重要，
    因此，跟踪谁更改了内容、什么时候更改的以及更改原因是非常重要的。
    此外，许多（甚至可以说大部分）应用程序是由多个开发人员修改的，并且不同开发人员引入的更改之间经常存在冲突。

    版本控制可帮助开发人员快速行动并保持效率，同时存储更改记录并提供解决冲突的工具。
    它可以将应用程序代码存储在代码仓库中并简化开发人员间的协作。
    现代应用程序开发非常依赖版本控制系统，如 git，来存储他们的代码。

- Vertical Scaling, 垂直扩缩

    垂直扩缩，也称为“向上和向下扩缩”，是一种通过在工作负载增加时向单个节点添加 CPU 和内存来增加系统容量的技术。
    假设您有一台 4GB RAM 的计算机，并且想要将其容量增加到 16GB RAM，垂直扩缩就意味着切换到 16GB RAM 系统。
    （请参阅水平扩缩了解不同的扩缩方法。）

    随着对应用程序的需求增长超出该应用程序实例的当前容量，我们需要找到一种方法来伸展（增加容量）系统。
    我们可以向现有节点添加更多计算资源（垂直扩缩）或向系统添加更多节点(水平扩缩)。
    可扩缩性有助于提高竞争力、效率、声誉和质量。

    垂直扩缩允许您在不更改应用程序代码的情况下调整服务器大小。
    这与水平扩缩形成对比，在水平扩缩中，应用程序必须可以被复制来进行扩缩，而这可能需要代码更新。
    垂直扩缩通过添加计算资源来增加现有应用程序的容量，允许应用程序处理更多请求并同时执行更多工作。

- Virtual Machine, 虚拟机

    虚拟机（VM）是一台计算机及其操作系统，不受特定硬件的约束。
    虚拟机依靠虚拟化将一台物理计算机分割成多个虚拟计算机。
    这种分离使组织和基础设施供应商能够轻松地创建和销毁虚拟机，而不影响底层硬件。

    虚拟机利用了虚拟化的优势。
    当裸机机器被束缚在一个单一的操作系统上时，该机器的资源的使用受到一定的限制。
    另外，当一个操作系统被绑定在一个单一的物理机上时，它的可用性直接与该硬件联系在一起。
    如果物理机由于维护或硬件故障而脱机，操作系统也会脱机。

    通过消除操作系统和单一物理机之间的直接关系，您解决了裸机的几个问题：配置时间、硬件利用率和弹性。

    由于不需要购买、安装或配置新的硬件来支持它，新计算机的配置时间得到了极大的改善。
    虚拟机通过在一台物理机上放置多个虚拟机，使您能够更好地利用现有的物理硬件资源。
    不受特定物理机的约束，虚拟机也比物理机更有弹性。
    当一台物理机需要下线时，在其上运行的虚拟机可以被转移到另一台机器上，几乎没有停机时间。

- Virtualization, 虚拟化

    虚拟化，在云原生计算的背景下，是指将一台物理计算机，有时称为服务器，并允许它运行多个隔离的操作系统的过程。
    这些隔离的操作系统及其专用的计算资源（CPU、内存和网络）被称为虚拟机或 VM。
    当我们谈论虚拟机时，我们在谈论一个软件定义的计算机。
    它看起来和行动都像一台真正的计算机，但与其他虚拟机共享硬件。
    举个例子，您可以从 AWS 租赁一台 "计算机"，该计算机实际上是一个虚拟机。

    虚拟化解决了许多问题，包括通过允许更多的应用程序在同一台物理机器上运行，同时为了安全起见仍然相互隔离，从而改善物理硬件的使用。

    在虚拟机上运行的应用程序没有意识到他们正在共享一台物理计算机。
    虚拟化还允许数据中心的用户在几分钟内启动一台新的 "计算机"（又称虚拟机），而不必担心在数据中心增加一台新计算机的物理限制。
    虚拟机还使用户能够加快获得新的虚拟计算机的时间。

- Virtual Service, 虚拟服务

    虚拟服务定义了一系列针对指定服务的流量路由规则。
    每个路由规则都针对特定协议定义流量匹配规则。
    如果流量符合这些特征，就会根据规则发送到服务注册表中的目标服务（或者目标服务的子集或版本）。

- Volume, 卷

    包含可被 Pod 中容器访问的数据目录。

    每个 Kubernetes 卷在所处的 Pod 存续期间保持存续状态。
    因此，卷的生命期会超出 Pod 中运行的容器，并且保证容器重启之后仍保留数据。

- Volume Plugin, 卷插件

    卷插件可以让 Pod 集成存储。

    卷插件让您能给 Pod 附加和挂载存储卷。
    卷插件既可以是 **in tree** 也可以是 **out of tree** 。
    **in tree** 插件是 Kubernetes 代码库的一部分，并遵循其发布周期。
    而 **Out of tree** 插件则是独立开发的。

### W, Z

- Weight, 权重

    权重为浮点数。权重越大，表示分配给该实例的流量越大。

- Workload, 工作负载

    工作负载是在 Kubernetes 上运行的应用程序。

    代表不同类型或部分工作负载的各种核心对象包括 [Deployment](../kpanda/07UserGuide/Workloads/CreateDeploymentByImage.md)、[StatefulSet](../kpanda/07UserGuide/Workloads/CreateStatefulSetByImage.md)、[DaemonSet](../kpanda/07UserGuide/Workloads/CreateDaemonSetByImage.md)、[Job](../kpanda/07UserGuide/Workloads/CreateJobByImage.md)、ReplicaSet。

    例如，具有 Web 服务器和数据库的工作负载可能在一个 StatefulSet 中运行数据库，而 Web 服务器运行在 Deployment。

- Workload Instance, 工作负载实例

    在服务网格中，工作负载实例是工作负载的一个二进制实例化对象。
    一个工作负载实例可以开放零个或多个服务 endpoint，也可以消费零个或多个服务。
    工作负载实例具有许多属性：名称和命名空间、IP 地址、唯一的 ID、标签、主体等

- Workload Instance Principal, 工作负载实例主体

    在服务网格中，工作负载实例主体是工作负载实例的可验证权限。服务网格的服务到服务身份验证用于生成工作负载实例主体。
    默认情况下，工作负载实例主体与 SPIFFE ID 格式兼容。

- Workspace, 工作空间

    [工作空间](../ghippo/04UserGuide/02Workspace/Workspaces.md)是一种资源范畴，代表一种资源层级关系。
    工作空间可以包含集群、[命名空间](../kpanda/07UserGuide/Namespaces/createns.md)、注册中心等资源。
    通常一个工作空间对应一个项目，可以为每个工作空间分配不同的资源，指派不同的用户和用户组。

- Worker Cluster, 工作集群

    工作集群是一个连接到集群外部控制平面的集群。
    工作集群可以连接到主集群的控制平面，或连接到一个外部控制平面。

- Zero Trust Architecture, 零信任架构

    零信任架构规定了一种完全消除信任的 IT 系统设计和实施方法。
    其核心原则是 "永不信任，永远验证"，设备或系统本身在与系统的其他组件进行通信时，总是先验证自己。
    在今天的许多网络中，在企业网络中，内部的系统和设备可以自由地相互通信，因为它们在企业网络外围的信任边界内。
    零信任架构采取了相反的方法，虽然在网络边界内，但系统内的组件在进行任何通信之前首先必须通过验证。

    在传统的基于信任的方法中，存在于企业网络周边的系统和设备，其假设是，因为有信任，所以没有问题。
    然而，零信任架构认识到，信任是一个弱点。
    如果攻击者获得了对受信任设备的访问，根据对该设备的信任和访问程度，系统现在很容易受到攻击，因为攻击者在 "受信任 "的网络边界内，能够在整个系统内横向移动。
    在零信任架构中，信任被移除，因此减少了攻击面，因为攻击者现在被迫在进入整个系统之前进行验证。

    采用零信任架构带来的主要好处是增加安全，减少攻击面。
    从您的企业系统中移除信任，现在增加了攻击者必须通过的安全门的数量和强度，以获得对系统的其他区域的访问。

[Download DCE 5.0](../download/dce5.md){ .md-button .md-button--primary }
[Install DCE 5.0](../install/intro.md){ .md-button .md-button--primary }
[Free Trial](license0.md){ .md-button .md-button--primary }
