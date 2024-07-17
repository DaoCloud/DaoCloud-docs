---
MTPE: windsonsesa
date: 2024-05-11
---

# Background and Challenges

This page briefly explains the research and development background and challenges faced by DCE 5.0 container networking.

## Network Background

**Multicloud and Hybrid Cloud**

As cloud-native application scenarios gradually scale up, the number of applications migrating to the cloud is rapidly increasing, and the scenarios are becoming increasingly complex. To handle situations like high availability, disaster recovery, and surging business traffic, users are gradually adopting multi-cluster and cross-cloud deployments. However, during the implementation of these solutions, issues such as application distribution, application connectivity, and platform management have become increasingly prominent.

Among these, the network is the key to the overall solution implementation, facing the following main issues:

- The demand for multi-cluster management is increasing, and the underlying infrastructure is diversified, requiring consideration of different public clouds, private clouds, and cross-regional environments. Therefore, in heterogeneous scenarios, it is necessary to achieve interconnectivity of heterogeneous cluster networks and have the capability for cross-cluster service discovery of public services.

- To ensure high availability, microservice application loads serve as primary and backup across different clusters. In this scenario, it is also necessary to ensure network interconnectivity.

**Cloud-Native Transformation of Traditional Applications**

- IP Management: In some traditional industries such as manufacturing, education, and energy, applications often migrate to the cloud without microservice transformation. Many applications still need to be accessed through a fixed IP. Additionally, such IPs need to be strictly controlled, such as through stringent firewall controls. Therefore, more flexible and efficient IP management capabilities are required.

- Interconnectivity Inside and Outside the Cluster: During the microservice transformation of traditional applications, users will gradually containerize some applications. Some containerized applications need to have externally accessible IPs to achieve interconnectivity inside and outside the cluster. Therefore, these applications also need to use fixed and externally accessible IPs.

- Diverse Network Types: Based on the strong control requirements for externally accessible IPs, users often open some applications for external access on a container cloud platform. For applications that do not need external access, dynamic virtual IPs are still used. For example, some applications use MacVLAN CNI for external access, while others use Calico CNI. Therefore, the diversification of network types is also gradually becoming a demand for applications migrating to the cloud.

**Cloud Migration of Applications like Databases and Machine Learning**

With the development of the cloud-native field, resource-sensitive applications such as databases and machine learning are also beginning to run on Kubernetes platforms. These applications have high requirements for computing power, network performance, and latency. Therefore, the integration of hardware-based virtualization acceleration network solutions like SR-IOV (Single Root I/O Virtualization) and network acceleration solutions like eBPF with Kubernetes is an inevitable development direction.

**Network Security Regulatory Requirements**

Containers and cloud-native platforms help enterprises achieve automated application deployment, bringing significant business benefits. However, Pods within the platform are flat, lacking horizontal network security isolation. Moreover, as the scale of cloud-native expands and microservices advance, east-west network traffic increases dramatically. Although traditional firewalls and host security tools can protect monolithic applications, for containers dynamically deployed between hosts and various clouds, it is necessary to strengthen monitoring of east-west traffic and internal traffic attacks. Enterprises need to consider more fine-grained network policies to enhance network security when building container cloud platforms.

## Network Challenges

**Network Connectivity in Multicloud and Multi-Cluster Environments**

In a multi-cluster environment, it is necessary to consider not only the different network CNIs used by each cluster but also the interconnectivity between clusters. Therefore, issues such as Cluster IP interconnectivity and DNS interconnectivity need to be resolved.

**Unified IP Resource Management in Multicloud and Multi-Cluster Environments**

To achieve network interconnectivity in a Multicloud and multi-cluster environment, IPs within and between clusters must not be duplicated or conflicted. Therefore, IP management and planning need to be based on a multi-cluster perspective to avoid IP conflicts and subnet conflicts (Underlay IP, Service IP, etc.).

**Single CNI Challenged by Diverse Scenarios**

Facing diverse network scenarios, the current network requirements of different types of applications vary. A single network CNI can hardly meet the diverse scenario requirements. Therefore, specific CNIs are needed to meet business needs in specific scenarios, and in more complex scenarios, a combination of CNIs is required.

**High Demand for Fixed and Externally Accessible IPs but Lack of Flexible and Efficient IPAM Mechanisms**

Fixed and externally accessible IPs are implemented based on Underlay CNI, but IP resources in Underlay CNI are relatively scarce and require strict firewall control. Therefore, the use of Underlay IPs needs to be strictly planned and allocated. When IP addresses are released and allocation fails, timely recovery is needed to prevent resource waste.

**Unified Management of Network Security Policies and Network Traffic**

It is necessary to uniformly issue network security policies for different clusters and manage and encrypt network traffic between different clusters.

**New Challenges Brought by the Combination of Software and Hardware, Network Acceleration, and Other New Technologies**

To meet high-performance, low-latency network requirements, the combination of hardware-based virtualization acceleration network solutions like SR-IOV and network acceleration solutions like eBPF is a significant opportunity and challenge faced by cloud-native container networks.
