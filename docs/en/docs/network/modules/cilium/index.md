# What is Cilium

Cilium is open source software for transparently providing and securing the network and API connectivity between application services deployed using Linux container management platforms such as Kubernetes.

At the foundation of Cilium is a new Linux kernel technology called eBPF, which enables the dynamic insertion of powerful security, visibility, and networking control logic within Linux itself.
eBPF is utilized to provide functionality such as multicluster routing, load balancing to replace kube-proxy, transparent encryption as well as network and service security.
Besides providing traditional network-level security, the flexibility of eBPF enables security with the context of application protocols and DNS requests/responses.
Cilium is tightly integrated with Envoy and provides an extension framework based on Go.
Because eBPF runs inside the Linux kernel, all Cilium functionality can be applied without any changes to the application code or container configuration.

Microservices-based applications are split into small, independent services that communicate with each other via APIs using lightweight protocols such as HTTP, gRPC, and Kafka.
However, traditional Linux network security mechanisms (e.g., iptables) only operate at the network and transport layers (i.e., IP addresses and ports) and lack visibility into the microservice layer.

Cilium brings API-aware network security filtering to Linux container platforms such as Docker and Kubernetes.
By leveraging a new Linux kernel technology called eBPF, Cilium provides a simple and effective way to define and enforce network and application layer security policies based on container/container identity.

> Note: Cilium literally means minute and ubiquitous hair.
