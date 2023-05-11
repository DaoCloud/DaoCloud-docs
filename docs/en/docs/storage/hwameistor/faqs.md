---
hide:
  - toc
---

# FAQs

**Question 1: How does the HwameiStor local storage scheduler work in the Kubernetes platform?**

HwameiStor's scheduler is deployed in the HwameiStor namespace in the form of Pods.



When the application (Deployment or StatefulSet) is created, the Pod of the application will be automatically deployed to the Worker node configured with HwameiStor local storage capability.

**Question 2: How does HwameiStor handle the scheduling of application multi-copy workloads? How is it different from traditional general-purpose shared storage?**

HwameiStor recommends using a stateful StatefulSet for multi-replica workloads.

The stateful application StatefulSet will deploy the replicated copy to the same Worker node, but will create a corresponding PV data volume for each Pod copy. If you need to deploy to different nodes to distribute workload, you need to manually configure it through pod affinity.



Since stateless application deployments cannot share block data volumes, it is recommended to use a single copy.

For traditional general-purpose shared storage:

The stateful application statefulSet will preferentially deploy replicated copies to other nodes to distribute workload, but will create a corresponding PV data volume for each Pod copy.
Only when the number of replicas exceeds the number of Worker nodes will there be multiple replicas on the same node.

Stateless application deployment will prioritize the deployment of replicated copies to other nodes to distribute workload, and all Pods share a PV data volume (currently only supports NFS).
Only when the number of replicas exceeds the number of Worker nodes will there be multiple replicas on the same node. For block storage, since data volumes cannot be shared, it is recommended to use a single copy.
