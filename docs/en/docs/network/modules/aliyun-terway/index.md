---
hide:
  - toc
---

# Introduction to Terway CNI Plugin

Terway is a CNI plugin developed by the Alibaba Cloud Container Service team specifically designed for Cloud VPC networks. It provides a stable and high-performance solution with advanced features such as Kubernetes network policy and traffic control.

Here are some key terms related to Terway:

- ECS Instance: It refers to a node in Kubernetes.
- Elastic Network Interface (ENI): ENI is a virtual network interface within Alibaba Cloud's Virtual Private Cloud (VPC) that connects ECS instances with the VPC.
- Secondary IP: ENI allows the allocation of one or more secondary private IP addresses, including both primary and secondary ENIs.
- Virtual Switch: It is the switch used by ECS for network communication between nodes.
- Pod Virtual Switch: This switch is responsible for allocating Pod IP addresses for Pod network communication. In the Terway network mode, the Pod IP assigned is obtained from the associated subnet.

The Terway CNI consists of two main components:

1. CNI Binary: This component interacts with the Kubernetes CRI runtime and handles requests from the API Server to manage Pods and configure their network protocol stack. It also communicates with its own daemon component, which invokes the Alibaba Cloud OpenAPI for managing and connecting to network resources.

2. Daemon Component: The daemon component is invoked by the CNI Binary and is responsible for interacting with the Alibaba Cloud OpenAPI. It performs various operations to manage VPC network resources, such as creating and deleting ENIs, and adding or removing secondary IPs.

Terway offers four different communication modes to cater to the diverse requirements of users:

1. VPC
2. ENI
3. ENIIP
4. ENI-Trunking

## What's Next

- [Terway Network Introduction](what.md)
- [Usage](usage.md)
- [Run Calico on Alibaba Cloud](aliyun-calico.md)
- [Run Cilium on Alibaba Cloud](aliyun-cilium.md)
- [Summary](Q_A.md)
