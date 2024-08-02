---
MTPE: windsonsea
Date: 2024-08-02
---

# Rollout Multicloud Applications with ArgoCD

This page explains how to integrate multicloud management with ArgoCD in the DCE 5.0 Workbench
to roll out multicloud applications.

## Prerequisites

- Fork the [manifest files](https://github.com/amamba-io/amamba-examples/tree/main/gueskbook-kairship) in advance,
  and have a basic understanding of Karmada's [PropagationPolicy](https://karmada.io/zh/docs/userguide/scheduling/resource-propagating) resources.
- Be able to access the ArgoCD UI normally.
- Be able to use the MultiCloud Management properly.

## Register Multicloud Instances to ArgoCD

1. Go to __MultiCloud Management__ and refer to [Add Instance](../../kairship/instance/add.md)
   to add a new multicloud instance. Create a multicloud instance named `k-amamba`:

    <!-- add image later -->

2. Refer to [Integrate Cluster](../../kairship/cluster.md#add-a-cluster) to add worker clusters to the
   multicloud instance. Connect the worker clusters named `zxw-dev`, `kpanda-global-cluster`, and `gwt-68`:

    <!-- add image later -->

3. In the __Overview__ section of the current multicloud instance, click __Get Certificate__ to obtain
   the `kubeconfig` of the current instance:

    <!-- add image later -->

4. Go to the environment where ArgoCD is located and register the multicloud instance to ArgoCD:

    ```shell
    argocd cluster add <CONTEXT_NAME> --kubeconfig <KUBECONFIG_NAME>
    ```

5. After successful addition, you can see the following cluster information in the ArgoCD UI:

    <!-- add image later -->

## Create Application

1. Refer to the [PropagationPolicy](https://github.com/amamba-io/amamba-examples/blob/main/gueskbook-kairship/propagationpolicy.yaml)
   manifest file and modify it according to the worker cluster information in the multicloud instance.

2. In the ArgoCD UI, click __+New APP__ :

    <!-- add image later -->

3. Fill in the required information:

    | Field | Example Value |
    | ------ | ----- |
    | name  | `karmamda-demo` |
    | project | `default` |
    | repository url | `https://github.com/amamba-io/amamba-examples.git` |
    | revision | `main` |
    | path  | `gueskbook-kairship` |
    | cluster url | `k-amamba`  |
    | namespace | `default` |

4. After creation, synchronize the application.

5. Go to __MultiCloud Management__ to check the application deployment status.
   Click __Multicloud Workload__ -> __Deployments__ to enter the `guestbook-ui` details page:

    <!-- add image later -->

6. You can see that the workload is deployed across 3 worker clusters:

    <!-- add image later -->
