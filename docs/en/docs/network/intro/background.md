---
hide:
  - toc
---

# Network background

**Multicloud hybrid cloud**

Cloud native use cases are gradually scaled up, cloud-based applications continue to surge, and the use cases are becoming more and more complex.
In order to cope with Cases such as high availability, disaster recovery, and business traffic surge, users gradually adopt multicluster and cross-cloud deployments. During the implementation of the solution, problems such as application distribution, application connectivity, and platform management have gradually become prominent.

Among them, the network is the key to the implementation of the overall plan, and the main problems are as follows:

- The demand for multicluster management increases, and the underlying infrastructure is diversified, so different public clouds, private clouds, and cross-regional environments need to be considered. Therefore, in the scenario of a heterogeneous environment, the interconnection of heterogeneous cluster networks is required, and the ability to discover public services across clusters is required.

- To ensure high availability, microservice application loads are mutually active and standby in different clusters. In this scenario, it is also necessary to ensure network connectivity.



**Traditional application cloud nativeization**

- IP management: In the process of migrating to the cloud in some traditional industries such as manufacturing, education, and energy, applications are often not transformed by microservices, and many applications still need to be accessed through a fixed IP. Moreover, such IPs also require strong control, such as strict firewall control. Therefore, more flexible and efficient IP management capabilities are required.

- Interconnection inside and outside the cluster: In the process of traditional application microservices, users will gradually containerize some applications. Some containerized applications need to have externally accessible IPs to achieve interconnection inside and outside the cluster. Therefore, such applications also need to use a fixed and externally accessible IP.

- Diversified network types: Based on the strong control requirements for external access IP, users often open some applications to external access in a container cloud platform. For applications that do not require external access, dynamic virtual IPs are still used. For example, some applications use MacVLAN CNI for external access, and some applications use Calico CNI. Therefore, diversification of network types has also gradually become a requirement for applications on the cloud.



**Database, machine learning and other applications on the cloud**

With the development of the cloud native field, resource-sensitive applications such as databases and machine learning have also begun to run on the Kubernetes platform.
Such applications have high requirements on computing power, network performance, and latency.
Therefore, the integration of hardware-based virtualization acceleration network solutions such as SR-IOV (Single Root I/O Virtualization) and network acceleration solutions such as eBPF with Kubernetes is also an inevitable development direction.

**Network Security Regulatory Requirements**

Containers and cloud native platforms help enterprises automate application deployment and bring huge business benefits.
However, the pods inside the platform are all flat, and the horizontal network security isolation is not guaranteed.
In addition, with the expansion of cloud native scale and the advancement of micro-services, east-west network traffic has increased dramatically.
Although a single application can be protected by traditional firewalls and host security tools, for containers dynamically deployed between hosts and even various clouds, it is necessary to strengthen monitoring of east-west traffic and internal traffic attacks.
When building a container cloud platform, enterprises need to consider finer-grained network policies to improve network security.