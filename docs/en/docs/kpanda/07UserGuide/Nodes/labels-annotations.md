---
hide:
  - toc
---

# Labels and annotations

Labels are identifying key-value pairs added to Kubernetes objects such as Pods, nodes, and clusters, which can be combined with label selectors to find and filter Kubernetes objects that meet certain conditions. Each key must be unique for a given object.

Annotations, like tags, are key/value pairs, but they do not have identification or filtering functions. Annotations can be used to add arbitrary metadata to nodes. Annotation keys usually use the format `prefix(optional)/name(required)`, for example `nfd.node.kubernetes.io/extended-resources`. If the prefix is ​​omitted, it means that the annotation key is private to the user.

For more information about labels and annotations, refer to the official Kubernetes documentation [labels and selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) Or [Annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).

The steps to add/delete tags and annotations are as follows:

1. On the `Cluster List` page, click the name of the target cluster.

    ![Enter the cluster list page](../../images/schedule01.png)

2. Click `Node Management` on the left navigation bar, click the `ⵗ` operation icon on the right side of the node, and click `Modify Label` or `Modify Comment`.

    ![Pause Scheduling](../../images/labels01.png)

3. Click `➕ Add` to add tags or annotations, click `X` to delete tags or annotations, and finally click `OK`.

    ![Node Management](../../images/labels02.png)