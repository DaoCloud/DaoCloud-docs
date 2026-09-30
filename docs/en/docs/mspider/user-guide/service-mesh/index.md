---
hide:
  - toc
---

# Mesh Types

DCE service mesh supports three kinds of meshes:

- [Hosted Mesh](./hosted-mesh.md) is fully hosted within the DCE service mesh. This mesh separates the core control plane components from the working cluster, and the control plane can be deployed in an independent cluster, enabling unified governance of multicluster services in the same mesh.
- [Dedicated Mesh](./dedicated-mesh.md) adopts the traditional structure of Istio, supports only one cluster, and has a dedicated control plane in the cluster.
- [External Mesh](./external-mesh.md) means that the existing mesh of the enterprise can be connected to the DCE service mesh for unified management. See [Create an External Mesh](external-mesh.md).

## FAQs

Some common problems when creating a mesh are summarized as follows:

- [Cannot find the cluster when creating a mesh](../../troubleshoot/cannot-find-cluster.md)
- [The mesh is always in "Creating" and eventually fails to be created](../../troubleshoot/always-in-creating.md)
- [The created mesh is abnormal, but the mesh cannot be deleted](../../troubleshoot/failed-to-delete.md)
- [Failed to add a cluster to the hosted mesh](../../troubleshoot/failed-to-add-cluster.md)
- [istio-ingressgateway is abnormal when adding a cluster to the hosted mesh](../../troubleshoot/hosted-mesh-errors.md)
- [Unable to unbind the mesh space properly](../../troubleshoot/mesh-space-cannot-unbind.md)
- [Multicloud interconnection of the hosted mesh is abnormal](../../troubleshoot/cluster-interconnect.md)
- [An unknown cluster exists in the cluster list when creating a mesh](../../troubleshoot/cluster-already-exist.md)
- [How to handle the expiration of the hosted mesh APIServer certificate](../../troubleshoot/hosted-apiserver-cert-expiration.md)
