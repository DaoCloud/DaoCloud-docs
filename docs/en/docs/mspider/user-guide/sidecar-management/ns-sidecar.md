# namespace sidecar management

Users can enable or disable features such as sidecar injection at the namespace level.

!!! note

    After a sidecar is selected, the buttons `Injection Disabled` and `Injection Enabled` will be displayed in the upper right corner.

## View sidecar injection information

In the left navigation bar, click `Sidecar Management` -> `Namespace Sidecar Management`, click a cluster (pictured as `centos-50`), you can view the sidecars of all namespaces under the cluster state.

When there are many namespaces, they can be sorted by the names of the namespaces and searched through the search function.



## Enable sidecar injection

Users can select one or more namespaces to enable automatic sidecar injection. The specific steps are as follows:

1. Select a namespace where sidecar injection is not enabled, and click the `Injection Enable` button;

    

2. In the pop-up dialog box, confirm whether the number of namespaces selected is correct, and click `OK` after confirmation.

    

3. Automatically return to the sidecar list of the namespace, and you can see that the status of `Sidecar Automatic Injection` in the namespace just selected has changed to `Enabled`. After the user completes the restart of the workload, the sidecar injection will be completed. For the injection progress, please refer to the sidecar injection amount column.

## Disable sidecar injection

Users can select one or more namespaces to disable the sidecar automatic injection function. The specific steps are as follows:

1. Select a namespace with sidecar injection enabled, and click the `Injection Disable` button;

    

2. In the pop-up dialog box, confirm whether the number of namespaces selected is correct, and click `OK` after confirmation.

    

3. Automatically return to the sidecar list of the namespace, and you can see that the status of `Sidecar Automatic Injection` in the namespace just selected has changed to `Disabled`. After the user completes the restart of the workload, the sidecar will be disabled. For related unloading progress, please refer to the sidecar injection column.