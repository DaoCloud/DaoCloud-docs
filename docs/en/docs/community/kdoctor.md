---
MTPE: windsonsea
date: 2024-06-19
---

# Kdoctor

Kdoctor is a cloud native project that performs data plane tests.
It uses pressure injection to carry out active inspections of the function and performance of clusters.

Traditionally, cluster and application status have been confirmed through passive inspection methods
such as collecting metrics, logs, and application statuses. However, in some situations, this method
may not be sufficient due to expected purpose, timeliness, or cluster range. In these cases,
administrators must manually inject pressure into the cluster to check its status, which is known as
active inspection. Large-scale clusters or high-frequency inspections can be challenging to implement
inspections manually.

The following scenarios are ideal for using kdoctor:

- After deploying a large cluster, administrators may need to confirm network connectivity
  between all nodes and detect network failures on certain nodes or occasional packet loss.
  There are various communication methods available, including podIP, clusterIP, nodePort,
  loadbalancerIP, ingress, or even pods with multiple network interfaces and dual-stack IP.

- To ensure that all pods on every node can access the coredns service, or that resource
  configurations and replica numbers of the coredns can support expected access pressure.

- Regular confirmation of local disk performance on all nodes, as disks are consumables,
  and applications like etcd are sensitive to disk performance.

- Active injection of pressure to services like registry, MySQL, or API server to help
  reproduce bugs or confirm service performance.

kdoctor is a practical solution based on production operation and maintenance experience.
with kdoctor, you can perform active inspections to ensure proper cluster performance and
functionality. It is suitable for various scenarios, including creating new clusters,
daily operations and maintenance, E2E testing, bug reproduction, and chaos testing.

[kdoctor on GitHub](https://github.com/kdoctor-io/kdoctor){ .md-button }
