---
hide:
  - toc
---

# View Notebook Workload

If you want to view the workload of a specific Notebook, you can follow these steps:

1. Click the **⋮** on the right side of the Notebook in the Notebook list, then choose **Workload Details** from the dropdown menu.

    <!-- add image later -->

2. You will be directed to the StatefulSet list, where you can view:

    - The running status, IP address, resource requests, and usage of the Pod containers
    - Container configuration information
    - Access methods: ClusterIP, NodePort
    - Scheduling strategies: node and workload affinity, anti-affinity
    - Labels and annotations: key-value pairs of labels and annotations for the workload and Pods
    - Elastic scaling: support for HPA, CronHPA, VPA, etc.
    - Event list: warnings, notifications, and other messages

    <!-- add image later -->

3. In the StatefulSet list, click the **⋮** on the right side to perform more actions specific to the Pods.

    <!-- add image later -->
