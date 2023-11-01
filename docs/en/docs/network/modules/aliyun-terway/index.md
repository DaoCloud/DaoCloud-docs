# Introduction to Terway CNI Plugin

Terway is a CNI plugin developed by the Alibaba Cloud Container Service team specifically for its Cloud VPC networks. It offers a stable and high-performance solution with support for advanced features like Kubernetes network policy and traffic control.
The Terway CNI mainly consists of two components:

- CNI Binary: this component interacts with Kubernetes CRI runtime, handling requests from the API Server to manage Pods and configure their network protocol stack. It also communicates with its own daemon component, which invokes the Alibaba Cloud OpenAPI for managing and connecting to network resources.

- Daemon Component: invoked by the CNI Binary, it is responsible for interacting with the Alibaba Cloud OpenAPI. It performs operations to manage VPC network resources such as creating and deleting ENIs and adding or removing secondary IPs.

To meet the diverse requirements of different users, Terway supports four different communication modes:

- VPC
- ENI
- ENIIP
- ENI-Trunking

Other contents:

[Terway Network Introduction](what.md)
