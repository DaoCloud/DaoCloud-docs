# Synchronize Working Cluster Resources of a Hosted Mesh

A hosted mesh stores its Istio-related resources in an independent virtual cluster,
which avoids polluting the resources of the working cluster and ensures the independence and security of the resources.
However, this raises a problem: the related mesh resources (Istio CRDs) of the working cluster will also lose effect.

When users need to adopt some open-source mesh components, they often store Istio resources in the working cluster.
For this reason, DCE service mesh provides an optional advanced feature: **Working Cluster Resource Synchronization**

!!! note

    Users need to ensure the accuracy of the Istio resources in the working cluster themselves, as well as whether they conflict with the current hosted resources of the mesh.

    If the name of a working cluster resource conflicts with that of a hosted resource, the working resource will not be synchronized.

## Enable/Disable

In the mesh instance list, click **...** on the right of a hosted mesh, and select **Edit Basic Information** from the pop-up menu to enable/disable **Working Cluster Resource Synchronization**.

![on/off](../images/sync-mesh01.png)

## Resource List

On the details page of a hosted mesh, you can distinguish different resources by their origin:

![resources](../images/sync-mesh02.png)

## Automatically Remove Unmanaged Resources

!!! warning

    When you disable **Working Cluster Resource Synchronization** or **change the working cluster**, the resources synchronized from the cluster will be **automatically deleted**.

You can prevent them from being removed when the configuration changes by disabling the automatic deletion capability, or by manually changing the origin of some resources.

## Disable the Automatic Deletion Capability

To disable the automatic deletion capability, you can modify the custom resource **GlobalMesh** in the global service management cluster, find the corresponding mesh, and add the following parameter in the YAML:

```yaml
global.enabled_resources_synchronizer_auto_remove: "false"
```

![disable](../images/sync-mesh03.png)

## Manually Change the Resource Origin

If you want to change the resource origin, you can find the API Server instance of the virtual machine cluster in the control plane cluster of the hosted mesh:
`[meshName]-hosted-apiserver`, then enter the shell or console of the container and perform the following operations:

```bash
kubectl label vs [resourceName] -n [ns] mspider.io/origin-cluster- mspider.io/synced-from-
```

The example effect is as follows:

![example 1](../images/sync-mesh04.png)

![example 2](../images/sync-mesh04.png)
