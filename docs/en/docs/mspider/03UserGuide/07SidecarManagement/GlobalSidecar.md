# Global sidecar management

Users can make uniform injection settings and sidecar resource limit settings for all clusters under the grid.

![Global Sidecar Management](../../images/globalSidecar.png)

## Global sidecar automatic injection

On the `Sidecar Management` -> `Global Sidecar Management` page, turn on the `Global Sidecar Automatic Injection` switch, this operation will enable the automatic sidecar injection function of all clusters under the grid, and the Pods under the newly connected cluster will also be Injection is performed automatically.

!!! note

The global injection function will enable the label `values.sidecarInjectorWebhook.enableNamespacesByDefault`, which will only take effect for Pod instances that have not been set for namespace and workload injection.

## Global sidecar resource limit

Select a cluster in the cluster list, click `Sidecar Resource Limit`, and set the requested resources and restricted resources for each Pod instance for the selected cluster in the pop-up window, where requested resources are resources that must be obtained, and restricted resources are available resources upper limit. Entering 0 means there is no limit for this item.

![Sidecar Resource Limit](../../images/globalSidecar-resourceLimit.png)

!!! note

The `Sidecar Resource Limit` set for a workload in `Workload Sidecar Management` takes precedence over the `Global Sidecar Resource Limit`.