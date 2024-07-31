---
hide:
  - toc
---

# Create Job from Image

Follow the steps below to create a Job.

1. In the left navigation bar, click __Multicloud Workload__ to enter the job page, and click the __Image creation__ button in the upper right corner.

1. On the __Create Job__ page, after configuring the basic information of the load, click __Next__ .

    - Payload Name: Can contain up to 63 characters, can only contain lowercase letters, numbers, and a separator ("-"), and must start and end with a lowercase letter or number. The name of the same type of workload in the same namespace cannot be repeated, and the name of the workload cannot be changed after the workload is created.
    - Multicloud namespace: Select the namespace where the newly created job will be deployed. The default namespace is used by default. If you cannot find the required namespace, you can create a new one according to the prompt on the page.
    - Deployment cluster: Provides three options to determine which clusters the workload will be deployed on.
    - Number of Instances: Enter the number of Pod instances for the workload. By default, 1 Pod instance is created.
    - Scheduling strategy: Provides three selection methods to determine how to allocate workload instances.
    - Description: Enter the description information of the workload and customize the content. The number of characters should not exceed 512.

    There are three ways to deploy a cluster:

    - Specify cluster: Specify a cluster by selecting the cluster name
    - Specified region: Specify the cluster by selecting the manufacturer, region, and availability zone
    - Specify tags: specify clusters by adding metrics
    - You can also choose to exclude clusters/set cluster taint tolerance/dynamic area selection in the advanced deployment strategy, and finally display which clusters are expected to be scheduled to at the bottom.

    Scheduling strategies are divided into three ways

    - Repeat: schedule the same number of instances in all selected clusters
    - Aggregation: schedule as few instances as possible in all selected clusters
    - Dynamic weight: according to the real-time schedulable maximum number of instances of all selected clusters, the total number of filled instances will be run in equal proportion

1. On the __Container Configuration__ page, configure the basic information of the container where the load resides, and optionally configure information such as life cycle and health check, and then click __Next__ .


1. On the __Advanced Configuration__ page, you can configure job settings and labels and annotations.


    Job settings need to include the following data:

    - Parallel number: the maximum number of Pods that can be created at the same time during job execution, and the parallel number should not be greater than the total number of Pods. Default is 1.
    - Timeout: When this time is exceeded, the job will be marked as failed to execute, and all Pods under the job will be deleted. When it is empty, it means that no timeout is set.
    - Restart Policy: Whether to restart the Pod when the setting fails.

    If you do not need to configure differentiation after the creation is complete, you can directly use __OK__ to complete the creation of the multicloud job

1. On the __Override Configuration__ page, after selecting the personalized container configuration, labels and annotations, click __OK__ .

    You can add the corresponding differentiated configmap in the list area on the left. After you add a differentiated configmap, you need to specify the corresponding cluster.
    The selectable range of the cluster is only the cluster selected at the beginning, and the selected cluster will use the specified differential configuration; the unspecified cluster will still use the default configuration.

!!! note

    - When creating a multicloud workload through mirroring, if you need to use the advanced capabilities of specifying a location and specifying a label to create, you need to ensure that the corresponding location or label has been set for the worker cluster;
    Adding tags needs to be added within a single cluster, and can be jumped to the corresponding cluster maintenance from the worker cluster management list.
    - When configuring the number of replicas, you need to pay attention to the corresponding scheduling strategy. Only when it is repeated, will all the configured replicas be started in multiple clusters.
