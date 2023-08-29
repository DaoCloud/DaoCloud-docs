# Start Observing

DCE 5.0 platform enables the management and creation of multi-cloud and multi-cluster environments.
Building upon this capability, Observability Insight serves as a unified observability solution for
multiple clusters. It collects observability data from multiple clusters by deploying the insight-agent
plugin and allows querying of metrics, logs, and trace data through the DCE 5.0 observability products.

`insight-agent` is a tool that facilitates the collection of observability data from multiple clusters.
Once installed without any modifications, it automatically collects metrics, logs, and trace data.

Clusters created through `Container Management` come pre-installed with insight-agent. Hence,
this guide specifically provides instructions on enabling observability for connected clusters.

- [Install insight-agent online](install-agent.md)

As a unified observability platform for multiple clusters, Observability Insight's resource consumption
of certain components is closely related to cluster creation and the number of connected clusters.
When installing insight-agent, it is necessary to adjust the resources of the corresponding components based on the cluster size.

1. Adjust the CPU and memory resources of the `Prometheus` collection component in insight-agent
   according to the cluster or connected cluster size. Please refer to
   [Prometheus resource planning](../res-plan/prometheus-res.md).

2. As the metric data from multiple clusters is stored centrally, DCE 5.0 platform administrators
   need to adjust the disk space of `vmstorage` based on the cluster creation or connected cluster size.
   Please refer to [vmstorage disk capacity planning](../res-plan/vms-res-plan.md).

- For instructions on adjusting the disk space of vmstorage, please refer to
  [Expanding vmstorage disk](../res-plan/modify-vms-disk.md).

Since DCE 5.0 supports the management of multi-cloud and multi-cluster environments,
insight-agent has undergone partial verification. However, there are known conflicts
with monitoring components when installing insight-agent in DCE 4.0 clusters and
Openshift 4.x clusters. If you encounter similar issues, please refer to the following documents:

- [Install insight-agent in DCE 4.0.x](../other/install-agentindce.md)
- [Install insight-agent in Openshift 4.x](../other/install-agent-on-ocp.md)

Currently, the insight-agent collection component has undergone functional testing
for popular versions of Kubernetes. Please refer to:

- [Kubernetes cluster compatibility testing](../../compati-test/k8s-compatibility.md)
- [Openshift 4.x cluster compatibility testing](../../compati-test/ocp-compatibility.md)
- [Rancher cluster compatibility testing](../../compati-test/rancher-compatibility.md)
