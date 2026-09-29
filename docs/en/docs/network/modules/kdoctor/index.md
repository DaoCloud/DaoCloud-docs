## kdoctor

kdoctor is a Kubernetes data plane testing component based on active stress injection. It tests the
functionality and performance of a cluster. By investigating and abstracting the common requirements of
O&M personnel, kdoctor implements network, storage, and application O&M tasks in a cloud native way.
In addition, it adopts a CRD-based design so that it can connect to observability components.

**kdoctor mainly includes the following three types of tasks:**

- [AppHttpHealthy](https://kdoctor-io.github.io/kdoctor/v0.2/reference/apphttphealthy/): According to the
  task configuration, uses HTTP and HTTPS protocols to check the connectivity of specified access addresses
  inside and outside the cluster, and supports PUT, GET, POST, and other request methods.
- [NetReach](https://kdoctor-io.github.io/kdoctor/v0.2/reference/netreach/): According to the task
  configuration, performs connectivity inspection on Pod IP, ClusterIP, NodePort, LoadBalancer IP, and
  Ingress IP in the cluster, and even on Pod multi-NIC and dual-stack IP.
- [NetDns](https://kdoctor-io.github.io/kdoctor/v0.2/reference/netdns/): According to the task
  configuration, checks the connectivity of specified DNS servers inside and outside the cluster,
  and supports UDP, TCP, and TCP-TLS protocols.

**What are the advantages of kdoctor over traditional testing components:**

- Inspection task requirements are delivered through CRD configuration. Users only need to focus on the
  inspection target, inspection frequency, stress parameters, and expected inspection results.
- By reading the task configuration, the stress agent runs as a Deployment or DaemonSet, achieving the
  effect of multiple stress machines.
- According to the task spec configuration, the default agent is used or a new agent is created to execute
  the task, achieving resource reuse and task resource isolation.
- Bind the corresponding resource targets, such as ingress and service. Each agent Pod accesses the bound
  resources according to the task configuration and draws conclusions based on the request results.
- The stress client is performance-tuned, which greatly reduces the resource consumption of stress requests.
- Inspection reports are output through logs, aggregated APIs, and file persistence.

## Architecture

<div style="text-align:center">
  <img src="../../images/kdoctor-arch.png" alt="kdoctor architecture">
</div>

Component composition:

- kdoctor controller: Resides as a Deployment and performs CR monitoring, task creation, and task report aggregation.
- kdoctor agent: Dynamically created on demand as a Deployment or DaemonSet, and is the executor of tasks.
