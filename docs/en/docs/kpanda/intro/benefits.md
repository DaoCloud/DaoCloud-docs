---
hide:
  - toc
---

# Benefits

The Container Management module offers the following advantages:

**Unified cluster management**

- Supports unified management of different clusters and includes any Kubernetes cluster within a specific
  version range in the scope of container management. This enables unified management of on-cloud, off-cloud,
  multicloud, and hybrid cloud container platforms while avoiding vendor lock-in.
- The web interface allows for one-click upgrade of the Kubernetes cluster.
- Unified web interface facilitates cluster creation, expansion and contraction of cluster nodes, and
  other management capabilities.
- Self-built clusters can implement certificate rotation on the web interface with one-click.
- Supports unified management of ultra-large-scale clusters.

**Production-ready applications**

- One-stop application distribution allows for distribution of applications through mirroring, YAML,
  and Helm, and enables unified management across clouds/clusters.
- High availability of applications: supports distributed deployment of applications and automatic
  switching of single-point-of-failure traffic.
- Rich monitoring metrics enable all-round monitoring of applications, early warning of application
  traffic peaks, and application failures.

**Unified policy distribution**

- Support formulation of network policies, quota policies, resource limit policies, disaster recovery
  policies, security policies, and other policies at the granularity of namespaces or clusters.
  Also, support policy delivery at the granularity of clusters/namespaces.

**Safe and reliable**

- The self-built cluster defaults to high-availability deployment mode to ensure high availability
  of your business. When a node fails or a natural disaster occurs, the application can continue to
  run, ensuring high availability of the production environment and uninterrupted business application systems.
- High availability of cross-regional applications: supports deployment of different container clusters across regions, can deploy services on multiple cloud container clusters in different regions simultaneously, enabling applications to achieve multi-regional traffic distribution. In case of failure of a cloud container cluster, computer room shutdown, or natural disaster occurrence, the business traffic is automatically switched to other cloud container platforms via a unified traffic distribution mechanism to ensure high availability of applications.
- Complete user permission system, integrating [Kubernetes RBAC permission system](https://kubernetes.io/docs/reference/access-authn-authz/rbac/), supports setting different granular permissions for different users.

**Heterogeneous compatibility**

- Provides highly automated and elastic heterogeneous multicloud support capabilities, adapting to both x86 and Xinchuang cloud architectures.
- Supports unified deployment of x86 and ARM architecture mixed clusters, unified management and support for application operation, and guarantees network interoperability between applications.

**Open and compatible**

- Based on native Kubernetes and Docker technology, fully compatible with Kubernetes API and Kubectl commands.
- Provides a rich plug-in system to expand the features of cloud container clusters, such as network plug-ins [Multus](https://github.com/k8snetworkplumbingwg/multus-cni), [Cillum](../../network/modules/cilium/index.md), [Contour](https://projectcontour.io/), and other components.
