---
hide:
  - toc
---

# Create mesh troubleshooting

This page will continue to count and sort out the error reports that may be caused by the environment or irregular operation during the process of creating the mesh, as well as the problem analysis and solutions for some error reports encountered during the use of the service mesh.
If you encounter problems with the use of the service mesh, please review this troubleshooting manual first.

- Hosted mesh: the control plane and the data plane are separated,
  and a virtual cluster is created to store managed Istio CRD resources

     When creating a hosted mesh, a managed control plane virtual cluster API Server will be created in the managed control plane cluster to store Istio CRD resources;
     In principle, only one hosted mesh is allowed in a DCE 5.0 environment.
     The global cluster of DCE 5.0 contains Istio-related components that global management depends on.
     It is not allowed to use this cluster to create a hosted mesh, and you can use an external mesh to create it during demo.

- Dedicated mesh: control plane and data plane are deployed in one cluster
- External mesh: the cluster to which it belongs must contain istio-related components

## Common failure cases

- [Cannot Find Cluster When Creating Mesh](./cannot-find-cluster.md)
- [Mesh Creation Stuck in "Creating" and Eventually Fails](./always-in-creating.md)
- [Unable to Delete Abnormal Mesh](./failed-to-delete.md)
- [Failed to Add Cluster to Hosted Mesh](./failed-to-add-cluster.md)
- [Istio-ingressgateway Issues When Adding Cluster to Hosted Mesh](./hosted-mesh-errors.md)
- [Unable to Unbind Mesh Space Properly](./mesh-space-cannot-unbind.md)
- [DCE 4.0 Integration Issue Tracking](./dce4.0-issues.md)
- [Namespace Sidecar Configuration Conflicts with Workload Sidecar](./sidecar.md)
- [MultiCloud Interconnect Issues in Hosted Mesh](./cluster-interconnect.md)
- [Sidecar Consuming Large Amount of Memory](./sidecar-memory-err.md)
- [Unknown Cluster Appears in Cluster List During Mesh Creation](./cluster-already-exist.md)
- [Handling Expired Certificates for Hosted Mesh APIServer](./hosted-apiserver-cert-expiration.md)
