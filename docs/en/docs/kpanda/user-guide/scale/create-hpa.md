# Create HPA

DaoCloud Enterprise 5.0 supports elastic scaling of Pod resources based on metrics (Horizontal Pod Autoscaling, HPA).
Users can dynamically adjust the number of copies of Pod resources by setting CPU utilization, memory usage, and custom metrics.
For example, after setting an auto scaling policy based on the CPU utilization metric for the workload,
when the CPU utilization of the Pod exceeds/belows the metric threshold you set, the workload controller
will automatically increase/decrease the number of Pod replicas.

This page describes how to configure auto scaling based on built-in metrics and custom metrics for workloads.

!!! note

     1. HPA is only applicable to Deployment and StatefulSet, and only one HPA can be created per workload.
     2. If you create an HPA policy based on CPU utilization, you must set the configuration limit (Limit) for the workload in advance, otherwise the CPU utilization cannot be calculated.
     3. If built-in metrics and multiple custom metrics are used at the same time, HPA will calculate the number of scaling copies required based on multiple metrics, and take the larger value (but not exceed the maximum number of copies configured when setting the HPA policy) for elastic scaling .

## Built-in metric elastic scaling policy

The system has two built-in elastic scaling metrics of CPU and memory to meet users' basic business cases.

### Prerequisites

Before configuring the built-in index auto scaling policy for the workload, the following prerequisites need to be met:

- [Integrated the Kubernetes cluster](../clusters/integrate-cluster.md) or
  [created the Kubernetes cluster](../clusters/create-cluster.md),
  and you can access the UI interface of the cluster.

- Created a [namespace](../namespaces/createns.md), [deployment](../workloads/create-deployment.md)
  or [statefulset](../workloads/create-statefulset.md).

- You should have permissions not lower than [NS Editor](../permissions/permission-brief.md#ns-editor).
  For details, refer to [Namespace Authorization](../namespaces/createns.md).

- Installed [metrics-server plugin install](install-metrics-server.md).

### Steps

Refer to the following steps to configure the built-in index auto scaling policy for the workload.

1. Click __Clusters__ on the left navigation bar to enter the cluster list page. Click a cluster name to enter the __Cluster Details__ page.

     

2. On the cluster details page, click __Workload__ in the left navigation bar to enter the workload list, and then click a workload name to enter the __Workload Details__ page.

     

3. Click the Auto Scaling tab to view the auto scaling configuration of the current cluster.

     

4. After confirming that the cluster has [installed the __metrics-server__ plug-in](install-metrics-server.md), and the plug-in is running normally, you can click the __New Scaling__ button.

     

5. Create custom metric auto scaling policy parameters.

     

     - Policy name: Enter the name of the auto scaling policy. Please note that the name can contain up to 63 characters, and can only contain lowercase letters, numbers, and separators ("-"), and must start and end with lowercase letters or numbers, such as hpa- my-dep.
     - Namespace: The namespace where the payload resides.
     - Workload: The workload object that performs auto scaling.
     - Target CPU Utilization: The CPU usage of the Pod under the workload resource. The calculation method is: the request (request) value of all Pod resources/workloads under the workload. When the actual CPU usage is greater/lower than the target value, the system automatically reduces/increases the number of Pod replicas.
     - Target Memory Usage: The memory usage of the Pod under the workload resource. When the actual memory usage is greater/lower than the target value, the system automatically reduces/increases the number of Pod replicas.
     - Replica range: the elastic scaling range of the number of Pod replicas. The default interval is 1 - 10.

6. After completing the parameter configuration, click the __OK__ button to automatically return to the elastic scaling details page. Click __┇__ on the right side of the list to edit, delete, and view related events.
