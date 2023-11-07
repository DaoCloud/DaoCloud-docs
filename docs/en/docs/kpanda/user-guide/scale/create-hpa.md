# Create HPA

DaoCloud Enterprise 5.0 supports elastic scaling of Pod resources based on metrics (Horizontal Pod Autoscaling, HPA).
Users can dynamically adjust the number of copies of Pod resources by setting CPU utilization, memory usage, and custom metrics.
For example, after setting an auto scaling policy based on the CPU utilization metric for the workload, when the CPU utilization of the Pod exceeds/belows the metric threshold you set, the workload controller will automatically increase/decrease the number of Pod replicas.

This page describes how to configure auto scaling based on built-in metrics and custom metrics for workloads.

!!! note

     1. HPA is only applicable to Deployment and StatefulSet, and only one HPA can be created per workload.
     2. If you create an HPA policy based on CPU utilization, you must set the configuration limit (Limit) for the workload in advance, otherwise the CPU utilization cannot be calculated.
     3. If built-in metrics and multiple custom metrics are used at the same time, HPA will calculate the number of scaling copies required based on multiple metrics, and take the larger value (but not exceed the maximum number of copies configured when setting the HPA policy) for elastic scaling .

## Built-in metric elastic scaling strategy

The system has two built-in elastic scaling metrics of CPU and memory to meet users' basic business cases.

### Prerequisites

Before configuring the built-in index auto scaling policy for the workload, the following prerequisites need to be met:

- The container management module [connected to the Kubernetes cluster](../clusters/integrate-cluster.md) or [created the Kubernetes cluster](../clusters/create-cluster.md), and can access the UI interface of the cluster .

- Completed a [namespace creation](../namespaces/createns.md), [stateless workload creation](../workloads/create-deployment.md) or [stateful workload creation](../workloads/create-statefulset.md).

- The current operating user should have [`NS Edit`](../permissions/permission-brief.md#ns-edit) or higher permissions, for details, please refer to [Namespace Authorization](../namespaces/createns.md).

- Completed [`metrics-server plugin install`](install-metrics-server.md).

### Steps

Refer to the following steps to configure the built-in index auto scaling policy for the workload.

1. Click `Cluster List` on the left navigation bar to enter the cluster list page. Click a cluster name to enter the `Cluster Details` page.

     

2. On the cluster details page, click `Workload` in the left navigation bar to enter the workload list, and then click a workload name to enter the `Workload Details` page.

     

3. Click the Auto Scaling tab to view the auto scaling configuration of the current cluster.

     

4. After confirming that the cluster has [installed the `metrics-server` plug-in](install-metrics-server.md), and the plug-in is running normally, you can click the `New Scaling` button.

     

5. Create custom metric auto scaling policy parameters.

     

     - Policy name: Enter the name of the auto scaling policy. Please note that the name can contain up to 63 characters, and can only contain lowercase letters, numbers, and separators ("-"), and must start and end with lowercase letters or numbers, such as hpa- my-dep.
     - Namespace: The namespace where the payload resides.
     - Workload: The workload object that performs auto scaling.
     - Target CPU Utilization: The CPU usage of the Pod under the workload resource. The calculation method is: the request (request) value of all Pod resources/workloads under the workload. When the actual CPU usage is greater/lower than the target value, the system automatically reduces/increases the number of Pod replicas.
     - Target Memory Usage: The memory usage of the Pod under the workload resource. When the actual memory usage is greater/lower than the target value, the system automatically reduces/increases the number of Pod replicas.
     - Replica range: the elastic scaling range of the number of Pod replicas. The default interval is 1 - 10.

6. After completing the parameter configuration, click the `OK` button to automatically return to the elastic scaling details page. Click `⋮` on the right side of the list to edit, delete, and view related events.

     

## Custom metric elastic scaling strategy

When the built-in CPU and memory metrics of the system cannot meet the actual needs of your business, you can configure ServiceMonitoring to add custom metrics, and achieve elastic scaling based on the custom metrics.

### Prerequisites

Before configuring a custom index auto scaling policy for a workload, the following prerequisites must be met:

- The container management module [connected to the Kubernetes cluster](../clusters/integrate-cluster.md) or [created the Kubernetes cluster](../clusters/create-cluster.md), and can access the UI interface of the cluster .

- Completed a [namespace creation](../namespaces/createns.md), [stateless workload creation](../workloads/create-deployment.md) or [stateful workload creation](../workloads/create-statefulset.md).

- The current operating user should have [`NS Edit`](../permissions/permission-brief.md#ns-edit) or higher permissions, for details, please refer to [Namespace Authorization](../namespaces/createns.md).

- Completed [`metrics-server plugin install`](install-metrics-server.md).
- Installation of the Insight plug-in is complete.
- The installation of the Prometheus-adapter plugin has been completed.

### Steps

Refer to the following steps to configure an index auto-scaling policy for a workload.

1. Click `Cluster List` on the left navigation bar to enter the cluster list page. Click a cluster name to enter the `Cluster Details` page.

     

2. On the cluster details page, click `Workload` in the left navigation bar to enter the workload list, and then click a workload name to enter the `Workload Details` page.

     

3. Click the Auto Scaling tab to view the auto scaling configuration of the current cluster.

     

4. After confirming that the cluster has [`metrics-server`](install-metrics-server.md), Insight, and Prometheus-adapter plug-ins installed and the plug-ins are running normally, click the `New Scaling` button.

     !!! note

         If the relevant plug-in is not installed or the plug-in is in an abnormal state, you will not be able to see the creation of custom metrics auto scaling entry on the page.

     

5. Create custom metric auto scaling policy parameters.

     

     - Policy name: Enter the name of the auto scaling policy. Please note that the name can contain up to 63 characters, and can only contain lowercase letters, numbers, and separators ("-"), and must start and end with lowercase letters or numbers, such as hpa- my-dep.
     - Namespace: The namespace where the payload resides.
     - Workload: The workload object that performs auto scaling.
     - Resource type: A custom metric type for monitoring, including Pod and Service.
     - Metrics: custom metric names created using ServiceMonitoring or custom metric names built into the system.
     - Data type: the method used to calculate the metric value, including target value and target average value. When the resource type is Pod, only the target average value is supported.