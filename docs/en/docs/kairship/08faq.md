---
hide:
   - toc
---

# FAQs

1. What is the version of Karmada? Can you specify the version? Is it possible to upgrade?

    The current default version is v1.4.0, which supports users to upgrade independently.

2. How to seamlessly migrate single-cluster applications to multicloud orchestration?

    You can use our new feature [One-click promotion to multicloud workloads](./05workload/promote.md).

3. Does it support cross-cluster application log collection?

    Currently not supported, this feature will be added later.

4. Is it possible to display monitoring information in one view for workloads distributed to multiple clusters?

    It supports viewing multicloud applications in a unified view, and can monitor which clusters they are deployed to, corresponding services, propagation strategies, and so on.

5. Can workloads communicate across clusters?

    Karmada itself does not support it. The product can be supported by the open source community Submariner. In the future, multicloud orchestration will provide programmatic support.

6. Can Service realize cross-cluster service discovery?

    Karmada itself does not support it. The product can borrow external solution multi-dns to support it. In the future, multicloud orchestration will provide programmatic support.

7. Does Karmada have production level support?

    It is still in the TP stage, and the high availability of many internal components needs to be resolved (Karmada depends on etcd, etc.).

8. How to achieve failover?

    Karmada natively supports the failover function. When a member cluster fails, Karmada will perform intelligent rescheduling to complete the failover.

9. Multi-cluster permission issues

    Tightly combine the existing permission system of 5.0, open up with workspace, complete the binding of Karmada instance and workspaces, and solve the permission problem.

10. How to query multi-cluster events?

    Multicloud orchestration completes the integration at the product level, showing all Karmada instance-level events.

11. After creating a multicloud application through multicloud orchestration, how can I obtain relevant resource information through Container Management?

    Friends who know Karmada know that the essence of Karmada control-plane is a complete kubernetes control plane, but there are no nodes that carry workload. Therefore, when multicloud orchestration creates a multicloud orchestration instance, it adopts a tricky action, adding the instance itself as a hidden cluster to Container Management (not displayed in container management). In this way, the capabilities of Container Management can be fully utilized (collecting and accelerating the retrieval of resources of each K8s cluster, CRD, etc.), when querying the resources (Deployment, PropagationPolicy, OverridePolicy, etc.) of a multicloud orchestration instance in the interface, they can be directly retrieved through Container Management. Achieve read-write separation and speed up response time.
