# Namespace Sidecar Management

You can enable, disable, or clean up the sidecar injection policy for namespaces in any cluster.

Note: If the sidecar injection setting for a workload is disabled, the workload will not have injection enabled even if its namespace has injection enabled.

## View Sidecar Injection Information

In the left navigation menu, click `Mesh Sidecar` -> `Namespace`, to view the sidecar status of all namespaces under the corresponding service mesh.

When there are many namespaces, you can sort them by name and search for them using the search function.

![View Sidecar Injection](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/ns-sidecar001.png)

## Enable Sidecar Injection

You can select one or more namespaces and enable sidecar injection using the following steps:

1. Select one or more namespaces that have not had sidecars injected and click `Enable injection`.

    ![Click Enable Injection](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/ns-sidecar02.png)

2. In the pop-up dialog, confirm the selected namespace(s) and click `OK`.

    ![Confirm](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/ns-sidecar03.png)

    Please follow the on-screen instructions to restart the corresponding Pods.

3. Return to the sidecar list of the namespace, and you can see that the `Injection Policy` status of the selected namespace has been changed to `Enabled`. After the user completes the restart of the workloads, the sidecar injection will be completed, and the relevant injection progress can be viewed in the `Sidecar Injections` column.

    ![Enabled](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/ns-sidecar03-01.png)

## Disable Sidecar Injection

You can select one or more namespaces and disable sidecar injection using the following steps:

1. Select one or more namespaces that have sidecar injection enabled and click `Disable injection`.

    ![Disable Injection](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/ns-sidecar04.png)

2. In the pop-up dialog, confirm the selected namespace(s) and click `OK`.

    ![Confirm](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/ns-sidecar05.png)

    Please follow the on-screen instructions to restart the corresponding Pods.

3. Return to the sidecar list of the namespace, and you can see that the `Injection Policy` status of the selected namespace has been changed to `Disabled`. After the user completes the restart of the workloads, the sidecar injection will be disabled, and the relevant uninstall progress can be viewed in the `Sidecar Injections` column.

## Cleanup Policy

You can select one or more namespaces and clean up the namespace-level sidecar policy. After cleanup, the sidecar status of workloads in the namespace will only be controlled by `Workload`. The following steps can be used:

1. Select one or more namespaces that have sidecar injection enabled and click `Cleanup Policy`.

    ![Cleanup Policy](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/ns-sidecar04.png)

2. In the pop-up dialog, confirm the selected namespace(s) and click `OK`.

    ![Confirm](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/ns-sidecar07.png)

3. Return to the sidecar list of the namespace, and you can see that the `Injection Policy` status of the selected namespace has been changed to `Not Set`. At this point, users can set sidecar injection policies for specific workloads using `Mesh Sidecar` -> `Workload`.

    ![Not Set](https://docs.daocloud.io/daocloud-docs-images/docs/en/docs/mspider/images/ns-sidecar07-01.png)

Next: [Workload Sidecar Management](./workload-sidecar.md)
