---
hide:
  - toc
---

# Creating Inspection Configuration

DCE 5.0 Container Management module provides cluster inspection functionality, which supports inspection at the cluster, node, and container group levels.

- Cluster level: Check the running status of system components in the cluster, including cluster status, resource usage, and specific inspection items for control nodes such as __kube-apiserver__ and __etcd__ .
- Node level: Includes common inspection items for both control nodes and worker nodes, such as node resource usage, handle count, PID status, and network status.
- Pod level: Check the CPU and memory usage, running status, PV and PVC status of Pods.

Here's how to create an inspection configuration.

1. Click __Cluster Inspection__ in the left navigation bar.

    ![nav](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kpanda/images/inspect01.png)

2. On the right side of the page, click __Inspection Configuration__ .

    ![create](../images/inspection-home.png)

3. Fill in the inspection configuration based on the following instructions, then click __OK__ at the bottom of the page.

    - Cluster: Select the clusters that you want to inspect from the dropdown list. **If you select multiple clusters, multiple inspection configurations will be automatically generated (only the inspected clusters are inconsistent, all other configurations are identical).**
    - Scheduled Inspection: When enabled, it allows for regular automatic execution of cluster inspections based on a pre-set inspection frequency.
    - Inspection Frequency: Set the interval for automatic inspections, e.g., every Tuesday at 10 AM. It supports custom CronExpressios, refer to [Cron Schedule Syntax](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#cron-schedule-syntax) for more information.
    - Number of Inspection Records to Retain: Specifies the maximum number of inspection records to be retained, including all inspection records for each cluster.
    - Parameter Configuration: The parameter configuration is divided into three parts: cluster level, node level, and container group level. You can enable or disable specific inspection items based on your requirements.

    ![basic](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kpanda/images/inspect03.png)

After creating the inspection configuration, it will be automatically displayed in the inspection configuration list. Click the more options button on the right of the configuration to immediately perform an inspection, modify the inspection configuration or delete the inspection configuration and reports.

- Click __Inspection__ to perform an inspection once based on the configuration.
- Click __Inspection Configuration__ to modify the inspection configuration.
- Click __Delete__ to delete the inspection configuration and reports.

    ![basic](../images/inspection-list-more.png)

!!! note

    - After creating the inspection configuration, if the __Scheduled Inspection__ configuration is enabled, inspections will be automatically executed at the specified time.
    - If __Scheduled Inspection__ configuration is not enabled, you need to manually [trigger the inspection](inspect.md).