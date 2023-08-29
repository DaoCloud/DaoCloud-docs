---
hide:
  - toc
---

# Create Multicloud Instance

To use the fantastic features provided by Multicloud Management module, you must create a multicloud instance at the first step. Then, you can manage resources under this instance.

!!! note

    - DCE 5.0 Multicloud Management is developed based on the open source project [Karmada](https://karmada.io/), so a Karmada instance will be automatically created when you create a multicloud instance.

    - The newly-created multicloud instance is deployed in the global management cluster by default, in the form of a virtual cluster, which is transparent to users.
    
    - To distinguish from real clusters, all virtual clusters have a `k-` prefix in their names.

1. Click `Create Multicloud Instance` in the upper right corner.

    ![add](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/create-instance01.png)

2. Fill in information and click "OK".

    - Management Cluster: available clusters come from those integrated or crated in DCE 5.0 [Container Management](../../kpanda/intro/index.md) module. If no target cluster is found, go to Container Management module [integrate](../../kpanda/user-guide/clusters/integrate-cluster.md) or [create](../../kpanda/user-guide/clusters/create-cluster.md) a cluster.
    - Delete Instance: If checked，the Karmada instance will also be deleted when you delete the multicloud management instance. If not checked, the Karmada instance will remain and you can use it in terminal, but not in DCE 5.0 Multicloud Management anymore.

    ![add](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/kairship/images/create-instance02.png)
