# Create HPA

DaoCloud Enterprise 5.0 supports scaling of Pod resources based on metrics (Horizontal Pod Autoscaling, HPA).
Users can dynamically adjust the number of copies of Pod resources by setting CPU utilization, memory usage, and custom metrics.
For example, after setting an auto scaling policy based on the CPU utilization metric for the workload,
when the CPU utilization of the Pod exceeds/belows the metric threshold you set, the workload controller
will automatically increase/decrease the number of Pod replicas.

This page describes how to configure auto scaling based on built-in metrics and custom metrics for workloads.

!!! note

     1. HPA is only applicable to Deployment and StatefulSet, and only one HPA can be created per workload.
     2. If you create an HPA policy based on CPU utilization, you must set the configuration limit (Limit) for the workload in advance, otherwise the CPU utilization cannot be calculated.
     3. If built-in metrics and multiple custom metrics are used at the same time, HPA will calculate the number of scaling copies required based on multiple metrics, and take the larger value (but not exceed the maximum number of copies configured when setting the HPA policy) for scaling .

## Built-in metric scaling policy

The system has two built-in scaling metrics of CPU and memory to meet users' basic business cases.

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


    - Policy Name: Enter the name of the scaling policy. Please note that the name can be up to 63 characters long and can only contain lowercase letters, numbers, and separators ("-"). It must also start and end with a lowercase letter or number, for example, hpa-my-dep.
    - Namespace: The namespace where the load is located.
    - Workload: The workload object that executes scaling.
    - Replica Range: Set the minimum number of container group replicas allowed, with a default value of 1. Set the maximum number of container group replicas allowed, with a default value of 10.
    - Stabilization Time Window: The stabilization window time for scaling up and down must be greater than or equal to 0 and less than or equal to 3600, with a range of [0, 3600] seconds.
    - System Metrics:
        - CPU Utilization: The CPU usage of the Pods under the workload resources. The calculation method is: total resources of all Pods under the workload / request value of the workload. When the actual CPU usage is greater than/less than the target value, the system automatically decreases/increases the number of Pod replicas.
        - Memory Usage: The memory usage of the Pods under the workload resources. When the actual memory usage is greater than/less than the target value, the system automatically decreases/increases the number of Pod replicas.
    - Custom Metrics: Refer to [Creating HPA Based on Custom Metrics](./custom-hpa.md).

6. After completing the parameter configuration, click the __OK__ button to automatically return to the scaling details page. Click __┇__ on the right side of the list to edit, delete, and view related events.
