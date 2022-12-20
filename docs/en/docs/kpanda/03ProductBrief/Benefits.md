---
hide:
  - toc
---

# Advantage

The container management platform has the following advantages:

**Unified management of clusters**

- Supports unified management of different clusters, supports any Kubernetes cluster within a specific version range to be included in the scope of container management, realizes unified management of on-cloud, off-cloud, multicloud, and hybrid cloud container cloud platforms, and avoids vendor lock-in.

- The smooth upgrade of the Kubernetes cluster can be completed with one click through the web interface.

- The unified web interface realizes cluster creation, expansion and contraction of cluster nodes and other management capabilities.

- One-click certificate rotation, self-built clusters can implement certificate rotation on the web interface.

- Supports unified management of ultra-large-scale clusters.

**Application production ready**

- One-stop application distribution, which can distribute applications through image, YAML, and Helm, and realize unified management across clouds/clusters.

- High availability of applications, support for distributed deployment of applications, and automatic switching of single-point-of-failure traffic.

- Abundant monitoring indicators to realize all-round monitoring of applications, early warning of application traffic peaks and application failures.

**Unified distribution of policies**

- Support the formulation of network policies, quota policies, resource limit policies, disaster recovery policies, security policies and other policies at the granularity of namespaces or clusters, and support policy delivery at the granularity of clusters/namespaces.

**Safe and reliable**

- The self-built cluster defaults to the high-availability deployment mode to ensure high availability of your business. When a node fails or a natural disaster occurs, the application can continue to run, ensuring high availability of the production environment and realizing uninterrupted business application systems.

- High availability of cross-regional applications, supports the deployment of different container clusters across regions, and can deploy services on multiple cloud container clusters in different regions at the same time, helping applications to achieve multi-regional traffic distribution.
  When a cloud container cluster fails, the computer room goes down, or a natural disaster occurs, the business traffic is automatically switched to other cloud container platforms through a unified traffic distribution mechanism to ensure high availability of applications.

- A complete user permission system, integrating [Kubernetes RBAC permission system](https://kubernetes.io/zh-cn/docs/reference/access-authn-authz/rbac/), supports setting different granular permissions for different users.

**Heterogeneous compatibility**

- Provides highly automated and elastic heterogeneous multicloud support capabilities, adapting to x86 and Xinchuang cloud architecture.

- Supports unified deployment of x86 and ARM architecture mixed clusters, unified management and support for application operation, and guarantees network interoperability between applications.

**Open and Compatible**

- Based on native Kubernetes and Docker technology, fully compatible with Kubernetes API and Kubectl commands.

- Provides a rich plug-in system to expand the functions of cloud container clusters, such as network plug-ins [Multus](https://github.com/k8snetworkplumbingwg/multus-cni), [Cillum](../../network/modules/ cilium/what.md), [Contour](https://projectcontour.io/) and other components.