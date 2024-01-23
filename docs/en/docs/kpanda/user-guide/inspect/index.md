---
hide:
  - toc
---

# Cluster Inspection

Cluster inspection allows administrators to regularly or ad-hoc check the overall health of the cluster,
giving them proactive control over ensuring cluster security. With a well-planned inspection schedule,
this proactive cluster check allows administrators to monitor the cluster status at any time and address
potential issues in advance. It eliminates the previous dilemma of passive troubleshooting during failures,
enabling proactive monitoring and prevention.

The cluster inspection feature provided by DCE 5.0's container management module supports custom inspection
items at the cluster, node, and container group levels. After the inspection is completed,
it automatically generates visual inspection reports.

- Cluster Level: Checks the running status of system components in the cluster, including cluster status,
  resource usage, and specific inspection items for control nodes, such as the status of
  __kube-apiserver__ and __etcd__ .
- Node Level: Includes common inspection items for both control nodes and worker nodes,
  such as node resource usage, handle counts, PID status, and network status.
- Container Group Level: Checks the CPU and memory usage, running status of pods,
  and the status of PV (Persistent Volume) and PVC (PersistentVolumeClaim).

For information on security inspections or executing security-related inspections,
refer to the [supported security scan types](../security/index.md) in DCE 5.0.
