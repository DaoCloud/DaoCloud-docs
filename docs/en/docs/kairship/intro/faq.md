---
hide:
  - toc
---

# common problem

1. What is the version of Karmada? Can you specify the version? Is it possible to upgrade?

    The current default version is v1.4.0, which supports users to upgrade independently.

2. How to seamlessly migrate single-cluster applications to multi-cloud orchestration?

    You can use our new feature [One-Click Promotion to Multi-Cloud Workloads](../workload/promote.md).

3. Does it support cross-cluster application log collection?

    Currently not supported, this feature will be added later.

4. Is it possible to display monitoring information in one view for workloads distributed to multiple clusters?

    It supports viewing multi-cloud applications in a unified view, and can monitor which clusters they are deployed to, corresponding services, propagation strategies, and so on.

5. Can workloads communicate across clusters?

    Karmada itself does not support it. The product can be supported by the open source community Submariner. In the future, multi-cloud orchestration will provide programmatic support.

6. Can Service realize cross-cluster service discovery?

    Karmada itself does not support it. The product can borrow external solution multi-dns to support it. In the future, multi-cloud orchestration will provide programmatic support.

7. Does Karmada have production level support?

    It is still in the TP stage, and the high availability of many internal components needs to be resolved (Karmada depends on etcd, etc.).

8. How to achieve failover?

    Karmada natively supports the failover function. When a member cluster fails, Karmada will perform intelligent rescheduling to complete the failover.

9. Multi-cluster permission issues

    Tightly combine the existing permission system of 5.0, open up with workspace, complete the binding of Karmada instance and workspaces, and solve the permission problem.

10. How to query multi-cluster events?

    Multi-cloud orchestration completes the integration at the product level, showing all Karmada instance-level events.

11. After creating a multi-cloud application through multi-cloud orchestration, how can I obtain relevant resource information through container management?

    Friends who know Karmada know that the essence of Karmada control-plane is a complete kubernetes control plane, but there are no nodes that carry workload. Therefore, when multi-cloud orchestration creates a multi-cloud orchestration instance, it adopts a tricky action, adding the instance itself as a hidden cluster to the container management (not displayed in the container management). In this way, the ability of container management can be fully used (collecting and accelerating the retrieval of resources of each K8s cluster, CRD, etc.), when querying the resources of a multi-cloud orchestration instance (Deployment, PropagationPolicy, OverridePolicy, etc.) in the interface, it can be directly through container management. Retrieval, separate reading and writing, and speed up response time.

12. How to customize `karmada` image source warehouse address?

    Kairship uses the open source `karmada-operator` for multi-instance LCM management; the Operator provides rich customization capabilities. Support customizing the warehouse address of the karmada resource image in the startup parameters.

    You can add the corresponding parameter configuration in the startup command, `--chat-repo-url`
    
    <!--screenshot-->

13. How to connect to karmada cluster?

    You can enter the `Console` in the upper right corner of the instance overview page to connect to the control plane of Karmada.

14. Is it possible to delete only the multicloud instance without deleting the components of karmada?

    Yes, when creating a multi-cloud instance, you can choose whether to check the instance release function. If checked, the corresponding Karmada instance will be deleted synchronously; if not deleted, it can continue to be used through the terminal, but the Karmada instance cannot be managed in Multi-Cloud Orchestration, it is recommended to delete it synchronously.

15. How do multiple working clusters in a multi-cloud instance realize network interworking?

    It is necessary to create a grid instance in the `service grid` and manage each working cluster. For details, please refer to [Multi-Cloud Network Interconnect](../../mspider/user-guide/multicluster/cluster-interconnect.md) .