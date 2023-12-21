---
hide:
  - toc
---

# Q&A

1. Can I specify my own Karmada version or get it upgraded? 

    Yes, you can upgrade the version by yourself.

2. How to convert single-cluster applications to multicloud applications?

    See [One-Click Conversion to Multicloud Workloads](../workload/promote.md).

3. Can I collect logs of applications deployed in different cluster?

    This is feature is still under development and will go public soon.

4. Can I check monitoring information of a multicloud workload in one picture?

    Yes. You can view it by clicking the name of the workload in the list of multicloud workloads.

5. Can workloads communicate across clusters?

    Yes. See [Multicloud Network Interconnection](../../mspider/user-guide/multicluster/cluster-interconnect.md)

6. Can Service realize cross-cluster service discovery?

    Yes. See [Multicloud Network Interconnection](../../mspider/user-guide/multicluster/cluster-interconnect.md)

7. Does Karmada have production level support?

    It is still in the TP stage, and the high availability issue of many internal components needs to be resolved (Karmada depends on etcd, etc.).

8. How to achieve failover?

    See [Failover Introduction](../failover/failover.md)

9. How about the permission system?

    It uses the existing [permission system of DCE 5.0](../../ghippo/user-guide/access-control/role.md), and bound Karmada instances with workspaces.

10. How to query multicluster events?

    Multicloud Management integrates resources at the product level. You can view all Karmada-instance-level events.

11. How can Container Management module get the information multicloud instances?

    Each Karmada instances has a corresponding virtual Kubernetes cluster in Container Management module, allowing it to collect info as quickly as possible.

12. How to customize registry URL of __karmada__ images?

    Add __--chat-repo-url__ in the startup commands of containers to specify the image source.

13. How to connect with karmada clusters?

    Click __Console__ in the upper right corner of the instance overview page.

14. Can I delete only the multicloud instance without deleting the corresponding karmada instance?

    Yes. You can set this configuration when creating the multicloud instance.

15. How can working clusters in a multicloud instance connect with each other?

    See [Multicloud Network Interconnection](../../mspider/user-guide/multicluster/cluster-interconnect.md)