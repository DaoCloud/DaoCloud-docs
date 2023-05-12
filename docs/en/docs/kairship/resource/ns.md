---
hide:
  - toc
---

# multi-cloud namespace

A multi-cloud namespace can manage workloads across clouds and across clusters. Currently, a wizard-based creation method is provided.

This article takes wizard creation as an example, and follows the steps below.

1. After entering a multi-cloud instance, in the left navigation bar, click `Resource Management` -> `Multi-cloud Namespace`, and click the `Create` button in the upper right corner.

    <!--screenshot-->

2. On the `Create Multi-Cloud Namespace` page, enter a name, add a tag, and click `OK`.

    <!--screenshot-->

3. Return to the list of multi-cloud namespaces, and the newly created one will be the first one by default. Click `⋮` on the right side of the list to edit the YAML and delete the namespace.

    <!--screenshot-->

    !!! note

        To delete a namespace, you need to remove all workloads under the namespace first. After the deletion, the workloads and services in the namespace will be affected, so please proceed with caution.