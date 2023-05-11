# Start observing

The DCE 5.0 platform realizes the management of multi-cloud and multi-cluster, and supports the creation of clusters. On this basis, Observability Insight, as a multi-cluster unified observation solution, realizes the collection of multi-cluster observation data by deploying the insight-agent plug-in, and supports the realization of indicators, logs, and link data through DCE 5.0 observability products. Inquire.

`insight-agent` is a tool for observability to realize multi-cluster data collection. After installation, it can realize automatic collection of indicators, logs and link data without any modification.

The cluster created through `container management` will install insight-agent by default, so here only provides guidance on how to enable the observation capability of the connected cluster.

- [Install insight-agent online](./install-agent.md)

Observability Insight is a unified observation platform for multiple clusters. The resource consumption of some of its components is closely related to the data of the created cluster and the number of connected clusters. When installing insight-agent, the resources of the corresponding components need to be adjusted according to the size of the cluster.

1. Adjust the CPU and memory of the acquisition component `Prometheus` in insight-agent according to the scale of the created cluster or the scale of the access cluster, please refer to: [Prometheus resource planning](../../best-practice/prometheus- res.md)

2. Since the index data of multiple clusters will be stored uniformly, the DCE 5.0 platform administrator needs to adjust the vmstorage disk according to the scale of the created cluster and the scale of the access cluster. Please refer to: [vmstorage disk capacity planning](../. ./best-practice/vms-res-plan.md).

- How to adjust the vmstorage disk, please refer to: [vmstorge disk expansion](../../best-practice/modify-vms-disk.md).

Since DCE 5.0 supports the management of multi-cloud and multi-clusters, insight-agent has also completed part of the verification. Due to the conflict of monitoring components, there will be problems installing insight-agent in DCE 4.0 clusters and Openshift 4.x clusters. If you encounter For the same problem, please refer to the following documents:

- [Installing insight-agent on DCE 4.0.x](../../faq/install-agentindce.md)
- [Installing insight-agent on Openshift 4.x](../../faq/install-agent-on-ocp.md)

At present, the collection component insight-agent has completed some functional tests on the current mainstream Kubernetes version, please refer to:

- [kubernetes cluster compatibility test](./k8s-compatibility.md)
- [Openshift 4.x Cluster Compatibility Test](./ocp-compatibility.md)
- [Rancher Cluster Compatibility Test](./rancher-compatibility.md)
