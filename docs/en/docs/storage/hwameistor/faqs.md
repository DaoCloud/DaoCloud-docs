# FAQs

**Question 1: How does the HwameiStor local storage scheduler work in the Kubernetes platform?**

HwameiStor's scheduler is deployed in the HwameiStor namespace as Pods. When an application such as a Deployment or StatefulSet is created, the Pod of the application automatically deploys to the Worker node configured with HwameiStor local storage capability.

**Question 2: How does HwameiStor handle the scheduling of application multi-copy workloads? How is it different from traditional general-purpose shared storage?**

For multi-replica workloads, HwameiStor recommends using a stateful StatefulSet. The stateful application StatefulSet deploys the replicated copy to the same Worker node but creates a corresponding PV data volume for each Pod copy. If workload distribution is required across different nodes, it needs to be manually configured through pod affinity.

In contrast, for traditional general-purpose shared storage:

- Stateful application StatefulSet will preferentially deploy replicated copies to other nodes to distribute workload, but will create a corresponding PV data volume for each Pod copy.
- Only when the number of replicas exceeds the number of Worker nodes will there be multiple replicas on the same node.

- Stateless application deployment prioritizes the deployment of replicated copies to other nodes to distribute workload, and all Pods share a PV data volume (currently only supports NFS).
- Only when the number of replicas exceeds the number of Worker nodes will there be multiple replicas on the same node. For block storage, since data volumes cannot be shared, it is recommended to use a single copy.
