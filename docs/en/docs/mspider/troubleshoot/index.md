# Create mesh troubleshooting

This page will continue to count and sort out the error reports that may be caused by the environment or irregular operation during the process of creating the mesh, as well as the problem analysis and solutions for some error reports encountered during the use of the service mesh.
If you encounter problems with the use of the service mesh, please review this troubleshooting manual first.

- Managed mode: the control plane and the data plane are separated, and a virtual cluster is created to store managed Istio CRD resources

     When creating a hosted mesh, a managed control plane virtual cluster API Server will be created in the managed control plane cluster to store Istio CRD resources;
     In principle, only one hosted mesh is allowed in a DCE 5.0 environment.
     The global cluster of DCE 5.0 contains Istio-related components that global management depends on.
     It is not allowed to use this cluster to create a hosted mode mesh, and you can use an external mesh to create it during demo.

- Proprietary mode: control plane and data plane are deployed in one cluster
- External mode: the cluster to which it belongs must contain istio-related components

## Common failure cases

- [Could not find cluster when creating mesh](./cannot-find-cluster.md)
- [Always in "creating" when creating a mesh, and eventually fails to create](./always-in-creating.md)
- [The mesh created is abnormal, but the mesh cannot be deleted](./failed-to-delete.md)
- [Failed to add cluster to hosted mesh](./failed-to-add-cluster.md)
- [The istio-ingressgateway is abnormal when hosting the mesh management cluster](./hosted-mesh-errors.md)
- [Unable to unbind mesh space](./mesh-space-cannot-unbind.md)
- [Troubleshooting on joining DCE 4.0](./dce4.0-issues.md)