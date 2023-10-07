# Glossary

This page lists some terms common to DCE 5.0 in alphabetical order.

### A

- Abstraction

    In the context of computing, an abstraction is a representation that
    hides specifics from a consumer of [services](../kpanda/user-guide/network/create-services.md)
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
    [Container Management](../kpanda/intro/index.md) -> [Helm chart](../kpanda/user-guide/helm/README.md).

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

    The aggregation layer allows Kubernetes to be extended with additional APIs, beyond what is offered
    by the core Kubernetes APIs. The additional APIs can either be ready-made solutions such as a metrics
    server, or APIs that you develop yourself.

    The aggregation layer is different from Custom Resources, which are a way to make the kube-apiserver
    recognise new kinds of object.

- [Alert Rule](../insight/user-guide/alert-center/alert-policy.md)

    In Insight, this is an alert object created based on the resource status. You can customize the conditions
    for triggering rules and sending notifications.

- Annotation

    [Annotation](../kpanda/user-guide/nodes/labels-annotations.md) is a key-value pair that is used to attach
    arbitrary non-identifying metadata to objects.

    The metadata in an annotation can be small or large, structured or unstructured, and can include characters
    not permitted by labels. Clients such as tools and libraries can retrieve this metadata.

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

    API-initiated eviction is the process by which you use the Eviction API to create an Eviction object
    that triggers graceful pod termination.

    You can request eviction by calling the Eviction API directly, or programmatically using a client of
    the API server, like the `kubectl drain` command. This creates an `Eviction` object, which causes the API server to terminate the Pod.

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
    It allows organizations to move key features,
    such as authentication and authorization or limiting the number of requests between applications,
    to a centrally managed location.
    An API gateway features as a common interface to (often external) API consumers.

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

    Init containers allow you to isolate initialization details that are important to the workload as a whole,
    and the init container does not need to continue running once the application container starts.
    If a Pod does not have an Init container configured, all containers in that Pod are application containers.

- App Architect

    The application architect is the development leader responsible for the high-level design of the application.

    The application architect ensures that the implementation of the application allows it to interact with
    surrounding components in a scalable and sustainable manner.
    Surrounding components include databases, logging infrastructure, and other microservices.

- App Developer

    Developers who write applications that run on Kubernetes clusters.
    Application developers focus on a certain part of the application. There is a marked difference in the size of their working areas.

- App, Application

    The layer where various containerized services run.

- Audit log, audit log

    [Audit Log](../ghippo/user-guide/audit/audit-log.md) provides a historical record of changes made to objects in the system.

- Authorization

    [Authorization](../ghippo/user-guide/access-control/iam.md) refers to granting users the permissions
    required to complete specific tasks, and the authorization takes effect through the permissions of system roles or custom roles.
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
    production traffic is switched over (often via the use of a load balancer).
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

    Canary deployments allow organizations to see how new software behaves in real-world use cases
    before moving significant traffic to the new version.
    This strategy enables organizations to minimize downtime and quickly rollback in case of issues with the new deployment.
    It also allows more in-depth production application testing without a significant impact on the overall user experience.

- cAdvisor

    cAdvisor is a daemon that provides users with information about the resource usage and performance characteristics
    of running containers. It collects, aggregates, processes, and outputs information about running containers.
    Specifically, for each container, the process records the container's resource isolation parameters, historical
    resource usage, complete historical resource usage, and network statistics histogram.
    This data can be output on a per-container or per-machine basis.

- Certificate

    A (digital) certificate — also often referred to as a public key certificate, or SSL certificate —
    is a digital document used to help secure communications over the network.
    Certificates allow us to know that the particular entity we're communicating with is who they say they are.
    They also allow us to ensure that our communications are private by encrypting the data we send and receive.

    When devices communicate over a network there is no inherent guarantee that a particular device is who it says it is.
    Additionally, we can't guarantee that the traffic between any two devices won't be intercepted by a third party.
    Consequently, any communication can potentially be intercepted, compromising sensitive information like usernames and passwords.

    Modern email clients that utilize certificates can notify you if a sender's identity is correct, as will web browsers
    (notice the little lock in front of the address bar of your web browser).
    On the other side, certificates can be used to encrypt communication between entities on the internet.
    They provide an encryption technique that makes it nearly impossible, for someone who intercepts the communication, to actually read the data.

- cgroup, control group

    A group of Linux processes with optional resource isolation, auditing, and limitation.
    cgroup is a Linux kernel feature that limits, audits, and isolates the resource usage (CPU, memory, disk I/O, network, etc.) of a group of processes.

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

    CIDR (Classless Inter-Domain Routing) is a notation used to describe IP address blocks and is widely used in various
    network configurations. In the context of Kubernetes, each node is assigned an IP address range in CIDR format
    (including the starting address and subnet mask), allowing for each Pod to be assigned a unique IP address.
    Although the concept originated from IPv4, CIDR has been extended to cover IPv6.

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
    Organizations can focus on their product or service without waiting, planning, and spending resources on new
    physical infrastructure. They can simply scale as needed and on-demand.
    Cloud computing allows organizations to adopt as much or as little infrastructure as they need.

- Cloud Controller Manager

    The `cloud-controller-manager` is a Kubernetes control plane component that embeds cloud-specific control logic.
    It allows you to connect your cluster to the API of a cloud provider and separate the components that interact
    with that cloud platform from the components that interact with your cluster.

    By separating the interoperability logic between Kubernetes and the underlying cloud infrastructure settings,
    the cloud-controller-manager component enables cloud providers to release new features at a different pace than
    the Kubernetes main project.

    In addition, cloud-native apps are specifically designed to take advantage of innovations in cloud computing.
    These applications integrate easily with their respective cloud architectures, taking advantage of the cloud's
    resources and scaling capabilities. Cloud native applications today include apps that run in a cloud provider's
    datacenter and on cloud native platforms on-premise.

    Cloud native security is an approach that builds security into cloud native applications.
    It ensures that security is part of the entire application lifecycle from development to production.
    Cloud native security seeks to ensure the same standards as traditional security models while adapting to
    the particulars of cloud native environments, namely rapid code changes and highly ephemeral infrastructure.

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

- Cloud Provider

    Cloud providers, also known as Cloud Service Providers (CSP), offer infrastructure as a service (IaaS)
    where they are responsible for the servers, storage, and network, while the user is responsible for
    managing the software layers running on top of it, such as a Kubernetes cluster. Some cloud providers
    also offer Kubernetes as a managed service, also known as platform as a service (PaaS), where the provider
    is responsible for the Kubernetes control plane and the nodes and infrastructure it depends on,
    such as networking, storage, and load balancers.

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

- Cluster Architect

    A person involved in the design of one or more Kubernetes cluster infrastructures. Cluster architects are usually more concerned with best practices for distributed systems, such as high availability and security.

- Cluster Infrastructure

    At the infrastructure layer, it provides and maintains virtual machines, networks, security groups, and other resources.

- Cluster Operations

    Kubernetes management-related work includes daily management and coordination of upgrades. Examples of cluster
    operations work include deploying new nodes to scale the cluster, performing software upgrades, implementing
    security controls, adding or removing storage, configuring cluster networks, managing cluster-wide observability, and responding to cluster events.

- Cluster Operator

    A person who configures, controls, and monitors the cluster. Their main responsibility is to ensure the
    normal operation of the cluster, which may require periodic maintenance and upgrade activities.

- CNCF, Cloud Native Computing Foundation

    A non-profit organization under the Linux Foundation, established in December 2015, dedicated to cultivating
    and maintaining a vendor-neutral open-source ecosystem to promote cloud-native technology and popularize cloud-native applications.

- CNI, Container network interface

    [CNI](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/)
    is a kind of network plugin that follows appc/CNI protocols.

    CNIs supported by DCE 5.0 include but not limited to:

    - Calico
    - Cilium
    - Contour
    - F5networks
    - Ingress-nginx
    - Metallb
    - Multus-underlay
    - Spiderpool

- [ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/)

    [ConfigMap](../kpanda/user-guide/configmaps-secrets/use-configmap.md) is an API object used to
    store non-sensitive data as key-value pairs. It can be used as environment variables, command-line parameters,
    or configuration files in storage volumes. ConfigMap decouples your environment configuration information
    from container images, making it easier to modify application configurations.

- Container Environment Variables

    Container Environment Variables provide important information in the form of name=value for running
    containerized applications. They provide necessary information for running containerized applications,
    as well as other important resource-related information such as file system information, container-specific
    information, and other cluster resource information such as service endpoints.

- Container Lifecycle Hooks

    Container Lifecycle Hooks expose events in container management lifecycles, allowing users to run code
    when events occur. Two hooks are exposed for containers: PostStart, which is executed immediately after
    the container is created, and PreStop, which is immediately blocked and called before the container stops.

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

    [containerd](https://github.com/containerd/containerd) is a container runtime that emphasizes simplicity,
    robustness, and portability. It can run in the background on Linux or Windows and is capable of retrieving
    and storing container images, executing container instances, and providing network access.

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
    automates key IT features on which containers are deployed and managed.
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
    Typically, trunk-based development is used in CD strategies as opposed To function branching or pull requests.

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

- Control Plane

    The control plane refers to the container orchestration layer that exposes APIs and interfaces to define, deploy,
    and manage the lifecycle of containers. It is composed of multiple components, including etcd, API server, scheduler,
    controller manager, and cloud controller manager, among others. These components can run as traditional OS services
    or containers, and the hosts running these components are referred to as Masters.

- Controller

    Controllers, as part of the control plane, monitor the cluster's public state through the API server and
    work towards transforming the current state into the desired state. Some controllers run within the control
    plane and provide core control operations for Kubernetes, such as the deployment controller, daemonset
    controller, namespace controller, and persistent volume controller, all of which run in kube-controller-manager.

- Counter

    Counters are a type of cumulative metric that is a **non-decreasing** value. Counters are mainly used
    for data such as service request counts, task completion counts, and error occurrence counts.

- Contour

    Contour is deployed as a control node and serves as the control plane for the microservice gateway,
    providing convenient gateway configuration, dynamic configuration updates, and multicluster deployment
    capabilities. Contour also provides the HTTPProxy CRD to enhance the core configuration capabilities of
    Kubernetes Ingress. It is recommended to deploy Contour in multiple replicas to ensure the stability of production services.

- Control Plane

    The control plane is a set of system services that configure the mesh or subnet of the mesh to manage
    communication between workload instances. All instances of the control plane in a single mesh share the same configuration resources.

- [CRD](../kpanda/user-guide/custom-resources/create.md), CustomResourceDefinition

    CustomResourceDefinition (CRD) allows you to add resource objects to your Kubernetes API server with
    customized code without having to compile a complete custom API server. When the API resources supported
    by Kubernetes cannot meet your needs, CRD allows you to extend the Kubernetes API in your own environment.
    Custom resource definitions are the default Kubernetes API extension, and the service mesh uses the Kubernetes CRD API for configuration.

- CRI-O

    CRI-O is a lightweight container runtime software tool dedicated to Kubernetes. This tool allows you to use
    [OCI](https://www.github.com/opencontainers/runtime-spec) container runtimes with Kubernetes CRI. CRI-O is an
    implementation of CRI that allows you to run pods using any OCI-compliant runtime as a container runtime and
    retrieve OCI container images from remote container repositories.

- CRI, Container Runtime Interface

    Container Runtime Interface (CRI) is a set of container runtime APIs integrated with kubelet on nodes,
    which is the main protocol for communication between kubelet and container runtime. CRI defines the main
    [gRPC](https://grpc.io) protocol for communication between cluster components kubelet and container runtime.

- CR, Container Runtime

    Container runtime is the component responsible for running containers. Kubernetes supports many container runtime environments, such as containerd, cri-o, and any other implementation of [Kubernetes CRI](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-node/container-runtime-interface.md).

- [CronJob](../kpanda/user-guide/workloads/create-cronjob.md)

    CronJob manages tasks that run periodically. Similar to a line of command in a crontab file, the CronJob object uses the [cron](https://en.wikipedia.org/wiki/Cron) format to set the schedule.

- CSI, Container Storage Interface

    Container Storage Interface (CSI) defines the standard interface for storage systems exposed to containers.
    CSI allows storage driver providers to create customized storage plugins for Kubernetes without adding the
    code of these plugins to the Kubernetes code repository (external plugins). To use a CSI driver from a
    storage provider, you must first [deploy it to your cluster](https://kubernetes-csi.github.io/docs/deploying.html).
    Then you can create a Storage Class that uses the CSI driver.

### D

- [DaemonSet](../kpanda/user-guide/workloads/create-daemonset.md)

    A DaemonSet ensures that a copy of a Pod is running on each node in a cluster.
    DaemonSets are useful for tasks that need to be performed on every node, such as collecting logs or monitoring system health.

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
    perform traditional database administration features.
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

    Data ID refers to the ID of a configuration set in Nacos, a platform for dynamic service discovery and
    configuration management. A configuration set is a collection of configuration items, typically represented
    as a configuration file, that includes various system configurations.

- Data Plane

    Data Plane, also known as the control plane, which is a part of a service mesh that directly controls
    communication between instances of a workload. The data plane of a service mesh uses intelligent Envoy
    proxies deployed as sidecars to regulate and control the traffic sent and received within the service mesh.
    The data plane provides capabilities such as CPU, memory, network, and storage to enable containers to run and connect to the network.

- Debugging

    Debugging is the process or activity of finding and resolving bugs (or errors) from computer programs,
    software, or systems to get the desired result. A bug is a defect or a problem leading to incorrect or unexpected results.

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

- [Deployement](../kpanda/user-guide/workloads/create-deployment.md)

    Deployment is an API object used to manage multi-replica applications, typically achieved by running stateless Pods.
    Each replica is represented by a Pod, which is distributed across nodes in the cluster.
    For workloads that do require local state, consider using StatefulSet.

- Device Plugin

    Device Plugin is a software extension that allows Pods to access devices initialized or installed by specific vendors.
    Device Plugins run on worker nodes and provide Pods with access to hardware features on the node where the Pod is running.
    For example, local hardware resources that require vendor-specific initialization or installation steps.
    Device Plugins expose resources to kubelet so that workload Pods can access hardware feature capabilities
    on the node where the Pod is running. You can deploy Device Plugins as DaemonSets or install Device Plugin software directly on each target node.

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

- Dependency topology

    Display the dependency relationship between service calls in a topology diagram.

- Destination

    The destination service is the remote upstream service that Envoy interacts with on behalf of a source service workload.
    These upstream services can have multiple service versions, and Envoy selects the corresponding version based on routing.

- Destination Rule

    The destination rule defines traffic policies applied to a service after routing.
    These rules specify load balancing configuration, connection pool size from the sidecar proxy, and outlier detection
    settings, enabling detection and circuit breaking of unhealthy hosts from the load balancing pool.

- Diagnosis

    Diagnosis mode is used to debug Contour and supports attaching corresponding startup parameters when Contour starts.

- Disruption

    An event that causes a Pod service to stop.

    Disruption refers to an event that causes one or more Pod services to stop.
    Disruption affects resources that depend on the affected Pod, such as Deployments.

    If you, as a cluster operator, destroy a Pod that belongs to an application, Kubernetes considers it a voluntary disruption.
    If a node failure or power outage affecting a larger area causes a Pod to go offline, Kubernetes considers it an involuntary disruption.

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

    Docker is a software technology that provides operating system-level virtualization (also known as containers).

    Docker uses resource isolation features in the Linux kernel (such as cgroups and kernel namespaces) and supports
    union filesystems (such as OverlayFS and others) to allow multiple independent "containers" to run on the same
    Linux instance, avoiding the overhead of starting and maintaining virtual machines (VMs).

- Dockershim

    Dockershim is a component in Kubernetes v1.23 and earlier versions that allows Kubernetes system components to communicate with the Docker Engine.

    As of Kubernetes v1.24, Dockershim has been removed from Kubernetes.

- Downward API

    A mechanism for exposing Pod and container field values to code running in the container.
    It is useful to have information about the container without modifying the container code.
    Modifying the code may couple the container directly to Kubernetes.

    The Kubernetes Downward API allows containers to use information about themselves or their environment in the Kubernetes cluster.
    Applications in the container can access this information without having to perform operations in the form of a Kubernetes API client.

    There are two ways to expose Pod and container fields to running containers:

    - Using environment variables
    - Using the downwardAPI volume

    These two ways of exposing Pod and container fields are collectively referred to as the Downward API.

- Dynamic Volume Provisioning

    Allows users to request the automatic creation of storage volumes.

    Dynamic provisioning allows cluster administrators to no longer pre-provision storage.
    Instead, it automatically provisions storage through user requests.
    Dynamic volume provisioning is based on the API object StorageClass,
    which can reference volumes provided by volume plugins or a set of parameters passed to the volume plugin.

### E, F

- Edge computing

    Edge computing is a distributed system approach that shifts some storage and computing capacity
    from the primary data center to the data source. The gathered data is computed locally
    (e.g., on a factory floor, in a store, or throughout a city) rather than sent to a centralized data center for processing and analysis.
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

    A method of combining network endpoints with Kubernetes resources.

    A scalable and extensible way to combine network endpoints.
    They will be used by kube-proxy to establish network routing on each node.

- Endpoint

    Endpoints are responsible for recording the IP addresses of Pods that match the selection operator of a Service.

    Endpoints can be manually configured on a Service without specifying a selection operator identifier.

    EndpointSlice provides a scalable and extensible alternative.

- Envoy

    Envoy is a high-performance proxy used in service meshes to schedule incoming and outgoing traffic for all services in the service mesh.

- Ephemeral Container

    A type of container that can be run temporarily in a Pod.

    If you want to investigate a running Pod with problems, you can add a temporary container to the Pod for diagnosis.
    Ephemeral containers have no resource or scheduling guarantees, so they should not be used to run any part of the workload itself.
    Static Pods do not support ephemeral containers.

- etcd

    A consistent and highly available key-value store used as the backend database for all cluster data in Kubernetes.

    If your Kubernetes cluster uses etcd as its backend database, make sure you have a backup plan for this data.

- Event

    A report of an event that occurred somewhere in the cluster. Typically used to describe a change in some kind of system state.

    Events have a limited retention time, and as time goes on, their triggering conditions and messages may change.
    Event users should not have any dependencies on the time characteristics of events with a given reason (reflecting the underlying trigger source),
    nor should they expect events caused by that reason to persist indefinitely.

    Events should be treated as informative, best-effort, supplementary data.

    In Kubernetes, an auditing mechanism generates a different category of Event records (API group `audit.k8s.io`).

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

- Eviction

    The process of terminating one or more Pods on a node.

    There are two types of eviction:

    - Node pressure eviction
    - API-initiated eviction

- Extensions

    Extensions are software components that extend Kubernetes and are deeply integrated with it to support new hardware.

    Many cluster administrators use managed Kubernetes or some distribution that comes with extensions pre-installed.
    Therefore, most Kubernetes users will not need to install extensions, and even fewer will need to write new ones.

- External Control Plane

    An external control plane can manage mesh workloads running in its own cluster or other infrastructure.
    The control plane can be deployed in one cluster but not in a subset of the mesh it controls.
    Its purpose is to completely separate the control plane from the data plane of the mesh.

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

    `Finalizer` is a key with a namespace that tells Kubernetes to completely delete a resource marked for deletion only after specific conditions are met. Finalizers remind controllers to clean up resources owned by the deleted object. When you tell Kubernetes to delete an object with a Finalizer, the Kubernetes API marks the object to be deleted by populating `.metadata.deletionTimestamp` and returns a `202` status code (HTTP "Accepted") to put it in read-only mode. At this point, the control plane or other components take the action defined by the Finalizer, and the target object remains in the Terminating state. After these actions are completed, the controller deletes the Finalizer associated with the target object. When the `metadata.finalizers` field is empty, Kubernetes considers the deletion complete and deletes the object. You can use Finalizer to control the garbage collection of resources. For example, you can define a Finalizer to clean up related resources or infrastructure before deleting the target resource.

- Folder

    In DCE, `Folder` is a [hierarchical concept](../ghippo/user-guide/workspace/folders.md) that corresponds to different departments, and each level can contain one or more workspaces to meet the branch division of various departments within the enterprise.

### G

- Garbage Collection

    Garbage Collection is a general term for the various mechanisms Kubernetes uses to clean up cluster resources. Kubernetes uses garbage collection mechanisms to clean up resources such as:

    - [unused containers and images](https://kubernetes.io/docs/concepts/architecture/garbage-collection/#containers-images)
    - [failed Pods](https://kubernetes.io//docs/concepts/workloads/pods/pod-lifecycle/#pod-garbage-collection)
    - [objects owned by target resources](https://kubernetes.io//docs/concepts/overview/working-with-objects/owners-dependents/)
    - [completed Jobs](https://kubernetes.io//docs/concepts/workloads/controllers/ttlafterfinished/)
    - expired or erroneous resources

- Gateway node

    A Gateway node is a worker node that mainly runs the Envoy open-source application, providing high-performance reverse proxy capabilities, supporting load balancing, routing, caching, custom routing, and other features. The number and performance of worker nodes will directly affect the performance of the gateway, so it is recommended to deploy enough worker nodes according to needs.

- Gateway Rule

    In a service mesh, [Gateway Rules](../mspider/user-guide/traffic-governance/gateway-rules.md) define the load balancer for north-south connection operations in the mesh, used to establish inbound and outbound HTTP/TCP access connections. It describes a set of ports, service domain names, protocol types, and SNI configurations for the load balancer that need to be exposed.

- Gauge

    A Gauge is a metric value that can be **both increased and decreased**. Gauges are mainly used to measure instantaneous data such as temperature and memory usage.

- GitOps

    GitOps is a set of best practices based on shared principles,
    applied to a workflow that depends on software agents that
    enable automation to reconcile a declared system state or configuration in a git repository.
    These software agents and practices are used to run a cohesive workflow that
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

- Gateway Rate Limit

    You can choose to add a gateway rate limiting component to support more traffic control capabilities. However, the rate limiting component can also cause some resource consumption and performance loss, and is not enabled by default. Please judge whether to enable it according to the actual situation.

- Grafana

    Grafana is an open-source visualization platform that provides a variety of monitoring data visualization panels.

- Group

    In global management, this refers to a combination of multiple users, that is, a [group](../ghippo/user-guide/access-control/group.md).

    In the microservice engine, this is a group of configurations in Nacos.

### H

- Heartbeat

    After the instance is started, the built-in Nacos client will actively send a heartbeat packet (HeartBeat) to the Nacos server every once in a while to indicate that the instance is still alive and avoid being removed by the server. The heartbeat packet contains information such as the name, IP, port, cluster name, and weight of the current service instance.

- Helm Chart

    A Helm Chart is a package consisting of a set of pre-configured K8s resources that can be managed using the Helm tool.

    The Chart provides a reproducible way to create and share K8s applications. A single Chart can be used to deploy a simple system (such as a memcached Pod), or a complex system (such as a complete web application stack consisting of HTTP servers, databases, caches, and other components).

- Histogram

    A histogram samples observation results (usually data such as request duration or response size) and statistically aggregates them into configurable buckets. There are several ways to generate a histogram (assuming the metric is `<basename>`):

    - Count by bucket, equivalent to `<basename>_bucket{le="<upper inclusive bound>"}`
    - Sum of sampled values, equivalent to `<basename>_sum`
    - Total number of sampled values, equivalent to `<basename>_count`, also equivalent to counting all sampled values in a bucket `<basename>_bucket{le="+Inf"}`

    Histogram can be understood as a bar chart, typically used for observation results such as request duration and response size. It can sample, group, and statistically aggregate observation results.

- Horizontal Pod Autoscaler, HPA

    Horizontal Pod Autoscaler is an API resource that scales Pod replicas based on target CPU utilization or custom metric targets.

    HPA is usually used on ReplicationController, Deployment, or ReplicaSet. HPA cannot be used on objects that do not support scaling, such as DaemonSet.

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

- HostAliases

    [HostAliases](https://kubernetes.io/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#hostalias-v1-core)
    is a list of hostnames and IP addresses that can be injected into the hosts file of a Pod.
    This option is only applicable to Pods that do not have hostNetwork configured.

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

- IAM, Identity and access management

    [IAM](../ghippo/user-guide/access-control/iam.md) stands for Identity and Access Management, which is a shorthand for user and access control in global management. An IAM Admin is the administrator with the highest level of permission in this module. Users or groups assigned as IAM Admin will have full and highest permission for user and access control.

- Image

    [Image](https://kubernetes.io/docs/concepts/containers/images/), on the other hand, refers to a saved container instance that packages a set of software required for application runtime. It is a way of packaging software, which can be stored in a container container registry, pulled to a local system, and run as an application. The metadata contained in the image specifies what executable program to run, who built it, and other information.

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

- Ingress

    [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)
    is an API object that manages external access to services in a Kubernetes cluster, typically for HTTP access.
    Ingress can provide load balancing, SSL termination, and name-based virtual hosting.

- [Init Container](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)

    Init Containers are one or more containers that must run to completion before the application container starts.
    The order of execution for Init Containers is that one must complete before the next one starts.

- Istio

    [Istio](https://istio.io/) is a free and open-source service mesh that provides a unified way to integrate microservices, manage traffic, enforce policies, and aggregate metric data. It does not require modification of application code and is a layer of infrastructure between services and the network.
    When combined with a service's deployment, it forms what is commonly referred to as a service mesh. Istio's control plane abstracts away the underlying cluster management platform, which can be Kubernetes, Mesosphere, and others.

### J, K

- [Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/)

    [Job](../kpanda/user-guide/workloads/create-job.md) is a deterministic or batch task that needs to run to completion. It creates one or more Pod objects and ensures that a specified number of Pods terminate successfully. As each Pod completes successfully, the Job tracks the number of successful completions.

- Kops

    [Kops](https://kubernetes.io/docs/setup/production-environment/tools/kops/)
    is a command-line tool that helps create, destroy, upgrade, and maintain production-grade, highly available Kubernetes clusters. Kops currently only supports AWS, and support for GCE, VMware vSphere, and other third-party PaaS platforms is still in alpha. You can also use your own cluster as a building block and construct a cluster using kubeadm. Kops is built on top of kubeadm.

- kube-apiserver

    [kube-apiserver](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/)
    is the control plane component that provides the Kubernetes API service. The Kubernetes API server validates and configures the data of API objects, including Pod, Service, replication controller, and others. The API server provides services for REST operations and provides a frontend for the shared state of the cluster. All other components interact with the frontend. The API server is a component of the Kubernetes control plane and is responsible for accepting requests. It is designed for horizontal scaling and can be scaled by deploying multiple instances. You can run multiple instances of kube-apiserver and balance traffic between them.

- kube-controller-manager

    [kube-controller-manager](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/)
    is a daemon that runs controllers on the master node and is responsible for running controller processes.
    Logically, each controller is a separate process, but for simplicity, they are compiled into the same executable and run in the same process.

- kube-proxy

    [kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/)
    is a network proxy that runs on each node in the cluster and is a component of the Kubernetes Service concept.
    kube-proxy maintains some network rules on the node that allow network sessions from inside or outside the cluster to communicate with Pods.
    If the operating system provides an available packet filtering layer, kube-proxy uses it to implement network rules. Otherwise, kube-proxy only does traffic forwarding.

- [kube-scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/)

    kube-scheduler is a control plane component that monitors newly created Pods that have not been assigned to a running node and selects a node for them to run on. Scheduling decisions consider factors such as the resource requirements of a single Pod or a set of Pods, hardware and policy constraints, affinity and anti-affinity specifications, data locality, workload interference, and deadlines.

- [Kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/)

    Kubeadm is a tool for quickly installing Kubernetes and building a secure and stable cluster. You can use Kubeadm to install control plane and worker node components.

- kubectl

    [kubectl](https://kubernetes.io/docs/reference/kubectl/) is a command-line tool for communicating with a Kubernetes cluster. You can use kubectl to create, inspect, update, and delete Kubernetes objects.

- kubelet

    [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/) is a command-line tool for communicating with a Kubernetes cluster. You can use kubectl to create, inspect, update, and delete Kubernetes objects.

    kubelet is a proxy that runs on each node in the cluster and ensures that containers run in Pods. kubelet receives a set of PodSpecs provided by various mechanisms and ensures that the containers described in these PodSpecs are running and healthy. kubelet does not manage containers that are not created by Kubernetes.

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

    [Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/) provides Kubernetes functionality services through a RESTful interface and is responsible for storing the cluster state. Kubernetes resources and "intention records" are stored as API objects and can be modified by calling the RESTful API. The API allows for declarative management of configurations. Users can interact directly with the Kubernetes API or through tools like kubectl. The core Kubernetes API is very flexible and can be extended to support custom resources.

### L

- Label

    A label is used to set identifiable attribute tags for objects; these tags are meaningful and important to users.

    Labels are key-value pairs associated with objects like Pods. They are typically used to organize and select subsets of objects.

- LimitRange

    LimitRange provides constraints to limit the resource consumption of each container or Pod in a namespace.

    LimitRanges limit the number of objects that can be created in a namespace by type, as well as the amount of compute resources a single container or Pod can request/use.

- Load Balancer

    A load balancer is a method of distributing incoming network traffic among a group of backend servers. This solution can be software or hardware-based.

    This helps to address issues related to high availability and distributed systems. When dealing with applications or services that need to scale to hundreds of thousands of users, it is often necessary to distribute the application across multiple servers. Load balancers act as the "traffic cops" routing traffic and clients to the appropriate backend server.

    Load balancers serve as the frontend for network traffic and clients. They typically have multiple methods for checking which servers are up and handling requests with the lowest load.

- [Log](https://opentelemetry.io/docs/concepts/signals/logs/)

    In Insight, [logs](../insight/user-guide/data-query/log.md) are a list of events recorded by the cluster or application. They are an abstract data type that changes during system operation and consists of an ordered collection of operations and their operation results for a specified object over time.

    Application and system logs can help you understand what is happening inside the cluster. Logs are useful for debugging issues and monitoring cluster activity.

- Loosely coupled architecture

    A loosely coupled architecture (the opposite paradigm of tightly coupled architecture) is an architectural style in which the various components of an application are built independently of each other. Each component, sometimes called a microservice, is built to perform a specific feature so that it can be used by any number of other services. Implementing this pattern is usually slower than tightly coupled architecture. But there are many benefits, especially as the application continues to scale. Loosely coupled applications allow teams to develop, deploy, and scale independently, which allows organizations to iterate quickly on individual components. Application development is faster, and team structures can be built around the capabilities of the application.

### M

- Managed Control Plane

    A managed control plane is a control plane that is managed for customers. It reduces the complexity of customer deployments and typically guarantees a certain level of performance and availability.

- Hosted Mesh

    A control plane created and managed by a service mesh in a selected cluster. It is characterized by simplicity, low cost, high availability, and no separate operation and maintenance management.

- Managed Service

    A managed service is a software product whose operation and management are handled by a third party. Examples include database-as-a-service products like Amazon RDS or external monitoring services like Datadog.

    Managing software is complex, especially when considering the variety of different technologies included in modern tech stacks. And having internal experts who are capable of managing everything to the fullest extent is either too expensive or would consume valuable engineering time. Your team should be focused on building new features, not handling operational tasks that can easily be solved through outsourcing.

    Managed services are ready to use from the start and have very low operational overhead. Managed services have well-defined, typically API-driven boundaries that make it easy for organizations to effectively outsource tasks that fall outside their core competencies.

- Manifest

    A serialization specification for one or more Kubernetes API objects.

    A manifest specifies the desired state of objects that Kubernetes will maintain when applying the manifest. Each configuration file can contain multiple manifests.

- Master cluster

    A master cluster is a cluster with a control plane. A mesh can have more than one master cluster for HA or low-latency use cases. A master cluster can serve as the control plane for a working cluster.

- [Metric](https://opentelemetry.io/docs/concepts/signals/metrics/)

    A description of performance data or status data for a resource, metrics consist of a namespace, dimensions, metric name, and unit. They are a series of labeled data that can fully reflect the monitored object's operation or business status.

- Metadata

    Metadata is descriptive information about data, or data about data, such as service version, various custom tags, etc. Metadata is divided into service-level metadata, cluster metadata, and instance metadata.

- Microservice

    A microservice is an architectural style that builds a single application by combining multiple small services. In a microservice engine, a microservice refers to the various small services obtained by splitting a complete application according to business features.

    Microservices are a modern approach to application development using cloud-native technologies. Although modern applications like Netflix appear to be a single application, they are actually a collection of smaller services that work closely together. For example, a single page that allows you to access, search, and preview videos is likely provided by smaller services, each of which handles one aspect (such as search, authentication, and running previews in the browser). In short, microservices refer to an application architecture pattern that is typically contrasted with monolithic applications.

    Microservices are a response to the challenges posed by monolithic applications. In a monolithic application, different parts of the application cannot be separately deployed or scaled. This can lead to inefficient resource utilization and high coupling between different parts of the codebase. Microservices address these issues by separating functionality into different services that can be independently deployed, updated, and scaled. This allows different teams to focus on their own small part of the application, without negatively impacting other parts of the organization.

    However, microservices also come with increased operational overhead, as there are more things to deploy and track. Many cloud-native technologies aim to make microservices easier to deploy and manage.

- Microservice instance

    A microservice instance is a single instance of a microservice deployed on a container or virtual machine. Multiple instances of a microservice can run simultaneously. A microservice instance group is a grouping of all instances of a microservice based on demand.

- Microservice instance group

    This refers to a group after division of microservice instances by following a customer requirements.

- Monolithic Apps

    Monolithic applications contain all functionality in a single deployable program. While this is the simplest and easiest way to create an application, it can become difficult to maintain as the complexity of the application increases. A well-designed monolith can adhere to lean principles and be the simplest way to start and run an application. Once the business value of the monolith has been proven, it can be broken down into microservices.

- Multitenancy

    Multitenancy refers to providing services to multiple tenants through a single software installation. Tenants can be individual users or groups of users/applications that use their own data sets to manipulate the same software. Multitenancy software provides each tenant with an isolated environment for their work data, settings, and credential lists, while providing services to multiple tenants. This saves resources and maintenance effort, ultimately reducing software costs.

- Mutual Transport Layer Security, mTLS

    A security protocol that provides mutual authentication and encryption for messages sent between two services. It ensures that there is no unauthorized party listening or impersonating legitimate requests, and prevents attacks such as path traversal, credential stuffing, and brute force attacks.

### N

- Nacos cluster node roles

    In the Raft protocol used by Nacos, there are two roles for nodes: Leader and Follower. The Leader handles all requests and writes them to the local log and synchronizes the log with other nodes, while the Follower receives update requests from the Leader and writes them to the local log, and submits the log when notified by the Leader.

- Name

    A string provided by the client that identifies an object in the resource URL, such as `/api/v1/pods/some-name`.
    At any given time, only one object of a given type can have a given name. However, if the object is deleted, a new object with the same name can be created.

- [Namespace](../kpanda/user-guide/namespaces/createns.md)

    An abstraction used by Kubernetes to support the isolation of resource groups within a single cluster. Objects within the same namespace must have unique names, but there is no requirement for names to be unique across namespaces. Namespace-based scoping only applies to objects within the namespace, not to cluster-scoped objects.

- Network Policy

    A specification that defines how communication can occur between Pod groups and between Pods and other network endpoints. Network policies help you declaratively configure which Pods and namespaces are allowed to communicate with each other, and which port numbers are used to run each policy.

- Node

    [Node](../kpanda/user-guide/nodes/add-node.md) is a computer that can work with other computers (or nodes) to complete a common task. In cloud computing, a node can be a physical machine, a virtual machine, or even a container. Nodes provide a unique computing unit (memory, CPU, network) that can be allocated to a cluster.

- Node Pressure Eviction

     process in which the kubelet actively causes Pods to fail to reclaim resources on a node. The kubelet monitors CPU, memory, disk space, and file system inode resources on cluster nodes. When one or more of these resources reaches a specific consumption level, the kubelet can actively invalidate one or more Pods on the node to reclaim resources and prevent starvation.

- Notification

    When an alert is generated due to an abnormality in a resource, the alert information can be sent to specified users via email, DingTalk, WeCom, webhook, etc.

### O

- Object

    Kubernetes objects are entities in the Kubernetes system that represent a portion of the cluster's state. The Kubernetes API uses these objects to represent the state of the cluster. Once an object is created, the Kubernetes control plane continuously works to ensure that the object's represented state exists. Creating an object is equivalent to telling the Kubernetes system what you expect a portion of the cluster's workload to look like, which is the expected state of your cluster.

- Objective

    It is the objectives that Prometheus captures. These objectives expose their own state or proxy the state of the monitored objects' operation and business metrics.

- Observability

    [Observability](../insight/intro/index.md) refers to the ability to collect signals from an observed system, continuously generate and discover actionable insights. In other words, observability allows users to gain insight into the state of a system from external outputs and take corrective action. The measuring mechanism of a computer system observes low-level signals such as CPU time, memory, and disk space, as well as high-level signals and business signals such as API response rate per second, error rate per second, and number of transactions processed per second.

    The observability of a system has a significant impact on its operational and development costs. An observable system provides meaningful and actionable data to operators, enabling them to achieve favorable results (i.e., faster event response, higher development efficiency) and fewer difficult moments and shorter downtime.

- Operator

    An operator is a way to package, deploy, and manage Kubernetes applications.

- Operator Pattern, Operator 模式

    The [operator pattern](https://kubernetes.io//docs/concepts/extend-kubernetes/operator/) is a specialized controller for managing custom resources. The operator pattern is a system design that associates controllers with one or more custom resources. In addition to using built-in controllers that are part of Kubernetes itself, you can also extend Kubernetes by adding controllers to the cluster. If a running application can act as a controller and manipulate tasks defined in custom resources in the control plane through API access, this is an example of an operator pattern.

- OverridePolicy

    [OverridePolicy](../kairship/policy/override.md) is a differentiated configuration policy that defines the differentiated configuration policy for distributing multicloud resource objects to different working clusters, such as using different images and adding different labels in different working clusters. OverridePolicy, as an independent policy API, can automatically handle cluster-related configurations, such as adding different prefixes to images based on the geographical distribution of subsets of clusters and using different StorageClasses based on your cloud provider.

### P

- Permission

    [Permissions](../ghippo/user-guide/access-control/iam.md) refer to whether a user is allowed to perform a certain operation on a certain resource. In order to reduce the threshold for use, DCE adopts the RBAC model to aggregate permissions into roles. Administrators only need to authorize roles to users, and the user will obtain a set of permissions aggregated under that role.

    By default, IAM users created by administrators have no role permissions. They need to be granted roles individually or added to groups and granted roles in order to obtain corresponding role permissions. This process is called authorization. After authorization, users can operate on platform resources based on the role permissions granted to them.

- Persistent Volume Claim, PVC

    A PVC is used to claim the storage resources defined in a persistent volume so that it can be mounted as a volume in a container.

    It specifies the amount of storage, how to access the storage (read-only, read-write, or exclusive), and how to reclaim the storage (retain, recycle, or delete). The detailed information of the storage is in the PersistentVolume object.

- Persistent Volume, PV

    A PV is an API object that represents a block of storage space in the cluster. It is a universal, pluggable, and persistent resource that is not constrained by the lifecycle of a single Pod.

    The PV provides an API that abstracts the details of the storage supply method and separates it from the usage method. In the scenario of creating storage in advance (static supply), the PV can be used directly. In the scenario of providing storage on demand (dynamic supply), PersistentVolumeClaims (PVC) are needed.

- Platform as a service, PaaS

    PaaS is an external platform on which application development teams deploy and run their applications. Heroku, Cloud Foundry, and App Engine are examples of PaaS products.

    To make good use of cloud-native patterns such as microservices or distributed applications, operations teams and developers need to be able to eliminate a lot of operational work, including provisioning infrastructure, handling service discovery and load balancing, and scaling applications.

    PaaS provides application developers with general infrastructure tools in a fully automated way. It enables developers to understand the infrastructure and reduce their concerns about it, and to spend more time and energy writing application code. It also provides some monitoring and observability to help application teams ensure that their applications are healthy.

- Pilot

    Pilot is a component in the service mesh that controls the Envoy proxy and is responsible for service discovery, load balancing, and routing.

- Pod

    A Pod represents a group of running containers on the cluster. The Pod is an atomic object in Kubernetes and is an instance of a workload deployed in Kubernetes.

    Typically, a Pod is created to run a single main container. A Pod can also run optional sidecar containers to add supplementary features such as logging. Pods are usually managed by Deployments.

    The Pod contains one or more containers that share storage and network, as well as specifications for how to run the containers.

- Pod Disruption Budget (PDB)

    A Pod Disruption Budget is an object that ensures that the number of Pods in a multi-instance application does not fall below a certain number during voluntary disruptions.

    PDB cannot prevent non-voluntary disruptions, but they are counted towards the budget.

- Pod Disruption

    The process of actively or non-actively terminating Pods on a node.

    Voluntary disruptions are initiated by application owners or cluster administrators. Non-voluntary disruptions are unintentional and may be triggered by unavoidable issues such as node resource exhaustion or accidental deletion.

- [Pod Lifecycle](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)

    It refers to what phase a pod is currently running in.

    Here is a brief overview of the different phases a Pod can be in during its lifecycle:

    - Running
    - Pending
    - Succeeded
    - Failed
    - Unknown

    For a higher-level description of a Pod's phase, please refer to the `phase` field in the [PodStatus](https://kubernetes.io/docs/reference/generated/kubernetes-api/{{< param "version" >}}/#podstatus-v1-core) object.

- Pod Priority

    [Pod priority](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#pod-priority) is a way to indicate the relative importance of a Pod compared to others. It allows users to set a priority for a Pod that is higher or lower than other Pods, which is an important feature for production cluster workloads.

- Pod Security Policy

    Pod security policy enables fine-grained authorization for creating and updating Pods. It is a cluster-level resource that controls security-sensitive content in Pod specifications. The `PodSecurityPolicy` object defines a set of conditions and default values for related fields that Pods must satisfy at runtime. Pod security policy is implemented as an optional admission controller.

    PodSecurityPolicy has been deprecated since Kubernetes v1.21 and removed in v1.25. As an alternative, use [Pod Security Admission](https://kubernetes.io/docs/concepts/security/pod-security-admission/) or third-party admission plugins.

- Policy as code, PaC

    Policy as code (PaC) is the practice of storing policy definitions as one or more machine-readable and processable format files. This replaces the traditional model of documenting policies in separate human-readable documents. PaC is useful for enforcing policies that constrain the building of applications and infrastructure, such as prohibiting storing secrets in source code, running containers with superuser privileges, or storing certain data outside of specific geographic regions. By using PaC, system properties and operations can be automatically checked. Best practices for software development also apply to building PaC, such as using Git and related workflows.

- Portability

    Portability is a software feature that is a form of reusability and helps avoid being "locked" into certain operational environments, such as cloud providers, operating systems, or vendors. Traditional software is often built for specific environments (e.g., AWS or Linux), while portable software can work in different operational environments without significant rework. If the amount of work required to adapt an application to a new environment is reasonable, the application is considered portable. The term "porting" implies modifying software to make it work on different computer systems.

- [Preemption](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#preemption)

    Preemption logic in Kubernetes helps suspended Pods find suitable nodes by evicting low-priority Pods on nodes. If a Pod cannot be scheduled, the scheduler will attempt to preempt lower-priority Pods to make it possible to schedule the suspended Pod.

- Prometheus

    Prometheus is a combination of open-source monitoring, alerting, and time-series database.

- PromQL

    PromQL is the built-in data query language in Prometheus, which provides rich query, aggregation, and logical operation capabilities for time-series data.

- PropagationPolicy

    In Multicloud Management, [PropagationPolicy](../kairship/policy/propagation.md) defines the distribution strategy for multicloud resource objects, supporting planning which workloads to deploy to which working clusters using specified clusters or labels. PropagationPolicy is an independent policy API that can define multicluster scheduling methods based on distribution requirements.

    - Supports 1:n `policy:workload`, and users do not need to repeat the scheduling constraints each time they create a multicloud application.
    - When using the default policy, users can interact directly with the Kubernetes API.

- Proxy

    In computer science, a proxy is a server that acts as an intermediary for requests from clients seeking resources from other servers. The client interacts with the proxy, which copies the client's data to the actual server. The actual server replies to the proxy, which sends the actual server's response to the client. [kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/) is a network proxy running on each node in the cluster that implements some Kubernetes Service concepts. You can run kube-proxy as a regular user-space proxy service. If your operating system supports it, you can run kube-proxy in mixed mode, which achieves the same overall effect with fewer system resources.

### R

- RBAC

    Role-Based Access Control (RBAC) allows administrators to dynamically configure access policies through the Kubernetes API. RBAC uses [roles](../ghippo/user-guide/access-control/role.md) (which contain permission rules) and role bindings (which grant a group the permissions defined in a role).

- Registration center

    The registration center is like a "phone book" for microservices, responsible for recording the mapping relationship between services and service addresses. The microservice engine supports several types of registration centers, including Eureka, Zookeeper, Nacos, Mesh, and Kubernetes.

- Reliability

    From a cloud-native perspective, reliability refers to a system's ability to respond to failures. If we have a distributed system that can continue to work through infrastructure changes and individual component failures, then it is reliable. On the other hand, if it is prone to failure and requires manual intervention by operators to keep it running, then it is unreliable. The goal of cloud-native applications is to build inherently reliable systems.

- ReplicaSet

    ReplicaSet is the next-generation replication controller. Like the ReplicationController, it ensures that a specified number of Pod replicas are running at any given time. However, ReplicaSet supports new collection-based selector requirements (described in the user guide for labels), while the ReplicationController only supports equality-based selector requirements.

- Replication Controller

    The Replication Controller is an (deprecated) API object that manages multi-replica applications. It is a workload that manages multiple replica applications and ensures that a specific number of Pod instances are running. The control plane ensures that the specified number of Pods are running, even if some Pods fail, such as when you manually delete them or start too many Pods due to other errors. The ReplicationController has been deprecated. Please refer to Deployment for similar functionality.

- Resource

    Resource refers to the specific data that completes authorization on the DCE platform through various sub-modules. Typically, a resource describes one or more objects of operation, and each sub-module has its own resources and corresponding resource definition details, such as clusters, namespaces, gateways, etc. The owner of the resource is the main account Super Admin. Super Admin has the authority to create/manage/delete resources in each sub-module. Ordinary users do not automatically have access to resource access rights without authorization from Super Admin. The workspace supports cross-sub-module authorization of user (group) access to resources.

- Resource limit

    The limit value is the upper limit of available resources for an instance. The request value is less than the limit value.

- Resource Quota

    [Resource quotas](../ghippo/user-guide/workspace/quota.md) provide constraints on the total resource consumption of each namespace. They limit the number of objects that can be created in a namespace and also limit the total amount of computing resources that can be used by resource objects in the project.

- Resource request

    The request value specifies how much available resources are pre-allocated for an instance.

- Resource Template

    In [Multicloud Management](../kairship/intro/index.md), a template called a federated resource is used. This is a multicloud resource template based on the native K8s API, which facilitates the integration of all cloud-native tools within the K8s ecosystem. This resource template can be used to centrally manage [multicloud services](../kairship/resource/service.md), [multicloud namespaces](../kairship/resource/ns.md), [multicloud configmap](../kairship/resource/configmap.md), and [multicloud secret](../kairship/resource/secret.md).

- Role

    A [role](../ghippo/user-guide/access-control/role.md) is a bridge that connects users and permissions.
    A role corresponds to a set of permissions, and different roles have different permissions. Granting a
    user a role means granting all the permissions included in that role.
    There are two types of roles in global management:

    - predefined roles created by the system that users can only use and cannot modify, and
    - custom roles that users can create, update, and delete themselves.

    The permissions in custom roles are maintained by the users themselves. At the same time, because global management brings together multiple sub-modules, each sub-module also has a corresponding administrator role, such as IAM Admin, which manages user and access control, i.e., managing users/groups and authorizations, Workspace Admin, which manages hierarchy and workspace permissions, and only this permission can create hierarchy, and Audit Admin, which manages audit logs.

- Rolling update

    [Rolling update](../mspider/install/istio-update.md) refers to updating a small portion of replicas at a time, then updating more replicas after success, and finally completing the update of all replicas. The biggest advantage of rolling updates is zero downtime, with replicas running throughout the update process, ensuring business continuity.

- Routing Rule

    In the virtual service configured in the service mesh's [virtual service](../mspider/user-guide/traffic-governance/virtual-service.md), the routing rules follow the path defined by the service mesh for requests. Using routing rules, you can define the workload to which traffic addressed to the virtual service host is routed. Routing rules allow you to control traffic to achieve tasks such as phased traffic distribution by percentage.

### S

- Scalability

    Scalability refers to how much a system can grow. This is the ability to add capacity to do anything a system should do. For example, a Kubernetes cluster scales by adding or removing containerized applications, but this scalability depends on several factors. How many nodes it has, how many containers each node can handle, how many records and operations the control plane can support?

    Scalable systems make it easier to add more capacity. There are two main scaling methods. On the one hand, horizontal scaling adds more nodes to handle increased load. In contrast, in vertical scaling, a single node is more powerful and can perform more transactions (for example, by adding more memory or CPU to a single machine). Scalable systems can easily change and meet user needs.

- Secret

    [Secret](../kpanda/user-guide/configmaps-secrets/create-secret.md) is used to store sensitive information such as passwords, OAuth tokens, and SSH keys.

    Secrets allow users to have more control over how sensitive information is used and reduce the risk of accidental exposure. By default, secret values are encoded as base64 strings and stored in unencrypted form, but can be configured for [static encryption (Encrypt at rest)](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/#ensure-all-secrets-are-encrypted).

    Pods can reference secrets in various ways, such as in volume mounts or as environment variables. Secrets are designed for confidential data, while [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/) is designed for non-confidential data.

- Security Context

    The `securityContext` field defines privilege and access control settings for a Pod or container, including the runtime UID and GID.

    In a `securityContext` field, you can set the user and group to which the process belongs, permission-related settings. You can also set security policies (such as SELinux, AppArmor, seccomp).

    The `PodSpec.securityContext` field configuration applies to all containers in a Pod.

- Selector

    Selector operators allow users to filter a set of resource objects by label.

    When querying a resource list, selector operators can filter resources by label.

- Serverless

    Serverless is a cloud-native development model that allows developers to build and run applications without
    managing servers. There are still servers in Serverless, but they are abstracted away from application development.
    Cloud providers handle the daily work of configuring, maintaining, and scaling server infrastructure. Developers
    can simply package their code in containers for deployment. After deployment, the Serverless application responds
    to demands and automatically scales up and down as needed. Public cloud providers' Serverless products typically
    meter on an event-driven execution model. Therefore, when the serverless feature is idle, it does not incur any costs.

    In the standard infrastructure as a service (IaaS) cloud computing model, users purchase capacity units in advance,
    which means that you need to pay the public cloud provider for the cost of the server components that are always
    online to run your application. Users are responsible for scaling server capacity when demand is high and reducing
    capacity when it is no longer needed. Even when the application is not in use, the cloud infrastructure required to
    run the application remains active.

    In contrast, using a Serverless architecture, the application only starts when needed. When an event triggers the
    application code to run, the public cloud provider dynamically allocates resources for that code. When the code
    execution is complete, the user stops paying for the resources. In addition to cost and efficiency advantages,
    Serverless also frees developers from the daily and tedious tasks associated with application scaling and server
    configuration. With Serverless, tasks such as managing operating systems and file systems, security patches,
    load balancing, capacity management, scaling, logging, and monitoring are all handed over to cloud service providers.

- Service

    Please note that in IT, the term "service" has multiple meanings. In this definition, we will focus on the more traditional definition: services in microservices. The difference between services and microservices, if any, is subtle and different people may have different opinions. In a higher-level definition, we will treat them as the same. Please refer to the definition of microservices for more details.

    The set of pods targeted by a service is typically determined by a selector. If a pod is added or removed, the set of pods matched by the selector will change. The service ensures that network traffic can be directed to the current set of pods for that workload.

- ServiceAccount

    Provides identity for processes running in a pod.

    When processes in a pod access the cluster, the API server authenticates them as a specific service account, such as default. If you don't specify a service account when you create a pod, it will be automatically assigned the default service account in the same namespace.

- Service Catalog

    The service catalog is an extension API that makes it easy for applications running in a Kubernetes cluster to use externally hosted software services, such as data warehousing services provided by cloud providers.

    The service catalog can retrieve, supply, and bind externally hosted services (Managed Services) without knowing how those services are created and managed.

- Service Discovery

    Service discovery is the process of finding the various instances that make up a service. Service discovery tools continuously track the various nodes or endpoints that make up a service.

    Cloud-native architectures are dynamic and uncertain, which means they are constantly changing. Containerized applications may start and stop multiple times during their lifecycle. Each time this happens, it has a new address, and any application that wants to find it needs a tool to provide the new address information.

    Service discovery continuously tracks applications in the network so that they can find each other when needed. It provides a common place to look up and identify different services. The service discovery engine is a database-like tool used to store which services are currently available and how to find them.

- Service Entry

    In a service mesh, a service entry is used to add an internal service (such as a VM) or an external server that cannot be registered with the service registry to the service mesh abstract model. After a service entry is added, the Envoy proxy can send traffic to that service, which will be treated like any other service in the mesh.

- Service Mesh

    In the concept of microservices, applications are broken down into smaller services that communicate over the network. Like your WIFI network, computer networks are inherently unreliable, hackable, and often slow. Service mesh solves this series of new challenges by managing the traffic (i.e., communication) between services and unifying reliability, observability, and security features across all services.

    After transitioning to a microservices architecture, engineers now have to deal with hundreds or even thousands of individual services that need to communicate. This means a lot of traffic is being transmitted back and forth over the network. In addition to this, a single application may need to encrypt communication to support regulatory requirements, provide common metrics for the operations team, or provide detailed insights into traffic to help diagnose issues. If these features were built into a single application, each one would cause conflicts between teams and slow down the development of new features.

    The service mesh adds reliability, observability, and security features to all services in the cluster without changing the code. Before the service mesh, these features had to be coded into each service and become the source that causes bugs and technical traps.

- Service Name

    The service name is the unique identifier for a service in a service mesh. It must be unique and is independent of the service's version.

- Service Operator

    The Service Operator manages services in the service mesh by manipulating configuration states and monitoring the services' runtime status through various dashboards.

- Service Proxy

    The Service Proxy intercepts traffic in and out of a service, applies some logic to it, and then forwards the traffic to another service. It collects data on network traffic and decides whether to apply rules to it. The proxy provides insight into the types of communication happening between services and decides where to send a particular request or even reject it. It collects critical data, manages routing (distributing traffic evenly between services or rerouting when some services are down), encrypts connections, and caches content (reducing resource consumption).

- Service Registry

    The Service Registry is an internal service registry maintained by the service mesh that contains a set of services running in the service mesh and their corresponding service endpoints. The service mesh uses the service registry to generate Envoy configurations.

- Self Healing

    A self-healing system can recover from certain types of failures without any human intervention. For example, DCE 5.0 has a "convergence" or "control" loop that actively checks the system's actual state against the operator's initial expected state. If there is a difference (e.g., the number of running application instances is less than the expected number), the system will automatically take corrective action (e.g., start new instances or pods).

- Shuffle Sharding

    Shuffle sharding is a technique for assigning requests to queues that has better isolation than hashing the number of queues. It is used to ensure that high-density request sequences do not overwhelm low-density ones. The technique involves hashing certain feature values of the request, shuffling a deck of cards based on the resulting hash value, and then selecting the shortest checked queue as the target queue for the request.

- Site Reliability Engineering

    Site Reliability Engineering (SRE) is a discipline that combines operations and software engineering, particularly for infrastructure and operational issues. SRE engineers build systems to run applications rather than building product features. They ensure that applications run reliably by monitoring performance, setting up alerts, debugging, and troubleshooting. Without these features, operators can only react to problems rather than proactively avoiding them, and downtime is only a matter of time. SRE continuously measures and monitors infrastructure and application components. When problems arise, the system prompts SRE engineers when, where, and how to fix them. This approach helps create highly scalable and reliable software systems through automated tasks.

- Software as a service

    Software as a Service (SaaS) allows users to connect to or use cloud services over the internet. Common examples include email, calendars, and office tools (e.g., Gmail, AWS, GitHub, Slack). SaaS provides a complete software solution on a pay-as-you-go basis. All maintenance tasks and application data are handled by the service provider. Traditional commercial software is installed on separate computers and requires administrators to maintain and update it. SaaS applications work without any special effort from the internal IT department. These applications are installed, maintained, upgraded, and secured by the provider. Scalability, availability, and capacity issues are handled by the service provider on a pay-as-you-go basis. For organizations that want to use enterprise-level applications, SaaS is an affordable option.

- Stateful Apps

    When we talk about stateful (and stateless) applications, state refers to any data that the application needs to store To function as designed. For example, any online store that remembers your shopping cart is a stateful application. Using an application typically requires multiple requests. For example, when using online banking, you will verify your identity by entering a password (request #1), then transfer money to a friend (request #2), and finally view the transfer details (request #3). To function properly, each step must remember the previous steps, and the bank needs to remember each person's account status. There are several ways to store state for stateful applications. The simplest is to store the state in memory rather than persisting it anywhere else. The problem with this approach is that all state is lost every time the application must restart. To prevent this, state is persisted locally (on disk) or in a database system.

- StatefulSet

    [StatefulSet](../kpanda/user-guide/workloads/create-statefulset.md) is used to manage a set of Pods with persistent storage and identifiers. Each Pod has a unique, immutable ID.

- Stateless Apps

    It refers to applications that do not store any client session data on the server. Each session is treated as a new request, and responses are not dependent on previous data.

- Static Pod

    a Pod managed directly by the kubelet daemon on a specific node, not visible to the API server.

- StorageClass

    This is a way for administrators to describe available storage types, with fields for `provisioner`, `parameters`, and `reclaimPolicy`.

- sysctl

    This is an interface for getting and setting Unix kernel parameters.

- Summary

    This is a way to sample and summarize observation results, with options for quantiles, sum, and count.

### T

- Taint

    [Taint](../kpanda/user-guide/nodes/taints.md) is a core object that contains three required attributes: key, value, and effect. Taints prevent Pods from being scheduled on nodes or node groups. Taints work with tolerations to ensure that Pods are only scheduled on nodes with tolerations that match the taints. One or more taints can be marked on the same node. Nodes should only schedule Pods with tolerations that match the taints.

- Temporary microservice instance

    A temporary microservice instance is a microservice instance that cannot be persistently stored on the Nacos server. Temporary microservice instances need to be kept alive by reporting heartbeats. If no heartbeat is reported within a certain period of time, the Nacos server will remove the instance.

- Threshold

    A threshold is a floating-point number between 0 and 1. When the number of healthy instances is less than this value, regardless of whether the instance is healthy or not, the instance will be returned to the client. This prevents healthy instances from being overwhelmed by traffic and causing a cascading effect.

- Tightly Coupled Architecture

    A tightly coupled architecture is an architecture style in which many application components depend on each other. This means that a change to one component may affect other components. It is usually easier to implement than a loosely coupled architecture, but it makes the system more susceptible to cascading failures. It also means that the deployment of each component needs to be coordinated, which can slow down developers' productivity. A tightly coupled application architecture is a fairly traditional way of building applications. In some specific cases, it can be useful when we don't need to be consistent with all the best practices of microservice development. This means faster and simpler implementation, similar to a monolithic application, which can speed up the initial development cycle.

- Toleration

    A toleration is a core object that consists of three required attributes: key, value, and effect. Tolerations allow Pods to be scheduled on nodes or node groups with corresponding taints. Tolerations and taints work together to ensure that Pods are not scheduled on unsuitable nodes. One or more tolerations can be set on the same Pod. Tolerations indicate that it is allowed (but not necessary) to schedule Pods on nodes or node groups that contain corresponding taints.

- Transport Layer Security

    Transport Layer Security (TLS) is a protocol designed to provide higher security for network communication. It ensures the secure delivery of data sent over the Internet, avoiding possible data monitoring and/or tampering. The protocol is widely used in applications such as messaging and email. Without TLS, sensitive information such as web browsing habits, email communication, online chat, and teleconferencing can be easily tracked and tampered with during transmission. Enabling support for TLS on server and client applications ensures that the data transmitted between them is encrypted and cannot be viewed by third parties. TLS uses multiple encoding techniques to provide security when transmitting data over the network. It allows for an encrypted connection between client applications and servers (such as browsers and bank sites). It also allows client applications to actively identify the servers they are calling, reducing the risk of client communication with fraudulent sites. This ensures that third parties cannot view and monitor data transmitted between applications using TLS, protecting sensitive privacy information such as credit card numbers, passwords, and locations.

- [Trace](https://opentelemetry.io/docs/concepts/signals/traces/)

    A trace records processing information within a single request scope, including
    service calls and processing duration data. A trace has a unique Trace ID and is composed of multiple Spans.

### U, V

- UID

    A string generated by the Kubernetes system to uniquely identify objects. Each object
    created throughout the lifecycle of a Kubernetes cluster has a different UID, which is
    intended to differentiate historical events of similar entities.

- User

    A [user](../ghippo/user-guide/access-control/user.md) is the subject who initiates an operation, each user has a unique ID and is granted different roles. The IAM users created by default have no permissions and need to be added to groups, granted roles or policies to gain corresponding permissions.

    Users log in to DCE with their usernames and operate platform resources and services according to the permissions granted to them. Therefore, users are the subjects of resource ownership and have corresponding permissions for the resources they own.

    Users can modify user information, set passwords, access keys, and UI languages in the personal center.

- user namespace

    A Linux kernel feature that simulates superuser privileges for non-privileged users. It is used to simulate the kernel feature of the root user to support "Rootless containers".

    user namespace is a Linux kernel feature that allows non-root users to simulate the privileges of the superuser ("root"), for example, to run containers without having to be a superuser outside the container.

    user namespaces are effective in mitigating potential container escape attacks.

    In the context of user namespaces, namespaces are a Linux kernel feature rather than the namespace concept in Kubernetes.

- Version Control

    Source code management (or version control) is a behavior that tracks and manages document changes. It is a system that continuously records changes to a single file or group of files so that you can roll back to a specific version later.

    Version control systems are dedicated to solving the following problems: backing up documents or code repositories that change over time, resolving conflicts when multiple users make cross-modifications, and storing change logs over time.

    Handling critical business application code is often complex and important, so it is very important to track who changed the content, when, and why. In addition, many (even most) applications are modified by multiple developers, and conflicts often exist between changes introduced by different developers.

    Version control can help developers act quickly and maintain efficiency while storing change records and providing tools to resolve conflicts. It can store application code in a code repository and simplify collaboration between developers. Modern application development relies heavily on version control systems such as git to store their code.

- Vertical Scaling

    Vertical scaling, also known as "up and down scaling", is a technique that increases system capacity by adding CPU and memory to a single node when the workload increases. Assuming you have a computer with 4GB of RAM and want to increase its capacity to 16GB of RAM, vertical scaling means switching to a 16GB RAM system. (See horizontal scaling for different scaling methods.)

    As the demand for an application grows beyond the current capacity of the application instance, we need to find a way to scale the system. We can add more computing resources to existing nodes (vertical scaling) or add more nodes to the system (horizontal scaling). Scalability helps improve competitiveness, efficiency, reputation, and quality.

    Vertical scaling allows you to adjust server size without changing the application code. This is in contrast to horizontal scaling, where the application must be able to be replicated for scaling, which may require code updates. Vertical scaling increases the capacity of existing applications by adding computing resources, allowing applications to handle more requests and perform more work at the same time.

- Virtual Machine

    A virtual machine (VM) is a computer and its operating system that is not constrained by specific hardware. Virtual machines rely on virtualization to partition a physical computer into multiple virtual machines. This separation allows organizations and infrastructure providers to easily create and destroy virtual machines without affecting the underlying hardware.

    Virtual machines take advantage of virtualization. When a bare-metal machine is bound to a single operating system, the use of resources on that machine is limited. In addition, when an operating system is bound to a single physical machine, its availability is directly tied to that hardware. If the physical machine goes offline due to maintenance or hardware failure, the operating system also goes offline.

    By eliminating the direct relationship between the operating system and a single physical machine, you solve several problems with bare-metal: configuration time, hardware utilization, and elasticity.

    Since you don't need to buy, install, or configure new hardware to support it, the configuration time for new computers is greatly improved. Virtual machines allow you to better utilize existing physical hardware resources by placing multiple virtual machines on a single physical machine. Virtual machines are also more elastic than physical machines because they are not tied to a specific physical machine. When a physical machine needs to be taken offline, the virtual machines running on it can be moved to another machine with almost no downtime.

- Virtualization

    Virtualization, in the context of cloud-native computing, refers to the process of taking a physical computer, sometimes called a server, and allowing it to run multiple isolated operating systems. These isolated operating systems and their dedicated computing resources (CPU, memory, and networking) are called virtual machines or VMs. When we talk about a virtual machine, we are talking about a software-defined computer. It looks and acts like a real computer, but shares hardware with other virtual machines. For example, you can rent a 'computer' from AWS that is actually a virtual machine.

    Virtualization solves many problems, including improving the use of physical hardware by allowing more applications to run on the same physical machine while still being isolated from each other for security purposes.

    Applications running on a virtual machine are not aware that they are sharing a physical computer. Virtualization also allows users in a data center to launch a new 'computer' (or virtual machine) in minutes without worrying about the physical limitations of adding a new computer to the data center. Virtual machines also enable users to get new virtual computers faster.

- Virtual Service

    Virtual service defines a set of traffic routing rules for a specified service. Each routing rule defines traffic matching rules for a specific protocol. If the traffic matches these characteristics, it is sent to the target service (or subset or version of the target service) in the service registry according to the rules.

- Volume

    A volume is a data directory that can be accessed by containers in a Pod. Each Kubernetes volume remains in existence for the lifetime of the Pod in which it is created. Therefore, the life of the volume exceeds that of the container running in the Pod, and the data is guaranteed to be retained even after the container restarts.

- Volume Plugin

    A volume plugin allows Pods to integrate with storage. Volume plugins allow you to attach and mount storage volumes to Pods. Volume plugins can be either in-tree or out-of-tree. In-tree plugins are part of the Kubernetes codebase and follow its release cycle, while out-of-tree plugins are developed independently.

### W, Z

- Weight

    The weight is a floating-point number. The larger the weight, the more traffic is allocated to the instance.

- Workload

    A workload is an application running on Kubernetes.

    Various core objects representing different types or parts of workloads include [Deployment](../kpanda/user-guide/workloads/create-deployment.md), [StatefulSet](../kpanda/user-guide/workloads/create-statefulset.md), [DaemonSet](../kpanda/user-guide/workloads/create-daemonset.md), [Job](../kpanda/user-guide/workloads/create-job.md), and ReplicaSet.

    For example, a workload with a web server and a database may run the database in a StatefulSet, while the web server runs in a Deployment.

- Workload Instance

    In a service mesh, a workload instance is a binary instantiation object of a workload. A workload instance can expose zero or more service endpoints and can also consume zero or more services. A workload instance has many attributes: name and namespace, IP address, unique ID, labels, principals, etc.

- Workload Instance Principal

    In a service mesh, a workload instance principal is the verifiable authority of a workload instance. Service-to-service authentication in the service mesh is used to generate the workload instance principal. By default, the workload instance principal is compatible with the SPIFFE ID format.

- Workspace

    A [workspace](../ghippo/user-guide/workspace/workspace.md) is a resource category that represents a resource hierarchy. A workspace can contain resources such as clusters, [namespaces](../kpanda/user-guide/namespaces/createns.md), and registries. Typically, a workspace corresponds to a project, and different resources can be assigned to each workspace, with different users and groups assigned.

- Worker Cluster

    A worker cluster is a cluster that connects to an external control plane outside the main cluster. A worker cluster can connect to the control plane of the main cluster or to an external control plane.

- Zero Trust Architecture

    Zero Trust Architecture specifies a method of designing and implementing IT systems that completely eliminates trust. Its core principle is "never trust, always verify," and a device or system always verifies itself when communicating with other components of the system. In many networks today, in enterprise networks, internal systems and devices can freely communicate with each other because they are within the trusted boundary of the enterprise network. Zero Trust Architecture takes the opposite approach, recognizing that trust is a weakness.

    In a traditional trust-based approach, systems and devices at the perimeter of the enterprise network assume that there are no problems because there is trust. However, Zero Trust Architecture recognizes that trust is a weakness. If an attacker gains access to a trusted device, the system is now vulnerable to attack based on the level of trust and access to that device, as the attacker is within the trusted network boundary and can move laterally throughout the system. In Zero Trust Architecture, trust is removed, reducing the attack surface, as attackers are now forced to authenticate before entering the entire system.

    The main benefit of adopting Zero Trust Architecture is increased security and reduced attack surface. Removing trust from your enterprise system now increases the number and strength of security gates that attackers must pass through to gain access to other areas of the system.

[Download DCE 5.0](../download/index.md){ .md-button .md-button--primary }
[Install DCE 5.0](../install/index.md){ .md-button .md-button--primary }
[Free Trial](license0.md){ .md-button .md-button--primary }
