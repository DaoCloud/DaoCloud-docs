---
MTPE: windsonsesa
date: 2024-05-11
hide:
  - toc
---

# Network Background

## Multicloud and Hybrid Cloud Environments

As cloud-native use cases expand, we see a surge in cloud-based applications, leading to increasingly complex scenarios.
To address challenges like high availability, disaster recovery, and spikes in business traffic, users are moving towards
multicluster and cross-cloud deployments. This shift highlights key issues related to application distribution,
connectivity, and platform management.

The network plays a crucial role in implementing these strategies, with major challenges including:

- **Multicluster Management**: As the underlying infrastructure diversifies across different public clouds,
  private clouds, and cross-regional environments, managing multicluster environments becomes more complex.
  This necessitates the interconnection of heterogeneous cluster networks and the capability to discover
  public services across these clusters.

- **High Availability**: To ensure high availability, microservice applications need to operate in
  active-standby modes across different clusters, requiring robust network connectivity to support this architecture.

## Traditional Application Cloud-Native Transformation

- **IP Management**: Industries like manufacturing, education, and energy, transitioning to cloud environments,
  often retain traditional application structures rather than adopting microservices. These applications
  frequently require access through fixed IPs, which need stringent management like firewall controls,
  calling for more adaptable and efficient IP management solutions.

- **Cluster Internal and External Connectivity**: As traditional applications evolve towards microservices,
  there's a gradual shift towards containerizing certain applications. These containerized applications might
  require externally accessible IPs to facilitate connectivity both within and outside the cluster,
  necessitating fixed and externally accessible IPs.

- **Diverse Network Types**: Given the strict control requirements for external access IPs,
  users often expose certain applications to external access on container cloud platforms.
  Applications not requiring external access continue using dynamic virtual IPs.
  This leads to a need for diverse network types, such as MacVLAN CNI for external access and Calico CNI for internal uses.

## Databases, Machine Learning, and Other Cloud Applications

With advancements in cloud-native technology, resource-intensive applications like databases and
machine learning are increasingly being hosted on Kubernetes platforms. These applications demand
high computational power, network performance, and low latency. Consequently, integrating
hardware-based virtualization acceleration solutions like SR-IOV and network acceleration technologies
like eBPF with Kubernetes is becoming essential.

## Network Security and Regulatory Requirements

Containers and cloud-native platforms automate application deployment, offering significant business advantages.
However, this often results in a lack of horizontal network security isolation within the platform. Moreover,
as the scale of cloud-native implementations grows and microservices become more prevalent, east-west network
traffic intensifies. While traditional firewalls and host security tools can protect individual applications,
the dynamic nature of containers deployed across various hosts and clouds necessitates enhanced monitoring of
east-west and internal traffic. Enterprises building container cloud platforms must consider implementing
finer-grained network policies to bolster network security.
